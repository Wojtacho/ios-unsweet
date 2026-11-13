import sys, struct, importlib.util, os, json
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'hfsremote.py'))
h = importlib.util.module_from_spec(spec); a = sys.argv; sys.argv = ['x']; spec.loader.exec_module(h); sys.argv = a
fs = h.HFS(h.Source())
rec = fs.resolve(fs.lookup('/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64.42.dyldlinkedit'))
i = fs.info(rec); fork = fs.fork(rec[88:168]); fork = (fork[0], fs.extents_of(i['cnid'], fork))
hdr = fs.fork_read(fork, 0, 0x4000)
moff, mcnt = struct.unpack('<II', hdr[16:24])
maps = [struct.unpack('<QQQII', hdr[moff+32*k:moff+32*k+32]) for k in range(mcnt)]
print('l42 maps', [(hex(m[0]), hex(m[1]), hex(m[2])) for m in maps])
symoff, nsyms, stroff = int(a[1], 0), int(a[2], 0), int(a[3], 0)
le_va, le_fo = int(a[4], 0), int(a[5], 0)
def fo_of(file_off):           # linkedit "file offset" -> VA -> .42 file offset
    va = le_va + file_off - le_fo
    for addr, size, foff, _, _ in maps:
        if addr <= va < addr + size:
            return foff + va - addr
    raise IOError(hex(va))
nl = fs.fork_read(fork, fo_of(symoff), nsyms * 16)
out = {}
for k in range(nsyms):
    strx, ntype, sect, desc, val = struct.unpack('<IBBHQ', nl[16*k:16*k+16])
    s = fs.fork_read(fork, fo_of(stroff + strx), 128).split(b'\0')[0].decode(errors='replace')
    out[s] = val
json.dump(out, open(a[6], 'w'), indent=0)
print(len(out), 'symbols ->', a[6])
