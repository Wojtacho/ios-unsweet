#pragma once
#include <stdint.h>

/*
 * A510F: the splash framebuffer S-Boot leaves programmed in DECON window 0
 * (found by the a510f probe, see a510f/NOTES.md). a8r8g8b8.
 * Must match SWEET_FB_* in a510f/xnu/patches/0102 and FB in mkadt_a510f.py.
 */
#define FB_BASE		0x67000000UL
#define FB_W		1080
#define FB_H		1920
#define FB_STRIDE	(FB_W * 4)

#define RED	0xffff0000U
#define BLUE	0xff0000a0U
#define WHITE	0xffffffffU
#define YELLOW	0xffffff00U
#define GREEN	0xff00ff00U

extern volatile uint32_t *con_fb;

void con_clear(uint32_t bg);
void con_skip(void);
void con_str(const char *label, const char *s);
void con_hex(const char *label, uint64_t v);
/* label, then "a=xxxxxxxx b=xxxxxxxx" style pairs of 32-bit values */
void con_hex2(const char *label, const char *a, uint32_t va, const char *b, uint32_t vb);
