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
    # Panfrost has coherent framebuffer fetch on Midgard (pan_screen.c
    # caps->fbfetch, fbfetch_coherent): CA's blend-mode shaders keep
    # gl_LastFragData and read the tile buffer. sailfish's emulation sampled
    # the framebuffer as a texture behind a barrier, which on Midgard ended
    # the render pass: ~10 full-screen passes per frame (timing boot).
    ('''	if (strstr(src, "GL_EXT_shader_framebuffer_fetch") != NULL || strstr(src, "gl_LastFragData") != NULL) {
		src = fbfetch_rewrite(src);''',
     '''	if (!sgl_native_fbfetch() &&
	    (strstr(src, "GL_EXT_shader_framebuffer_fetch") != NULL || strstr(src, "gl_LastFragData") != NULL)) {
		src = fbfetch_rewrite(src);'''),
    ('''#define FBFETCH_UNIT 15''',
     '''#define FBFETCH_UNIT 15

/* A510F: the driver's own GL_EXT_shader_framebuffer_fetch (adapt.py), checked once */
static int
sgl_native_fbfetch(void)
{
	static int native = -1;
	if (native < 0) {
		const char *e = (const char *)glGetString(GL_EXTENSIONS);
		native = e != NULL && strstr(e, "GL_EXT_shader_framebuffer_fetch") != NULL;
		sweet_drm_log("sweetgl: framebuffer fetch %s", native ? "native (Mesa)" : "emulated");
	}
	return native;
}'''),
    # safety net: a shader the native path cannot compile gets the emulation
    ('''	SGL_CUR(rctx);
	glCompileShader(H(shader));
	GLint ok = 0;
	glGetShaderiv(H(shader), GL_COMPILE_STATUS, &ok);
	if (!ok) {''',
     '''	SGL_CUR(rctx);
	glCompileShader(H(shader));
	GLint ok = 0;
	glGetShaderiv(H(shader), GL_COMPILE_STATUS, &ok);
	if (!ok && sgl_native_fbfetch()) {
		GLint len = 0;
		glGetShaderiv(H(shader), GL_SHADER_SOURCE_LENGTH, &len);
		char *fsrc = len > 0 ? malloc((size_t)len + 1) : NULL;
		if (fsrc != NULL) {
			glGetShaderSource(H(shader), len + 1, NULL, fsrc);
			if (strstr(fsrc, "gl_LastFragData") != NULL) {
				fsrc = fbfetch_rewrite(fsrc);
				if (n_fbfetch_shaders < FBFETCH_MAX) {
					fbfetch_shaders[n_fbfetch_shaders++] = H(shader);
				}
				const GLchar *one = fsrc;
				glShaderSource(H(shader), 1, &one, NULL);
				glCompileShader(H(shader));
				glGetShaderiv(H(shader), GL_COMPILE_STATUS, &ok);
				sweet_drm_log("sweetgl: shader %u: native framebuffer fetch failed, emulated: %s",
				    H(shader), ok ? "ok" : "failed too");
			}
			free(fsrc);
		}
	}
	if (!ok) {'''),
    # draw recorder: the last 64 draws, logged (with the fragment shaders'
    # sources) when a GPU job fails (sweet_drm_pan.c submit -> sweetgl_draw_ring_dump)
    ('''/* before a draw: each unit holds what the program samples there, rect scale set */
static bool
draw_prep(GLenum mode, GLsizei count)
{
	GLint prog = 0, unit = -1, w = 0, h = 0, scale = -1;
	bool fresh = false;
	glGetIntegerv(GL_CURRENT_PROGRAM, &prog);''',
     '''/* A510F: ring of recent draws (adapt.py) */
#define RING_N 64
static struct ring_draw {
	GLint prog, fbo, vw, vh;
	GLenum mode;
	GLsizei count;
	uint32_t seq;
} ring[RING_N];
static uint32_t ring_seq;

static void
ring_note(GLint prog, GLenum mode, GLsizei count)
{
	struct ring_draw *r = &ring[ring_seq % RING_N];
	GLint vp[4] = {0};
	r->prog = prog;
	glGetIntegerv(GL_FRAMEBUFFER_BINDING, &r->fbo);
	glGetIntegerv(GL_VIEWPORT, vp);
	r->vw = vp[2];
	r->vh = vp[3];
	r->mode = mode;
	r->count = count;
	r->seq = ++ring_seq;
	/*
	 * A510F: an incomplete framebuffer makes Mesa drop the draw, or CA's
	 * offscreen passes land elsewhere (garbage at the screen's top left,
	 * black backdrops): check at the first draw into each binding.
	 */
	static GLint last_fbo = -1;
	static int fb_logged;
	if ((r->fbo != last_fbo || (ring_seq & 63) == 0) && fb_logged < 40) {
		last_fbo = r->fbo;
		GLenum st = glCheckFramebufferStatus(GL_DRAW_FRAMEBUFFER);
		if (st != GL_FRAMEBUFFER_COMPLETE) {
			GLint type = 0, name = 0, comp = 0, rs = 0, gs = 0, bs = 0, as = 0;
			if (r->fbo != 0) {
				glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
				    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE, &type);
				if (type != GL_NONE) {
					glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
					    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME, &name);
					glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
					    GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE, &comp);
					glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
					    GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE, &rs);
					glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
					    GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE, &gs);
					glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
					    GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE, &bs);
					glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
					    GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE, &as);
				}
			}
			while (glGetError() != GL_NO_ERROR) {
			}
			fb_logged++;
			sweet_drm_log("sweetgl: draw %u into INCOMPLETE fbo %d (status %#x): color0 type %#x name %d "
			    "comp %#x bits %d/%d/%d/%d, viewport %dx%d prog %d",
			    r->seq, r->fbo, st, type, name, comp, rs, gs, bs, as, r->vw, r->vh, prog);
		}
	}
	/* draws straight into the default framebuffer (CA always renders into FBOs) */
	static int fb0_logged;
	if (r->fbo == 0 && fb0_logged < 10) {
		fb0_logged++;
		sweet_drm_log("sweetgl: draw %u into fbo 0, viewport %dx%d prog %d", r->seq, r->vw, r->vh, prog);
	}
}

static int
shader_reads_fb(GLuint sh)
{
	GLint len = 0;
	glGetShaderiv(sh, GL_SHADER_SOURCE_LENGTH, &len);
	char *src = len > 0 ? malloc((size_t)len + 1) : NULL;
	int r = 0;
	if (src != NULL) {
		glGetShaderSource(sh, len + 1, NULL, src);
		r = strstr(src, "gl_LastFragData") != NULL ? 1 : strstr(src, "sgl_fb") != NULL ? 2 : 0;
		free(src);
	}
	return r;
}

/*
 * Called by sweet_drm_pan.c when a GPU job failed, i.e. inside Mesa's flush:
 * only note it; ring_dump() runs at the start of the next draw.
 */
static volatile uint32_t ring_dump_at;
void sweetgl_draw_ring_dump(void);
void
sweetgl_draw_ring_dump(void)
{
	if (ring_dump_at == 0) {
		ring_dump_at = ring_seq;
	}
}

static void
ring_dump(void)
{
	static int dumps;
	static GLint shown[16];
	static int n_shown;
	uint32_t upto = ring_dump_at;
	ring_dump_at = 0;
	if (dumps >= 6) {
		return;
	}
	dumps++;
	uint32_t first = upto > RING_N ? upto - RING_N : 0;
	sweet_drm_log("sweetgl: failed job: draws %u..%u (prog fbo vpw x vph mode count fbread):", first + 1, upto);
	for (uint32_t i = first; i < upto; i++) {
		struct ring_draw *r = &ring[i % RING_N];
		GLuint sh[4] = {0};
		GLsizei n = 0;
		int fbr = 0;
		if (r->prog > 0) {
			glGetAttachedShaders((GLuint)r->prog, 4, &n, sh);
			for (GLsizei k = 0; k < n; k++) {
				GLint type = 0;
				glGetShaderiv(sh[k], GL_SHADER_TYPE, &type);
				if (type == GL_FRAGMENT_SHADER) {
					fbr = shader_reads_fb(sh[k]);
				}
			}
		}
		sweet_drm_log("sweetgl:   %u: prog %d fbo %d %dx%d mode %u count %d fbread %d",
		    r->seq, r->prog, r->fbo, r->vw, r->vh, r->mode, r->count, fbr);
	}
	/* fragment shader sources of the programs that read the framebuffer, once each */
	for (uint32_t i = first; i < upto; i++) {
		struct ring_draw *r = &ring[i % RING_N];
		bool seen = false;
		for (int k = 0; k < n_shown; k++) {
			seen |= shown[k] == r->prog;
		}
		if (seen || r->prog <= 0 || n_shown >= 16) {
			continue;
		}
		GLuint sh[4] = {0};
		GLsizei n = 0;
		glGetAttachedShaders((GLuint)r->prog, 4, &n, sh);
		for (GLsizei k = 0; k < n; k++) {
			GLint type = 0, len = 0;
			glGetShaderiv(sh[k], GL_SHADER_TYPE, &type);
			if (type != GL_FRAGMENT_SHADER || shader_reads_fb(sh[k]) == 0) {
				continue;
			}
			shown[n_shown++] = r->prog;
			glGetShaderiv(sh[k], GL_SHADER_SOURCE_LENGTH, &len);
			char *src = len > 0 ? malloc((size_t)len + 1) : NULL;
			if (src != NULL) {
				glGetShaderSource(sh[k], len + 1, NULL, src);
				sweet_drm_log("sweetgl: prog %d fragment shader %u (%d bytes):", r->prog, sh[k], len);
				for (GLint o = 0; o < len; o += 200) {
					sweet_drm_log("sweetgl:   | %.200s", src + o);
				}
				free(src);
			}
		}
	}
}

/* before a draw: each unit holds what the program samples there, rect scale set */
static bool
draw_prep(GLenum mode, GLsizei count)
{
	GLint prog = 0, unit = -1, w = 0, h = 0, scale = -1;
	bool fresh = false;
	if (ring_dump_at != 0) {
		ring_dump();
	}
	glGetIntegerv(GL_CURRENT_PROGRAM, &prog);
	ring_note(prog, mode, count);'''),
    # QuartzCore addresses: sailfish's are for the iPhone 8 (iPhone10,1)
    # shared cache. In the iPhone 8 Plus cache of the same build (20H392)
    # QuartzCore's code and data sit 0x4000 higher (all 12 hook prologues,
    # the switch cases and tex_fragment_shaders verified against the phone's
    # cache). Detect the shift from emit_filter's prologue and add it to the
    # slide, so the texture-function fixes (App Library plates, vibrancy)
    # install instead of being skipped as "unexpected QuartzCore".
    ('''extern const void *_dyld_get_shared_cache_range(size_t *length);''',
     '''extern const void *_dyld_get_shared_cache_range(size_t *length);

/* A510F: QuartzCore's offset from sailfish's iPhone 8 cache (adapt.py) */
static uint64_t
sgl_qc_delta(const void *cache)
{
	static const uint32_t want[4] = {0xd103c3ff, 0x6d072beb, 0x6d0823e9, 0xa9096ffc};      /* emit_filter */
	static const uint64_t deltas[] = {0, 0x4000};
	static int64_t found = -1;
	if (found >= 0) {
		return (uint64_t)found;
	}
	uint64_t slide = (uint64_t)(uintptr_t)cache - 0x180000000ull;
	for (size_t i = 0; i < sizeof(deltas) / sizeof(deltas[0]); i++) {
		const uint32_t *t = (const uint32_t *)(uintptr_t)(0x188424e54ull + slide + deltas[i]);
		if (memcmp(t, want, sizeof(want)) == 0) {
			found = (int64_t)deltas[i];
			sweet_drm_log("sweetgl: QuartzCore at sailfish's addresses + %#llx", (unsigned long long)found);
			return (uint64_t)found;
		}
	}
	sweet_drm_log("sweetgl: QuartzCore not at a known offset: sailfish's own checks decide");
	found = 0;              /* their prologue/table checks then refuse to patch */
	return 0;
}'''),
    ('''	sgl_cache_slide = (uint64_t)(uintptr_t)cache - 0x180000000ull;''',
     '''	sgl_cache_slide = (uint64_t)(uintptr_t)cache - 0x180000000ull + sgl_qc_delta(cache);'''),
    ('''	uint64_t slide = (uint64_t)(uintptr_t)cache - 0x180000000ull;
	const char **table = (const char **)(uintptr_t)(0x1d5b44a10ull + slide);''',
     '''	uint64_t slide = (uint64_t)(uintptr_t)cache - 0x180000000ull + sgl_qc_delta(cache);
	const char **table = (const char **)(uintptr_t)(0x1d5b44a10ull + slide);'''),
    ("""			.type = WINSYS_HANDLE_TYPE_KMS,
			.handle = handle,""",
     """			/* panfrost imports by prime fd only (sweet_drm_pan.c) */
			.type = WINSYS_HANDLE_TYPE_FD,
			.handle = (unsigned)sweet_drm_handle_to_fd(handle),"""),
    ("""		img.res = screen->resource_from_handle(screen, &templ, &wh, PIPE_HANDLE_USAGE_FRAMEBUFFER_WRITE);""",
     """		img.res = screen->resource_from_handle(screen, &templ, &wh, PIPE_HANDLE_USAGE_FRAMEBUFFER_WRITE);
		sweet_drm_close_fd((int)wh.handle);"""),
])
