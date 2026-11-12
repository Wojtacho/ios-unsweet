"""Pull the A510F persistent console log from TOMBSTONES through TWRP (read only).

  python mmclog_pull.py [OUT.txt]

The kernel (sweet_mmc.c, mmc_log_thread) keeps the newest console output in
the TOMBSTONES partition: a 4 KiB header "SWEETLOG" | u32 version | u32 ring
size | u64 total bytes | u64 seq, then the ring, byte n at offset n % size.
"""
import os, struct, subprocess, sys

ADB = r'W:\AdbPlatform\platform-tools\adb.exe'
os.environ['MSYS_NO_PATHCONV'] = '1'
out = sys.argv[1] if len(sys.argv) > 1 else 'mmclog.txt'

dev = subprocess.run([ADB, 'shell', 'readlink -f /dev/block/platform/*/by-name/TOMBSTONES'],
                     capture_output=True, text=True, check=True).stdout.strip()
if not dev.startswith('/dev/block/mmcblk0p'):
    sys.exit(f'TOMBSTONES not found ({dev!r})')
raw = subprocess.run([ADB, 'exec-out', f'cat {dev}'], capture_output=True, check=True).stdout
if raw[:8] != b'SWEETLOG':
    sys.exit(f'{dev}: no SWEETLOG header (first bytes {raw[:8]!r}): the kernel has not written a log yet')
version, size, total, seq = struct.unpack('<IIQQ', raw[8:32])
ring = raw[4096:4096 + size]
keep = min(total, size)
start = total - keep
data = bytes(ring[(start + i) % size] for i in range(keep))
with open(out, 'wb') as f:
    f.write(data)
print(f'{dev}: log v{version}, ring {size >> 10} KiB, {total} bytes written this boot, '
      f'flush #{seq}; newest {keep} bytes -> {out}')
