# Ideas for iOS on the Galaxy A5 2016 (SM-A510F)

Picked ideas for later, beyond the current GPU work. Size is a rough guess:
**S** = one or two builds, **M** = a few builds, **L** = a project of its own.
Tick the box when done.

Current focus (not listed here): the GPU, i.e. the SweetMali kernel driver,
Mesa Panfrost for iOS, and CoreAnimation rendering on the Mali-T720.

## Performance

- [x] **8th CPU core** (M)
  Core 1 only refreshes the screen (the panel is in MIPI command mode and needs
  a DECON trigger every ~16 ms). Move that job into the kernel (a timer or the
  vsync interrupt) and give iOS all 8 cores: about 14% more CPU.
  Done: round 55 (2026-11-17): no shim refresher, SweetFramebuffer triggers DECON every vsync/flip, cpus=8 (testing).

- [ ] **60 Hz direct scanout** (M) (partly: presents at 60 Hz into a double buffer, round 50s; still a CPU copy + scale per frame)
  The framebuffer driver copies the finished frame to the panel only 10 times a
  second (`sweetfb_hz`, default 10) and scales 1242x2208 -> 1080x1920 on the
  CPU. Present at 60 Hz and point DECON straight at the finished image (no copy),
  like ios-topaz's direct scanout. Needed for smooth animation once the GPU draws.
  With native 1080p rendering (below) the CPU scale goes away and only a 1:1
  copy is left.

- [x] **GPU at full clock** (S)
  The Mali runs from the 400 MHz bus clock (aclk_g3d_400). Program its own PLL
  (Samsung's table: 668 MHz at 1.1 V, up to 800 MHz) with the same park-on-bus,
  change-PLL, switch-back sequence as Samsung's gpu_set_clock.
  Done: 668 MHz (rounds 13-16; 400 MHz was ~40% slower).

## Graphics and display

- [ ] **Native 1080p rendering** (M) (next speed round, 2026-11-17)
  iOS renders the iPhone 8 Plus canvas, 1242x2208: 32% more pixels than the
  1080x1920 panel. Render at the panel size, or let the GPU do the scaling.
  Plan: iOS keeps its 1242x2208 layout (same look); sweetgl draws the screen
  target at 1080x1920 (viewport, scissor and copy rectangles scaled by
  1920/2208) into the top-left of the same surface, and the kernel shows it
  1:1. About 24% less GPU work per full-screen pass and no CPU scaling (the
  GPU is the frame limit at ~12 fps, round 60).

- [x] **Fix the red clock text** (S-M)
  The lock-screen clock starts red and fades to white when pressing Home. Likely
  CoreAnimation's vibrancy / colour filter misbehaving on the CPU renderer; may
  go away with the GPU, check again then.
  Done: gone since CoreAnimation renders on the GPU (user check, 2026-11-17).

- [ ] **Folder and app switcher materials** (S-M)
  The frosted square behind folder icons, the open folder's panel and the app
  switcher's blurred background are missing (the dock's material works; the
  folder recipe is the same with a smaller backdrop scale). Cards of apps not
  opened since boot are blank: snapshots need a JPEG codec (AppleJPEGDriver is
  a stand-in). Round 63 probes every draw over the folder icon.

- [x] **Astronomy wallpaper off** (S)
  AegirPoster (the 3D Earth wallpaper) needs Metal: it crashed 93 times in one
  boot and makes the wallpaper gallery lag. Hide or disable that one extension.
  Done: no longer crash-loops (rounds 49-53 logs: no AegirPoster).

- [x] **Async GPU submission** (M)
  SweetMali waits for every job to finish. Use the Mali's job/MMU interrupts
  and a queue so the CPU and GPU work in parallel (Linux panfrost's model).
  Done: SweetMali job queue (sel 17/18, worker thread), ~25% more frames.

## Hardware

- [ ] **Real date and time** (S-M) (partly: calendar set to the patch time at boot, round 47; RTC still to read)
  The phone starts in 1969: no RTC driver yet. Read the S2MPU03 PMIC's real-time
  clock (through the HSI2C3 batcher, like the touch power and the CPU voltage)
  and set the kernel clock from it.

- [ ] **Wi-Fi** (L) (next big project after the speed round, for Safari)
  Plan: SDIO host (same DW-MMC family as our eMMC driver), the Broadcom
  firmware + NVRAM from the phone's own Android backups, the firmware's own
  WPA2 supplicant (no wpa_supplicant), and an Ethernet-style interface that
  iOS uses like a wired network (network name and password from boot-args).
  The Settings Wi-Fi page would stay empty: it needs Apple's own driver.
  Broadcom Wi-Fi chip: SDIO host, firmware loading and a driver that wifid
  accepts (ios-flame did this for Qualcomm's WCN3990 in user space: `wland`).

- [ ] **Audio** (L)
  Speaker and headphones through the codec (I2S + amplifier). No sweet-based
  port has audio yet.

- [ ] **Charger chip reading** (S)
  Plug/unplug is guessed from the battery current. Read the SM5705 charger's
  own status (HSI2C at 0x13890000, address 0x49) for exact charging state.

## Tools

- [ ] **SSH into iOS** (M)
  A root shell on the running iOS over USB (ios-flame: dropbear + USB Ethernet).
  Much faster debugging than videos and TWRP visits.

- [ ] **Faster root writes** (S)
  Writing the 14.7 GB iOS root through TWRP takes ~75 minutes because empty
  space is written and verified too. Skip all-zero chunks after one fast clear:
  roughly half the time.

- [x] **Remove crash-loop daemons** (S)
  bluetoothd (27 restarts per boot), fairplayd (32) and the speech synthesizer
  services keep crashing and being restarted, which costs CPU. Remove or disable
  them in the root build (and in place on the phone).
  Done: sweetnoexec: bluetoothd, fairplayd, speech services, vmd (round 49); widget/poster extensions at background priority.
