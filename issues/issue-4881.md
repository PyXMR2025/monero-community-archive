---
title: '`corrupted double-linked list` error on wallet cli exit on Ubuntu 17.10 amd64'
source_url: https://github.com/monero-project/monero/issues/4881
author: naughtyfox
assignees: []
labels: []
created_at: '2018-11-21T11:18:01+00:00'
updated_at: '2018-12-04T16:17:17+00:00'
type: issue
status: closed
closed_at: '2018-12-04T16:17:17+00:00'
---

# Original Description
Master branch, commit 84dd674cd049884c5841c4142e717ae4cb8879f2
Got an error on exit:
```
[wallet 53MGew]: *** Error in `./monero-wallet-cli': corrupted double-linked list: 0x000055ec6862f760 ***
Aborted (core dumped)
```

gdb:
```
[wallet 53MGew]: [Thread 0x7fffeea29700 (LWP 10699) exited]
[Thread 0x7fffe6611700 (LWP 10703) exited]
[Thread 0x7fffe6b12700 (LWP 10702) exited]
[Thread 0x7fffe7013700 (LWP 10701) exited]
[Thread 0x7fffe7514700 (LWP 10700) exited]
*** Error in `/home/user/src/monero/build/bin/monero-wallet-cli': corrupted double-linked list: 0x0000555555926760 ***

Thread 1 "monero-wallet-c" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
51	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) thread apply all bt

Thread 1 (Thread 0x7ffff7fbc7c0 (LWP 10695)):
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007ffff38fcf5d in __GI_abort () at abort.c:90
#2  0x00007ffff394528d in __libc_message (action=<optimized out>, fmt=fmt@entry=0x7ffff3a6c528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007ffff394d449 in malloc_printerr (ar_ptr=0x7ffff3c9ec20 <main_arena>, ptr=0x555555926760, str=0x7ffff3a68e0b "corrupted double-linked list", action=<optimized out>) at malloc.c:5426
#4  malloc_consolidate (av=av@entry=0x7ffff3c9ec20 <main_arena>) at malloc.c:4498
#5  0x00007ffff394ee08 in _int_free (av=0x7ffff3c9ec20 <main_arena>, p=<optimized out>, have_lock=0) at malloc.c:4398
#6  0x00007ffff395344e in __GI___libc_free (mem=<optimized out>) at malloc.c:3145
#7  0x00007ffff38ffeed in __run_exit_handlers (status=0, listp=0x7ffff3c9e6f8 <__exit_funcs>, run_list_atexit=run_list_atexit@entry=true, run_dtors=run_dtors@entry=true) at exit.c:92
#8  0x00007ffff38fff1a in __GI_exit (status=<optimized out>) at exit.c:105
#9  0x00007ffff38e51c8 in __libc_start_main (main=0x555555609d61 <main(int, char**)>, argc=8, argv=0x7fffffffd9d8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffd9c8) at ../csu/libc-start.c:342
#10 0x00005555555cccda in _start ()
(gdb) 
```


# Discussion History
## moneromooo-monero | 2018-11-21T11:30:40+00:00
Either run with valgrind, or rebuild with ASAN (-D SANITIZE=ON) and run again. Then see what errors you get before that.

As for the mlocker thing, that's been fixed a while back.

## naughtyfox | 2018-11-21T12:09:41+00:00
> As for the mlocker thing, that's been fixed a while back

Okay, I'll change the issue description

## naughtyfox | 2018-11-21T12:21:45+00:00
I launched it with valgrind (without additional options). The log is pretty big (65 KB), I uploaded it here - https://www.dropbox.com/s/k66efh7c8ch00c3/valgrind.log?dl=0

## moneromooo-monero | 2018-11-21T15:27:57+00:00
Does this fix it ?

<pre>
diff --git a/contrib/epee/src/mlocker.cpp b/contrib/epee/src/mlocker.cpp
index 807e60984..ad18fe0fe 100644
--- a/contrib/epee/src/mlocker.cpp
+++ b/contrib/epee/src/mlocker.cpp
@@ -89,8 +89,8 @@ namespace epee
   }
   std::map<size_t, unsigned int> &mlocker::map()
   {
-    static std::map<size_t, unsigned int> vmap;
-    return vmap;
+    static std::map<size_t, unsigned int> *vmap = new std::map<size_t, unsigned int>();
+    return *vmap;
   }
 
   size_t mlocker::get_page_size()
</pre>

## sanderfoobar | 2018-11-22T01:38:19+00:00
moo's patch did not work for me. This however did:

```
diff --git a/contrib/epee/src/mlocker.cpp b/contrib/epee/src/mlocker.cpp
index c3262e8f..b3539308 100644
--- a/contrib/epee/src/mlocker.cpp
+++ b/contrib/epee/src/mlocker.cpp
@@ -89,8 +89,8 @@ namespace epee
   }
   std::map<size_t, unsigned int> &mlocker::map()
   {
-    static std::map<size_t, unsigned int> vmap;
-    return vmap;
+    static std::map<size_t, unsigned int> *vmap = new std::map<size_t, unsigned int>();
+    return *vmap;
   }
 
   size_t mlocker::get_page_size()
```

## moneromooo-monero | 2018-11-22T01:47:31+00:00
I could repro the problem, so I PRed it: https://github.com/monero-project/monero/pull/4883

## moneromooo-monero | 2018-11-22T01:48:06+00:00
Sorry, dumb github mangling patches if you forget to escape...

## moneromooo-monero | 2018-12-04T16:05:28+00:00
+resolved

# Action History
- Created by: naughtyfox | 2018-11-21T11:18:01+00:00
- Closed at: 2018-12-04T16:17:17+00:00
