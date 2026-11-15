"""Rewrite 0122's new-file hunk for iokit/Kernel/arm/SweetMali.cpp from gen/mali/SweetMali.cpp."""
import os
G = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(G, '..', 'patches', '0122-a510f-sweetmali-gpu-driver.patch')
src = open(os.path.join(G, 'mali', 'SweetMali.cpp'), encoding='utf-8').read().replace('\r\n', '\n')
lines = src.rstrip('\n').split('\n')
pat = open(P, encoding='utf-8').read().replace('\r\n', '\n')
start = pat.index('diff --git a/iokit/Kernel/arm/SweetMali.cpp')
end = pat.index('diff --git', start + 10)
hunk = ('diff --git a/iokit/Kernel/arm/SweetMali.cpp b/iokit/Kernel/arm/SweetMali.cpp\n'
        'new file mode 100644\nindex 0000000..1111111\n--- /dev/null\n+++ b/iokit/Kernel/arm/SweetMali.cpp\n'
        '@@ -0,0 +1,%d @@\n' % len(lines) + ''.join('+' + l + '\n' for l in lines))
open(P, 'w', encoding='utf-8', newline='\n').write(pat[:start] + hunk + pat[end:])
print('0122: SweetMali.cpp', len(lines), 'lines')
