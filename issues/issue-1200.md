---
title: Can't compile on macOS 10.11.6
source_url: https://github.com/xmrig/xmrig/issues/1200
author: davdpwr
assignees: []
labels: []
created_at: '2019-09-28T07:55:58+00:00'
updated_at: '2020-10-25T23:58:40+00:00'
type: issue
status: closed
closed_at: '2019-10-03T06:27:58+00:00'
---

# Original Description
I understand this is probably a clang vs gcc issue. I've tried forcing gcc with:

`cmake -D CMAKE_C_COMPILER=gcc -v -D CMAKE_CXX_COMPILER=g++ -v .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl`

...but that doesn't seem to be working either. Make gets to 71% and then fails with:

```
In file included from /usr/local/opt/xmrig/src/crypto/cn/CnHash.cpp:37:
In file included from /usr/local/opt/xmrig/src/crypto/cn/CryptoNight_x86.h:42:
/usr/local/opt/xmrig/src/crypto/cn/soft_aes.h:145:26: error: use of undeclared
      identifier '_rotr'
    return _mm_set_epi32(_rotr(X3, 8) ^ rcon, X3, _rotr(X1, 8) ^ rcon, X1);
                         ^
/usr/local/opt/xmrig/src/crypto/cn/soft_aes.h:145:51: error: use of undeclared
      identifier '_rotr'
    return _mm_set_epi32(_rotr(X3, 8) ^ rcon, X3, _rotr(X1, 8) ^ rcon, X1);
                                                  ^
2 errors generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

Is it even possible to get this up and running on 10.11.x?


# Discussion History
## xmrig | 2019-09-28T11:54:20+00:00
It strange for clang availability of `_rotr` detected by cmake, for gcc assume this function always exists, but seems not always.

Please show output of `gcc -v`
For workaround you can remove 2 lines 133 and 138 https://github.com/xmrig/xmrig/blob/evo/src/crypto/cn/soft_aes.h#L133
Thank you.

## davdpwr | 2019-09-29T07:33:29+00:00
```
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/Cellar/gcc/9.2.0/libexec/gcc/x86_64-apple-darwin15/9.2.0/lto-wrapper
Target: x86_64-apple-darwin15
Configured with: ../configure --build=x86_64-apple-darwin15 --prefix=/usr/local/Cellar/gcc/9.2.0 --libdir=/usr/local/Cellar/gcc/9.2.0/lib/gcc/9 --disable-nls --enable-checking=release --enable-languages=c,c++,objc,obj-c++,fortran --program-suffix=-9 --with-gmp=/usr/local/opt/gmp --with-mpfr=/usr/local/opt/mpfr --with-mpc=/usr/local/opt/libmpc --with-isl=/usr/local/opt/isl --with-system-zlib --with-pkgversion='Homebrew GCC 9.2.0' --with-bugurl=https://github.com/Homebrew/homebrew-core/issues
Thread model: posix
gcc version 9.2.0 (Homebrew GCC 9.2.0)
```

I tried your suggested line changes and got this:

```
[  1%] Built target argon2-sse2
[  4%] Built target xmrig-asm
[  6%] Built target argon2-avx512f
[  7%] Built target argon2-avx2
[  8%] Built target argon2-xop
[ 10%] Built target argon2-ssse3
[ 16%] Built target argon2
[ 16%] Linking CXX executable xmrig
Undefined symbols for architecture x86_64:
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)0>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)0, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)0, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)0, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)0, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)0, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)0, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)0, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)0>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)0, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)0, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)0, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)0, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)10>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)10, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)10, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)10, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)10, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)10, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)10, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)10, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)10>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)10, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)10, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)10, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)10, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)11>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)11, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)11, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)11, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)11, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)11, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)11, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)11, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)11>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)11, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)11, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)11, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)11, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)12>::m_memory", referenced from:
      void xmrig::cryptonight_single_hash_gpu<(xmrig::Algorithm::Id)12, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash_gpu<(xmrig::Algorithm::Id)12, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)13>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)13, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)13, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)13, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)13, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)13, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)13, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)13, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)13>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)13, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)13, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)13, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)13, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)14>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)14, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)14, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)14, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)14, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)14, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)14, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)14, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)14>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)14, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)14, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)14, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)14, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)15>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)15, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)15, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)15, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)15, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)15, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)15, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)15, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)15>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)15, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)15, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)15, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)15, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)16>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)16, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)16, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)16, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)16, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)16, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)16, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)16, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)16>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)16, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)16, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)16, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)16, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)17>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)17, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)17, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)17, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)17, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)17, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)17, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)17, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)17>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)17, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)17, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)17, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)17, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)18>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)18, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)18, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)18, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)18, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)18, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)18, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)18, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)18>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)18, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)18, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)18, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)18, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)1>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)1, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)1, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)1, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)1, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)1, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)1, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)1, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)1>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)1, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)1, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)1, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)1, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)2>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)2, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)2, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)2, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)2, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)2, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)2, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)2, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)2>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)2, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)2, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)2, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)2, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)3>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)3, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)3, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)3, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)3, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)3, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)3, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)3, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)3>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)3, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)3, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)3, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)3, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)4>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)4, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)4, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)4, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)4, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)4, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)4, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)4, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)4>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)4, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)4, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)4, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)4, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)5>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)5, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)5, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)5, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)5, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)5, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)5, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)5, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)5>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)5, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)5, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)5, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)5, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)6, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)6, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)6, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)6, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)6, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)6, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)6, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)6>::m_memory", referenced from:
      xmrig::CnHash::CnHash() in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)6, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)6, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)6, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)6, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)7>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)7, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)7, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)7, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)7, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)7, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)7, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)7, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)7>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)7, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)7, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)7, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)7, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)8>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)8, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)8, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)8, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)8, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)8, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)8, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)8, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)8>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)8, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)8, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)8, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)8, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)9>::m_iterations", referenced from:
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)9, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_single_hash<(xmrig::Algorithm::Id)9, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)9, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_double_hash<(xmrig::Algorithm::Id)9, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)9, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_triple_hash<(xmrig::Algorithm::Id)9, true>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      void xmrig::cryptonight_quad_hash<(xmrig::Algorithm::Id)9, false>(unsigned char const*, unsigned long, unsigned char*, cryptonight_ctx**, unsigned long long) in CnHash.cpp.o
      ...
  "xmrig::CnAlgo<(xmrig::Algorithm::Id)9>::m_memory", referenced from:
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)9, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)9, false>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_explode_scratchpad<(xmrig::Algorithm::Id)9, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
      void xmrig::cn_implode_scratchpad<(xmrig::Algorithm::Id)9, true>(long long vector[2] const*, long long vector[2]*) in CnHash.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

## xmrig | 2019-09-29T15:59:13+00:00
Use v4.2+. Thank you.

## davdpwr | 2019-10-01T02:51:25+00:00
Works!

## realdivinetech | 2020-10-25T23:58:40+00:00
Please what is the thing that we are going to change the version 4.2+

# Action History
- Created by: davdpwr | 2019-09-28T07:55:58+00:00
- Closed at: 2019-10-03T06:27:58+00:00
