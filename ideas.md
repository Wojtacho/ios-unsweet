# Ideas for iOS on the Galaxy A5 2016 (SM-A510F)

Picked ideas for later, beyond the current GPU work. Size is a rough guess:
**S** = one or two builds, **M** = a few builds, **L** = a project of its own.
Tick the box when done.

Current focus (not listed here): the GPU, i.e. the SweetMali kernel driver,
Mesa Panfrost for iOS, and CoreAnimation rendering on the Mali-T720.

## Performance

- [ ] **8th CPU core** (M)
  Core 1 only refreshes the screen (the panel is in MIPI command mode and needs
  a DECON trigger every ~16 ms). Move that job into the kernel (a timer or the
  vsync interrupt) and give iOS all 8 cores: about 14% more CPU.

- [ ] **60 Hz direct scanout** (M)
  The framebuffer driver copies the finished frame to the panel only 10 times a
  second (`sweetfb_hz`, default 10) and scales 1242x2208 -> 1080x1920 on the
  CPU. Present at 60 Hz and point DECON straight at the finished image (no copy),
  like ios-topaz's direct scanout. Needed for smooth animation once the GPU draws.

- [ ] **GPU at full clock** (S)
  The Mali runs from the 400 MHz bus clock (aclk_g3d_400). Program its own PLL
  (Samsung's table: 668 MHz at 1.1 V, up to 800 MHz) with the same park-on-bus,
  change-PLL, switch-back sequence as Samsung's gpu_set_clock.

## Graphics and display

- [ ] **Native 1080p rendering** (M)
  iOS renders the iPhone 8 Plus canvas, 1242x2208: 32% more pixels than the
  1080x1920 panel. Render at the panel size, or let the GPU do the scaling.

- [ ] **Fix the red clock text** (S-M)
  The lock-screen clock starts red and fades to white when pressing Home. Likely
  CoreAnimation's vibrancy / colour filter misbehaving on the CPU renderer; may
  go away with the GPU, check again then.

- [ ] **Astronomy wallpaper off** (S)
  AegirPoster (the 3D Earth wallpaper) needs Metal: it crashed 93 times in one
  boot and makes the wallpaper gallery lag. Hide or disable that one extension.

- [ ] **Async GPU submission** (M)
  SweetMali waits for every job to finish. Use the Mali's job/MMU interrupts
  and a queue so the CPU and GPU work in parallel (Linux panfrost's model).

## Hardware

- [ ] **Real date and time** (S-M)
  The phone starts in 1969: no RTC driver yet. Read the S2MPU03 PMIC's real-time
  clock (through the HSI2C3 batcher, like the touch power and the CPU voltage)
  and set the kernel clock from it.

- [ ] **Wi-Fi** (L)
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

- [ ] **Remove crash-loop daemons** (S)
  bluetoothd (27 restarts per boot), fairplayd (32) and the speech synthesizer
  services keep crashing and being restarted, which costs CPU. Remove or disable
  them in the root build (and in place on the phone).
