#!/usr/bin/env python3
"""Build the Apple Device Tree for the SM-A510F (Exynos 7580) bring-up kernel.

  mkadt_a510f.py OUT.adt [--dump]

Reuses sweet's tools/mkadt.py (same nodes the kernel's early boot reads) and
swaps in the A510F hardware facts. Sources: LineageOS exynos7580-common
device trees (exynos7580.dtsi, exynos7580-reserve-2000MB-Ax.dtsi) and the
a510f probe run (a510f/NOTES.md).
"""
import os, struct, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '../../tools'))
import adt     # noqa: E402
import mkadt   # noqa: E402

# Kernel RAM: above the S-Boot framebuffer (0x67000000 + 8MB) and the
# shim/ramdisk/DTB in low memory, below the first reserved carve-out
# (video_ext 0xaec00000; CP 0xb0000000; EL3 monitor 0xbee00000).
PHYS_BASE = 0x70000000
PHYS_END = 0xaec00000

mkadt.PHYS_BASE = PHYS_BASE
mkadt.MEM_SIZE = PHYS_END - PHYS_BASE
mkadt.FB, mkadt.FB_SIZE = 0x67000000, 0x800000
mkadt.FB_W, mkadt.FB_H, mkadt.FB_STRIDE = 1080, 1920, 1080 * 4
mkadt.TIMEBASE = 26000000                   # timer clock-frequency
# GIC-400 (GICv2): GICD 0x10c01000, GICC 0x10c02000. sweet's kernel drives
# a GICv3; these only stop it touching Qualcomm addresses until the A510F
# gets its own GICv2 code (interrupts are not needed for the first text).
mkadt.GICD, mkadt.GICD_SIZE = 0x10c01000, 0x1000
mkadt.GICR, mkadt.GICR_SIZE = 0x10c02000, 0x2000
mkadt.VTIMER_INTID = 27                      # PPI 11, standard numbering

# Cortex-A53 x8: cluster 0 = MPIDR 0x000-0x003, cluster 1 = 0x100-0x103.
MPIDR = [(c // 4) << 8 | (c % 4) for c in range(8)]
CPU_HZ = 1600000000


def setprop(node, name, value):
    for i, (k, f, v) in enumerate(node.props):
        if k == name:
            node.props[i] = (k, f, value)
            return
    node.props.append((name, 0, value))


def child(node, name):
    for c in node.children:
        if c.name == name:
            return c
    raise KeyError(name)


def build():
    root = mkadt.build(qemu=False, highmem=False)
    # No UFS on this phone (eMMC); sweet_ufs must not probe Qualcomm MMIO.
    root.children = [c for c in root.children if c.name != 'sweet-ufs']
    for i, cpu in enumerate(child(root, 'cpus').children):
        setprop(cpu, 'reg', struct.pack('<I', MPIDR[i]))
        # 'qcom,kryo470' stays: sweet's SweetCPU driver matches it
        # (IONameMatch in KernelConfigTables.cpp). Without a CPU driver the
        # boot CPU never registers with IOKit and the kernel waits silently
        # (sixth boot: output stopped after SWEET FB, no panic).
        setprop(cpu, 'compatible', mkadt.cstr('arm,cortex-a53') + mkadt.cstr('qcom,kryo470') + mkadt.cstr('ARM,v8'))
        setprop(cpu, 'cluster-core-id', struct.pack('<I', i % 4))
        setprop(cpu, 'clock-frequency', struct.pack('<I', CPU_HZ))
        setprop(cpu, 'l2-cache-id', struct.pack('<I', i // 4))
    # Keep the sweet compatibles the kernel's platform expert matches on.
    compat = root.prop('compatible')
    setprop(root, 'compatible', compat + mkadt.cstr('samsung,a5xelte') + mkadt.cstr('samsung,exynos7580'))
    return root


if __name__ == '__main__':
    blob = adt.serialize(build())
    open(sys.argv[1], 'wb').write(blob)
    if '--dump' in sys.argv:
        adt.dump(adt.parse(blob)[0])
    print(f'{sys.argv[1]}: {len(blob)} bytes', file=sys.stderr)
