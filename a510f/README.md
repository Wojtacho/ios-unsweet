# a510f/: the Galaxy A5 2016 port

Everything specific to the SM-A510F lives here. The project overview, status
and build steps are in the [main README](../README.md); the full engineering
log (every boot, crash and decision) is [`NOTES.md`](NOTES.md).

| Path | What |
| --- | --- |
| `xnu/patches/` | Kernel patches applied after the ios-sweet series in `../xnu/patches/` |
| `shim/` | 64-bit boot shim started by S-Boot from the `BOOT` partition |
| `tools/` | ADT builder (`mkadt_a510f.py`), root tweaks, kernel log reader (`mmclog_pull.py`), HFS+, dyld cache and block-patch helpers |
| `sweetgl/` | GPU user space: Mesa panfrost for iOS (see below) |
| `boot-args.txt` | Kernel boot arguments of the boot image |
| `apps.txt` | Stock apps kept in the iOS root |
| `build.sh` | Packs shim, ADT, kernel and boot-args into the boot image |
| `probe/` | The first feasibility probe (64-bit code, PSCI, CPU features), kept for reference |

## sweetgl

`sweetgl.dylib` is Mesa's panfrost GLES driver for the Mali-T720 as an iOS
library, built by the `a510f-sweetgl` workflow:

- `sweet_drm_pan.c`, `include/`: the libdrm and panfrost DRM calls Mesa makes,
  answered over the kernel's `SweetMali` user client (buffer objects, submit,
  parameters, IOSurface import, log lines).
- `mesa-fixup.py`: small changes to Mesa 26.2.4 (bo mappings come from the
  kernel, smaller tiler heap, no Linux-only perf-counter calls).
- `adapt.py`: takes the EAGL shim and gallium frontend from
  [joranv1/ios-sailfish](https://github.com/joranv1/ios-sailfish) (pinned
  commit, fetched at build time) and switches them from freedreno to
  panfrost.
- `build.sh`, `ci-run.sh`: the macOS build and its error reporting.

It is loaded into backboardd with the kernel's `sweetenv` boot-arg
(`sweetenv=backboardd:DYLD_INSERT_LIBRARIES=/usr/lib/sweetgl.dylib`). Only set
that once the library is on the phone: dyld stops backboardd if an inserted
library is missing.
