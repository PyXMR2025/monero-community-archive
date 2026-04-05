---
title: Error compiling using MSYS2
source_url: https://github.com/xmrig/xmrig/issues/102
author: sanitariu
assignees: []
labels: []
created_at: '2017-09-08T10:09:09+00:00'
updated_at: '2017-09-08T13:08:42+00:00'
type: issue
status: closed
closed_at: '2017-09-08T13:08:42+00:00'
---

# Original Description
Seems like affinity is missing on Windows. How we can fix this ?

--------------------------------------------
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
/home/dri/xmrig/src/Cpu_unix.cpp: In static member function ‘static void Cpu::setAffinity(int, uint64_t)’:
/home/dri/xmrig/src/Cpu_unix.cpp:46:5: error: ‘cpu_set_t’ was not declared in this scope
     cpu_set_t set;
     ^~~~~~~~~
/home/dri/xmrig/src/Cpu_unix.cpp:47:15: error: ‘set’ was not declared in this scope
     CPU_ZERO(&set);
               ^~~
/home/dri/xmrig/src/Cpu_unix.cpp:47:18: error: ‘CPU_ZERO’ was not declared in this scope
     CPU_ZERO(&set);
                  ^
/home/dri/xmrig/src/Cpu_unix.cpp:51:28: error: ‘CPU_SET’ was not declared in this scope
             CPU_SET(i, &set);
                            ^
/home/dri/xmrig/src/Cpu_unix.cpp:56:48: error: ‘sched_setaffinity’ was not declared in this scope
         sched_setaffinity(0, sizeof(&set), &set);
                                                ^
/home/dri/xmrig/src/Cpu_unix.cpp:58:66: error: ‘pthread_setaffinity_np’ was not declared in this scope
         pthread_setaffinity_np(pthread_self(), sizeof(&set), &set);
                                                                  ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:639: CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:69: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
------------------------------------------------


# Discussion History
## xmrig | 2017-09-08T11:49:50+00:00
Somehow you trying to build Linux specific code on Windows. Windows  specific code placed in Cpu_win.cpp.

## sanitariu | 2017-09-08T13:08:42+00:00
I fixed it thanks for helping.

# Action History
- Created by: sanitariu | 2017-09-08T10:09:09+00:00
- Closed at: 2017-09-08T13:08:42+00:00
