# A510F kernel patches (applied after sweet's xnu/patches)

- `0100-a510f-4k-commpage-assert.patch`
- `0101-a510f-commpage-pfz-llsc.patch`
- `0102-a510f-early-fb-small-memory.patch`
- `0103-a510f-gicv2-panic-power-off.patch`
- `0104-a510f-ios-zone-map-size.patch`
- `0105-a510f-rebase-timebase.patch`
- `0106-a510f-emmc.patch`
- `0107-a510f-initproc-panic-delay-srtrace.patch`
- `0108-a510f-16k-code-signatures-on-4k.patch`
- `0109-a510f-display-always-on.patch`
- `0110-a510f-touchscreen.patch` (ZT7538 touch, PMIC LDO33 through the HSI2C3 batcher, GPIO buttons; also the CPU clock raise, the SM5705 gauge reader, eMMC DMA reads and the persistent console log on TOMBSTONES, `mmclog=0` off, read in TWRP with twrp-write/mmclog_pull.py)
- `0111-a510f-display-fit.patch` (boot-arg sweetfb_fit=1: scale the presented frame to the panel)
- `0112-a510f-iphone8plus-display.patch` (present 1242x2208 @401 ppi like the iPhone 8 Plus; touch 1:1 on the panel with sweetfb_fit)
- `0113-a510f-smp.patch` (SMP on 2 x 4 Cortex-A53: MPIDR Aff1:Aff0 topology, GIC-400 interface per core from ITARGETSR0, no ICC_SRE_EL2 on the EL2 entry path, CNTVCT check per core)
- `0114-a510f-physical-counter.patch` (kernel time from the system-wide CNTPCT, as Samsung's use-physical-timer; user space takes the mach_absolute_time trap)
- `0115-a510f-boot-waits.patch` (from MakrSas/ios-topaz 0138/0128: empty IOAcceleratorES service so QuartzCore stops its 30 s poll at every backboardd start, `sweetaccel=0` off; no registry busy hold for an IOKit daemon that never reports in, `sweetiokitdhold=1` restores it; SWEET AKS console lines capped at 48, `sweetakslog=1` all)
- `0116-a510f-battery-sm5705.patch` (SweetBattery reads the SM5705 fuel gauge: level, voltage, current, temperature; 2900 mAh; charging = current into the battery; `sweetbattery=0` keeps the static 100%. The GPIO-I2C gauge reader `a510f_fg_read` is in 0110)
- `0117-a510f-surfaces.patch` (SweetSurface fixes from MakrSas/ios-topaz 0131-0137 and 0139, merged without topaz's Qualcomm scanout code: surface values/attachments kept instead of zeroes, client-memory surfaces, detach/zombie-state lifetime fixes, IOSurfaceAddress surfaces published with real ids; framebuffer converts 10-bit l10r/w30r layers; one log line per new layer format and per new process+surface format)
- `0118-a510f-framebuffer-low-ram.patch` (SWEET_FB_BASE 0x40800000: the shim moves DECON window 0 there from S-Boot's 0x67000000, so RAM is 0x44000000..0xaec00000, 1708 MB instead of 1004 MB; goes with a510f/shim and mkadt_a510f.py)
- `0119-a510f-compressor-pool-4x.patch` (compressor pool 4 x RAM instead of the macOS 16 x: with 1.7 GB of RAM the 27 GB compressor VA claim plus the 24 GB zone map no longer fit the 4K iOS VA layout; the vm_compression_limit boot-arg is in 16 KB VM pages and bypasses the formula, so it is not used)
- `0120-a510f-commpage-text-aligned.patch` (commpage text page at a random leaf rounded to a 16 KB VM page: write_pte_fast writes 4 leaf PTEs and panicked on leaf 146, which the fixed early random() sequence picked once RAM was 1708 MB)
- `0121-a510f-software-scaler.patch` (software AppleM2ScalerCSCDriver: IOSurfaceAccelerator selector 1, 0x170-byte request with source/destination surface ids at +0/+4; whole-surface nearest-neighbour scale and BGRA/L008/420f/420v conversion on the CPU, destination seed bumped. SpringBoard's home-screen wallpaper copies were never written without it)
- `0122-a510f-sweetmali-gpu-driver.patch` (SweetMali: Mali-T720 kernel driver after Linux panfrost: power/clock/reset, AS0 with on-demand Mali LPAE tables and lock+FLUSH_PT, wired or IOSurface-backed BOs mapped write-combined into the client, synchronous job submit on JS0 (fragment) / JS1 with fault recovery, panfrost GET_PARAM values; user client selectors 10-15; boot self-test job; `sweetmali=0` off)

See a510f/NOTES.md for what each boot showed.
