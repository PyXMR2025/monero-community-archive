---
title: Repeated failures to compile ARM & cannot disable Argon2
source_url: https://github.com/xmrig/xmrig/issues/3413
author: I2pRandom
assignees: []
labels: []
created_at: '2024-01-28T23:37:41+00:00'
updated_at: '2025-06-18T22:17:12+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:17:12+00:00'
---

# Original Description
**Describe the bug**
Tried to compile ARM, and installed multiple AUR packages looking for -mfpu=neon
Began disabling Algo's due to failure to missing toolchains. 
XMRig refuses to compile without Agron2

**To Reproduce**

mkdir xmrig/build && cd xmrig/scripts

> ./build_deps.sh && cd ../build
cmake -DBUILD_STATIC=ON -DARM_TARGET=7 -DWITH_TLS=OFF -DWITH_OPENCL=OFF DWITH_CUDA=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_CN_FEMTO=OFF -DWITH_ARGON2=OFF -DWITH_KAWPOW=OFF -DWITH_GHOSTRIDER=OFF ..
make -j$(nproc)

**Expected behavior**
Compilation for ARMv7 completes without critical error.

**Required data**
 - OS: ArchLinux (synced to latest Packages.

**Additional context**
<details><summary>Details</summary>
<p>

  MonkeySex% cmake -DBUILD_STATIC=ON -DARM_TARGET=7 -DWITH_TLS=OFF -DWITH_OPENCL=OFF DWITH_CUDA=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DWITH_CN_FEMTO=OFF -DWITH_ARGON2=OFF -DWITH_KAWPOW=OFF -DWITH_GHOSTRIDER=OFF ..
CMake Warning:
  Ignoring extra path from command line:

   "/home/jasonpanic/xmrig/build/DWITH_CUDA=OFF"


CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 13.2.1
-- The CXX compiler identification is GNU 13.2.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Success
-- Use ARM_TARGET=7 (x86_64)
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/libhwloc.so
CMake Warning at src/backend/cuda/cuda.cmake:2 (message):
  CUDA backend is not compatible with static build, use -DWITH_CUDA=OFF to
  suppress this warning
Call Stack (most recent call first):
  src/backend/backend.cmake:3 (include)
  CMakeLists.txt:49 (include)


-- Found UV: /usr/lib/libuv.so
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
CMake Deprecation Warning at src/3rdparty/argon2/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Configuring done (0.7s)
-- Generating done (0.0s)
-- Build files have been written to: /home/jasonpanic/xmrig/build
MonkeySex% make -j$(nproc)
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
cc: error: unrecognized command-line option ‘-mfpu=neon’
cc: error: unrecognized command-line option ‘-mfpu=neon’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:146: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:90: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o] Error 1
cc: error: unrecognized command-line option ‘-mfpu=neon’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:76: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1
cc: error: unrecognized command-line option ‘-mfpu=neon’
cc: error: unrecognized command-line option ‘-mfpu=neon’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:118: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o] Error 1
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:132: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o] Error 1
cc: error: unrecognized command-line option ‘-mfpu=neon’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:160: src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o] Error 1
cc: error: unrecognized command-line option ‘-mfpu=neon’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:104: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:126: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
MonkeySex%


</p>
</details>

# Discussion History
# Action History
- Created by: I2pRandom | 2024-01-28T23:37:41+00:00
- Closed at: 2025-06-18T22:17:12+00:00
