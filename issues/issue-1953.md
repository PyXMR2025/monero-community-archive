---
title: armv8l make error
source_url: https://github.com/xmrig/xmrig/issues/1953
author: calvintam236
assignees: []
labels: []
created_at: '2020-11-23T06:18:55+00:00'
updated_at: '2021-04-12T14:34:04+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:34:03+00:00'
---

# Original Description
**Describe the bug**
- Cannot build for `armv8l` on ARMTARGET 7 and 8.
- `cpu.cmake` not handling for this arch

**To Reproduce**
Ubuntu build instruction on xmrig.com

**Expected behavior**
Successfully built

**Required data**
 - CPU: MT8183
 - Logs will be in comment
 - OS: Ubuntu

# Discussion History
## calvintam236 | 2020-11-23T06:19:46+00:00
7
```bash
[  1%] Built target ethash
[  4%] Built target argon2
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
In file included from /home/amazon/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function 'void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x0 = _mm_aesenc_si128(*x0, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: note: (if you use '-fpermissive', G++ will accept your code, but allowing the use of an undeclared name is deprecated)
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:175:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:176:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:177:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:178:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:179:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:180:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:181:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function '__m128i aes_round_tweak_div(const __m128i&, const __m128i&)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:367:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:368:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:18: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
             cx = _mm_aesenc_si128(cx, ax0);
                  ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:19: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:19: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(2) long long int]':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from 'void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; __m128i = __vector(2) long long int]'
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]'
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: '_mm_aesenc_si128' was not declared in this scope
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: '_mm_and_si128'
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = true; __m128i = __vector(2) long long int]':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from 'void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; __m128i = __vector(2) long long int]'
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]'
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: '_mm_and_si128'
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: At global scope:
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true]' used but never defined
In file included from /home/amazon/xmrig/src/crypto/cn/CryptoNight_monero.h:183:0,
                 from /home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:33,
                 from /home/amazon/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/amazon/xmrig/src/crypto/cn/r/variant4_random_math.h:95:13: warning: 'void v4_random_math(const V4_Instruction*, v4_reg*) [with v4_reg = unsigned int]' used but never defined
 static void v4_random_math(const struct V4_Instruction* code, v4_reg* r)
             ^~~~~~~~~~~~~~
In file included from /home/amazon/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true]' used but never defined
cc1plus: warning: unrecognized command line option '-Wno-class-memaccess'
CMakeFiles/xmrig.dir/build.make:4118: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

## calvintam236 | 2020-11-23T06:23:08+00:00
8
```bash
[  1%] Built target ethash
[  4%] Built target argon2
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[  4%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[  6%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[  6%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[  8%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
/home/amazon/xmrig/src/crypto/randomx/aes_hash.cpp: In lambda function:
/home/amazon/xmrig/src/crypto/randomx/aes_hash.cpp:390:38: warning: requested alignment 16 is larger than 8 [-Wattributes]
           alignas(16) uint8_t hash[64] = {};
                                      ^
/home/amazon/xmrig/src/crypto/randomx/aes_hash.cpp:391:39: warning: requested alignment 16 is larger than 8 [-Wattributes]
           alignas(16) uint8_t state[64] = {};
                                       ^
In file included from /home/amazon/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function 'void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x0 = _mm_aesenc_si128(*x0, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:15: note: (if you use '-fpermissive', G++ will accept your code, but allowing the use of an undeclared name is deprecated)
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:175:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:176:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:177:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:178:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:179:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:180:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:181:15: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function '__m128i aes_round_tweak_div(const __m128i&, const __m128i&)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:367:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:368:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:18: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
             cx = _mm_aesenc_si128(cx, ax0);
                  ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In function 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t)':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:19: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:19: error: there are no arguments to '_mm_aesenc_si128' that depend on a template parameter, so a declaration of '_mm_aesenc_si128' must be available [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ^~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:238:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:239:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:240:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:241:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:242:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:243:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:244:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:245:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:246:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:256:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:257:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:261:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:262:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:263:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:267:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:269:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: note: suggested alternative: '_mm_and_si128'
             cx = _mm_aesenc_si128(cx, ax0);
                  ~~~~~~~~~~~~~~~~^~~~~~~~~
                  _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]':
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:273:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: suggested alternative: '_mm_and_si128'
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
                   _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = _mm_aesenc_si128(cx1, ax1);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: note: '_mm_aesenc_si128' declared here, later in the translation unit
             cx0 = _mm_aesenc_si128(cx0, ax0);
                   ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(2) long long int]':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from 'void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; __m128i = __vector(2) long long int]'
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]'
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: '_mm_aesenc_si128' was not declared in this scope
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: '_mm_and_si128'
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of 'void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = true; __m128i = __vector(2) long long int]':
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:224:32:   required from 'void xmrig::cn_explode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; __m128i = __vector(2) long long int]'
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:453:42:   required from 'void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]'
/home/amazon/xmrig/src/crypto/cn/CnHash.cpp:236:5:   required from here
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: error: '_mm_aesenc_si128' was not declared in this scope
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: suggested alternative: '_mm_and_si128'
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
               _mm_and_si128
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:175:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = _mm_aesenc_si128(*x1, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:176:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = _mm_aesenc_si128(*x2, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:177:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = _mm_aesenc_si128(*x3, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:178:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = _mm_aesenc_si128(*x4, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:179:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = _mm_aesenc_si128(*x5, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:180:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = _mm_aesenc_si128(*x6, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:181:31: error: '_mm_aesenc_si128' was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = _mm_aesenc_si128(*x7, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:174:31: note: '_mm_aesenc_si128' declared here, later in the translation unit
         *x0 = _mm_aesenc_si128(*x0, key);
               ~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h: At global scope:
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)0; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)1]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)2]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3; bool SOFT_AES = true]' used but never defined
In file included from /home/amazon/xmrig/src/crypto/cn/CryptoNight_monero.h:183:0,
                 from /home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:33,
                 from /home/amazon/xmrig/src/crypto/cn/CnHash.cpp:35:
/home/amazon/xmrig/src/crypto/cn/r/variant4_random_math.h:95:13: warning: 'void v4_random_math(const V4_Instruction*, v4_reg*) [with v4_reg = unsigned int]' used but never defined
 static void v4_random_math(const struct V4_Instruction* code, v4_reg* r)
             ^~~~~~~~~~~~~~
In file included from /home/amazon/xmrig/src/crypto/cn/CnHash.cpp:35:0:
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)3]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)4]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)5]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)6; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)7]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)8]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)9]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)10]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)11; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)12]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)13; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)14]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)15; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = false]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)16]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17; bool SOFT_AES = true]' used but never defined
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:391:20: warning: 'void xmrig::cryptonight_monero_tweak(const uint8_t*, uint64_t, __m128i, __m128i, __m128i, __m128i&) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)17]' used but never defined
 static inline void cryptonight_monero_tweak(const uint8_t* l, uint64_t idx, __m128i ax0, __m128i bx0, __m128i bx1, __m128i& cx)
                    ^~~~~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = false]' used but never defined
 static inline void cn_implode_scratchpad(const __m128i *input, __m128i *output)
                    ^~~~~~~~~~~~~~~~~~~~~
/home/amazon/xmrig/src/crypto/cn/CryptoNight_arm.h:264:20: warning: 'void xmrig::cn_implode_scratchpad(const __m128i*, __m128i*) [with xmrig::Algorithm::Id ALGO = (xmrig::Algorithm::Id)18; bool SOFT_AES = true]' used but never defined
cc1plus: warning: unrecognized command line option '-Wno-class-memaccess'
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp: In member function 'void RandomX_ConfigurationBase::Apply()':
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:290:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IADD_RS, NULL);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:290:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IADD_RS, NULL);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:291:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IADD_M, IADD_RS);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:291:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IADD_M, IADD_RS);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:292:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISUB_R, IADD_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:292:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISUB_R, IADD_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:293:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISUB_M, ISUB_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:293:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISUB_M, ISUB_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:294:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IMUL_R, ISUB_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:294:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IMUL_R, ISUB_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:295:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IMUL_M, IMUL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:295:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IMUL_M, IMUL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:305:3: note: in expansion of macro 'INST_HANDLE'
   INST_HANDLE(IMULH_R, IMUL_M);
   ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:305:3: note: in expansion of macro 'INST_HANDLE'
   INST_HANDLE(IMULH_R, IMUL_M);
   ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:306:3: note: in expansion of macro 'INST_HANDLE'
   INST_HANDLE(IMULH_M, IMULH_R);
   ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:306:3: note: in expansion of macro 'INST_HANDLE'
   INST_HANDLE(IMULH_M, IMULH_R);
   ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:309:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISMULH_R, IMULH_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:309:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISMULH_R, IMULH_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:310:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISMULH_M, ISMULH_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:310:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISMULH_M, ISMULH_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:311:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IMUL_RCP, ISMULH_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:311:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IMUL_RCP, ISMULH_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:312:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(INEG_R, IMUL_RCP);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:312:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(INEG_R, IMUL_RCP);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:313:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IXOR_R, INEG_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:313:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IXOR_R, INEG_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:314:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IXOR_M, IXOR_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:314:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IXOR_M, IXOR_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:315:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IROR_R, IXOR_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:315:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IROR_R, IXOR_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:316:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IROL_R, IROR_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:316:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(IROL_R, IROR_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:317:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISWAP_R, IROL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:317:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISWAP_R, IROL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:318:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSWAP_R, ISWAP_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:318:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSWAP_R, ISWAP_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:319:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FADD_R, FSWAP_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:319:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FADD_R, FSWAP_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:320:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FADD_M, FADD_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:320:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FADD_M, FADD_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:321:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSUB_R, FADD_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:321:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSUB_R, FADD_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:322:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSUB_M, FSUB_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:322:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSUB_M, FSUB_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:323:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSCAL_R, FSUB_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:323:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSCAL_R, FSUB_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:324:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FMUL_R, FSCAL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:324:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FMUL_R, FSCAL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:325:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FDIV_M, FMUL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:325:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FDIV_M, FMUL_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:326:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSQRT_R, FDIV_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:326:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(FSQRT_R, FDIV_M);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:336:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(CBRANCH, FSQRT_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:336:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(CBRANCH, FSQRT_R);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:346:3: note: in expansion of macro 'INST_HANDLE'
   INST_HANDLE(CFROUND, CBRANCH);
   ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:346:3: note: in expansion of macro 'INST_HANDLE'
   INST_HANDLE(CFROUND, CBRANCH);
   ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:349:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISTORE, CFROUND);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:349:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(ISTORE, CFROUND);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:38: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                      ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:350:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(NOP, ISTORE);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:273:76: error: 'randomx::JitCompilerA64' has not been declared
 #define JIT_HANDLE(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                            ^
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:284:30: note: in expansion of macro 'JIT_HANDLE'
  for (; k < freq_sum; ++k) { JIT_HANDLE(x, prev); }
                              ^~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:350:2: note: in expansion of macro 'INST_HANDLE'
  INST_HANDLE(NOP, ISTORE);
  ^~~~~~~~~~~
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp: In function 'void randomx_calculate_hash(randomx_vm*, const void*, size_t, void*)':
/home/amazon/xmrig/src/crypto/randomx/randomx.cpp:568:34: warning: requested alignment 16 is larger than 8 [-Wattributes]
   alignas(16) uint64_t tempHash[8];
                                  ^
At global scope:
cc1plus: warning: unrecognized command line option '-Wno-class-memaccess'
CMakeFiles/xmrig.dir/build.make:4118: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
CMakeFiles/xmrig.dir/build.make:4454: recipe for target 'CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o] Error 1
At global scope:
cc1plus: warning: unrecognized command line option '-Wno-class-memaccess'
CMakeFiles/Makefile2:68: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

## Spudz76 | 2020-12-04T09:38:02+00:00
If your build command includes extra CFLAGS or CXXFLAGS ... don't

## calvintam236 | 2020-12-04T19:46:04+00:00
> If your build command includes extra CFLAGS or CXXFLAGS ... don't

I did not use any extra flags. I did `cmake ..` as in the build instructions.

## NetherStar64 | 2021-01-09T14:44:55+00:00
I have also the exact same Issue building on ARM. I followed the normal Build from Source Guide.

## renjieliu | 2021-02-15T04:29:00+00:00
I faced the same issue, but figured out I was using the 32-bit compiler by using below commands., although the ```uname -a``` is showing **armv8l**

1. Find out which compiler it's using
```which GCC```

2. With the path found, check the file type
```file THE_PATH_FOUND```

3. In case above step returns a symbolic, use ```file``` command to check the target file of the symbolic link, until the real compiler is found.

## domexie | 2021-02-27T14:35:25+00:00
> I faced the same issue, but figured out I was using the 32-bit compiler by using below commands., although the `uname -a` is showing **armv8l**
> 
> 1. Find out which compiler it's using
>    `which GCC`
> 2. With the path found, check the file type
>    `file THE_PATH_FOUND`
> 3. In case above step returns a symbolic, use `file` command to check the target file of the symbolic link, until the real compiler is found.

So did you eventually solve the problem?
If true, could you please tell us how to use the 64bit compiler?

## renjieliu | 2021-02-27T15:00:59+00:00
> > I faced the same issue, but figured out I was using the 32-bit compiler by using below commands., although the `uname -a` is showing **armv8l**
> > 
> > 1. Find out which compiler it's using
> >    `which GCC`
> > 2. With the path found, check the file type
> >    `file THE_PATH_FOUND`
> > 3. In case above step returns a symbolic, use `file` command to check the target file of the symbolic link, until the real compiler is found.
> 
> So did you eventually solve the problem?
> If true, could you please tell us how to use the 64bit compiler?

Yes, I am able to build and compile on ARM64 (aarch64) 
I am using Raspberry Pi 4, 8GB version, with Raspberry Pi OS 64 bit.
You can try below commands on your box. 

```
sudo apt-get install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake ..
make -j4
./xmrig -o ca.minexmr.com -u YOUR_WALLET_ADDRESS
```

I am using ca.minexmr.com as pool, but you can replace it per your need. The alternative pools can be found here - 

https://minexmr.com/miningguide

Hope it works for you.


## calvintam236 | 2021-02-27T20:25:25+00:00
> > > I faced the same issue, but figured out I was using the 32-bit compiler by using below commands., although the `uname -a` is showing **armv8l**
> > > 
> > > 1. Find out which compiler it's using
> > >    `which GCC`
> > > 2. With the path found, check the file type
> > >    `file THE_PATH_FOUND`
> > > 3. In case above step returns a symbolic, use `file` command to check the target file of the symbolic link, until the real compiler is found.
> > 
> > 
> > So did you eventually solve the problem?
> > If true, could you please tell us how to use the 64bit compiler?
> 
> Yes, I am able to build and compile on ARM64 (aarch64)
> I am using Raspberry Pi 4, 8GB version, with Raspberry Pi OS 64 bit.
> You can try below commands on your box.
> 
> ```
> sudo apt-get install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
> git clone https://github.com/xmrig/xmrig.git
> mkdir xmrig/build && cd xmrig/build
> cmake ..
> make -j4
> ./xmrig -o ca.minexmr.com -u YOUR_WALLET_ADDRESS
> ```
> 
> I am using ca.minexmr.com as pool, but you can replace it per your need. The alternative pools can be found here -
> 
> https://minexmr.com/miningguide
> 
> Hope it works for you.

This is an issue for `armv8l` arch, not `aarch64`...

## renjieliu | 2021-02-27T22:30:18+00:00
If ```uname -a``` shows armv8l, it means your OS is essentially a 32bit kernel, so the OS will not run 64 bit compiler, which is needed for xmrig to run. 

So the answer is No. 

## calvintam236 | 2021-02-27T22:55:27+00:00
> If `uname -a` shows armv8l, it means your OS is essentially a 32bit kernel. It will not run 64 bit compiler, which is needed for xmrig to run.
> 
> So the answer is No.

Yet it won't build for ARMTARGET 7 under `armv8l`, which is 32 bit architecture. XMRig can build and compile on `armv7` and `armv7l`.

# Action History
- Created by: calvintam236 | 2020-11-23T06:18:55+00:00
- Closed at: 2021-04-12T14:34:03+00:00
