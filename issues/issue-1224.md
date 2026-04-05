---
title: Compiling Issues - Raspberry Pi 4 - Raspbian
source_url: https://github.com/xmrig/xmrig/issues/1224
author: tgwaste
assignees: []
labels: []
created_at: '2019-10-07T07:58:22+00:00'
updated_at: '2023-05-29T22:30:02+00:00'
type: issue
status: closed
closed_at: '2019-10-07T17:34:11+00:00'
---

# Original Description
```
# cmake ..
-- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=7 (armv7l)
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.1d")
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/local/bin/xmrig/build

```
```
[  6%] Built target argon2
[  7%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::Nonce()':
Nonce.cpp:(.text+0x38): undefined reference to `__atomic_store_8'
/usr/bin/ld: Nonce.cpp:(.text+0x4c): undefined reference to `__atomic_store_8'
/usr/bin/ld: Nonce.cpp:(.text+0x60): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::stop()':
Nonce.cpp:(.text+0x184): undefined reference to `__atomic_store_8'
/usr/bin/ld: Nonce.cpp:(.text+0x198): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o:Nonce.cpp:(.text+0x1ac): more undefined references to `__atomic_store_8' follow
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::touch()':
Nonce.cpp:(.text+0x1e0): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: Nonce.cpp:(.text+0x1f4): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: Nonce.cpp:(.text+0x208): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::storeStats()':
Worker.cpp:(.text+0x90): undefined reference to `__atomic_store_8'
/usr/bin/ld: Worker.cpp:(.text+0xbc): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::timestamp() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::hashCount() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x4c): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::consumeJob()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x20): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj2EE10consumeJobEv]+0x20): more undefined references to `__atomic_load_8' follow
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1709: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

# Discussion History
## tgwaste | 2019-10-07T17:34:09+00:00
Fixed this by adding the following to CMakeLists.txt:

```
set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")
```

IE:

```
cmake_minimum_required(VERSION 2.8)
project(xmrig)

option(WITH_LIBCPUID        "Enable libcpuid support" ON)
option(WITH_HWLOC           "Enable hwloc support" ON)
option(WITH_CN_LITE         "Enable CryptoNight-Lite algorithms family" ON)
option(WITH_CN_HEAVY        "Enable CryptoNight-Heavy algorithms family" ON)
option(WITH_CN_PICO         "Enable CryptoNight-Pico algorithm" ON)
option(WITH_CN_GPU          "Enable CryptoNight-GPU algorithm" ON)
option(WITH_RANDOMX         "Enable RandomX algorithms family" ON)
option(WITH_ARGON2          "Enable Argon2 algorithms family" ON)
option(WITH_HTTP            "Enable HTTP protocol support (client/server)" ON)
option(WITH_DEBUG_LOG       "Enable debug log output" OFF)
option(WITH_TLS             "Enable OpenSSL support" ON)
option(WITH_ASM             "Enable ASM PoW implementations" ON)
option(WITH_EMBEDDED_CONFIG "Enable internal embedded JSON config" OFF)

option(BUILD_STATIC         "Build static binary" OFF)
option(ARM_TARGET           "Force use specific ARM target 8 or 7" 0)
option(HWLOC_DEBUG          "Enable hwloc debug helpers and log" OFF)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")
set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")    <-------------

include (CheckIncludeFile)
include (cmake/cpu.cmake)
include (src/base/base.cmake)
include (src/backend/backend.cmake)
```

## pragathoys | 2020-05-12T05:27:15+00:00
> Fixed this by adding the following to CMakeLists.txt:
> 
> ```
> set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")
> ```
> 

> ```

thank you @tgwaste !
This help me to build it for an RPi 2 ( armv7l )

## razvanwir | 2021-12-04T12:10:09+00:00

i tried with with that  command set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic") and set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")  and after tryed compile the console show/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: in function `Workers::onTick(uv_timer_s*)':
Workers.cpp:(.text+0x148): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text+0x174): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: in function `Workers::setEnabled(bool)':
Workers.cpp:(.text+0x5b0): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: in function `Workers::setJob(xmrig::Job const&, bool)':
Workers.cpp:(.text+0x764): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: in function `Workers::stop()':
Workers.cpp:(.text+0x800): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o: in function `Workers::start(xmrig::Controller*)':
Workers.cpp:(.text+0xc98): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/net/Network.cpp.o: in function `xmrig::Network::onPause(xmrig::IStrategy*)':
Network.cpp:(.text+0x43c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/net/Network.cpp.o: in function `non-virtual thunk to xmrig::Network::onPause(xmrig::IStrategy*)':
Network.cpp:(.text+0x928): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: in function `Worker::timestamp() const':
MultiWorker.cpp:(.text._ZNK6Worker9timestampEv[_ZNK6Worker9timestampEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: in function `Worker::hashCount() const':
MultiWorker.cpp:(.text._ZNK6Worker9hashCountEv[_ZNK6Worker9hashCountEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: in function `MultiWorker<1u>::consumeJob()':
MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE10consumeJobEv[_ZN11MultiWorkerILj1EE10consumeJobEv]+0x1c): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o: in function `MultiWorker<1u>::start()':
MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x20): undefined reference to `__atomic_load_8'
/usr/bin/ld: MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0xd0): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o:MultiWorker.cpp:(.text._ZN11MultiWorkerILj1EE5startEv[_ZN11MultiWorkerILj1EE5startEv]+0x220): more undefined references to `__atomic_load_8' follow
/usr/bin/ld: CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o: in function `Worker::storeStats()':
Worker.cpp:(.text+0x158): undefined reference to `__atomic_store_8'
/usr/bin/ld: Worker.cpp:(.text+0x16c): undefined reference to `__atomic_store_8'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:886: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:95: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2


## DiogoCruz40 | 2023-05-29T22:29:42+00:00
@mrrat1337 have you solved the problem? If yes, how?

# Action History
- Created by: tgwaste | 2019-10-07T07:58:22+00:00
- Closed at: 2019-10-07T17:34:11+00:00
