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


# The iOS userland is the iPhone 8 Plus (iPhone10,2 / D21AP) IPSW: its
# 1080x1920 panel is the A510F's, and it has a Home button. The real D21AP
# device tree (an Apple artifact, fetched in CI from the IPSW, not in git)
# gives /product (artwork, screen class) and /buttons (Home button type).
D21AP_ADT = os.path.join(HERE, '../../research/ipsw-8p/d21ap.adt')
CANVAS_W, CANVAS_H = 1242, 2208             # 414x736 points @3x, as iOS renders on an 8 Plus


def real_node(name, path=D21AP_ADT):
    """Properties of /NAME in the real D21AP tree (no syscfg placeholders)."""
    root, _ = adt.parse(open(path, 'rb').read())
    for c in root.children:
        if dict((k, v) for k, f, v in c.props).get('name') == name.encode() + b'\0':
            return [(k, v) for k, f, v in c.props if not f and k not in ('name', 'AAPL,phandle')]
    return None


def iphone8plus(root):
    if not os.path.exists(D21AP_ADT):
        raise SystemExit(f'{D21AP_ADT} missing: extract DeviceTree.d21ap.im4p from the 8 Plus IPSW')
    # Identity: compatible[0] = hw.model (D21AP), model = hw.machine (iPhone10,2).
    compat = root.prop('compatible').split(b'\0')
    rest = b''.join(c + b'\0' for c in compat[2:] if c)
    setprop(root, 'compatible', mkadt.cstr('D21AP') + mkadt.cstr('iPhone10,2') + rest)
    setprop(root, 'model', mkadt.cstr('iPhone10,2'))
    setprop(root, 'target-type', mkadt.cstr('D21'))
    setprop(root, 'target-sub-type', mkadt.cstr('D21AP'))
    # Display canvas: the size iOS renders at (SweetFramebuffer scales it to the panel).
    disp = child(child(root, 'arm-io'), 'disp0')
    setprop(disp, 'canvas-width', struct.pack('<I', CANVAS_W))
    setprop(disp, 'canvas-height', struct.pack('<I', CANVAS_H))
    # /product and /buttons from the real tree (replace the iPhone X ones).
    for name in ('product', 'buttons'):
        props = real_node(name)
        if props is not None and name == 'buttons':
            # Only what MobileGestalt reads; not Apple's wiring (compatible,
            # interrupts, function-button_* phandles) that drivers would match.
            props = [(k, v) for k, v in props
                     if k in ('button-names', 'home-button-type', 'opposed-power-vol-buttons')]
        root.children = [c for c in root.children if c.name != name]
        if props is not None:
            n = mkadt.node(name, [('AAPL,phandle', struct.pack('<I', 900 + len(root.children)))] + props)
            root.children.append(n)
            print(f'D21AP /{name}: ' + ', '.join(k for k, v in props), file=sys.stderr)
        elif name == 'product':
            raise SystemExit('D21AP tree has no /product')
        else:
            # No /buttons in the tree: a Home-button device has no home-button-type (= 0).
            root.children.append(mkadt.node('buttons', [
                ('AAPL,phandle', struct.pack('<I', 899)),
                ('button-names', mkadt.cstr('volup') + mkadt.cstr('voldown') + mkadt.cstr('hold') + mkadt.cstr('menu')),
                ('opposed-power-vol-buttons', struct.pack('<I', 1)),
            ]))
            print('D21AP has no /buttons: Home-button default', file=sys.stderr)


def build():
    root = mkadt.build(qemu=False, highmem=False)
    iphone8plus(root)
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
