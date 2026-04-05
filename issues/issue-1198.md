---
title: error when building
source_url: https://github.com/xmrig/xmrig/issues/1198
author: tar-xz
assignees: []
labels:
- question
- libuv
created_at: '2019-09-27T10:42:00+00:00'
updated_at: '2019-09-27T11:06:50+00:00'
type: issue
status: closed
closed_at: '2019-09-27T11:06:50+00:00'
---

# Original Description
system: ubuntu
xmrig ver.: 2.14.4

`root@ip-172-31-29-147:~/xmrig-2.14.4/build# cmake .. -DWITH_HTTPD=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig-2.14.4/build
root@ip-172-31-29-147:~/xmrig-2.14.4/build# make
Scanning dependencies of target cpuid
[  1%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
Linking C static library libcpuid.a
[  7%] Built target cpuid
Scanning dependencies of target xmrig-asm
[  9%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/cn_main_loop.S.o
[ 10%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/asm/CryptonightR_template.S.o
Linking C static library libxmrig-asm.a
[ 10%] Built target xmrig-asm
Scanning dependencies of target xmrig
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
In file included from /root/xmrig-2.14.4/src/workers/Workers.h:35:0,
                 from /root/xmrig-2.14.4/src/App.cpp:45:
/root/xmrig-2.14.4/src/net/JobResult.h: In member function ‘uint64_t xmrig::JobResult::actualDiff() const’:
/root/xmrig-2.14.4/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
/root/xmrig-2.14.4/src/App.cpp: In member function ‘int xmrig::App::exec()’:
/root/xmrig-2.14.4/src/App.cpp:123:36: error: ‘uv_loop_close’ was not declared in this scope
     uv_loop_close(uv_default_loop());
                                    ^
At global scope:
cc1plus: warning: unrecognized command line option "-Wno-class-memaccess" [enabled by default]
make[2]: *** [CMakeFiles/xmrig.dir/src/App.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2`

# Discussion History
## xmrig | 2019-09-27T10:56:50+00:00
libuv 0.10.xx not supported, you should use libuv 1+.
Thank you.

## tar-xz | 2019-09-27T11:06:47+00:00
thxxx~

# Action History
- Created by: tar-xz | 2019-09-27T10:42:00+00:00
- Closed at: 2019-09-27T11:06:50+00:00
