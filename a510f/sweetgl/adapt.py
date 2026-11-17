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
		if (nm > 0 && nm < 8192 && (is_blur_s[nm] || (cc[0] == 0 && cc[1] == 0 && cc[2] == 0 && cc[3] == 0))) {
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


# held clears (variable blur): run before a framebuffer switch, a flush, a finish
edit('eagl.c', [
    ('''	WTRACE("BindFramebuffer %u", framebuffer);
	glBindFramebuffer(target, framebuffer);''', '''	WTRACE("BindFramebuffer %u", framebuffer);
	if (pend_clear.on && (GLint)framebuffer != pend_clear.fb) {
		pend_clear_apply();
	}
	glBindFramebuffer(target, framebuffer);'''),
    ('''sgl_Flush(void *rctx)
{
	SGL_CUR(rctx);''', '''sgl_Flush(void *rctx)
{
	SGL_CUR(rctx);
	pend_clear_apply();'''),
    ('''sgl_FinishObjectAPPLE(void *rctx, GLenum object, GLint name)
{
	(void)object;
	(void)name;
	SGL_CUR(rctx);
	glFinish();''', '''sgl_FinishObjectAPPLE(void *rctx, GLenum object, GLint name)
{
	(void)object;
	(void)name;
	SGL_CUR(rctx);
	pend_clear_apply();
	glFinish();'''),
])


# The 0x26 mip passes draw nothing (sgl_nop discards): do not send them. The
# queued GPU jobs that fail with DATA_INVALID all render into the 1056x1068
# variable-blur surface (their FBD; round 32), i.e. batches of only these
# discard-everything draws (+ the held clears, dropped before them).
edit('eagl.c', [
    ('''static GLint copy_src_of[8192];''', '''static GLint copy_src_of[8192];
static bool sgl_skip_draw;              /* ring_note: this draw is a 0x26 pass, skip it */'''),
    ('''	int vb = prog_texfn_kind(prog);
	GLint vb_min[2] = {0, 0};''', '''	int vb = prog_texfn_kind(prog);
	GLint vb_min[2] = {0, 0};
	sgl_skip_draw = vb == 1;'''),
    ('''	glDrawArrays(mode, first, count);''', '''	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(65);
		return;
	}
	glDrawArrays(mode, first, count);'''),
    ('''	glDrawElements(mode, count, type, indices);''', '''	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(67);
		return;
	}
	glDrawElements(mode, count, type, indices);'''),
])


# Variable blur direction: round 32 full-resolution strips show the App Library
# header's blur weak at the top (icons behind the status bar almost sharp) and
# strong at its bottom edge (a dark line where the taps leave the copied area):
# the reverse of iOS. SWEETGL_VBLUR_FLIP (default 1) flips the mask direction.
edit('eagl.c', [
    ('''static const char nop_copy_func[] =''', '''static const char *
sgl_vblur_src(void)
{
	static char *flipped;
	static int flip = -1;
	if (flip < 0) {
		const char *e = getenv("SWEETGL_VBLUR_FLIP");
		flip = !(e != NULL && e[0] == '0');
	}
	if (!flip) {
		return vblur_func;
	}
	if (flipped == NULL) {
		const char *a = "(minmax_dir.y > .5 ? 1. - m.a : m.a)";
		const char *at = strstr(vblur_func, a);
		size_t n = strlen(vblur_func);
		flipped = malloc(n + 8);
		if (flipped == NULL || at == NULL) {
			return vblur_func;
		}
		size_t pre = (size_t)(at - vblur_func);
		memcpy(flipped, vblur_func, pre);
		strcpy(flipped + pre, "(minmax_dir.y > .5 ? m.a : 1. - m.a)");
		strcat(flipped, at + strlen(a));
	}
	return flipped;
}

static const char nop_copy_func[] ='''),
    ('''strstr(src, "sgl_vblur(") ? vblur_func : ""''', '''strstr(src, "sgl_vblur(") ? sgl_vblur_src() : ""'''),
])


# Round 36: the scrolled App Library header showed one full-width row about
# 20% darker (output row 281) at the variable blur's bottom edge: the backdrop
# copy's last row is partly transparent, and the blurred (or plain) sample
# carried that alpha into an opaque backdrop. Backdrops are opaque: a sample
# with some alpha is un-premultiplied and made opaque (fully transparent
# samples stay as they are).
edit('eagl.c', [
    ('''    "  if (r < .75) {\\n"
    "    return texture2D(texture0, tc);\\n"
    "  }\\n"''', '''    "  if (r < .75) {\\n"
    "    mediump vec4 c = texture2D(texture0, tc);\\n"
    "    return c.a > .02 ? vec4(c.rgb / c.a, 1.) : c;\\n"
    "  }\\n"'''),
    ('''    "  return acc / 6.;\\n"''', '''    "  acc /= 6.;\\n"
    "  return acc.a > .02 ? vec4(acc.rgb / acc.a, 1.) : acc;\\n"'''),
])


# Round 41: YUV (multi-plane) IOSurfaces as textures. The app switcher's
# background (wallpaper poster snapshots, 420f) is black and app card previews
# (snapshots, 420f) are blank: bind_surface refused every multi-plane surface.
# A plane is now a texture of its own: the GL format CA asks for (LUMINANCE /
# LUMINANCE_ALPHA / RED / RG), else R8 for 1-byte and RG8 for 2-byte elements,
# at the plane's offset inside the surface's buffer. Logged: the GL extension
# string once, and the first 40 multi-plane binds. SWEETGL_DUMPSH=1: shader
# sources (the weather widget's gradient banding: find its shader).
edit('eagl.c', [
    ('''		if (ext == NULL && asprintf(&ext, "%s GL_EXT_shader_framebuffer_fetch", s) < 0) {''',
     '''		if (ext == NULL) {
			sweet_drm_log("sweetgl: GL_EXTENSIONS (%zu bytes): %.380s", strlen((const char *)s), (const char *)s);
			if (strlen((const char *)s) > 380) {
				sweet_drm_log("sweetgl: GL_EXTENSIONS ...%.400s", (const char *)s + 380);
			}
		}
		if (ext == NULL && asprintf(&ext, "%s GL_EXT_shader_framebuffer_fetch%s", s,
		    strstr((const char *)s, "GL_EXT_texture_rg") ? "" : " GL_EXT_texture_rg") < 0) {'''),
    ('''	bool multi = IOSurfaceGetPlaneCount(s) > 1 || plane != 0;   /* ponytail: YUV surfaces not yet */
	img.format = format && !multi ? gl_format(format, type, &img.internalformat) : PIPE_FORMAT_NONE;
	if (img.format == PIPE_FORMAT_NONE && !multi) {
		img.format = surface_format(fourcc, IOSurfaceGetBytesPerElementOfPlane(s, plane), &img.internalformat);
	}''', '''	bool multi = IOSurfaceGetPlaneCount(s) > 1 || plane != 0;   /* YUV: one plane per texture */
	img.format = format ? gl_format(format, type, &img.internalformat) : PIPE_FORMAT_NONE;
	if (img.format == PIPE_FORMAT_NONE && !multi) {
		img.format = surface_format(fourcc, IOSurfaceGetBytesPerElementOfPlane(s, plane), &img.internalformat);
	} else if (img.format == PIPE_FORMAT_NONE) {
		size_t pbpe = IOSurfaceGetBytesPerElementOfPlane(s, plane);
		img.format = pbpe == 1 ? gl_format(GL_RED, GL_UNSIGNED_BYTE, &img.internalformat) :
		    pbpe == 2 ? gl_format(GL_RG, GL_UNSIGNED_BYTE, &img.internalformat) : PIPE_FORMAT_NONE;
	}
	if (multi) {
		static int ylog;
		if (ylog++ < 40) {
			sweet_drm_log("sweetgl: %s: YUV surface %u %c%c%c%c plane %u/%zu %zux%zu pitch %zu bpe %zu at +%#lx, GL fmt %#x type %#x -> pipe %d",
			    why, IOSurfaceGetID(s), FCC(fourcc), plane, IOSurfaceGetPlaneCount(s), w, h, pitch,
			    IOSurfaceGetBytesPerElementOfPlane(s, plane),
			    (unsigned long)((uintptr_t)IOSurfaceGetBaseAddressOfPlane(s, plane) - (uintptr_t)IOSurfaceGetBaseAddress(s)),
			    format, type, img.format);
		}
	}'''),
    ('''			.offset = (unsigned)((uintptr_t)IOSurfaceGetBaseAddressOfPlane(s, plane) & vm_page_mask),''',
     '''			.offset = (unsigned)(((uintptr_t)IOSurfaceGetBaseAddressOfPlane(s, plane) -
			    (uintptr_t)IOSurfaceGetBaseAddress(s)) + ((uintptr_t)IOSurfaceGetBaseAddress(s) & vm_page_mask)),'''),
    ('''	dump_shaders = trace_left > 0;''', '''	dump_shaders = trace_left > 0 || getenv("SWEETGL_DUMPSH") != NULL;'''),
])


# Round 42 trace: windows also on full-screen draws (1242x2208), for the
# weather widget gradient (CA dithers with a 32x32 noise texture and
# noise_scale: values?) and the app switcher's black background.
edit('eagl.c', [
    ('''#define WIN_TRIGGER(w, h) ((w) == 1194 && (h) == 1164)''',
     '''#define WIN_TRIGGER(w, h) (((w) == 1194 && (h) == 1164) || ((w) == 1242 && (h) == 2208))'''),
])


# Round 43: the weather widget's gradient goes through CA's color-matching
# shader (uniform colorP0): a 32x32x32 LUT flattened into a 32x1024 RGBA16F
# texture, looked up with mediump (fp16 on Mali) coordinates. In a 1024-row
# texture fp16 resolves only about half a row near 1.0, so neighbouring
# shades collapse onto the same LUT position: ~9 visible bands. Shaders with
# colorP0 now run at highp (fp32) throughout.
edit('eagl.c', [
    ('''	const GLchar *one = src;
	glShaderSource(H(shader), 1, &one, NULL);
	free(src);
}''', '''	if (strstr(src, "colorP0") != NULL) {
		src = sgl_all_highp(src);
	}
	const GLchar *one = src;
	glShaderSource(H(shader), 1, &one, NULL);
	free(src);
}'''),
    ('''static char *
texfn_rewrite(char *src)''', '''/* every lowp / mediump qualifier of src becomes highp (frees src) */
static char *
sgl_all_highp(char *src)
{
	size_t n = strlen(src), extra = 0;
	for (const char *p = src; (p = strstr(p, "lowp")) != NULL; p += 4) {
		extra += 1;
	}
	char *out = malloc(n + extra + 1), *o = out;
	if (out == NULL) {
		return src;
	}
	for (const char *p = src; *p;) {
		if (strncmp(p, "mediump", 7) == 0) {
			memcpy(o, "highp", 5);
			o += 5;
			p += 7;
		} else if (strncmp(p, "lowp", 4) == 0) {
			memcpy(o, "highp", 5);
			o += 5;
			p += 4;
		} else {
			*o++ = *p++;
		}
	}
	*o = 0;
	free(src);
	return out;
}

static char *
texfn_rewrite(char *src)'''),
])


# Round 44: with tracing on from the start, SpringBoard missed every home
# double press (rounds 42-43c: no app switcher). SWEETGL_TRACE=N (N > 1) now
# leaves tracing off entirely until N s after the start, then traces windows.
edit('eagl.c', [
    ('''	if (t && atoi(t) > 1) {
		struct timespec ts;
		clock_gettime(CLOCK_MONOTONIC, &ts);
		win_next = ts.tv_sec + atoi(t);
	}''', '''	if (t && atoi(t) > 1) {
		struct timespec ts;
		clock_gettime(CLOCK_MONOTONIC, &ts);
		win_next = ts.tv_sec + atoi(t);
		trace_left = 0;                 /* switched on at win_next (window_draw) */
		trace_late = true;
	}'''),
    ('''	if (trace_left <= 0) {
		return false;
	}
	if (win_left > 0 && --win_left > 0) {''', '''	if (trace_late && trace_left <= 0) {
		clock_gettime(CLOCK_MONOTONIC, &t);
		if (t.tv_sec >= win_next) {
			trace_late = false;
			trace_left = 20000;
		}
	}
	if (trace_left <= 0) {
		return false;
	}
	if (win_left > 0 && --win_left > 0) {'''),
    ('''static time_t win_next;''', '''static time_t win_next;
static bool trace_late;         /* SWEETGL_TRACE=N: tracing waits for win_next */'''),
])


# Round 45: the app switcher draws its background from one texture, opaque
# over the whole screen (round 44c trace: prog 17, then a 25% black dim), and
# that texture is black. It is made before any trace can run (tracing earlier
# loses the home double press). Every large texture upload (>= 600k pixels:
# a few per boot) is now logged always: source (IOSurface id/format, copy or
# TexImage2D), size, GL texture, and the mean of an 8x8 grid of its pixels.
edit('eagl.c', [
    ('''static char *
sgl_all_highp(char *src)''', '''/* mean of an 8x8 grid of 4-byte pixels, as "b0 b1 b2 b3" (memory order) */
static void
sgl_grid_mean(const uint8_t *base, size_t w, size_t h, size_t pitch, char *out, size_t outlen)
{
	unsigned sum[4] = {0, 0, 0, 0};
	if (base == NULL || w < 8 || h < 8) {
		snprintf(out, outlen, "no data");
		return;
	}
	for (int gy = 0; gy < 8; gy++) {
		for (int gx = 0; gx < 8; gx++) {
			const uint8_t *p = base + (h * (2 * (size_t)gy + 1) / 16) * pitch + (w * (2 * (size_t)gx + 1) / 16) * 4;
			for (int c = 0; c < 4; c++) {
				sum[c] += p[c];
			}
		}
	}
	snprintf(out, outlen, "%02x %02x %02x %02x", sum[0] / 64, sum[1] / 64, sum[2] / 64, sum[3] / 64);
}

static char *
sgl_all_highp(char *src)'''),
    ('''	glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels);
	SGL_POST(301);''', '''	if ((size_t)width * (size_t)height >= 600000) {
		static int biglog;
		if (biglog++ < 60) {
			char mean[32];
			GLint row = unpack_row();
			sgl_grid_mean(pixels != NULL && type == GL_UNSIGNED_BYTE && (format == GL_RGBA || format == GL_BGRA_EXT) ?
			    pixels : NULL, (size_t)width, (size_t)height,
			    (size_t)(row > 0 ? row : width) * 4, mean, sizeof(mean));
			sweet_drm_log("sweetgl: BIG TexImage2D tex %u level %d ifmt %#x %dx%d fmt %#x type %#x data %s mean %s",
			    unit_held[active_unit()], level, internalformat, width, height, format, type,
			    pixels ? "yes" : "none", mean);
		}
	}
	glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels);
	SGL_POST(301);'''),
    ('''	if (trace_left > 0) {
		const uint8_t *base = IOSurfaceGetBaseAddress(s);
		const uint8_t *c = base ? base + (h / 2) * pitch + (w / 2) * IOSurfaceGetBytesPerElement(s) : NULL;''', '''	if (w * h >= 600000) {
		static int biglog;
		if (biglog++ < 60) {
			char mean[32];
			GLint btex = 0;
			glGetIntegerv(GL_TEXTURE_BINDING_2D, &btex);
			sgl_grid_mean(IOSurfaceGetBytesPerElement(s) == 4 ? IOSurfaceGetBaseAddress(s) : NULL, w, h, pitch, mean, sizeof(mean));
			sweet_drm_log("sweetgl: BIG %s surf %u %c%c%c%c %zux%zu pitch %zu fmt %#x/%#x -> tex %d mean %s",
			    why, IOSurfaceGetID(s), FCC(fourcc), w, h, pitch, format, type, btex, mean);
		}
	}
	if (trace_left > 0) {
		const uint8_t *base = IOSurfaceGetBaseAddress(s);
		const uint8_t *c = base ? base + (h / 2) * pitch + (w / 2) * IOSurfaceGetBytesPerElement(s) : NULL;'''),
    ('''	size_t bpe = IOSurfaceGetBytesPerElement(s);
	const void *base = IOSurfaceGetBaseAddress(s);
	if (base == NULL || bpe == 0 || pitch % bpe != 0) {''', '''	size_t bpe = IOSurfaceGetBytesPerElement(s);
	const void *base = IOSurfaceGetBaseAddress(s);
	if (w * h >= 600000) {
		static int biglog;
		if (biglog++ < 60) {
			char mean[32];
			GLint btex = 0;
			glGetIntegerv(GL_TEXTURE_BINDING_2D, &btex);
			sgl_grid_mean(bpe == 4 ? base : NULL, w, h, pitch, mean, sizeof(mean));
			sweet_drm_log("sweetgl: BIG %s (copy) surf %u %zux%zu pitch %zu fmt %#x/%#x tex %d mean %s",
			    why, IOSurfaceGetID(s), w, h, pitch, format, type, btex, mean);
		}
	}
	if (base == NULL || bpe == 0 || pitch % bpe != 0) {'''),
])


# Round 46: where each texture came from (IOSurface id/format/size, copy or
# CPU upload, pixel mean at the time), and the first draw of a texture over
# at least half the screen logs it: the app switcher's background (texture
# 194 in round 45, smaller than the BIG threshold) and the home screen folder
# icon's missing frosted background.
edit('eagl.c', [
    ('''void
sgl_DrawArrays(void *rctx, GLenum mode, GLint first, GLsizei count)''', '''#define FCC_C(c) ((c) >= 0x20 && (c) < 0x7f ? (c) : '.')
#define FCC(f) FCC_C((f) >> 24), FCC_C(((f) >> 16) & 0xff), FCC_C(((f) >> 8) & 0xff), FCC_C((f) & 0xff)

static struct {
	uint32_t surf, fourcc;
	uint16_t w, h;
	char mean[16];
	char kind;              /* s: IOSurface import, c: IOSurface copy, t: TexImage2D */
	uint8_t checks, logged;
} tex_src[8192];

static void
sgl_tex_note(GLint tex, char kind, uint32_t surf, uint32_t fourcc, size_t w, size_t h, const void *base, size_t pitch,
    size_t bpe)
{
	if (tex <= 0 || tex >= 8192) {
		return;
	}
	tex_src[tex].surf = surf;
	tex_src[tex].fourcc = fourcc;
	tex_src[tex].w = (uint16_t)w;
	tex_src[tex].h = (uint16_t)h;
	tex_src[tex].kind = kind;
	tex_src[tex].checks = 0;
	tex_src[tex].logged = 0;
	sgl_grid_mean(bpe == 4 ? base : NULL, w, h, pitch, tex_src[tex].mean, sizeof(tex_src[tex].mean));
}

/* before a draw: unit 0's texture drawn over half the screen or more, first time */
static void
sgl_big_draw_check(void)
{
	GLint tex = (GLint)unit_held[0];
	if (tex <= 0 || tex >= 8192 || tex_src[tex].logged || tex_src[tex].checks >= 16) {
		return;
	}
	tex_src[tex].checks++;
	GLint vp[4] = {0}, sc[4] = {0}, fb = 0;
	glGetIntegerv(GL_VIEWPORT, vp);
	GLboolean scon = glIsEnabled(GL_SCISSOR_TEST);
	glGetIntegerv(GL_SCISSOR_BOX, sc);
	glGetIntegerv(GL_FRAMEBUFFER_BINDING, &fb);
	long area = scon ? (long)sc[2] * sc[3] : 0;   /* unscissored: quads of any size, not counted */
	if (area * 2 < 1242L * 2208L) {
		return;
	}
	tex_src[tex].logged = 1;
	static int n;
	if (n++ < 80) {
		GLint prog = 0;
		glGetIntegerv(GL_CURRENT_PROGRAM, &prog);
		sweet_drm_log("sweetgl: LARGE DRAW tex %d (%c surf %u %c%c%c%c %ux%u mean %s) prog %d fb %d vp %dx%d scissor %d %d,%d %dx%d blend %d",
		    tex, tex_src[tex].kind ? tex_src[tex].kind : '?', tex_src[tex].surf, FCC(tex_src[tex].fourcc),
		    tex_src[tex].w, tex_src[tex].h, tex_src[tex].mean, prog, fb, vp[2], vp[3], scon, sc[0], sc[1], sc[2], sc[3],
		    glIsEnabled(GL_BLEND));
	}
}

void
sgl_DrawArrays(void *rctx, GLenum mode, GLint first, GLsizei count)'''),
    ('''	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(65);''', '''	sgl_big_draw_check();
	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(65);'''),
    ('''	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(67);''', '''	sgl_big_draw_check();
	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(67);'''),
    ('''	glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels);
	SGL_POST(301);''', '''	glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels);
	if (level == 0) {
		GLint row2 = unpack_row();
		/* 4-byte pixels only: A8/L8 uploads are 1 byte a pixel (round 46-48: backboardd read past them) */
		bool four = type == GL_UNSIGNED_BYTE && (format == GL_RGBA || format == GL_BGRA_EXT);
		sgl_tex_note((GLint)unit_held[active_unit()], 't', 0, 0, (size_t)width, (size_t)height,
		    four ? pixels : NULL, (size_t)(row2 > 0 ? row2 : width) * 4, 4);
	}
	SGL_POST(301);'''),
    ('''	if (w * h >= 600000) {
		static int biglog;
		if (biglog++ < 60) {
			char mean[32];
			GLint btex = 0;
			glGetIntegerv(GL_TEXTURE_BINDING_2D, &btex);
			sgl_grid_mean(IOSurfaceGetBytesPerElement(s) == 4''', '''	{
		GLint ntex = 0;
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &ntex);
		sgl_tex_note(ntex, 's', IOSurfaceGetID(s), fourcc, w, h, IOSurfaceGetBaseAddressOfPlane(s, plane), pitch,
		    IOSurfaceGetBytesPerElementOfPlane(s, plane));
	}
	if (w * h >= 600000) {
		static int biglog;
		if (biglog++ < 60) {
			char mean[32];
			GLint btex = 0;
			glGetIntegerv(GL_TEXTURE_BINDING_2D, &btex);
			sgl_grid_mean(IOSurfaceGetBytesPerElement(s) == 4'''),
    ('''	size_t bpe = IOSurfaceGetBytesPerElement(s);
	const void *base = IOSurfaceGetBaseAddress(s);
	if (w * h >= 600000) {''', '''	size_t bpe = IOSurfaceGetBytesPerElement(s);
	const void *base = IOSurfaceGetBaseAddress(s);
	{
		GLint ntex = 0;
		glGetIntegerv(GL_TEXTURE_BINDING_2D, &ntex);
		sgl_tex_note(ntex, 'c', IOSurfaceGetID(s), IOSurfaceGetPixelFormat(s), w, h, base, pitch, bpe);
	}
	if (w * h >= 600000) {'''),
])


# Round 50 (speed): the round 49 CPU profile shows backboardd's draws
# (CA::OGL::GLContext::draw_elements) going into the kernel for new GPU
# buffers (bo_new/bo_make, zeroing, cache flushes): IOSurface imports. The home
# screen alone binds more than 32 surfaces a frame (icons, widgets, dock,
# wallpaper, layers), so the 32-entry cache dropped and re-imported surfaces
# every frame. Now 192 entries, at most 48 MB of surfaces kept imported by the
# cache (memory is tight), least recently used dropped first.
edit('eagl.c', [
    ('''struct surf_res {
	uint32_t id, w, h, pitch;
	enum pipe_format format;
	uintptr_t base;
	struct pipe_resource *res;
	uint64_t used;
};
#define SURF_RES_MAX 32''', '''struct surf_res {
	uint32_t id, w, h, pitch;
	enum pipe_format format;
	uintptr_t base;
	struct pipe_resource *res;
	uint64_t used;
};
#define SURF_RES_MAX 192
#define SURF_RES_BYTES (48u << 20)
static uint64_t surf_res_bytes;'''),
    ('''	int victim = 0;
	for (int i = 1; i < SURF_RES_MAX; i++) {
		if (surf_res[i].used < surf_res[victim].used) {
			victim = i;
		}
	}
	pipe_resource_reference(&surf_res[victim].res, NULL);
	surf_res[victim] = *key;
	surf_res[victim].used = ++surf_res_clock;
	pipe_resource_reference(&surf_res[victim].res, res);''', '''	uint64_t need = (uint64_t)key->pitch * key->h;
	int victim;
	for (;;) {
		/* a free slot, else the least recently used; drop more while over budget */
		victim = 0;
		int empty = -1;
		for (int i = 0; i < SURF_RES_MAX; i++) {
			if (surf_res[i].res == NULL) {
				empty = empty < 0 ? i : empty;
			} else if (surf_res[victim].res == NULL || surf_res[i].used < surf_res[victim].used) {
				victim = i;
			}
		}
		if (empty >= 0 && surf_res_bytes + need <= SURF_RES_BYTES) {
			victim = empty;
			break;
		}
		if (surf_res[victim].res == NULL) {
			break;          /* nothing cached at all */
		}
		surf_res_bytes -= (uint64_t)surf_res[victim].pitch * surf_res[victim].h;
		pipe_resource_reference(&surf_res[victim].res, NULL);
		if (empty < 0 && surf_res_bytes + need <= SURF_RES_BYTES) {
			break;          /* reuse the slot just dropped */
		}
	}
	pipe_resource_reference(&surf_res[victim].res, NULL);
	surf_res[victim] = *key;
	surf_res[victim].used = ++surf_res_clock;
	surf_res_bytes += need;
	pipe_resource_reference(&surf_res[victim].res, res);'''),
])


# Round 51 (speed): sgl_Flush was glFinish: backboardd waited ~20 ms a frame
# for the GPU before building the next one. The kernel already waits for the
# queued GPU jobs where it matters: the panel copy of a presented surface and
# IOSurface CPU locks (SweetMali queue + trapLock). glFlush hands the batch to
# the GPU queue and returns, so the CPU builds frame N+1 while the GPU draws
# frame N. SWEETGL_FINISH=1: the old wait.
edit('eagl.c', [
    ('''	pend_clear_apply();
	uint64_t t0 = mach_absolute_time();
	glFinish();
	flush_stats(t0, mach_absolute_time());''', '''	pend_clear_apply();
	uint64_t t0 = mach_absolute_time();
	static int finish = -1;
	if (finish < 0) {
		const char *e = getenv("SWEETGL_FINISH");
		finish = !(e != NULL && e[0] == '0');      /* round 51: glFlush did not raise the frame rate (the kernel present waits) and brought back failed jobs: wait again; SWEETGL_FINISH=0 flushes */
	}
	if (finish) {
		glFinish();
	} else {
		glFlush();
	}
	flush_stats(t0, mach_absolute_time());'''),
])


# Round 52: how many draws and fbfetch flushes (each a new render pass: a
# full load/store of the 1242x2208 target on Midgard) per stats window.
edit('eagl.c', [
    ('''	sgl_texture_barrier();
	/* SWEETGL_TRACE: the first draws of each fbfetch program, wherever they happen */''', '''	{
		extern uint32_t sweet_drm_win_fbfetch;
		sweet_drm_win_fbfetch++;
	}
	sgl_texture_barrier();
	/* SWEETGL_TRACE: the first draws of each fbfetch program, wherever they happen */'''),
    ('''	sgl_big_draw_check();
	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(65);''', '''	sgl_big_draw_check();
	{
		extern uint32_t sweet_drm_win_draws;
		sweet_drm_win_draws++;
	}
	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(65);'''),
    ('''	sgl_big_draw_check();
	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(67);''', '''	sgl_big_draw_check();
	{
		extern uint32_t sweet_drm_win_draws;
		sweet_drm_win_draws++;
	}
	if (sgl_skip_draw) {
		sgl_skip_draw = false;
		SGL_POST(67);'''),
])
