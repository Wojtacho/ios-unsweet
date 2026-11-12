"""Patch bytes of one file on the A510F iOS root in place (same length, data only).
Used for launchd.plist: fairplayd service names renamed (locationd / CoreLocation
migrator hang). Reads each 4K block first and writes only if it holds exactly the
expected old bytes; reads it back afterwards."""
import os, subprocess, sys
sys.argv = ['x']
import importlib.util
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'hfsremote.py'))
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
ADB = h.ADB
os.environ['MSYS_NO_PATHCONV'] = '1'

path = '/System/Library/xpc/launchd.plist'
old = open(os.path.join(here, 'pulled/mig/launchd.plist'), 'rb').read()
new = open(os.path.join(here, 'pulled/mig/launchd.plist.new'), 'rb').read()
assert len(old) == len(new)
diff = [i for i in range(len(old)) if old[i] != new[i]]
print('changed file offsets', [hex(i) for i in diff])

fs = h.HFS(h.Source())
rec = fs.resolve(fs.lookup(path))
i = fs.info(rec)
fork = fs.fork(rec[88:168]); fork = (fork[0], fs.extents_of(i['cnid'], fork))
assert fork[0] == len(old), (fork[0], len(old))


def phys(off):
    base = 0
    for start, cnt in fork[1]:
        size = cnt * fs.bs
        if off < base + size:
            return h.VOL_BASE_MIB * (1 << 20) + start * fs.bs + (off - base)
        base += size
    raise IOError('offset past extents')


def read_block(blk):
    return subprocess.run([ADB, 'exec-out', f'dd if=/dev/block/mmcblk0 bs=4096 skip={blk} count=1 2>/dev/null'],
                          capture_output=True, check=True).stdout


for blk in sorted({phys(d) // 4096 for d in diff}):
    d0 = next(d for d in diff if phys(d) // 4096 == blk)
    file_off = d0 - (phys(d0) % 4096)
    want_old = old[file_off:file_off + 4096]
    want_new = new[file_off:file_off + 4096]
    assert len(want_old) == 4096
    cur = read_block(blk)
    if cur == want_new:
        print('block', blk, 'already patched')
        continue
    if cur != want_old:
        sys.exit(f'block {blk} does not hold the expected launchd.plist bytes: nothing written')
    print('block', blk, 'matches launchd.plist at file offset', hex(file_off), '- writing')
    open(os.path.join(here, 'blk.bin'), 'wb').write(want_new)
    subprocess.run([ADB, 'push', os.path.join(here, 'blk.bin'), '/tmp/blk.bin'], check=True, capture_output=True)
    subprocess.run([ADB, 'shell', f'dd if=/tmp/blk.bin of=/dev/block/mmcblk0 bs=4096 seek={blk} count=1 conv=notrunc 2>/dev/null && sync'], check=True)
    back = read_block(blk)
    print('block', blk, 'read-back', 'OK' if back == want_new else 'MISMATCH')
