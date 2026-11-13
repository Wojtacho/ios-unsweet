"""Read byte ranges of one file on the iOS root through TWRP (read only): rangeread.py PATH OFF LEN OUT"""
import sys, importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h', os.path.join(here, 'hfsremote.py'))
h = importlib.util.module_from_spec(spec); sys_argv = sys.argv; sys.argv = ['x']; spec.loader.exec_module(h); sys.argv = sys_argv
fs = h.HFS(h.Source())
rec = fs.resolve(fs.lookup(sys.argv[1]))
i = fs.info(rec)
fork = fs.fork(rec[88:168]); fork = (fork[0], fs.extents_of(i['cnid'], fork))
off, n = int(sys.argv[2], 0), int(sys.argv[3], 0)
open(sys.argv[4], 'wb').write(fs.fork_read(fork, off, n))
print(f'{sys.argv[1]} [{off:#x}+{n:#x}] -> {sys.argv[4]} (file size {fork[0]:#x})')
