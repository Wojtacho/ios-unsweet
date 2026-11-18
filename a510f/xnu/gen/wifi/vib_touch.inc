/*
 * A510F vibration motor (Samsung sec_vib): an ERM motor on S2MPU03 LDO34
 * (register 0x4F, "VDD_MOTOR_3P3", board revisions 3-7). a510f_vibrate(ms)
 * asks for a buzz (at most 2 s); the touch thread, which owns the PMIC bus,
 * switches the LDO on (0xFC: [7:6]=11 on, 0x3C = 3.3 V, as LDO33) and off
 * again. A 150 ms buzz when touch polling starts tests the motor at boot.
 * Boot-arg a510fvib=0: off.
 */
#define PMIC_REG_L34    0x4F
#define PMIC_L34_ON     0xFC

void a510f_vibrate(uint32_t ms);

static volatile uint64_t vib_until;
static bool vib_on;

void
a510f_vibrate(uint32_t ms)
{
	uint64_t abs = 0;
	if (ms > 2000) {
		ms = 2000;
	}
	nanoseconds_to_absolutetime((uint64_t)ms * NSEC_PER_MSEC, &abs);
	vib_until = mach_absolute_time() + abs;
}

static void
vib_poll(void)
{
	static int enabled = -1;
	if (enabled < 0) {
		int v = 1;
		PE_parse_boot_argn("a510fvib", &v, sizeof(v));
		enabled = v != 0;
		if (enabled) {
			a510f_vibrate(150);     /* motor test: a short buzz as touch polling starts */
		}
	}
	if (!enabled) {
		return;
	}
	bool want = mach_absolute_time() < vib_until;
	if (want == vib_on) {
		return;
	}
	uint8_t v = 0;
	if (pmic_read(PMIC_REG_L34, &v) != 0) {
		return;
	}
	uint8_t nv = want ? (uint8_t)PMIC_L34_ON : (uint8_t)(v & 0x3F);
	if (pmic_write(PMIC_REG_L34, nv) == 0) {
		static unsigned told;
		vib_on = want;
		if (told++ < 6) {
			printf("A510F VIB: motor %s (L34 0x%x -> 0x%x)\n", want ? "on" : "off", v, nv);
		}
	}
}

