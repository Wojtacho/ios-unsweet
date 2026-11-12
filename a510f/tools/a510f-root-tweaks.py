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
  stock apps      every app in /private/var/staged_system_apps moves into
                  /Applications (Weather, Calendar, Clock, Reminders, ... and
                  their widget/poster extensions). iOS installs them on the
                  first boot, which fails on code signing here.
  wallpapers      the stock wallpapers' HEIC layers get PNG twins and each
                  main.caml points at them: there is no hardware HEVC decoder.
                  Needs heif-convert (libheif-examples). The HEIC files stay.
"""
import glob, os, plistlib, shutil, subprocess, sys

MOBILE = 501


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


def stock_apps(root):
    staged = os.path.join(root, 'private/var/staged_system_apps')
    moved = 0
    for app in sorted(glob.glob(os.path.join(staged, '*.app'))):
        dst = os.path.join(root, 'Applications', os.path.basename(app))
        if os.path.exists(dst):
            print('kept existing', os.path.relpath(dst, root))
            continue
        os.rename(app, dst)                    # same volume: owners and modes stay
        moved += 1
    print(f'stock apps: {moved} moved from staged_system_apps to /Applications')


def wallpapers(root):
    base = os.path.join(root, 'Library/Wallpaper/Collections')
    if not os.path.isdir(base):
        print('no', os.path.relpath(base, root))
        return
    converted = 0
    for dirpath, _, files in os.walk(base):
        for name in files:
            if not name.lower().endswith('.heic'):
                continue
            heic = os.path.join(dirpath, name)
            png = os.path.splitext(heic)[0] + '.png'
            if not os.path.exists(png):
                subprocess.run(['heif-convert', heic, png], check=True, stdout=subprocess.DEVNULL)
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
        new = text.replace(b'.HEIC"', b'.png"').replace(b'.heic"', b'.png"')
        with open(caml, 'wb') as f:
            f.write(new)
        edited += 1
    print(f'wallpapers: {converted} HEIC layers as PNG, {edited} main.caml edited')


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
