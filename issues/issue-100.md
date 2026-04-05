---
title: Make faild
source_url: https://github.com/xmrig/xmrig/issues/100
author: Halbritter
assignees: []
labels: []
created_at: '2017-09-08T08:34:53+00:00'
updated_at: '2017-09-08T08:47:46+00:00'
type: issue
status: closed
closed_at: '2017-09-08T08:47:46+00:00'
---

# Original Description
Make faild with the folowing message:

/home/henrik/xmrig/build$ make
[ 21%] Built target jansson
[ 30%] Built target cpuid
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
/home/henrik/xmrig/src/App.cpp: In member function ‘int App::exec()’:
/home/henrik/xmrig/src/App.cpp:124:36: error: ‘uv_loop_close’ was not declared in this scope
     uv_loop_close(uv_default_loop());
                                    ^
CMakeFiles/xmrig.dir/build.make:54: recipe for target 'CMakeFiles/xmrig.dir/src/App.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Error 1
CMakeFiles/Makefile2:61: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:76: recipe for target 'all' failed
make: *** [all] Error 2

I am using 
henrik@srv01:/home/henrik/xmrig/build$ make -v
GNU Make 4.0
Built for x86_64-pc-linux-gnu

henrik@srv01:/home/henrik/xmrig/build$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/4.9/lto-wrapper
Target: x86_64-linux-gnu
[...]
gcc version 4.9.2 (Debian 4.9.2-10)

and 

henrik@srv01:/home/henrik/xmrig/build$ cmake --version
cmake version 3.0.2


# Discussion History
## xmrig | 2017-09-08T08:36:17+00:00
libuv 0.10 not supported, you need libuv 1.x.x

## Halbritter | 2017-09-08T08:47:46+00:00
Thank you. That was the problem. 

# Action History
- Created by: Halbritter | 2017-09-08T08:34:53+00:00
- Closed at: 2017-09-08T08:47:46+00:00
