#!/usr/bin/env python3
"""Count instructions a Cortex-A53 cannot execute in one Mach-O (e.g. the kernel).

  macho_isa_scan.py FILE

Uses the patterns of dsc_isa_scan.py on every S_ATTR_PURE_INSTRUCTIONS
section. Exits 1 if any LSE, LDAPR, RDMA, FP16 or DC CVAP instruction is
found, so CI fails on a kernel the A53 could not run.
"""
import os, struct, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsc_isa_scan import count, LC_SEGMENT_64, MH_MAGIC_64, S_ATTR_PURE_INSTRUCTIONS

BAD = ('lse', 'ldapr', 'rdma', 'fp16', 'dc_cvap')


def main():
    data = open(sys.argv[1], 'rb').read()
    magic, _cpu, _sub, _ft, ncmds, _size = struct.unpack_from('<IiiIII', data)
    assert magic == MH_MAGIC_64, 'not a 64-bit Mach-O'
    p, total = 32, None
    for _ in range(ncmds):
        cmd, size = struct.unpack_from('<II', data, p)
        if cmd == LC_SEGMENT_64:
            nsects, = struct.unpack_from('<I', data, p + 64)
            for s in range(nsects):
                q = p + 72 + 80 * s
                name = data[q:q + 16].rstrip(b'\0').decode() + ',' + data[q + 16:q + 32].rstrip(b'\0').decode()
                _addr, ssize, off = struct.unpack_from('<QQI', data, q + 32)
                flags, = struct.unpack_from('<I', data, q + 64)
                if flags & S_ATTR_PURE_INSTRUCTIONS and ssize >= 4 and off:
                    c = count(np.frombuffer(data, dtype='<u4', count=ssize // 4, offset=off))
                    print(name, {k: v for k, v in c.items() if v})
                    total = c if total is None else {k: total[k] + c[k] for k in total}
        p += size
    print('total', total)
    bad = {k: total[k] for k in BAD if total[k]}
    print('A53-incompatible:', bad or 'none')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
