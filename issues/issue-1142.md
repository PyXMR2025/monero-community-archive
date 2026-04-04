---
title: monerod v0-10-0-0 segfaults frequently
source_url: https://github.com/monero-project/monero/issues/1142
author: ElLamparto
assignees: []
labels: []
created_at: '2016-09-27T09:02:54+00:00'
updated_at: '2017-08-09T19:17:21+00:00'
type: issue
status: closed
closed_at: '2017-08-09T19:17:21+00:00'
---

# Original Description
1. Always at exit
   ![monerodsegfault](https://cloud.githubusercontent.com/assets/9163437/18866787/c315e452-84a1-11e6-859b-eb1097fc88a9.png)
2. After synchro at 99.5%, it segfaults every a few minutes
   ![monerodsegfault2](https://cloud.githubusercontent.com/assets/9163437/18866839/e640802c-84a1-11e6-93ca-4eb37fc0ed35.png)

OS: Debian Jessie 32bit


# Discussion History
## moneromooo-monero | 2016-09-27T17:41:17+00:00
You can ignore the first one.

For second one, can you share a stack trace ?

ulimit -c unlimited
Run monerod with whatever options you use
gdb monerod core*
bt


## ElLamparto | 2016-09-28T07:26:44+00:00
Last time I started monerod, it quickly took 100% CPU and I had to kill it... I'll play with it in the coming weekend.


## moneromooo-monero | 2016-09-29T18:52:47+00:00
If you have a fast connection, and you're not synced, it's expected: it will quickly download blocks, and verify them. The verification part is somewhat CPU intensive.


## ElLamparto | 2016-10-01T10:25:51+00:00
Here is the gdb output:

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x986fdb40 (LWP 757)]
0x0850f203 in mdb_cursor_unref ()

backtrace:

(gdb) backtrace
#0  0x0850f203 in mdb_cursor_unref ()
#1  0x085199b3 in mdb_cursor_close ()
#2  0x0848b2fe in boost::thread_specific_ptrcryptonote::mdb_threadinfo::delete_data::operator()(void*) ()
#3  0x085302ad in tls_destructor.part ()
#4  0x0853177b in thread_proxy ()
#5  0xb7f4fefb in start_thread (arg=0x986fdb40) at pthread_create.c:309
#6  0xb7e87d0e in clone () at ../sysdeps/unix/sysv/linux/i386/clone.S:129


## moneromooo-monero | 2016-10-01T16:09:27+00:00
Thanks.


## rboe | 2017-01-09T18:21:43+00:00
Same here with version (v0.10.1.0-release) on Ubuntu 16.04.1 LTS 32 Bit.

- crashes nearly always at exit
- crashes after snychronizing most of the blocks (7 days behind) randomly after snychronizing some more blocks.

Before this lots of threads are crated and exit. I'm not sure if this is normal behavior.

```
...
[New Thread 0x938fcb40 (LWP 26085)]
[New Thread 0x940fdb40 (LWP 26086)]
[New Thread 0x948feb40 (LWP 26087)]
[New Thread 0x950ffb40 (LWP 26088)]
[Thread 0x950ffb40 (LWP 26088) exited]
[Thread 0x948feb40 (LWP 26087) exited]
[Thread 0x940fdb40 (LWP 26086) exited]
[Thread 0x938fcb40 (LWP 26085) exited]
2017-Jan-09 19:10:28.518271 [P2P3][37.59.53.25:18080 OUT]Synced 1214804/1220160
[New Thread 0x950ffb40 (LWP 26089)]
[New Thread 0x948feb40 (LWP 26090)]
[New Thread 0x940fdb40 (LWP 26091)]
[New Thread 0x938fcb40 (LWP 26092)]
[Thread 0x950ffb40 (LWP 26089) exited]
[Thread 0x940fdb40 (LWP 26091) exited]
[Thread 0x948feb40 (LWP 26090) exited]
[Thread 0x938fcb40 (LWP 26092) exited]
[New Thread 0x938fcb40 (LWP 26093)]
[New Thread 0x940fdb40 (LWP 26094)]
[New Thread 0x948feb40 (LWP 26095)]
[New Thread 0x950ffb40 (LWP 26096)]
[Thread 0x948feb40 (LWP 26095) exited]

Thread 10836 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x940fdb40 (LWP 26094)]
0x08528c33 in mdb_cursor_unref ()
(gdb) bt
#0  0x08528c33 in mdb_cursor_unref ()
#1  0x085333e3 in mdb_cursor_close ()
#2  0x08407efe in boost::thread_specific_ptr<cryptonote::mdb_threadinfo>::delete_data::operator()(void*) ()
#3  0x08549cdd in tls_destructor.part ()
#4  0x0854b1ab in thread_proxy ()
#5  0xb7f4c295 in start_thread (arg=0x940fdb40) at pthread_create.c:333
#6  0xb7e76eee in clone () at ../sysdeps/unix/sysv/linux/i386/clone.S:114

```

## moneromooo-monero | 2017-08-08T11:21:03+00:00
Is this still happening with 0.10.3.1 ?

## ElLamparto | 2017-08-09T19:17:21+00:00
No, it isn't.

# Action History
- Created by: ElLamparto | 2016-09-27T09:02:54+00:00
- Closed at: 2017-08-09T19:17:21+00:00
