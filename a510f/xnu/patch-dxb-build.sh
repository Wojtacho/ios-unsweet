#!/bin/bash
# Adjust blacktop's darwin-xnu-build build.sh for the A510F kernel.
#
#   patch-dxb-build.sh DXB_DIR
#
# libfirehose_kernel (kernel logging buffer, linked into xnu) is built by
# xcodebuild, outside xnu's makefiles, so the kernel's -mcpu flag never
# reaches it: Apple clang then targets apple-m1 and emits LSE/LDAPR
# (a510f-kernel-check run 42801602322 located 12 of 13 hits in
# firehose_buffer_*). Build its plain arm64 slice for cortex-a53.
set -euo pipefail

f="$1/build.sh"
python3 - "$f" <<'EOF'
import sys
path = sys.argv[1]
s = open(path).read()
old = 'xcodebuild install -target libfirehose_kernel -sdk macosx ARCHS="x86_64 arm64e" VALID_ARCHS="x86_64 arm64e"'
new = ('xcodebuild install -target libfirehose_kernel -sdk macosx ARCHS="x86_64 arm64e arm64" '
       'VALID_ARCHS="x86_64 arm64e arm64" \'OTHER_CFLAGS[arch=arm64]=$(inherited) -mcpu=cortex-a53\'')
assert s.count(old) == 1, 'libfirehose_kernel xcodebuild line not found'
open(path, 'w').write(s.replace(old, new))
EOF
grep -n 'target libfirehose_kernel' "$f"
