/*
 * A510F: the fit scale (1242x2208 -> 1080x1920) split over CPUs. One job
 * a frame: SWEET_FIT_WORKERS kernel threads plus the presenting thread each
 * take a band of panel rows: drop the stale cached lines of the source rows
 * they read (the GPU wrote them), scale a row into a cached row buffer, then
 * one block copy into the write-combined panel memory. Single-threaded and
 * per-pixel-checked this took ~48 ms a frame.
 */
#define SWEET_FIT_WORKERS 3
struct sweet_fit_job {
	const uint8_t *base;            /* surface pixels (cached mapping) + offset */
	uint64_t       bpr;
	uintptr_t      draw;
	uint64_t       drawBpr;
	const int32_t *col;             /* panel column -> logical column */
	int32_t        sx, sy, dx, dy, w, h, px0, px1, py0, py1;
	int32_t        num, den;
};
static IOLock              *sweet_fit_lock;
static struct sweet_fit_job sweet_fit_cur;
static uint32_t             sweet_fit_gen, sweet_fit_left;
static uint32_t            *sweet_fit_rows[SWEET_FIT_WORKERS + 1];
static bool                 sweet_fit_ready;
extern "C" kern_return_t kernel_thread_start(void (*)(void *, int), void *, thread_t *);
extern "C" void thread_deallocate(thread_t);

static void
sweet_fit_band(const struct sweet_fit_job *j, uint32_t band, uint32_t nbands)
{
	int32_t rows = j->py1 - j->py0;
	int32_t b0 = j->py0 + (int32_t)((int64_t)rows * band / nbands);
	int32_t b1 = j->py0 + (int32_t)((int64_t)rows * (band + 1) / nbands);
	uint32_t *buf = sweet_fit_rows[band];
	if (b0 >= b1 || buf == NULL) {
		return;
	}
	/* source rows this band reads, out of the cache first */
	int32_t l0 = (int32_t)(((int64_t)b0 * j->den) / j->num) - j->dy;
	int32_t l1 = (int32_t)(((int64_t)(b1 - 1) * j->den) / j->num) - j->dy;
	l0 = l0 < 0 ? 0 : l0;
	l1 = l1 >= j->h ? j->h - 1 : l1;
	if (l1 >= l0) {
		uintptr_t a = (uintptr_t)(j->base + (uint64_t)(j->sy + l0) * j->bpr) & ~(uintptr_t)63;
		uintptr_t end = (uintptr_t)(j->base + (uint64_t)(j->sy + l1 + 1) * j->bpr);
		for (; a < end; a += 64) {
			__asm__ volatile ("dc civac, %0" : : "r"(a) : "memory");
		}
		__asm__ volatile ("dsb sy" : : : "memory");
	}
	/* columns inside the layer: the same for every row */
	int32_t c0 = j->px0, c1 = j->px1;
	while (c0 < c1 && (j->col[c0] - j->dx < 0 || j->col[c0] - j->dx >= j->w)) {
		c0++;
	}
	while (c1 > c0 && (j->col[c1 - 1] - j->dx < 0 || j->col[c1 - 1] - j->dx >= j->w)) {
		c1--;
	}
	if (c0 >= c1) {
		return;
	}
	const int32_t *col = j->col;
	const int32_t off = j->sx - j->dx;
	for (int32_t py = b0; py < b1; py++) {
		int32_t ly = (int32_t)(((int64_t)py * j->den) / j->num) - j->dy;
		if (ly < 0 || ly >= j->h) {
			continue;
		}
		const uint32_t *row = (const uint32_t *)(j->base + (uint64_t)(j->sy + ly) * j->bpr) + off;
		int32_t px = c0;
		for (; px + 4 <= c1; px += 4) {
			uint32_t v0 = row[col[px]], v1 = row[col[px + 1]], v2 = row[col[px + 2]], v3 = row[col[px + 3]];
			buf[px] = v0;
			buf[px + 1] = v1;
			buf[px + 2] = v2;
			buf[px + 3] = v3;
		}
		for (; px < c1; px++) {
			buf[px] = row[col[px]];
		}
		memcpy((void *)(j->draw + (uint64_t)py * j->drawBpr + (uint64_t)c0 * 4), buf + c0, (size_t)(c1 - c0) * 4);
	}
}

static void
sweet_fit_worker(void *arg, int wr)
{
	(void)wr;
	uint32_t band = (uint32_t)(uintptr_t)arg, seen = 0;
	IOLockLock(sweet_fit_lock);
	for (;;) {
		while (sweet_fit_gen == seen) {
			IOLockSleep(sweet_fit_lock, &sweet_fit_gen, THREAD_UNINT);
		}
		seen = sweet_fit_gen;
		struct sweet_fit_job j = sweet_fit_cur;
		IOLockUnlock(sweet_fit_lock);
		sweet_fit_band(&j, band, SWEET_FIT_WORKERS + 1);
		IOLockLock(sweet_fit_lock);
		if (--sweet_fit_left == 0) {
			IOLockWakeup(sweet_fit_lock, &sweet_fit_left, false);
		}
	}
}

static void
sweet_fit_setup(uint32_t width)
{
	uint32_t on = 1;
	PE_parse_boot_argn("sweetfb_mt", &on, sizeof(on));
	sweet_fit_lock = IOLockAlloc();
	for (uint32_t i = 0; i <= SWEET_FIT_WORKERS; i++) {
		sweet_fit_rows[i] = (uint32_t *)IOMallocData((vm_size_t)width * 4);
		if (sweet_fit_rows[i] == NULL) {
			return;
		}
	}
	if (sweet_fit_lock == NULL || !on) {
		IOLog("SWEET FB: fit scale single-threaded\n");
		return;
	}
	for (uint32_t i = 0; i < SWEET_FIT_WORKERS; i++) {
		thread_t th;
		if (kernel_thread_start(sweet_fit_worker, (void *)(uintptr_t)(i + 1), &th) != KERN_SUCCESS) {
			IOLog("SWEET FB: fit worker %u not started\n", i);
			return;
		}
		thread_deallocate(th);
	}
	sweet_fit_ready = true;
	IOLog("SWEET FB: fit scale on %u CPUs\n", SWEET_FIT_WORKERS + 1);
}

/* Band 0 here, the others on the workers; returns when all are done. */
static void
sweet_fit_run(const struct sweet_fit_job *j)
{
	if (!sweet_fit_ready) {
		sweet_fit_band(j, 0, 1);
		return;
	}
	IOLockLock(sweet_fit_lock);
	sweet_fit_cur = *j;
	sweet_fit_left = SWEET_FIT_WORKERS;
	sweet_fit_gen++;
	IOLockWakeup(sweet_fit_lock, &sweet_fit_gen, false);
	IOLockUnlock(sweet_fit_lock);
	sweet_fit_band(j, 0, SWEET_FIT_WORKERS + 1);
	IOLockLock(sweet_fit_lock);
	while (sweet_fit_left != 0) {
		IOLockSleep(sweet_fit_lock, &sweet_fit_left, THREAD_UNINT);
	}
	IOLockUnlock(sweet_fit_lock);
}

