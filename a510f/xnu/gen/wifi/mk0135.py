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
start = k        # 1-based line number of tl[k-1]
out += ['diff --git a/bsd/dev/a510f_touch.c b/bsd/dev/a510f_touch.c', '--- a/bsd/dev/a510f_touch.c',
        '+++ b/bsd/dev/a510f_touch.c', '@@ -%d,6 +%d,10 @@' % (start, start)]
out += [' ' + tl[j] for j in (k - 1, k, k + 1)]
out += ['+\t{', '+\t\textern void a510f_wifi_start(void);   /* bsd/dev/a510f_wifi.c */', '+\t\ta510f_wifi_start();', '+\t}']
out += [' ' + tl[j] for j in (k + 2, k + 3, k + 4)]
out += ['diff --git a/bsd/dev/a510f_wifi.c b/bsd/dev/a510f_wifi.c', 'new file mode 100644', '--- /dev/null',
        '+++ b/bsd/dev/a510f_wifi.c', '@@ -0,0 +1,%d @@' % len(new)]
out += ['+' + l for l in new]
open(os.path.join(P, '0135-a510f-wifi-sdio.patch'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('0135 regenerated:', len(new), 'lines of a510f_wifi.c')
