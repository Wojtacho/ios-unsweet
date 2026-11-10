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

Power-off: the phone switched itself off ~60 s after the rows appeared, so
the probe ran to the end (PSCI SYSTEM_OFF or the PS_HOLD fallback; not
distinguished).

## 2026-11-10: iOS 16 instruction scan (run 42790485292, commit 776368e)

`a510f-isa-scan` workflow, `a510f/tools/dsc_isa_scan.py`: iPhone X iOS
16.7.16 (20H392) main dyld shared cache from the SystemOS cryptex
(`087-86593-047.dmg`), code sections only, exact encodings.

| | count |
|---|---|
| images scanned | 2647 |
| instructions | 387,147,500 |
| LL/SC exclusives (ARMv8.0 atomics) | 823,085 |
| **LSE atomics** | **990** in 21 images (CAS 346, CASP 15, LD*/SWP 629) |
| FP16 arithmetic | 1530 (1417 in libBNNS, 74 in ActionKit) |
| RDMA (SQRDMLAH/SH) | 50 (33 in ActionKit) |
| LDAPR | 1 |
| DC CVAP | 0 |

LSE by image: libdispatch 697, libsystem_pthread 86, libsystem_platform 81,
ActionKit 73, libsystem_malloc 20, the rest 1-6 each (libsystem_m,
libSparse, MediaToolbox, AudioCodecs, corecrypto, MobileGestalt, dyld, ...).

Reading:
- The compiler baseline for this userland is ARMv8.0: libobjc, libswiftCore,
  Foundation, CoreFoundation, UIKitCore, libc++ and JavaScriptCore have
  **zero** LSE and use LL/SC throughout.
- LSE sits only in the hand-tuned atomics of libdispatch / pthread /
  platform / malloc, which also carry LL/SC paths. Guess (to verify in xnu
  `cpu_capabilities.h` and libplatform): these pick LSE at run time from a
  commpage capability bit the kernel sets from ID_AA64ISAR0. On the A53 that
  bit stays clear and the LL/SC paths run, at no cost.
- Whatever still executes LSE/FP16/RDMA can be trapped (undefined
  instruction) and emulated in the kernel. Only niche code (Shortcuts'
  ActionKit, BNNS neural-net kernels) has more than a handful of sites.
- Conclusion: **atomics are not a blocker.** The 16 KB page granule is now
  the main open problem.

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
