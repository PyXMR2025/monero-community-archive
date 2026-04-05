---
title: 'xmrig/src/api/NetworkState.h:48: error: function definition does not declare
  parameters'
source_url: https://github.com/xmrig/xmrig/issues/444
author: minzak
assignees: []
labels: []
created_at: '2018-03-13T15:34:56+00:00'
updated_at: '2018-03-16T17:47:01+00:00'
type: issue
status: closed
closed_at: '2018-03-16T17:47:01+00:00'
---

# Original Description
CentOS 6.
I replaces -Ofast to -O2 and use -std=gnu++0x

make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
In file included from /opt/xmrig/src/api/ApiState.h:28,
                 from /opt/xmrig/src/api/Api.cpp:28:
/opt/xmrig/src/api/NetworkState.h:48: error: function definition does not declare parameters
/opt/xmrig/src/api/Api.cpp:31: error: ‘nullptr’ was not declared in this scope
/opt/xmrig/src/api/Api.cpp: In static member function ‘static char* Api::get(const char*, int*)’:
/opt/xmrig/src/api/Api.cpp:53: error: ‘nullptr’ was not declared in this scope
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

# Discussion History
## xmrig | 2018-03-13T15:42:08+00:00
You must use C++11, actual error is:
`error: ‘nullptr’ was not declared in this scope`
Thank you.

# Action History
- Created by: minzak | 2018-03-13T15:34:56+00:00
- Closed at: 2018-03-16T17:47:01+00:00
