#!/bin/sh
# Regenerate the patches built by scripts from a base file:
#   0125 (SweetFramebuffer.cpp)  fb/base + fb/edit.py (+ fb/fit_fast.inc)
#   0126 (SweetSurface.cpp/.h)   ss/base + ss/edit_ss.py
# mali/SweetMali.cpp is the whole new file that 0122 adds.
# Run from anywhere: sh a510f/xnu/gen/gen.sh
set -e
G=$(cd "$(dirname "$0")" && pwd)
P=$G/../patches
T=$(mktemp -d)
fix() { sed -i 's#^diff --git a/a/#diff --git a/#; s# b/b/# b/#; s#^--- a/a/#--- a/#; s#^+++ b/b/#+++ b/#' "$1"; }

mkdir -p $T/fb/a/iokit/Kernel/arm
cp $G/fb/base/SweetFramebuffer.cpp $T/fb/a/iokit/Kernel/arm/
chmod 644 $T/fb/a/iokit/Kernel/arm/*
cp -r $T/fb/a $T/fb/b
python3 $G/fb/edit.py $T/fb/b/iokit/Kernel/arm/SweetFramebuffer.cpp
(cd $T/fb && git diff --no-index a b > fb.diff || true)
fix $T/fb/fb.diff
cp $T/fb/fb.diff $P/0125-a510f-fb-double-buffer-present.patch

mkdir -p $T/ss/a/iokit/Kernel/arm
cp $G/ss/base/SweetSurface.cpp $G/ss/base/SweetSurface.h $T/ss/a/iokit/Kernel/arm/
chmod 644 $T/ss/a/iokit/Kernel/arm/*
cp -r $T/ss/a $T/ss/b
python3 $G/ss/edit_ss.py $T/ss/b/iokit/Kernel/arm/SweetSurface.cpp $T/ss/b/iokit/Kernel/arm/SweetSurface.h
(cd $T/ss && git diff --no-index a b > ss.diff || true)
fix $T/ss/ss.diff
cp $T/ss/ss.diff $P/0126-a510f-display-surfaces-cached.patch
rm -rf $T
echo "0125 and 0126 regenerated"
