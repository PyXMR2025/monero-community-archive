---
title: emmintrin.h not found
source_url: https://github.com/xmrig/xmrig/issues/168
author: ghost
assignees: []
labels:
- arm
created_at: '2017-10-23T23:04:05+00:00'
updated_at: '2017-11-27T00:32:39+00:00'
type: issue
status: closed
closed_at: '2017-10-24T07:49:53+00:00'
---

# Original Description
pi@ELR-RPI3B:~/Downloads/xmrig/build $ cmake ..
-- The C compiler identification is GNU 4.9.2
-- The CXX compiler identification is GNU 4.9.2
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
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.so  
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found mhd: /usr/include  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/Downloads/xmrig/build
pi@ELR-RPI3B:~/Downloads/xmrig/build $ make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  4%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  6%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  8%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[ 10%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 12%] Linking C static library libcpuid.a
[ 12%] Built target cpuid
Scanning dependencies of target xmrig
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
In file included from /home/pi/Downloads/xmrig/src/3rdparty/rapidjson/document.h:20:0,
                 from /home/pi/Downloads/xmrig/src/api/ApiState.cpp:41:
/home/pi/Downloads/xmrig/src/3rdparty/rapidjson/reader.h:35:23: fatal error: emmintrin.h: No existe el fichero o el directorio
 #include <emmintrin.h>
                       ^
compilation terminated.
CMakeFiles/xmrig.dir/build.make:86: recipe for target 'CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


# Discussion History
## xmrig | 2017-10-24T07:49:53+00:00
ARM not supported #94 

## ghost | 2017-10-24T17:03:58+00:00
You only need edit some words.

## xmrig | 2017-11-27T00:32:39+00:00
ARMv7 support recently added.
Thank you.

# Action History
- Created by: ghost | 2017-10-23T23:04:05+00:00
- Closed at: 2017-10-24T07:49:53+00:00
