---
title: please add the Solaris/SmartOS support
source_url: https://github.com/xmrig/xmrig/issues/363
author: drook
assignees: []
labels:
- bug
- enhancement
- wontfix
created_at: '2018-01-26T06:52:09+00:00'
updated_at: '2019-08-02T12:48:09+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:48:09+00:00'
---

# Original Description
Yup, I know I'm probably requesting something weird, but would be nice to have this,

Solaris derivatives don't have _cpu_set_t_, _processor_bind()_ needs to be called instead of _sched_setaffinity()_/_pthread_setaffinity_np()_.

Currently it crashes on the affinity code part:

````buildlog
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o                                                      
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o                                                      
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp: In static member function ‘static void Cpu::setAffinity(int, uint64_t)’:
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp:59:5: error: ‘cpu_set_t’ was not declared in this scope
     cpu_set_t set;
     ^
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp:59:15: error: expected ‘;’ before ‘set’
     cpu_set_t set;
               ^
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp:60:15: error: ‘set’ was not declared in this scope
     CPU_ZERO(&set);
               ^
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp:60:18: error: ‘CPU_ZERO’ was not declared in this scope
     CPU_ZERO(&set);
                  ^
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp:64:28: error: ‘CPU_SET’ was not declared in this scope
             CPU_SET(i, &set);
                            ^
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp:70:48: error: ‘sched_setaffinity’ was not declared in this scope
         sched_setaffinity(0, sizeof(&set), &set);
                                                ^
/home/emz/src/xmrig-2.4.4/src/Cpu_unix.cpp:74:66: error: ‘pthread_setaffinity_np’ was not declared in this scope
         pthread_setaffinity_np(pthread_self(), sizeof(&set), &set);
                                                                  ^
gmake[2]: *** [CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o] Error 1
gmake[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
````

Also, variables named ERR interferes with some of the solaris system ones, so it needs some workaround:

````patch
--- ConsoleLog.cpp.orig 2018-01-26 09:49:03.681665834 +0300
+++ ConsoleLog.cpp      2018-01-26 09:49:10.291900222 +0300
@@ -80,7 +80,7 @@
     const char* color = nullptr;
     if (m_colors) {
         switch (level) {
-        case Log::ERR:
+        case Log::XMRRERR:
             color = Log::kCL_RED;
             break;
 
--- Log.h.orig  2018-01-26 09:33:24.842139927 +0300
+++ Log.h       2018-01-26 09:34:26.603765819 +0300
@@ -36,7 +36,7 @@
 {
 public:
     enum Level {
-        ERR,
+        XMRRERR,
         WARNING,
         NOTICE,
         INFO,
@@ -71,7 +71,7 @@
 };
 
 
-#define LOG_ERR(x, ...)    Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
+#define LOG_ERR(x, ...)    Log::i()->message(Log::XMRRERR,     x, ##__VA_ARGS__)
 #define LOG_WARN(x, ...)   Log::i()->message(Log::WARNING, x, ##__VA_ARGS__)
 #define LOG_NOTICE(x, ...) Log::i()->message(Log::NOTICE,  x, ##__VA_ARGS__)
 #define LOG_INFO(x, ...)   Log::i()->message(Log::INFO,    x, ##__VA_ARGS__)
@@ -83,7 +83,7 @@
 #endif
 
 #if defined(APP_DEBUG) || defined(APP_DEVEL)
-#   define LOG_DEBUG_ERR(x, ...)  Log::i()->message(Log::ERR,     x, ##__VA_ARGS__)
+#   define LOG_DEBUG_ERR(x, ...)  Log::i()->message(Log::XMRRERR,     x, ##__VA_ARGS__)
 #   define LOG_DEBUG_WARN(x, ...) Log::i()->message(Log::WARNING, x, ##__VA_ARGS__)
 #else
 #   define LOG_DEBUG_ERR(x, ...)
````

# Discussion History
## drook | 2018-01-26T22:09:48+00:00
I managed to build on Solaris 11 (and it's working), here's [edited: almost clean and sane version] the Solaris patch, I hope it's compatible with the rest of platforms (however, cmake platform detection still needs to be worked on):

````patch
--- Cpu_unix.cpp.orig   2018-01-11 11:08:24.000000000 +0300
+++ Cpu_unix.cpp        2018-01-28 09:27:02.851690079 +0300
@@ -43,6 +43,13 @@
 typedef cpuset_t cpu_set_t;
 #endif

+#ifdef __SOLARIS__
+#include <sys/types.h>
+#include <sys/processor.h>
+#include <sys/procset.h>
+#include <sys/pset.h>
+typedef psetid_t cpu_set_t;
+#endif

 void Cpu::init()
 {
@@ -57,21 +64,31 @@
 void Cpu::setAffinity(int id, uint64_t mask)
 {
     cpu_set_t set;
+#   ifndef __SOLARIS__
     CPU_ZERO(&set);
+#   else
+    pset_create(&set);
+#   endif

     for (int i = 0; i < m_totalThreads; i++) {
         if (mask & (1UL << i)) {
+#       ifndef __SOLARIS__
             CPU_SET(i, &set);
+#       else
+            pset_assign(set, i, NULL);
+#       endif
         }
     }

     if (id == -1) {
-#       ifndef __FreeBSD__
+#       if !defined(__FreeBSD__) && !defined(__SOLARIS__)
         sched_setaffinity(0, sizeof(&set), &set);
 #       endif
     } else {
-#       ifndef __ANDROID__
+#       if !defined(__ANDROID__) && !defined(__SOLARIS__)
         pthread_setaffinity_np(pthread_self(), sizeof(&set), &set);
+#       elif defined(__SOLARIS__)
+        pset_bind(set, P_LWPID, P_MYID, NULL);
 #       else
         sched_setaffinity(gettid(), sizeof(&set), &set);
 #       endif
--- Mem_unix.cpp.orig   2018-01-26 22:39:35.792328524 +0300
+++ Mem_unix.cpp        2018-01-28 12:10:07.539791032 +0300
@@ -59,6 +59,8 @@
     m_memory = static_cast<uint8_t*>(mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, VM_FLAGS_SUPERPAGE_SIZE_2MB, 0));
 #   elif defined(__FreeBSD__)
     m_memory = static_cast<uint8_t*>(mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_ALIGNED_SUPER | MAP_PREFAULT_READ, -1, 0));
+#   elif defined(__SOLARIS__)
+    m_memory = static_cast<uint8_t*>(mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, 0, 0));
 #   else
     m_memory = static_cast<uint8_t*>(mmap(0, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE, 0, 0));
 #   endif
@@ -69,7 +71,11 @@

     m_flags |= HugepagesEnabled;

+#   if defined(__SOLARIS__)
+    if (madvise((char*)m_memory, size, MADV_RANDOM | MADV_WILLNEED) != 0) {
+#   else
     if (madvise(m_memory, size, MADV_RANDOM | MADV_WILLNEED) != 0) {
+#   endif
         LOG_ERR("madvise failed");
     }
````

Sure thing it needs more work - especially for integrating in in the tree with proper conditioning, as well with adding some tests for cmake to detect a Solaris platform.

## yuhong | 2018-01-27T02:12:36+00:00
It might be worth adding SPARC assembly as well.

# Action History
- Created by: drook | 2018-01-26T06:52:09+00:00
- Closed at: 2019-08-02T12:48:09+00:00
