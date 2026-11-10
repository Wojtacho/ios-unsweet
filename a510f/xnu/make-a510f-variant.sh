#!/bin/bash
# Turn a copy of sweet's xnu patch set into the A510F (Cortex-A53) variant.
#
#   make-a510f-variant.sh PATCH_DIR
#
# Edits PATCH_DIR/0004-sweet-machine-config.patch in place (run it on the copy
# in dxb/patches, never on xnu/patches). Each edit replaces one added line
# with another, so hunk line counts stay valid:
#   - no __ARM_16K_PG__: 4 KB pages, as xnu's own Cortex-A53 config BCM2837
#   - no __ARM_PAN_AVAILABLE__ (PAN is ARMv8.1); BCM2837's
#     __ARM64_PMAP_SUBPAGE_L1__ in its place
#   - -mcpu=cortex-a53 instead of -march=armv8.2-a: no LSE/RCpc from the
#     compiler and no __ARM_ARCH_8_2__ paths (machine_routines_asm.s casa).
#     -march alone is not enough: Apple clang keeps its default CPU
#     (apple-m1 for macOS targets) and emitted 875 LSE + 209 LDAPR
#     (a510f-kernel-check run 42798173229).
# The machine config keeps the name SWEET so sweet's stage scripts, MASTER
# config and kernel name still apply; the board code is still sweet's.
set -euo pipefail

p="$1/0004-sweet-machine-config.patch"
[[ -f $p ]] || { echo "missing $p" >&2; exit 1; }

edit() {	# edit OLD NEW: exactly one line must match
	local n
	n=$(grep -cxF -- "$1" "$p" || true)
	[[ $n == 1 ]] || { echo "expected one line '$1' in $p, found $n" >&2; exit 1; }
	python3 - "$p" "$1" "$2" <<'EOF'
import sys
path, old, new = sys.argv[1:]
lines = open(path).read().split('\n')
lines[lines.index(old)] = new
open(path, 'w').write('\n'.join(lines))
EOF
}

edit '+#define __ARM_16K_PG__            1' \
     '+/* A510F: 4 KB pages, the Cortex-A53 has no 16 KB granule */'
edit '+#define __ARM_PAN_AVAILABLE__     1' \
     '+#define __ARM64_PMAP_SUBPAGE_L1__ 1 /* A510F: as BCM2837; no PAN on A53 */'
edit '+MACHINE_FLAGS_ARM64_SWEET = -DARM64_BOARD_CONFIG_SWEET                -march=armv8.2-a+crypto' \
     '+MACHINE_FLAGS_ARM64_SWEET = -DARM64_BOARD_CONFIG_SWEET                -mcpu=cortex-a53'

grep -nE '16K_PG|PAN_AVAILABLE|SUBPAGE_L1|march=' "$p"
