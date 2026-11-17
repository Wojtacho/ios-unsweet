import sys
cpp, h = sys.argv[1], sys.argv[2]


def edit(path, pairs):
    s = open(path, encoding='utf-8').read()
    for a, b in pairs:
        c = s.count(a)
        assert c == 1, (path, c, a[:70])
        s = s.replace(a, b)
    assert '\x00' not in s
    open(path, 'w', encoding='utf-8', newline='\n').write(s)
    print('edited', path)


edit(h, [
    ("""	bool                      wrapped;      /* memory is a prepared range of a task (IOSurfaceWrapClient*) */
""", """	bool                      wrapped;      /* memory is a prepared range of a task (IOSurfaceWrapClient*) */
	/*
	 * A510F: a full-screen surface made by backboardd (CoreAnimation's
	 * display surfaces): written only by the GPU, read by the panel copy.
	 * Never mapped write-combined: on arm a write-combined mapping of the
	 * pages turns every other mapping of them uncached too, the kernel's
	 * included (panel copy ~350 ms per frame).
	 */
	bool                      display;
"""),
    ("""	bool init() APPLE_KEXT_OVERRIDE { values = NULL; purgeable = 0; wrapDelta = 0; wrapped = false; return OSObject::init(); }""",
     """	bool init() APPLE_KEXT_OVERRIDE { values = NULL; purgeable = 0; wrapDelta = 0; wrapped = false; display = false; return OSObject::init(); }"""),
])

edit(cpp, [
    ("""		kernelMap = memory->map(wrapped ? kIOMapDefaultCache : kIOMapWriteCombineCache);""",
     """		kernelMap = memory->map((wrapped || display) ? kIOMapDefaultCache : kIOMapWriteCombineCache);"""),
    ("""			bzero(mem->getBytesNoCopy(), s->allocSize);
			s->memory = mem;
			s->mapCache = kIOMapDefaultCache;
			if (!sweet_surface_publish(s)) {
				ret = kIOReturnNoResources;
			}
		}
	}
	char name[32];
	proc_selfname(name, sizeof(name));""",
     """			bzero(mem->getBytesNoCopy(), s->allocSize);
			s->memory = mem;
			s->mapCache = kIOMapDefaultCache;
			/* A510F: CoreAnimation's full-screen surfaces stay cacheable (SweetSurface.h) */
			char creator[32];
			proc_selfname(creator, sizeof(creator));
			if (strcmp(creator, "backboardd") == 0 && s->bytesPerElement == 4 && s->planeCount <= 1 &&
			    (uint64_t)s->width * s->height >= 1080ull * 1920ull) {
				s->display = true;
				/* the zeros must reach RAM before the GPU draws: no dirty lines left behind */
				uintptr_t p = (uintptr_t)mem->getBytesNoCopy();
				for (uintptr_t a = p & ~(uintptr_t)63; a < p + s->allocSize; a += 64) {
					__asm__ volatile ("dc civac, %0" : : "r"(a) : "memory");
				}
				__asm__ volatile ("dsb sy" : : : "memory");
			}
			if (!sweet_surface_publish(s)) {
				ret = kIOReturnNoResources;
			}
		}
	}
	char name[32];
	proc_selfname(name, sizeof(name));"""),
    ("""		IOLog("SWEET SURF: %s create id %u %ux%u fmt 0x%x bpe %u bpr %u planes %u size %u keys %u -> 0x%x\\n",
		    name, s->id, s->width, s->height, s->pixelFormat, s->bytesPerElement,
		    s->bytesPerRow, s->planeCount, s->allocSize, props->getCount(), ret);""",
     """		IOLog("SWEET SURF: %s create id %u %ux%u fmt 0x%x bpe %u bpr %u planes %u size %u keys %u -> 0x%x%s\\n",
		    name, s->id, s->width, s->height, s->pixelFormat, s->bytesPerElement,
		    s->bytesPerRow, s->planeCount, s->allocSize, props->getCount(), ret,
		    s->display ? " (display, cached)" : "");"""),
])

# --- memory accounting for the log (SweetFramebuffer prints it every 10 s)
edit(cpp, [
    ("""static uint64_t      sweet_surface_wired;       /* bytes of buffer surfaces */
""", """static uint64_t      sweet_surface_wired;       /* bytes of buffer surfaces */
static SInt32        sweet_surface_live;        /* buffer surfaces alive (A510F) */
extern "C" void sweet_surface_stats(uint64_t *bytes, uint32_t *count);
extern "C" void
sweet_surface_stats(uint64_t *bytes, uint32_t *count)
{
	*bytes = sweet_surface_wired;
	*count = (uint32_t)sweet_surface_live;
}
"""),
    ("""		OSAddAtomic64(-(SInt64)allocSize, (volatile SInt64 *)&sweet_surface_wired);
""", """		OSAddAtomic64(-(SInt64)allocSize, (volatile SInt64 *)&sweet_surface_wired);
		OSDecrementAtomic(&sweet_surface_live);
"""),
    ("""			bzero(mem->getBytesNoCopy(), s->allocSize);
			s->memory = mem;""", """			bzero(mem->getBytesNoCopy(), s->allocSize);
			OSIncrementAtomic(&sweet_surface_live);
			s->memory = mem;"""),
])

# A510F GPU job queue (SweetMali): a CPU lock of a surface waits for the GPU
# jobs queued so far, as IOSurfaceLock does on iOS (no reads of a half-drawn
# surface, no writes under a job still sampling it).
edit(cpp, [
    ("""IOReturn
IOSurfaceRootUserClient::trapLock(void *id, __unused void *options, void *seedOut,
    void *, void *, void *)
{
""", """extern "C" uint64_t sweet_mali_seq(void);       /* SweetMali.cpp */
extern "C" void sweet_mali_wait_seq(uint64_t seq);

IOReturn
IOSurfaceRootUserClient::trapLock(void *id, __unused void *options, void *seedOut,
    void *, void *, void *)
{
	sweet_mali_wait_seq(sweet_mali_seq());
"""),
])

# A510F round 45: AppleJPEGDriver stand-in. SpringBoard saves app snapshots
# as JPEG through the hardware encoder (it makes a 420f surface and a 'JPEG'
# surface per snapshot); with no AppleJPEGDriver they are never written, so
# cards of apps not opened since the boot are blank. This version logs every
# call (selector, struct sizes, the struct as hex, the surfaces it names) and
# answers the start calls with kIOReturnUnsupported: the call layout for a
# software encoder (and maybe a software fallback in AppleJPEG).
edit(cpp, [
    ("""void sweet_scaler_publish(IOService *provider);

void
sweet_scaler_publish(IOService *provider)
{""", """static void
sweet_jpeg_surf(const char *what, uint32_t id)
{
	SweetSurface *s = id ? sweet_surface_copy(id) : NULL;
	if (s != NULL) {
		IOLog("SWEET JPEG:   %s surface %u %ux%u fmt 0x%x bpr %u planes %u size %u\\n", what, id, s->width, s->height,
		    s->pixelFormat, s->bytesPerRow, s->planeCount, s->allocSize);
		OSSafeReleaseNULL(s);
	}
}

class AppleJPEGUserClient : public IOUserClient {
	OSDeclareDefaultStructors(AppleJPEGUserClient);

public:
	IOReturn externalMethod(uint32_t selector, IOExternalMethodArguments *args,
	    IOExternalMethodDispatch *dispatch, OSObject *target, void *reference) APPLE_KEXT_OVERRIDE;
	IOReturn clientClose(void) APPLE_KEXT_OVERRIDE;
};

OSDefineMetaClassAndStructors(AppleJPEGUserClient, IOUserClient);

IOReturn
AppleJPEGUserClient::clientClose(void)
{
	terminate();
	return kIOReturnSuccess;
}

IOReturn
AppleJPEGUserClient::externalMethod(uint32_t selector, IOExternalMethodArguments *args,
    IOExternalMethodDispatch *, OSObject *, void *)
{
	static uint32_t told;
	IOReturn ret = (selector == 1 || selector == 3) ? kIOReturnUnsupported : kIOReturnSuccess;
	if (told++ < 40) {
		char name[32];
		proc_selfname(name, sizeof(name));
		IOLog("SWEET JPEG: %s selector %u scalars in %u out %u struct in %u out %u -> 0x%x\\n", name, selector,
		    args->scalarInputCount, args->scalarOutputCount, args->structureInputSize, args->structureOutputSize, ret);
		uint32_t len = 0;
		uint8_t *req = sweet_struct_in(args, &len);
		if (req != NULL) {
			for (uint32_t o = 0; o < len && o < 0x80; o += 32) {
				uint32_t w[8] = {0, 0, 0, 0, 0, 0, 0, 0};
				memcpy(w, req + o, MIN(32u, len - o));
				IOLog("SWEET JPEG:   +0x%02x %08x %08x %08x %08x %08x %08x %08x %08x\\n", o,
				    w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[7]);
			}
			if (len >= 12) {
				uint32_t a, b, c;
				memcpy(&a, req, 4);
				memcpy(&b, req + 4, 4);
				memcpy(&c, req + 8, 4);
				sweet_jpeg_surf("+0x0", a);
				sweet_jpeg_surf("+0x4", b);
				sweet_jpeg_surf("+0x8", c);
			}
			IOFreeData(req, len);
		}
	}
	if (args->scalarOutput != NULL) {
		for (uint32_t i = 0; i < args->scalarOutputCount; i++) {
			args->scalarOutput[i] = 0;
		}
	}
	return ret;
}

class AppleJPEGDriver : public IOService {
	OSDeclareDefaultStructors(AppleJPEGDriver);

public:
	IOReturn newUserClient(task_t owningTask, void *securityID, UInt32 type, IOUserClient **handler) APPLE_KEXT_OVERRIDE;
};

OSDefineMetaClassAndStructors(AppleJPEGDriver, IOService);

IOReturn
AppleJPEGDriver::newUserClient(task_t owningTask, void *securityID, UInt32 type, IOUserClient **handler)
{
	AppleJPEGUserClient *uc = OSTypeAlloc(AppleJPEGUserClient);
	if (uc == NULL) {
		return kIOReturnNoMemory;
	}
	if (!uc->initWithTask(owningTask, securityID, type) || !uc->attach(this)) {
		uc->release();
		return kIOReturnError;
	}
	if (!uc->start(this)) {
		uc->detach(this);
		uc->release();
		return kIOReturnError;
	}
	char name[32];
	proc_selfname(name, sizeof(name));
	IOLog("SWEET JPEG: %s opened AppleJPEGDriver type %u\\n", name, (unsigned)type);
	*handler = uc;
	return kIOReturnSuccess;
}

void sweet_scaler_publish(IOService *provider);

void
sweet_scaler_publish(IOService *provider)
{
	{
		AppleJPEGDriver *jd = OSTypeAlloc(AppleJPEGDriver);
		if (jd != NULL && jd->init() && jd->attach(provider)) {
			jd->registerService();
			IOLog("SWEET JPEG: stand-in AppleJPEGDriver published (logs calls, no codec yet)\\n");
		}
		OSSafeReleaseNULL(jd);
	}"""),
])

# A510F round 51: the pre-blurred wallpaper picture (folder icon background,
# open folder panel, app switcher background) comes from CollectionsPoster as
# 420f (YUV) surfaces, which CoreAnimation never draws through sweetgl (no
# multi-plane binds ever logged): an empty picture. Wallpaper processes are
# refused 420f/420v surfaces, so they fall back to RGB ones (or fail visibly
# in the log). Boot-arg sweetyuv=1: allow again.
edit(cpp, [
    ("""	s->pixelFormat = sweet_dict_u32(props, "IOSurfacePixelFormat", 0);
	s->cacheMode = sweet_dict_u32(props, "IOSurfaceCacheMode", 0);""", """	s->pixelFormat = sweet_dict_u32(props, "IOSurfacePixelFormat", 0);
	if (s->pixelFormat == 0x34323066u || s->pixelFormat == 0x34323076u) {    /* '420f', '420v' */
		static int allow = -1;
		if (allow < 0) {
			int v = 0;
			(void)PE_parse_boot_argn("sweetyuv", &v, sizeof(v));
			allow = v;
		}
		char who[32];
		proc_selfname(who, sizeof(who));
		bool poster = false;
		for (const char *c = who; *c && !poster; c++) {
			poster = strncmp(c, "Poster", 6) == 0;
		}
		if (allow == 0 && poster && false) {     /* round 51: did not help (CollectionsPoster was killed, no RGB fallback): off */
			static unsigned told;
			if (told++ < 20) {
				IOLog("SWEET SURF: %s: 420f/420v refused (wallpaper picture: RGB instead)\\n", who);
			}
			return kIOReturnUnsupported;
		}
	}
	s->cacheMode = sweet_dict_u32(props, "IOSurfaceCacheMode", 0);"""),
])

# A510F round 60: a CPU lock waits for the GPU only when the GPU can touch the
# surface (imported into SweetMali by some process). CPU-only surfaces (text,
# icons drawn by apps before upload, IOSurface-backed CPU buffers) lock at
# once. Every 10 s: lock count, how many waited and the time spent waiting.
edit(h, [
    ("""	bool                      display;
""", """	bool                      display;
	volatile uint32_t         gpuImported;  /* SweetMali IMPORT made a GPU mapping of it (round 60) */
"""),
    ("""wrapped = false; display = false; return OSObject::init(); }""",
     """wrapped = false; display = false; gpuImported = 0; return OSObject::init(); }"""),
])
edit(cpp, [
    ("""	sweet_mali_wait_seq(sweet_mali_seq());
""", """	SweetSurface *ls = sweet_surface_held(fLock, fRefs, (uint32_t)(uintptr_t)id);
	if (ls != NULL) {
		static uint64_t n_lock, n_wait, t_wait, t_last;
		uint64_t t0 = mach_absolute_time();
		n_lock++;
		if (ls->gpuImported) {
			uint64_t q = sweet_mali_seq();
			if (q != 0) {
				sweet_mali_wait_seq(q);
				n_wait++;
				t_wait += mach_absolute_time() - t0;
			}
		}
		if (t_last == 0) {
			t_last = t0;
		}
		uint64_t ns = 0;
		absolutetime_to_nanoseconds(t0 - t_last, &ns);
		if (ns >= 10000000000ull) {
			uint64_t w = 0;
			absolutetime_to_nanoseconds(t_wait, &w);
			IOLog("SWEET SURF: locks (10 s): %llu, %llu waited for the GPU, %llu ms waiting\\n",
			    n_lock, n_wait, w / 1000000);
			n_lock = n_wait = t_wait = 0;
			t_last = t0;
		}
		ls->release();
	}
"""),
])
edit(cpp, [
    ("""extern "C" void sweet_mali_wait_seq(uint64_t seq);

IOReturn
IOSurfaceRootUserClient::trapLock(""", """extern "C" void sweet_mali_wait_seq(uint64_t seq);
extern "C" uint64_t mach_absolute_time(void);
extern "C" void absolutetime_to_nanoseconds(uint64_t abstime, uint64_t *result);

IOReturn
IOSurfaceRootUserClient::trapLock("""),
])

# A510F round 61: SpringBoard scales CoreAnimation snapshots (app switcher
# cards 1242x2208 -> 621x1104, the wallpaper material chain 1242x2208 ->
# 311x552 -> 104x184 behind folders and the switcher) right after asking
# backboardd to render them. The GPU may still be drawing the source: the
# scaler copied a surface that was still empty (black switcher background and
# cards, no folder materials). Wait for the queued GPU work first, and log a
# sample of the source (64 pixels: how many are not 0) to see it.
edit(cpp, [
    ("""		sweet_scaler_cache((uintptr_t)src + sf, (size_t)(se - sf));
""", """		sweet_mali_wait_seq(sweet_mali_seq());
		sweet_scaler_cache((uintptr_t)src + sf, (size_t)(se - sf));
		if (sweet_scaler_logged < 40 && s->pixelFormat == SWEET_FMT_BGRA) {
			uint32_t nz = 0;
			for (uint32_t k = 0; k < 64; k++) {
				uint32_t px = 0;
				memcpy(&px, src + (uint64_t)((k * 37) % s->height) * s->bytesPerRow + (uint64_t)((k * 53) % s->width) * 4, 4);
				nz += px != 0;
			}
			IOLog("SWEET SCALER: source %u: %u of 64 sampled pixels not 0 (after the GPU wait)\\n", sid, nz);
		}
"""),
])
