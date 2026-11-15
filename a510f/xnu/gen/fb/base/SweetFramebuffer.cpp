/*
 * Built-in IOMobileFramebuffer for SWEET: the ABL's continuous-splash
 * framebuffer (1080x2400 a8r8g8b8 in RAM, the panel scans it out by
 * itself) as the main display, driven by CoreAnimation's CPU renderer.
 *
 * IOMobileFramebuffer.framework (iOS 16.7) counts /arm-io children with
 * device_type "display-subsystem", waits for that many services matching
 * IOServiceMatching("IOMobileFramebuffer"), opens each with type 0 and
 * reads canvas-width/canvas-height from the service's provider. The class
 * here (AppleCLCD, an IOMobileFramebuffer) matches the /arm-io/disp0 nub.
 *
 * User client selectors used by CoreAnimation:
 *   3  GetLayerDefaultSurface [layer, ?] -> [IOSurface port name]
 *   4  SwapBegin -> [swap id]
 *   5  SwapEnd, struct 0x46c: +0x50 swap id, +0x54 IOSurface id per layer
 *      (4 layers), +0x64 rect a / +0xc4 rect b per layer (int x,y,w,h),
 *      +0x104 enabled layer mask
 *   6  SwapWait, 7 GetID, 8 GetDisplaySize -> [w, h],
 *   12 RequestPowerChange [state]: 0 = display off (backboardd, power
 *      button / auto-lock), else on. Off fades the panel out over a few
 *      vsyncs (halving each pixel) and keeps it black until on again;
 *      the panel itself stays powered (AMOLED black pixels are off).
 *   18 IsMainDisplay,
 *   28 GetDotPitch, 72 Enable/DisableNotifications [func, refcon, type, 0]
 * Everything else is accepted and logged once.
 *
 * SwapEnd copies the enabled layers' surfaces into the panel memory (no
 * scaling, CPU copy). Vsync (notification type 5) is a 60 Hz timer that
 * sends (count, mach_absolute_time, 0) as 32-bit halves to clients that
 * enabled it, through the port they registered (IOConnectSetNotificationPort).
 *
 * The panel memory itself is published as an IOSurface and returned as the
 * default framebuffer surface. The kernel text console keeps drawing over
 * the GUI by default: boot-arg sweetfb_noconsole=1 stops drawing it from
 * the first swap on (it still reaches the persistent log; panics draw).
 */
#include "SweetSurface.h"

extern "C" int sweet_console_muted;     /* osfmk/console/serial_console.c */

#if defined(SWEET)
#include <IOKit/IOService.h>
#include <IOKit/IOUserClient.h>
#include <IOKit/IOKitKeys.h>
#include <IOKit/IOLib.h>
#include <IOKit/IOLocks.h>
#include <IOKit/IOWorkLoop.h>
#include <IOKit/IOTimerEventSource.h>
#include <IOKit/system.h>
#include <pexpert/pexpert.h>
#include <kern/clock.h>
#include <sys/proc.h>

enum {
	kSweetFBGetLayerDefaultSurface  = 3,
	kSweetFBSwapBegin               = 4,
	kSweetFBSwapEnd                 = 5,
	kSweetFBSwapWait                = 6,
	kSweetFBGetID                   = 7,
	kSweetFBGetDisplaySize          = 8,
	kSweetFBRequestPowerChange      = 12,
	kSweetFBIsMainDisplay           = 18,
	kSweetFBGetDotPitch             = 28,
	kSweetFBNotifications           = 72,
};

#define SWEET_FB_SWAP_REC_SIZE          0x46c
#define SWEET_FB_LAYERS                 4
#define SWEET_FB_NOTIFY_TYPES           8
#define SWEET_FB_NOTIFY_VSYNC           5
#define SWEET_FB_VSYNC_US               16667
#define SWEET_FB_DOT_PITCH              401     /* ppi, as the iPhone 8 Plus panel */
/*
 * The iOS userland only has status bar / layout data for real iPhone
 * screens (UIKit: "No status bar visual provider for screen", the red
 * rdar://45025538 bar for 360x800 points). A510F: the userland is the
 * iPhone 8 Plus, which renders 1242x2208 (414x736 points @3x) and scales
 * it to its 1080x1920 panel; the A510F panel is the same, so the frame is
 * presented as 1242x2208 and scaled to fit (boot-arg sweetfb_fit=1, exact
 * 16:9, no borders). Boot-arg sweetfb_native=1 presents the panel size.
 */
#define SWEET_FB_LOGICAL_W              1242
#define SWEET_FB_LOGICAL_H              2208
#define SWEET_FB_FORMAT_BGRA            0x42475241

class IOMobileFramebuffer : public IOService {
	OSDeclareDefaultStructors(IOMobileFramebuffer);
};

OSDefineMetaClassAndStructors(IOMobileFramebuffer, IOService);

class IOMobileFramebufferUserClient;

class AppleCLCD : public IOMobileFramebuffer {
	OSDeclareDefaultStructors(AppleCLCD);

	IOWorkLoop         *fWorkLoop;
	IOTimerEventSource *fVsync;
	uint64_t            fVsyncCount;

	static void vsyncFired(OSObject *owner, IOTimerEventSource *sender);

public:
	uint64_t      fPhys;
	uint32_t      fWidth, fHeight, fRowBytes;
	uint32_t      fLogicalW, fLogicalH;     /* size reported to userland */
	int32_t       fOffX, fOffY;             /* logical origin of the panel */
	/*
	 * A510F (boot-arg sweetfb_fit=1): scale the whole logical frame into the
	 * panel (height fits, pillarbox fPadX each side) instead of cropping
	 * its centre. Panel = pad + logical * fFitNum / fFitDen.
	 */
	bool          fFit, fFitCleared;
	int32_t       fFitNum, fFitDen, fPadX;
	int32_t      *fFitCol;                  /* panel column -> logical column */
	uintptr_t     fPixels;          /* kernel mapping of the panel memory */
	IOMemoryMap  *fMap;
	SweetSurface *fSurface;         /* the panel memory as an IOSurface */
	IOLock       *fLock;            /* swaps and client list */
	OSArray      *fClients;
	uint32_t      fSwapID;
	bool          fConsolePaused;
	uint8_t       fPending[SWEET_FB_SWAP_REC_SIZE];     /* latest swap, not yet shown */
	bool          fDirty;
	uint32_t      fFlushTicks;    /* vsync ticks between panel copies */
	bool          fPowerOff;      /* RequestPowerChange(0) */
	uint32_t      fFadeStep;      /* fade-out steps done while off */

	bool start(IOService *provider) APPLE_KEXT_OVERRIDE;
	void addClient(IOMobileFramebufferUserClient *client);
	void removeClient(IOMobileFramebufferUserClient *client);
	void swap(const uint8_t *rec);
	void present(const uint8_t *rec);
	void presentFit(SweetSurface *s, uintptr_t src, uint32_t bpe, int32_t sx, int32_t sy,
	    int32_t dx, int32_t dy, int32_t w, int32_t h);
};

OSDefineMetaClassAndStructors(AppleCLCD, IOMobileFramebuffer);

/*
 * A510F (from MakrSas/ios-topaz 0138): the GPU's service class. QuartzCore
 * (CAMetalContextCreate, once per process) polls
 * IOServiceMatching("IOAcceleratorES") 300 times, 100 ms apart, before it
 * goes on: thirty seconds at every backboardd start. One without
 * MetalPluginName/MetalPluginClassName is found and then passed over by
 * Metal, which leaves the renderers as they were. sweetaccel=0: none.
 */
class IOAcceleratorES : public IOService {
	OSDeclareDefaultStructors(IOAcceleratorES);
};

OSDefineMetaClassAndStructors(IOAcceleratorES, IOService);

class IOMobileFramebufferUserClient : public IOUserClient {
	OSDeclareDefaultStructors(IOMobileFramebufferUserClient);

public:
	AppleCLCD          *fFB;
	task_t              fTask;
	mach_port_t         fPort;
	io_user_reference_t fFunc[SWEET_FB_NOTIFY_TYPES];
	io_user_reference_t fRefcon[SWEET_FB_NOTIFY_TYPES];

	bool initWithTask(task_t owningTask, void *securityID, UInt32 type) APPLE_KEXT_OVERRIDE;
	bool start(IOService *provider) APPLE_KEXT_OVERRIDE;
	IOReturn clientClose(void) APPLE_KEXT_OVERRIDE;
	IOReturn registerNotificationPort(mach_port_t port, UInt32 type,
	    io_user_reference_t refCon) APPLE_KEXT_OVERRIDE;
	IOReturn externalMethod(uint32_t selector, IOExternalMethodArguments *args,
	    IOExternalMethodDispatch *dispatch, OSObject *target,
	    void *reference) APPLE_KEXT_OVERRIDE;
	void notify(uint32_t type, const uint64_t *values, uint32_t count);
};

OSDefineMetaClassAndStructors(IOMobileFramebufferUserClient, IOUserClient);

bool
AppleCLCD::start(IOService *provider)
{
	PE_Video video;

	if (!IOService::start(provider)) {
		return false;
	}
	PE_current_console(&video);
	fPhys = video.v_baseAddr;
	fWidth = (uint32_t)video.v_width;
	fHeight = (uint32_t)video.v_height;
	fRowBytes = (uint32_t)video.v_rowBytes;
	if (fPhys == 0 || fWidth == 0 || fHeight == 0 || fRowBytes < fWidth * 4) {
		IOLog("SWEET FB: no boot framebuffer\n");
		return false;
	}
	int native = 0;
	PE_parse_boot_argn("sweetfb_native", &native, sizeof(native));
	fLogicalW = fWidth;
	fLogicalH = fHeight;
	if (!native && fWidth <= SWEET_FB_LOGICAL_W && fHeight <= SWEET_FB_LOGICAL_H) {
		fLogicalW = SWEET_FB_LOGICAL_W;
		fLogicalH = SWEET_FB_LOGICAL_H;
	}
	fOffX = (int32_t)(fLogicalW - fWidth) / 2;
	fOffY = (int32_t)(fLogicalH - fHeight) / 2;
	int fit = 0;
	PE_parse_boot_argn("sweetfb_fit", &fit, sizeof(fit));
	fFit = fit && (fLogicalW != fWidth || fLogicalH != fHeight);
	if (fFit) {
		/* Scale by the tighter axis so the whole frame is visible. */
		if ((int64_t)fWidth * fLogicalH < (int64_t)fHeight * fLogicalW) {
			fFitNum = (int32_t)fWidth;
			fFitDen = (int32_t)fLogicalW;
		} else {
			fFitNum = (int32_t)fHeight;
			fFitDen = (int32_t)fLogicalH;
		}
		fPadX = ((int32_t)fWidth - (int32_t)((int64_t)fLogicalW * fFitNum / fFitDen)) / 2;
		fFitCol = (int32_t *)IOMalloc(sizeof(int32_t) * fWidth);
		if (fFitCol == NULL) {
			fFit = false;
		} else {
			for (uint32_t px = 0; px < fWidth; px++) {
				fFitCol[px] = (int32_t)(((int64_t)((int32_t)px - fPadX) * fFitDen) / fFitNum);
			}
			IOLog("SWEET FB: fit %ux%u into %ux%u: scale %d/%d, pillarbox %d px\n",
			    fLogicalW, fLogicalH, fWidth, fHeight, fFitNum, fFitDen, fPadX);
		}
	}
	fLock = IOLockAlloc();
	fClients = OSArray::withCapacity(4);
	fSurface = sweet_surface_create_physical(fPhys, fWidth, fHeight, fRowBytes, SWEET_FB_FORMAT_BGRA);
	fPixels = fSurface != NULL ? fSurface->kernelAddress() : 0;
	fWorkLoop = IOWorkLoop::workLoop();
	if (fLock == NULL || fClients == NULL || fPixels == 0 || fWorkLoop == NULL) {
		IOLog("SWEET FB: setup failed\n");
		OSSafeReleaseNULL(fSurface);    /* stays published: also held by the table */
		OSSafeReleaseNULL(fWorkLoop);
		return false;
	}
	fVsync = IOTimerEventSource::timerEventSource(this, &AppleCLCD::vsyncFired);
	if (fVsync == NULL || fWorkLoop->addEventSource(fVsync) != kIOReturnSuccess) {
		IOLog("SWEET FB: no vsync timer\n");
		return false;
	}
	uint32_t hz = 10;
	PE_parse_boot_argn("sweetfb_hz", &hz, sizeof(hz));
	fFlushTicks = (hz == 0 || hz >= 60) ? 1 : 60 / hz;
	fVsync->setTimeoutUS(SWEET_FB_VSYNC_US);

	setProperty(kIOUserClientClassKey, "IOMobileFramebufferUserClient");
	setProperty("external", false);
	setProperty("DisplayPipePlaneBaseAlignment", 64ULL, 32);
	registerService();
	IOLog("SWEET FB: AppleCLCD %ux%u stride %u at 0x%llx, default surface %u, presented as %ux%u\n",
	    fWidth, fHeight, fRowBytes, fPhys, fSurface->id, fLogicalW, fLogicalH);
	uint32_t accelOn = 1;
	(void)PE_parse_boot_argn("sweetaccel", &accelOn, sizeof(accelOn));
	IOAcceleratorES *accel = accelOn ? OSTypeAlloc(IOAcceleratorES) : NULL;
	if (accel != NULL && accel->init()) {
		accel->setName("sgx");
		if (accel->attach(this)) {
			accel->registerService();
			IOLog("SWEET FB: empty IOAcceleratorES published (no 30 s wait in CAMetalContextCreate)\n");
		}
	}
	OSSafeReleaseNULL(accel);
	return true;
}

void
AppleCLCD::vsyncFired(OSObject *owner, IOTimerEventSource *sender)
{
	AppleCLCD *fb = (AppleCLCD *)owner;
	uint64_t now = mach_absolute_time();
	uint64_t count = ++fb->fVsyncCount;
	uint64_t values[6] = {
		(uint32_t)count, (uint32_t)(count >> 32),
		(uint32_t)now, (uint32_t)(now >> 32),
		0, 0,
	};

	IOLockLock(fb->fLock);
	for (unsigned int i = 0; i < fb->fClients->getCount(); i++) {
		IOMobileFramebufferUserClient *client =
		    (IOMobileFramebufferUserClient *)fb->fClients->getObject(i);
		client->notify(SWEET_FB_NOTIFY_VSYNC, values, 6);
	}
	if (fb->fPowerOff) {
		/* Fade out: halve every channel each vsync, then black, then idle. */
		uint32_t step = fb->fFadeStep;
		if (step <= 6) {
			fb->fFadeStep = step + 1;
		}
		IOLockUnlock(fb->fLock);
		if (step <= 6) {
			for (uint32_t y = 0; y < fb->fHeight; y++) {
				volatile uint32_t *row = (volatile uint32_t *)(fb->fPixels + (uint64_t)y * fb->fRowBytes);
				for (uint32_t x = 0; x < fb->fWidth; x++) {
					row[x] = step < 6 ? (row[x] >> 1) & 0x7f7f7f7f : 0;
				}
			}
		}
		sender->setTimeoutUS(SWEET_FB_VSYNC_US);
		return;
	}
	bool flush = fb->fDirty && (count % fb->fFlushTicks) == 0;
	uint8_t *rec = NULL;
	if (flush) {
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

void
AppleCLCD::addClient(IOMobileFramebufferUserClient *client)
{
	IOLockLock(fLock);
	fClients->setObject(client);
	IOLockUnlock(fLock);
}

void
AppleCLCD::removeClient(IOMobileFramebufferUserClient *client)
{
	IOLockLock(fLock);
	unsigned int i = fClients->getNextIndexOfObject(client, 0);
	if (i != (unsigned int)-1) {
		fClients->removeObject(i);
	}
	IOLockUnlock(fLock);
}

static uint32_t
get32(const uint8_t *p, uint32_t off)
{
	uint32_t v;
	memcpy(&v, p + off, 4);
	return v;
}

static uint32_t sweet_fb_swaps_logged;

/*
 * A510F: layer pixel formats. Every 4-byte format used to be copied as if it
 * were BGRA. With wide colour iOS also presents 10-bit layers in 4 bytes
 * (joranv1/ios-sailfish saw w30r and b3a8): read as BGRA they come out as
 * scrambled colours. 'l10r' (ARGB2101010) and 'w30r' (XR10, extended range:
 * 384..894 is 0..1) are converted; anything else of 4 bytes is copied as
 * before. Each new (format, bytes per element) is logged once.
 */
#define SWEET_FMT_L10R 0x6c313072u      /* 'l10r' */
#define SWEET_FMT_W30R 0x77333072u      /* 'w30r' */

static uint32_t sweet_fb_seen[32];
static uint32_t sweet_fb_seen_n;

static void
sweet_fb_note_format(uint32_t fmt, uint32_t bpe, uint32_t w, uint32_t h)
{
	uint32_t key = fmt ^ (bpe << 24);
	for (uint32_t i = 0; i < sweet_fb_seen_n; i++) {
		if (sweet_fb_seen[i] == key) {
			return;
		}
	}
	if (sweet_fb_seen_n < 32) {
		sweet_fb_seen[sweet_fb_seen_n++] = key;
	}
	IOLog("SWEET FB: new layer format 0x%08x '%c%c%c%c' bpe %u (%ux%u)%s\n", fmt,
	    (int)((fmt >> 24) & 0x7f) ?: '.', (int)((fmt >> 16) & 0x7f) ?: '.',
	    (int)((fmt >> 8) & 0x7f) ?: '.', (int)(fmt & 0x7f) ?: '.', bpe, w, h,
	    bpe != 4 ? ": not drawn" :
	    (fmt == SWEET_FMT_L10R || fmt == SWEET_FMT_W30R) ? ": converted from 10 bit" : "");
}

static inline uint32_t
sweet_xr10(uint32_t v)
{
	int32_t c = ((int32_t)v - 384) * 255 / 510;
	return c < 0 ? 0 : c > 255 ? 255 : (uint32_t)c;
}

static inline uint32_t
sweet_fb_pixel(uint32_t fmt, uint32_t v)
{
	if (fmt == SWEET_FMT_L10R) {
		return 0xff000000u | (((v >> 22) & 0xff) << 16) | (((v >> 12) & 0xff) << 8) | ((v >> 2) & 0xff);
	}
	if (fmt == SWEET_FMT_W30R) {
		return 0xff000000u | (sweet_xr10((v >> 20) & 0x3ff) << 16) |
		       (sweet_xr10((v >> 10) & 0x3ff) << 8) | sweet_xr10(v & 0x3ff);
	}
	return v;
}
static uint64_t sweet_fb_swap_count;

/* Copy each enabled layer's surface into the panel memory (no scaling). */
/*
 * A swap only records the frame: copying 10 MB into the panel on every
 * swap (backboardd presents at 60 Hz) took the whole CPU. The vsync timer
 * shows the latest frame every fFlushTicks ticks (boot-arg sweetfb_hz,
 * default 10 Hz).
 */
void
AppleCLCD::swap(const uint8_t *rec)
{
	IOLockLock(fLock);
	memcpy(fPending, rec, SWEET_FB_SWAP_REC_SIZE);
	fDirty = true;
	IOLockUnlock(fLock);
	if ((++sweet_fb_swap_count % 1000) == 0) {
		IOLog("SWEET FB: %llu swaps\n", sweet_fb_swap_count);
	}
}

void
AppleCLCD::present(const uint8_t *rec)
{
	uint32_t mask = get32(rec, 0x104);


	if (!fConsolePaused) {
		int quiet = 0;
		fConsolePaused = true;
		if (PE_parse_boot_argn("sweetfb_noconsole", &quiet, sizeof(quiet)) && quiet != 0) {
			/* Not PE_initialize_console(kPEDisableScreen): its console switch
			 * writes the read-only-late cons_ops_index and panics. */
			sweet_console_muted = 1;
		}
	}

	for (uint32_t layer = 0; layer < SWEET_FB_LAYERS; layer++) {
		uint32_t id = get32(rec, 0x54 + 4 * layer);
		const uint8_t *a = rec + 0x64 + 16 * layer;
		const uint8_t *b = rec + 0xc4 + 16 * layer;
		int32_t sx = (int32_t)get32(a, 0), sy = (int32_t)get32(a, 4);
		int32_t dx = (int32_t)get32(b, 0), dy = (int32_t)get32(b, 4);
		int32_t w = (int32_t)get32(b, 8), h = (int32_t)get32(b, 12);

		if (!(mask & (1u << layer)) || id == 0) {
			continue;
		}
		SweetSurface *s = sweet_surface_copy(id);
		if (sweet_fb_swaps_logged < 16) {
			sweet_fb_swaps_logged++;
			IOLog("SWEET FB: swap %u layer %u surface %u %ux%u fmt 0x%x bpr %u a %d,%d %ux%u b %d,%d %dx%d\n",
			    get32(rec, 0x50), layer, id, s ? s->width : 0, s ? s->height : 0,
			    s ? s->pixelFormat : 0, s ? s->bytesPerRow : 0, sx, sy, get32(a, 8),
			    get32(a, 12), dx, dy, w, h);
		}
		if (s == NULL || s == fSurface) {
			OSSafeReleaseNULL(s);
			continue;
		}
		uintptr_t src = s->kernelAddress();
		uint32_t bpe = s->bytesPerElement ? s->bytesPerElement : 4;
		sweet_fb_note_format(s->pixelFormat, bpe, s->width, s->height);
		if (w <= 0 || h <= 0) {
			w = (int32_t)s->width;
			h = (int32_t)s->height;
		}
		if (sx < 0 || sy < 0) {
			sx = sy = 0;
		}
		if (dx < 0 || dy < 0) {
			dx = dy = 0;
		}
		if (fFit) {
			presentFit(s, src, bpe, sx, sy, dx, dy, w, h);
			s->release();
			continue;
		}
		/* Logical (presented) display coordinates -> panel coordinates. */
		dx -= fOffX;
		dy -= fOffY;
		if (dx < 0) {
			sx -= dx;
			w += dx;
			dx = 0;
		}
		if (dy < 0) {
			sy -= dy;
			h += dy;
			dy = 0;
		}
		if (w > (int32_t)s->width - sx) {
			w = (int32_t)s->width - sx;
		}
		if (h > (int32_t)s->height - sy) {
			h = (int32_t)s->height - sy;
		}
		if (w > (int32_t)fWidth - dx) {
			w = (int32_t)fWidth - dx;
		}
		if (h > (int32_t)fHeight - dy) {
			h = (int32_t)fHeight - dy;
		}
		uint64_t last = (uint64_t)s->offset + (uint64_t)(sy + h - 1) * s->bytesPerRow +
		    (uint64_t)(sx + w) * 4;
		if (w <= 0 || h <= 0 || s->elementWidth != 1 || s->elementHeight != 1 ||
		    s->memory == NULL || last > s->memory->getLength()) {
			src = 0;
		}
		if (src != 0 && bpe == 4) {
			for (int32_t y = 0; y < h; y++) {
				memcpy((void *)(fPixels + (uint64_t)(dy + y) * fRowBytes + (uint64_t)dx * 4),
				    (const void *)(src + s->offset + (uint64_t)(sy + y) * s->bytesPerRow + (uint64_t)sx * 4),
				    (size_t)w * 4);
			}
		}
		s->release();
	}
}

/*
 * A510F sweetfb_fit: nearest-neighbour scale of one layer, logical rect
 * (dx, dy, w, h) read from the surface at (sx, sy), into the panel.
 */
void
AppleCLCD::presentFit(SweetSurface *s, uintptr_t src, uint32_t bpe, int32_t sx, int32_t sy,
    int32_t dx, int32_t dy, int32_t w, int32_t h)
{
	if (src == 0 || bpe != 4 || s->elementWidth != 1 || s->elementHeight != 1 || s->memory == NULL) {
		return;
	}
	if (w > (int32_t)s->width - sx) {
		w = (int32_t)s->width - sx;
	}
	if (h > (int32_t)s->height - sy) {
		h = (int32_t)s->height - sy;
	}
	if (w <= 0 || h <= 0) {
		return;
	}
	uint64_t last = (uint64_t)s->offset + (uint64_t)(sy + h - 1) * s->bytesPerRow + (uint64_t)(sx + w) * 4;
	if (last > s->memory->getLength()) {
		return;
	}
	if (!fFitCleared) {
		/* Black pillarbox (the console text was there). */
		for (uint32_t y = 0; y < fHeight; y++) {
			bzero((void *)(fPixels + (uint64_t)y * fRowBytes), (size_t)fWidth * 4);
		}
		fFitCleared = true;
	}
	int32_t py0 = (int32_t)(((int64_t)dy * fFitNum + fFitDen - 1) / fFitDen);
	int32_t py1 = (int32_t)(((int64_t)(dy + h) * fFitNum + fFitDen - 1) / fFitDen);
	int32_t px0 = fPadX + (int32_t)(((int64_t)dx * fFitNum + fFitDen - 1) / fFitDen);
	int32_t px1 = fPadX + (int32_t)(((int64_t)(dx + w) * fFitNum + fFitDen - 1) / fFitDen);
	if (py0 < 0) {
		py0 = 0;
	}
	if (px0 < 0) {
		px0 = 0;
	}
	if (py1 > (int32_t)fHeight) {
		py1 = (int32_t)fHeight;
	}
	if (px1 > (int32_t)fWidth) {
		px1 = (int32_t)fWidth;
	}
	const uint8_t *base = (const uint8_t *)(src + s->offset);
	const uint32_t fmt = s->pixelFormat;
	const bool convert = fmt == SWEET_FMT_L10R || fmt == SWEET_FMT_W30R;
	for (int32_t py = py0; py < py1; py++) {
		int32_t ly = (int32_t)(((int64_t)py * fFitDen) / fFitNum) - dy;
		if (ly < 0 || ly >= h) {
			continue;
		}
		const uint32_t *row = (const uint32_t *)(base + (uint64_t)(sy + ly) * s->bytesPerRow) + sx;
		uint32_t *out = (uint32_t *)(fPixels + (uint64_t)py * fRowBytes);
		for (int32_t px = px0; px < px1; px++) {
			int32_t lx = fFitCol[px] - dx;
			if (lx >= 0 && lx < w) {
				out[px] = convert ? sweet_fb_pixel(fmt, row[lx]) : row[lx];
			}
		}
	}
}

bool
IOMobileFramebufferUserClient::initWithTask(task_t owningTask, void *securityID, UInt32 type)
{
	if (!IOUserClient::initWithTask(owningTask, securityID, type)) {
		return false;
	}
	fTask = owningTask;
	return true;
}

bool
IOMobileFramebufferUserClient::start(IOService *provider)
{
	fFB = OSDynamicCast(AppleCLCD, provider);
	if (fFB == NULL || !IOUserClient::start(provider)) {
		return false;
	}
	fFB->addClient(this);
	return true;
}

IOReturn
IOMobileFramebufferUserClient::clientClose(void)
{
	if (fFB != NULL) {
		fFB->removeClient(this);
		IOLockLock(fFB->fLock);
		mach_port_t old = fPort;
		fPort = MACH_PORT_NULL;
		IOLockUnlock(fFB->fLock);
		if (old != MACH_PORT_NULL) {
			releaseNotificationPort(old);
		}
	}
	terminate();
	return kIOReturnSuccess;
}

IOReturn
IOMobileFramebufferUserClient::registerNotificationPort(mach_port_t port, __unused UInt32 type,
    __unused io_user_reference_t refCon)
{
	mach_port_t old;
	IOLockLock(fFB->fLock);
	old = fPort;
	fPort = port;
	IOLockUnlock(fFB->fLock);
	if (old != MACH_PORT_NULL) {
		releaseNotificationPort(old);
	}
	return kIOReturnSuccess;
}

/* Called with the framebuffer lock held. */
void
IOMobileFramebufferUserClient::notify(uint32_t type, const uint64_t *values, uint32_t count)
{
	OSAsyncReference64 ref;

	if (type >= SWEET_FB_NOTIFY_TYPES || fFunc[type] == 0 || fPort == MACH_PORT_NULL) {
		return;
	}
	bzero(ref, sizeof(ref));
	setAsyncReference64(ref, fPort, (mach_vm_address_t)fFunc[type], fRefcon[type], fTask);
	sendAsyncResult64WithOptions(ref, kIOReturnSuccess, (io_user_reference_t *)values, count,
	    kIOUserNotifyOptionCanDrop);
}

static uint64_t sweet_fb_logged;        /* selectors already logged (< 64) */

IOReturn
IOMobileFramebufferUserClient::externalMethod(uint32_t selector, IOExternalMethodArguments *args,
    __unused IOExternalMethodDispatch *dispatch, __unused OSObject *target,
    __unused void *reference)
{
	IOReturn ret = kIOReturnSuccess;
	uint64_t out[2] = { 0, 0 };
	uint32_t outCount = 0;

	switch (selector) {
	case kSweetFBGetLayerDefaultSurface:
		out[0] = sweet_surface_port_in_task(fFB->fSurface, fTask);
		outCount = 1;
		break;
	case kSweetFBSwapBegin:
		IOLockLock(fFB->fLock);
		out[0] = ++fFB->fSwapID;
		IOLockUnlock(fFB->fLock);
		outCount = 1;
		break;
	case kSweetFBSwapEnd: {
		uint8_t rec[SWEET_FB_SWAP_REC_SIZE];
		if (args->structureInputDescriptor != NULL ||
		    args->structureInputSize < SWEET_FB_SWAP_REC_SIZE) {
			ret = kIOReturnBadArgument;
			break;
		}
		memcpy(rec, args->structureInput, sizeof(rec));
		fFB->swap(rec);
		break;
	}
	case kSweetFBGetID:
		out[0] = 0;
		outCount = 1;
		break;
	case kSweetFBGetDisplaySize:
		out[0] = fFB->fLogicalW;
		out[1] = fFB->fLogicalH;
		outCount = 2;
		break;
	case kSweetFBIsMainDisplay:
		out[0] = 1;
		outCount = 1;
		break;
	case kSweetFBGetDotPitch:
		out[0] = SWEET_FB_DOT_PITCH;
		outCount = 1;
		break;
	case kSweetFBNotifications:
		if (args->scalarInputCount >= 3 && args->scalarInput[2] < SWEET_FB_NOTIFY_TYPES) {
			uint32_t type = (uint32_t)args->scalarInput[2];
			IOLockLock(fFB->fLock);
			fFunc[type] = args->scalarInput[0];
			fRefcon[type] = args->scalarInput[1];
			IOLockUnlock(fFB->fLock);
			char name[32];
			proc_selfname(name, sizeof(name));
			IOLog("SWEET FB: %s notifications type %u %s\n", name, type,
			    args->scalarInput[0] ? "on" : "off");
		}
		break;
	case kSweetFBRequestPowerChange:
		if (args->scalarInputCount >= 1) {
			bool off = args->scalarInput[0] == 0;
			/*
			 * A510F: boot-arg sweetfb_alwayson=1 ignores "display off"
			 * (auto-lock) while there is no button to turn it back on.
			 */
			static int alwayson = -1;
			if (alwayson < 0) {
				uint32_t v = 0;
				alwayson = PE_parse_boot_argn("sweetfb_alwayson", &v, sizeof(v)) && v;
			}
			if (off && alwayson) {
				IOLog("SWEET FB: display off ignored (sweetfb_alwayson)\n");
				break;
			}
			IOLockLock(fFB->fLock);
			if (off != fFB->fPowerOff) {
				fFB->fPowerOff = off;
				fFB->fFadeStep = 0;
				fFB->fDirty = true;     /* on: redraw the latest frame */
			}
			IOLockUnlock(fFB->fLock);
			IOLog("SWEET FB: display %s\n", off ? "off" : "on");
		}
		break;
	case kSweetFBSwapWait:
	default:
		break;
	}

	for (uint32_t i = 0; i < args->scalarOutputCount; i++) {
		args->scalarOutput[i] = i < outCount ? out[i] : 0;
	}
	if (args->structureOutputDescriptor == NULL && args->structureOutput != NULL) {
		bzero(args->structureOutput, args->structureOutputSize);
	}
	if (selector >= 64 || !(sweet_fb_logged & (1ULL << selector))) {
		if (selector < 64) {
			sweet_fb_logged |= 1ULL << selector;
		}
		char name[32];
		proc_selfname(name, sizeof(name));
		IOLog("SWEET FB: %s sel %u in %u/%u out %u/%u -> 0x%x\n", name, selector,
		    args->scalarInputCount, args->structureInputSize,
		    args->scalarOutputCount, args->structureOutputSize, ret);
	}
	return ret;
}
#endif /* SWEET */
