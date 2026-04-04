---
title: Monero-gui refuses to build
source_url: https://github.com/monero-project/monero-gui/issues/3093
author: lulighttec
assignees: []
labels: []
created_at: '2020-09-19T17:35:05+00:00'
updated_at: '2020-09-29T19:39:41+00:00'
type: issue
status: closed
closed_at: '2020-09-25T23:26:07+00:00'
---

# Original Description
Beating my head against the wall trying to get the gui to install on Ubuntu 20.04 for Arm7. Following these instructions: https://github.com/monero-project/monero-gui"     
./build.sh" can't find 3 files that should be there.
-lwallet_merged
-lepee
-leasylogging (even though I installed the easylogging package separately to make sure it was there)
Read a few threads similar to mine, but no avail. Here's a paste of the log output: [PrivateBin](https://privatebin.rxyz.rocks/?a9fc11ffce49fd90#DFAN1FuVdbnFPhYBsRK1G6Pe9K9U4hCNupzkifozWEjn) I tried installing the regular monero first, then the gui; regular monerod installs and runs ok. Guibuild still produced this error. Noticed there's also a monero directory inside monero-gui, so tried "make" in that directory first, then "./build.sh" in monero-gui, but still no joy.

# Discussion History
## selsta | 2020-09-20T01:45:23+00:00
We currently don’t officially support the GUI on ARM. It should still work, but I have never tried it.

You might have more success with the cmake build system, delete your build directory and do:

`make release -j4`

Alternatively the CLI offers ARM binaries.

## lulighttec | 2020-09-20T03:08:02+00:00
`make: Nothing to be done for 'release'.`

## selsta | 2020-09-20T08:32:57+00:00
Checkout #3090

## lulighttec | 2020-09-20T16:04:42+00:00
Funny story: I found #3090 shortly after I posted my last comment.  As long as the oom-reaper doesn't get me, I think it might build.  Thanks for the direction!

## lulighttec | 2020-09-20T20:37:37+00:00
well, it built, finally.  It runs until I try to create a wallet, and then has a segmentation fault and quits.  But it built with no errors.  Yay?

## selsta | 2020-09-20T20:39:11+00:00
Do you have a backtrace? Do you know how to start monero-wallet-gui with gdb and get a backtrace?

## lulighttec | 2020-09-20T20:39:42+00:00
I don't... enlighten me?

## selsta | 2020-09-20T20:42:22+00:00
start the GUI like this:

`gdb ./monero-wallet-gui`

`run`

Reproduce the crash

`thread apply all bt`

And then copy / paste the backtrace.

## lulighttec | 2020-09-20T20:51:13+00:00
Thread 1 "monero-wallet-g" received signal SIGSEGV, Segmentation fault.
0xb6921dbe in _ULarm_step () from /usr/lib/arm-linux-gnueabihf/libunwind.so.8
(gdb) thread apply all bt

Thread 31 (Thread 0xadcae1e0 (LWP 1921)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c454 in futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0xadcadb20, clockid=<optimized out>, expected=0, futex_word=0x49f74a8) at ../sysdeps/nptl/futex-internal.h:320
#2  __pthread_cond_wait_common (abstime=0xadcadb20, clockid=<optimized out>, mutex=0x49f7468, cond=0x49f7480) at pthread_cond_wait.c:520
#3  __pthread_cond_timedwait (cond=0x49f7480, mutex=0x49f7468, abstime=0xadcadb20) at pthread_cond_wait.c:656
#4  0x0052659a in Monero::WalletImpl::refreshThreadFunc() ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 30 (Thread 0x941ff1e0 (LWP 1920)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x44cc4bc) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x44cc478, cond=0x44cc490) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x44cc490, mutex=0x44cc478) at pthread_cond_wait.c:638
--Type <RET> for more, q to quit, c to continue without paging--
#4  0xb54524a2 in QWaitCondition::wait(QMutex*, QDeadlineTimer) () at /usr/lib/arm-linux-gnueabihf/libQt5Core.so.5
#5  0xb54525ae in QWaitCondition::wait(QMutex*, unsigned long) () at /usr/lib/arm-linux-gnueabihf/libQt5Core.so.5
#6  0xb60e6094 in  () at /usr/lib/arm-linux-gnueabihf/libQt5Quick.so.5

Thread 29 (Thread 0x954b81e0 (LWP 1919)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x12973f8 <tools::threadpool::getInstance()::instance+104>) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>, cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>) at pthread_cond_wait.c:638
#4  0x007548f0 in tools::threadpool::run(bool) ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 28 (Thread 0x959b91e0 (LWP 1918)):
--Type <RET> for more, q to quit, c to continue without paging--c
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x12973f8 <tools::threadpool::getInstance()::instance+104>) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>, cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>) at pthread_cond_wait.c:638
#4  0x007548f0 in tools::threadpool::run(bool) ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 27 (Thread 0x95eba1e0 (LWP 1917)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x12973f8 <tools::threadpool::getInstance()::instance+104>) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>, cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>) at pthread_cond_wait.c:638
#4  0x007548f0 in tools::threadpool::run(bool) ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 26 (Thread 0x963bb1e0 (LWP 1916)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x12973f8 <tools::threadpool::getInstance()::instance+104>) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>, cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>) at pthread_cond_wait.c:638
#4  0x007548f0 in tools::threadpool::run(bool) ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 25 (Thread 0x968bc1e0 (LWP 1915)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x12973f8 <tools::threadpool::getInstance()::instance+104>) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>, cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>) at pthread_cond_wait.c:638
#4  0x007548f0 in tools::threadpool::run(bool) ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 24 (Thread 0x96dbd1e0 (LWP 1914)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x12973f8 <tools::threadpool::getInstance()::instance+104>) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>, cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>) at pthread_cond_wait.c:638
#4  0x007548f0 in tools::threadpool::run(bool) ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 23 (Thread 0x972be1e0 (LWP 1913)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c16e in futex_wait_cancelable (private=0, expected=0, futex_word=0x12973f8 <tools::threadpool::getInstance()::instance+104>) at ../sysdeps/nptl/futex-internal.h:183
#2  __pthread_cond_wait_common (abstime=0x0, clockid=0, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>, cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>) at pthread_cond_wait.c:508
#3  __pthread_cond_wait (cond=0x12973d0 <tools::threadpool::getInstance()::instance+64>, mutex=0x12973b8 <tools::threadpool::getInstance()::instance+40>) at pthread_cond_wait.c:638
#4  0x007548f0 in tools::threadpool::run(bool) ()
#5  0xb6df1124 in  () at /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.71.0
#6  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#7  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 22 (Thread 0xa36ff1e0 (LWP 1911)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=1, fds=0xa2d03360) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xa2d03360, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb35c77a6 in  () at /usr/lib/arm-linux-gnueabihf/libglib-2.0.so.0

Thread 21 (Thread 0xa40ff1e0 (LWP 1910)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400c454 in futex_abstimed_wait_cancelable (private=<optimized out>, abstime=0xa40feb00, clockid=<optimized out>, expected=0, futex_word=0x2ceb490) at ../sysdeps/nptl/futex-internal.h:320
#2  __pthread_cond_wait_common (abstime=0xa40feb00, clockid=<optimized out>, mutex=0x2ceb450, cond=0x2ceb468) at pthread_cond_wait.c:520
#3  __pthread_cond_timedwait (cond=0x2ceb468, mutex=0x2ceb450, abstime=0xa40feb00) at pthread_cond_wait.c:656
#4  0xb545244c in QWaitCondition::wait(QMutex*, QDeadlineTimer) () at /usr/lib/arm-linux-gnueabihf/libQt5Core.so.5
#5  0xb5452572 in QWaitCondition::wait(QMutex*, unsigned long) () at /usr/lib/arm-linux-gnueabihf/libQt5Core.so.5
#6  0xb545022c in  () at /usr/lib/arm-linux-gnueabihf/libQt5Core.so.5
#7  0xb544d840 in  () at /usr/lib/arm-linux-gnueabihf/libQt5Core.so.5
#8  0xb40069be in start_thread (arg=0xbe2dd1b9) at pthread_create.c:477
#9  0xb3dc84cc in  () at ../sysdeps/unix/sysv/linux/arm/clone.S:73

Thread 20 (Thread 0xa4aff1e0 (LWP 1909)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=1, fds=0xa4102758) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xa4102758, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb35c77a6 in  () at /usr/lib/arm-linux-gnueabihf/libglib-2.0.so.0

Thread 19 (Thread 0xa5a351e0 (LWP 1905)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0xb53c178c) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0xb53c178c, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0xb53c178c, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb41ed102 in gles_vertexp_bb_neon_transform_and_produce_clip_bits () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 18 (Thread 0xa62361e0 (LWP 1904)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=4, fds=0xa6235ae8) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xa6235ae8, nfds=4, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb4466cca in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 17 (Thread 0xa6a371e0 (LWP 1903)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e0788) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e0788, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e0788, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 16 (Thread 0xa72381e0 (LWP 1902)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e0728) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e0728, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e0728, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 15 (Thread 0xa7a391e0 (LWP 1901)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e06c8) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e06c8, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e06c8, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 14 (Thread 0xa823a1e0 (LWP 1900)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e0668) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e0668, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e0668, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 13 (Thread 0xa8a3b1e0 (LWP 1899)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e0608) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e0608, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e0608, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 12 (Thread 0xa923c1e0 (LWP 1898)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e05a8) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e05a8, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e05a8, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 11 (Thread 0xa9a3d1e0 (LWP 1897)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e0548) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e0548, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e0548, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 10 (Thread 0xaa23e1e0 (LWP 1896)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x15e04e8) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x15e04e8, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x15e04e8, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4466ada in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 9 (Thread 0xaaa3f1e0 (LWP 1895)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb400e5f6 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, clockid=0, expected=1, futex_word=0x1642064) at ../sysdeps/nptl/futex-internal.h:320
#2  do_futex_wait (sem=sem@entry=0x1642064, abstime=0x0, clockid=0) at sem_waitcommon.c:117
#3  0xb400e6e4 in __new_sem_wait_slow (sem=0x1642064, abstime=0x0, clockid=0) at sem_waitcommon.c:285
#4  0xb4496d30 in  () at /usr/lib/arm-linux-gnueabihf/libGLESv2.so

Thread 8 (Thread 0xac8ff1e0 (LWP 1870)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=1, fds=0xabf02d78) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xabf02d78, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb35c77a6 in  () at /usr/lib/arm-linux-gnueabihf/libglib-2.0.so.0

Thread 7 (Thread 0xad2ff1e0 (LWP 1868)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=5, fds=0xac90dd40) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xac90dd40, nfds=5, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb35c77a6 in  () at /usr/lib/arm-linux-gnueabihf/libglib-2.0.so.0

Thread 5 (Thread 0xae6ff1e0 (LWP 1866)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=2, fds=0xae706bf0) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xae706bf0, nfds=2, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb35c77a6 in  () at /usr/lib/arm-linux-gnueabihf/libglib-2.0.so.0

Thread 4 (Thread 0xaf0ff1e0 (LWP 1865)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=1, fds=0xae701658) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xae701658, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb35c77a6 in  () at /usr/lib/arm-linux-gnueabihf/libglib-2.0.so.0

Thread 3 (Thread 0xafa4e1e0 (LWP 1864)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=1, fds=0x13cefb8) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0x13cefb8, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb35c77a6 in  () at /usr/lib/arm-linux-gnueabihf/libglib-2.0.so.0

Thread 2 (Thread 0xb12061e0 (LWP 1863)):
#0  __libc_do_syscall () at ../sysdeps/unix/sysv/linux/arm/libc-do-syscall.S:46
#1  0xb3dc1324 in __GI___poll (timeout=-1, nfds=1, fds=0xb1205ae4) at ../sysdeps/unix/sysv/linux/poll.c:29
#2  __GI___poll (fds=0xb1205ae4, nfds=1, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:26
#3  0xb38868fc in  () at /usr/lib/arm-linux-gnueabihf/libxcb.so.1

Thread 1 (Thread 0xb1926d50 (LWP 1860)):
#0  0xb6921dbe in _ULarm_step () at /usr/lib/arm-linux-gnueabihf/libunwind.so.8
#1  0xb6920864 in unw_backtrace () at /usr/lib/arm-linux-gnueabihf/libunwind.so.8
#2  0x008e3350 in el::base::debug::StackTrace::generateNew() ()
#3  0x00758de6 in tools::log_stack_trace(char const*) ()
#4  0x00486b1a in __cxa_throw ()
#5  0x00483c2e in boost::asio::detail::do_throw_error(boost::system::error_code const&, char const*) ()
#6  0x008d1c12 in epee::net_utils::direct_connect::operator()(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_waitable_timer<std::chrono::_V2::steady_clock, boost::asio::wait_traits<std::chrono::_V2::steady_clock>, boost::asio::executor>&) const ()
#7  0x004ffcba in std::_Function_handler<boost::unique_future<boost::asio::basic_stream_socket<boost::asio::ip::tcp, boost::asio::executor> > (std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_waitable_timer<std::chrono::_V2::steady_clock, boost::asio::wait_traits<std::chrono::_V2::steady_clock>, boost::asio::executor>&), epee::net_utils::direct_connect>::_M_invoke(std::_Any_data const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::asio::basic_waitable_timer<std::chrono::_V2::steady_clock, boost::asio::wait_traits<std::chrono::_V2::steady_clock>, boost::asio::executor>&) ()
#8  0x004e91be in epee::net_utils::blocked_mode_client::try_connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long long, std::ratio<1ll, 1000ll> >) ()
#9  0x004e983c in epee::net_utils::blocked_mode_client::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long long, std::ratio<1ll, 1000ll> >) ()
#10 0x004e9c04 in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::connect(std::chrono::duration<long long, std::ratio<1ll, 1000ll> >) ()
#11 0x004f819c in epee::net_utils::http::http_simple_client_template<epee::net_utils::blocked_mode_client>::invoke(boost::basic_string_ref<char, std::char_traits<char> >, boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::chrono::duration<long long, std::ratio<1ll, 1000ll> >, epee::net_utils::http::http_response_info const**, std::__cxx11::list<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > const&) ()
#12 0x006f27f8 in bool epee::net_utils::invoke_http_json<epee::json_rpc::request<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::request_t> >, epee::json_rpc::response<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::response_t>, epee::json_rpc::error>, epee::net_utils::http::abstract_http_client>(boost::basic_string_ref<char, std::char_traits<char> >, epee::json_rpc::request<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::request_t> > const&, epee::json_rpc::response<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::response_t>, epee::json_rpc::error>&, epee::net_utils::http::abstract_http_client&, std::chrono::duration<long long, std::ratio<1ll, 1000ll> >, boost::basic_string_ref<char, std::char_traits<char> >) ()
#13 0x006f2df2 in bool epee::net_utils::invoke_http_json_rpc<epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::request_t>, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::response_t>, epee::net_utils::http::abstract_http_client>(boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::request_t> const&, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_GET_INFO::response_t>&, epee::json_rpc::error&, epee::net_utils::http::abstract_http_client&, std::chrono::duration<long long, std::ratio<1ll, 1000ll> >, boost::basic_string_ref<char, std::char_traits<char> >, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#14 0x006ee4d8 in tools::NodeRPCProxy::get_info[abi:cxx11]() ()
#15 0x006eed6c in tools::NodeRPCProxy::get_target_height[abi:cxx11](unsigned long long&) ()
#16 0x0057cdfa in tools::wallet2::get_daemon_blockchain_target_height(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ()
#17 0x0057d0dc in tools::wallet2::estimate_blockchain_height() ()
#18 0x00600a56 in tools::wallet2::generate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, epee::mlocked<tools::scrubbed<crypto::ec_scalar> > const&, bool, bool, bool) ()
#19 0x0051dab4 in Monero::WalletImpl::create(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#20 0x0053dcce in Monero::WalletManagerImpl::createWallet(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType, unsigned long long) ()
#21 0x004b0c1e in WalletManager::createWallet(QString const&, QString const&, QString const&, NetworkType::Type, unsigned long long) ()
#22 0x0050fd58 in WalletManager::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) ()
#23 0x00510050 in WalletManager::qt_metacall(QMetaObject::Call, int, void**) ()
#24 0xb5adc296 in  () at /usr/lib/arm-linux-gnueabihf/libQt5Qml.so.5
(gdb) 



## xiphon | 2020-09-21T16:59:37+00:00
Seems there is some issue with libunwind on ARM. Please apply the following patch to `monero/CMakeLists.txt` and rebuild the GUI.
```diff
@@ -395,7 +395,7 @@ elseif(CMAKE_C_COMPILER_ID STREQUAL "GNU" AND NOT MINGW)
   set(DEFAULT_STACK_TRACE ON)
   set(STACK_TRACE_LIB "easylogging++") # for diag output only
   set(LIBUNWIND_LIBRARIES "")
-elseif (ARM AND STATIC)
+elseif (ARM)
   set(DEFAULT_STACK_TRACE OFF)
   set(LIBUNWIND_LIBRARIES "")
 else()
```

## lulighttec | 2020-09-21T20:07:33+00:00
Change applied; it gets to the end of 
`Removing translations equal to source text in 'usr/src/monero-gui/build/translations/monero-core_zu.qm'...`
`     Generated 0 translation(s) (0 finished and 0 unfinished)`
`     Ignored 690 untranslated source text(s)`
`make: *** No rule to make target '../translations/monero-core_hr.qm', needed by 'qrc_translations.cpp;'.  Stop.`


## xiphon | 2020-09-21T20:12:31+00:00
Could you run clean build (i.e. `rm -rf build` before `make release -j4`)?

## lulighttec | 2020-09-21T20:21:07+00:00
I did run 'make clean' beforehand; this time I used 'rm -rf build' as you suggested.  
 'make release' only results in 'make: Nothing to be done for 'release'.'  Only the ./build.sh works, though I'd love to limit it to 7 threads while we're on the topic, since I only have 8, and ./build.sh seems to want to use all 8.

## selsta | 2020-09-21T20:28:43+00:00
What happens when you edit ARCH from `x86-64` to `armv7-a` on line 32 in Makefile?

## lulighttec | 2020-09-21T20:41:52+00:00
The Makefile in /usr/src/monero-gui?  term "ARCH" is not in this Makefile; line 32 is:
`QINSTALL_PROGRAM = /usr/lib/qt5/bin/qmake -install qinstall -exe`

## selsta | 2020-09-21T20:43:04+00:00
Not sure which file you are looking at, see here: https://github.com/monero-project/monero-gui/blob/master/Makefile#L32

## xiphon | 2020-09-21T21:04:59+00:00
Please run the following commands:
```
mkdir -p build/release
cd build/release
cmake -D ARCH="armv7-a" -D CMAKE_BUILD_TYPE=Release ../..
make -j7
```

## lulighttec | 2020-09-21T21:24:08+00:00
There was a configuration error I included near the top before I ran the 'cmake' command with added
 -DMANUAL_SUBMODULES=1

[PrivateBin](https://privatebin.rxyz.rocks/?2bbd750a536161d4#G59rjFVPaDbteuXPkefrUztBAqJ4gZXrUCETm6YMBtSs)

## xiphon | 2020-09-21T21:42:30+00:00
`=` sign is missing

Edit:
was talking about
```
root@odroid:/usr/src/monero-gui/build/release# cmake -D ARCH"armv7-a" -D CMAKE_BUILD_TYPE=release ../..
Parse error in command line argument: -D
Should be: VAR:type=value
CMake Error: No cmake script provided.
CMake Error: Problem processing arguments. Aborting.
```

## selsta | 2020-09-21T21:43:55+00:00
seems to have failed here

```
[  4%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
cc: error: unrecognized -march target: x86-64
cc: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
cc: error: missing argument to ‘-march=’
cc: error: unrecognized command line option ‘-maes’
make[2]: *** [monero/src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:63: monero/src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1884: monero/src/crypto/CMakeFiles/obj_cncrypto.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
```

## lulighttec | 2020-09-21T21:46:25+00:00
@xiphon - at the very very top, yes there was an = missing between ARCH and "armv7-a", but right after that error, I entered it correctly the second time :-)  There was a different error about updating all submodules; that's what I was referring to.

@selsta - Yes, I noticed this too.. what do I do?

@both of you  - Thank you in advance for taking the time to help me 

## xiphon | 2020-09-21T21:49:35+00:00
~Try to comment out another line (additionally to previous patch) in `monero/CMakeLists.txt`~

Edit: thought you are building it on MacOS. The previous patch should work just fine.

## lulighttec | 2020-09-21T22:03:02+00:00
I just copied the errors near the top this time...

````
make -j7
[  2%] Built target qrcodegen
[  2%] Built target lmdb
[  2%] Built target genversiongui
[  5%] Built target libminiupnpc-static
[  7%] Automatic MOC and UIC for target gui_version
[  9%] Built target generate_translations_header
[ 10%] Built target easylogging
[ 10%] Built target genversion
[ 10%] Building CXX object monero/src/device/CMakeFiles/obj_device.dir/device.cpp.o
c++: error: unrecognized -march target: x86-64
c++: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
c++: error: missing argument to ‘-march=’
c++: error: unrecognized command line option ‘-maes’
[ 11%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o
make[2]: *** [monero/src/device/CMakeFiles/obj_device.dir/build.make:63: monero/src/device/CMakeFiles/obj_device.dir/device.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:4126: monero/src/device/CMakeFiles/obj_device.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
[ 11%] Built target gui_version_autogen
[ 11%] Building CXX object monero/src/blocks/CMakeFiles/blocks.dir/blocks.cpp.o
[ 11%] Building C object monero/external/randomx/CMakeFiles/randomx.dir/src/jit_compiler_x86_static.S.o
c++: error: unrecognized -march target: x86-64
c++: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
c++: error: missing argument to ‘-march=’
cc: error: unrecognized -march target: x86-64
cc: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
cc: error: missing argument to ‘-march=’
c++: error: unrecognized command line option ‘-maes’
make[2]: *** [monero/src/blocks/CMakeFiles/blocks.dir/build.make:75: monero/src/blocks/CMakeFiles/blocks.dir/blocks.cpp.o] Error 1
[ 11%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o
make[2]: *** Waiting for unfinished jobs....
cc: error: unrecognized command line option ‘-maes’
[ 11%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o
make[2]: *** [monero/src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:63: monero/src/crypto/CMakeFiles/obj_cncrypto.dir/aesb.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
c++: error: unrecognized -march target: x86-64
c++: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
[ 12%] Building C object monero/src/blocks/CMakeFiles/blocks.dir/generated_checkpoints.c.o
c++: error: missing argument to ‘-march=’
c++: error: unrecognized command line option ‘-maes’
[ 14%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o
make[2]: *** [monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/build.make:63: monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
cc: error: unrecognized -march target: x86-64
cc: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
cc: error: missing argument to ‘-march=’
cc: error: unrecognized command line option ‘-maes’
make[2]: *** [monero/src/blocks/CMakeFiles/blocks.dir/build.make:88: monero/src/blocks/CMakeFiles/blocks.dir/generated_checkpoints.c.o] Error 1
cc: error: unrecognized -march target: x86-64
cc: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
cc: error: missing argument to ‘-march=’
make[1]: *** [CMakeFiles/Makefile2:4064: monero/src/blocks/CMakeFiles/blocks.dir/all] Error 2
c++: error: unrecognized -march target: x86-64
c++: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
c++: error: missing argument to ‘-march=’
cc: error: unrecognized command line option ‘-maes’
c++: error: unrecognized command line option ‘-maes’
make[2]: *** [monero/src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:76: monero/src/crypto/CMakeFiles/obj_cncrypto.dir/blake256.c.o] Error 1
make[2]: *** [monero/src/ringct/CMakeFiles/obj_ringct.dir/build.make:63: monero/src/ringct/CMakeFiles/obj_ringct.dir/rctSigs.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1949: monero/src/ringct/CMakeFiles/obj_ringct.dir/all] Error 2
[ 14%] Building CXX object monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o
[ 14%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o
cc: error: unrecognized -march target: x86-64
c++: error: unrecognized -march target: x86-64
c++: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
cc: note: valid arguments are: armv4 armv4t armv5t armv5te armv5tej armv6 armv6j armv6k armv6z armv6kz armv6zk armv6t2 armv6-m armv6s-m armv7 armv7-a armv7ve armv7-r armv7-m armv7e-m armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8-m.base armv8-m.main armv8-r iwmmxt iwmmxt2 native
c++: error: missing argument to ‘-march=’
cc: error: missing argument to ‘-march=’
c++: error: unrecognized command line option ‘-maes’
cc: error: unrecognized command line option ‘-maes’
make[2]: *** [monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/build.make:76: monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o] Error 1
make[2]: *** [monero/src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:89: monero/src/crypto/CMakeFiles/obj_cncrypto.dir/chacha.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:2008: monero/src/ringct/CMakeFiles/obj_ringct_basic.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:1884: monero/src/crypto/CMakeFiles/obj_cncrypto.dir/all] Error 2
/usr/src/monero-gui/monero/external/randomx/src/jit_compiler_x86_static.S: Assembler messages:
/usr/src/monero-gui/monero/external/randomx/src/jit_compiler_x86_static.S:27: Error: unknown pseudo-op: `.intel_syntax'
/usr/src/monero-gui/monero/external/randomx/src/jit_compiler_x86_static.S:72: Error: ARM register expected -- `mov rdx,rax'
/usr/src/monero-gui/monero/external/randomx/src/jit_compiler_x86_static.S:73: Error: ARM register expected -- `and eax,(2097152-64)'
/usr/src/monero-gui/monero/external/randomx/src/jit_compiler_x86_static.S:74: Error: bad instruction `prefetcht0 [rsi+rax]'
/usr/src/monero-gui/monero/external/randomx/src/jit_compiler_x86_static.S:75: Error: ARM register expected -- `ror rdx,32'
/usr/src/monero-gui/monero/external/randomx/src/jit_compiler_x86_static.S:76: Error: ARM register expected -- `and edx,(2097152-64)'
```


## xiphon | 2020-09-21T22:51:30+00:00
Sounds weird, could you try clean build again and post the entire output (with patched `monero/CMakeLists.txt`)?

## lulighttec | 2020-09-21T22:57:07+00:00
sure, what was the second line number again? (so I can uncomment it)

nevermind, found it.


## xiphon | 2020-09-21T23:04:54+00:00
Pleas apply https://github.com/monero-project/monero-gui/pull/3094 (before patching the `monero/CMakeLists.txt`) as well 

## lulighttec | 2020-09-21T23:55:16+00:00
Holy Errors on 'cmake -D ARCH="armv7-a" -D CMAKE_BUILD_TYPE=release ../..', Batman

```
/usr/src/monero-gui/build/release# cmake -D ARCH="armv7-a" -D CMAKE_CUILD_TYPE=release ../..
CMake Warning (dev) at CMakeLists.txt:46:
  Syntax Warning in cmake code at column 23

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:46:
  Syntax Warning in cmake code at column 42

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:52:
  Syntax Warning in cmake code at column 38

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:52:
  Syntax Warning in cmake code at column 128

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:53:
  Syntax Warning in cmake code at column 30

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:53:
  Syntax Warning in cmake code at column 85

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:62:
  Syntax Warning in cmake code at column 52

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:62:
  Syntax Warning in cmake code at column 58

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:63:
  Syntax Warning in cmake code at column 46

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:63:
  Syntax Warning in cmake code at column 52

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:64:
  Syntax Warning in cmake code at column 51

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:64:
  Syntax Warning in cmake code at column 57

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:65:
  Syntax Warning in cmake code at column 55

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:65:
  Syntax Warning in cmake code at column 61

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:66:
  Syntax Warning in cmake code at column 51

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:66:
  Syntax Warning in cmake code at column 57

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:68:
  Syntax Warning in cmake code at column 36

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:68:
  Syntax Warning in cmake code at column 41

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:73:
  Syntax Warning in cmake code at column 19

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:73:
  Syntax Warning in cmake code at column 42

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:76:
  Syntax Warning in cmake code at column 36

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:76:
  Syntax Warning in cmake code at column 38

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:82:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:82:
  Syntax Warning in cmake code at column 63

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:91:
  Syntax Warning in cmake code at column 45

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:91:
  Syntax Warning in cmake code at column 48

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:91:
  Syntax Warning in cmake code at column 70

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:92:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:92:
  Syntax Warning in cmake code at column 43

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:94:
  Syntax Warning in cmake code at column 16

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:94:
  Syntax Warning in cmake code at column 23

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:100:
  Syntax Warning in cmake code at column 16

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:100:
  Syntax Warning in cmake code at column 42

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:104:
  Syntax Warning in cmake code at column 24

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:104:
  Syntax Warning in cmake code at column 73

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:110:
  Syntax Warning in cmake code at column 44

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:110:
  Syntax Warning in cmake code at column 51

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:120:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:120:
  Syntax Warning in cmake code at column 37

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:127:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:127:
  Syntax Warning in cmake code at column 52

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:128:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:128:
  Syntax Warning in cmake code at column 63

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:129:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:129:
  Syntax Warning in cmake code at column 84

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:135:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:135:
  Syntax Warning in cmake code at column 64

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:136:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:136:
  Syntax Warning in cmake code at column 60

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:141:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:141:
  Syntax Warning in cmake code at column 58

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:145:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:145:
  Syntax Warning in cmake code at column 62

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:146:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:146:
  Syntax Warning in cmake code at column 57

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:150:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:150:
  Syntax Warning in cmake code at column 65

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:151:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:151:
  Syntax Warning in cmake code at column 60

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:176:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:176:
  Syntax Warning in cmake code at column 45

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:177:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:177:
  Syntax Warning in cmake code at column 57

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:178:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:178:
  Syntax Warning in cmake code at column 53

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:183:
  Syntax Warning in cmake code at column 25

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:183:
  Syntax Warning in cmake code at column 58

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:188:
  Syntax Warning in cmake code at column 25

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:188:
  Syntax Warning in cmake code at column 78

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:189:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:189:
  Syntax Warning in cmake code at column 57

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:190:
  Syntax Warning in cmake code at column 29

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:190:
  Syntax Warning in cmake code at column 77

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:219:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:219:
  Syntax Warning in cmake code at column 92

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:229:
  Syntax Warning in cmake code at column 28

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:229:
  Syntax Warning in cmake code at column 52

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:255:
  Syntax Warning in cmake code at column 23

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:255:
  Syntax Warning in cmake code at column 37

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:257:
  Syntax Warning in cmake code at column 25

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:257:
  Syntax Warning in cmake code at column 49

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:266:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:266:
  Syntax Warning in cmake code at column 145

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:267:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:267:
  Syntax Warning in cmake code at column 137

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:268:
  Syntax Warning in cmake code at column 21

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:268:
  Syntax Warning in cmake code at column 143

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:338:
  Syntax Warning in cmake code at column 35

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:338:
  Syntax Warning in cmake code at column 40

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:375:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:375:
  Syntax Warning in cmake code at column 65

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:376:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:376:
  Syntax Warning in cmake code at column 60

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:380:
  Syntax Warning in cmake code at column 30

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:380:
  Syntax Warning in cmake code at column 68

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:388:
  Syntax Warning in cmake code at column 24

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:388:
  Syntax Warning in cmake code at column 41

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:390:
  Syntax Warning in cmake code at column 24

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:396:
  Syntax Warning in cmake code at column 50

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:413:
  Syntax Warning in cmake code at column 24

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:413:
  Syntax Warning in cmake code at column 88

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:417:
  Syntax Warning in cmake code at column 26

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:417:
  Syntax Warning in cmake code at column 89

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:429:
  Syntax Warning in cmake code at column 67

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:429:
  Syntax Warning in cmake code at column 70

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:437:
  Syntax Warning in cmake code at column 67

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:437:
  Syntax Warning in cmake code at column 70

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:447:
  Syntax Warning in cmake code at column 40

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:447:
  Syntax Warning in cmake code at column 43

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:458:
  Syntax Warning in cmake code at column 64

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:458:
  Syntax Warning in cmake code at column 67

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:466:
  Syntax Warning in cmake code at column 26

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:466:
  Syntax Warning in cmake code at column 65

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:470:
  Syntax Warning in cmake code at column 26

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:470:
  Syntax Warning in cmake code at column 64

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:496:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:496:
  Syntax Warning in cmake code at column 70

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:497:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:497:
  Syntax Warning in cmake code at column 74

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:498:
  Syntax Warning in cmake code at column 17

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:498:
  Syntax Warning in cmake code at column 76

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:500:
  Syntax Warning in cmake code at column 20

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:500:
  Syntax Warning in cmake code at column 65

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:501:
  Syntax Warning in cmake code at column 22

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:501:
  Syntax Warning in cmake code at column 73

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:502:
  Syntax Warning in cmake code at column 29

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:502:
  Syntax Warning in cmake code at column 91

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Warning (dev) at CMakeLists.txt:507:
  Syntax Warning in cmake code at column 36

  Argument not separated from preceding token by whitespace.
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Error at CMakeLists.txt:523:
  Parse error.  Function missing ending ")".  Instead found unterminated
  string with text ")

      else()
        find_library(COREFOUNDATION CoreFoundation)
        find_library(IOKIT IOKit)
        list(APPEND EXTRA_LIBRARIES ${IOKIT})
        list(APPEND EXTRA_LIBRARIES ${COREFOUNDATION})
      endif()
    endif()
    if (WIN32)
      list(APPEND EXTRA_LIBRARIES setupapi Version)
    endif()

  endif()

  

  add_subdirectory(translations)

  

  add_subdirectory(src)

  ".


-- Configuring incomplete, errors occurred!
See also "/usr/src/monero-gui/CMakeFiles/CMakeOutput.log".
See also "/usr/src/monero-gui/CMakeFiles/CMakeError.log".

```

## lulighttec | 2020-09-21T23:56:06+00:00
I looked for this whitespace, but couldn't find it; looked for other things like hanging ) but couldn't find any of those either.

```set(BUILD_GUI_DEPS ON)
set(ARCH "x86-64")
set(BUILD_64 ON)

if(NOT MANUAL_SUBMODULES)
  find_package(Git)
  if(GIT_FOUND)
    if(NOT DEV_MODE)
      function (check_submodule relative_path)
        execute_process(COMMAND git rev-parse "HEAD" WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${relative_path} OUTPUT_VARIABLE localHead)
        execute_process(COMMAND git rev-parse "HEAD:${relative_path}" WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} OUTPUT_VARIABLE checkedHead)
        string(COMPARE EQUAL "${localHead}" "${checkedHead}" upToDate)
        if (upToDate)
          message(STATUS "Submodule '${relative_path}' is up-to-date")
        else()
          message(FATAL_ERROR "Submodule '${relative_path}' is not using the checked head. Please update all submodules with\ngit submodule update --init --force --recursive\>
        endif()
      endfunction ()
      message(STATUS "Checking submodules")
      check_submodule(monero)
    else()
      execute_process(COMMAND ${GIT_EXECUTABLE} fetch WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/monero RESULT_VARIABLE GIT_FETCH_RESULT)
      execute_process(COMMAND ${GIT_EXECUTABLE} checkout -f origin/master WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/monero RESULT_VARIABLE GIT_CHECKOUT_MASTER_RESULT)
      execute_process(COMMAND ${GIT_EXECUTABLE} submodule update --init --force --recursive WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/monero RESULT_VARIABLE GIT_SUBMODULE>
      if(NOT GIT_FETCH_RESULT EQUAL "0" OR NOT GIT_CHECKOUT_MASTER_RESULT EQUAL "0" OR NOT GIT_SUBMODULE_UPDATE_RESULT EQUAL "0")
        message(FATAL_ERROR "Updating git submodule to master (-DDEV_MODE=ON) failed")
      endif()

add_subdirectory(monero)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)
```

## xiphon | 2020-09-21T23:58:53+00:00
You can reset the changes with `git checkout CMakeLists.txt` and then apply the patches again.

## selsta | 2020-09-22T00:00:32+00:00
```
if(NOT MANUAL_SUBMODULES)
  find_package(Git)
  if(GIT_FOUND)
    if(NOT DEV_MODE)
      function (check_submodule relative_path)
        execute_process(COMMAND git rev-parse "HEAD" WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${relative_path} OUTPUT_VARIABLE localHead)
        execute_process(COMMAND git rev-parse "HEAD:${relative_path}" WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} OUTPUT_VARIABLE checkedHead)
        string(COMPARE EQUAL "${localHead}" "${checkedHead}" upToDate)
        if (upToDate)
          message(STATUS "Submodule '${relative_path}' is up-to-date")
        else()
          message(FATAL_ERROR "Submodule '${relative_path}' is not using the checked head. Please update all submodules with\ngit submodule update --init --force --recursive\nor run cmake with -DMANUAL_SUBMODULES=1,\n or if you want to build from latest master run cmake with -DDEV_MODE=ON,\n or run make devmode")
        endif()
      endfunction ()
      message(STATUS "Checking submodules")
      check_submodule(monero)
    else()
      execute_process(COMMAND ${GIT_EXECUTABLE} fetch WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/monero RESULT_VARIABLE GIT_FETCH_RESULT)
      execute_process(COMMAND ${GIT_EXECUTABLE} checkout -f origin/master WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/monero RESULT_VARIABLE GIT_CHECKOUT_MASTER_RESULT)
      execute_process(COMMAND ${GIT_EXECUTABLE} submodule update --init --force --recursive WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/monero RESULT_VARIABLE GIT_SUBMODULE_UPDATE_RESULT)
      if(NOT GIT_FETCH_RESULT EQUAL "0" OR NOT GIT_CHECKOUT_MASTER_RESULT EQUAL "0" OR NOT GIT_SUBMODULE_UPDATE_RESULT EQUAL "0")
        message(FATAL_ERROR "Updating git submodule to master (-DDEV_MODE=ON) failed")
      endif()
    endif()
  endif()
endif()
```

It should look like this.

## lulighttec | 2020-09-22T00:23:29+00:00
I made it look like that, and still got the same errors, but this time they started on line 73.  I included the CMakeLists.txt this time.
[CMakeLists.txt](https://github.com/monero-project/monero-gui/files/5258726/CMakeLists.txt)

Here are the errors:

[errors.txt](https://github.com/monero-project/monero-gui/files/5258733/errors.txt)


## xiphon | 2020-09-22T00:28:29+00:00
Have a closer look at line 70 ending

## selsta | 2020-09-22T00:30:54+00:00
If you want to try it from scratch, full list of commands:

```
git clone --recursive https://github.com/monero-project/monero-gui/ monero-gui2
cd monero-gui2
git pull origin pull/3094/head
```

Apply steps in this comment: https://github.com/monero-project/monero-gui/issues/3093#issuecomment-696242832 then back inside monero-gui2 folder:

``` 
mkdir -p build/release
cd build/release
cmake -D ARCH="armv7-a" -D MANUAL_SUBMODULES=ON -D CMAKE_BUILD_TYPE=Release ../..
make -j7
```

## lulighttec | 2020-09-22T00:43:35+00:00
I fixed the missing end of line 70, as @xiphon suggested.  (Must have been a copy/paste error)

Looked good until:
[errors (1).txt](https://github.com/monero-project/monero-gui/files/5258764/errors.1.txt)

One thing mentioned is that some monero files were missing, as in not built yet, though the directory is there so I'm not sure why it couldn't find it.

## selsta | 2020-09-22T00:57:16+00:00
It seems like you forgot `-D MANUAL_SUBMODULES=ON` and also broke your cmake file somehow. Can you try what I described here to make sure no spurious changes are included? https://github.com/monero-project/monero-gui/issues/3093#issuecomment-696451681

## lulighttec | 2020-09-22T01:17:34+00:00
Ok, cloned as instructed into monero-gui2, cmake built the configuration, and then make -j7 resulted in some errors that looked concerned with x86-64, included here.

[errors.txt](https://github.com/monero-project/monero-gui/files/5258801/errors.txt)


## xiphon | 2020-09-22T01:23:02+00:00
Please comment out line 29 in `CMakeLists.txt`:
```diff
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -26,7 +26,7 @@ if(DEBUG)
 endif()

 set(BUILD_GUI_DEPS ON)
-set(ARCH "x86-64")
+#set(ARCH "x86-64")
 set(BUILD_64 ON)

 find_package(Git)
```

## lulighttec | 2020-09-22T01:40:19+00:00
For a second I thought we got a little farther, but no

[errors.txt](https://github.com/monero-project/monero-gui/files/5258853/errors.txt)


## selsta | 2020-09-22T01:41:31+00:00
Also did you make sure to delete your build directory before retrying? :)

## lulighttec | 2020-09-22T01:42:43+00:00
i did, but never hurts to remind me ;-)

## lulighttec | 2020-09-22T01:43:05+00:00
speaking of reminding me, remind me to get you two some lattes when we're done

## xiphon | 2020-09-22T01:49:16+00:00
We are almost there, just don't do `cd ..` after running `cmake` step.

I.e.
```
root@odroid:/usr/src/monero-gui2/build/release# cd ..
root@odroid:/usr/src/monero-gui2/build# cd ..
root@odroid:/usr/src/monero-gui2# make -j7
```

Just run `make -j7` right in `build/release` folder.

## lulighttec | 2020-09-22T02:15:48+00:00
Should I be concerned about this?
```
CMake Warning:
    Manually-specified variables were not used by the project:

            CMAKE_CUILD_TYPE

```


(It's currently 27% into the build, so I guess not)

## selsta | 2020-09-22T02:18:04+00:00
looks like you mistyped CMAKE_BUILD_TYPE during the cmake step

though afaik it should still work so you don't have to cancel the build.

## lulighttec | 2020-09-22T02:20:25+00:00
That's what I thought too,  but I don't remember typing that particular bit


## lulighttec | 2020-09-22T02:56:23+00:00
Still going, but only at 36%, so... dinner time...

## lulighttec | 2020-09-22T15:57:09+00:00
I woke up this morning, and it was finally finished in the monero-gui2/build/release/ folder, and the monerod bin (along with others) is in the monero-gui2/build/release/bin folder.  Does this mean I can now 'make -j7' in the monero-gui2 folder?

## selsta | 2020-09-22T18:54:49+00:00
there should be a `monero-wallet-gui` binary inside monero-gui2/build/release/bin, no more make necessary.

## lulighttec | 2020-09-22T19:00:35+00:00
So about those lattes... :-D

## selsta | 2020-09-22T19:01:48+00:00
does it work now? :) no crash?

## lulighttec | 2020-09-22T19:02:32+00:00
It seems this way, I'm exiting root before I create the wallet and really make sure, but it got past the part where it crashed the first time

## lulighttec | 2020-09-22T19:03:47+00:00
There's probably a quick and easy CLI command to write the contents of monero-gui2 over the original monero-gui, right?  And will that break anything?  like, 
```mv monero-gui2/* monero-gui/```
or would 
```
cd monero-gui2
find -exec mv {} ../monero-gui/ +
```
be better?

## selsta | 2020-09-22T19:11:09+00:00
You should be able to move around the binaries, not sure about changing the whole folder. Might reduce in weird issues if you want to rebuild.

## lulighttec | 2020-09-22T21:03:06+00:00
It is running, and currently downloading the blockchain.  :-)  Also, I opted for fixing a broken shortcut instead of moving anything around; seemed like a safer solution.  Thank you so much for your help!

One question: is there a way to change the transparency of the interface?  When it's in Dark mode, it almost blends in with the background (which is orange) with white floating text, but if I reverse it, the text becomes transparent on a white background, which is even _harder_ to read.  If it means rebuilding, I probably won't bother, but if there's an easy fix...

Also, was serious about lattes.

## selsta | 2020-09-22T23:00:50+00:00
> One question: is there a way to change the transparency of the interface? When it's in Dark mode, it almost blends in with the background (which is orange) with white floating text, but if I reverse it, the text becomes transparent on a white background, which is even harder to read. If it means rebuilding, I probably won't bother, but if there's an easy fix...

Can you make a screenshot? Not sure what you mean with transparency.

> Also, was serious about lattes.

:))

## lulighttec | 2020-09-23T00:48:23+00:00
Took a while, but yes.  lol  Top photo is Dark theme, Bottom photo is Light Theme.

![Screenshot from 2020-09-22 20-34-07](https://user-images.githubusercontent.com/7953383/93951649-ecaaa100-fd14-11ea-9195-317f50da29f9.png)


![Screenshot from 2020-09-22 20-35-28](https://user-images.githubusercontent.com/7953383/93951651-eddbce00-fd14-11ea-82ef-86482b00d1d8.png)


## selsta | 2020-09-23T00:50:33+00:00
That’s definitely a bug, it should not look like that.. hmm

Which Qt version did you use to compile? Can you update your graphics drivers?

Alternatively you can start the GUI with the `QMLSCENE_DEVICE=softwarecontext` env var, but this will use the low quality renderer.. 

## lulighttec | 2020-09-23T00:53:14+00:00
Qt Creator 4.11.0

Based on Qt 5.12.8 (GCC 9.3.0, 32 bit)


Anytime I tried to search for 5, I kept getting pointed here...
TBH, at first I thought it was just extra fancy, because when the wallet is locked, everything behind the password field is blurred and looks pretty cool LOL

Oh, and I should probably mention that that's the way the interface has looked (after it built) for me from day 1, so this looks the same as crashing binary did.

## lulighttec | 2020-09-23T16:06:43+00:00
oooo, it really didn't like when I turned off custom decorations...
Luckily the hotspots still work for the checkboxes and I was able to set it back... the first time.  the second time it crashed the whole shell :-o
I know now not to fiddle with that setting (since it's only for the titlebar).

![Screenshot from 2020-09-23 11-59-33](https://user-images.githubusercontent.com/7953383/94038983-24592d80-fd95-11ea-9dff-68f8ea95e15d.png)




## lulighttec | 2020-09-24T03:09:57+00:00
I did a clean clone into (a fresh) /monero-gui (not the current monero-gui2) and applied patches with git pull (though 3094 wouldn't, so I had to manually remove "AND STATIC" from line 398).  I decided to stop the daemon and go ahead and build it.

it's building _faster_ now...

## lulighttec | 2020-09-24T16:31:31+00:00
Well, no errors anywhere that I could see this time; though something is still not quite right.  Still had the crash when trying to check/uncheck the special decorations box.  This is not a crucial component, right?  Probably ok to load my wallet and continue downloading blockchain?


![Screenshot from 2020-09-24 11-53-06](https://user-images.githubusercontent.com/7953383/94170724-68fccb80-fe5e-11ea-856c-44209bcf978b.png)
![Screenshot from 2020-09-24 11-53-53](https://user-images.githubusercontent.com/7953383/94170728-6a2df880-fe5e-11ea-8b8e-acc39dc01e74.png)
![Screenshot from 2020-09-24 12-28-09](https://user-images.githubusercontent.com/7953383/94173337-cf371d80-fe61-11ea-9e1e-ac8e07c3c111.png)

## selsta | 2020-09-24T16:38:14+00:00
> This is not a crucial component, right?

No, not crucial.

My only suggestion to fix these weird visual issues:

- Try to build with Qt 5.15 instead of 5.12
- update your graphics drivers (not sure if that is possible)

## lulighttec | 2020-09-24T16:39:25+00:00
I'm not sure if that's possible either, (updating graphics drivers) but I'll try.  Might be worth trying that first.

## lulighttec | 2020-09-24T17:26:59+00:00
OMG, updated firmware and now it won't boot.  This is a problem for a different chunk of github, but seriously? ready to cry

## selsta | 2020-09-24T17:47:32+00:00
Does anything described here help? https://wiki.odroid.com/troubleshooting/odroid_flashing_tools

## lulighttec | 2020-09-24T18:03:07+00:00
Well, that's what I was currently looking at.  I was able to rescue the wallet file, and i can probably rescue the partially downloaded blockchain too, should i need to re-etch my card.  I found a spare microSD and I'm flashing with the image.  I'm hoping that will bring it back, and then I can go from there.

## lulighttec | 2020-09-25T15:23:49+00:00
well, it boots again.  in the process of putting things back together.  Since I essentially had to start over, I'm taking the opportunity to build Qt 5.15 first.

## lulighttec | 2020-09-28T01:18:38+00:00
<sigh> It gets all the way to the end of the build and fails.  I have a different error, though.

[errors.txt](https://github.com/monero-project/monero-gui/files/5289439/errors.txt)


## selsta | 2020-09-28T01:27:56+00:00
Anything different with this setup?

## lulighttec | 2020-09-28T01:31:51+00:00
I built qt 5.15.1, built qt creator, otherwise no, I tried to do it exactly the same.

Sent from my iPhone

On Sep 27, 2020, at 9:28 PM, selsta <notifications@github.com> wrote:

﻿

Anything different with this setup?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3093#issuecomment-699722169>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AB4VXZ25SGRMEMPWCSRSAILSH7RCRANCNFSM4RTEL5IA>.


## selsta | 2020-09-28T01:34:10+00:00
You have to set CMAKE_PREFIX_PATH to your Qt 5.15.1 path in your cmake command, else 5.12 from your package manager gets picked up. On my system it is `-D CMAKE_PREFIX_PATH=~/dev/Qt/5.15.1/clang_64/`, on your system it won’t be called clang_64 but something else.

## lulighttec | 2020-09-28T01:37:08+00:00
Ok.  I’ll try that.  I put the path in the environment, but I guess it didn’t pick it up. 

Sent from my iPhone

On Sep 27, 2020, at 9:34 PM, selsta <notifications@github.com> wrote:

﻿

You have to set CMAKE_PREFIX_PATH to your Qt 5.15.1 path in your cmake command, else 5.12 gets picked up. On my system it is -D CMAKE_PREFIX_PATH=~/dev/Qt/5.15.1/clang_64/, on your system it won’t be called clang_64 but something else.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3093#issuecomment-699723395>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AB4VXZ35XSJ6M4NTFJQTGDTSH7RZ5ANCNFSM4RTEL5IA>.


## lulighttec | 2020-09-28T02:06:45+00:00
`CMAKE_PREFIX_PATH=/usr/local/Qt-5.15.1/bin/`?

## selsta | 2020-09-28T07:32:25+00:00
I think it should be without bin, just /usr/local/Qt-5.15.1/

Anyway if you want to try Qt 5.12.1 again make sure to remove 5.15 out of your path, I can imagine this producing weird issues.

## lulighttec | 2020-09-28T14:43:51+00:00
I did make sure to clean out 5.12 to avoid weird issues before I started building again.  At one point, if I was non-root, I had access to 5.15.1 in the path, but if I was root, only had access to 5.12.  I fixed that.  

It built last night, again with one error at the very end, but I used /bin/ on the end of the path.  I do wish it didn't take 8 hours to get to the error at the end.  I just set it to "make" again, this time without /bin/.  I guess in about 7 hours I'll let you know what happens.

## lulighttec | 2020-09-28T21:19:03+00:00
It got all the way through both cmake and make without any errors.  However, when I try to run it:

[errors.txt](https://github.com/monero-project/monero-gui/files/5295113/errors.txt)

Which application is it suggesting I reinstall?

## lulighttec | 2020-09-28T21:37:37+00:00
Holdup... I ran from /usr/local/bin.... and... I think it's running... is _this_ it?

![Screenshot from 2020-09-28 21-33-05](https://user-images.githubusercontent.com/7953383/94488788-47c71280-01b1-11eb-9a08-fc5e31d2e91e.png)
![Screenshot from 2020-09-28 21-33-29](https://user-images.githubusercontent.com/7953383/94488795-4990d600-01b1-11eb-9c5e-827f9a0b28b7.png)


## selsta | 2020-09-29T00:44:14+00:00
Looks good without graphics glitches :)

## selsta | 2020-09-29T01:25:11+00:00
By the way, you can install `ccache` with your package manager it it will greatly speed up subsequent builds, but looks like you managed to build the GUI now anyway.

## lulighttec | 2020-09-29T06:53:45+00:00
I wish I had known about ccache at the beginning... oh well, next time I'll know.  Hopefully there won't be a next time.  :-)  Right now, it's syncing, and the interface doesn't seem to be doing any glitching or crashing, so I'm going to leave it be until it finishes and go to bed.  I think we're there, though.


I may have spoken too soon.  Doesn't appear to be syncing...
```
E Unexpected recv fail
I Failed to invoke http request to /json_rpc
D Wallet connection status changed 0
D checking connection status
D Wallet connection status changed 3
D Problems at read: Operation canceled
```
Just keeps looping this over and over


## xiphon | 2020-09-29T16:33:40+00:00
Make sure you have `monerod` process running. You can start it from the GUI, see Settings -> Node tab.

## lulighttec | 2020-09-29T16:40:51+00:00
I have tried, but monerod keeps failing when I start it, saying:
```

I SYNCHRONIZATION started
I [batch] DB resize needed
W Failed to set new mapsize: Cannot allocate memory
E Error in handle_invoke_map: Failed to set new mapsize: Cannot allocate memory
```
It won't go past this point, and if I type "exit" to try to stop the daemon, it will 'Stop signal sent', but the process never stops.  Same thing with "stop_daemon".  (I typed "help" at one point, and learned some commands.)

I should also add that I have tried rebooting to start fresh, and have tried starting the daemon from inside the gui, but it fails to start, so the gui suggests trying to start manually.  When I start manually (from the terminal) I get what you see above.

## lulighttec | 2020-09-29T17:23:21+00:00
Not only this, but once monerod is started, I can't get it to stop and free up the IPv4 binding so I can try again.  It just keeps running and running, not doing anything.  I even tried closing the terminal to kill the running process, and _that_ didn't work.  Edit: learned how to properly use the kill command in terminal.  Still, this is kind of a problem, yes?

## xiphon | 2020-09-29T18:24:07+00:00
> Cannot allocate memory

The device ran out of memory. Nothing we can do about it on the Monero GUI side.

## lulighttec | 2020-09-29T18:26:45+00:00
That can't be the case.  I'm looking at htop and it's definitely not, and it worked at least once right after I built it, and besides that, other things keep running, so how can this be?

## xiphon | 2020-09-29T18:37:56+00:00
Do you have enough free space on the disk?

## lulighttec | 2020-09-29T18:41:59+00:00
I have 92 of 128GB available, and I could probably dump some things and get a bit more if i needed to, though last I read the blockchain was only 75GB, so that should be enough, shouldn't it? 

Edit: I have increased free space to 105GB.  Same result.

## xiphon | 2020-09-29T19:08:58+00:00
Could you try official monero ARMV7 cli binary? https://downloads.getmonero.org/cli/linuxarm7

## lulighttec | 2020-09-29T19:23:38+00:00
^^^^This daemon works, and works with the gui, so it must be a build problem.  I think my solution will be to replace what I built with what I just downloaded, and that should fix things, yes?

## xiphon | 2020-09-29T19:39:41+00:00
Right.

# Action History
- Created by: lulighttec | 2020-09-19T17:35:05+00:00
- Closed at: 2020-09-25T23:26:07+00:00
