#!/usr/bin/env python3
"""Count instructions a Cortex-A53 cannot execute in one Mach-O (e.g. the kernel).

  macho_isa_scan.py FILE

Uses the patterns of dsc_isa_scan.py on every S_ATTR_PURE_INSTRUCTIONS
section. Exits 1 if any LSE, LDAPR, RDMA, FP16 or DC CVAP instruction is
found, so CI fails on a kernel the A53 could not run.
"""
import bisect, os, struct, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsc_isa_scan import count, PATTERNS, LC_SEGMENT_64, MH_MAGIC_64, S_ATTR_PURE_INSTRUCTIONS

BAD = ('lse', 'ldapr', 'rdma', 'fp16', 'dc_cvap')
# Patterns of the incompatible features; LDAPR also matches lse_amo, so
# it is listed first and wins.
HIT_PATTERNS = [('ldapr', PATTERNS['ldapr'])] + [
    (k, PATTERNS[k]) for k in ('lse_cas', 'lse_casp', 'lse_amo', 'rdma', 'fp16', 'dc_cvap')]
LC_SYMTAB = 0x2


def symbols(data, symoff, nsyms, stroff):
    out = []
    for i in range(nsyms):
        strx, ntype, nsect, _desc, value = struct.unpack_from('<IBBHQ', data, symoff + 16 * i)
        if ntype & 0xE0 or not (ntype & 0x0E) == 0x0E or not value:	# defined in a section, no stabs
            continue
        name = data[stroff + strx:data.index(b'\0', stroff + strx)].decode(errors='replace')
        out.append((value, name))
    out.sort()
    return out


def main():
    data = open(sys.argv[1], 'rb').read()
    magic, _cpu, _sub, _ft, ncmds, _size = struct.unpack_from('<IiiIII', data)
    assert magic == MH_MAGIC_64, 'not a 64-bit Mach-O'
    p, total, sects, syms = 32, None, [], []
    for _ in range(ncmds):
        cmd, size = struct.unpack_from('<II', data, p)
        if cmd == LC_SEGMENT_64:
            nsects, = struct.unpack_from('<I', data, p + 64)
            for s in range(nsects):
                q = p + 72 + 80 * s
                name = data[q:q + 16].rstrip(b'\0').decode() + ',' + data[q + 16:q + 32].rstrip(b'\0').decode()
                addr, ssize, off = struct.unpack_from('<QQI', data, q + 32)
                flags, = struct.unpack_from('<I', data, q + 64)
                if flags & S_ATTR_PURE_INSTRUCTIONS and ssize >= 4 and off:
                    words = np.frombuffer(data, dtype='<u4', count=ssize // 4, offset=off)
                    c = count(words)
                    print(name, {k: v for k, v in c.items() if v})
                    total = c if total is None else {k: total[k] + c[k] for k in total}
                    sects.append((name, addr, words))
        elif cmd == LC_SYMTAB:
            symoff, nsyms, stroff, _strsize = struct.unpack_from('<IIII', data, p + 8)
            syms = symbols(data, symoff, nsyms, stroff)
        p += size
    print('total', total)
    # Where: each incompatible instruction with the function it sits in.
    addrs = [v for v, _ in syms]
    hits = 0
    for name, addr, words in sects:
        for feat, pats in HIT_PATTERNS:
            mask = np.zeros(words.size, dtype=bool)
            for m, v in pats:
                mask |= (words & np.uint32(m)) == np.uint32(v)
            for i in np.nonzero(mask)[0]:
                a = addr + 4 * int(i)
                j = bisect.bisect_right(addrs, a) - 1
                where = f'{syms[j][1]}+0x{a - syms[j][0]:x}' if j >= 0 else '?'
                hits += 1
                if hits <= 60:
                    print(f'  {feat:8} 0x{a:x} {int(words[i]):08x} {where}')
                if feat == 'ldapr':
                    words = words.copy()
                    words[i] = 0	# do not report it again as lse_amo
    print(f'{len(syms)} symbols; {hits} incompatible instruction(s) located')
    bad = {k: total[k] for k in BAD if total[k]}
    print('A53-incompatible:', bad or 'none')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
