---
title: Cannot build on Raspberry Pi 3 (Raspbian OS 10)
source_url: https://github.com/xmrig/xmrig/issues/2550
author: Zenitur
assignees: []
labels:
- bug
- arm
created_at: '2021-08-21T10:29:16+00:00'
updated_at: '2025-06-16T20:01:38+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:01:38+00:00'
---

# Original Description
```
cd ~
mv ~/Downloads/xmrig-6.14.1.tar.gz .
tar xf xmrig-6.14.1.tar.gz
cd xmrig-6.14.1
mkdir build && cd build
cmake ..
```
```
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
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.1d")  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/xmrig-6.14.1/build
```
```
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
In file included from /home/pi/xmrig-6.14.1/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/xmrig-6.14.1/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/pi/xmrig-6.14.1/src/crypto/cn/CnHash.cpp:27:
/home/pi/xmrig-6.14.1/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
 #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  ^~~~~
```
I had retried with the `-O2 -march=armv8-a+crc -mtune=cortex-a53 -mfpu=neon-fp-armv8 -mfloat-abi=hard -funsafe-math-optimizations` params but I had got the same thing.

# Discussion History
## Zenitur | 2021-08-22T09:36:15+00:00
I remove the block of code with the checking. Now it compiles.
```
 * ABOUT        XMRig/6.14.1 gcc/8.3.0
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1d hwloc/1.11.12
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A53 (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.6/0.9 GB (69%)
 * DONATE       1%
 * POOL #1      stratum+tcp://xmr.pool.minergate.com:45700 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled (selected OpenCL platform NOT found)
 * CUDA         disabled
```

## novazz | 2021-09-16T15:34:08+00:00
how is your speed on ARM Cortex-A53 32bit

## Spudz76 | 2021-09-17T00:28:34+00:00
What does `g++ -dM -E -x c++ - < /dev/null | grep -i arm` say on that Raspbian compiler/toolchain?

`__arm__` and `__ARM_ARCH` must be there or the logic needs an update, but I need your compiler predefines to figure out how to detect it correctly.


## Zenitur | 2021-09-18T08:22:28+00:00
**Spudz76** I ran it twice. First time I ran it without additional CXXFLAGS, hovewer in second time I tried it with them.

```
$ g++ -dM -E -x c++ - < /dev/null | grep -i arm
#define __ARM_SIZEOF_WCHAR_T 4
#define __ARM_FEATURE_SAT 1
#define __ARM_ARCH_ISA_ARM 1
#define __ARMEL__ 1
#define __ARM_FEATURE_UNALIGNED 1
#define __ARM_FP 12
#define __ARM_SIZEOF_MINIMAL_ENUM 4
#define __ARM_PCS_VFP 1
#define __ARM_FEATURE_LDREX 4
#define __ARM_FEATURE_QBIT 1
#define __ARM_ARCH_6__ 1
#define __ARM_32BIT_STATE 1
#define __ARM_FEATURE_CLZ 1
#define __ARM_ARCH_ISA_THUMB 1
#define __ARM_ARCH 6
#define __arm__ 1
#define __ARM_FEATURE_SIMD32 1
#define __ARM_FEATURE_COPROC 15
#define __ARM_EABI__ 1
#define __ARM_FEATURE_DSP 1
```

```
$ g++ -dM -E -x c++ -O2 -march=armv8-a+crc -mtune=cortex-a53 -mfpu=neon-fp-armv8 -mfloat-abi=hard -funsafe-math-optimizations - < /dev/null | grep -i arm
#define __ARM_SIZEOF_WCHAR_T 4
#define __ARM_FEATURE_SAT 1
#define __ARM_ARCH_ISA_ARM 1
#define __ARMEL__ 1
#define __ARM_FEATURE_UNALIGNED 1
#define __ARM_FEATURE_IDIV 1
#define __ARM_FP 14
#define __ARM_ARCH_8A__ 1
#define __ARM_NEON_FP 6
#define __ARM_SIZEOF_MINIMAL_ENUM 4
#define __ARM_PCS_VFP 1
#define __ARM_FEATURE_LDREX 15
#define __ARM_FEATURE_QBIT 1
#define __ARM_FEATURE_FMA 1
#define __ARM_NEON__ 1
#define __ARM_ARCH_PROFILE 65
#define __ARM_32BIT_STATE 1
#define __ARM_FEATURE_CLZ 1
#define __ARM_ARCH_ISA_THUMB 2
#define __ARM_ARCH 8
#define __arm__ 1
#define __ARM_FEATURE_SIMD32 1
#define __ARM_FEATURE_CRC32 1
#define __ARM_NEON 1
#define __ARM_FEATURE_NUMERIC_MAXMIN 1
#define __ARM_ARCH_EXT_IDIV__ 1
#define __ARM_EABI__ 1
#define __ARM_FEATURE_DSP 1
```

## Zenitur | 2021-09-18T08:24:11+00:00
> how is your speed on ARM Cortex-A53 32bit

I tried RandomX algo only. It cannot run. My target was OpenCL on Pi, and it also did't run.

## Spudz76 | 2021-09-18T11:34:34+00:00
How about with `-march=native`?

## Zenitur | 2021-09-23T10:36:26+00:00
> How about with `-march=native`?

I'm sorry for the delay.

```
$ g++ -dM -E -x c++ -march=native - < /dev/null | grep -i arm
#define __ARM_SIZEOF_WCHAR_T 4
#define __ARM_FEATURE_SAT 1
#define __ARM_ARCH_ISA_ARM 1
#define __ARMEL__ 1
#define __ARM_FEATURE_UNALIGNED 1
#define __ARM_FEATURE_IDIV 1
#define __ARM_FP 12
#define __ARM_ARCH_8A__ 1
#define __ARM_SIZEOF_MINIMAL_ENUM 4
#define __ARM_PCS_VFP 1
#define __ARM_FEATURE_LDREX 15
#define __ARM_FEATURE_QBIT 1
#define __ARM_ARCH_PROFILE 65
#define __ARM_32BIT_STATE 1
#define __ARM_FEATURE_CLZ 1
#define __ARM_ARCH_ISA_THUMB 2
#define __ARM_ARCH 8
#define __arm__ 1
#define __ARM_FEATURE_SIMD32 1
#define __ARM_FEATURE_CRC32 1
#define __ARM_ARCH_EXT_IDIV__ 1
#define __ARM_EABI__ 1
#define __ARM_FEATURE_DSP 1
```

## benthetechguy | 2022-01-26T00:11:27+00:00
fixed in #2898

## Apetree100122 | 2024-01-02T12:39:16+00:00
cd ~
mv ~/Downloads
/xmrig-6.14.1.tar.gz .tar 
xf xmrig-6.14.1.tar.gz
cd- xmrig-
6.14.1
mkdir - 
build-
 && cd -build
cmake -
- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -
- works
-- Detecting C compiler ABI info
-
- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-
- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=7 (armv7l)
- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so  
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF-- Found OpenSSL: /usr/lib/
arm-linux-gnueabihf/libcrypto.so (
found version "1.1.1d")  
- Configuring done

-- Generating done
-- Build files have been written to: /home/pi/xmrig-6.14.1/build

# Action History
- Created by: Zenitur | 2021-08-21T10:29:16+00:00
- Closed at: 2025-06-16T20:01:38+00:00
