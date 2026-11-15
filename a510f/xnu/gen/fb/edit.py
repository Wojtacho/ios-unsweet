import os, sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
NL = chr(92) + 'n'


def rep(a, b, n=1):
    global s
    a = a.replace('@NL@', NL)
    b = b.replace('@NL@', NL)
    c = s.count(a)
    assert c == n, (c, a[:70])
    s = s.replace(a, b)


# --- members
rep("""	uint32_t      fFadeStep;      /* fade-out steps done while off */
""", """	uint32_t      fFadeStep;      /* fade-out steps done while off */
	/*
	 * A510F (boot-arg sweetfb_flip, default 1): double-buffered panel. Each
	 * frame is drawn into the buffer DECON is not showing, then window 0's
	 * start address is switched to it (shadow-protected VIDW_ADD0 + standalone
	 * update, as the shim's fb_move), so a refresh never shows a half-drawn
	 * frame. Buffer 0 is the boot framebuffer (0x40800000, console/panics),
	 * buffer 1 the free 8 MiB below S-Boot's ramdisk at 0x41000000.
	 */
	bool          fFlip;
	uint64_t      fBufPA[2];
	uintptr_t     fBufVA[2];
	uint32_t      fShown;         /* buffer DECON scans out */
	uintptr_t     fDraw;          /* buffer being drawn by present() */
	vm_offset_t   fDecon;
	IOMemoryDescriptor *fBackMD;  /* buffer 1 (not ml_io_map: 8 MiB exhausts the io_map range) */
	IOMemoryMap   *fBackMap;
	IOLock       *fPresentLock;   /* one present at a time (swap thread, vsync) */
	uint64_t      fMinGap;        /* abs time between presents (sweetfb_hz) */
	uint64_t      fLastPresent;
	uint64_t      fPresents, fPresentAbs, fPresentMaxAbs, fFlipWaits;

	uintptr_t frontVA() const { return fFlip ? fBufVA[fShown] : fPixels; }
	void flipTo(uint32_t idx);
	bool waitFlipped(void);
""")

# --- start(): rate and buffers
rep("""	uint32_t hz = 10;
	PE_parse_boot_argn("sweetfb_hz", &hz, sizeof(hz));
	fFlushTicks = (hz == 0 || hz >= 60) ? 1 : 60 / hz;
""", """	uint32_t hz = 10;
	PE_parse_boot_argn("sweetfb_hz", &hz, sizeof(hz));
	fFlushTicks = (hz == 0 || hz >= 60) ? 1 : 60 / hz;
	nanoseconds_to_absolutetime((hz == 0 || hz >= 60) ? 0 : 1000000000ull / hz, &fMinGap);
	fPresentLock = IOLockAlloc();
	fBufPA[0] = fPhys;
	fBufVA[0] = fPixels;
	fDraw = fPixels;
	uint32_t flip = 1;
	PE_parse_boot_argn("sweetfb_flip", &flip, sizeof(flip));
	if (fPresentLock == NULL) {
		IOLog("SWEET FB: no present lock@NL@");
		return false;
	}
	if (flip && fPhys == A510F_FB_A && (uint64_t)fRowBytes * fHeight <= A510F_FB_SIZE) {
		fDecon = ml_io_map(A510F_DECON_PA, 0x1000);
		fBufPA[1] = A510F_FB_B;
		fBackMD = IOMemoryDescriptor::withPhysicalAddress(A510F_FB_B, A510F_FB_SIZE, kIODirectionInOut);
		fBackMap = fBackMD != NULL ? fBackMD->map(kIOMapWriteCombineCache) : NULL;
		fBufVA[1] = fBackMap != NULL ? (uintptr_t)fBackMap->getVirtualAddress() : 0;
		if (fDecon != 0 && fBufVA[1] != 0 &&
		    *(volatile uint32_t *)(fDecon + A510F_DECON_ADD0) == (uint32_t)fPhys) {
			memcpy((void *)fBufVA[1], (const void *)fPixels, (size_t)fRowBytes * fHeight);
			fFlip = true;
		}
		IOLog("SWEET FB: double buffer %s (DECON ADD0 0x%x, back 0x%llx), present at most %u Hz@NL@",
		    fFlip ? "on" : "OFF", fDecon ? *(volatile uint32_t *)(fDecon + A510F_DECON_ADD0) : 0,
		    (unsigned long long)A510F_FB_B, hz);
	}
""")

# --- vsync: fade on the shown buffer, time-based deferred present
rep("""				volatile uint32_t *row = (volatile uint32_t *)(fb->fPixels + (uint64_t)y * fb->fRowBytes);""",
    """				volatile uint32_t *row = (volatile uint32_t *)(fb->frontVA() + (uint64_t)y * fb->fRowBytes);""")
rep("""	bool flush = fb->fDirty && (count % fb->fFlushTicks) == 0;
	uint8_t *rec = NULL;
	if (flush) {""", """	/* frames a swap left pending (too soon after the last present) */
	bool flush = fb->fDirty && now - fb->fLastPresent >= fb->fMinGap;
	uint8_t *rec = NULL;
	if (flush) {
		fb->fLastPresent = now;""")

# --- swap(): present at once when due
rep("""	IOLockLock(fLock);
	memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);
	fDirty = true;
	IOLockUnlock(fLock);
	if ((++sweet_fb_swap_count % 1000) == 0) {
		IOLog("SWEET FB: %llu swaps@NL@", sweet_fb_swap_count);
	}
}""", """	/*
	 * A510F: present in the swapping thread when due, so CoreAnimation does
	 * not render into the surface while it is being read (mixed frames);
	 * otherwise leave it for the vsync timer.
	 */
	uint64_t now = mach_absolute_time();
	IOLockLock(fLock);
	memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);
	bool due = !fPowerOff && now - fLastPresent >= fMinGap;
	fDirty = !due;
	if (due) {
		fLastPresent = now;
	}
	IOLockUnlock(fLock);
	if (due) {
		present(rec);
	}
	if ((++sweet_fb_swap_count % 1000) == 0) {
		IOLog("SWEET FB: %llu swaps@NL@", sweet_fb_swap_count);
	}
}

static void
sweet_fb_dc_civac(uintptr_t p, uint64_t len)
{
	for (uintptr_t a = p & ~(uintptr_t)63, end = p + len; a < end; a += 64) {
		__asm__ volatile ("dc civac, %0" : : "r"(a) : "memory");
	}
	__asm__ volatile ("dsb sy" : : : "memory");
}

void
AppleCLCD::flipTo(uint32_t idx)
{
	volatile uint32_t *shadow = (volatile uint32_t *)(fDecon + A510F_DECON_SHADOWCON);
	volatile uint32_t *add0 = (volatile uint32_t *)(fDecon + A510F_DECON_ADD0);
	volatile uint32_t *update = (volatile uint32_t *)(fDecon + A510F_DECON_UPDATE);
	__asm__ volatile ("dsb sy" : : : "memory");
	*shadow = *shadow | A510F_SHADOWCON_WIN0_PROTECT;
	*add0 = (uint32_t)fBufPA[idx];
	*shadow = *shadow & ~A510F_SHADOWCON_WIN0_PROTECT;
	*update = *update | A510F_UPDATE_STANDALONE;
	fShown = idx;
}

/* The last flip has reached the panel (the shim's CPU1 kicks DECON every 16 ms). */
bool
AppleCLCD::waitFlipped(void)
{
	volatile uint32_t *update = (volatile uint32_t *)(fDecon + A510F_DECON_UPDATE);
	for (int i = 0; i < 50; i++) {
		if (!(*update & A510F_UPDATE_STANDALONE)) {
			return true;
		}
		if (i == 0) {
			fFlipWaits++;
		}
		IOSleep(1);
	}
	return false;
}""")

# --- present(): serialize, choose buffer, invalidate sources, flip, stats
rep("""void
AppleCLCD::present(const uint8_t *rec)
{
	uint32_t mask = get32(rec, 0x104);
""", """void
AppleCLCD::present(const uint8_t *rec)
{
	uint32_t mask = get32(rec, 0x104);
	uint64_t t0 = mach_absolute_time();

	IOLockLock(fPresentLock);
	if (fFlip && !waitFlipped()) {
		/* DECON did not take the last address: draw over the shown buffer */
		fDraw = fBufVA[fShown];
	} else {
		fDraw = fFlip ? fBufVA[fShown ^ 1] : fPixels;
	}
""")
rep("""		if (fFit) {
			presentFit(s, src, bpe, sx, sy, dx, dy, w, h);""", """		/* GPU-rendered (Mali, not coherent): drop stale cached lines first */
		if (src != 0 && s->memory != NULL && s->offset < s->memory->getLength()) {
			sweet_fb_dc_civac(src + s->offset, s->memory->getLength() - s->offset);
		}
		if (fFit) {
			presentFit(s, src, bpe, sx, sy, dx, dy, w, h);""")
rep("""			memcpy((void *)(fPixels + (uint64_t)(dy + y) * fRowBytes + (uint64_t)dx * 4),""",
    """			memcpy((void *)(fDraw + (uint64_t)(dy + y) * fRowBytes + (uint64_t)dx * 4),""")
rep("""		s->release();
	}
}

/*
 * A510F sweetfb_fit""", """		s->release();
	}
	if (fFlip && fDraw != fBufVA[fShown]) {
		flipTo(fShown ^ 1);
	}
	uint64_t dt = mach_absolute_time() - t0;
	fPresents++;
	fPresentAbs += dt;
	if (dt > fPresentMaxAbs) {
		fPresentMaxAbs = dt;
	}
	if (fPresents == 1 || fPresents % 300 == 0) {
		uint64_t avg = 0, max = 0;
		absolutetime_to_nanoseconds(fPresentAbs / fPresents, &avg);
		absolutetime_to_nanoseconds(fPresentMaxAbs, &max);
		IOLog("SWEET FB: %llu presents, avg %llu us max %llu us, flip waits %llu@NL@",
		    fPresents, avg / 1000, max / 1000, fFlipWaits);
		fPresentMaxAbs = 0;
	}
	IOLockUnlock(fPresentLock);
}

/*
 * A510F sweetfb_fit""")
rep("""			bzero((void *)(fPixels + (uint64_t)y * fRowBytes), (size_t)fWidth * 4);""",
    """			bzero((void *)(fDraw + (uint64_t)y * fRowBytes), (size_t)fWidth * 4);""")
rep("""		uint32_t *out = (uint32_t *)(fPixels + (uint64_t)py * fRowBytes);""",
    """		uint32_t *out = (uint32_t *)(fDraw + (uint64_t)py * fRowBytes);""")

# --- constants and externs
rep("""#define SWEET_FB_FORMAT_BGRA            0x42475241
""", """#define SWEET_FB_FORMAT_BGRA            0x42475241
/* A510F panel buffers and DECON (a510f/shim/shim.c, decon_7580 regs) */
#define A510F_FB_A                      0x40800000ull
#define A510F_FB_B                      0x41000000ull
#define A510F_FB_SIZE                   0x800000ull
#define A510F_DECON_PA                  0x14830000ull
#define A510F_DECON_SHADOWCON           0x0030
#define A510F_DECON_UPDATE              0x0710
#define A510F_DECON_ADD0                0x0880
#define A510F_SHADOWCON_WIN0_PROTECT    (1u << 8)
#define A510F_UPDATE_STANDALONE         (1u << 0)
extern "C" vm_offset_t ml_io_map(vm_offset_t phys_addr, vm_size_t size);
""")
assert '\x00' not in s
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')

# --- read the source through a cached mapping (kernelAddress() is write-combined: uncached reads, 324 ms per frame)
s = open(p, encoding='utf-8').read()
rep("""		uintptr_t src = s->kernelAddress();
""", """		/*
		 * A510F: kernelAddress() is a write-combined mapping, so every CPU
		 * read of it goes to RAM uncached (324 ms per 1242x2208 frame). Read
		 * through a cached mapping instead; the dc civac below drops stale
		 * lines first.
		 */
		IOMemoryMap *rmap = s->memory != NULL ? s->memory->map(kIOMapCopybackCache) : NULL;
		uintptr_t src = rmap != NULL ? (uintptr_t)rmap->getVirtualAddress() : s->kernelAddress();
""")
rep("""			presentFit(s, src, bpe, sx, sy, dx, dy, w, h);
			s->release();
			continue;""", """			presentFit(s, src, bpe, sx, sy, dx, dy, w, h);
			OSSafeReleaseNULL(rmap);
			s->release();
			continue;""")
rep("""		s->release();
	}
	if (fFlip && fDraw != fBufVA[fShown]) {""", """		OSSafeReleaseNULL(rmap);
		s->release();
	}
	if (fFlip && fDraw != fBufVA[fShown]) {""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok cached read')

# --- async again (CA must not wait for the copy) + per-step timing
s = open(p, encoding='utf-8').read()
rep("""	bool due = !fPowerOff && now - fLastPresent >= fMinGap;
	fDirty = !due;
	if (due) {
		fLastPresent = now;
	}
	IOLockUnlock(fLock);
	if (due) {
		present(rec);
	}""", """	(void)now;
	/*
	 * Build 44: presenting here made CoreAnimation wait ~340 ms per frame
	 * (worse than the old background copy): the vsync timer presents it.
	 */
	fDirty = true;
	IOLockUnlock(fLock);""")
rep("""	uint64_t      fPresents, fPresentAbs, fPresentMaxAbs, fFlipWaits;
""", """	uint64_t      fPresents, fPresentAbs, fPresentMaxAbs, fFlipWaits;
	uint64_t      fTMap, fTInval, fTScale, fTWait, fTSteps;  /* abs time per step */
""")
rep("""	IOLockLock(fPresentLock);
	if (fFlip && !waitFlipped()) {""", """	IOLockLock(fPresentLock);
	uint64_t tw = mach_absolute_time();
	if (fFlip && !waitFlipped()) {""")
rep("""		fDraw = fFlip ? fBufVA[fShown ^ 1] : fPixels;
	}
""", """		fDraw = fFlip ? fBufVA[fShown ^ 1] : fPixels;
	}
	fTWait += mach_absolute_time() - tw;
""")
rep("""		IOMemoryMap *rmap = s->memory != NULL ? s->memory->map(kIOMapCopybackCache) : NULL;
""", """		uint64_t t1 = mach_absolute_time();
		IOMemoryMap *rmap = s->memory != NULL ? s->memory->map(kIOMapCopybackCache) : NULL;
		fTMap += mach_absolute_time() - t1;
""")
rep("""		if (src != 0 && s->memory != NULL && s->offset < s->memory->getLength()) {
			sweet_fb_dc_civac(src + s->offset, s->memory->getLength() - s->offset);
		}
		if (fFit) {
			presentFit(s, src, bpe, sx, sy, dx, dy, w, h);""", """		uint64_t t2 = mach_absolute_time();
		if (src != 0 && s->memory != NULL && s->offset < s->memory->getLength()) {
			sweet_fb_dc_civac(src + s->offset, s->memory->getLength() - s->offset);
		}
		uint64_t t3 = mach_absolute_time();
		fTInval += t3 - t2;
		if (fFit) {
			presentFit(s, src, bpe, sx, sy, dx, dy, w, h);
			fTScale += mach_absolute_time() - t3;""")
rep("""	if (fPresents == 1 || fPresents % 300 == 0) {
		uint64_t avg = 0, max = 0;""", """	if (++fTSteps == 20 || fTSteps % 100 == 0) {
		uint64_t m = 0, i = 0, c = 0, wt = 0;
		absolutetime_to_nanoseconds(fTMap / fTSteps, &m);
		absolutetime_to_nanoseconds(fTInval / fTSteps, &i);
		absolutetime_to_nanoseconds(fTScale / fTSteps, &c);
		absolutetime_to_nanoseconds(fTWait / fTSteps, &wt);
		IOLog("SWEET FB: per present: map %llu us, cache inval %llu us, scale %llu us, flip wait %llu us@NL@",
		    m / 1000, i / 1000, c / 1000, wt / 1000);
	}
	if (fPresents == 1 || fPresents % 300 == 0) {
		uint64_t avg = 0, max = 0;""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok async+timing')

# --- the copy on its own workloop: the vsync timer (CA's frame pacing) keeps firing
s = open(p, encoding='utf-8').read()
rep("""	/* frames a swap left pending (too soon after the last present) */
	bool flush = fb->fDirty && now - fb->fLastPresent >= fb->fMinGap;
	uint8_t *rec = NULL;
	if (flush) {
		fb->fLastPresent = now;
		rec = (uint8_t *)IOMallocData(SWEET_FB_SWAP_REC_SIZE);
		if (rec != NULL) {
			memcpy(rec, fb->fPending, SWEET_FB_SWAP_REC_SIZE);
			fb->fDirty = false;
		}
	}
	IOLockUnlock(fb->fLock);
	if (rec != NULL) {
		fb->present(rec);
		IOFreeData(rec, SWEET_FB_SWAP_REC_SIZE);
	}
	sender->setTimeoutUS(SWEET_FB_VSYNC_US);
}
""", """	/*
	 * A510F: the panel copy runs on its own workloop (presentFired). Run
	 * here it stopped these vsync notifications, which pace CoreAnimation,
	 * for the whole copy.
	 */
	bool flush = fb->fDirty && !fb->fPresentBusy && fb->fPresentTimer != NULL &&
	    now - fb->fLastPresent >= fb->fMinGap;
	if (flush) {
		fb->fLastPresent = now;
		fb->fPresentBusy = true;
	}
	IOLockUnlock(fb->fLock);
	if (flush) {
		fb->fPresentTimer->setTimeoutUS(1);
	}
	sender->setTimeoutUS(SWEET_FB_VSYNC_US);
}

void
AppleCLCD::presentFired(OSObject *owner, IOTimerEventSource *sender)
{
	(void)sender;
	AppleCLCD *fb = (AppleCLCD *)owner;
	uint8_t *rec = (uint8_t *)IOMallocData(SWEET_FB_SWAP_REC_SIZE);
	IOLockLock(fb->fLock);
	if (rec != NULL) {
		memcpy(rec, fb->fPending, SWEET_FB_SWAP_REC_SIZE);
		fb->fDirty = false;
	}
	IOLockUnlock(fb->fLock);
	if (rec != NULL) {
		fb->present(rec);
		IOFreeData(rec, SWEET_FB_SWAP_REC_SIZE);
	}
	IOLockLock(fb->fLock);
	fb->fPresentBusy = false;
	IOLockUnlock(fb->fLock);
}
""")
rep("""	uint64_t      fTMap, fTInval, fTScale, fTWait, fTSteps;  /* abs time per step */
""", """	uint64_t      fTMap, fTInval, fTScale, fTWait, fTSteps;  /* abs time per step */
	IOWorkLoop         *fPresentLoop;
	IOTimerEventSource *fPresentTimer;
	bool                fPresentBusy;
	static void presentFired(OSObject *owner, IOTimerEventSource *sender);
""")
rep("""	fVsync->setTimeoutUS(SWEET_FB_VSYNC_US);
""", """	fPresentLoop = IOWorkLoop::workLoop();
	fPresentTimer = IOTimerEventSource::timerEventSource(this, &AppleCLCD::presentFired);
	if (fPresentLoop == NULL || fPresentTimer == NULL ||
	    fPresentLoop->addEventSource(fPresentTimer) != kIOReturnSuccess) {
		IOLog("SWEET FB: no present workloop@NL@");
		OSSafeReleaseNULL(fPresentTimer);
	}
	fVsync->setTimeoutUS(SWEET_FB_VSYNC_US);
""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok present loop')

# --- build each output row in a cached buffer, store it to the panel memory in one block
s = open(p, encoding='utf-8').read()
rep("""		uint32_t *out = (uint32_t *)(fDraw + (uint64_t)py * fRowBytes);
		for (int32_t px = px0; px < px1; px++) {
			int32_t lx = fFitCol[px] - dx;
			if (lx >= 0 && lx < w) {
				out[px] = convert ? sweet_fb_pixel(fmt, row[lx]) : row[lx];
			}
		}
	}
}""", """		uint32_t *out = (uint32_t *)(fDraw + (uint64_t)py * fRowBytes);
		if (fRowBuf == NULL) {
			for (int32_t px = px0; px < px1; px++) {
				int32_t lx = fFitCol[px] - dx;
				if (lx >= 0 && lx < w) {
					out[px] = convert ? sweet_fb_pixel(fmt, row[lx]) : row[lx];
				}
			}
			continue;
		}
		/* cached row, then one block store into the (write-combined) panel memory */
		int32_t first = -1, last = -1;
		for (int32_t px = px0; px < px1; px++) {
			int32_t lx = fFitCol[px] - dx;
			if (lx >= 0 && lx < w) {
				fRowBuf[px] = convert ? sweet_fb_pixel(fmt, row[lx]) : row[lx];
				if (first < 0) {
					first = px;
				}
				last = px;
			}
		}
		if (first >= 0) {
			memcpy(out + first, fRowBuf + first, (size_t)(last - first + 1) * 4);
		}
	}
}""")
rep("""	IOWorkLoop         *fPresentLoop;
""", """	IOWorkLoop         *fPresentLoop;
	uint32_t           *fRowBuf;        /* one panel row, cached (presentFit) */
""")
rep("""	fPresentLoop = IOWorkLoop::workLoop();
""", """	fRowBuf = (uint32_t *)IOMallocData((vm_size_t)fWidth * 4);
	fPresentLoop = IOWorkLoop::workLoop();
""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok rowbuf')

# --- present synchronously at SwapEnd again: CA cannot redraw a surface being read (incomplete frames in build 46)
s = open(p, encoding='utf-8').read()
rep("""	(void)now;
	/*
	 * Build 44: presenting here made CoreAnimation wait ~340 ms per frame
	 * (worse than the old background copy): the vsync timer presents it.
	 */
	fDirty = true;
	IOLockUnlock(fLock);""", """	/*
	 * Present here, in the swapping thread: CoreAnimation reuses a surface
	 * once it is swapped, so a copy in the background read half-redrawn
	 * frames (build 46). With display surfaces cached (SweetSurface
	 * display) the copy is short. Frames left by the rate limit go through
	 * the present workloop.
	 */
	bool due = !fPowerOff && now - fLastPresent >= fMinGap;
	fDirty = !due;
	if (due) {
		fLastPresent = now;
	}
	IOLockUnlock(fLock);
	if (due) {
		present(rec);
	}""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok sync again')

# --- screen-off fade: whole dimmed frames into the back buffer, not in-place halving of the shown one
s = open(p, encoding='utf-8').read()
rep("""		/* Fade out: halve every channel each vsync, then black, then idle. */
		uint32_t step = fb->fFadeStep;
		if (step <= 6) {
			fb->fFadeStep = step + 1;
		}
		IOLockUnlock(fb->fLock);
		if (step <= 6) {""", """		/*
		 * A510F with the double buffer: the present workloop redraws the
		 * last frame at 1/2, 1/4, 1/8 brightness, then black, each into
		 * the hidden buffer and flipped (the in-place halving below read
		 * the write-combined panel memory uncached and showed it drawn
		 * top to bottom).
		 */
		if (fb->fFlip && fb->fPresentTimer != NULL) {
			uint32_t fstep = fb->fFadeStep;
			bool go = fstep <= 3 && !fb->fPresentBusy;
			if (go) {
				fb->fFadeStep = fstep + 1;
				fb->fPresentBusy = true;
			}
			IOLockUnlock(fb->fLock);
			if (go) {
				fb->fPresentTimer->setTimeoutUS(1);
			}
			sender->setTimeoutUS(SWEET_FB_VSYNC_US);
			return;
		}
		/* Fade out: halve every channel each vsync, then black, then idle. */
		uint32_t step = fb->fFadeStep;
		if (step <= 6) {
			fb->fFadeStep = step + 1;
		}
		IOLockUnlock(fb->fLock);
		if (step <= 6) {""")
rep("""	AppleCLCD *fb = (AppleCLCD *)owner;
	uint8_t *rec = (uint8_t *)IOMallocData(SWEET_FB_SWAP_REC_SIZE);
	IOLockLock(fb->fLock);
	if (rec != NULL) {""", """	AppleCLCD *fb = (AppleCLCD *)owner;
	IOLockLock(fb->fLock);
	bool off = fb->fPowerOff;
	uint32_t fstep = fb->fFadeStep;
	IOLockUnlock(fb->fLock);
	if (off) {
		if (fstep >= 1 && fstep <= 3 && fb->fHaveLast) {
			fb->fDim = fstep;               /* 1/2, 1/4, 1/8 */
			fb->present(fb->fLastRec);
			fb->fDim = 0;
		} else {
			IOLockLock(fb->fPresentLock);
			fb->waitFlipped();
			uintptr_t back = fb->fBufVA[fb->fShown ^ 1];
			bzero((void *)back, (size_t)fb->fRowBytes * fb->fHeight);
			fb->flipTo(fb->fShown ^ 1);
			IOLockUnlock(fb->fPresentLock);
		}
		IOLockLock(fb->fLock);
		fb->fPresentBusy = false;
		IOLockUnlock(fb->fLock);
		return;
	}
	uint8_t *rec = (uint8_t *)IOMallocData(SWEET_FB_SWAP_REC_SIZE);
	IOLockLock(fb->fLock);
	if (rec != NULL) {""")
rep("""	IOWorkLoop         *fPresentLoop;
""", """	IOWorkLoop         *fPresentLoop;
	uint8_t             fLastRec[SWEET_FB_SWAP_REC_SIZE];   /* last presented swap (fade) */
	bool                fHaveLast;
	uint32_t            fDim;           /* fade: shift right by fDim (presentFit) */
""")
rep("""	IOLockLock(fPresentLock);
	uint64_t tw = mach_absolute_time();""", """	IOLockLock(fPresentLock);
	if (rec != fLastRec) {
		memcpy(fLastRec, rec, SWEET_FB_SWAP_REC_SIZE);
		fHaveLast = true;
	}
	uint64_t tw = mach_absolute_time();""")
rep("""				fRowBuf[px] = convert ? sweet_fb_pixel(fmt, row[lx]) : row[lx];""",
    """				uint32_t v = convert ? sweet_fb_pixel(fmt, row[lx]) : row[lx];
				fRowBuf[px] = fDim ? (v >> fDim) & (0x01010101u * (0xffu >> fDim)) : v;""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok fade')

# --- wake without the stale frame, slower fade, memory line every 10 s
s = open(p, encoding='utf-8').read()
rep("""			if (off != fFB->fPowerOff) {
				fFB->fPowerOff = off;
				fFB->fFadeStep = 0;
				fFB->fDirty = true;     /* on: redraw the latest frame */
			}""", """			if (off != fFB->fPowerOff) {
				fFB->fPowerOff = off;
				fFB->fFadeStep = 0;
				/*
				 * A510F: on wake, wait for CoreAnimation's new frame (the
				 * lock screen) instead of showing the one from before
				 * the screen went off; the vsync timer shows the old one
				 * only if nothing comes within 0.5 s.
				 */
				fFB->fDirty = false;
				fFB->fWakeSkip = !off;
				fFB->fWakeAt = mach_absolute_time();
			}""")
rep("""	memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);
	/*
	 * Present here, in the swapping thread:""", """	memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);
	fWakeSkip = false;
	/*
	 * Present here, in the swapping thread:""")
rep("""			uint32_t fstep = fb->fFadeStep;
			bool go = fstep <= 3 && !fb->fPresentBusy;""", """			uint32_t fstep = fb->fFadeStep;
			/* one step every 6 vsyncs (~0.1 s plus the redraw): ~0.5 s in all */
			bool go = fstep <= 3 && !fb->fPresentBusy && (count % 6) == 0;""")
rep("""	/*
	 * A510F: the panel copy runs on its own workloop (presentFired). Run""", """	if (fb->fWakeSkip && now - fb->fWakeAt > fb->fWakeWait) {
		fb->fWakeSkip = false;
		fb->fDirty = true;              /* nothing new since the wake: show the last frame */
	}
	if ((count % 600) == 0) {
		/* A510F: memory every 10 s (thrashing in the wallpaper editor) */
		uint64_t sb = 0, bb = 0;
		uint32_t sn = 0, bn = 0;
		sweet_surface_stats(&sb, &sn);
		sweet_mali_bo_stats(&bb, &bn);
		IOLog("SWEET MEM: free %llu MB, wired %llu MB | surfaces %u = %llu MB | GPU buffers %u = %llu MB@NL@",
		    (uint64_t)vm_page_free_count * page_size >> 20, (uint64_t)vm_page_wire_count * page_size >> 20,
		    sn, sb >> 20, bn, bb >> 20);
	}
	/*
	 * A510F: the panel copy runs on its own workloop (presentFired). Run""")
rep("""	bool                fHaveLast;
""", """	bool                fHaveLast;
	bool                fWakeSkip;      /* display just on: wait for a new frame */
	uint64_t            fWakeAt, fWakeWait;
""")
rep("""	fPresentLock = IOLockAlloc();
""", """	fPresentLock = IOLockAlloc();
	nanoseconds_to_absolutetime(500000000ull, &fWakeWait);
""")
rep("""extern "C" vm_offset_t ml_io_map(vm_offset_t phys_addr, vm_size_t size);
""", """extern "C" vm_offset_t ml_io_map(vm_offset_t phys_addr, vm_size_t size);
extern "C" void sweet_surface_stats(uint64_t *bytes, uint32_t *count);     /* SweetSurface.cpp */
extern "C" void sweet_mali_bo_stats(uint64_t *bytes, uint32_t *count);     /* SweetMali.cpp */
extern "C" unsigned int vm_page_free_count, vm_page_wire_count;
""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok wake/fade/mem')

# --- autopilot screenshots (sweet_mmc.c sweet_auto): a downscaled copy of the shown buffer
rep("""	setProperty(kIOUserClientClassKey, "IOMobileFramebufferUserClient");
	setProperty("external", false);""", """	sweet_fb_instance = this;
	setProperty(kIOUserClientClassKey, "IOMobileFramebufferUserClient");
	setProperty("external", false);""")
rep("""extern "C" void sweet_surface_stats(uint64_t *bytes, uint32_t *count);     /* SweetSurface.cpp */
""", """extern "C" void sweet_surface_stats(uint64_t *bytes, uint32_t *count);     /* SweetSurface.cpp */
class AppleCLCD;
static AppleCLCD *sweet_fb_instance;
extern "C" int sweet_fb_shot(uint16_t *out, uint32_t maxpix, uint32_t div, uint32_t *w, uint32_t *h, uint32_t *flags);
""")
rep("""bool
AppleCLCD::start(IOService *provider)
{""", """/*
 * A510F autopilot (sweet_mmc.c): the buffer the panel shows, every div-th
 * pixel of every div-th row, as RGB565. flags: bit 0 display off, bit 1
 * double buffer, bits 8.. the shown buffer. Reads only, no lock: a flip in
 * the middle tears the picture at worst.
 */
extern "C" int
sweet_fb_shot(uint16_t *out, uint32_t maxpix, uint32_t div, uint32_t *w, uint32_t *h, uint32_t *flags)
{
	AppleCLCD *fb = sweet_fb_instance;
	if (fb == NULL || div == 0) {
		return 6;       /* ENXIO */
	}
	uint32_t ow = fb->fWidth / div, oh = fb->fHeight / div;
	if ((uint64_t)ow * oh > maxpix) {
		return 22;      /* EINVAL */
	}
	uintptr_t base = fb->frontVA();
	for (uint32_t y = 0; y < oh; y++) {
		const volatile uint32_t *row = (const volatile uint32_t *)(base + (uint64_t)y * div * fb->fRowBytes);
		uint16_t *o = out + (uint64_t)y * ow;
		for (uint32_t x = 0; x < ow; x++) {
			uint32_t px = row[x * div];
			o[x] = (uint16_t)(((px >> 8) & 0xf800) | ((px >> 5) & 0x07e0) | ((px >> 3) & 0x001f));
		}
	}
	*w = ow;
	*h = oh;
	*flags = (fb->fPowerOff ? 1u : 0u) | (fb->fFlip ? 2u : 0u) | (fb->fShown << 8);
	return 0;
}

bool
AppleCLCD::start(IOService *provider)
{""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok shot')

# --- log every new layer geometry, not just the first 16 swaps (the top-left copy)
rep("""		if (sweet_fb_swaps_logged < 16) {
			sweet_fb_swaps_logged++;""", """		uint64_t sig = ((uint64_t)layer << 60) ^ ((uint64_t)(s ? s->width : 0) << 44) ^
		    ((uint64_t)(s ? s->height : 0) << 30) ^ ((uint64_t)get32(a, 8) << 17) ^ get32(a, 12) ^
		    ((uint64_t)(uint32_t)dx << 50) ^ ((uint64_t)(uint32_t)dy << 36) ^ ((uint64_t)(uint32_t)w << 22) ^
		    ((uint64_t)(uint32_t)h << 8) ^ ((uint64_t)(uint32_t)sx << 40) ^ ((uint64_t)(uint32_t)sy << 26);
		bool newsig = true;
		for (uint32_t k = 0; k < sweet_fb_sig_n && newsig; k++) {
			newsig = sweet_fb_sig[k] != sig;
		}
		if (newsig && sweet_fb_sig_n < 64) {
			sweet_fb_sig[sweet_fb_sig_n++] = sig;
		}
		if (sweet_fb_swaps_logged < 16 || (newsig && sweet_fb_sig_n < 64)) {
			sweet_fb_swaps_logged++;""")
rep("""static uint32_t sweet_fb_swaps_logged;
""", """static uint32_t sweet_fb_swaps_logged;
static uint64_t sweet_fb_sig[64];       /* layer geometries seen (A510F) */
static uint32_t sweet_fb_sig_n;
""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok sig')

# --- wake: hold CA's frames for fWakeWait (it first sends the old home screen), then show the newest
rep("""	memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);
	fWakeSkip = false;
	/*""", """	memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);
	if (fWakeSkip || now - fWakeAt < fWakeWait * 4) {
		static uint32_t wake_logged;
		if (wake_logged < 200) {
			uint64_t ns = 0;
			absolutetime_to_nanoseconds(now - fWakeAt, &ns);
			wake_logged++;
			IOLog("SWEET FB: swap %u at wake +%llu ms%s@NL@", get32(rec, 0x50), ns / 1000000,
			    fWakeSkip ? " (held)" : "");
		}
	}
	if (fWakeSkip) {
		/* the vsync timer shows the newest one when fWakeWait is over */
		IOLockUnlock(fLock);
		return;
	}
	/*""")
rep("""	nanoseconds_to_absolutetime(500000000ull, &fWakeWait);""",
    """	uint32_t wake_ms = 800;
	PE_parse_boot_argn("sweetfb_wake_ms", &wake_ms, sizeof(wake_ms));
	nanoseconds_to_absolutetime((uint64_t)wake_ms * 1000000ull, &fWakeWait);""")
rep("""		fb->fDirty = true;              /* nothing new since the wake: show the last frame */""",
    """		fb->fDirty = true;              /* the newest frame (held since the wake), or the last one */""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok wake hold')

# --- fit scale: tight loop on 4 CPUs (fit_fast.inc), per-band cache invalidation
FIT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fit_fast.inc'), encoding='utf-8').read()
rep("""extern "C" int
sweet_fb_shot(""", FIT.replace(chr(92) + 'n', '@NL@') + """extern "C" int
sweet_fb_shot(""")
rep("""	fRowBuf = (uint32_t *)IOMallocData((vm_size_t)fWidth * 4);
""", """	fRowBuf = (uint32_t *)IOMallocData((vm_size_t)fWidth * 4);
	sweet_fit_setup(fWidth);
""")
rep("""		if (src != 0 && s->memory != NULL && s->offset < s->memory->getLength()) {
			sweet_fb_dc_civac(""", """		if (!fFit && src != 0 && s->memory != NULL && s->offset < s->memory->getLength()) {
			/* (fit: presentFit drops the lines it reads, band by band) */
			sweet_fb_dc_civac(""")
rep("""	const bool convert = fmt == SWEET_FMT_L10R || fmt == SWEET_FMT_W30R;
""", """	const bool convert = fmt == SWEET_FMT_L10R || fmt == SWEET_FMT_W30R;
	if (!convert) {
		/* the fade too: dimmed in the same fast copy (the slow path did not dim without fRowBuf) */
		struct sweet_fit_job j = {
			base, s->bytesPerRow, fDraw, fRowBytes, fFitCol, sx, sy, dx, dy, w, h,
			px0, px1, py0, py1, fFitNum, fFitDen, fDim,
		};
		sweet_fit_run(&j);
		return;
	}
	sweet_fb_dc_civac((uintptr_t)base, s->memory->getLength() - s->offset);
""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok fit fast')

# --- pipelined present: the swap hands the frame to the present thread; the next swap waits for it
rep("""	bool due = !fPowerOff && now - fLastPresent >= fMinGap;
	fDirty = !due;
	if (due) {
		fLastPresent = now;
	}
	IOLockUnlock(fLock);
	if (due) {
		present(rec);
	}""", """	bool due = !fPowerOff && now - fLastPresent >= fMinGap;
	if (due && sweet_fb_async && fPresentTimer != NULL) {
		/*
		 * A510F (sweetfb_async, default 1): CoreAnimation alternates two
		 * surfaces, so the copy of this one can run while it draws the
		 * next into the other; only the next swap waits for this copy
		 * (before CA can draw into this surface again).
		 */
		uint64_t w0 = mach_absolute_time();
		while (fPresentBusy) {
			IOLockSleep(fLock, &fPresentBusy, THREAD_UNINT);
		}
		fTSwapWait += mach_absolute_time() - w0;
		memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);  /* the newest swap */
		fPresentBusy = true;
		fDirty = true;
		fLastPresent = mach_absolute_time();
		IOLockUnlock(fLock);
		fPresentTimer->setTimeoutUS(1);
		due = false;
	} else {
		fDirty = !due;
		if (due) {
			fLastPresent = now;
		}
		IOLockUnlock(fLock);
	}
	if (due) {
		present(rec);
	}""")
# wake the waiting swap when a present ends
rep("""		IOLockLock(fb->fLock);
		fb->fPresentBusy = false;
		IOLockUnlock(fb->fLock);
		return;
	}""", """		IOLockLock(fb->fLock);
		fb->fPresentBusy = false;
		IOLockWakeup(fb->fLock, &fb->fPresentBusy, false);
		IOLockUnlock(fb->fLock);
		return;
	}""")
rep("""	IOLockLock(fb->fLock);
	fb->fPresentBusy = false;
	IOLockUnlock(fb->fLock);
}""", """	IOLockLock(fb->fLock);
	fb->fPresentBusy = false;
	IOLockWakeup(fb->fLock, &fb->fPresentBusy, false);
	IOLockUnlock(fb->fLock);
}""")
rep("""	bool                fHaveLast;
""", """	bool                fHaveLast;
	uint64_t            fTSwapWait;     /* swaps waiting for the previous present (async) */
	uint64_t            fPresentsAt10s;
""")
rep("""	fRowBuf = (uint32_t *)IOMallocData((vm_size_t)fWidth * 4);
""", """	PE_parse_boot_argn("sweetfb_async", &sweet_fb_async, sizeof(sweet_fb_async));
	fRowBuf = (uint32_t *)IOMallocData((vm_size_t)fWidth * 4);
""")
rep("""static IOLock              *sweet_fit_lock;""", """#ifndef THREAD_UNINT
#define THREAD_UNINT 0
#endif
static uint32_t             sweet_fb_async = 1;
static IOLock              *sweet_fit_lock;""")
# frames per second in the 10 s memory line
rep("""		IOLog("SWEET MEM: free %llu MB, wired %llu MB | surfaces %u = %llu MB | GPU buffers %u = %llu MB@NL@",
		    (uint64_t)vm_page_free_count * page_size >> 20, (uint64_t)vm_page_wire_count * page_size >> 20,
		    sn, sb >> 20, bn, bb >> 20);""", """		uint64_t sw = 0;
		absolutetime_to_nanoseconds(fb->fTSwapWait, &sw);
		fb->fTSwapWait = 0;
		IOLog("SWEET MEM: free %llu MB, wired %llu MB | surfaces %u = %llu MB | GPU buffers %u = %llu MB | "
		    "%llu frames/10 s, swaps waited %llu ms@NL@",
		    (uint64_t)vm_page_free_count * page_size >> 20, (uint64_t)vm_page_wire_count * page_size >> 20,
		    sn, sb >> 20, bn, bb >> 20, fb->fPresents - fb->fPresentsAt10s, sw / 1000000);
		fb->fPresentsAt10s = fb->fPresents;""")
# GPU job queue (SweetMali): the frame's render jobs may still be running; copy after them
rep("""extern "C" void sweet_mali_bo_stats(uint64_t *bytes, uint32_t *count);     /* SweetMali.cpp */
""", """extern "C" void sweet_mali_bo_stats(uint64_t *bytes, uint32_t *count);     /* SweetMali.cpp */
extern "C" uint64_t sweet_mali_seq(void);                                   /* SweetMali.cpp */
extern "C" void sweet_mali_wait_seq(uint64_t seq);
""")
rep("""AppleCLCD::present(const uint8_t *rec)
{
	uint32_t mask = get32(rec, 0x104);
	uint64_t t0 = mach_absolute_time();
""", """AppleCLCD::present(const uint8_t *rec)
{
	uint32_t mask = get32(rec, 0x104);
	sweet_mali_wait_seq(sweet_mali_seq());          /* every GPU job queued so far is done */
	uint64_t t0 = mach_absolute_time();
""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok async')

# Screen-off fade: begin at the first vsync after "display off" and step every
# 2 vsyncs (~0.15 s in all, about an iPhone's); log each step's time since off.
rep("""			/* one step every 6 vsyncs (~0.1 s plus the redraw): ~0.5 s in all */
			bool go = fstep <= 3 && !fb->fPresentBusy && (count % 6) == 0;""", """			/* first step at once, then every 2 vsyncs: ~0.15 s in all */
			bool go = fstep <= 3 && !fb->fPresentBusy && (fstep == 0 || (count % 2) == 0);""")
rep("""	if (off) {
		if (fstep >= 1 && fstep <= 3 && fb->fHaveLast) {""", """	if (off) {
		{
			uint64_t ns = 0;
			absolutetime_to_nanoseconds(mach_absolute_time() - fb->fOffAt, &ns);
			IOLog("SWEET FB: fade step %u at off +%llu ms%s@NL@", fstep, ns / 1000000,
			    fb->fHaveLast ? "" : " (no last frame)");
		}
		if (fstep >= 1 && fstep <= 3 && fb->fHaveLast) {""")
rep("""				fFB->fPowerOff = off;
				fFB->fFadeStep = 0;""", """				fFB->fPowerOff = off;
				fFB->fFadeStep = 0;
				if (off) {
					fFB->fOffAt = mach_absolute_time();
				}""")
rep("""	bool          fPowerOff;      /* RequestPowerChange(0) */""", """	bool          fPowerOff;      /* RequestPowerChange(0) */
	uint64_t      fOffAt;         /* when it went off (fade log) */""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok fade timing')

# Boot hold: at startup backboardd turns the display on and draws an early
# lock screen (half-drawn wallpaper), SpringBoard turns it off while it sets
# up, then on again (round 18: on -> 2 swaps -> off -> on, no key). Hold the
# frames of the first "on" of the boot for up to sweetfb_boot_hold_ms
# (default 8000): the console stays until the real lock screen.
rep("""	uint64_t            fWakeAt, fWakeWait;""", """	uint64_t            fWakeAt, fWakeWait;
	uint64_t            fHoldWait;      /* this hold: fWakeWait, or the boot hold */
	bool                fBootSeen;      /* the first "display on" of the boot came */""")
rep("""	if (fb->fWakeSkip && now - fb->fWakeAt > fb->fWakeWait) {""", """	if (fb->fWakeSkip && now - fb->fWakeAt > (fb->fHoldWait ? fb->fHoldWait : fb->fWakeWait)) {""")
rep("""				fFB->fDirty = false;
				fFB->fWakeSkip = !off;
				fFB->fWakeAt = mach_absolute_time();
			}""", """				fFB->fDirty = false;
				fFB->fWakeSkip = !off;
				fFB->fWakeAt = mach_absolute_time();
				fFB->fHoldWait = fFB->fWakeWait;
				if (!off) {
					fFB->fBootSeen = true;
				}
			} else if (!off && !fFB->fBootSeen) {
				/* the first "on" of the boot (no change: it starts on): boot hold */
				uint32_t ms = 8000;
				PE_parse_boot_argn("sweetfb_boot_hold_ms", &ms, sizeof(ms));
				fFB->fBootSeen = true;
				if (ms > 0) {
					fFB->fDirty = false;
					fFB->fWakeSkip = true;
					fFB->fWakeAt = mach_absolute_time();
					nanoseconds_to_absolutetime((uint64_t)ms * 1000000ull, &fFB->fHoldWait);
					IOLog("SWEET FB: boot hold: frames held up to %u ms@NL@", ms);
				}
			}""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok boot hold')

# Fade frames found no surface (round 19 bursts: full-brightness frames, then
# black): CA drops its display surfaces at "display off", so the lookup by id
# failed and the dim redraw drew nothing over an older frame. Keep a
# reference to each layer's last surface; the fade redraws from it.
rep("""	uint32_t            fDim;           /* fade: shift right by fDim (presentFit) */""",
    """	uint32_t            fDim;           /* fade: shift right by fDim (presentFit) */
	SweetSurface       *fFadeSurf[SWEET_FB_LAYERS];     /* last surface of each layer, kept for the fade */""")
rep("""		SweetSurface *s = sweet_surface_copy(id);""", """		SweetSurface *s = NULL;
		if (fDim != 0 && fFadeSurf[layer] != NULL) {
			s = fFadeSurf[layer];   /* CA may have dropped it at display off */
			s->retain();
		} else {
			s = sweet_surface_copy(id);
			if (s != NULL && fFadeSurf[layer] != s) {
				OSSafeReleaseNULL(fFadeSurf[layer]);
				s->retain();
				fFadeSurf[layer] = s;
			}
		}""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok fade surfaces')

# Fade debug (round 22: dim steps ran and flipped but frames stayed bright):
# what each dim redraw finds per layer, and whether the fast copy ran.
rep("""		if (fDim != 0 && fFadeSurf[layer] != NULL) {
			s = fFadeSurf[layer];   /* CA may have dropped it at display off */
			s->retain();
		} else {""", """		if (fDim != 0 && fFadeSurf[layer] != NULL) {
			s = fFadeSurf[layer];   /* CA may have dropped it at display off */
			s->retain();
			IOLog("SWEET FB: fade dim %u layer %u id %u: kept surface %ux%u fmt 0x%x mem %p@NL@", fDim, layer, id,
			    s->width, s->height, s->pixelFormat, s->memory);
		} else {
			if (fDim != 0) {
				IOLog("SWEET FB: fade dim %u layer %u id %u: no kept surface@NL@", fDim, layer, id);
			}""")
rep("""	if (!convert) {
		/* the fade too: dimmed in the same fast copy (the slow path did not dim without fRowBuf) */""", """	if (fDim != 0) {
		IOLog("SWEET FB: fade copy dim %u: fit rows %d..%d cols %d..%d into %p@NL@", fDim, py0, py1, px0, px1,
		    (void *)fDraw);
	}
	if (!convert) {
		/* the fade too: dimmed in the same fast copy (the slow path did not dim without fRowBuf) */""")
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('ok fade debug')
