#!/usr/bin/env python3
"""Extract the payload of an (unencrypted) IM4P, e.g. DeviceTree.d22ap.im4p.

  im4p_extract.py IN.im4p OUT

IM4P = DER SEQUENCE { IA5String "IM4P", IA5String type, IA5String version,
OCTET STRING payload, ... }. LZFSE payloads ("bvx2") are decompressed with
the pyliblzfse module (pip install pyliblzfse); LZSS "complzss" too.
"""
import struct, sys


def der(buf, off):
    """(tag, header length, content length) of the DER element at off."""
    tag = buf[off]
    ln = buf[off + 1]
    if ln < 0x80:
        return tag, 2, ln
    n = ln & 0x7f
    return tag, 2 + n, int.from_bytes(buf[off + 2:off + 2 + n], 'big')


def payload(im4p):
    tag, hl, cl = der(im4p, 0)
    assert tag == 0x30, 'not a DER SEQUENCE'
    off, end = hl, hl + cl
    items = []
    while off < end:
        t, h, c = der(im4p, off)
        items.append((t, im4p[off + h:off + h + c]))
        off += h + c
    assert items[0] == (0x16, b'IM4P'), items[0]
    data = items[3][1]
    assert items[3][0] == 0x04, 'payload is not an OCTET STRING'
    return items[1][1].decode(), data


def decompress(data):
    if data[:4] in (b'bvx2', b'bvx1', b'bvxn', b'bvx-'):
        import liblzfse
        return liblzfse.decompress(data)
    if data[:8] == b'complzss':
        size = struct.unpack('>I', data[12:16])[0]
        return lzss(data[0x180:], size)
    return data


def lzss(src, size):
    """Apple's LZSS (4096-byte window, threshold 2)."""
    N, F, T = 4096, 18, 2
    text = bytearray(b' ' * (N + F - 1))
    r = N - F
    out = bytearray()
    flags = 0
    i = 0
    while i < len(src) and len(out) < size:
        flags >>= 1
        if not flags & 0x100:
            flags = src[i] | 0xff00
            i += 1
            if i >= len(src):
                break
        if flags & 1:
            c = src[i]
            i += 1
            out.append(c)
            text[r] = c
            r = (r + 1) & (N - 1)
        else:
            if i + 1 >= len(src):
                break
            p = src[i] | ((src[i + 1] & 0xf0) << 4)
            ln = (src[i + 1] & 0x0f) + T
            i += 2
            for k in range(ln + 1):
                c = text[(p + k) & (N - 1)]
                out.append(c)
                text[r] = c
                r = (r + 1) & (N - 1)
    return bytes(out[:size])


if __name__ == '__main__':
    typ, data = payload(open(sys.argv[1], 'rb').read())
    raw = decompress(data)
    open(sys.argv[2], 'wb').write(raw)
    print(f'{sys.argv[1]}: type {typ}, {len(data)} -> {len(raw)} bytes')
