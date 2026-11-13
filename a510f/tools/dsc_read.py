"""Minimal dyld shared cache reader (split cache, iOS 16): VA reads + Mach-O symbols."""
import struct, os
class DSC:
    def __init__(self, files):
        self.maps = []
        for f in files:
            d = open(f, 'rb').read()
            moff, mcnt = struct.unpack('<II', d[16:24])
            for i in range(mcnt):
                addr, size, foff, maxp, initp = struct.unpack('<QQQII', d[moff+32*i:moff+32*i+32])
                self.maps.append((addr, size, foff, d))
    def read(self, va, n):
        for addr, size, foff, d in self.maps:
            if addr <= va < addr + size:
                o = foff + (va - addr)
                return d[o:o+n]
        return None
    def macho(self, base):
        h = self.read(base, 32)
        ncmds, sizeofcmds = struct.unpack('<II', h[16:24])
        lc = self.read(base + 32, sizeofcmds)
        segs, symtab, off = {}, None, 0
        for _ in range(ncmds):
            cmd, sz = struct.unpack('<II', lc[off:off+8])
            if cmd == 0x19:
                name = lc[off+8:off+24].rstrip(b'\0').decode()
                vmaddr, vmsize, fileoff, filesize = struct.unpack('<4Q', lc[off+24:off+56])
                nsect = struct.unpack('<I', lc[off+64:off+68])[0]
                sects = {}
                for j in range(nsect):
                    so = off + 72 + 80 * j
                    sn = lc[so:so+16].rstrip(b'\0').decode()
                    sa, ss = struct.unpack('<QQ', lc[so+32:so+48])
                    sects[sn] = (sa, ss)
                segs[name] = (vmaddr, vmsize, fileoff, sects)
            elif cmd == 0x2:
                symtab = struct.unpack('<4I', lc[off+8:off+24])
            off += sz
        return segs, symtab
    def symbols(self, base):
        segs, (symoff, nsyms, stroff, strsize) = self.macho(base)
        le_va, _, le_fo, _ = segs['__LINKEDIT']
        syms = {}
        for i in range(nsyms):
            e = self.read(le_va + symoff - le_fo + 16 * i, 16)
            strx, ntype, sect, desc, val = struct.unpack('<IBBHQ', e)
            s = self.read(le_va + stroff - le_fo + strx, 160)
            if s and val:
                syms[s.split(b'\0')[0].decode(errors='replace')] = val
        return segs, syms
