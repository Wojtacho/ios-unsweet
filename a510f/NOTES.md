# SM-A510F port: engineering log

## 2026-11-10: probe run 1 (commit 9217ddc, Actions run 42782171816)

Device: SM-A510F, firmware A510FXXS8CSF3 (Android 7.0), hw_rev 4
(running DT reports `model_info-hw_rev` 3, matched by the 3-7 dt.img entry).

Flashed `a510f-probe-recovery.tar` to RECOVERY with Odin 3.13.3 (Auto Reboot
off). First attempt was lost: Android booted before recovery and the stock
`install-recovery` restored Samsung recovery. Second attempt, going straight
from download mode to recovery (Vol Down+Home+Power, then swap Vol Down for
Vol Up), ran the probe and drew all 13 rows.

Decoded from a photo of the screen:

| Row | Value | Meaning |
|---|---|---|
| 0 alive | `0xFFFFFFFF` | S-Boot runs our arm64 Image; display works |
| 1 EL | `0x00000001` | entered at **EL1** (no EL2 access) |
| 2 PSCI_VERSION | `0xFFFFFFFF` | NOT_SUPPORTED, no fault: PSCI 0.1-style firmware (IDs from DT) |
| 3 CPU_ON | `0x00000000` | SUCCESS with 0xC4000003 |
| 4 2nd core | `0xC0DE0001` | second A53 came up at EL1 and ran our code |
| 5 ID_AA64ISAR0 | `0x00011120` | AES+PMULL, SHA1, SHA2, CRC32; **Atomic = 0 (no LSE)** |
| 6 ID_AA64MMFR0 | `0x00001122` | 40-bit PA, 16-bit ASID; **TGran16 = 0 (no 16 KB pages)**; 4K and 64K OK |
| 7 MIDR | `0x410FD033` | Cortex-A53 r0p3 |
| 8 exceptions | `0x00000000` | none taken |
| 9 load address | `0x40205000` (photo read, low confidence on bits 15:12) | where S-Boot placed the Image |
| 10 DTB | `0x48000000` | x0 at entry |
| 11 framebuffer | `0x67000000` | DECON window 0 buffer left by S-Boot |
| 12 display | win 0, fmt 0 (ARGB8888), TRIGCON `0x0088` | HW (TE) trigger mode; unmasking HWTRIGMASK refreshes the panel |

Observations vs. guesses:
- Observed: 64-bit boot, EL1, SMP bring-up via PSCI CPU_ON, framebuffer
  console via S-Boot's DECON setup. These are enough for an XNU bring-up shim.
- Observed: no LSE atomics, no 16 KB granule. Hardware facts, not fixable.
- Guess: PSCI SYSTEM_OFF is likely unsupported too (PSCI_VERSION is).
  Power-off timing not yet reported.

## Open problems before XNU work

1. **16 KB pages.** XNU arm64 builds its kernel pmap on a 16 KB granule.
   xnu-8796 has 4 KB page-table attributes (`pmap_pt_attr_4k`, used for
   Rosetta processes on Apple silicon); the port needs the kernel's native
   attributes switched to 4 KB. iOS binaries are 16 KB aligned, which is also
   4 KB aligned.
2. **LSE atomics.** Check whether the iPhone X iOS 16.7 dyld_shared_cache
   uses CAS/LDADD/SWP etc. If it does, trap and emulate them in the kernel
   (undefined-instruction handler), at a speed cost.
3. eMMC driver (DW-MMC), GICv2, Exynos HS-I2C touch, S2MPU05 PMIC: new
   drivers compared to sweet.
