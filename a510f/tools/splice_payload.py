#!/usr/bin/env python3
"""Swap the ramdisk (SWEETXNU payload) of an A510F recovery/boot image.

  splice_payload.py OLD.img NEW_RAMDISK OUT.img
  splice_payload.py OLD.img --extract RAMDISK_OUT

Keeps the header, the shim (kernel section), second and the DTBH dt section
of OLD.img; replaces the ramdisk, fixes ramdisk_size and the SHA-1 id the way
mkbootimg computes it, and appends SEANDROIDENFORCE like build.sh. For days
when CI cannot install the cross toolchain: the payload comes from
tools/mkpayload.py, which is plain Python.
"""
import hashlib, struct, sys

TAIL = b'SEANDROIDENFORCE'
RECOVERY_MAX = 35651584


def split(d):
    assert d[:8] == b'ANDROID!', 'bad boot magic'
    ks, ka, rs, ra, ss, sa, ta, ps, dts = struct.unpack_from('<9I', d, 8)
    pg = lambda n: (n + ps - 1) // ps * ps
    off = ps
    kern = d[off:off + ks]; off += pg(ks)
    rd = d[off:off + rs]; off += pg(rs)
    sec = d[off:off + ss]; off += pg(ss)
    dt = d[off:off + dts]
    return ps, kern, rd, sec, dt


def build(hdr, ps, kern, rd, sec, dt):
    h = bytearray(hdr[:ps])
    struct.pack_into('<I', h, 16, len(rd))                  # ramdisk_size
    s = hashlib.sha1()
    for blob in (kern, rd, sec, dt):
        s.update(blob)
        s.update(struct.pack('<I', len(blob)))
    h[576:608] = s.digest().ljust(32, b'\0')                # id[8] at 0x240
    pad = lambda b: b + b'\0' * (-len(b) % ps)
    return bytes(h) + pad(kern) + pad(rd) + pad(sec) + pad(dt) + TAIL


def main():
    old = open(sys.argv[1], 'rb').read()
    ps, kern, rd, sec, dt = split(old)
    if sys.argv[2] == '--extract':
        open(sys.argv[3], 'wb').write(rd)
        print(f'ramdisk {len(rd)} bytes -> {sys.argv[3]}')
        return
    new_rd = open(sys.argv[2], 'rb').read()
    assert new_rd[:8] == b'SWEETXNU', 'not a SWEETXNU payload'
    out = build(old, ps, kern, new_rd, sec, dt)
    assert dt[:4] == b'DTBH', 'no DTBH dt section'
    assert len(out) <= RECOVERY_MAX, f'{len(out)} B does not fit the partition'
    open(sys.argv[3], 'wb').write(out)
    print(f'{sys.argv[3]}: shim {len(kern)} B, payload {len(new_rd)} B, dt {len(dt)} B, total {len(out)} B')


if __name__ == '__main__':
    main()
