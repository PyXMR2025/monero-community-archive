---
title: Don't compile on RPI3
source_url: https://github.com/xmrig/xmrig/issues/166
author: ghost
assignees: []
labels:
- arm
created_at: '2017-10-23T22:50:34+00:00'
updated_at: '2017-11-27T00:31:56+00:00'
type: issue
status: closed
closed_at: '2017-10-24T07:50:15+00:00'
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
-- Looking for syslog.h - not found
-- Found mhd: /usr/include  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/Downloads/xmrig/build
pi@ELR-RPI3B:~/Downloads/xmrig/build $ make
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc: error: unrecognized command line option '-maes'
src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make:62: recipe for target 'src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o' failed
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
CMakeFiles/Makefile2:122: recipe for target 'src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all' failed
make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


# Discussion History
## ghost | 2017-10-23T22:52:35+00:00
The same error https://github.com/monero-project/monero/issues/954

You need to remove the -maes flag when compiling on ARM, that flag is x86-specific.

## xmrig | 2017-10-24T07:50:15+00:00
ARM not supported #94 

## dunklesToast | 2017-10-27T09:22:29+00:00
It also makes no sense to mine on a Pi - you would get about 1$ per Year which is much more than the Price of the Pi and the Power Consumption Costs

## xmrig | 2017-11-27T00:31:56+00:00
ARMv7 support recently added.
Thank you.

# Action History
- Created by: ghost | 2017-10-23T22:50:34+00:00
- Closed at: 2017-10-24T07:50:15+00:00
