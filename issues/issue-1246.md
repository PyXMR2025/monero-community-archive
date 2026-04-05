---
title: enabling Randomx breaks build for all iOS systems
source_url: https://github.com/xmrig/xmrig/issues/1246
author: resistor4u
assignees: []
labels:
- bug
created_at: '2019-10-17T18:31:08+00:00'
updated_at: '2021-04-12T15:05:15+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:05:15+00:00'
---

# Original Description
Working from a02ee96651d4268b on a mac v. 10.13.6 with xcode 10.1, the following cmake settings fail to produce a working binary:
```
cmake .. -DCMAKE_TOOLCHAIN_FILE=/Users/user/ios-cmake/ios.toolchain.cmake -DENABLE_ARC=OFF -DENABLE_BITCODE=OFF -DPLATFORM=OS64 -DDEPLOYMENT_TARGET=12.0 -DCMAKE_HOST_SYSTEM_PROCESSOR=aarch64 -DCMAKE_SYSTEM_PROCESSOR=aarch64 -DWITH_HWLOC=OFF -DWITH_RANDOMX=ON -DWITH_TLS=OFF -DWITH_HTTP=OFF -DWITH_CN_LITE=OFF -DWITH_CN_GPU=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DUV_LIBRARY=/Users/user/libuv/libuv.a -DUV_INCLUDE_DIR=/Users/user/libuv/libuv/include -DWITH_ARGON2=OFF -DWITH_OPENCL=OFF
```
The make command succeeds up to 100%, but fails at the final linking phase because according to `ld` none of the object files are 4-byte aligned. Here's a sample of the `ld` warnings:
```
ld: warning: arm64 function not 4-byte aligned: randomx_program_aarch64 from CMakeFiles/xmrig-notls.dir/src/crypto/randomx/jit_compiler_a64_static.S.o
ld: warning: arm64 function not 4-byte aligned: literal_x25 from CMakeFiles/xmrig-notls.dir/src/crypto/randomx/jit_compiler_a64_static.S.o
...
ld: warning: arm64 function not 4-byte aligned: randomx_program_aarch64_imul_rcp_literals_end from CMakeFiles/xmrig-notls.dir/src/crypto/randomx/jit_compiler_a64_static.S.o
...
ld: warning: arm64 function not 4-byte aligned: randomx_calc_dataset_item_aarch64_end from CMakeFiles/xmrig-notls.dir/src/crypto/randomx/jit_compiler_a64_static.S.o
Undefined symbols for architecture arm64:
  "___clear_cache", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
...
ld: symbol(s) not found for architecture arm64
```

Yet each of the object files reports being ` Mach-O 64-bit object arm64`

Setting `-DWITH_RANDOMX=OFF` will produce a working binary, but without the randomx support.

What can be done to fix this?

# Discussion History
## xmrig | 2019-10-18T05:03:23+00:00
`___clear_cache` issue fixed. Thank you

## SChernykh | 2019-10-18T14:19:39+00:00
https://github.com/xmrig/xmrig/pull/1247 should fix `arm64 function not 4-byte aligned` warnings.

## resistor4u | 2019-10-18T19:31:06+00:00
i've updated to 128c5f67ad05da3a9a8c8a0eaa8c664b868bec96, but the build fails for me. `__builtin___clear_cache` is still not found, according to cmake, and build fails at 100% with
```
Undefined symbols for architecture arm64:
  "___clear_cache", referenced from:
...
  "_randomx_calc_dataset_item_aarch64", referenced from:
...
  "_randomx_calc_dataset_item_aarch64_end", referenced from:
...
...
  "_randomx_program_aarch64_vm_instructions_end_light", referenced from:
```
etc., etc., etc. #1247 did resolve the `arm64 function not 4-byte aligned` errors though. Need more logs?

## SChernykh | 2019-10-18T19:34:59+00:00
It should have used sys_icache_invalidate instead of ___clear_cache. It's hard to fix it when I have only Android phone for testing. Your compiler should define either `ios_HOST_OS` or `darwin_HOST_OS` macro, otherwise it won't work.

## resistor4u | 2019-11-04T21:42:54+00:00
@SChernykh here's `clang --version` for MacOS 10.13.6:
```
Apple LLVM version 10.0.0 (clang-1000.11.45.5)
Target: x86_64-apple-darwin17.7.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```
And here's a list of the builtin defined macros:
```
#define OBJC_NEW_PROPERTIES 1
#define _LP64 1
#define __APPLE_CC__ 6000
#define __APPLE__ 1
#define __ATOMIC_ACQUIRE 2
#define __ATOMIC_ACQ_REL 4
#define __ATOMIC_CONSUME 1
#define __ATOMIC_RELAXED 0
#define __ATOMIC_RELEASE 3
#define __ATOMIC_SEQ_CST 5
#define __BIGGEST_ALIGNMENT__ 16
#define __BLOCKS__ 1
#define __BYTE_ORDER__ __ORDER_LITTLE_ENDIAN__
#define __CHAR16_TYPE__ unsigned short
#define __CHAR32_TYPE__ unsigned int
#define __CHAR_BIT__ 8
#define __CLANG_ATOMIC_BOOL_LOCK_FREE 2
#define __CLANG_ATOMIC_CHAR16_T_LOCK_FREE 2
#define __CLANG_ATOMIC_CHAR32_T_LOCK_FREE 2
#define __CLANG_ATOMIC_CHAR_LOCK_FREE 2
#define __CLANG_ATOMIC_INT_LOCK_FREE 2
#define __CLANG_ATOMIC_LLONG_LOCK_FREE 2
#define __CLANG_ATOMIC_LONG_LOCK_FREE 2
#define __CLANG_ATOMIC_POINTER_LOCK_FREE 2
#define __CLANG_ATOMIC_SHORT_LOCK_FREE 2
#define __CLANG_ATOMIC_WCHAR_T_LOCK_FREE 2
#define __CONSTANT_CFSTRINGS__ 1
#define __DBL_DECIMAL_DIG__ 17
#define __DBL_DENORM_MIN__ 4.9406564584124654e-324
#define __DBL_DIG__ 15
#define __DBL_EPSILON__ 2.2204460492503131e-16
#define __DBL_HAS_DENORM__ 1
#define __DBL_HAS_INFINITY__ 1
#define __DBL_HAS_QUIET_NAN__ 1
#define __DBL_MANT_DIG__ 53
#define __DBL_MAX_10_EXP__ 308
#define __DBL_MAX_EXP__ 1024
#define __DBL_MAX__ 1.7976931348623157e+308
#define __DBL_MIN_10_EXP__ (-307)
#define __DBL_MIN_EXP__ (-1021)
#define __DBL_MIN__ 2.2250738585072014e-308
#define __DECIMAL_DIG__ __LDBL_DECIMAL_DIG__
#define __DYNAMIC__ 1
#define __ENVIRONMENT_MAC_OS_X_VERSION_MIN_REQUIRED__ 101300
#define __FINITE_MATH_ONLY__ 0
#define __FLT16_DECIMAL_DIG__ 5
#define __FLT16_DENORM_MIN__ 5.9604644775390625e-8F16
#define __FLT16_DIG__ 3
#define __FLT16_EPSILON__ 9.765625e-4F16
#define __FLT16_HAS_DENORM__ 1
#define __FLT16_HAS_INFINITY__ 1
#define __FLT16_HAS_QUIET_NAN__ 1
#define __FLT16_MANT_DIG__ 11
#define __FLT16_MAX_10_EXP__ 4
#define __FLT16_MAX_EXP__ 15
#define __FLT16_MAX__ 6.5504e+4F16
#define __FLT16_MIN_10_EXP__ (-13)
#define __FLT16_MIN_EXP__ (-14)
#define __FLT16_MIN__ 6.103515625e-5F16
#define __FLT_DECIMAL_DIG__ 9
#define __FLT_DENORM_MIN__ 1.40129846e-45F
#define __FLT_DIG__ 6
#define __FLT_EPSILON__ 1.19209290e-7F
#define __FLT_EVAL_METHOD__ 0
#define __FLT_HAS_DENORM__ 1
#define __FLT_HAS_INFINITY__ 1
#define __FLT_HAS_QUIET_NAN__ 1
#define __FLT_MANT_DIG__ 24
#define __FLT_MAX_10_EXP__ 38
#define __FLT_MAX_EXP__ 128
#define __FLT_MAX__ 3.40282347e+38F
#define __FLT_MIN_10_EXP__ (-37)
#define __FLT_MIN_EXP__ (-125)
#define __FLT_MIN__ 1.17549435e-38F
#define __FLT_RADIX__ 2
#define __FXSR__ 1
#define __GCC_ATOMIC_BOOL_LOCK_FREE 2
#define __GCC_ATOMIC_CHAR16_T_LOCK_FREE 2
#define __GCC_ATOMIC_CHAR32_T_LOCK_FREE 2
#define __GCC_ATOMIC_CHAR_LOCK_FREE 2
#define __GCC_ATOMIC_INT_LOCK_FREE 2
#define __GCC_ATOMIC_LLONG_LOCK_FREE 2
#define __GCC_ATOMIC_LONG_LOCK_FREE 2
#define __GCC_ATOMIC_POINTER_LOCK_FREE 2
#define __GCC_ATOMIC_SHORT_LOCK_FREE 2
#define __GCC_ATOMIC_TEST_AND_SET_TRUEVAL 1
#define __GCC_ATOMIC_WCHAR_T_LOCK_FREE 2
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_1 1
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_16 1
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_2 1
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_4 1
#define __GCC_HAVE_SYNC_COMPARE_AND_SWAP_8 1
#define __GNUC_MINOR__ 2
#define __GNUC_PATCHLEVEL__ 1
#define __GNUC_STDC_INLINE__ 1
#define __GNUC__ 4
#define __GXX_ABI_VERSION 1002
#define __INT16_C_SUFFIX__ 
#define __INT16_FMTd__ "hd"
#define __INT16_FMTi__ "hi"
#define __INT16_MAX__ 32767
#define __INT16_TYPE__ short
#define __INT32_C_SUFFIX__ 
#define __INT32_FMTd__ "d"
#define __INT32_FMTi__ "i"
#define __INT32_MAX__ 2147483647
#define __INT32_TYPE__ int
#define __INT64_C_SUFFIX__ LL
#define __INT64_FMTd__ "lld"
#define __INT64_FMTi__ "lli"
#define __INT64_MAX__ 9223372036854775807LL
#define __INT64_TYPE__ long long int
#define __INT8_C_SUFFIX__ 
#define __INT8_FMTd__ "hhd"
#define __INT8_FMTi__ "hhi"
#define __INT8_MAX__ 127
#define __INT8_TYPE__ signed char
#define __INTMAX_C_SUFFIX__ L
#define __INTMAX_FMTd__ "ld"
#define __INTMAX_FMTi__ "li"
#define __INTMAX_MAX__ 9223372036854775807L
#define __INTMAX_TYPE__ long int
#define __INTMAX_WIDTH__ 64
#define __INTPTR_FMTd__ "ld"
#define __INTPTR_FMTi__ "li"
#define __INTPTR_MAX__ 9223372036854775807L
#define __INTPTR_TYPE__ long int
#define __INTPTR_WIDTH__ 64
#define __INT_FAST16_FMTd__ "hd"
#define __INT_FAST16_FMTi__ "hi"
#define __INT_FAST16_MAX__ 32767
#define __INT_FAST16_TYPE__ short
#define __INT_FAST32_FMTd__ "d"
#define __INT_FAST32_FMTi__ "i"
#define __INT_FAST32_MAX__ 2147483647
#define __INT_FAST32_TYPE__ int
#define __INT_FAST64_FMTd__ "ld"
#define __INT_FAST64_FMTi__ "li"
#define __INT_FAST64_MAX__ 9223372036854775807L
#define __INT_FAST64_TYPE__ long int
#define __INT_FAST8_FMTd__ "hhd"
#define __INT_FAST8_FMTi__ "hhi"
#define __INT_FAST8_MAX__ 127
#define __INT_FAST8_TYPE__ signed char
#define __INT_LEAST16_FMTd__ "hd"
#define __INT_LEAST16_FMTi__ "hi"
#define __INT_LEAST16_MAX__ 32767
#define __INT_LEAST16_TYPE__ short
#define __INT_LEAST32_FMTd__ "d"
#define __INT_LEAST32_FMTi__ "i"
#define __INT_LEAST32_MAX__ 2147483647
#define __INT_LEAST32_TYPE__ int
#define __INT_LEAST64_FMTd__ "ld"
#define __INT_LEAST64_FMTi__ "li"
#define __INT_LEAST64_MAX__ 9223372036854775807L
#define __INT_LEAST64_TYPE__ long int
#define __INT_LEAST8_FMTd__ "hhd"
#define __INT_LEAST8_FMTi__ "hhi"
#define __INT_LEAST8_MAX__ 127
#define __INT_LEAST8_TYPE__ signed char
#define __INT_MAX__ 2147483647
#define __LDBL_DECIMAL_DIG__ 21
#define __LDBL_DENORM_MIN__ 3.64519953188247460253e-4951L
#define __LDBL_DIG__ 18
#define __LDBL_EPSILON__ 1.08420217248550443401e-19L
#define __LDBL_HAS_DENORM__ 1
#define __LDBL_HAS_INFINITY__ 1
#define __LDBL_HAS_QUIET_NAN__ 1
#define __LDBL_MANT_DIG__ 64
#define __LDBL_MAX_10_EXP__ 4932
#define __LDBL_MAX_EXP__ 16384
#define __LDBL_MAX__ 1.18973149535723176502e+4932L
#define __LDBL_MIN_10_EXP__ (-4931)
#define __LDBL_MIN_EXP__ (-16381)
#define __LDBL_MIN__ 3.36210314311209350626e-4932L
#define __LITTLE_ENDIAN__ 1
#define __LONG_LONG_MAX__ 9223372036854775807LL
#define __LONG_MAX__ 9223372036854775807L
#define __LP64__ 1
#define __MACH__ 1
#define __MMX__ 1
#define __NO_INLINE__ 1
#define __NO_MATH_INLINES 1
#define __OBJC_BOOL_IS_BOOL 0
#define __OPENCL_MEMORY_SCOPE_ALL_SVM_DEVICES 3
#define __OPENCL_MEMORY_SCOPE_DEVICE 2
#define __OPENCL_MEMORY_SCOPE_SUB_GROUP 4
#define __OPENCL_MEMORY_SCOPE_WORK_GROUP 1
#define __OPENCL_MEMORY_SCOPE_WORK_ITEM 0
#define __ORDER_BIG_ENDIAN__ 4321
#define __ORDER_LITTLE_ENDIAN__ 1234
#define __ORDER_PDP_ENDIAN__ 3412
#define __PIC__ 2
#define __POINTER_WIDTH__ 64
#define __PRAGMA_REDEFINE_EXTNAME 1
#define __PTRDIFF_FMTd__ "ld"
#define __PTRDIFF_FMTi__ "li"
#define __PTRDIFF_MAX__ 9223372036854775807L
#define __PTRDIFF_TYPE__ long int
#define __PTRDIFF_WIDTH__ 64
#define __REGISTER_PREFIX__ 
#define __SCHAR_MAX__ 127
#define __SHRT_MAX__ 32767
#define __SIG_ATOMIC_MAX__ 2147483647
#define __SIG_ATOMIC_WIDTH__ 32
#define __SIZEOF_DOUBLE__ 8
#define __SIZEOF_FLOAT__ 4
#define __SIZEOF_INT128__ 16
#define __SIZEOF_INT__ 4
#define __SIZEOF_LONG_DOUBLE__ 16
#define __SIZEOF_LONG_LONG__ 8
#define __SIZEOF_LONG__ 8
#define __SIZEOF_POINTER__ 8
#define __SIZEOF_PTRDIFF_T__ 8
#define __SIZEOF_SHORT__ 2
#define __SIZEOF_SIZE_T__ 8
#define __SIZEOF_WCHAR_T__ 4
#define __SIZEOF_WINT_T__ 4
#define __SIZE_FMTX__ "lX"
#define __SIZE_FMTo__ "lo"
#define __SIZE_FMTu__ "lu"
#define __SIZE_FMTx__ "lx"
#define __SIZE_MAX__ 18446744073709551615UL
#define __SIZE_TYPE__ long unsigned int
#define __SIZE_WIDTH__ 64
#define __SSE2_MATH__ 1
#define __SSE2__ 1
#define __SSE3__ 1
#define __SSE4_1__ 1
#define __SSE_MATH__ 1
#define __SSE__ 1
#define __SSP__ 1
#define __SSSE3__ 1
#define __STDC_HOSTED__ 1
#define __STDC_NO_THREADS__ 1
#define __STDC_UTF_16__ 1
#define __STDC_UTF_32__ 1
#define __STDC_VERSION__ 201112L
#define __STDC__ 1
#define __UINT16_C_SUFFIX__ 
#define __UINT16_FMTX__ "hX"
#define __UINT16_FMTo__ "ho"
#define __UINT16_FMTu__ "hu"
#define __UINT16_FMTx__ "hx"
#define __UINT16_MAX__ 65535
#define __UINT16_TYPE__ unsigned short
#define __UINT32_C_SUFFIX__ U
#define __UINT32_FMTX__ "X"
#define __UINT32_FMTo__ "o"
#define __UINT32_FMTu__ "u"
#define __UINT32_FMTx__ "x"
#define __UINT32_MAX__ 4294967295U
#define __UINT32_TYPE__ unsigned int
#define __UINT64_C_SUFFIX__ ULL
#define __UINT64_FMTX__ "llX"
#define __UINT64_FMTo__ "llo"
#define __UINT64_FMTu__ "llu"
#define __UINT64_FMTx__ "llx"
#define __UINT64_MAX__ 18446744073709551615ULL
#define __UINT64_TYPE__ long long unsigned int
#define __UINT8_C_SUFFIX__ 
#define __UINT8_FMTX__ "hhX"
#define __UINT8_FMTo__ "hho"
#define __UINT8_FMTu__ "hhu"
#define __UINT8_FMTx__ "hhx"
#define __UINT8_MAX__ 255
#define __UINT8_TYPE__ unsigned char
#define __UINTMAX_C_SUFFIX__ UL
#define __UINTMAX_FMTX__ "lX"
#define __UINTMAX_FMTo__ "lo"
#define __UINTMAX_FMTu__ "lu"
#define __UINTMAX_FMTx__ "lx"
#define __UINTMAX_MAX__ 18446744073709551615UL
#define __UINTMAX_TYPE__ long unsigned int
#define __UINTMAX_WIDTH__ 64
#define __UINTPTR_FMTX__ "lX"
#define __UINTPTR_FMTo__ "lo"
#define __UINTPTR_FMTu__ "lu"
#define __UINTPTR_FMTx__ "lx"
#define __UINTPTR_MAX__ 18446744073709551615UL
#define __UINTPTR_TYPE__ long unsigned int
#define __UINTPTR_WIDTH__ 64
#define __UINT_FAST16_FMTX__ "hX"
#define __UINT_FAST16_FMTo__ "ho"
#define __UINT_FAST16_FMTu__ "hu"
#define __UINT_FAST16_FMTx__ "hx"
#define __UINT_FAST16_MAX__ 65535
#define __UINT_FAST16_TYPE__ unsigned short
#define __UINT_FAST32_FMTX__ "X"
#define __UINT_FAST32_FMTo__ "o"
#define __UINT_FAST32_FMTu__ "u"
#define __UINT_FAST32_FMTx__ "x"
#define __UINT_FAST32_MAX__ 4294967295U
#define __UINT_FAST32_TYPE__ unsigned int
#define __UINT_FAST64_FMTX__ "lX"
#define __UINT_FAST64_FMTo__ "lo"
#define __UINT_FAST64_FMTu__ "lu"
#define __UINT_FAST64_FMTx__ "lx"
#define __UINT_FAST64_MAX__ 18446744073709551615UL
#define __UINT_FAST64_TYPE__ long unsigned int
#define __UINT_FAST8_FMTX__ "hhX"
#define __UINT_FAST8_FMTo__ "hho"
#define __UINT_FAST8_FMTu__ "hhu"
#define __UINT_FAST8_FMTx__ "hhx"
#define __UINT_FAST8_MAX__ 255
#define __UINT_FAST8_TYPE__ unsigned char
#define __UINT_LEAST16_FMTX__ "hX"
#define __UINT_LEAST16_FMTo__ "ho"
#define __UINT_LEAST16_FMTu__ "hu"
#define __UINT_LEAST16_FMTx__ "hx"
#define __UINT_LEAST16_MAX__ 65535
#define __UINT_LEAST16_TYPE__ unsigned short
#define __UINT_LEAST32_FMTX__ "X"
#define __UINT_LEAST32_FMTo__ "o"
#define __UINT_LEAST32_FMTu__ "u"
#define __UINT_LEAST32_FMTx__ "x"
#define __UINT_LEAST32_MAX__ 4294967295U
#define __UINT_LEAST32_TYPE__ unsigned int
#define __UINT_LEAST64_FMTX__ "lX"
#define __UINT_LEAST64_FMTo__ "lo"
#define __UINT_LEAST64_FMTu__ "lu"
#define __UINT_LEAST64_FMTx__ "lx"
#define __UINT_LEAST64_MAX__ 18446744073709551615UL
#define __UINT_LEAST64_TYPE__ long unsigned int
#define __UINT_LEAST8_FMTX__ "hhX"
#define __UINT_LEAST8_FMTo__ "hho"
#define __UINT_LEAST8_FMTu__ "hhu"
#define __UINT_LEAST8_FMTx__ "hhx"
#define __UINT_LEAST8_MAX__ 255
#define __UINT_LEAST8_TYPE__ unsigned char
#define __USER_LABEL_PREFIX__ _
#define __VERSION__ "4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)"
#define __WCHAR_MAX__ 2147483647
#define __WCHAR_TYPE__ int
#define __WCHAR_WIDTH__ 32
#define __WINT_MAX__ 2147483647
#define __WINT_TYPE__ int
#define __WINT_WIDTH__ 32
#define __amd64 1
#define __amd64__ 1
#define __apple_build_version__ 10001145
#define __block __attribute__((__blocks__(byref)))
#define __clang__ 1
#define __clang_major__ 10
#define __clang_minor__ 0
#define __clang_patchlevel__ 0
#define __clang_version__ "10.0.0 (clang-1000.11.45.5)"
#define __core2 1
#define __core2__ 1
#define __llvm__ 1
#define __nonnull _Nonnull
#define __null_unspecified _Null_unspecified
#define __nullable _Nullable
#define __pic__ 2
#define __strong 
#define __tune_core2__ 1
#define __unsafe_unretained 
#define __weak __attribute__((objc_gc(weak)))
#define __x86_64 1
#define __x86_64__ 1
```
Unless I'm looking in the wrong place, it doesn't seem like `ios_HOST_OS` or `darwin_HOST_OS` are included there, but `__APPLE__` is. So, I changed:

https://github.com/xmrig/xmrig/blob/4c4a674a4be37cdc9860eef0b025eb66e8a95be4/src/crypto/randomx/jit_compiler_a64.cpp#L106 `ios_HOST_OS` to `__APPLE__` in lines 106 and 112. Then I rebuilt and here is the output:
```
Undefined symbols for architecture arm64:
  "randomx::sys_icache_invalidate(void*, unsigned long)", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
  "_randomx_calc_dataset_item_aarch64", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
  "_randomx_calc_dataset_item_aarch64_end", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
  "_randomx_calc_dataset_item_aarch64_mix", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
  "_randomx_calc_dataset_item_aarch64_prefetch", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
  "_randomx_calc_dataset_item_aarch64_store_result", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::~JitCompilerA64() in jit_compiler_a64.cpp.o
  "_randomx_init_dataset_aarch64", referenced from:
      randomx::JitCompilerA64::getDatasetInitFunc() in jit_compiler_a64.cpp.o
  "_randomx_init_dataset_aarch64_end", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64", referenced from:
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::JitCompilerA64() in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::getDatasetInitFunc() in jit_compiler_a64.cpp.o
      __GLOBAL__sub_I_jit_compiler_a64.cpp in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_cacheline_align_mask1", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_cacheline_align_mask2", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_imul_rcp_literals_end", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_light_cacheline_align_mask", referenced from:
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_light_dataset_offset", referenced from:
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_main_loop", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_update_spMix1", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_vm_instructions", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_vm_instructions_end", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
  "_randomx_program_aarch64_vm_instructions_end_light", referenced from:
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1570: xmrig-notls.app/xmrig-notls] Error 1
make[2]: Leaving directory '/Users/user/github/xmrig/build_iphone_evo'
make[1]: *** [CMakeFiles/Makefile2:76: CMakeFiles/xmrig-notls.dir/all] Error 2
make[1]: Leaving directory '/Users/user/github/xmrig/build_iphone_evo'
make: *** [Makefile:84: all] Error 2
```

Is this any help?

## resistor4u | 2019-11-13T17:51:01+00:00
@SChernykh PR #1277 seems to have made significant progress, but it fails at the very last. I reverted the changes I mentioned above, and here's the latest output:
```
[100%] Linking CXX executable xmrig-notls.app/xmrig-notls
Undefined symbols for architecture arm64:
  "___clear_cache", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<16ul>(randomx::SuperscalarProgram (&) [16ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in jit_compiler_a64.cpp.o
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in jit_compiler_a64.cpp.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1570: xmrig-notls.app/xmrig-notls] Error 1
make[1]: *** [CMakeFiles/Makefile2:76: CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

## resistor4u | 2019-12-01T21:37:28+00:00
@SChernykh @xmrig 
I fixed the build!!! The builtin calls must be changed from `ios_HOST_OS` to `__APPLE__` here https://github.com/xmrig/xmrig/blob/84ebf9d37244172220c2697de98edf80615eccd2/src/crypto/randomx/jit_compiler_a64.cpp#L106 and https://github.com/xmrig/xmrig/blob/84ebf9d37244172220c2697de98edf80615eccd2/src/crypto/randomx/jit_compiler_a64.cpp#L112

Then, critically, we must add an include to the same file, which I did at line 107. (I just added an absolute path b/c I'm not a programmer. There's probably a better way to include this?)
```
#include </Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/usr/include/libkern/OSCacheControl.h>
```

The produces an executable binary. However, there's a `Bus error` when trying to execute it.
```
iPhone:~ root$ ./xmrig-notls -o xome.pool.poolface:1000 -u someuser@gmail.com
 * ABOUT        XMRig/5.1.0-dev clang/10.0.0
 * LIBS         libuv/2.0.0-dev
 * CPU          ARMv8 (1) x64 AES
                threads:2
 * MEMORY       1.8/2.0 GB (94%)
 * DONATE       5%
 * POOL #1      xome.pool.poolface:1000 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-12-01 14:25:55.911]  net  use pool xome.pool.poolface:1000  xx.xx.xxx.xxxx
[2019-12-01 14:25:55.912]  net  new job from xome.pool.poolface:1000 diff 1000 algo rx/0 height 1979499
[2019-12-01 14:25:55.912]  rx   init dataset algo rx/0 (2 threads) seed 993ba25f61d47e1e...
[2019-12-01 14:25:55.912]  rx   not enough memory for RandomX dataset
[2019-12-01 14:25:55.913]  rx   failed to allocate RandomX dataset, switching to slow mode (1 ms)
[2019-12-01 14:25:58.767]  rx   dataset ready (2854 ms)
[2019-12-01 14:25:58.767]  cpu  use profile  *  (1 thread) scratchpad 2048 KB
[2019-12-01 14:25:58.769]  cpu  READY threads 1/1 (1) huge pages 0% 0/1 memory 2048 KB (2 ms)
Bus error: 10
iPhone:~ root$ 
```

So, how can I go about parsing the bus error?

## SChernykh | 2019-12-01T21:52:25+00:00
It's hard to say what causes bus error, probably JIT compiler doesn't account for some iPhone CPU requirements, or Apple's clang generates code which doesn't fit together with JIT generated code.

## resistor4u | 2020-01-14T17:32:13+00:00
@SChernykh @xmrig update for b5fb96dca081121c9b3519a1e6188707916add98:

Using the same workaround described above, when I run the binary I get similar failure:
```
 * ABOUT        XMRig/5.5.2-dev clang/10.0.0
 * LIBS         libuv/2.0.0-dev
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (1) x64 AES
                threads:2
 * MEMORY       1.8/2.0 GB (93%)
 * DONATE       5%
 * POOL #1      xmr.pool.minergate.com:45700 algo auto
 * COMMANDS     hashrate, pause, resume
[2020-01-14 10:15:43.411] [xmr.pool.minergate.com:45700] connect error: "connection timed out"
[2020-01-14 10:16:09.343] [xmr.pool.minergate.com:45700] connect error: "connection timed out"
[2020-01-14 10:16:38.886]  net  use pool xmr.pool.minergate.com:45700  136.243.102.154
[2020-01-14 10:16:38.886]  net  new job from xmr.pool.minergate.com:45700 diff 2000 algo rx/0 height 2011197
[2020-01-14 10:16:38.886]  rx   init dataset algo rx/0 (2 threads) seed 8d3b98130fa15d16...
[2020-01-14 10:16:38.886]  rx   not enough memory for RandomX dataset
[2020-01-14 10:16:38.887]  rx   failed to allocate RandomX dataset, switching to slow mode (1 ms)
[2020-01-14 10:16:40.866]  rx   dataset ready (1979 ms)
[2020-01-14 10:16:40.866]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
Bus error: 10
```

Do you have suggestions how I can go about debugging the problem? It seems that an android user is getting a similar problem: https://github.com/xmrig/xmrig/issues/1481

## SChernykh | 2020-01-14T18:29:08+00:00
`MEMORY       1.8/2.0 GB (93%)`
You need to have more free memory before starting the miner.

## resistor4u | 2020-01-15T20:54:05+00:00
even if specifying slow mode??

## resistor4u | 2020-08-17T09:18:13+00:00
@SChernykh in #1801 you reported:
> I've checked the latest code and it compiles fine on my Android phone and on my RPi3b+. I don't have any other ARM devices to test with. You probably need to try newer compiler - I have GCC 8.3.0 on RPi3b+ and clang 8.0.1 on the phone.

I've compiled latest releases for iphone 11, which has 4gb ram, and I'm getting the same bus errors. I began suspecting it was a `clang` issue because I got the same errors on my RPi3b+ (running 64bit ubuntu 18). The Pi only has 1gb memory and the gcc4 and gcc7 builds execute fine, but both clang7 and clang9 builds fail with bus error. Here's the output of most recent attempt executing on the new iphone11:
```
 * ABOUT        XMRig/6.3.2-dev clang/10.0.1
 * LIBS         libuv/2.0.0-dev
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARMv8 (1) x64 AES
                threads:6
 * MEMORY       2.9/3.8 GB (78%)
 * DONATE       1%
 * POOL #1      xmr.pool.minergate.com:45700 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2020-08-17 02:11:26.588]  net      xmr.pool.minergate.com:45700 connect error: "operation canceled"
[2020-08-17 02:11:51.960]  net      xmr.pool.minergate.com:45700 connect error: "operation canceled"
[2020-08-17 02:11:57.877]  net      use pool xmr.pool.minergate.com:45700  49.12.80.38
[2020-08-17 02:11:57.877]  net      new job from xmr.pool.minergate.com:45700 diff 1000 algo rx/0 height 2166293
[2020-08-17 02:11:57.877]  cpu      use argon2 implementation default
[2020-08-17 02:11:57.877]  randomx  init dataset algo rx/0 (6 threads) seed 270c0cfdd8c22818...
[2020-08-17 02:11:57.879]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (2 ms)
Bus error: 10
```
With that much free memory, is low mem really the cause of the `bus error: 10`? Since you've got a working build on android, any insight to help get a working iOS build?

## SChernykh | 2020-10-14T15:08:32+00:00
You'll have to edit source code to disable JIT, but running without JIT is too slow even on desktop PCs. You'll get less than 10 h/s on smartphones without JIT.

## Saikatsaha1996 | 2020-10-14T15:32:09+00:00
> You'll have to edit source code to disable JIT, but running without JIT is too slow even on desktop PCs. You'll get less than 10 h/s on smartphones without JIT.

Can you please tell me ? Why my JIT showing 0% ? How can i solve it?..I got hash rate in my mobile 350 h/s how can i solve ?..![Screenshot_20201014-205920.png](https://user-images.githubusercontent.com/72664192/96011414-8111aa80-0e60-11eb-9968-57f280445f9f.png)

# Action History
- Created by: resistor4u | 2019-10-17T18:31:08+00:00
- Closed at: 2021-04-12T15:05:15+00:00
