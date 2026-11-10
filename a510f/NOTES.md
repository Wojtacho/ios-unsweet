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

## 2026-11-10: 4 KB pages in xnu-8796 (source study, xnu-8796.141.3)

Finding: **xnu-8796 still carries a 4 KB-page arm64 configuration**, and it
is for a Cortex-A53: `MACHINE_CONFIG=BCM2837` (Raspberry Pi 3).

- `makedefs/MakeInc.def`: `SUPPORTED_ARM64_MACHINE_CONFIGS = BCM2837 T6000
  T8101 T8103 VMAPPLE`; `MACHINE_FLAGS_ARM64_BCM2837 = -DARM64_BOARD_CONFIG_BCM2837`
  (no `-mcpu`, i.e. plain ARMv8.0).
- `pexpert/pexpert/arm64/BCM2837.h` defines `__ARM_ARCH__ 8`,
  `__ARM_VMSA__ 8`, `__ARM64_PMAP_SUBPAGE_L1__ 1`, `NO_MONITOR`, and **no
  `__ARM_16K_PG__`** (H13.h and VMAPPLE.h define it). sweet's patch 0004
  defines it for SWEET.
- Without `__ARM_16K_PG__`: `ARM_PGSHIFT 12` (proc_reg.h) and
  `PAGE_SHIFT_CONST 12` (mach/arm/vm_param.h), so the VM, pmap and user
  `vm_page_size` are all 4 KB. The pmap, TLB and proc_reg code keep full
  `#else` 4 KB branches (4K L0-L3 table geometry).
- Shared cache sliding is page-size independent: `PAGE_SIZE_FOR_SR_SLIDE`
  is 4096 everywhere (vm_shared_region.h), so the iOS 16 cache's slide info
  is usable.

Atomics, confirmed in the kernel source:
- `osfmk/arm/commpage/commpage.c` sets `kHasFeatLSE` (= `kHasARMv81Atomics`)
  only when `ID_AA64ISAR0_EL1.Atomic >= 8.1`; RDM and FP16 bits likewise come
  from the ID registers. On the A53 they stay clear, so libdispatch,
  pthread, platform and malloc take their LL/SC paths.
- The only explicit LSE in the kernel (`casa` in
  `hw_lck_ticket_reserve_orig_allow_invalid`, machine_routines_asm.s) is
  under `#if defined(__ARM_ARCH_8_2__)`. sweet builds with
  `-march=armv8.2-a+crypto`; an A510F config must use `-march=armv8-a+crc+crypto`
  so neither this nor compiler-generated atomics use LSE.

sweet patches that assume 16 KB (from grepping `xnu/patches`):
- 0004 (machine config: defines `__ARM_16K_PG__`): new A510F config instead.
- 0010 (early framebuffer block mapping assumes the 16K bootstrap table
  layout, `+ 2*PGBYTES`, 32 MB L2 block): rewrite for 4K (2 MB L2 blocks).
- 0011 (physmap padding) is written in `ARM_TT_*` terms: should follow.
- Other hits (0028 `DMA_BOUNCE 0x4000`, 0046, 0058, 0060, 0073) are buffer
  or MMIO sizes, not page-size assumptions.

Risks still open (cannot be settled from source):
- iOS 16 userland never shipped on 4 KB-page hardware (the last 4 KB arm64
  iOS was iOS 12 on A7/A8). Code that reads `vm_page_size` adapts; anything
  hard-coding 16 KB will show up only at run time.
- Whether the BCM2837 config still builds cleanly with this toolchain.
  Apple's open-source releases do list it; nothing here shows it booting.

Verdict: 16 KB pages are **not a blocker in principle**. The kernel side is a
supported configuration; the work is a new A510F machine config modelled on
BCM2837 plus porting sweet's SWEET-specific patches to it.

## 2026-11-10: first 4 KB / Cortex-A53 kernel build (a510f-xnu run 42803068442, commit 7a9c842)

Result: `kernel.development.sweet`, 17,203,280 bytes, Mach-O arm64,
sha256 d355129c9203d687...; the Linux `isa-check` job found **no
A53-incompatible instructions** in 2,290,622 instructions (2,271 LL/SC
exclusives; the one LSE-shaped word is the SHA-256 `K256` table in
`__hib_text`, data).

How it is built (`.github/workflows/a510f-xnu.yml`):
- sweet's 77 patches + `a510f/xnu/make-a510f-variant.sh` on the copied 0004:
  no `__ARM_16K_PG__`, `__ARM64_PMAP_SUBPAGE_L1__` instead of
  `__ARM_PAN_AVAILABLE__`, `-mcpu=cortex-a53`. Machine config name stays
  SWEET, so the board code is still sweet's (GICv3, UFS, Goodix...).
- `a510f/xnu/patches/0100`: 4K commpage nesting static_assert skipped on
  macOS-platform builds (the 1GB nesting region is reserved by the VM, as
  the 16K branch documents). The only compile error of the 4 KB build.
- `a510f/xnu/patches/0101`: commpage PFZ FIFO trylocks (user-visible
  OSAtomicFifoEnqueue/Dequeue) use LDAXR/STXR when `__ARM_FEATURE_ATOMICS`
  is off; they were unconditional `casa`.
- `a510f/xnu/patch-dxb-build.sh`: libfirehose_kernel is built by xcodebuild
  outside xnu's makefiles; build only its arm64 slice with
  `-mcpu=cortex-a53`.
- Runner: `macos-15-intel`. macos-14 is retired; arm64 macOS runners
  repeatedly never picked the job up. Xcode 16.0 builds xnu-8796 here
  (sweet chose macos-14 for Xcode 15's iig; not needed so far).

Lessons (observed, with run ids in git log):
- `-march=armv8-a` alone left Apple clang's default CPU (apple-m1) in
  charge: 875 LSE + 209 LDAPR in the kernel. Use `-mcpu`.
- Run logs need a GitHub login; workflows publish errors as annotations,
  readable via the check-runs API or the run page.

## 2026-11-10: first xnu boot on the A510F (a510f-xnu run 42807157271, commit ab07160)

Image: `a510f-xnu-recovery.tar` (shim 77,824 B + SWEETXNU payload
16,493,360 B), flashed to RECOVERY with Odin, booted straight from download
mode into recovery. Kernel cmdline `debug=0xc serial=3 cpus=1 keepsyms=1
-enable_kprintf_spam`.

Observed (photo):
- Shim red screen: payload found, `VIRT FFFFFFF006000000`, `ENTRY
  FFFFFFF007428488`, `SEGS n=0A end=724AC000`, `BOOTARG pa=724B0000
  top=724B4000`, `JUMP 71428488`. The DECON/CPU1 lines had scrolled away.
- Stage-0 white band, then green stage bands: xnu's first instruction ran.
- `SWEET EARLY 1` .. `7`: arm_init with the 4K MMU on, PE_init_platform
  (ADT), ml_parse_cpu_topology (8 A53 MPIDRs), cpu_bootstrap,
  kernel_startup_bootstrap, cpu_init, entering arm_vm_init.
- The display kept updating after the jump: the CPU1 DECON refresher works.
- `SWEET EARLY PANIC: arm_vm_init.c:1843 Assertion failed: (l1 &
  (ARM_TTE_VALID | ARM_TTE_TYPE_MASK)) == (ARM_TTE_VALID |
  ARM_TTE_TYPE_TABLE)` in sweet_early_map_final: without ARM_LARGE_MEMORY
  no L2 table exists at VM_MIN_KERNEL_ADDRESS for the early-console alias.

Fix (commit 270f478, patch 0102): allocate that L2 table with alloc_ptpage
when the L1 entry is empty; clear the alias blocks when the early console is
disabled after kprintf startup.

## 2026-11-10: second boot (a510f-xnu run 42809529936, commit 270f478)

Observed (photo): the early console ran through arm_vm_init and was
replaced by the normal framebuffer console, i.e. stages 8-20 passed:
`kprintf initialized`, `Serial mode specified: 00000003`,
`initialize_screen: b=67000000, w=00000438, h=00000780, r=000010E0, d=0`,
`pe_arm_init_interrupts`, `pe_arm_map_interrupt_controller: failed to find
the interrupt-controller` (message only), `pe_arm_init_debug: failed to find
cpu-debug-interface`, `SWEET GIC: virtual timer INTID 27`, then
`panic(cpu 0 caller 0xfffffff007b19748): find_gicr_pe_base: cannot find GICR
base for core 0 @pe_fiq.c:73` and nested panics ending in "Nested panic
stall. Stage 2 bailout" (spins; screen stays on).

Also observed: after this image ran, Vol Down + Power and the download-mode
"cancel" restart both came back into recovery (our image), not Android. Way
out used: download mode (Vol Down + Home + Power, then Vol Up), charging.

Fix (commit bc2409f, patch 0103): GIC-400 (GICv2) through GICD/GICC MMIO
(per-CPU init, IRQ ack/EOI, SGIs via GICD_SGIR) and power-off 60 s after a
panic (PSCI SYSTEM_OFF, then PS_HOLD).

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
