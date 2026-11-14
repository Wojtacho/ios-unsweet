/*
 * A510F sweetgl: Linux eventfd for Mesa's panfrost perf-counter sessions
 * (panfrost_kmod.c), which this port never opens. Every call fails.
 */
#ifndef A510F_SYS_EVENTFD_H
#define A510F_SYS_EVENTFD_H

#include <errno.h>
#include <stdint.h>

typedef uint64_t eventfd_t;

#define EFD_CLOEXEC  0x80000
#define EFD_NONBLOCK 0x800

static inline int eventfd(unsigned int initval, int flags) { (void)initval; (void)flags; errno = ENOSYS; return -1; }
static inline int eventfd_read(int fd, eventfd_t *value) { (void)fd; (void)value; errno = ENOSYS; return -1; }
static inline int eventfd_write(int fd, eventfd_t value) { (void)fd; (void)value; errno = ENOSYS; return -1; }

#endif
