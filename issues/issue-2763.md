---
title: can't get it working
source_url: https://github.com/xmrig/xmrig/issues/2763
author: IRONPOOL91
assignees: []
labels: []
created_at: '2021-11-30T16:06:56+00:00'
updated_at: '2021-12-04T12:33:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj5EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x14): more undefined references to `__atomic_load_8' follow
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3048: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:115: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2

# Discussion History
## Spudz76 | 2021-11-30T16:22:46+00:00
What compiler and version

## razvanwir | 2021-12-04T12:33:10+00:00
hello [  1%] Built target ethash
[  2%] Building CXX object src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o
In file included from /home/pi/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:
/home/pi/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  122 | #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
      |  ^~~~~
In file included from /home/pi/xmrig/src/crypto/ghostrider/ghostrider.cpp:57:
/home/pi/xmrig/src/crypto/ghostrider/../../crypto/cn/sse2neon.h:7594:9: warning: ‘#pragma GCC pop_options’ without a corresponding ‘#pragma GCC push_options’ [-Wpragmas]
 7594 | #pragma GCC pop_options
      |         ^~~
make[2]: *** [src/crypto/ghostrider/CMakeFiles/ghostrider.dir/build.make:290: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/ghostrider.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:240: src/crypto/ghostrider/CMakeFiles/ghostrider.dir/all] Error 2
 i have this problem help me.

# Action History
- Created by: IRONPOOL91 | 2021-11-30T16:06:56+00:00
