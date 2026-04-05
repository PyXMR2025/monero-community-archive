---
title: Compiling errors at Raspberry pi 3 B+ with Raspbian
source_url: https://github.com/xmrig/xmrig/issues/1116
author: pyro7777777
assignees: []
labels:
- arm
created_at: '2019-08-15T19:25:51+00:00'
updated_at: '2021-04-12T15:55:03+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:55:03+00:00'
---

# Original Description
When i do make this is the result:
[100%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: en la función `xmrig::Nonce::Nonce()':
Nonce.cpp:(.text+0x38): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x4c): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x60): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: en la función `xmrig::Nonce::reset(unsigned char)':
Nonce.cpp:(.text+0x174): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x188): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x19c): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: en la función `xmrig::Nonce::stop()':
Nonce.cpp:(.text+0x204): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x218): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x22c): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: en la función `xmrig::Nonce::touch()':
Nonce.cpp:(.text+0x260): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x274): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: Nonce.cpp:(.text+0x288): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: en la función `xmrig::Worker::storeStats()':
Worker.cpp:(.text+0x90): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Worker.cpp:(.text+0xbc): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: en la función `xmrig::Worker::timestamp() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: en la función `xmrig::Worker::hashCount() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): referencia a `__atomic_store_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x94): referencia a `__atomic_fetch_add_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: en la función `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x4c): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x70): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x6c): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<1u>::consumeJob()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x20): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: en la función `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x6c): referencia a `__atomic_load_8' sin definir
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj2EE10consumeJobEv]+0x20): más referencias a `__atomic_load_8' sin definir a continuación
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1678: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

the result of CMAKE:
 $ sudo cmake .. -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7
-- The C compiler identification is GNU 7.3.0
-- The CXX compiler identification is GNU 7.3.0
-- Check for working C compiler: /usr/bin/gcc-7
-- Check for working C compiler: /usr/bin/gcc-7 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/g++-7
-- Check for working CXX compiler: /usr/bin/g++-7 -- works
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
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.1c")
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/BTN/xmrig/build

i dont know if its ARM_TARGET.. my raspberry have armv8a but cmake compiling to armv7l

# Discussion History
## xmrig | 2019-08-15T19:29:42+00:00
About atomic bug #1102

`armv8a` only available if use 64-bit OS.
Thank you.

## pyro7777777 | 2019-08-15T20:23:19+00:00
Wich OS can u recommend for use in RPi3B+ with xmrig?


## grahamreeds | 2020-06-02T09:18:57+00:00
If you are still looking then there is a new Raspberry Pi OS (https://www.raspberrypi.org/forums/viewtopic.php?f=117&t=275370).  I can can compile and run, with no modifications, XMRig and get 9.9H/s on stock.  I expect about 11H/s with a stable overclock.

# Action History
- Created by: pyro7777777 | 2019-08-15T19:25:51+00:00
- Closed at: 2021-04-12T15:55:03+00:00
