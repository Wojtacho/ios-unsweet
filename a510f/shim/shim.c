/*
 * SM-A510F (Exynos 7580) boot shim: S-Boot -> xnu.
 *
 * S-Boot starts this like an arm64 Linux kernel (EL1, MMU off, x0 = DTB).
 * Then:
 *   1. CPU1 is started (PSCI CPU_ON) as a display refresher: the S6E3FA3
 *      panel runs in MIPI command mode, so DECON only sends a frame to it
 *      when triggered. CPU1 re-arms the trigger every ~16 ms forever, from
 *      this image's memory, which lies below the kernel's RAM. xnu boots
 *      with cpus=1 and never touches CPU1.
 *   2. loader.c (from sweet, unchanged logic) finds the SWEETXNU payload in
 *      the ramdisk, copies xnu to its physical address, writes the ADT and
 *      boot_args and jumps to it with the MMU off.
 * On failure the reason stays on screen and the phone powers off after 60 s.
 */
#include <stdint.h>
#include "console.h"
#include "loader.h"
#include "fdt.h"

#define DECON_BASE		0x14830000UL
#define DECON_WINCON0		(DECON_BASE + 0x0050)
#define DECON_ADD0_W0		(DECON_BASE + 0x0880)
#define DECON_TRIGCON		(DECON_BASE + 0x06B0)
#define DECON_UPDATE		(DECON_BASE + 0x0710)	/* regs-decon.h (decon_7580) */
#define UPDATE_STANDALONE_F	(1u << 0)
#define DECON_SHADOWCON		(DECON_BASE + 0x0030)
#define SHADOWCON_WIN0_PROTECT	(1u << 8)
#define TRIG_SWTRIGEN		(1u << 0)
#define TRIG_SWTRIGCMD		(1u << 1)
#define TRIG_HWTRIGEN		(1u << 3)
#define TRIG_HWTRIGMASK		(1u << 4)

#define PMU_PS_HOLD_CONTROL	0x1046330CUL
#define PS_HOLD_OUTPUT_HIGH	(1u << 8)

#define PSCI_CPU_ON64		0xC4000003UL
#define PSCI_SYSTEM_OFF		0x84000008UL

#define rsr(r) ({ uint64_t _v; __asm__ volatile("mrs %0, " r : "=r"(_v)); _v; })

static inline uint32_t rd32(uintptr_t a) { return *(volatile uint32_t *)a; }
static inline void wr32(uintptr_t a, uint32_t v) { *(volatile uint32_t *)a = v; }

extern char secondary_entry[];

static volatile uint64_t refresher_alive;
static const char *stage;	/* set at runtime: no absolute pointers in data */

static uint64_t smc(uint64_t fn, uint64_t a1, uint64_t a2, uint64_t a3)
{
	register uint64_t x0 __asm__("x0") = fn;
	register uint64_t x1 __asm__("x1") = a1;
	register uint64_t x2 __asm__("x2") = a2;
	register uint64_t x3 __asm__("x3") = a3;
	__asm__ volatile("smc #0"
			 : "+r"(x0), "+r"(x1), "+r"(x2), "+r"(x3)
			 :
			 : "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11",
			   "x12", "x13", "x14", "x15", "x16", "x17", "memory");
	return x0;
}

static uint64_t now(void)
{
	__asm__ volatile("isb");
	return rsr("cntvct_el0");
}

static uint64_t ticks_per_ms(void)
{
	uint64_t f = rsr("cntfrq_el0") & 0xffffffff;
	return (f ? f : 26000000) / 1000;	/* exynos7580.dtsi: 26 MHz */
}

static void delay_ms(uint64_t ms)
{
	uint64_t end = now() + ticks_per_ms() * ms;
	while (now() < end)
		;
}

static void __attribute__((noreturn)) power_off(void)
{
	smc(PSCI_SYSTEM_OFF, 0, 0, 0);
	wr32(PMU_PS_HOLD_CONTROL, rd32(PMU_PS_HOLD_CONTROL) & ~PS_HOLD_OUTPUT_HIGH);
	for (;;)
		__asm__ volatile("wfe");
}

/* Ask DECON for one more frame (same as the probe, which worked). */
static void decon_kick(void)
{
	uint32_t t = rd32(DECON_TRIGCON);
	if (t & TRIG_SWTRIGEN)
		wr32(DECON_TRIGCON, t | TRIG_SWTRIGCMD);
	else if (t & TRIG_HWTRIGEN)
		wr32(DECON_TRIGCON, t | TRIG_HWTRIGMASK);
}

/*
 * Move DECON window 0 from S-Boot's buffer (FB_SBOOT, mid-RAM) to FB_BASE:
 * copy the splash (MMU off: 8-byte words), set the window's start address
 * (VIDW_ADD0, the only buffer register: size and offsets stay) and request
 * a standalone shadow update, which DECON applies at the next frame and then
 * clears. Returns 0 when the new address is live.
 */
static int fb_move(void)
{
	if (rd32(DECON_ADD0_W0) != FB_SBOOT)
		return -1;
	volatile uint64_t *d = (volatile uint64_t *)FB_BASE;
	volatile const uint64_t *s = (volatile const uint64_t *)FB_SBOOT;
	for (uint64_t i = 0; i < (uint64_t)FB_H * FB_STRIDE / 8; i++)
		d[i] = s[i];
	__asm__ volatile("dsb sy" ::: "memory");
	/* Linux (decon_reg_7580.c): protect, write, unprotect, standalone update. */
	wr32(DECON_SHADOWCON, rd32(DECON_SHADOWCON) | SHADOWCON_WIN0_PROTECT);
	wr32(DECON_ADD0_W0, (uint32_t)FB_BASE);
	wr32(DECON_SHADOWCON, rd32(DECON_SHADOWCON) & ~SHADOWCON_WIN0_PROTECT);
	wr32(DECON_UPDATE, rd32(DECON_UPDATE) | UPDATE_STANDALONE_F);
	for (int i = 0; i < 60; i++) {
		decon_kick();
		delay_ms(17);
		if (!(rd32(DECON_UPDATE) & UPDATE_STANDALONE_F))
			return 0;
	}
	/* Not applied: back to S-Boot's buffer, nothing boots with this layout. */
	wr32(DECON_ADD0_W0, (uint32_t)FB_SBOOT);
	wr32(DECON_UPDATE, rd32(DECON_UPDATE) | UPDATE_STANDALONE_F);
	return -2;
}

/* ---- CPU1: display refresher ---- */

void secondary_main(uint64_t idx)
{
	(void)idx;
	refresher_alive = 1;
	__asm__ volatile("dsb sy" ::: "memory");
	for (;;) {
		decon_kick();
		delay_ms(16);
	}
}

/* ---- exceptions on CPU0 before xnu ---- */

void exc_handler(uint64_t slot, uint64_t *regs)
{
	con_clear(BLUE);
	con_str("PANIC", "shim exception");
	con_hex2("SLOT", "n=", slot, "cpu=", rsr("mpidr_el1"));
	con_str("STAGE", stage);
	con_hex("ESR", rsr("esr_el1"));
	con_hex("ELR", rsr("elr_el1"));
	con_hex("FAR", rsr("far_el1"));
	con_hex("X0", regs[0]);
	delay_ms(60000);
	power_off();
}

void shim_main(uint64_t dtb)
{
	stage = "start";
	decon_kick();
	/* Draw on S-Boot's buffer first: visible whatever happens to the move. */
	con_fb = (volatile uint32_t *)FB_SBOOT;
	con_clear(RED);
	con_str("SHIM", "a510f: S-Boot -> xnu loader");
	con_skip();

	uint32_t wincon = rd32(DECON_WINCON0), add0 = rd32(DECON_ADD0_W0);
	con_hex2("DECON", "win0=", wincon, "add0=", add0);
	con_hex2("DECON2", "shadow=", rd32(DECON_SHADOWCON), "upd=", rd32(DECON_UPDATE));
	con_hex2("DECON3", "trig=", rd32(DECON_TRIGCON), "fbnew=", (uint32_t)FB_BASE);
	con_hex2("DTB", "at=", dtb, "mpidr=", rsr("mpidr_el1"));
	uint64_t rd_s = 0, rd_e = 0;
	fdt_chosen_u64(dtb, "linux,initrd-start", &rd_s);
	fdt_chosen_u64(dtb, "linux,initrd-end", &rd_e);
	con_hex2("INITRD", "lo=", (uint32_t)rd_s, "hi=", (uint32_t)rd_e);

	stage = "refresher";
	uint64_t self = rsr("mpidr_el1") & 0xffff;
	uint64_t target = (self & 0xff00) | ((self & 0xff) == 1 ? 0 : 1);
	uint64_t rc = smc(PSCI_CPU_ON64, target, (uintptr_t)secondary_entry, 1);
	for (int i = 0; i < 100 && !refresher_alive; i++)
		delay_ms(1);
	con_hex2("CPU1", "on=", (uint32_t)rc, "alive=", (uint32_t)refresher_alive);
	if (!refresher_alive)
		con_str("WARN", "no refresher: screen may freeze");

	stage = "fbmove";
	con_str("FBMOVE", "moving the framebuffer to low RAM...");
	int moved = fb_move();
	if (moved != 0) {
		con_hex2("FBMOVE", "FAILED rc=", (uint32_t)moved, "upd=", rd32(DECON_UPDATE));
		con_hex2("FBMOVE", "add0=", rd32(DECON_ADD0_W0), "shadow=", rd32(DECON_SHADOWCON));
		con_str("OFF", "not booting (RAM layout needs the move); off in 60 s");
		delay_ms(60000);
		power_off();
	}
	con_fb = (volatile uint32_t *)FB_BASE;	/* the copy already shows the lines above */
	con_hex2("FBMOVE", "ok add0=", rd32(DECON_ADD0_W0), "upd=", rd32(DECON_UPDATE));
	con_str("WAIT", "8 s for a photo");
	delay_ms(8000);
	con_skip();

	stage = "loader";
	const char *why = loader_boot(dtb);
	con_str("LOADER", why);
	con_str("OFF", "power off in 60 s");
	delay_ms(60000);
	power_off();
}
