---
title: msys2 erro
source_url: https://github.com/xmrig/xmrig/issues/1412
author: axsoftshi
assignees: []
labels: []
created_at: '2019-12-13T13:09:12+00:00'
updated_at: '2021-04-12T15:09:53+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:09:53+00:00'
---

# Original Description
# cmake .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-- The C compiler identification is GNU 9.1.0
-- The CXX compiler identification is GNU 9.1.0
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Check for working C compiler: /usr/bin/cc.exe
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Check for working C compiler: /usr/bin/cc.exe -- works
-- Detecting C compiler ABI info
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/CC.exe
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Check for working CXX compiler: /usr/bin/CC.exe -- works
-- Detecting CXX compiler ABI info
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Looking for syslog.h - found
-- Found HWLOC: c:/xmrig-deps/gcc/x64/lib/libhwloc.a
-- Found UV: c:/xmrig-deps/gcc/x64/lib/libuv.a
-- Looking for __builtin___clear_cache
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Looking for __builtin___clear_cache - found
-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_sse2_NOFLAG - Success
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_ssse3_FLAG - Success
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_xop_FLAG - Success
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_avx2_FLAG - Success
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
System is unknown to cmake, create:
Platform/MINGW64_NT-6.1-7600 to use this system, please send your config file to cmake@www.cmake.org so it can be added to cmake
-- Performing Test FEATURE_avx512f_FLAG - Success
-- argon2: feature 'avx512f' detected!
CMake Error at /usr/share/cmake-3.15.5/Modules/FindOpenSSL.cmake:347 (file):
  file STRINGS file
  "/home/Administrator/xmrig/c:/xmrig-deps/gcc/x64/include/openssl/opensslv.h"
  cannot be read.
Call Stack (most recent call first):
  cmake/OpenSSL.cmake:13 (find_package)
  CMakeLists.txt:178 (include)


-- Found OpenSSL: c:/xmrig-deps/gcc/x64/lib/libcrypto.a
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc.exe
-- Configuring incomplete, errors occurred!
See also "/home/Administrator/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "/home/Administrator/xmrig/build/CMakeFiles/CMakeError.log".


# Discussion History
## axsoftshi | 2019-12-13T13:14:56+00:00
@xmrig 

## axsoftshi | 2019-12-13T13:15:28+00:00
Scanning dependencies of target xmrig-asm
[  0%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
[  1%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
[  1%] Linking C static library libxmrig-asm.a
[  1%] Built target xmrig-asm
Scanning dependencies of target argon2-avx2
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.obj
[  2%] Linking C static library libargon2-avx2.a
[  2%] Built target argon2-avx2
Scanning dependencies of target argon2-ssse3
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-ssse3.dir/arch/x86_64/lib/argon2-ssse3.c.obj
[  3%] Linking C static library libargon2-ssse3.a
[  3%] Built target argon2-ssse3
Scanning dependencies of target argon2-sse2
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.obj
[  4%] Linking C static library libargon2-sse2.a
[  4%] Built target argon2-sse2
Scanning dependencies of target argon2-xop
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-xop.dir/arch/x86_64/lib/argon2-xop.c.obj
[  5%] Linking C static library libargon2-xop.a
[  5%] Built target argon2-xop
Scanning dependencies of target argon2-avx512f
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.obj
[  6%] Linking C static library libargon2-avx512f.a
[  6%] Built target argon2-avx512f
Scanning dependencies of target argon2
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.obj
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.obj
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.obj
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.obj
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.obj
[  8%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.obj
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/argon2-arch.c.obj
[  9%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/x86_64/lib/cpu-flags.c.obj
[ 10%] Linking C static library libargon2.a
[ 10%] Built target argon2
Scanning dependencies of target xmrig-notls
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o
In file included from /home/Administrator/xmrig/src/base/io/Console.cpp:26:
/home/Administrator/xmrig/src/base/io/Console.h:32:10: 致命错误：uv.h：No such file or directory
   32 | #include <uv.h>
      |          ^~~~~~
编译中断。
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:89：CMakeFiles/xmrig-notls.dir/src/base/io/Console.cpp.o] 错误 1
make[1]: *** [CMakeFiles/Makefile2:116：CMakeFiles/xmrig-notls.dir/all] 错误 2
make: *** [Makefile:84：all] 错误 2


## axsoftshi | 2019-12-13T13:16:08+00:00
I disabled the SSL option. It's good again, but make is wrong

## 2010phenix | 2019-12-13T13:50:00+00:00
https://github.com/xmrig/xmrig/wiki/Windows-Build

## axsoftshi | 2019-12-13T13:51:27+00:00
> https://github.com/xmrig/xmrig/wiki/Windows-Build

I downloaded the new dependency according to the above 

## axsoftshi | 2019-12-13T13:52:18+00:00
Xmrig DEPs is also the latest

# Action History
- Created by: axsoftshi | 2019-12-13T13:09:12+00:00
- Closed at: 2021-04-12T15:09:53+00:00
