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
