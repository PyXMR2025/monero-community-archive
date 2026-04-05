---
title: Windows Compiler Error
source_url: https://github.com/xmrig/xmrig/issues/3672
author: MoneroArbo
assignees: []
labels: []
created_at: '2025-06-17T14:04:04+00:00'
updated_at: '2025-06-17T15:42:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
[100%] Linking CXX executable xmrig.exe
C:/msys64/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/xmrig-deps/gcc/x64/lib/libuv.a(libuv_
la-process.o): in function `_vsnwprintf_s_l':
C:/msys/ucrt64/include/sec_api/stdio_s.h:805:(.text+0x63b): undefined reference to `__local_stdio_printf_options'
C:/msys64/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/14.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/xmrig-deps/gcc/x64/lib/libhwloc.a(top
ology-xml-nolibxml.o): in function `hwloc_nolibxml_read_file':
C:/msys/home/xmrig/build/hwloc-2.12.1/hwloc/topology-xml-nolibxml.c:364:(.text+0x4dd): undefined reference to `stat64i32'
collect2.exe: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:4102: xmrig.exe] Error 1
make[1]: *** [CMakeFiles/Makefile2:213: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
```

Followed the instructions for MSYS2 at https://xmrig.com/docs/miner/build/windows

Tried to build xmrig v6.23.0 as well as master, got the same error. Ubuntu build on the same machine goes fine.

# Discussion History
## xmrig | 2025-06-17T14:51:05+00:00
Likely need to redownload xmrig-deps if it does not help fully clear the build directory. As mentioned, in #3668, the build system switched to ucrt, which led to compatibility issues like this. It should be fine if built from scratch.
Thank you.

## MoneroArbo | 2025-06-17T14:55:30+00:00
Hey thanks for the quick response. I was indeed using old xmrig-deps at first. However, I have now downloaded new xmrig-deps, made sure msys2 was the latest (20250221), got the latest cmake (4.03), nuked the entire xmrig directory, and also double checked I was using ucrt64, but still get the above error.

results from cmake:

```
$ "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
-- The C compiler identification is GNU 14.2.0
-- The CXX compiler identification is GNU 14.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: C:/msys64/ucrt64/bin/cc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: C:/msys64/ucrt64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Success
-- Found HWLOC: C:/xmrig-deps/gcc/x64/lib/libhwloc.a
-- Found UV: C:/xmrig-deps/gcc/x64/lib/libuv.a
-- Looking for _aligned_malloc
-- Looking for _aligned_malloc - found
-- WITH_MSR=ON
-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Success
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
-- Performing Test FEATURE_ssse3_FLAG - Success
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Success
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
-- Performing Test FEATURE_avx2_FLAG - Success
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
-- Performing Test FEATURE_avx512f_FLAG - Success
-- argon2: feature 'avx512f' detected!
-- Found OpenSSL: C:/xmrig-deps/gcc/x64/lib/libcrypto.a (found version "3.0.16")
-- The ASM compiler identification is GNU
-- Found assembler: C:/msys64/ucrt64/bin/cc.exe
-- Configuring done (14.5s)
-- Generating done (0.4s)
-- Build files have been written to: C:/msys64/home/user/xmrig/build
```


## xmrig | 2025-06-17T15:11:14+00:00
Dependencies need to be as latest as Yesterday's latest. I taged it to make it less confusing https://github.com/xmrig/xmrig-deps/releases/tag/v25.06.16

Or maybe your MSYS2 installation needs an update https://www.msys2.org/docs/updating/ dependencies built with GCC 15.1.0. I usually build dependencies with relatively old GCC to maximize compatibility, but not in this case.
Thank you.

## MoneroArbo | 2025-06-17T15:34:22+00:00
Ok I made sure msys2 was up to date (pacman -Suy), downloaded the deps from your v25.06.16 tag and put them in place, nuked the xmrig folder to start over again, but unfortunately keep getting the same error.

I can try on a fresh machine, but at this point I'm not sure what on my end could be the issue. I did change all my Windows 10 Pro installs to Windows 10 LTSC since the last time I built xmrig, if that could make a difference.

## xmrig | 2025-06-17T15:42:40+00:00
No ideas anymore, as failback you use `mingw64.exe` with `mingw-w64-x86_64-gcc` and older deps https://github.com/xmrig/xmrig-deps/releases/tag/v5.0

# Action History
- Created by: MoneroArbo | 2025-06-17T14:04:04+00:00
