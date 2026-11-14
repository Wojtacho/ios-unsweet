/*
 * A510F sweetgl: libdrm + panfrost DRM emulation for Mesa on iOS.
 *
 * Mesa's panfrost driver (src/panfrost/lib/kmod/panfrost_kmod.c,
 * src/gallium/drivers/panfrost) reaches the kernel only through the libdrm
 * calls in include/xf86drm.h and one mmap (pan_kmod.h os_mmap, redirected by
 * mesa-fixup.py to sweet_drm_bo_map). This file answers them in user space
 * on top of the SweetMali user client (xnu patch 0122):
 *
 *   CREATE_BO            sel 10 [size, flags] -> [handle, gpu va, user va, size]
 *   GEM_CLOSE            sel 11 [handle]
 *   (IOSurface import)   sel 12 [surface id] -> as sel 10
 *   SUBMIT               sel 13 [jc, requirements] -> [status, us]; synchronous
 *   GET_PARAM            sel 15 [param] -> [value] (panfrost param numbering)
 *   log line             sel 16 (struct input)
 *
 *   MMAP_BO              offset = handle << 32; sweet_drm_bo_map() turns it
 *                        back into the kernel's write-combined user mapping
 *   GET_BO_OFFSET        the bo's GPU VA
 *   WAIT_BO, syncobjs    nothing to wait for: every submit has finished when
 *                        the call returns
 *
 * One device per process; the "fd" is /dev/null. Imported IOSurfaces become
 * prime fds (dups of /dev/null) that drmPrimeFDToHandle maps back.
 */
#include <errno.h>
#include <fcntl.h>
#include <pthread.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <IOKit/IOKitLib.h>

#include "xf86drm.h"
#include "drm-uapi/panfrost_drm.h"
#include "sweet_drm.h"

#define SEL_BO_NEW      10
#define SEL_BO_FREE     11
#define SEL_IMPORT      12
#define SEL_SUBMIT      13
#define SEL_PARAM       15
#define SEL_LOG         16

struct sbo {
	uint64_t gpu, map, size;
};

struct prime {
	int fd;
	uint32_t handle;
};

static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
static io_connect_t conn;
static int dev_fd = -1;
static struct sbo *bos;
static uint32_t nbos;
static struct prime primes[64];
static uint32_t next_syncobj = 1;
static uint32_t submits, failed_submits;

void
sweet_drm_log(const char *fmt, ...)
{
	char line[240];
	va_list ap;
	va_start(ap, fmt);
	int n = vsnprintf(line, sizeof(line), fmt, ap);
	va_end(ap);
	if (n < 0) {
		return;
	}
	if (n >= (int)sizeof(line)) {
		n = sizeof(line) - 1;
	}
	io_connect_t c = conn;
	if (c) {
		(void)IOConnectCallStructMethod(c, SEL_LOG, line, (size_t)n + 1, NULL, NULL);
	}
}

/* Lock held. The GPU service comes up during boot: callers may retry. */
static void
connect_dev(void)
{
	io_service_t svc = IOServiceGetMatchingService(kIOMainPortDefault, IOServiceMatching("SweetMali"));
	if (svc == 0) {
		return;
	}
	kern_return_t kr = IOServiceOpen(svc, mach_task_self(), 0, &conn);
	IOObjectRelease(svc);
	if (kr != KERN_SUCCESS) {
		conn = 0;
		return;
	}
	uint64_t in = DRM_PANFROST_PARAM_GPU_PROD_ID, out = 0;
	uint32_t n = 1;
	if (IOConnectCallScalarMethod(conn, SEL_PARAM, &in, 1, &out, &n) != KERN_SUCCESS) {
		IOServiceClose(conn);
		conn = 0;
		return;
	}
	dev_fd = open("/dev/null", O_RDWR | O_CLOEXEC);
	sweet_drm_log("sweetgl: SweetMali open, GPU product 0x%llx", (unsigned long long)out);
}

int
sweet_drm_open(void)
{
	pthread_mutex_lock(&lock);
	if (!conn) {
		connect_dev();
	}
	int fd = conn && dev_fd >= 0 ? dup(dev_fd) : -1;
	pthread_mutex_unlock(&lock);
	return fd;
}

/* Lock held: the bo for a handle, or NULL. */
static struct sbo *
sbo(uint32_t handle)
{
	return handle >= 1 && handle <= nbos && bos[handle - 1].size ? &bos[handle - 1] : NULL;
}

/* Lock held. */
static int
sbo_add(uint32_t handle, uint64_t gpu, uint64_t map, uint64_t size)
{
	if (handle == 0) {
		return -EINVAL;
	}
	if (handle > nbos) {
		uint32_t n = nbos ? nbos : 256;
		while (n < handle) {
			n *= 2;
		}
		struct sbo *b = realloc(bos, n * sizeof(*b));
		if (b == NULL) {
			return -ENOMEM;
		}
		memset(b + nbos, 0, (n - nbos) * sizeof(*b));
		bos = b;
		nbos = n;
	}
	bos[handle - 1] = (struct sbo){ .gpu = gpu, .map = map, .size = size };
	return 0;
}

/* Lock held. Reply of sel 10 / 12 -> recorded bo. */
static int
bo_reply(kern_return_t kr, const uint64_t out[4], uint32_t *handle)
{
	if (kr != KERN_SUCCESS) {
		return kr == kIOReturnNoMemory ? -ENOMEM : -EINVAL;
	}
	int err = sbo_add((uint32_t)out[0], out[1], out[2], out[3]);
	if (err == 0) {
		*handle = (uint32_t)out[0];
	}
	return err;
}

static int
create_bo(struct drm_panfrost_create_bo *r)
{
	uint64_t in[2] = {r->size, r->flags}, out[4] = {0};
	uint32_t n = 4;
	pthread_mutex_lock(&lock);
	kern_return_t kr = IOConnectCallScalarMethod(conn, SEL_BO_NEW, in, 2, out, &n);
	int err = bo_reply(kr, out, &r->handle);
	if (err == 0) {
		r->offset = out[1];
	}
	pthread_mutex_unlock(&lock);
	if (err) {
		sweet_drm_log("sweetgl: CREATE_BO %u bytes flags 0x%x failed: 0x%x", r->size, r->flags, kr);
	}
	return err;
}

static int
close_bo(uint32_t handle)
{
	pthread_mutex_lock(&lock);
	struct sbo *b = sbo(handle);
	int err = -EINVAL;
	if (b != NULL) {
		uint64_t in = handle;
		IOConnectCallScalarMethod(conn, SEL_BO_FREE, &in, 1, NULL, NULL);
		memset(b, 0, sizeof(*b));
		err = 0;
	}
	pthread_mutex_unlock(&lock);
	return err;
}

static int
get_param(struct drm_panfrost_get_param *p)
{
	if (p->param <= DRM_PANFROST_PARAM_NR_CORE_GROUPS) {
		uint64_t in = p->param, out = 0;
		uint32_t n = 1;
		if (IOConnectCallScalarMethod(conn, SEL_PARAM, &in, 1, &out, &n) != KERN_SUCCESS) {
			return -EINVAL;
		}
		p->value = out;
		return 0;
	}
	switch (p->param) {
	case DRM_PANFROST_PARAM_THREAD_TLS_ALLOC:       /* 0: Mesa uses max threads per core */
	case DRM_PANFROST_PARAM_AFBC_FEATURES:          /* Midgard: no AFBC feature register */
		p->value = 0;
		return 0;
	default:
		return -EINVAL;
	}
}

static int
submit(struct drm_panfrost_submit *s)
{
	uint64_t in[2] = {s->jc, s->requirements}, out[2] = {0};
	uint32_t n = 2;
	kern_return_t kr = IOConnectCallScalarMethod(conn, SEL_SUBMIT, in, 2, out, &n);
	pthread_mutex_lock(&lock);
	uint32_t nr = ++submits, nf = failed_submits += kr != KERN_SUCCESS;
	pthread_mutex_unlock(&lock);
	if (kr != KERN_SUCCESS && nf <= 20) {
		sweet_drm_log("sweetgl: submit %u (jc 0x%llx req 0x%x, %u bos) failed: 0x%x status 0x%llx",
		    nr, (unsigned long long)s->jc, s->requirements, s->bo_handle_count, kr,
		    (unsigned long long)out[0]);
	}
	if (nr == 1 || nr == 10 || nr == 100 || nr == 1000 || nr % 10000 == 0) {
		sweet_drm_log("sweetgl: %u submits, %u failed; last req 0x%x took %llu us", nr, nf,
		    s->requirements, (unsigned long long)out[1]);
	}
	/* a failed job has been stopped and the GPU reset: let Mesa carry on */
	return 0;
}

static int
command(unsigned nr, void *data)
{
	switch (nr) {
	case DRM_PANFROST_SUBMIT:
		return submit(data);
	case DRM_PANFROST_WAIT_BO:
		return 0;
	case DRM_PANFROST_CREATE_BO:
		return create_bo(data);
	case DRM_PANFROST_MMAP_BO: {
		struct drm_panfrost_mmap_bo *m = data;
		pthread_mutex_lock(&lock);
		int ok = sbo(m->handle) != NULL;
		pthread_mutex_unlock(&lock);
		m->offset = (uint64_t)m->handle << 32;
		return ok ? 0 : -EINVAL;
	}
	case DRM_PANFROST_GET_PARAM:
		return get_param(data);
	case DRM_PANFROST_GET_BO_OFFSET: {
		struct drm_panfrost_get_bo_offset *g = data;
		pthread_mutex_lock(&lock);
		struct sbo *b = sbo(g->handle);
		g->offset = b ? b->gpu : 0;
		pthread_mutex_unlock(&lock);
		return b ? 0 : -EINVAL;
	}
	case DRM_PANFROST_MADVISE: {
		struct drm_panfrost_madvise *m = data;
		m->retained = 1;                        /* never purged */
		return 0;
	}
	case DRM_PANFROST_SET_LABEL_BO:
	case DRM_PANFROST_SYNC_BO:                      /* write-combined maps: nothing to flush */
	case DRM_PANFROST_JM_CTX_DESTROY:
		return 0;
	case DRM_PANFROST_JM_CTX_CREATE: {
		struct drm_panfrost_jm_ctx_create *c = data;
		c->handle = 1;
		return 0;
	}
	case DRM_PANFROST_QUERY_BO_INFO: {
		struct drm_panfrost_query_bo_info *q = data;
		q->extra_flags = 0;
		return 0;
	}
	default:
		return -ENOSYS;
	}
}

int
drmIoctl(int fd, unsigned long request, void *arg)
{
	(void)fd;
	if (!conn) {
		errno = ENODEV;
		return -1;
	}
	unsigned nr = (unsigned)(request & 0xff);       /* _IOC number (drm.h has no DRM_IOCTL_NR here) */
	int err;
	if (nr >= DRM_COMMAND_BASE && nr < DRM_COMMAND_END) {
		err = command(nr - DRM_COMMAND_BASE, arg);
	} else if (request == DRM_IOCTL_GEM_CLOSE) {
		err = close_bo(((struct drm_gem_close *)arg)->handle);
	} else {
		err = -ENOSYS;
	}
	if (err) {
		errno = -err;
		return -1;
	}
	return 0;
}

int
drmCommandWrite(int fd, unsigned long index, void *data, unsigned long size)
{
	(void)fd;
	(void)size;
	int err = conn ? command((unsigned)index, data) : -ENODEV;
	return err;
}

int
drmCommandWriteRead(int fd, unsigned long index, void *data, unsigned long size)
{
	return drmCommandWrite(fd, index, data, size);
}

void *
sweet_drm_bo_map(int fd, uint64_t offset)
{
	(void)fd;
	pthread_mutex_lock(&lock);
	struct sbo *b = sbo((uint32_t)(offset >> 32));
	void *p = b && b->map ? (void *)(uintptr_t)b->map : MAP_FAILED;
	pthread_mutex_unlock(&lock);
	return p;
}

int
sweet_drm_import_iosurface(uint32_t surface_id, uint64_t map, uint32_t *handle, uint64_t *size)
{
	(void)map;
	if (!conn) {
		return -ENODEV;
	}
	uint64_t in = surface_id, out[4] = {0};
	uint32_t n = 4;
	pthread_mutex_lock(&lock);
	kern_return_t kr = IOConnectCallScalarMethod(conn, SEL_IMPORT, &in, 1, out, &n);
	int err = bo_reply(kr, out, handle);
	pthread_mutex_unlock(&lock);
	if (err == 0) {
		*size = out[3];
	}
	return err;
}

int
sweet_drm_handle_to_fd(uint32_t handle)
{
	int fd = -1;
	pthread_mutex_lock(&lock);
	for (unsigned i = 0; i < sizeof(primes) / sizeof(primes[0]); i++) {
		if (primes[i].fd == 0) {
			fd = dup(dev_fd);
			if (fd >= 0) {
				primes[i] = (struct prime){ .fd = fd, .handle = handle };
			}
			break;
		}
	}
	pthread_mutex_unlock(&lock);
	return fd;
}

void
sweet_drm_close_fd(int fd)
{
	pthread_mutex_lock(&lock);
	for (unsigned i = 0; i < sizeof(primes) / sizeof(primes[0]); i++) {
		if (primes[i].fd == fd && fd > 0) {
			primes[i] = (struct prime){0};
			close(fd);
			break;
		}
	}
	pthread_mutex_unlock(&lock);
}

/* Lock held. */
static struct prime *
prime(int fd)
{
	for (unsigned i = 0; i < sizeof(primes) / sizeof(primes[0]); i++) {
		if (primes[i].fd == fd && fd > 0) {
			return &primes[i];
		}
	}
	return NULL;
}

uint64_t
sweet_drm_prime_size(int fd)
{
	pthread_mutex_lock(&lock);
	struct prime *p = prime(fd);
	struct sbo *b = p ? sbo(p->handle) : NULL;
	uint64_t size = b ? b->size : 0;
	pthread_mutex_unlock(&lock);
	return size;
}

int
drmPrimeFDToHandle(int fd, int prime_fd, uint32_t *handle)
{
	(void)fd;
	pthread_mutex_lock(&lock);
	struct prime *p = prime(prime_fd);
	if (p != NULL) {
		*handle = p->handle;
	}
	pthread_mutex_unlock(&lock);
	return p ? 0 : -EINVAL;
}

int
drmPrimeHandleToFD(int fd, uint32_t handle, uint32_t flags, int *prime_fd)
{
	(void)fd;
	(void)flags;
	*prime_fd = sweet_drm_handle_to_fd(handle);
	return *prime_fd >= 0 ? 0 : -EMFILE;
}

int
drmCloseBufferHandle(int fd, uint32_t handle)
{
	(void)fd;
	return close_bo(handle);
}

static drmVersion version = {
	/* 1.1: HEAP/NOEXEC bo flags, nothing newer (no timestamp or coherency queries) */
	.version_major = 1, .version_minor = 1,
	.name_len = 8, .name = "panfrost",
	.date_len = 8, .date = "20261114",
	.desc_len = 9, .desc = "SweetMali",
};

drmVersionPtr
drmGetVersion(int fd)
{
	(void)fd;
	return conn ? &version : NULL;
}

void
drmFreeVersion(drmVersionPtr v)
{
	(void)v;
}

int
drmGetCap(int fd, uint64_t capability, uint64_t *value)
{
	(void)fd;
	(void)capability;
	*value = 0;
	return -EINVAL;
}

/* Every submit has completed by the time it returns: syncobjs are always signalled. */
int
drmSyncobjCreate(int fd, uint32_t flags, uint32_t *handle)
{
	(void)fd;
	(void)flags;
	pthread_mutex_lock(&lock);
	*handle = next_syncobj++;
	pthread_mutex_unlock(&lock);
	return 0;
}

int drmSyncobjDestroy(int fd, uint32_t h) { (void)fd; (void)h; return 0; }
int drmSyncobjHandleToFD(int fd, uint32_t h, int *o) { (void)fd; (void)h; *o = -1; return -ENOSYS; }
int drmSyncobjFDToHandle(int fd, int o, uint32_t *h) { (void)fd; (void)o; (void)h; return -ENOSYS; }
int drmSyncobjImportSyncFile(int fd, uint32_t h, int s) { (void)fd; (void)h; (void)s; return 0; }
/*
 * Panfrost snapshots every flush's out-fence as a sync file (pan_fence.c);
 * failing here logged "export failed" thousands of times and gave CA no
 * fences. Everything has completed already: any fd stands for a signalled
 * fence (ImportSyncFile ignores it).
 */
int
drmSyncobjExportSyncFile(int fd, uint32_t h, int *s)
{
	(void)fd;
	(void)h;
	*s = dev_fd >= 0 ? dup(dev_fd) : -1;
	return *s >= 0 ? 0 : -EMFILE;
}
int drmSyncobjReset(int fd, const uint32_t *h, uint32_t n) { (void)fd; (void)h; (void)n; return 0; }
int drmSyncobjSignal(int fd, const uint32_t *h, uint32_t n) { (void)fd; (void)h; (void)n; return 0; }

int drmSyncobjTimelineSignal(int fd, const uint32_t *h, uint64_t *p, uint32_t n) { (void)fd; (void)h; (void)p; (void)n; return 0; }
int drmSyncobjTransfer(int fd, uint32_t d, uint64_t dp, uint32_t s, uint64_t sp, uint32_t f)
{ (void)fd; (void)d; (void)dp; (void)s; (void)sp; (void)f; return 0; }

int
drmSyncobjQuery2(int fd, uint32_t *h, uint64_t *p, uint32_t n, uint32_t f)
{
	(void)fd;
	(void)h;
	(void)f;
	for (uint32_t i = 0; i < n && p; i++) {
		p[i] = UINT64_MAX;                      /* every point signalled */
	}
	return 0;
}

int drmSyncobjQuery(int fd, uint32_t *h, uint64_t *p, uint32_t n) { return drmSyncobjQuery2(fd, h, p, n, 0); }

int
drmSyncobjWait(int fd, uint32_t *h, unsigned n, int64_t t, unsigned f, uint32_t *s)
{
	(void)fd;
	(void)h;
	(void)n;
	(void)t;
	(void)f;
	if (s) {
		*s = 0;
	}
	return 0;
}

int
drmSyncobjTimelineWait(int fd, uint32_t *h, uint64_t *p, unsigned n, int64_t t, unsigned f, uint32_t *s)
{
	(void)p;
	return drmSyncobjWait(fd, h, n, t, f, s);
}
