---
title: 'XMRig fails to compile on Asus Tinker board '
source_url: https://github.com/xmrig/xmrig/issues/1955
author: FerrahWolfeh
assignees: []
labels: []
created_at: '2020-11-24T21:49:06+00:00'
updated_at: '2021-04-12T14:33:47+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:33:47+00:00'
---

# Original Description
**Describe the bug**
Xmrig does not build on armbian with arm 7 cpu

**To Reproduce**
Install armbian on a arm 7 SBC, try to compile xmrig

**Expected behavior**
It should just compile everything ok without spamming errors when compiling cryptonight

**Required data**
OS- Armbian 20.04 bionic Rockchip
GCC - 7.5.0
CMake 3.8.0
CPU - Rockchip RK3288

When compiling xmrig, at about 80-90ish% it spams this error many times and then halts the compilation
`/dev/shm/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);                                                                     ~~~~~~~~~~~~~~~~^~~~~~~~~~
/dev/shm/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~`
**Additional context**
This error also occurs on my raspi 4


# Discussion History
## SChernykh | 2020-11-24T23:24:35+00:00
32-bit ARM compilation is not supported, make sure you're compiling for 64-bit (ARMv8-a).

## FerrahWolfeh | 2020-11-24T23:50:55+00:00
Still not working
Compiling xmrig on raspbian with 64bit kernel, cmake and make flags for 64 bit architecture still give the same error at the same point

## FerrahWolfeh | 2020-11-24T23:55:09+00:00
Here's the cmake output
`-- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0                                                 -- Check for working C compiler: /usr/bin/cc                                                    -- Check for working C compiler: /usr/bin/cc -- works                                           -- Detecting C compiler ABI info                                                                -- Detecting C compiler ABI info - done                                                         -- Detecting C compile features                                                                 -- Detecting C compile features - done                                                          -- Check for working CXX compiler: /usr/bin/c++                                                 -- Check for working CXX compiler: /usr/bin/c++ -- works                                        -- Detecting CXX compiler ABI info                                                              -- Detecting CXX compiler ABI info - done                                                       -- Detecting CXX compile features
-- Detecting CXX compile features - done                                                        -- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found                                                                 -- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so                                        -- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a                                               -- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found                                                  -- WITH_MSR=OFF                                                                                 -- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.1d")            -- Configuring done                                                                             -- Generating done
-- Build files have been written to: /dev/shm/xmrig/build`

And this is the make command I used
`make -j 4 CFLAGS='-march=native -mtune=native -O3' CXXFLAGS='-march=native -mtune=native -O3'`

Also the output of lscpu
`Architecture:        aarch64                                                                    Byte Order:          Little Endian                                                              CPU(s):              4
On-line CPU(s) list: 0-3                                                                        Thread(s) per core:  1                                                                          Core(s) per socket:  4                                                                          Socket(s):           1                                                                          Vendor ID:           ARM
Model:               3
Model name:          Cortex-A72                                                                 Stepping:            r0p3                                                                       CPU max MHz:         2100,0000                                                                  CPU min MHz:         600,0000                                                                   BogoMIPS:            108.00
Flags:               fp asimd evtstrm crc32 cpuid`

## SChernykh | 2020-11-25T07:05:49+00:00
You shouldn't overwrite CFLAGS/CXXFLAGS in your command line, this is why you get errors with `_mm_aesenc_si128`

# Action History
- Created by: FerrahWolfeh | 2020-11-24T21:49:06+00:00
- Closed at: 2021-04-12T14:33:47+00:00
