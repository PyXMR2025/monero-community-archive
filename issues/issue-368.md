---
title: 'GUI: Heap corruption on exit'
source_url: https://github.com/seraphis-migration/monero/issues/368
author: ModemNakata
assignees: []
labels: []
created_at: '2026-05-09T17:25:01+00:00'
updated_at: '2026-05-09T23:22:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm running monero-wallet-gui on CachyOS using this command:

`QT_QPA_PLATFORM=xcb ./monero-wallet-gui`

I use "QT_QPA_PLATFORM=xcb" to make it work on Wayland.

When I exit GUI, but keep the daemon running, it crashes during shutdown:

**31385 Segmentation fault         (core dumped) QT_QPA_PLATFORM=xcb ./monero-wallet-gui**

```
[Thread 0x7fffb95fe6c0 (LWP 39603) exited]
free(): invalid size
free(): chunks in smallbin corrupted

Thread 1 "monero-wallet-g" received signal SIGABRT, Aborted.
```

Backtrace: (GDB)
```
Downloading 4.48 K source file /usr/src/debug/glibc/glibc/nptl/pthread_kill.c
__pthread_kill_implementation (threadid=<optimized out>, signo=6, no_tid=0) at pthread_kill.c:44                                                                                                
44	      return INTERNAL_SYSCALL_ERROR_P (ret) ? INTERNAL_SYSCALL_ERRNO (ret) : 0;
(gdb) 
(gdb) bt full
#0  __pthread_kill_implementation (threadid=<optimized out>, signo=6, no_tid=0) at pthread_kill.c:44
        tid = <optimized out>
        ret = 0
        pd = <optimized out>
        old_mask = {__val = {93825113665192}}
        ret = <optimized out>
#1  __pthread_kill_internal (threadid=<optimized out>, signo=6) at pthread_kill.c:89
No locals.
#2  __GI___pthread_kill (threadid=<optimized out>, signo=signo@entry=6) at pthread_kill.c:100
No locals.
#3  0x00007ffff7644c88 in __GI_raise (sig=sig@entry=6) at ../sysdeps/posix/raise.c:26
        ret = <optimized out>
#4  0x00007ffff7625795 in __GI_abort () at abort.c:77
        act = {__sigaction_handler = {sa_handler = 0x7fffffffdaf0, sa_sigaction = 0x7fffffffdaf0}, sa_mask = {__val = {140737488344800, 140737488345840, 16731240226869022976, 
              140737488345584, 140737488345840, 140737488345840, 1, 93825116550432, 5, 140737488345696, 93825006932379, 93825118317088, 93824997314753, 93825116550432, 140737488346216, 
              140737488346224}}, sa_flags = 1555969104, sa_restorer = 0x0}
#5  0x00007ffff7626a31 in __libc_message_impl (vma_name=vma_name@entry=0x7ffff77e8851 "glibc: fatal", fmt=fmt@entry=0x7ffff77eb8e8 "%s\n") at ../sysdeps/posix/libc_fatal.c:138
        ap = {{gp_offset = 24, fp_offset = 32767, overflow_arg_area = 0x7fffffffd890, reg_save_area = 0x7fffffffd820}}
        fd = 2
        iov = {{iov_base = 0x7ffff77e9d89, iov_len = 20}, {iov_base = 0x7ffff77eb8ea, iov_len = 1}, {iov_base = 0x5, iov_len = 93825018790018}, {iov_base = 0x700000008, 
            iov_len = 16731240226869022976}, {iov_base = 0x7ffff788f080, iov_len = 16731240226869022976}, {iov_base = 0x7fffffffd9f0, iov_len = 16731240226869022976}, {
            iov_base = 0x7fffffffdaf0, iov_len = 93825116550224}, {iov_base = 0x55555ca77eb0, iov_len = 93825115059264}, {iov_base = 0x5, iov_len = 93825003261087}, {
            iov_base = 0x55555cbe3450, iov_len = 93825114555952}, {iov_base = 0x55555cbe3450, iov_len = 93825018988602}, {iov_base = 0x0, iov_len = 93825003300832}, {
            iov_base = 0x55555cb2a600, iov_len = 140737488347424}, {iov_base = 0xb, iov_len = 93825113744472}, {iov_base = 0x7fff94b40140, iov_len = 140735684958536}}
        iovcnt = <optimized out>
        total = <optimized out>
        cp = <optimized out>
#6  0x00007ffff76b92ae in __libc_message_wrapper (vmaname=0x7ffff77e8851 "glibc: fatal", fmt=0x7ffff77eb8e8 "%s\n") at ../include/stdio.h:203
No locals.
#7  malloc_printerr (str=<optimized out>) at malloc.c:5341
No locals.
#8  0x00007ffff76b92c1 in malloc_printerr_tail (str=<optimized out>) at malloc.c:5358
No locals.
#9  0x0000555556e76e2a in QSortFilterProxyModelPrivate::_q_sourceModelDestroyed() ()
No symbol table info available.
#10 0x0000555556e75dc2 in QAbstractProxyModel::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) ()
No symbol table info available.
#11 0x0000555556ed9aa9 in QObject::event(QEvent*) ()
No symbol table info available.
#12 0x0000555555fd8c9f in QApplicationPrivate::notify_helper(QObject*, QEvent*) ()
No symbol table info available.
#13 0x0000555555fe27e0 in QApplication::notify(QObject*, QEvent*) ()
No symbol table info available.
#14 0x0000555556ea8cda in QCoreApplication::notifyInternal2(QObject*, QEvent*) ()
No symbol table info available.
#15 0x0000555556eaca15 in QCoreApplicationPrivate::sendPostedEvents(QObject*, int, QThreadData*) ()
--Type <RET> for more, q to quit, c to continue without paging--c
No symbol table info available.
#16 0x0000555556f03f73 in postEventSourceDispatch(_GSource*, int (*)(void*), void*) ()
No symbol table info available.
#17 0x00007ffff7ceb02d in ?? () from /usr/lib/libglib-2.0.so.0
No symbol table info available.
#18 0x00007ffff7cec558 in ?? () from /usr/lib/libglib-2.0.so.0
No symbol table info available.
#19 0x00007ffff7cec6b2 in g_main_context_iteration () from /usr/lib/libglib-2.0.so.0
No symbol table info available.
#20 0x0000555556f040ce in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) ()
No symbol table info available.
#21 0x0000555556ea7a8e in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) ()
No symbol table info available.
#22 0x0000555556eb1106 in QCoreApplication::exec() ()
No symbol table info available.
#23 0x000055555598f147 in main ()
No symbol table info available.
(gdb) 
```

# Discussion History
## ComputeryPony | 2026-05-09T22:16:33+00:00
Judging from the call stack this looks like another instance of #268 

## ModemNakata | 2026-05-09T23:22:04+00:00
Sorry, I should have checked it before submitting

> Judging from the call stack this looks like another instance of [#268](https://github.com/seraphis-migration/monero/issues/268)



# Action History
- Created by: ModemNakata | 2026-05-09T17:25:01+00:00
