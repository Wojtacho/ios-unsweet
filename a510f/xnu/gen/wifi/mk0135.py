"""Regenerate a510f/xnu/patches/0135-a510f-wifi-sdio.patch from gen/wifi/a510f_wifi.c.

The patch adds bsd/dev/a510f_wifi.c, its bsd/conf/files line (after
a510f_touch.c, line 109 once 0106/0110 are applied) and the
a510f_wifi_start() call in a510f_touch_start() (a510f_touch.c comes whole
from 0110; the call goes after the a510f_bg_start() block).
Run from anywhere: python a510f/xnu/gen/wifi/mk0135.py
"""
import os

G = os.path.dirname(os.path.abspath(__file__))
P = os.path.normpath(os.path.join(G, '..', '..', 'patches'))

new = open(os.path.join(G, 'a510f_wifi.c'), encoding='utf-8').read().rstrip('\n').split('\n')

# a510f_touch.c as 0110 creates it
L = open(os.path.join(P, '0110-a510f-touchscreen.patch'), encoding='utf-8', newline='').read().split('\n')
i = L.index('+++ b/bsd/dev/a510f_touch.c')
n = int(L[i + 1].split('+1,')[1].split(' ')[0])
tl = [l[1:] for l in L[i + 2:i + 2 + n]]
k = tl.index('\t\ta510f_bg_start();')          # 0-based; the block is tl[k-2..k+1]
assert tl[k + 1] == '\t}', tl[k + 1]

out = ['diff --git a/bsd/conf/files b/bsd/conf/files', '--- a/bsd/conf/files', '+++ b/bsd/conf/files',
       '@@ -107,6 +107,7 @@',
       ' bsd/dev/sweet_ufs.c\t\t\tstandard',
       ' bsd/dev/sweet_mmc.c\t\t\tstandard',
       ' bsd/dev/a510f_touch.c\t\t\tstandard',
       '+bsd/dev/a510f_wifi.c\t\t\tstandard',
       ' bsd/dev/sweet_sample.c\t\t\tstandard',
       ' bsd/dev/sweet_keys.c\t\t\tstandard',
       ' bsd/dev/sweet_touch.c\t\t\tstandard']
# a510f_touch.c hunks, in file order: (index of the line the insertion goes before, added lines)
vib = open(os.path.join(G, 'vib_touch.inc'), encoding='utf-8').read().rstrip('\n').split('\n') + ['']
kt = tl.index('touch_thread(__unused void *arg, __unused wait_result_t w)')
assert tl[kt - 1] == 'static void', tl[kt - 1]
kl = tl.index('\tunsigned lows = 0;') + 2      # keys_poll() in touch_thread's loop (another loop calls it too)
assert tl[kl - 1] == '\tfor (;;) {' and tl[kl - 2] == '\tunsigned lows = 0;', tl[kl - 2:kl]
inserts = [
    (kt - 1, vib),                                                      # the motor code before touch_thread()
    (kl + 1, ['\t\tvib_poll();']),
    (k + 2, ['\t{', '\t\textern void a510f_wifi_start(void);   /* bsd/dev/a510f_wifi.c */', '\t\ta510f_wifi_start();', '\t}']),
]
out += ['diff --git a/bsd/dev/a510f_touch.c b/bsd/dev/a510f_touch.c', '--- a/bsd/dev/a510f_touch.c',
        '+++ b/bsd/dev/a510f_touch.c']
shift = 0
for at, add in inserts:
    old_start = at - 3 + 1                      # 1-based number of the first context line (3 before)
    out += ['@@ -%d,6 +%d,%d @@' % (old_start, old_start + shift, 6 + len(add))]
    out += [' ' + tl[j] for j in (at - 3, at - 2, at - 1)]
    out += ['+' + l for l in add]
    out += [' ' + tl[j] for j in (at, at + 1, at + 2)]
    shift += len(add)
# sweet_mmc.c as 0106 + 0110 leave it: a510f_mmc_read() after sweet_bootlogo_load()
import shutil
import subprocess
import tempfile
T = tempfile.mkdtemp()
try:
    subprocess.run(['git', 'init', '-q'], cwd=T, check=True)
    for pn in ('0106-a510f-emmc.patch', '0110-a510f-touchscreen.patch'):
        subprocess.run(['git', 'apply', '--include=bsd/dev/sweet_mmc.c', os.path.join(P, pn)], cwd=T, check=True)
    ml = open(os.path.join(T, 'bsd', 'dev', 'sweet_mmc.c'), encoding='utf-8', newline='').read().replace('\r', '').split('\n')
finally:
    shutil.rmtree(T, ignore_errors=True)
k = [j for j, l in enumerate(ml) if 'printf("SWEET MMC: no boot logo (error %d)' in l]
assert len(k) == 1, k
k = k[0]
assert ml[k + 1] == '}' and ml[k + 2] == '' and ml[k + 3] == 'static void', ml[k + 1:k + 4]
helper = [
    '/*',
    ' * A510F Wi-Fi (bsd/dev/a510f_wifi.c): read nsect sectors at lba inside the',
    ' * partition named part (NULL: absolute LBA) into dst (any kernel memory:',
    ' * bounced through a DMA buffer, 64 sectors a read). 0 or an errno.',
    ' */',
    'int a510f_mmc_read(const char *part, uint64_t lba, uint32_t nsect, void *dst);',
    '',
    'int',
    'a510f_mmc_read(const char *part, uint64_t lba, uint32_t nsect, void *dst)',
    '{',
    '\tstatic uint8_t *bounce;',
    '\tint error = 0;',
    '\tuint64_t first = 0, n = UINT64_MAX;',
    '\tmmc_lock();',
    '\tif (bounce == NULL) {',
    '\t\tbounce = mmc_alloc(64 * MMC_SECTOR);',
    '\t}',
    '\tif (part != NULL) {',
    '\t\terror = mmc_part_find(part, &first, &n);',
    '\t}',
    '\tif (!error && (bounce == NULL || lba + nsect > n)) {',
    '\t\terror = bounce == NULL ? ENOMEM : EINVAL;',
    '\t}',
    '\tfor (uint32_t k = 0; !error && k < nsect; k += 64) {',
    '\t\tuint32_t c = nsect - k < 64 ? nsect - k : 64;',
    '\t\terror = mmc_read(first + lba + k, c, bounce);',
    '\t\tif (!error) {',
    '\t\t\tmemcpy((uint8_t *)dst + (uint64_t)k * MMC_SECTOR, bounce, (size_t)c * MMC_SECTOR);',
    '\t\t}',
    '\t}',
    '\tmmc_unlock();',
    '\treturn error;',
    '}',
    '',
]
start = k + 1                                   # 1-based number of ml[k]
out += ['diff --git a/bsd/dev/sweet_mmc.c b/bsd/dev/sweet_mmc.c', '--- a/bsd/dev/sweet_mmc.c', '+++ b/bsd/dev/sweet_mmc.c',
        '@@ -%d,6 +%d,%d @@' % (start, start, 6 + len(helper))]
out += [' ' + ml[j] for j in (k, k + 1, k + 2)]
out += ['+' + l for l in helper]
out += [' ' + ml[j] for j in (k + 3, k + 4, k + 5)]

out += ['diff --git a/bsd/dev/a510f_wifi.c b/bsd/dev/a510f_wifi.c', 'new file mode 100644', '--- /dev/null',
        '+++ b/bsd/dev/a510f_wifi.c', '@@ -0,0 +1,%d @@' % len(new)]
out += ['+' + l for l in new]
open(os.path.join(P, '0135-a510f-wifi-sdio.patch'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('0135 regenerated:', len(new), 'lines of a510f_wifi.c')
