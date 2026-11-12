#!/usr/bin/env python3
"""A510F changes to the iOS root, run after tools/sweet-root-tweaks.py.

  sudo a510f-root-tweaks.py MOUNTED_ROOT

Wallpapers and widgets (all four found by joranv1/ios-sailfish, which hit the
same PosterBoard crash: _stateLock_setupSwitcherConfigurationForFirstTime,
no wallpaper provider):

  feature flag    ExtensionKit enforce_xpc_cache_code_signing off. Extension
                  point definitions (System/Library/xpc/extensions.plist) are
                  checked through a detached .sig that needs trust caches this
                  kernel does not have; with the check on, installd rejects
                  every app extension (wallpapers, widgets, ...).
  migration       DataMigration runs once on the first boot (the
                  /private/var/datamigrator/migrate sentinel): it registers
                  the app extensions. sweet-root-tweaks.py skips it through
                  LastSystemVersion, which left LaunchServices with 1 of 524
                  extensions on sailfish; that is undone here.
  stock apps      the apps in /private/var/staged_system_apps listed in
                  a510f/apps.txt move into /Applications (with their widget
                  and poster extensions); the others are deleted. iOS would
                  install them on the first boot, which fails on code signing
                  here. No apps.txt: all of them.
  wallpapers      the stock wallpapers' HEIC layers get PNG twins and each
                  main.caml points at them: there is no hardware HEVC decoder.
                  Needs heif-convert (libheif-examples). The HEIC files stay.
"""
import glob, os, plistlib, shutil, subprocess, sys

MOBILE = 501
KEEP_FREE = 2 << 30          # PNG wallpapers never take the volume under 2 GiB free


def feature_flag(root):
    d = os.path.join(root, 'private/var/preferences/FeatureFlags/Domain')
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, 'ExtensionKit.plist')
    with open(path, 'wb') as f:
        plistlib.dump({'enforce_xpc_cache_code_signing': {'Enabled': False}}, f, fmt=plistlib.FMT_XML)
    os.chown(path, 0, 0)
    os.chmod(path, 0o644)
    print('feature flag ExtensionKit/enforce_xpc_cache_code_signing off')


def migration(root):
    path = os.path.join(root, 'private/var/mobile/Library/Preferences/com.apple.migration.plist')
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = plistlib.load(f)
        st = os.stat(path)
        for k in ('LastSystemVersion', 'DMUserDataDisposition'):
            data.pop(k, None)
        if data:
            with open(path, 'wb') as f:
                plistlib.dump(data, f, fmt=plistlib.FMT_BINARY)
            os.chown(path, st.st_uid, st.st_gid)
        else:
            os.remove(path)
        print('migration: LastSystemVersion removed')
    sentinel = os.path.join(root, 'private/var/datamigrator/migrate')
    os.makedirs(os.path.dirname(sentinel), exist_ok=True)
    open(sentinel, 'a').close()
    os.chown(sentinel, MOBILE, MOBILE)
    print('migration: runs once on the first boot (datamigrator/migrate)')


APPS_TXT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../apps.txt')


def chosen_apps():
    """Names from a510f/apps.txt ('Weather.app'; # comments); None: no file = all."""
    if not os.path.exists(APPS_TXT):
        return None
    names = set()
    for line in open(APPS_TXT, encoding='utf-8'):
        line = line.split('#', 1)[0].strip()
        if line:
            names.add(line if line.endswith('.app') else line + '.app')
    return names


def stock_apps(root):
    staged = os.path.join(root, 'private/var/staged_system_apps')
    want = chosen_apps()
    moved, removed = [], []
    for app in sorted(glob.glob(os.path.join(staged, '*.app'))):
        name = os.path.basename(app)
        if want is not None and name not in want:
            shutil.rmtree(app)                 # not chosen: not installed, space freed
            removed.append(name)
            continue
        dst = os.path.join(root, 'Applications', name)
        if os.path.exists(dst):
            print('kept existing', os.path.relpath(dst, root))
            continue
        os.rename(app, dst)                    # same volume: owners and modes stay
        moved.append(name)
    print(f'stock apps: {len(moved)} into /Applications: {" ".join(moved)}')
    print(f'stock apps: {len(removed)} left out: {" ".join(removed)}')
    if want is not None:
        missing = sorted(want - set(moved) - {os.path.basename(a) for a in glob.glob(os.path.join(root, 'Applications', '*.app'))})
        if missing:
            print('apps.txt names not found:', ' '.join(missing))


def wallpapers(root):
    base = os.path.join(root, 'Library/Wallpaper/Collections')
    if not os.path.isdir(base):
        print('no', os.path.relpath(base, root))
        return
    converted = 0
    failed = []
    low = False
    free0 = shutil.disk_usage(root).free
    for dirpath, _, files in list(os.walk(base)):
        for name in files:
            if not name.lower().endswith('.heic'):
                continue
            heic = os.path.join(dirpath, name)
            png = os.path.splitext(heic)[0] + '.png'
            if not os.path.exists(png) and shutil.disk_usage(root).free < KEEP_FREE:
                if not low:
                    print(f'wallpapers: stopped converting, under {KEEP_FREE >> 30} GiB free')
                low = True
                continue
            if not os.path.exists(png):
                r = subprocess.run(['heif-convert', heic, png], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, text=True)
                if r.returncode != 0 or not os.path.exists(png):
                    failed.append(os.path.relpath(heic, root))
                    print('heif-convert failed:', os.path.relpath(heic, root), r.stdout.strip()[-300:])
                    continue
                st = os.stat(heic)
                os.chown(png, st.st_uid, st.st_gid)
                os.chmod(png, st.st_mode & 0o7777)
            converted += 1
    edited = 0
    for dirpath, _, files in os.walk(base):
        if 'main.caml' not in files:
            continue
        caml = os.path.join(dirpath, 'main.caml')
        with open(caml, 'rb') as f:
            text = f.read()
        if b'.HEIC"' not in text and b'.heic"' not in text:
            continue
        new = text
        for name in os.listdir(os.path.join(dirpath, 'assets')) if os.path.isdir(os.path.join(dirpath, 'assets')) else []:
            stem, ext = os.path.splitext(name)
            if ext.lower() == '.heic' and os.path.exists(os.path.join(dirpath, 'assets', stem + '.png')):
                new = new.replace(name.encode() + b'"', stem.encode() + b'.png"')
        if new == text:
            continue
        with open(caml, 'wb') as f:
            f.write(new)
        edited += 1
    free1 = shutil.disk_usage(root).free
    print(f'wallpapers: {converted} HEIC layers as PNG, {len(failed)} failed, {edited} main.caml edited, '
          f'{(free0 - free1) >> 20} MiB used, {free1 >> 20} MiB free')


def main():
    if len(sys.argv) != 2 or not os.path.isdir(os.path.join(sys.argv[1], 'System/Library/xpc')):
        sys.exit(__doc__)
    root = sys.argv[1]
    feature_flag(root)
    migration(root)
    stock_apps(root)
    wallpapers(root)


if __name__ == '__main__':
    main()
