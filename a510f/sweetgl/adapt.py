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
		const char *emul = getenv("SWEETGL_FBFETCH_EMUL");      /* =1: the emulation (test) */
		native = e != NULL && strstr(e, "GL_EXT_shader_framebuffer_fetch") != NULL &&
		    !(emul != NULL && emul[0] == '1');
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
	GLint prog, fbo, vw, vh, tex0;
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
	{
		GLint a = 0;
		glGetIntegerv(GL_ACTIVE_TEXTURE, &a);
		if (a != GL_TEXTURE0) {
			glActiveTexture(GL_TEXTURE0);
		}
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &r->tex0);
		if (a != GL_TEXTURE0) {
			glActiveTexture((GLenum)a);
		}
	}
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

# Variable blur (CAFilter variableBlur: the App Library header, bars over
# scrolled content). eagl.c draws nothing for the 0x26 mip passes (sgl_nop)
# and blurs surface S in one 0x27 pass; the App Library header comes out
# black. Log where each 0x26/0x27 pass draws and what it samples, and with
# SWEETGL_VBLUR_COPY=1 let the 0x26 passes copy texture0 instead (test).
edit('eagl.c', [
    ('''static char *
texfn_rewrite(char *src)
{''', '''static const char nop_copy_func[] =
    "lowp vec4 sgl_nop() {\\n"
    "  return texture2D(texture0, texcoord0_0);\\n"
    "}\\n";

static const char *
sgl_nop_src(void)
{
	static int copy = -1;
	if (copy < 0) {
		const char *e = getenv("SWEETGL_VBLUR_COPY");
		copy = e != NULL && e[0] == '1';
	}
	return copy ? nop_copy_func : nop_func;
}

static char *
texfn_rewrite(char *src)
{'''),
    ('''strstr(src, "sgl_nop(") ? nop_func : ""''', '''strstr(src, "sgl_nop(") ? sgl_nop_src() : ""'''),
    ('''static void
ring_note(GLint prog, GLenum mode, GLsizei count)
{''', '''/* the last draw that rendered into each texture name, and through which fbo */
static uint32_t tex_last_draw[8192];
static GLint tex_last_fbo[8192];
static GLint copy_src_of[8192];

/* 1: the program's fragment shader uses sgl_nop (0x26), 2: sgl_vblur (0x27), 0: neither */
static int
prog_texfn_kind(GLint prog)
{
	static int8_t kind[8192];
	if (prog <= 0 || prog >= 8192) {
		return 0;
	}
	if (kind[prog] == 0) {
		int k = 3;
		GLuint sh[4];
		GLsizei n = 0;
		glGetAttachedShaders((GLuint)prog, 4, &n, sh);
		for (GLsizei i = 0; i < n; i++) {
			GLint type = 0, len = 0;
			glGetShaderiv(sh[i], GL_SHADER_TYPE, &type);
			if (type != GL_FRAGMENT_SHADER) {
				continue;
			}
			glGetShaderiv(sh[i], GL_SHADER_SOURCE_LENGTH, &len);
			char *s = len > 0 ? malloc((size_t)len + 1) : NULL;
			if (s != NULL) {
				glGetShaderSource(sh[i], len + 1, NULL, s);
				k = strstr(s, "sgl_nop(") ? 1 : strstr(s, "sgl_vblur(") ? 2 : 3;
				free(s);
			}
		}
		kind[prog] = (int8_t)k;
	}
	return kind[prog] == 3 ? 0 : kind[prog];
}

static void
ring_note(GLint prog, GLenum mode, GLsizei count)
{'''),
    ('''	r->seq = ++ring_seq;
''', '''	r->seq = ++ring_seq;
	/* which texture each draw renders into (re-read when the fbo binding changes) */
	{
		static GLint att_fbo = -1, att_tex;
		if (r->fbo != att_fbo) {
			GLint t = 0, nm = 0;
			att_fbo = r->fbo;
			if (r->fbo != 0) {
				glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
				    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE, &t);
				if (t == GL_TEXTURE) {
					glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
					    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME, &nm);
				}
			}
			att_tex = nm;
		}
		if (att_tex > 0 && att_tex < 8192) {
			tex_last_draw[att_tex] = r->seq;
			tex_last_fbo[att_tex] = r->fbo;
			/* an ordinary draw into a texture: what it copied (variable blur source, below) */
			if (r->tex0 > 0 && prog_texfn_kind(prog) == 0) {
				copy_src_of[att_tex] = r->tex0;
			}
		}
	}
	/*
	 * Variable blur passes (0x26 mip passes, 0x27 blur): CA samples surface
	 * S with a mipmap filter, but GLES surfaces here have level 0 only, so S
	 * is mipmap-incomplete and every texel reads black (App Library header
	 * black when scrolled). Make the sampled textures complete with one level.
	 */
	int vb = prog_texfn_kind(prog);
	GLint vb_min[2] = {0, 0};
	/*
	 * Variable blur (App Library header and bars over scrolled content): CA
	 * copies the backdrop into S, then before each 0x26 mip pass clears the
	 * framebuffer of S, which on Apple's GPUs targets the next mip level.
	 * Here S has level 0 only, so the clears wiped it and the 0x27 blur read
	 * nothing (black header, round 21 trace). The blur reads the texture the
	 * copy came from instead: the same pixels S held before the clears.
	 */
	if (vb == 2) {
		GLint act0 = 0, t = 0;
		glGetIntegerv(GL_ACTIVE_TEXTURE, &act0);
		glActiveTexture(GL_TEXTURE0);
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &t);
		if (0 && t > 0 && t < 8192 && copy_src_of[t] > 0) {      /* not needed since the held clears keep S */
			glBindTexture(GL_TEXTURE_2D, (GLuint)copy_src_of[t]);
			static int told;
			if (told++ < 3) {
				sweet_drm_log("sweetgl: variable blur reads %d (the copy source of %d, cleared by the mip passes)",
				    copy_src_of[t], t);
			}
		}
		glActiveTexture((GLenum)act0);
	}
	if (vb) {
		GLint act0 = 0;
		glGetIntegerv(GL_ACTIVE_TEXTURE, &act0);
		for (int u = 0; u < 2; u++) {
			GLint t = 0;
			glActiveTexture(GL_TEXTURE0 + u);
			glGetIntegerv(GL_TEXTURE_BINDING_2D, &t);
			if (t != 0) {
				glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, &vb_min[u]);
				if (vb_min[u] != GL_NEAREST && vb_min[u] != GL_LINEAR) {
					glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0);
				}
			}
		}
		glActiveTexture((GLenum)act0);
	}
	/* where they draw, what they sample */
	static int vb_logged;
	if (vb && vb_logged < 120) {
		GLint at = 0, name = 0, t0 = 0, t1 = 0, act = 0;
		if (r->fbo != 0) {
			glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
			    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE, &at);
			if (at == GL_TEXTURE) {
				glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
				    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME, &name);
			}
		}
		glGetIntegerv(GL_ACTIVE_TEXTURE, &act);
		glActiveTexture(GL_TEXTURE0);
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &t0);
		glActiveTexture(GL_TEXTURE1);
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &t1);
		glActiveTexture((GLenum)act);
		while (glGetError() != GL_NO_ERROR) {
		}
		vb_logged++;
		/* the first few blur passes: what S (tex0) and the mask (tex1) hold, and the draws before */
		static int vb_read;
		if (vb == 2 && vb_read < 6) {
			vb_read++;
			for (int k = 6; k >= 1; k--) {
				struct ring_draw *q = &ring[(ring_seq - (uint32_t)k) % RING_N];
				sweet_drm_log("sweetgl:   before: draw %u prog %d kind %d fbo %d viewport %dx%d mode %#x count %d tex0 %d",
				    q->seq, q->prog, prog_texfn_kind(q->prog), q->fbo, q->vw, q->vh, q->mode, q->count, q->tex0);
			}
			GLint keep_draw = 0, keep_read = 0;
			glGetIntegerv(GL_DRAW_FRAMEBUFFER_BINDING, &keep_draw);
			glGetIntegerv(GL_READ_FRAMEBUFFER_BINDING, &keep_read);
			GLuint tmp = 0;
			glGenFramebuffers(1, &tmp);
			glBindFramebuffer(GL_READ_FRAMEBUFFER, tmp);
			/* the copy into S: the last ordinary draw before the mip passes */
			GLint copy_src = 0;
			for (uint32_t k = 1; k <= 8; k++) {
				struct ring_draw *q = &ring[(ring_seq - k) % RING_N];
				if (prog_texfn_kind(q->prog) == 0) {
					copy_src = q->tex0;
					break;
				}
			}
			GLint tex[3] = {t0, t1, copy_src};
			for (int u = 0; u < 3; u++) {
				if (tex[u] == 0) {
					continue;
				}
				glFramebufferTexture2D(GL_READ_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, (GLuint)tex[u], 0);
				GLenum st = glCheckFramebufferStatus(GL_READ_FRAMEBUFFER);
				uint8_t px[5][4];
				memset(px, 0, sizeof(px));
				if (st == GL_FRAMEBUFFER_COMPLETE) {
					GLint w = r->vw, h = r->vh;
					GLint pts[5][2] = {{w / 2, h / 2}, {w / 4, h / 4}, {3 * w / 4, h / 4}, {w / 2, h - 8}, {w / 2, 8}};
					for (int i = 0; i < 5; i++) {
						glReadPixels(pts[i][0], pts[i][1], 1, 1, GL_RGBA, GL_UNSIGNED_BYTE, px[i]);
					}
				}
				sweet_drm_log("sweetgl:   %s %d (status %#x) rgba: %02x%02x%02x%02x %02x%02x%02x%02x %02x%02x%02x%02x "
				    "%02x%02x%02x%02x %02x%02x%02x%02x", u == 0 ? "S (tex0)" : u == 1 ? "mask (tex1)" : "copy source", tex[u], st,
				    px[0][0], px[0][1], px[0][2], px[0][3], px[1][0], px[1][1], px[1][2], px[1][3],
				    px[2][0], px[2][1], px[2][2], px[2][3], px[3][0], px[3][1], px[3][2], px[3][3],
				    px[4][0], px[4][1], px[4][2], px[4][3]);
			}
			if (copy_src > 0 && copy_src < 8192) {
				if (tex_last_draw[copy_src]) {
					sweet_drm_log("sweetgl:   copy source %d last rendered by draw %u (%u draws ago) into fbo %d",
					    copy_src, tex_last_draw[copy_src], ring_seq - tex_last_draw[copy_src], tex_last_fbo[copy_src]);
				} else {
					sweet_drm_log("sweetgl:   copy source %d never rendered by GL (uploaded or imported surface)",
					    copy_src);
				}
			}
			glBindFramebuffer(GL_READ_FRAMEBUFFER, (GLuint)keep_read);
			glBindFramebuffer(GL_DRAW_FRAMEBUFFER, (GLuint)keep_draw);
			glDeleteFramebuffers(1, &tmp);
			while (glGetError() != GL_NO_ERROR) {
			}
		}
		sweet_drm_log("sweetgl: draw %u %s: fbo %d color0 %s %d, viewport %dx%d, tex0 %d tex1 %d, min filters %#x/%#x%s",
		    r->seq, vb == 1 ? "0x26 mip pass" : "0x27 vblur", r->fbo,
		    at == GL_TEXTURE ? "tex" : at == GL_RENDERBUFFER ? "rb" : "none", name, r->vw, r->vh, t0, t1,
		    vb_min[0], vb_min[1],
		    name != 0 && (name == t0 || name == t1) ? " (samples its own target)" : "");
	}
'''),
])

# App Library header (variable blur reads an empty copy): trace windows open on
# the variable blur's 1194x1164 viewport only, every 15 s.
edit('eagl.c', [
    ('''#define WIN_SECS 30''', '''#define WIN_SECS 15'''),
    ('''#define WIN_TRIGGER(w, h) (((w) == 138 && (h) == 306) || ((w) == 296 && (h) == 296) || ((w) == 297 && (h) == 296))''',
     '''#define WIN_TRIGGER(w, h) ((w) == 1194 && (h) == 1164)'''),
])

# Round 21 trace: windows only from SWEETGL_TRACE=N s after backboardd's
# start (the App Library scroll), every 3 s, 300 draws; thumbnails also for the
# 1194x1164 App Library surfaces (up to 1.5 Mpx, was 250 kpx).
edit('eagl.c', [
    ('''#define WIN_SECS 15''', '''#define WIN_SECS 3'''),
    ('''#define WIN_DRAWS 500''', '''#define WIN_DRAWS 300'''),
    ('''(size_t)r[2] * (size_t)r[3] > 250000) {''', '''(size_t)r[2] * (size_t)r[3] > 1500000) {'''),
    ('''	trace_left = t && t[0] == '1' ? 20000 : 0;''', '''	/* SWEETGL_TRACE=1: trace; =N (N > 1): trace, windows from N s after start */
	trace_left = t && atoi(t) > 0 ? 20000 : 0;
	if (t && atoi(t) > 1) {
		struct timespec ts;
		clock_gettime(CLOCK_MONOTONIC, &ts);
		win_next = ts.tv_sec + atoi(t);
	}'''),
])


# Variable blur, round 29 (user: "the App Library search field blur looks weird";
# search pull-down: black blocks in the status bar).
# 1. Clears of a variable blur's source S are held until the next draw and
#    dropped when that draw is a 0x26 mip pass on S (they wiped S's only
#    level; covers sources filled by copies sweetgl does not see as draws).
# 2. Before the 0x27 pass the sampled texture gets a real mip chain, and
#    sgl_vblur reads the level that matches the radius (5 bilinear taps,
#    trilinear) instead of 24 full-resolution taps (grainy, doubled edges).
edit('eagl.c', [
    ('''static const char vblur_func[] =''', '''static const char vblur_func_old[] ='''),
    ('''static const char nop_copy_func[] =''', '''static const char vblur_func[] =
    "uniform highp vec4 minmax_dir;\\n"
    "lowp vec4 sgl_vblur(lowp vec4 m) {\\n"
    "  highp vec2 tc = texcoord0_0;\\n"
    "  highp vec2 px = vec2(length(vec2(dFdx(tc.x), dFdy(tc.x))), length(vec2(dFdx(tc.y), dFdy(tc.y))));\\n"
    "  mediump float r = (minmax_dir.y > .5 ? 1. - m.a : m.a) * minmax_dir.x * .5;\\n"
    "  if (r < .75) {\\n"
    "    return texture2D(texture0, tc);\\n"
    "  }\\n"
    "  mediump float b = max(log2(r) - 1., 0.);\\n"
    "  highp vec2 d = .55 * r * px;\\n"
    "  mediump vec4 acc = 2. * texture2D(texture0, tc, b);\\n"
    "  acc += texture2D(texture0, tc + vec2(d.x, d.y), b);\\n"
    "  acc += texture2D(texture0, tc + vec2(-d.x, d.y), b);\\n"
    "  acc += texture2D(texture0, tc + vec2(d.x, -d.y), b);\\n"
    "  acc += texture2D(texture0, tc + vec2(-d.x, -d.y), b);\\n"
    "  return acc / 6.;\\n"
    "}\\n";

static const char nop_copy_func[] ='''),
    ('''static GLint copy_src_of[8192];''', '''static GLint copy_src_of[8192];
static GLint vb_restore_tex, vb_restore_min;
static uint8_t is_blur_s[8192];         /* textures a 0x26 mip pass drew into */
static struct {
	int on;
	GLint fb;
	GLbitfield mask;
	GLfloat cc[4];
	GLboolean sc_on;
	GLint sc[4];
} pend_clear;

/* run a held clear now, with the clear colour and scissor it was issued with */
static void
pend_clear_apply(void)
{
	if (!pend_clear.on) {
		return;
	}
	pend_clear.on = 0;
	GLint cur = 0, sc[4] = {0};
	GLfloat cc[4] = {0};
	GLboolean on = glIsEnabled(GL_SCISSOR_TEST);
	glGetIntegerv(GL_DRAW_FRAMEBUFFER_BINDING, &cur);
	glGetFloatv(GL_COLOR_CLEAR_VALUE, cc);
	glGetIntegerv(GL_SCISSOR_BOX, sc);
	if (cur != pend_clear.fb) {
		glBindFramebuffer(GL_DRAW_FRAMEBUFFER, (GLuint)pend_clear.fb);
	}
	glClearColor(pend_clear.cc[0], pend_clear.cc[1], pend_clear.cc[2], pend_clear.cc[3]);
	if (pend_clear.sc_on) {
		glEnable(GL_SCISSOR_TEST);
		glScissor(pend_clear.sc[0], pend_clear.sc[1], pend_clear.sc[2], pend_clear.sc[3]);
	} else {
		glDisable(GL_SCISSOR_TEST);
	}
	glClear(pend_clear.mask);
	glClearColor(cc[0], cc[1], cc[2], cc[3]);
	glScissor(sc[0], sc[1], sc[2], sc[3]);
	if (on) {
		glEnable(GL_SCISSOR_TEST);
	} else {
		glDisable(GL_SCISSOR_TEST);
	}
	if (cur != pend_clear.fb) {
		glBindFramebuffer(GL_DRAW_FRAMEBUFFER, (GLuint)cur);
	}
}'''),
    ('''	r->seq = ++ring_seq;
	/* which texture each draw renders into''', '''	r->seq = ++ring_seq;
	/* a held clear: dropped before a 0x26 pass on the same fbo, otherwise run first */
	if (pend_clear.on) {
		if (prog_texfn_kind(prog) == 1 && r->fbo == pend_clear.fb) {
			pend_clear.on = 0;
		} else {
			pend_clear_apply();
		}
	}
	/* which texture each draw renders into'''),
    ('''			if (r->tex0 > 0 && prog_texfn_kind(prog) == 0) {
				copy_src_of[att_tex] = r->tex0;
			}''', '''			if (r->tex0 > 0 && prog_texfn_kind(prog) == 0) {
				copy_src_of[att_tex] = r->tex0;
			}
			if (prog_texfn_kind(prog) == 1) {
				is_blur_s[att_tex] = 1;
			}'''),
    ('''	int vb = prog_texfn_kind(prog);
	GLint vb_min[2] = {0, 0};''', '''	/* the previous draw was a variable blur: its source's filter back to what CA set */
	if (vb_restore_tex > 0) {
		GLint act1 = 0, keep = 0;
		glGetIntegerv(GL_ACTIVE_TEXTURE, &act1);
		glActiveTexture(GL_TEXTURE0);
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &keep);
		glBindTexture(GL_TEXTURE_2D, (GLuint)vb_restore_tex);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, vb_restore_min);
		glBindTexture(GL_TEXTURE_2D, (GLuint)keep);
		glActiveTexture((GLenum)act1);
		vb_restore_tex = 0;
	}
	int vb = prog_texfn_kind(prog);
	GLint vb_min[2] = {0, 0};'''),
    ('''				sweet_drm_log("sweetgl: variable blur reads %d (the copy source of %d, cleared by the mip passes)",
				    copy_src_of[t], t);
			}
		}''', '''				sweet_drm_log("sweetgl: variable blur reads %d (the copy source of %d, cleared by the mip passes)",
				    copy_src_of[t], t);
			}
		}
		/*
		 * The level-based blur needs a mip chain. Not on CA's own texture:
		 * mips on an imported IOSurface texture made Mesa reallocate it
		 * (round 29: black screen and a white rounded shape mid-animation).
		 * Copy the source into a private mipmapped texture and blur that.
		 */
		GLint st = 0;
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &st);
		GLint vw = r->vw, vh = r->vh;
		static GLuint priv, rfb;
		static GLint pw, ph;
		if (st > 0 && vw > 0 && vh > 0) {
			if (priv == 0 || pw != vw || ph != vh) {
				if (priv != 0) {
					glDeleteTextures(1, &priv);
				}
				GLint levels = 1;
				for (GLint m = vw > vh ? vw : vh; m > 1; m >>= 1) {
					levels++;
				}
				glGenTextures(1, &priv);
				glBindTexture(GL_TEXTURE_2D, priv);
				glTexStorage2D(GL_TEXTURE_2D, levels, GL_RGBA8, vw, vh);
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
				glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
				pw = vw;
				ph = vh;
			}
			if (rfb == 0) {
				glGenFramebuffers(1, &rfb);
			}
			GLint keep_read = 0;
			glGetIntegerv(GL_READ_FRAMEBUFFER_BINDING, &keep_read);
			glBindFramebuffer(GL_READ_FRAMEBUFFER, rfb);
			glFramebufferTexture2D(GL_READ_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, (GLuint)st, 0);
			if (glCheckFramebufferStatus(GL_READ_FRAMEBUFFER) == GL_FRAMEBUFFER_COMPLETE) {
				glBindTexture(GL_TEXTURE_2D, priv);
				glCopyTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 0, 0, vw, vh);
				glGenerateMipmap(GL_TEXTURE_2D);
			} else {
				glBindTexture(GL_TEXTURE_2D, (GLuint)st);
			}
			glBindFramebuffer(GL_READ_FRAMEBUFFER, (GLuint)keep_read);
			while (glGetError() != GL_NO_ERROR) {
			}
		}'''),
    ('''	glClear(mask);
	SGL_POST(10);''', '''	/* a variable blur source: hold the clear (see pend_clear) */
	if (fb != 0 && mask == GL_COLOR_BUFFER_BIT) {
		GLint at = 0, nm = 0;
		glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
		    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE, &at);
		if (at == GL_TEXTURE) {
			glGetFramebufferAttachmentParameteriv(GL_DRAW_FRAMEBUFFER, GL_COLOR_ATTACHMENT0,
			    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME, &nm);
		}
		if (nm > 0 && nm < 8192 && is_blur_s[nm]) {
			pend_clear_apply();
			pend_clear.on = 1;
			pend_clear.fb = fb;
			pend_clear.mask = mask;
			memcpy(pend_clear.cc, cc, sizeof(cc));
			pend_clear.sc_on = glIsEnabled(GL_SCISSOR_TEST);
			memcpy(pend_clear.sc, sc, sizeof(sc));
			SGL_POST(10);
			return;
		}
	}
	glClear(mask);
	SGL_POST(10);'''),
])
