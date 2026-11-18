/*
 * A510F Wi-Fi, step 1: Broadcom BCM43454 on SDIO.
 *
 * Samsung's a5xelte device tree: the chip sits on DW-MMC channel 1
 * (0x13550000, SPI 246, 4-bit, fifo depth 64), pins gpr2-0 clk / gpr2-1 cmd
 * / gpr3-0..3 data (function 2, FSYS pinctrl 0x13750000), WL_REG_ON on
 * gpd1-0 (WLAN_EN, TOP pinctrl 0x139C0000). Clocks (clk-exynos7580.c):
 * aclk_mmc1 = CMU_FSYS EN_ACLK_FSYS0 bit 8, sclk_mmc1_sdclkin = CMU_FSYS
 * EN_SCLK_FSYS bit 6, sclk_fsys_mmc1 = CMU_TOP EN_SCLK_TOP_FSYS bit 1,
 * mux/div CMU_TOP 0x224 / 0x624 (mmc0: 0x220 / 0x620).
 *
 * Step 1 only: clocks on (before any MMC1 register access: a gated block
 * can hang the bus), pins, power the chip, enumerate the SDIO card
 * (CMD5/CMD3/CMD7), read CCCR, enable function 1, request the ALP clock and
 * read the chip id from ChipCommon (backplane 0x18000000) with CMD53.
 * Everything goes to the log as "A510F WIFI:". Nothing else uses the chip.
 * Boot-arg a510fwifi=N: run N seconds after start (unset or 0: off).
 */

#include <pexpert/arm64/board_config.h>

#include <sys/param.h>
#include <sys/systm.h>
#include <sys/errno.h>
#include <kern/clock.h>
#include <kern/thread.h>
#include <kern/locks.h>
#include <kern/sched_prim.h>
#include <machine/machine_routines.h>
#include <pexpert/pexpert.h>

extern vm_offset_t ml_io_map(vm_offset_t, vm_size_t);
extern void IOSleep(unsigned int milliseconds);
extern kern_return_t thread_terminate(thread_t);

void a510f_wifi_start(void);

#define CMU_TOP_PA      0x10010000u
#define CMU_FSYS_PA     0x13730000u
#define PIN_FSYS_PA     0x13750000u     /* gpr2 at +0x40 (clk, cmd), gpr3 at +0x60 (data 0-3) */
#define PIN_TOP_PA      0x139C0000u     /* gpd1 at +0xe0: pin 0 WLAN_EN */
#define MMC1_PA         0x13550000u

#define TOP_MUX_FSYS0   0x220
#define TOP_MUX_FSYS1   0x224
#define TOP_DIV_FSYS0   0x620
#define TOP_DIV_FSYS1   0x624
#define TOP_EN_SCLK_FSYS 0xa00          /* bit 1: sclk_fsys_mmc1_sdclkin */
#define FSYS_EN_ACLK0   0x800           /* bit 8: aclk_mmc1 */
#define FSYS_EN_SCLK    0xa00           /* bit 6: sclk_mmc1_sdclkin */

#define W_CTRL          0x000
#define W_PWREN         0x004
#define W_CLKDIV        0x008
#define W_CLKSRC        0x00c
#define W_CLKENA        0x010
#define W_TMOUT         0x014
#define W_CTYPE         0x018
#define W_BLKSIZ        0x01c
#define W_BYTCNT        0x020
#define W_INTMASK       0x024
#define W_CMDARG        0x028
#define W_CMD           0x02c
#define W_RESP0         0x030
#define W_RINTSTS       0x044
#define W_STATUS        0x048
#define W_FIFOTH        0x04c
#define W_VERID         0x06c
#define W_HCON          0x070
#define W_CLKSEL        0x09c           /* Exynos: sample [2:0], drive [18:16], divider [26:24] */

#define I_RESP_ERR      (1u << 1)
#define I_CMD_DONE      (1u << 2)
#define I_DATA_OVER     (1u << 3)
#define I_RXDR          (1u << 5)
#define I_RCRC          (1u << 6)
#define I_DCRC          (1u << 7)
#define I_RTO           (1u << 8)
#define I_DRTO          (1u << 9)
#define I_HTO           (1u << 10)
#define I_FRUN          (1u << 11)
#define I_HLE           (1u << 12)
#define I_SBE           (1u << 13)
#define I_EBE           (1u << 15)
#define I_CMD_ERR       (I_RESP_ERR | I_RCRC | I_RTO | I_HLE)
#define I_DATA_ERR      (I_DCRC | I_DRTO | I_FRUN | I_SBE | I_EBE)

#define C_START         (1u << 31)
#define C_USE_HOLD      (1u << 29)
#define C_UPD_CLK       (1u << 21)
#define C_SEND_INIT     (1u << 15)
#define C_PRV_WAIT      (1u << 13)
#define C_DAT_EXP       (1u << 9)
#define C_RESP_CRC      (1u << 8)
#define C_RESP_EXP      (1u << 6)

static struct {
	vm_offset_t top, fsys, pfsys, ptop, mmc;
	uint32_t data_off, fifo_bytes;
	int after_s;
} w;

static inline uint32_t
rd(vm_offset_t b, uint32_t o)
{
	return *(volatile uint32_t *)(b + o);
}

static inline void
wr(vm_offset_t b, uint32_t o, uint32_t v)
{
	*(volatile uint32_t *)(b + o) = v;
}

static void
field(vm_offset_t b, uint32_t o, unsigned shift, unsigned width, uint32_t v)
{
	uint32_t m = ((1u << width) - 1u) << shift;
	wr(b, o, (rd(b, o) & ~m) | ((v << shift) & m));
}

static uint64_t
after_ms(uint32_t ms)
{
	uint64_t abs;
	nanoseconds_to_absolutetime((uint64_t)ms * NSEC_PER_MSEC, &abs);
	return mach_absolute_time() + abs;
}

static bool
wait_clear(uint32_t off, uint32_t bits, uint32_t ms)
{
	uint64_t end = after_ms(ms);
	while (rd(w.mmc, off) & bits) {
		if (mach_absolute_time() > end) {
			return false;
		}
	}
	return true;
}

static int
clk_update(void)
{
	wr(w.mmc, W_CMD, C_START | C_UPD_CLK | C_PRV_WAIT);
	return wait_clear(W_CMD, C_START, 100) ? 0 : ETIMEDOUT;
}

/* one command; *resp = RESP0; ETIMEDOUT (no response), EIO (CRC/response error) */
static int
cmd(uint32_t c, uint32_t arg, uint32_t *resp)
{
	wr(w.mmc, W_RINTSTS, I_CMD_DONE | I_CMD_ERR);
	wr(w.mmc, W_CMDARG, arg);
	wr(w.mmc, W_CMD, c | C_START | C_USE_HOLD);
	if (!wait_clear(W_CMD, C_START, 100)) {
		return EBUSY;
	}
	uint64_t end = after_ms(100);
	uint32_t s;
	while (!((s = rd(w.mmc, W_RINTSTS)) & (I_CMD_DONE | I_HLE))) {
		if (mach_absolute_time() > end) {
			return ETIMEDOUT;
		}
	}
	wr(w.mmc, W_RINTSTS, s & (I_CMD_DONE | I_CMD_ERR));
	if (resp != NULL) {
		*resp = rd(w.mmc, W_RESP0);
	}
	if (s & I_RTO) {
		return ETIMEDOUT;
	}
	return (s & I_CMD_ERR) ? EIO : 0;
}

/* CMD52: one byte of function fn at addr (write: data; *out: the byte the card returns) */
static int
cmd52(unsigned fn, uint32_t addr, bool write, uint8_t data, uint8_t *out)
{
	uint32_t arg = (write ? (1u << 31) : 0) | ((fn & 7u) << 28) | ((addr & 0x1ffffu) << 9) | data;
	uint32_t r = 0;
	int e = cmd(52 | C_RESP_EXP | C_RESP_CRC | C_PRV_WAIT, arg, &r);
	if (e == 0 && (((r >> 8) & 0xcbu) != 0)) {
		e = EIO;                                /* R5 flags: CRC, illegal, error, function, range */
	}
	if (out != NULL) {
		*out = (uint8_t)r;
	}
	return e;
}

/* CMD53 byte mode read of n (<= 64) bytes of function fn at addr, incrementing */
static int
cmd53_read(unsigned fn, uint32_t addr, uint8_t *buf, uint32_t n)
{
	if (!wait_clear(W_STATUS, 1u << 9, 100)) {
		return EBUSY;
	}
	wr(w.mmc, W_CTRL, rd(w.mmc, W_CTRL) | 2u);  /* FIFO reset */
	if (!wait_clear(W_CTRL, 2u, 100)) {
		return EBUSY;
	}
	wr(w.mmc, W_RINTSTS, 0xffffffffu);
	wr(w.mmc, W_BLKSIZ, n);
	wr(w.mmc, W_BYTCNT, n);
	uint32_t arg = ((fn & 7u) << 28) | (1u << 26) | ((addr & 0x1ffffu) << 9) | (n & 0x1ffu);
	wr(w.mmc, W_CMDARG, arg);
	wr(w.mmc, W_CMD, 53 | C_RESP_EXP | C_RESP_CRC | C_DAT_EXP | C_PRV_WAIT | C_START | C_USE_HOLD);
	if (!wait_clear(W_CMD, C_START, 100)) {
		return EBUSY;
	}
	uint32_t got = 0, s = 0;
	uint64_t end = after_ms(1000);
	volatile uint8_t *fifo = (volatile uint8_t *)(w.mmc + w.data_off);
	for (;;) {
		s = rd(w.mmc, W_RINTSTS);
		uint32_t cnt = (rd(w.mmc, W_STATUS) >> 17) & 0x1fffu;
		while (cnt-- > 0 && got < n) {
			uint32_t v[2] = {0, 0};
			v[0] = *(volatile uint32_t *)fifo;
			if (w.fifo_bytes == 8) {
				v[1] = *(volatile uint32_t *)(fifo + 4);
			}
			for (uint32_t k = 0; k < w.fifo_bytes && got < n; k++) {
				buf[got++] = ((uint8_t *)v)[k];
			}
		}
		if (s & I_RXDR) {
			wr(w.mmc, W_RINTSTS, I_RXDR);
		}
		if (s & (I_CMD_ERR | I_DATA_ERR)) {
			printf("A510F WIFI: CMD53 fn %u addr 0x%x x%u: rintsts 0x%x, %u bytes, r5 0x%x status 0x%x\n", fn, addr, n, s, got,
			    rd(w.mmc, W_RESP0), rd(w.mmc, W_STATUS));
			return EIO;
		}
		if ((s & I_DATA_OVER) && got >= n) {
			return 0;
		}
		if (mach_absolute_time() > end) {
			printf("A510F WIFI: CMD53 fn %u addr 0x%x x%u timed out: rintsts 0x%x, %u bytes, r5 0x%x status 0x%x\n", fn, addr, n, s,
			    got, rd(w.mmc, W_RESP0), rd(w.mmc, W_STATUS));
			return ETIMEDOUT;
		}
	}
}

static void
wifi_step1(void)
{
	/* 1. clocks: the same source and dividers as mmc0 (S-Boot set those up), gates on */
	printf("A510F WIFI: before: top mux 0x%x/0x%x div 0x%x/0x%x en_sclk_top_fsys 0x%x, fsys en_aclk0 0x%x en_sclk 0x%x, "
	    "gpr2 con 0x%x pud 0x%x drv 0x%x, gpr3 con 0x%x, gpd1 con 0x%x dat 0x%x\n",
	    rd(w.top, TOP_MUX_FSYS0), rd(w.top, TOP_MUX_FSYS1), rd(w.top, TOP_DIV_FSYS0), rd(w.top, TOP_DIV_FSYS1),
	    rd(w.top, TOP_EN_SCLK_FSYS), rd(w.fsys, FSYS_EN_ACLK0), rd(w.fsys, FSYS_EN_SCLK),
	    rd(w.pfsys, 0x40), rd(w.pfsys, 0x48), rd(w.pfsys, 0x4c), rd(w.pfsys, 0x60),
	    rd(w.ptop, 0xe0), rd(w.ptop, 0xe4));
	wr(w.top, TOP_MUX_FSYS1, rd(w.top, TOP_MUX_FSYS0));
	wr(w.top, TOP_DIV_FSYS1, rd(w.top, TOP_DIV_FSYS0));
	field(w.top, TOP_EN_SCLK_FSYS, 1, 1, 1);
	field(w.fsys, FSYS_EN_ACLK0, 8, 1, 1);
	field(w.fsys, FSYS_EN_SCLK, 6, 1, 1);
	IOSleep(2);

	/* 2. pins: SDIO function 2, pull-up on cmd/data, drive strength 3 */
	for (unsigned p = 0; p < 2; p++) {
		field(w.pfsys, 0x40, 4 * p, 4, 2);
		field(w.pfsys, 0x48, 2 * p, 2, p == 0 ? 0 : 3);
		field(w.pfsys, 0x4c, 4 * p, 4, 3);
	}
	for (unsigned p = 0; p < 4; p++) {
		field(w.pfsys, 0x60, 4 * p, 4, 2);
		field(w.pfsys, 0x68, 2 * p, 2, 3);
		field(w.pfsys, 0x6c, 4 * p, 4, 3);
	}

	/* 3. power cycle the chip: WL_REG_ON low, then high (bcmdhd waits ~200 ms) */
	field(w.ptop, 0xe0, 0, 4, 1);
	field(w.ptop, 0xe4, 0, 1, 0);
	IOSleep(20);
	field(w.ptop, 0xe4, 0, 1, 1);
	IOSleep(250);

	/* 4. controller */
	uint32_t verid = rd(w.mmc, W_VERID), hcon = rd(w.mmc, W_HCON);
	w.data_off = (verid & 0xffffu) >= 0x240a ? 0x200 : 0x100;
	w.fifo_bytes = ((hcon >> 7) & 7u) == 2 ? 8 : 4;
	printf("A510F WIFI: mmc1 verid 0x%x hcon 0x%x (fifo %u-byte at +0x%x), ctrl 0x%x clkena 0x%x clksel 0x%x\n",
	    verid, hcon, w.fifo_bytes, w.data_off, rd(w.mmc, W_CTRL), rd(w.mmc, W_CLKENA), rd(w.mmc, W_CLKSEL));
	wr(w.mmc, W_CTRL, rd(w.mmc, W_CTRL) | 7u);
	if (!wait_clear(W_CTRL, 7u, 200)) {
		printf("A510F WIFI: controller reset stuck, ctrl 0x%x\n", rd(w.mmc, W_CTRL));
		return;
	}
	wr(w.mmc, W_PWREN, 1);
	wr(w.mmc, W_INTMASK, 0);
	wr(w.mmc, W_RINTSTS, 0xffffffffu);
	wr(w.mmc, W_TMOUT, 0xffffffffu);
	wr(w.mmc, W_FIFOTH, (2u << 28) | (31u << 16) | 32u);
	wr(w.mmc, W_CTYPE, 0);
	wr(w.mmc, W_CLKSEL, (3u << 24) | 2u);       /* ciu / 4 (samsung,dw-mshc-ciu-div = 3), sample phase 2 */
	wr(w.mmc, W_CLKENA, 0);
	int e1 = clk_update();
	wr(w.mmc, W_CLKDIV, 255);                   /* card clock = ciu / 510: a few hundred kHz */
	wr(w.mmc, W_CLKSRC, 0);
	int e2 = clk_update();
	wr(w.mmc, W_CLKENA, 1);
	int e3 = clk_update();
	printf("A510F WIFI: card clock on (updates %d %d %d)\n", e1, e2, e3);
	IOSleep(10);

	/* 5. SDIO reset (CCCR 6 bit 3; may not answer), 80 clocks + CMD0, then CMD5 */
	(void)cmd52(0, 0x06, true, 0x08, NULL);
	int e0 = cmd(0 | C_SEND_INIT, 0, NULL);
	uint32_t ocr = 0;
	int e5 = cmd(5 | C_RESP_EXP, 0, &ocr);
	printf("A510F WIFI: CMD0 %d, CMD5 %d ocr 0x%x (functions %u)\n", e0, e5, ocr, (ocr >> 28) & 7u);
	if (e5 != 0) {
		printf("A510F WIFI: no SDIO answer: rintsts 0x%x status 0x%x\n", rd(w.mmc, W_RINTSTS), rd(w.mmc, W_STATUS));
		return;
	}
	uint32_t want = (ocr & 0x00ffff00u) != 0 ? (ocr & 0x00300000u ? 0x00300000u : ocr & 0x00ffff00u) : 0x00300000u;
	int tries = 0;
	do {
		e5 = cmd(5 | C_RESP_EXP, want, &ocr);
		if (e5 == 0 && (ocr & (1u << 31))) {
			break;
		}
		IOSleep(10);
	} while (++tries < 100);
	printf("A510F WIFI: CMD5 0x%x: %d ocr 0x%x after %d tries\n", want, e5, ocr, tries);
	if (!(ocr & (1u << 31))) {
		return;
	}
	uint32_t r6 = 0, r1 = 0;
	int e3c = cmd(3 | C_RESP_EXP | C_RESP_CRC, 0, &r6);
	uint32_t rca = r6 >> 16;
	int e7 = cmd(7 | C_RESP_EXP | C_RESP_CRC | C_PRV_WAIT, rca << 16, &r1);
	printf("A510F WIFI: CMD3 %d rca 0x%x, CMD7 %d r1 0x%x\n", e3c, rca, e7, r1);
	if (e3c != 0 || e7 != 0) {
		return;
	}

	/* 6. CCCR */
	uint8_t cccr[20];
	int ecc = 0;
	for (unsigned i = 0; i < 20; i++) {
		cccr[i] = 0;
		ecc |= cmd52(0, i, false, 0, &cccr[i]);
	}
	printf("A510F WIFI: CCCR (%d): %02x %02x %02x %02x %02x %02x %02x %02x  %02x %02x %02x %02x %02x %02x %02x %02x  %02x %02x %02x %02x\n",
	    ecc, cccr[0], cccr[1], cccr[2], cccr[3], cccr[4], cccr[5], cccr[6], cccr[7], cccr[8], cccr[9], cccr[10], cccr[11],
	    cccr[12], cccr[13], cccr[14], cccr[15], cccr[16], cccr[17], cccr[18], cccr[19]);

	/* 7. CIS (function 0): manufacturer / card id tuple (0x20), with CMD52 only */
	{
		uint32_t cis = (uint32_t)cccr[9] | ((uint32_t)cccr[10] << 8) | ((uint32_t)cccr[11] << 16);
		uint32_t a = cis;
		for (int t = 0; t < 32 && a < cis + 512; t++) {
			uint8_t code = 0, link = 0;
			if (cmd52(0, a, false, 0, &code) != 0 || code == 0xff) {
				break;
			}
			(void)cmd52(0, a + 1, false, 0, &link);
			if (code == 0x20 && link >= 4) {
				uint8_t m[4] = {0, 0, 0, 0};
				for (unsigned b = 0; b < 4; b++) {
					(void)cmd52(0, a + 2 + b, false, 0, &m[b]);
				}
				printf("A510F WIFI: CIS at 0x%x: manufacturer 0x%02x%02x, card 0x%02x%02x\n", cis, m[1], m[0], m[3], m[2]);
			}
			a += 2u + link;
		}
	}

	/* 8. function 1 on, block size 64 */
	(void)cmd52(0, 0x02, true, 0x02, NULL);
	uint8_t rdy = 0;
	tries = 0;
	do {
		(void)cmd52(0, 0x03, false, 0, &rdy);
		if (rdy & 0x02) {
			break;
		}
		IOSleep(10);
	} while (++tries < 100);
	(void)cmd52(0, 0x110, true, 64, NULL);
	(void)cmd52(0, 0x111, true, 0, NULL);
	printf("A510F WIFI: function 1 ready 0x%x after %d tries\n", rdy, tries);
	if (!(rdy & 0x02)) {
		return;
	}

	/* 9. backplane: ALP clock (CHIPCLKCSR 0x1000e: FORCE_HW_CLKREQ_OFF | ALP_AVAIL_REQ, wait ALP_AVAIL 0x40) */
	(void)cmd52(1, 0x1000e, true, 0x28, NULL);
	uint8_t csr = 0;
	tries = 0;
	do {
		(void)cmd52(1, 0x1000e, false, 0, &csr);
		if (csr & 0x40) {
			break;
		}
		IOSleep(1);
	} while (++tries < 200);
	/* keep ALP forced (brcmfmac: FORCE_HW_CLKREQ_OFF | FORCE_ALP); 0x20 alone dropped it and the backplane hung */
	(void)cmd52(1, 0x1000e, true, 0x21, NULL);
	printf("A510F WIFI: chip clock csr 0x%x after %d ms\n", csr, tries);

	/* 10. ChipCommon chip id: window 0x18000000 (SBADDR low/mid/high), 4-byte access at +0x8000 */
	(void)cmd52(1, 0x1000a, true, 0x00, NULL);
	(void)cmd52(1, 0x1000b, true, 0x00, NULL);
	(void)cmd52(1, 0x1000c, true, 0x18, NULL);
	/* 10a. the chip id byte by byte (CMD52 into the window, no 4-byte flag) */
	uint8_t cb[4] = {0, 0, 0, 0};
	int e52 = 0;
	for (unsigned b = 0; b < 4; b++) {
		e52 |= cmd52(1, b, false, 0, &cb[b]);
	}
	uint32_t v = (uint32_t)cb[0] | ((uint32_t)cb[1] << 8) | ((uint32_t)cb[2] << 16) | ((uint32_t)cb[3] << 24);
	printf("A510F WIFI: chipid by CMD52 (%d) 0x%08x: chip 0x%x (%u) rev %u, package %u, %u cores\n",
	    e52, v, v & 0xffffu, v & 0xffffu, (v >> 16) & 0xfu, (v >> 20) & 0xfu, (v >> 24) & 0xfu);
	/* 10b. the same with CMD53 (4 bytes, 4-byte access flag), 1-bit bus */
	uint8_t id[4] = {0, 0, 0, 0};
	int eid = cmd53_read(1, 0x8000, id, 4);
	v = (uint32_t)id[0] | ((uint32_t)id[1] << 8) | ((uint32_t)id[2] << 16) | ((uint32_t)id[3] << 24);
	printf("A510F WIFI: chipid by CMD53, 1-bit (%d) 0x%08x\n", eid, v);

	/* 11. 4-bit bus, then CMD53 again */
	uint8_t bic = 0;
	if (cmd52(0, 0x07, false, 0, &bic) == 0 && cmd52(0, 0x07, true, (uint8_t)((bic & ~3u) | 2u), NULL) == 0) {
		wr(w.mmc, W_CTYPE, 1);
	}
	uint8_t chk = 0;
	int ebw = cmd52(0, 0x07, false, 0, &chk);
	printf("A510F WIFI: bus interface 0x%x -> 0x%x (%d), 4-bit\n", bic, chk, ebw);
	id[0] = id[1] = id[2] = id[3] = 0;
	eid = cmd53_read(1, 0x8000, id, 4);
	v = (uint32_t)id[0] | ((uint32_t)id[1] << 8) | ((uint32_t)id[2] << 16) | ((uint32_t)id[3] << 24);
	printf("A510F WIFI: chipid by CMD53, 4-bit (%d) 0x%08x\n", eid, v);
	printf("A510F WIFI: step 1 done\n");
}

static void
wifi_thread(__unused void *arg, __unused wait_result_t wr_)
{
	IOSleep((unsigned)w.after_s * 1000u);
	printf("A510F WIFI: step 1 (SDIO bring-up, chip id) at %d s\n", w.after_s);
	wifi_step1();
	thread_terminate(current_thread());
}

void
a510f_wifi_start(void)
{
	w.after_s = 0;
	PE_parse_boot_argn("a510fwifi", &w.after_s, sizeof(w.after_s));
	if (w.after_s <= 0) {
		return;
	}
	w.top = ml_io_map(CMU_TOP_PA, 0x1000);
	w.fsys = ml_io_map(CMU_FSYS_PA, 0x1000);
	w.pfsys = ml_io_map(PIN_FSYS_PA, 0x1000);
	w.ptop = ml_io_map(PIN_TOP_PA, 0x1000);
	w.mmc = ml_io_map(MMC1_PA, 0x2000);
	thread_t th;
	if (kernel_thread_start(wifi_thread, NULL, &th) == KERN_SUCCESS) {
		thread_deallocate(th);
	}
}
