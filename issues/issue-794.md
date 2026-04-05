---
title: 'xmrig-2.8.1 compile failed on Centos 6.8 '
source_url: https://github.com/xmrig/xmrig/issues/794
author: PyroPhenom
assignees: []
labels:
- libuv
created_at: '2018-10-13T07:05:12+00:00'
updated_at: '2018-10-14T09:54:12+00:00'
type: issue
status: closed
closed_at: '2018-10-14T09:54:12+00:00'
---

# Original Description
CentOS 6 cannot run the latest programs, so I try to compile programs on centos6.8.
I have manually upgraded GCC to 4.9.4 version, but the following errors have occurred.

[root@localhost build]# make
Scanning dependencies of target xmrig-asm
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cnv2_main_loop.S.o
Linking C static library libxmrig-asm.a
[  1%] Built target xmrig-asm
Scanning dependencies of target cpuid
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 11%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
In file included from /tmp/xmrig/src/workers/Workers.h:34:0,
                 from /tmp/xmrig/src/App.cpp:42:
/tmp/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/tmp/xmrig/src/net/JobResult.h:52:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
/tmp/xmrig/src/App.cpp: In member function ‘int App::exec()’:
/tmp/xmrig/src/App.cpp:131:36: error: ‘uv_loop_close’ was not declared in this scope
     uv_loop_close(uv_default_loop());
                                    ^
At global scope:
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess"
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

# Discussion History
## gxk001 | 2018-10-13T08:35:52+00:00
libuv version ?
rhel6u6 ,  with gcc-4.9.4/libuv1.22.0, works fine

## xmrig | 2018-10-13T08:57:17+00:00
libuv should be v1.0+ not v0.10.
Thank you.

# Action History
- Created by: PyroPhenom | 2018-10-13T07:05:12+00:00
- Closed at: 2018-10-14T09:54:12+00:00
