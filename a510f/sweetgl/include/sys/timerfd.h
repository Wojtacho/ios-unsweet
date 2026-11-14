/*
 * A510F sweetgl: Linux timerfd for Mesa's panfrost perf-counter sessions
 * (panfrost_kmod.c), which this port never opens. Every call fails.
 */
#ifndef A510F_SYS_TIMERFD_H
#define A510F_SYS_TIMERFD_H

#include <errno.h>
#include <time.h>

#define TFD_CLOEXEC       0x80000
#define TFD_NONBLOCK      0x800
#define TFD_TIMER_ABSTIME 1

#ifndef A510F_HAVE_ITIMERSPEC
#define A510F_HAVE_ITIMERSPEC
struct itimerspec {
	struct timespec it_interval;
	struct timespec it_value;
};
#endif

static inline int timerfd_create(int clockid, int flags) { (void)clockid; (void)flags; errno = ENOSYS; return -1; }
static inline int
timerfd_settime(int fd, int flags, const struct itimerspec *new_value, struct itimerspec *old_value)
{
	(void)fd; (void)flags; (void)new_value; (void)old_value;
	errno = ENOSYS;
	return -1;
}

#endif
