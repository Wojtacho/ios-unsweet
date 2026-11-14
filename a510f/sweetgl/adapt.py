#!/usr/bin/env python3
"""A510F sweetgl: take joranv1/ios-sailfish's tools/sweetgl (freedreno, Adreno)
and turn its gallium frontend and EAGL shim into the panfrost (Mali) build.

usage: adapt.py SAILFISH_SWEETGL_DIR OUT_DIR

eagl.c (CoreAnimation's EAGL/GLI layer), layerdump.c, gen-dispatch.py and
ios-dispatch.txt are GPU-independent and used as they are, except the
IOSurface import, which panfrost takes as a prime fd. sweetgl.c gets the
panfrost screen; its DRM emulation (sweet_drm.c, msm) is replaced by our
sweet_drm_pan.c.
"""
import os
import re
import shutil
import sys

src, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
for f in ('eagl.c', 'eagl.h', 'gen-dispatch.py', 'ios-dispatch.txt', 'layerdump.c', 'sweetgl.c', 'sweetgl.h'):
    shutil.copy(os.path.join(src, f), os.path.join(out, f))


def edit(name, pairs, regex=()):
    p = os.path.join(out, name)
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        n = s.count(a)
        assert n == 1, '%s: %d matches for %r' % (name, n, a[:80])
        s = s.replace(a, b)
    for a, b in regex:
        s, n = re.subn(a, b, s, count=1, flags=re.S)
        assert n == 1, '%s: no match for /%s/' % (name, a[:80])
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('adapt:', name)


edit('sweetgl.c', [
    ('#include "freedreno/drm/freedreno_drm_public.h"', '#include "panfrost/drm/panfrost_drm_public.h"'),
    ('#include "freedreno/driinfo_freedreno.h"', '#include "panfrost/driinfo_panfrost.h"'),
    ('fd_drm_screen_create_renderonly(fd, NULL, &cfg)', 'panfrost_drm_screen_create(fd, &cfg)'),
    ('"sweetgl: freedreno screen creation failed"', '"sweetgl: panfrost screen creation failed"'),
    ('"MESA GLES ON THE ADRENO WORKS"', '"MESA GLES ON THE MALI WORKS"'),
], regex=[
    # the log goes through SweetMali (sweet_drm_pan.c), not /dev/null
    (r'\nvoid\nsweet_drm_log\(const char \*fmt, \.\.\.\)\n\{.*?\n\}\n', '\n'),
    # freedreno settings -> Mali-T720 ones: Mesa lists Midgard v4 as GLES 2.0,
    # CoreAnimation's GL renderer and eagl.c ask for 3.x
    (r'/\*\n\t+ \* Render straight to memory.*?setenv\("IR3_SHADER_DEBUG", "nofp16", 0\);',
     'setenv("MESA_GLES_VERSION_OVERRIDE", "3.1", 0);'),
])

# Mesa 26.2's st_api_create_context calls fscreen->get_param without a NULL
# check (st_manager.c: invalidate_on_gl_viewport); sailfish's frontend leaves
# it unset -> jump to 0 in the first context creation (backboardd crash
# loop, boot of build 40). glthread would call set_background_context.
edit('sweetgl.c', [
    ("""struct sweetgl_ctx {""",
     """static int
sweetgl_fscreen_get_param(struct pipe_frontend_screen *fs, enum st_manager_param param)
{
	(void)fs;
	(void)param;
	return 0;       /* ST_MANAGER_BROKEN_INVALIDATE: no */
}

static void
sweetgl_fscreen_set_background_context(struct st_context *st, struct util_queue_monitoring *q)
{
	(void)st;
	(void)q;
}

struct sweetgl_ctx {"""),
    ("""				sweetgl_image_hooks(fscreen);""",
     """				fscreen->get_param = sweetgl_fscreen_get_param;
				fscreen->set_background_context = sweetgl_fscreen_set_background_context;
				sweetgl_image_hooks(fscreen);"""),
])

edit('eagl.c', [
    # Panfrost on Midgard has no texture barrier: glTextureBarrier set
    # GL_INVALID_OPERATION (MESA_DEBUG boot), which the IOSurface upload
    # paths then read as their own failure and dropped the image. Ending the
    # batch makes the next draws sample what was rendered (tiler GPU).
    ('''extern void _mesa_TextureBarrierNV(void);''',
     '''/* A510F: Midgard has no texture barrier; end the batch instead (adapt.py) */
static inline void
sgl_texture_barrier(void)
{
	glFlush();
}'''),
    ('''			_mesa_TextureBarrierNV();
			return;''',
     '''			sgl_texture_barrier();
			return;'''),
    ('''	_mesa_TextureBarrierNV();
	/* SWEETGL_TRACE: the first draws of each fbfetch program''',
     '''	sgl_texture_barrier();
	/* SWEETGL_TRACE: the first draws of each fbfetch program'''),
    ("""			.type = WINSYS_HANDLE_TYPE_KMS,
			.handle = handle,""",
     """			/* panfrost imports by prime fd only (sweet_drm_pan.c) */
			.type = WINSYS_HANDLE_TYPE_FD,
			.handle = (unsigned)sweet_drm_handle_to_fd(handle),"""),
    ("""		img.res = screen->resource_from_handle(screen, &templ, &wh, PIPE_HANDLE_USAGE_FRAMEBUFFER_WRITE);""",
     """		img.res = screen->resource_from_handle(screen, &templ, &wh, PIPE_HANDLE_USAGE_FRAMEBUFFER_WRITE);
		sweet_drm_close_fd((int)wh.handle);"""),
])
