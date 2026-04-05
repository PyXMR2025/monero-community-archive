---
title: It's difficult for me to compile armv7 successfully. Can you help me compile
  a binary file
source_url: https://github.com/xmrig/xmrig/issues/1997
author: darkness-A
assignees: []
labels:
- question
created_at: '2020-12-23T04:59:50+00:00'
updated_at: '2021-01-10T01:10:24+00:00'
type: issue
status: closed
closed_at: '2021-01-10T01:10:24+00:00'
---

# Original Description
`root@usera:~/Desktop/xmrig-master/build# cmake -DARM_TARGET=7 ..
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
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
-- Use ARM_TARGET=7 (x86_64)
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/x86_64-linux-gnu/libhwloc.so  
-- Found UV: /usr/lib/x86_64-linux-gnu/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/x86_64-linux-gnu/libcrypto.so (found version "1.1.1") 
-- Configuring done
-- Generating done
-- Build files have been written to: /root/Desktop/xmrig-master/build
root@crossbug-H410M-T-PRO:~/Desktop/xmrig-master/build# make
Scanning dependencies of target ethash
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
cc: error: unrecognized command line option ‘-mfpu=neon’
src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:62: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o' failed
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
CMakeFiles/Makefile2:178: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/all' failed
make[1]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2`

# Discussion History
## darkness-A | 2020-12-23T10:04:03+00:00
cc: error: unrecognized command line option ‘-mfpu=neon’

## xmrig | 2020-12-23T14:17:46+00:00
ARM without `neon` not supported. Theoretically possible rewrite some old algorithms to work without neon, but no one will do that.
Thank you.

## xmrig | 2020-12-23T14:22:00+00:00
Seems you try to build ARM on x86_64, it is not possible in a direct way also theoretically you can do crosscompile but it is very advanced.
Thank you.


## darkness-A | 2020-12-23T14:24:27+00:00
> 似乎您尝试在x86_64上构建ARM，这不可能直接实现，理论上也可以进行交叉编译，但是它非常先进。
> 谢谢。

Where should I compile？

## xmrig | 2020-12-23T14:25:48+00:00
On real ARM hardware. 

## darkness-A | 2020-12-23T14:33:21+00:00
> 在实际的ARM硬件上。

What electronic devices can be compiled



## darkness-A | 2020-12-23T15:27:12+00:00
> On real ARM hardware.



> On real ARM hardware.

Can you help me compile on armv7



# Action History
- Created by: darkness-A | 2020-12-23T04:59:50+00:00
- Closed at: 2021-01-10T01:10:24+00:00
