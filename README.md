# ios-unsweet

**Apple's iOS 16 running on a Samsung Galaxy A5 2016 (SM-A510F).**

This project ports Apple's open-source XNU kernel (xnu-8796, the iOS 16 generation) to the Galaxy A5 2016 (`SM-A510F`, codename `a5xelte`, Samsung Exynos 7580, 8× Cortex-A53, 2 GB RAM). On top of it runs the **unmodified iOS 16.7.16 (20H392) userland of the iPhone 8 Plus**: launchd, the system daemons, backboardd, SpringBoard and the stock apps.

It is a fork of [dipa-studio/ios-sweet](https://github.com/dipa-studio/ios-sweet), which first brought this kernel up on a Redmi Note 10 Pro. The GPU work follows [joranv1/ios-sailfish](https://github.com/joranv1/ios-sailfish) (Pixel 1).

> Experimental, not a usable phone OS. Many things are missing or stubbed, and Apple's security model is mostly switched off. The iOS root replaces Android: it is written over the `SYSTEM`..`USERDATA` partitions, so **Android and its data are erased**.

## Status (2026-11-14)

- Boots to the lock screen in about **1 minute 20 seconds** (Apple logo at ~0:40) and is usable at ~1:30.
- Lock screen, home screen, Control Center, notification center, Settings, **widgets**, wallpapers, and 28 stock apps.
- Touchscreen, power / volume / Home buttons, **real battery percentage and charging state**.
- **GPU: kernel driver working.** The Mali-T720 powers up, runs jobs through its own MMU and has drawn its first image (all 4096 test pixels correct). Mesa's panfrost GL driver now builds as an iOS library (`sweetgl.dylib`); hooking it into CoreAnimation is in progress. Until then everything is drawn by the CPU.

## What works

| Area | State |
| --- | --- |
| Boot | Samsung S-Boot (stock, OEM unlocked) → our 64-bit shim in the `BOOT` partition → XNU. TWRP stays in `RECOVERY` for logs and root writes |
| CPU | 7 of the 8 Cortex-A53 cores via PSCI at 1.2 GHz; core 1 keeps the command-mode panel refreshed. 4 KB hardware pages under XNU's 16 KB VM pages, GIC-400 (GICv2) interrupts, timers |
| Memory | 1.7 GB of the 2 GB (`0x44000000`–`0xaec00000`) |
| Storage | Own DW-MMC eMMC driver with 64-bit IDMAC DMA (~63 MB/s); the iOS root is a journaled HFS+ volume over `SYSTEM`..`USERDATA` (14.4 GiB), read/write |
| iOS userland | Real iPhone 8 Plus 16.7.16 root filesystem, cryptexes and shared cache. The A11 userland runs on ARMv8.0 Cortex-A53 cores |
| Display | Kernel IOSurface + IOMobileFramebuffer services; iOS sees an iPhone 8 Plus panel (1242×2208), scaled to the 1080×1920 S6E3FA3 AMOLED and pushed through DECON in MIPI command mode |
| GPU | Mali-T720 MP2 (Midgard): power domain, clocks, soft reset, LPAE page tables, job submission, buffer objects and IOSurface import for user space (`SweetMali`). Mesa panfrost GLES library built, not yet in use |
| Touch | Touchscreen over I²C, HID digitizer events |
| Buttons | Power, volume up/down, Home as HID keys |
| Battery | SM5705 fuel gauge: percentage, voltage, current, temperature; charging inferred from the current |
| Device identity | iPhone 8 Plus, Home-button UI |
| Activation | mobileactivationd's own "Hactivation" path, chosen through device-tree security status. No Apple servers involved |

## What does not work (yet)

- **No GPU rendering yet**: CoreAnimation draws on the CPU, and the panel is updated 10 times a second, so animations are slow.
- **No Wi-Fi, Bluetooth, cellular, audio, camera, sensors, GPS or Touch ID.**
- **No real-time clock**: the date starts at 1969.
- **No Metal**: the 3D Earth wallpaper and anything else that needs Metal crashes.
- Wallpaper previews in the gallery are white; the lock-screen clock starts red.
- **Security is off:** permissive code signing (AMFI) and sandbox policies, a stub AppleKeyStore, no data protection. Do not put anything personal on it.

Planned work is listed in [`ideas.md`](ideas.md).

## How it boots

```
S-Boot (Samsung bootloader, OEM unlocked; flashed with Odin)
  -> BOOT partition: our shim (64-bit), moves the framebuffer, starts XNU
     -> XNU Mach-O + generated Apple Device Tree (ADT) + boot-args
        -> XNU -> eMMC driver -> HFS+ root over SYSTEM..USERDATA
           -> dyld + shared cache -> launchd -> daemons -> backboardd + SpringBoard
```

There is no serial port. The kernel draws its console on the screen during boot and keeps a persistent log in the `TOMBSTONES` partition. You read it back from TWRP with `a510f/tools/mmclog_pull.py`.

## Building

Everything builds on GitHub Actions. Pushes to `a510f` start the matching workflow:

| Workflow | Builds | From |
| --- | --- | --- |
| `a510f-xnu` | Kernel and boot image (`a510f-xnu-recovery`; `recovery.img` inside is the boot image) | `xnu/patches/`, `a510f/xnu/patches/` |
| `a510f-repack` | Boot image only, reusing the newest kernel (boot-args, device tree, shim) | `a510f/boot-args.txt`, `a510f/shim/`, `a510f/tools/mkadt_a510f.py` |
| `a510f-iosroot` | The iOS root image from the iPhone 8 Plus IPSW | `tools/mkiosroot.sh`, `a510f/tools/a510f-root-tweaks.py`, `a510f/apps.txt` |
| `a510f-sweetgl` | `sweetgl.dylib`: Mesa panfrost GLES for iOS (macOS runner) | `a510f/sweetgl/` |

To flash a boot image: rename `recovery.img` to `boot.img`, pack it with `tar --format=ustar -cf boot.tar boot.img`, and flash the tar in **Odin under AP**. Flashing unofficial images trips Knox permanently.

The iOS root cannot go through Odin (S-Boot refuses non-Samsung images for `SYSTEM`..`USERDATA`). It is written from TWRP 3.2.3 in 256 MiB chunks over adb, each verified by SHA-256; it takes about 75 minutes.

## Repository layout

| Path | What |
| --- | --- |
| `a510f/xnu/patches/` | A510F kernel patches (on top of `xnu/patches/`): eMMC, GICv2, 4 KB pages, touch, battery, framebuffer, scaler, the Mali GPU driver (`0122`), `sweetenv` (`0123`) |
| `a510f/shim/` | The 64-bit boot shim |
| `a510f/tools/` | ADT builder, root tweaks, kernel log reader (`mmclog_pull.py`), HFS+ and dyld cache helpers |
| `a510f/sweetgl/` | GPU user space: panfrost DRM emulation over SweetMali, Mesa fix-ups, adapter for sailfish's EAGL shim, build script |
| `a510f/boot-args.txt`, `a510f/apps.txt` | Boot arguments; stock apps kept in the root |
| `a510f/NOTES.md` | Engineering log: every boot, crash and decision, plus hardware facts |
| `a510f/probe/` | The original feasibility probe (64-bit code, PSCI, CPU features) |
| `xnu/patches/`, `tools/`, `shim/` | The ios-sweet base: kernel patch series and its tools |
| `ideas.md` | Picked ideas for later |

Not in git: partition backups, Apple firmware and root images, and downloaded build trees. They contain device data or Apple's copyrighted files.

## Key hardware facts

- Exynos 7580: 8× Cortex-A53 (ARMv8.0: no LSE atomics, no 16 KB pages), GIC-400 at `0x10C00000`, PSCI over `smc`.
- RAM 2 GB at `0x40000000`; S-Boot's framebuffer is moved by the shim to `0x40800000`.
- eMMC: DW-MMC at `0x13540000`, 64-bit IDMAC.
- Display: DECON at `0x14830000`, S6E3FA3 1080×1920 AMOLED, MIPI command mode (needs a trigger per frame).
- GPU: Mali-T720 MP2 r1p0 (`GPU_ID 0x07201000`) at `0x11400000`, IRQs SPI 282/283/281, G3D power domain at `0x10464060`, supply BUCK4 of the S2MPU03 PMIC.
- Battery: SM5705 fuel gauge, 2900 mAh.

More in [`a510f/NOTES.md`](a510f/NOTES.md).

## Credits

Built on [dipa-studio/ios-sweet](https://github.com/dipa-studio/ios-sweet) and [joranv1/ios-sailfish](https://github.com/joranv1/ios-sailfish) (EAGL shim and gallium frontend for CoreAnimation, fetched at build time), Apple's open-source releases (xnu, IOHIDFamily, libpthread, hfs), [Mesa](https://mesa3d.org) (panfrost), Linux's panfrost driver for the Mali programming model, [BearSSL](https://bearssl.org), [blacktop/darwin-xnu-build](https://github.com/blacktop/darwin-xnu-build), [ipsw](https://github.com/blacktop/ipsw), Samsung's and LineageOS's Exynos 7580 kernel sources for the hardware details, and [TWRP](https://twrp.me). iOS itself is Apple's and is not distributed here.
