#!/usr/bin/env python3
"""Count instructions a Cortex-A53 (ARMv8.0) cannot execute in a dyld shared cache.

  dsc_isa_scan.py CACHE_DIR OUT.json

CACHE_DIR holds dyld_shared_cache_arm64 and its subcaches (.01, .02, ...).
Only sections marked S_ATTR_PURE_INSTRUCTIONS (__text, __stubs, ...) are
scanned, so every 32-bit word is an instruction and the fixed-mask matches
below are exact decodes, not heuristics.

Features counted (all absent on Cortex-A53, present or not on Apple A11):
  lse_cas   CAS/CASA/CASL/CASAL (+B/H)         ARMv8.1 LSE
  lse_casp  CASP family                         ARMv8.1 LSE
  lse_amo   LDADD/LDCLR/LDEOR/LDSET/LD[SU]MAX/MIN, SWP, ST* aliases  ARMv8.1 LSE
  ldapr     LDAPR (RCpc)                        ARMv8.3 (A11 lacks it: sanity check)
  rdma      SQRDMLAH/SQRDMLSH                   ARMv8.1
  fp16      half-precision arithmetic (scalar and vector)  ARMv8.2
  dc_cvap   DC CVAP                             ARMv8.2
For scale it also counts all instructions and LL/SC exclusives (LDXR/STXR...),
the ARMv8.0 way to do atomics.
"""
import json, mmap, os, struct, sys
import numpy as np

S_ATTR_PURE_INSTRUCTIONS = 0x80000000
LC_SEGMENT_64 = 0x19
MH_MAGIC_64 = 0xFEEDFACF

# name: list of (mask, value); a word matches if any pair matches.
PATTERNS = {
    'lse_cas':  [(0x3FA07C00, 0x08A07C00)],
    'lse_casp': [(0xBFA07C00, 0x08207C00)],
    'lse_amo':  [(0x3F200C00, 0x38200000)],
    'ldapr':    [(0x3FFFFC00, 0x38BFC000)],
    'rdma':     [(0xBF20F400, 0x2E008400), (0xFF20F400, 0x7E008400),
                 (0xBF00D400, 0x2F00D000), (0xFF00D400, 0x7F00D000)],
    # Scalar 1-source with ftype=11 is left out: it includes FCVT from half,
    # which ARMv8.0 has.
    'fp16':     [(0xFFE00C00, 0x1EE00800),	# scalar 2-source (FADD H...)
                 (0xFFC00000, 0x1FC00000),	# scalar 3-source (FMADD H...)
                 (0x9F60C400, 0x0E400400),	# vector three-same FP16
                 (0x9F7E0C00, 0x0E780800)],	# vector two-reg-misc FP16
    'dc_cvap':  [(0xFFFFFFE0, 0xD50B7C20)],
    'llsc':     [(0x3F800000, 0x08000000)],	# LDXR/STXR/LDAXR/STLXR (+pairs)
}
LSE = ('lse_cas', 'lse_casp', 'lse_amo')


class Cache:
    def __init__(self, d):
        self.maps = []		# (addr, size, mm, fileoff)
        self.files = {}
        names = sorted(n for n in os.listdir(d)
                       if n.startswith('dyld_shared_cache_arm64')
                       and not n.endswith(('.symbols', '.map', '.atlas')))
        if 'dyld_shared_cache_arm64' not in names:
            sys.exit(f'no dyld_shared_cache_arm64 in {d}: {names}')
        for n in names:
            f = open(os.path.join(d, n), 'rb')
            mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            self.files[n] = mm
            assert mm[:7] == b'dyld_v1', n
            moff, mcnt = struct.unpack_from('<II', mm, 0x10)
            for i in range(mcnt):
                addr, size, fo, _maxp, _initp = struct.unpack_from('<QQQII', mm, moff + 32 * i)
                self.maps.append((addr, size, mm, fo))
        self.main = self.files['dyld_shared_cache_arm64']
        print(f'{len(names)} cache files, {len(self.maps)} mappings', flush=True)

    def read(self, addr, n):
        for a, s, mm, fo in self.maps:
            if a <= addr and addr + n <= a + s:
                o = fo + (addr - a)
                return mm[o:o + n]
        return None

    def images(self):
        mm = self.main
        moff, = struct.unpack_from('<I', mm, 0x10)
        off_old, cnt_old = struct.unpack_from('<II', mm, 0x18)
        if cnt_old == 0 and moff >= 0x1C8:
            off, cnt = struct.unpack_from('<II', mm, 0x1C0)
        else:
            off, cnt = off_old, cnt_old
        for i in range(cnt):
            addr, _mt, _ino, poff = struct.unpack_from('<QQQI', mm, off + 32 * i)
            path = mm[poff:mm.find(b'\0', poff)].decode(errors='replace')
            yield addr, path


def code_sections(cache, addr):
    hdr = cache.read(addr, 32)
    if hdr is None:
        return
    magic, _cpu, _sub, _ft, ncmds, sizeofcmds = struct.unpack_from('<IiiIII', hdr)
    if magic != MH_MAGIC_64:
        return
    cmds = cache.read(addr + 32, sizeofcmds)
    if cmds is None:
        return
    p = 0
    for _ in range(ncmds):
        cmd, size = struct.unpack_from('<II', cmds, p)
        if cmd == LC_SEGMENT_64:
            nsects, = struct.unpack_from('<I', cmds, p + 64)
            for s in range(nsects):
                q = p + 72 + 80 * s
                sect = cmds[q:q + 16].rstrip(b'\0').decode()
                saddr, ssize = struct.unpack_from('<QQ', cmds, q + 32)
                flags, = struct.unpack_from('<I', cmds, q + 64)
                if flags & S_ATTR_PURE_INSTRUCTIONS and ssize >= 4:
                    yield sect, saddr, ssize
        p += size


def count(words):
    out = {'insns': int(words.size)}
    for name, pats in PATTERNS.items():
        hit = np.zeros(words.size, dtype=bool)
        for m, v in pats:
            hit |= (words & np.uint32(m)) == np.uint32(v)
        out[name] = int(hit.sum())
    # LDAPR sits inside the atomic-memory-op encoding space: keep them apart.
    out['lse_amo'] -= out['ldapr']
    # CASP shares the exclusive-pair encoding space the llsc mask covers.
    out['llsc'] -= out['lse_casp']
    out['lse'] = sum(out[k] for k in LSE)
    return out


def main():
    cache = Cache(sys.argv[1])
    total, per = None, []
    for i, (addr, path) in enumerate(cache.images()):
        acc = None
        for _sect, saddr, ssize in code_sections(cache, addr):
            raw = cache.read(saddr, ssize & ~3)
            if raw is None:
                continue
            c = count(np.frombuffer(raw, dtype='<u4'))
            acc = c if acc is None else {k: acc[k] + c[k] for k in acc}
        if acc is None:
            continue
        per.append({'path': path, **acc})
        total = dict(acc) if total is None else {k: total[k] + acc[k] for k in total}
        if i % 200 == 0:
            print(f'{i} images scanned', flush=True)
    keys = ['insns', 'lse', 'lse_cas', 'lse_casp', 'lse_amo', 'ldapr', 'rdma', 'fp16', 'dc_cvap', 'llsc']
    with_lse = [p for p in per if p['lse']]
    result = {
        'images': len(per),
        'images_with_lse': len(with_lse),
        'total': {k: total[k] for k in keys},
        'top_lse': sorted(with_lse, key=lambda p: -p['lse'])[:60],
        'core_libs': [p for p in per if any(s in p['path'] for s in (
            '/libobjc.A.dylib', '/libdispatch.dylib', '/libsystem_platform.dylib',
            '/libsystem_pthread.dylib', '/libsystem_malloc.dylib', '/libc++.1.dylib',
            '/libsystem_kernel.dylib', '/libdyld.dylib', '/CoreFoundation',
            '/Foundation', '/libswiftCore.dylib', '/UIKitCore', '/JavaScriptCore'))],
        'top_fp16': sorted((p for p in per if p['fp16']), key=lambda p: -p['fp16'])[:20],
        'top_rdma': sorted((p for p in per if p['rdma']), key=lambda p: -p['rdma'])[:20],
    }
    json.dump(result, open(sys.argv[2], 'w'), indent=1)
    print(json.dumps({k: result[k] for k in ('images', 'images_with_lse', 'total')}, indent=1))


if __name__ == '__main__':
    main()
