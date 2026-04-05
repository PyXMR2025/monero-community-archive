---
title: Linux PPC64 (Big-Endian) Support
source_url: https://github.com/xmrig/xmrig/issues/2424
author: WMark77
assignees: []
labels: []
created_at: '2021-06-05T19:03:43+00:00'
updated_at: '2025-06-16T20:32:40+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:32:40+00:00'
---

# Original Description
Hello everyone,

Operating System: Debian Bullseye
Architecture: Powerpc64 (ppc64)

I'm aware that PPC64 is not (officialy) supported, but I'd really like to run Xmrig on my IBM POWER7+. I'm trying to compile it from source. 

I did append "set(CMAKE_SYSTEM_NAME Linux) and set(CMAKE_SYSTEM_PROCESSOR powerpc64)" in flags.cmake and cpu.cmake. I also removed "-maes" flags from them.

So I did run:

1) cmake (OK)
2) make (got several errors):

/opt/xmrig/src/crypto/cn/asm/cn_main_loop.S: Assembler messages:
/opt/xmrig/src/crypto/cn/asm/cn_main_loop.S:6: Error: unknown pseudo-op: `.intel_syntax' 
....
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:82: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig-asm.dir/all] Error 2
...

Is there any chance to get Xmrig installed on my machine?
Can you give me a help?


Thank you in advance.

# Discussion History
## SChernykh | 2021-06-05T19:59:15+00:00
Try to add `-DWITH_ASM=OFF` to cmake command line, because `cn_main_loop.S` is intended for x86-64 CPUs.

## WMark77 | 2021-06-05T20:52:37+00:00
> Try to add `-DWITH_ASM=OFF` to cmake command line, because `cn_main_loop.S` is intended for x86-64 CPUs.
Thanks. I'll try that way.

Is there a cmake parameter to get rid of ‘-maes’ error or the only way is removing "set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -maes")" from "cmake/flags.cmake" ? 

Thank you very much.

## WMark77 | 2021-06-05T22:07:39+00:00
I did try the following commands.

1) cmake -DWITH_ASM=OFF  -DCMAKE_SYSTEM_NAME=Linux -DCMAKE_SYSTEM_PROCESSOR=powerpc64  -DWITH_ARGON2=OFF -DWITH_ASTROBWT=OFF -DWITH_KAWPOW=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF .. 
(OK)

2) make -j8 CFLAGS='-mcpu=power7 -mtune=power8' CXXFLAGS='-mcpu=power7 -mtune=power8' :
(FAIL)

Scanning dependencies of target argon2-sse2
...
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
...
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
/opt/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:13: **fatal error**: **cpuid.h**: No such file or directory
   29 | #   include <cpuid.h>
      |             ^~~~~~~~~
compilation terminated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1174: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
....

# Action History
- Created by: WMark77 | 2021-06-05T19:03:43+00:00
- Closed at: 2025-06-16T20:32:40+00:00
