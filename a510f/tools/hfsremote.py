"""Read files from the A510F iOS root (HFS+/HFSX) straight off the phone.

The volume spans SYSTEM..USERDATA on mmcblk0, starting at LBA 507904
(248 MiB). Blocks are fetched on demand through TWRP's adb as root
(`dd if=/dev/block/mmcblk0`) in 1 MiB pieces and cached in memory and on
disk. Read-only: nothing is ever written to the phone.

  hfsremote.py ls PATH [PATH ...]        list a directory (type, size, name)
  hfsremote.py get PATH OUTFILE          copy one file to the PC
  hfsremote.py find PATH DEPTH [SUBSTR]  walk directories (optionally filter names)
  --image IMG                            read a local raw image instead of the phone

The HFS+ journal is not replayed: files written in the last seconds before
the phone was switched off may be missing or stale.
"""
import os, struct, subprocess, sys

ADB = r'W:\AdbPlatform\platform-tools\adb.exe'
VOL_BASE_MIB = 248          # LBA 507904 * 512
CH = 1 << 20
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hfscache')


class Source:
    def __init__(self, image=None):
        self.image = open(image, 'rb') if image else None
        self.mem = {}
        os.makedirs(CACHE_DIR, exist_ok=True)

    def chunk(self, i):
        if i in self.mem:
            return self.mem[i]
        if self.image:
            self.image.seek(i * CH)
            data = self.image.read(CH)
        else:
            path = os.path.join(CACHE_DIR, f'{i:06d}.bin')
            if os.path.exists(path) and os.path.getsize(path) == CH:
                data = open(path, 'rb').read()
            else:
                cmd = [ADB, 'exec-out', f'dd if=/dev/block/mmcblk0 bs=1048576 skip={VOL_BASE_MIB + i} count=1 2>/dev/null']
                data = subprocess.run(cmd, capture_output=True, check=True).stdout
                if len(data) != CH:
                    raise IOError(f'short read of MiB {i}: {len(data)} bytes')
                open(path, 'wb').write(data)
        self.mem[i] = data
        return data

    def read(self, off, n):
        out = bytearray()
        while n > 0:
            i, o = divmod(off, CH)
            take = min(n, CH - o)
            out += self.chunk(i)[o:o + take]
            off += take
            n -= take
        return bytes(out)


class HFS:
    def __init__(self, src):
        self.src = src
        vh = src.read(1024, 512)
        if vh[:2] not in (b'H+', b'HX'):
            raise ValueError(f'no HFS+ volume header (got {vh[:2]!r})')
        self.case_sensitive = vh[:2] == b'HX'
        self.bs = struct.unpack('>I', vh[40:44])[0]
        self.ext_fork = self.fork(vh[192:272])
        self.cat_fork = self.fork(vh[272:352])
        self.overflow = None
        self.ext_fork = (self.ext_fork[0], self.extents_of(3, self.ext_fork))
        self.cat_fork = (self.cat_fork[0], self.extents_of(4, self.cat_fork))
        hdr = self.fork_read(self.cat_fork, 0, 512)
        self.cat_root = struct.unpack('>I', hdr[16:20])[0]
        self.cat_nsize = struct.unpack('>H', hdr[32:34])[0]

    @staticmethod
    def fork(fd):
        size = struct.unpack('>Q', fd[0:8])[0]
        ext = [struct.unpack('>II', fd[16 + 8 * i:24 + 8 * i]) for i in range(8)]
        return size, [e for e in ext if e[1]]

    def fork_read(self, fork, off, n):
        out = bytearray()
        base = 0
        for start, cnt in fork[1]:
            size = cnt * self.bs
            if off < base + size and n > 0:
                o = off - base
                take = min(n, size - o)
                out += self.src.read(start * self.bs + o, take)
                off += take
                n -= take
            base += size
        if n:
            raise IOError('read past the extents of a fork')
        return bytes(out)

    # ---- extents overflow -------------------------------------------------
    def extents_of(self, file_id, fork, fork_type=0):
        """All extents of a fork: the 8 in the record + overflow records."""
        size, ext = fork
        if sum(c for _, c in ext) * self.bs >= size or file_id == 3:
            return ext
        if self.overflow is None:
            self.overflow = {}
            hdr = self.fork_read(self.ext_fork, 0, 512)
            nsize = struct.unpack('>H', hdr[32:34])[0]
            node = struct.unpack('>I', hdr[24:28])[0]   # first leaf
            while node:
                nd = self.fork_read(self.ext_fork, node * nsize, nsize)
                flink, _, kind, _, nrec = struct.unpack('>IIbBH', nd[:12])
                offs = [struct.unpack('>H', nd[nsize - 2 * (i + 1):nsize - 2 * i])[0] for i in range(nrec + 1)]
                for i in range(nrec):
                    r = nd[offs[i]:offs[i + 1]]
                    _, ft, _, fid, sblk = struct.unpack('>HBBII', r[:12])
                    recs = [struct.unpack('>II', r[12 + 8 * j:20 + 8 * j]) for j in range(8)]
                    self.overflow.setdefault((ft, fid), []).append((sblk, [x for x in recs if x[1]]))
                node = flink
        more = sorted(self.overflow.get((fork_type, file_id), []))
        return ext + [e for _, recs in more for e in recs]

    # ---- catalog B-tree -----------------------------------------------------
    def node(self, n):
        nd = self.fork_read(self.cat_fork, n * self.cat_nsize, self.cat_nsize)
        flink, _, kind, height, nrec = struct.unpack('>IIbBH', nd[:12])
        ns = self.cat_nsize
        offs = [struct.unpack('>H', nd[ns - 2 * (i + 1):ns - 2 * i])[0] for i in range(nrec + 1)]
        return flink, kind, [nd[offs[i]:offs[i + 1]] for i in range(nrec)]

    @staticmethod
    def key(r):
        klen = struct.unpack('>H', r[:2])[0]
        parent = struct.unpack('>I', r[2:6])[0]
        nlen = struct.unpack('>H', r[6:8])[0]
        units = struct.unpack(f'>{nlen}H', r[8:8 + 2 * nlen])
        return klen, parent, units

    def cmp_units(self, a, b):
        if not self.case_sensitive:
            a = tuple(u | 0x20 if 0x41 <= u <= 0x5a else u for u in a)
            b = tuple(u | 0x20 if 0x41 <= u <= 0x5a else u for u in b)
        return (a > b) - (a < b)

    def keycmp(self, k, parent, units):
        if k[1] != parent:
            return (k[1] > parent) - (k[1] < parent)
        return self.cmp_units(k[2], units)

    def first_leaf_ge(self, parent, units):
        """(node, index) of the first leaf record with key >= (parent, units)."""
        n = self.cat_root
        while True:
            flink, kind, recs = self.node(n)
            if kind == -1:
                for i, r in enumerate(recs):
                    if self.keycmp(self.key(r), parent, units) >= 0:
                        return n, i
                return flink, 0
            child = None
            for r in recs:
                k = self.key(r)
                if self.keycmp(k, parent, units) <= 0 or child is None:
                    child = struct.unpack('>I', r[2 + k[0]:6 + k[0]])[0]
                if self.keycmp(k, parent, units) > 0:
                    break
            n = child

    def records(self, parent, units=()):
        """Leaf records from (parent, units) on, as (key, data)."""
        n, i = self.first_leaf_ge(parent, units)
        while n:
            flink, kind, recs = self.node(n)
            for r in recs[i:]:
                k = self.key(r)
                d = r[2 + k[0]:]
                yield k, d
            n, i = flink, 0

    def children(self, cnid):
        out = []
        for k, d in self.records(cnid):
            if k[1] != cnid:
                break
            rtype = struct.unpack('>h', d[:2])[0]
            if rtype not in (1, 2):
                continue
            name = ''.join(map(chr, k[2]))
            out.append((name, d))
        return out

    @staticmethod
    def info(d):
        rtype = struct.unpack('>h', d[:2])[0]
        cnid = struct.unpack('>I', d[8:12])[0]
        if rtype == 1:
            return {'type': 'dir', 'cnid': cnid, 'size': 0}
        mode = struct.unpack('>H', d[42:44])[0]
        special = struct.unpack('>I', d[44:48])[0]
        ftype = d[48:52]
        size = struct.unpack('>Q', d[88:96])[0]
        kind = 'link' if (mode & 0o170000) == 0o120000 else 'file'
        return {'type': kind, 'cnid': cnid, 'size': size, 'hlnk': special if ftype == b'hlnk' else None,
                'data': d}

    def lookup(self, path):
        cnid, rec = 2, None
        for part in [p for p in path.split('/') if p]:
            units = tuple(map(ord, part))
            found = None
            for k, d in self.records(cnid, units):
                if k[1] == cnid and self.cmp_units(k[2], units) == 0:
                    found = d
                break
            if found is None:
                return None
            rec = found
            cnid = self.info(found)['cnid']
        return rec

    def resolve(self, rec):
        i = self.info(rec)
        if i.get('hlnk') is not None:
            priv = self.lookup('\0\0\0\0HFS+ Private Data')
            pcnid = self.info(priv)['cnid']
            name = tuple(map(ord, f'iNode{i["hlnk"]}'))
            for k, d in self.records(pcnid, name):
                if k[1] == pcnid and self.cmp_units(k[2], name) == 0:
                    return d
                break
            raise IOError(f'hard link target iNode{i["hlnk"]} missing')
        return rec

    def file_bytes(self, rec):
        rec = self.resolve(rec)
        i = self.info(rec)
        fork = self.fork(rec[88:168])
        fork = (fork[0], self.extents_of(i['cnid'], fork))
        return self.fork_read(fork, 0, fork[0])


def main():
    args = sys.argv[1:]
    image = None
    if args[:1] == ['--image']:
        image, args = args[1], args[2:]
    fs = HFS(Source(image))
    cmd = args[0]
    if cmd == 'ls':
        for path in args[1:]:
            rec = fs.lookup(path) if path.strip('/') else None
            cnid = fs.info(rec)['cnid'] if rec else 2
            print(f'== {path}')
            for name, d in sorted(fs.children(cnid)):
                i = fs.info(d)
                extra = f' -> iNode{i["hlnk"]}' if i.get('hlnk') is not None else ''
                print(f'  {i["type"]:4} {i["size"]:>12} {name}{extra}')
    elif cmd == 'get':
        rec = fs.lookup(args[1])
        if rec is None:
            sys.exit(f'not found: {args[1]}')
        data = fs.file_bytes(rec)
        open(args[2], 'wb').write(data)
        print(f'{args[1]}: {len(data)} bytes -> {args[2]}')
    elif cmd == 'find':
        root, depth = args[1], int(args[2])
        sub = args[3] if len(args) > 3 else None

        def walk(path, cnid, d):
            for name, rec in sorted(fs.children(cnid)):
                i = fs.info(rec)
                p = path.rstrip('/') + '/' + name
                if sub is None or sub in name:
                    print(f'{i["type"]:4} {i["size"]:>12} {p}')
                if i['type'] == 'dir' and d > 1:
                    walk(p, i['cnid'], d - 1)
        rec = fs.lookup(root) if root.strip('/') else None
        walk(root, fs.info(rec)['cnid'] if rec else 2, depth)


if __name__ == '__main__':
    main()
