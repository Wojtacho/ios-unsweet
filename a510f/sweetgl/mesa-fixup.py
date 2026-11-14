#!/usr/bin/env python3
"""A510F sweetgl: changes to the Mesa tree (mesa-26.2.4) for panfrost on iOS.

usage: mesa-fixup.py MESA_DIR

Each change is a literal replacement that must match exactly once, so a
different Mesa version fails here instead of building something unexpected.
"""
import sys

M = sys.argv[1]


def edit(path, pairs):
    p = M + '/' + path
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        n = s.count(a)
        assert n == 1, '%s: %d matches for %r' % (path, n, a[:80])
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('mesa-fixup:', path)


# bo CPU mappings: the kernel already mapped every bo into the process
# (SweetMali selector 10); mmap of the DRM fd becomes a lookup, munmap a no-op
edit('src/panfrost/lib/kmod/pan_kmod.h', [
    ("""static inline void *
pan_kmod_bo_mmap(struct pan_kmod_bo *bo, int prot, int flags, void *host_addr)
{""",
     """#ifdef __APPLE__
void *sweet_drm_bo_map(int fd, uint64_t offset);
#endif

static inline void *
pan_kmod_bo_mmap(struct pan_kmod_bo *bo, int prot, int flags, void *host_addr)
{"""),
    ("""   host_addr =
      os_mmap(host_addr, bo->size, prot, flags, bo->dev->fd, mmap_offset);""",
     """#ifdef __APPLE__
   host_addr = sweet_drm_bo_map(bo->dev->fd, (uint64_t)mmap_offset);
#else
   host_addr =
      os_mmap(host_addr, bo->size, prot, flags, bo->dev->fd, mmap_offset);
#endif"""),
])

edit('src/gallium/drivers/panfrost/pan_bo.c', [
    ("""   if (os_munmap((void *)(uintptr_t)bo->ptr.cpu, panfrost_bo_size(bo))) {""",
     """#ifdef __APPLE__
   if (0) {     /* the kernel's mapping goes away with the bo */
#else
   if (os_munmap((void *)(uintptr_t)bo->ptr.cpu, panfrost_bo_size(bo))) {
#endif"""),
])

# imported IOSurfaces: the prime "fd" is a dup of /dev/null, its size comes
# from the emulation instead of lseek
edit('src/panfrost/lib/kmod/pan_kmod.c', [
    ("""      size_t size = lseek(fd, 0, SEEK_END);""",
     """#ifdef __APPLE__
      extern uint64_t sweet_drm_prime_size(int fd);
      size_t size = sweet_drm_prime_size(fd);
#else
      size_t size = lseek(fd, 0, SEEK_END);
#endif"""),
])

# tiler heap: SweetMali bos are wired memory; 128 MiB of a 1.7 GB phone is
# too much for the small scenes CoreAnimation draws
edit('src/gallium/drivers/panfrost/pan_device.c', [
    ("""         dev, 128 * 1024 * 1024, PAN_BO_INVISIBLE | PAN_BO_GROWABLE, "Tiler heap");""",
     """#ifdef __APPLE__
         dev, 32 * 1024 * 1024, PAN_BO_INVISIBLE | PAN_BO_GROWABLE, "Tiler heap");
#else
         dev, 128 * 1024 * 1024, PAN_BO_INVISIBLE | PAN_BO_GROWABLE, "Tiler heap");
#endif"""),
])
