---
title: On FreeBSD, monerod crashes trying to handle SIGTERM
source_url: https://github.com/monero-project/monero/issues/4563
author: ndorf
assignees: []
labels: []
created_at: '2018-10-11T20:08:51+00:00'
updated_at: '2018-10-15T12:40:59+00:00'
type: issue
status: closed
closed_at: '2018-10-15T12:40:59+00:00'
---

# Original Description
On FreeBSD 11.2-RELEASE-p4, every time monerod receives SIGTERM it raises SIGABRT and crashes instead of exiting cleanly. The system's thread library also prints this to stderr:

`Fatal error 'thread 0x807816000 was already on queue.' at line 271 in file /usr/src/lib/libthr/thread/thr_cond.c (errno = 19)`

Full stack trace [here](https://github.com/monero-project/monero/files/2470386/monerod_crash_log.txt)

If we are really invoking the whole shutdown procedure directly from the signal handler as this suggests, IMHO it's not a great idea. In particular, `pthread_cond_wait` is most definitely not on the list of allowed calls. [Linux](https://linux.die.net/man/7/signal) and [FreeBSD](https://www.freebsd.org/cgi/man.cgi?query=sigaction&apropos=0&sektion=0&manpath=FreeBSD+11.2-RELEASE+and+Ports&arch=default&format=html) agree on this, even though Linux appears to be more lenient in practice.

In this case, I bet the thread is already waiting on the same condition, although I didn't actually confirm that. That error message finally makes sense though!

I think the best practice is to do as little as possible in the handler, preferably just set a flag or write(an_fd) and return.

# Discussion History
## moneromooo-monero | 2018-10-12T14:22:27+00:00
https://github.com/monero-project/monero/pull/4571

## moneromooo-monero | 2018-10-15T12:29:54+00:00
+resolved

# Action History
- Created by: ndorf | 2018-10-11T20:08:51+00:00
- Closed at: 2018-10-15T12:40:59+00:00
