#!/bin/bash
# Build a Samsung recovery image for the SM-A510F plus an Odin tar.
#
#   build.sh                        the feasibility probe
#   build.sh xnu KERNEL [CMDLINE [ROOTFS]]
#                                   boot shim + xnu payload (ADT, boot-args);
#                                   ROOTFS becomes the md0 RAM disk (rd=md0)
#
# Needs (Ubuntu): gcc gcc-aarch64-linux-gnu device-tree-compiler libfdt-dev
#                 libssl-dev cpio git python3
# Output: a510f/out/recovery.img, a510f/out/a510f-{probe,xnu}-recovery.tar
set -euo pipefail
MODE=${1:-probe}
if [ "$MODE" = xnu ]; then
	KERNEL=$(realpath "$2")
	CMDLINE=${3:-debug=0xc serial=3 cpus=1 keepsyms=1 -enable_kprintf_spam}
	ROOTFS=${4:+$(realpath "$4")}
fi
cd "$(dirname "$0")"

OUT=out
CC=aarch64-linux-gnu-gcc
OBJCOPY=aarch64-linux-gnu-objcopy
# LineageOS exynos7580-common kernel: source of the a5xelte device trees.
KREPO=https://github.com/Exynos7580/android_kernel_samsung_exynos7580-common
KSHA=5a9711eabaa7df7a1136ccddc2b14b668ba657a4	# lineage-15.1

rm -rf "$OUT/dtb" "$OUT/probe" "$OUT/shim"
mkdir -p "$OUT/dtb" "$OUT/probe" "$OUT/shim"

# --- 1. device trees -------------------------------------------------------
# S-Boot only boots images whose dt.img has an entry for this board, so we
# ship the same a5xelte EUR-open device trees LineageOS ships.
K="$OUT/kernel"
if [ ! -d "$K/.git" ]; then
	git init -q "$K"
	git -C "$K" remote add origin "$KREPO"
	git -C "$K" config core.sparseCheckout true
	printf '%s\n' /arch/arm64/boot/dts/ /include/dt-bindings/ > "$K/.git/info/sparse-checkout"
	git -C "$K" fetch -q --depth 1 --filter=blob:none origin "$KSHA"
	git -C "$K" checkout -q FETCH_HEAD
fi
DTS="$K/arch/arm64/boot/dts"
n=0
for f in "$DTS"/exynos7580-a5xelte_eur_open_[0-9][0-9].dts; do
	b=$(basename "$f" .dts)
	cpp -nostdinc -undef -D__DTS__ -x assembler-with-cpp \
		-I "$DTS" -I "$DTS/include" -I "$K/include" "$f" \
		| dtc -q -I dts -O dtb -i "$DTS" -o "$OUT/dtb/$b.dtb" -
	n=$((n + 1))
done
[ "$n" -gt 0 ] || { echo "error: no a5xelte_eur_open device trees found" >&2; exit 1; }
echo "built $n device trees"

# --- 2. Samsung boot image tool (LineageOS hardware/samsung/dtbhtool) ------
gcc -O2 -Wno-deprecated-declarations -I tools/dtbhtool -I tools/dtbhtool/libdtbimg \
	tools/dtbhtool/mkbootimg.c tools/dtbhtool/dtbimg.c -lfdt -lcrypto \
	-o "$OUT/mkdtbhbootimg"

# --- 3. the image S-Boot starts ---------------------------------------------
CFLAGS="-O2 -ffreestanding -nostdlib -fno-pic -mcmodel=tiny -mgeneral-regs-only \
	-mstrict-align -fno-stack-protector -fno-builtin -Wall -Wextra"
# image DIR LDSCRIPT SOURCES...: compile, link at 0, flat binary -> $OUT/DIR/Image
image() {
	local dir=$1 ld=$2; shift 2
	local objs=() f o abs size
	for f in "$@"; do
		$CC $CFLAGS -c "$dir/$f" -o "$OUT/$dir/${f%.*}.o"
		objs+=("$OUT/$dir/${f%.*}.o")
	done
	# The image runs wherever S-Boot puts it with no relocation pass: only the
	# header's image_size (start.o, linked at 0) may be an absolute address.
	for o in "${objs[@]}"; do
		[ "$(basename "$o")" = start.o ] && continue
		abs=$(aarch64-linux-gnu-readelf -r "$o" | grep -c ABS64 || true)
		[ "$abs" = 0 ] || { echo "error: $abs absolute relocations in $o" >&2; exit 1; }
	done
	$CC $CFLAGS -static -T "$dir/$ld" -Wl,--build-id=none -Wl,--no-warn-rwx-segments -Wl,-N \
		"${objs[@]}" -o "$OUT/$dir/$dir.elf"
	$OBJCOPY -O binary "$OUT/$dir/$dir.elf" "$OUT/$dir/Image"
	# Pad to image_size so .bss and the stacks exist as zeroed bytes.
	size=$(aarch64-linux-gnu-nm "$OUT/$dir/$dir.elf" | awk '$3=="_end"{print strtonum("0x"$1)}')
	truncate -s "$size" "$OUT/$dir/Image"
}

if [ "$MODE" = xnu ]; then
	IMG_DIR=shim
	image shim shim.ld start.S shim.c console.c fdt.c loader.c
	# Ramdisk = the payload the shim's loader looks for: kernel segments,
	# ADT, boot-args (tools/mkpayload.py from sweet).
	python3 tools/mkadt_a510f.py "$OUT/shim/a510f.adt"
	python3 ../tools/mkpayload.py "$KERNEL" "$OUT/shim/a510f.adt" "$OUT/shim/ramdisk.bin" \
		--cmdline "$CMDLINE" ${ROOTFS:+--ramdisk "$ROOTFS"}
	RAMDISK="$OUT/shim/ramdisk.bin"
	TAR=a510f-xnu-recovery.tar
else
	IMG_DIR=probe
	image probe probe.ld start.S probe.c
	# Empty newc ramdisk: bootloaders tend to dislike a zero-size one.
	(cd "$OUT/probe" && rm -rf rd && mkdir rd && cd rd && find . | cpio -o -H newc --quiet | gzip -9 > ../ramdisk.gz)
	RAMDISK="$OUT/probe/ramdisk.gz"
	TAR=a510f-probe-recovery.tar
fi

# --- 4. recovery.img, same layout as LineageOS a5xeltexx -------------------
"$OUT/mkdtbhbootimg" --kernel "$OUT/$IMG_DIR/Image" --ramdisk "$RAMDISK" \
	--dt_dir "$OUT/dtb" --base 0x10000000 --pagesize 2048 \
	--kernel_offset 0x00008000 --ramdisk_offset 0x01000000 --tags_offset 0x00000100 \
	--board SRPOJ08A000KU --cmdline "" -o "$OUT/recovery.img"
printf 'SEANDROIDENFORCE' >> "$OUT/recovery.img"

# Sanity: header magic, non-empty DT section with a DTBH table.
python3 - "$OUT/recovery.img" <<'EOF'
import struct, sys
d = open(sys.argv[1], 'rb').read()
assert d[:8] == b'ANDROID!', 'bad boot magic'
ks, ka, rs, ra, ss, sa, ta, ps, dts = struct.unpack_from('<9I', d, 8)
pg = lambda n: (n + ps - 1) // ps * ps
off = ps + pg(ks) + pg(rs) + pg(ss)
assert dts > 0 and d[off:off + 4] == b'DTBH', 'no DTBH dt section'
ver, cnt = struct.unpack_from('<2I', d, off + 4)
revs = [struct.unpack_from('<8I', d, off + 12 + 32 * i)[3] for i in range(cnt)]
print(f'recovery.img: kernel {ks} B, ramdisk {rs} B, page {ps}, dt.img v{ver} with {cnt} entries, hw_rev {revs}')
# RECOVERY partition of the A510F (LineageOS a5xeltexx configs/board/fs.mk)
assert len(d) <= 35651584, f'recovery.img is {len(d)} B, the partition holds 35651584'
EOF

# --- 5. Odin tar (flash in the AP slot) ------------------------------------
(cd "$OUT" && rm -f "$TAR" && tar -H ustar -cf "$TAR" recovery.img)
ls -l "$OUT/$IMG_DIR/Image" "$RAMDISK" "$OUT/recovery.img" "$OUT/$TAR"
