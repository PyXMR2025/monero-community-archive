---
title: Errors compiling xmrig on a Rock64 machine
source_url: https://github.com/xmrig/xmrig/issues/1801
author: kofif1
assignees: []
labels:
- arm
created_at: '2020-08-05T23:45:12+00:00'
updated_at: '2021-04-12T14:50:40+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:50:40+00:00'
---

# Original Description
I was unable to install xmrig on a Rock64 machine wit Ubuntu "18.04.4 LTS (Bionic Beaver)"
I downloaded the OS here: https://wiki.pine64.org/index.php/ROCK64_Software_Release#Ubuntu_18.04_Bionic_minimal_64bit_.28arm64.29_Image_.5BmicroSD_.2F_eMMC_Boot.5D_.5B0.8.3.5D


**To Reproduce**
I used the installation instructions on this page to install xmrig.
https://xmrig.com/docs/miner/ubuntu-build

**Expected behavior**
I expected the miner to install. It generated many errors and did not install.

**Required data**
/tmp/ccXAWK3E.s: Assembler messages:
/tmp/ccXAWK3E.s:3390: IT blocks containing 32-bit Thumb instructions are performance deprecated in ARMv8-A and ARMv8-R
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
In file included from /home/rock64/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x0 = _mm_aesenc_si128(*x0, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: note: (if you use ‘-fpermissive’, G++ will accept your code, but allowing the use of an undeclared name is deprecated)
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:175:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:176:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:177:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:178:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:179:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:180:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:181:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i aes_round_tweak_div(const __m128i&, const __m128i&)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:367:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:368:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:18: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
             cx = _mm_aesenc_si128(cx, ax0);
                  ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:19: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:19: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(2) long long int]’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from ‘void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; __m128i = __vector(2) long long int]’
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: ‘_mm_aesenc_si128’ was not declared in this scope
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: ‘_mm_and_si128’
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = true; __m128i = __vector(2) long long int]’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from ‘void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; __m128i = __vector(2) long long int]’
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: ‘_mm_and_si128’
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: At global scope:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true]’ used but never defined
In file included from /home/rock64/xmrig/src/crypto/cn/CryptoNight_monero.h:183:0,
                 from /home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:33,
                 from /home/rock64/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/rock64/xmrig/src/crypto/cn/r/variant4_random_math.h:95:13: warning: ‘void v4_random_math(const V4_Instruction*, v4_reg*) [with v4_reg = unsigned int]’ used but never defined
 static void v4_random_math(const struct V4_Instruction* code, v4_reg* r)
             ^~~~~~~~~~~~~~
In file included from /home/rock64/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true]’ used but never defined
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
CMakeFiles/xmrig.dir/build.make:3926: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


**Additional context**
Any help in getting the miner to work on the Rock64 machine will be appreciated.

Thanks
Ilan


# Discussion History
## SChernykh | 2020-08-07T15:02:44+00:00
Please double check that you're building 64-bit binary. These `_mm_aesenc_si128` errors happen when building for 32-bit ARM. Can you start from the beginning and paste `cmake ..` output?

## kofif1 | 2020-08-07T15:56:41+00:00
This is what I am getting when I am looking for the Linux version:
 lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.4 LTS
Release:	18.04
Codename:	bionic
rock64@rock64:~$ uname -a
Linux rock64 4.4.167-1213-rockchip-ayufan-g34ae07687fce #1 SMP Tue Jun 18 20:44:49 UTC 2019 aarch64 aarch64 aarch64 GNU/Linux

This looks like a 64-bit distribution.
Do you still want me to run the process again? 
Let me know.
Thanks
Ilan


## SChernykh | 2020-08-07T16:32:18+00:00
@kofif1 When you run `cmake ..` it shows you which ARM architecture it builds for in the output. It should be ARMv8-a, not ARMv7-l. Undefined `_mm_aesenc_si128` error can only happen in 32-bit builds, if I read the source code right.

## kofif1 | 2020-08-07T19:01:46+00:00
In the middle of the make command this message appears:
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/ProxyUrl.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Socks5.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
/tmp/ccev6QB0.s: Assembler messages:
/tmp/ccev6QB0.s:8073: IT blocks containing 32-bit Thumb instructions are performance deprecated in ARMv8-A and ARMv8-R
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o

The process continues to 76% of the make and then/tmp/cccE4vPZ.s: Assembler messages:
/tmp/cccE4vPZ.s:3390: IT blocks containing 32-bit Thumb instructions are performance deprecated in ARMv8-A and ARMv8-R
[ 76%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/HugePagesInfo.cpp.o
[ 79%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/MemoryPool.cpp.o
In file included from /home/rock64/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x0 = _mm_aesenc_si128(*x0, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: note: (if you use ‘-fpermissive’, G++ will accept your code, but allowing the use of an undeclared name is deprecated)
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:175:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:176:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:177:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:178:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:179:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:180:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:181:15: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i aes_round_tweak_div(const __m128i&, const __m128i&)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:367:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:368:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:18: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
             cx = _mm_aesenc_si128(cx, ax0);
                  ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:19: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:19: error: there are no arguments to ‘_mm_aesenc_si128’ that depend on a template parameter, so a declaration of ‘_mm_aesenc_si128’ must be available [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ^~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/NUMAMemoryPool.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: ‘_mm_and_si128’
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: ‘_mm_and_si128’
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_hwloc.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(2) long long int]’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from ‘void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; __m128i = __vector(2) long long int]’
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: ‘_mm_aesenc_si128’ was not declared in this scope
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: ‘_mm_and_si128’
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = true; __m128i = __vector(2) long long int]’:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from ‘void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; __m128i = __vector(2) long long int]’
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’
/home/rock64/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: ‘_mm_aesenc_si128’ was not declared in this scope
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: ‘_mm_and_si128’
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: ‘_mm_aesenc_si128’ declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h: At global scope:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true]’ used but never defined
In file included from /home/rock64/xmrig/src/crypto/cn/CryptoNight_monero.h:183:0,
                 from /home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:33,
                 from /home/rock64/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/rock64/xmrig/src/crypto/cn/r/variant4_random_math.h:95:13: warning: ‘void v4_random_math(const V4_Instruction*, v4_reg*) [with v4_reg = unsigned int]’ used but never defined
 static void v4_random_math(const struct V4_Instruction* code, v4_reg* r)
             ^~~~~~~~~~~~~~
In file included from /home/rock64/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true]’ used but never defined
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: ‘void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17]’ used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false]’ used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/rock64/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true]’ used but never defined
cc1plus: warning: unrecognized command line option ‘-Wno-class-memaccess’
CMakeFiles/xmrig.dir/build.make:3926: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2 these errors appear:

That's where the process terminates. 
What do you think?
Ilan


## SChernykh | 2020-08-08T09:01:03+00:00
I repeat:  Can you start from the beginning and paste `cmake ..` output? These errors happen when building for 32-bit ARM.

## kofif1 | 2020-08-08T18:47:09+00:00
Of course.
I started the process again.
Here is the output from the cmake command
rock64@rock64:~/xmrig/build$ cmake ..
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
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Failed
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so  
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.1") 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/rock64/xmrig/build

Let me know what you think and thanks for having the patience to help me.
Best
Ilan

## SChernykh | 2020-08-08T19:40:08+00:00
I've checked the latest code and it compiles fine on my Android phone and on my RPi3b+. I don't have any other ARM devices to test with. You probably need to try newer compiler - I have GCC 8.3.0 on RPi3b+ and clang 8.0.1 on the phone.

## wzykubek | 2020-08-08T19:52:29+00:00
> I repeat: Can you start from the beginning and paste `cmake ..` output? These errors happen when building for 32-bit ARM.

So armv7l is not supported? Is any solution to build XMRig for this architecture? 

## SChernykh | 2020-08-08T19:59:01+00:00
32-bit ARM is not supported because it's too inefficient for mining. There's no RandomX JIT compiler for it, so it would do 1 h/s RandomX at best.

## wzykubek | 2020-08-08T20:00:30+00:00
> 32-bit ARM is not supported because it's too inefficient for mining. There's no RandomX JIT compiler for it, so it would do 1 h/s RandomX at best.

Ok, thanks for answer.

## kofif1 | 2020-08-08T20:06:06+00:00
Thanks for taking the time, but this is a 64 Bit architecture. 
lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 18.04.4 LTS
Release: 18.04
Codename: bionic
rock64@rock64:~$ uname -a
Linux rock64 4.4.167-1213-rockchip-ayufan-g34ae07687fce #1 SMP Tue Jun 18 20:44:49 UTC 2019 aarch64 aarch64 aarch64 GNU/Linux

So, it must be something else. 
Ilan

## xmrig | 2020-08-08T20:25:22+00:00
Something very wrong with the compiler:
`Performing Test XMRIG_ARM_CRYPTO - Failed` you compiler don't support crypto extensions for hardware AES support, it's bad but not fatal in that case software implementation will be used as failback, but only on 64 bits.

I also suspect your compiler is 32 bit, `/usr/lib/arm-linux-gnueabihf/libuv.a` should be `/usr/lib/aarch64-linux-gnu/libuv.a`.
Thank you.

## kofif1 | 2020-08-08T20:29:20+00:00
Can you tell me where to download the right compiler?
Thanks
Ilan

## xmrig | 2020-08-08T20:48:47+00:00
Maybe it already exists in your system just named differently or can be installed via apt, also please check if directory `/usr/lib/aarch64-linux-gnu` (or similar) exists, if it exists it is a good sign.

Your Linux kernel may 64 bit, but user land is 32 bit, for Raspberry PI such issues are big pain, maybe your board has similar issues, you need to fugue it by yourself, we can't help with Rock64 specific issues.
Thank you.


## RhinoAK | 2020-11-20T02:43:49+00:00
Following the same steps as original poster on RPi 4 8GB and it get the same issue. I'm running latest ARM 64bit OS and have verified the same.  Each time I attempt to initiate xmrig I continually get 👍🏾 

/home/xmrig/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: ‘void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true]’ used but never defined
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2260: CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:74: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
pi@rhinotoshipi:/home/xmrig/xmrig/build $ xmrig --version
-bash: xmrig: command not found


## NetherStar64 | 2021-03-08T09:49:48+00:00
Try building it on 64 Bit, worked for me

# Action History
- Created by: kofif1 | 2020-08-05T23:45:12+00:00
- Closed at: 2021-04-12T14:50:40+00:00
