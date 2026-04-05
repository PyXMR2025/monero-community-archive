---
title: ARM Compilation
source_url: https://github.com/xmrig/xmrig/issues/94
author: atarate
assignees: []
labels:
- enhancement
- arm
created_at: '2017-09-06T21:24:33+00:00'
updated_at: '2017-11-27T00:33:44+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:33:43+00:00'
---

# Original Description
Facing the below error while compiling on ARMV8

[ 94%] Building C object CMakeFiles/xmrig.dir/src/crypto/soft_aes.c.o
In file included from /root/xmrig/src/crypto/soft_aes.c:29:
In file included from /usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/x86intrin.h:29:
In file included from /usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/immintrin.h:28:
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:64:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_vec_init_v2si(__i, 0);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:143:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_packsswb((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:173:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_packssdw((__v2si)__m1, (__v2si)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:203:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_packuswb((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:230:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_punpckhbw((__v8qi)__m1, (__v8qi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:253:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_punpckhwd((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:274:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_punpckhdq((__v2si)__m1, (__v2si)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:301:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_punpcklbw((__v8qi)__m1, (__v8qi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:324:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_punpcklwd((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:345:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_punpckldq((__v2si)__m1, (__v2si)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:366:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_paddb((__v8qi)__m1, (__v8qi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:387:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_paddw((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:408:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_paddd((__v2si)__m1, (__v2si)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:430:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_paddsb((__v8qi)__m1, (__v8qi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:453:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_paddsw((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:475:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_paddusb((__v8qi)__m1, (__v8qi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:497:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_paddusw((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:518:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_psubb((__v8qi)__m1, (__v8qi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/lib/llvm-4.0/bin/../lib/clang/4.0.0/include/mmintrin.h:539:12: error: 
      invalid conversion between vector type '__m64' (vector of 1 'long long'
      value) and integer type 'int' of different size
    return (__m64)__builtin_ia32_psubw((__v4hi)__m1, (__v4hi)__m2);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated.
CMakeFiles/xmrig.dir/build.make:830: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/soft_aes.c.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/soft_aes.c.o] Error 1
CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

seems to be an issue with immintrin.h interfacing with your code. Whaddya think may be the issue?

# Discussion History
## xmrig | 2017-09-07T04:11:03+00:00
ARM not supported and it not just header issue, there actively used x86/x64 specific SSE2 and AES-NI instructions. 

## atarate | 2017-09-07T20:48:17+00:00
Okay.... After recompiling and debugging for ARM, I am beginning to see the specific SSE2 and AES instruction set.
the _mm_aeskeygenassist,  is one of the major functions without which the AES functions are pretty much useless. 
I can now see now why porting AES instruction sets to ARM is going to be a pain in the arse.

## atarate | 2017-09-08T09:21:44+00:00
is there a document that I can refer to the intrinsic  for ARM64? neon doesnt help much

## calvintam236 | 2017-10-15T03:15:06+00:00
Actually, I think `cpuminer-multi` have limited support for ARM instructions. Maybe it is worth to take a look at its [source code](https://github.com/lucasjones/cpuminer-multi)?

## calvintam236 | 2017-10-17T06:36:16+00:00
It said to be support Android (ARM). Click [here](https://www.reddit.com/r/Monero/comments/6avezv/wolfxmrminer_ported_to_android_with_openclgpu/) for more info.

## xmrig | 2017-11-06T00:35:20+00:00
ARM support added in [arm](https://github.com/xmrig/xmrig/tree/arm) branch, commit https://github.com/xmrig/xmrig/commit/6cc152e26fe438b23a522caf28670817906d761b.

* First working prototype I received via email from user https://github.com/imranyusuff many thanks.
* Build tested on Ubuntu 16.04, both gcc and clang compiler supported.
* Only ARMv8 (aarch64) tested, hardware and software AES supported.
* [sse2neon](https://github.com/jratcliff63367/sse2neon) used to translate SSE2  intrinsics to NEON ones.
* All ARM crypto code located in separated file [CryptoNight_arm.h](https://github.com/xmrig/xmrig/blob/arm/src/crypto/CryptoNight_arm.h)

Known issues:
 * No CPU information detected, probably good candidate to use https://github.com/Maratyszcza/cpuinfo
 * I get bad hashrate with hardware aes and huge pages, use `--no-huge-pages` option.

## layalered | 2017-11-06T03:19:51+00:00
Please help me how to create exe On the Visual Studio 2017 C ++ 

## leeroyjkins | 2017-11-13T16:28:05+00:00
@xmrig I'm having trouble cross compiling. 
I just added another .cmake file with:
```SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_PROCESSOR aarch64)

SET(CMAKE_C_COMPILER /usr/bin/arm-linux-gnueabi-gcc)
SET(CMAKE_CXX_COMPILER /usr/bin/arm-linux-gnueabi-g++)
SET(CMAKE_FIND_ROOT_PATH /usr/arm-linux-gnueabi)
```
steps:
mkdir build
cd build
cmake -DCMAKE_TOOLCHAIN_FILE=../cmake/arm.cmake ..
make

## leeroyjkins | 2017-11-13T16:28:23+00:00
any tips how to cross compile on Ubuntu 16.04 ?


## xmrig | 2017-11-14T08:45:37+00:00
Actually I don't know how to make cross compile for ARM. I used native ARM Ubuntu for it https://www.scaleway.com/armv8-cloud-servers/ ARM64-2GB instance.
Thank you.

## gennadicho | 2017-11-19T00:11:16+00:00
very nice working! best miner for ARM, ha-ha :) I got 20 h/s on my arm64 wileyfox spark, for example tpruvot cpuminer got me only 9h/s 

# Action History
- Created by: atarate | 2017-09-06T21:24:33+00:00
- Closed at: 2017-11-27T00:33:43+00:00
