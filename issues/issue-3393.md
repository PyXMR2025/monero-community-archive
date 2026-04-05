---
title: 'Error: unknown pseudo-op: `.intel_syntax'''
source_url: https://github.com/xmrig/xmrig/issues/3393
author: furkanonder
assignees: []
labels:
- RISC-V
created_at: '2023-12-27T11:04:15+00:00'
updated_at: '2025-06-18T22:25:29+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:25:29+00:00'
---

# Original Description
```
ubuntu@ubuntu:~$ git clone https://github.com/xmrig/xmrig
ubuntu@ubuntu:~$ mkdir xmrig/build && cd xmrig/build
ubuntu@ubuntu:~/xmrig/build$ cmake ..
```
Output:
```
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 13.2.0
-- The CXX compiler identification is GNU 13.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/riscv64-linux-gnu/libhwloc.so  
-- Found UV: /usr/lib/riscv64-linux-gnu/libuv.so  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=ON
CMake Deprecation Warning at src/3rdparty/argon2/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Failed
-- Performing Test FEATURE_sse2_FLAG
-- Performing Test FEATURE_sse2_FLAG - Failed
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
-- Performing Test FEATURE_ssse3_FLAG - Failed
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Failed
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
-- Performing Test FEATURE_avx2_FLAG - Failed
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
-- Performing Test FEATURE_avx512f_FLAG - Failed
CMake Deprecation Warning at src/3rdparty/libethash/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


CMake Deprecation Warning at src/crypto/ghostrider/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Found OpenSSL: /usr/lib/riscv64-linux-gnu/libcrypto.so (found version "3.0.10")  
-- The ASM compiler identification is GNU
-- Found assembler: /usr/bin/cc
-- Configuring done (4.3s)
-- Generating done (0.3s)
-- Build files have been written to: /home/ubuntu/xmrig/build
```

```sh
ubuntu@ubuntu:~/xmrig/build$ make -j$(nproc)
```
Output:
```
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o
cc: error: unrecognized command-line option ‘-maes’
cc: error: unrecognized command-line option ‘-maes’
cc: error: unrecognized command-line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/build.make:76: src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o] Error 1
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/build.make:76: src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o] Error 1
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:76: src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:286: src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:208: src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:368: src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
[  2%] Building ASM object CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o
/home/ubuntu/xmrig/src/crypto/cn/asm/cn_main_loop.S: Assembler messages:
/home/ubuntu/xmrig/src/crypto/cn/asm/cn_main_loop.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/ubuntu/xmrig/src/crypto/cn/asm/cn_main_loop.S:25: Warning: alignment too large: 63 assumed

as: out of memory allocating 9223372036854841462 bytes after a total of 135168 bytes
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:75: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/home/ubuntu/xmrig/src/crypto/cn/asm/CryptonightR_template.S: Assembler messages:
/home/ubuntu/xmrig/src/crypto/cn/asm/CryptonightR_template.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/ubuntu/xmrig/src/crypto/cn/asm/CryptonightR_template.inc:13: Warning: alignment too large: 63 assumed

as: out of memory allocating 9223372036854841462 bytes after a total of 270336 bytes
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:88: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:148: CMakeFiles/xmrig-asm.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
ubuntu@ubuntu:~/xmrig/build$ 
```

## Enviroment
```
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.5.0-14-generic #14.1-Ubuntu SMP Fri Nov 24 06:09:26 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
```

# Discussion History
## SChernykh | 2023-12-27T13:51:56+00:00
RISC-V is not supported yet.

## Apetree100122 | 2024-01-02T12:07:18+00:00
[  1
%] Building 
C object src
/3rdparty
/libethash
/CMakeFiles/ethash.dir/
ethash_internal.c.o
[  1
%] Building C ob
ject src/3rdparty/argon2
/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o
[  1
%] Building C object 
src/3rdparty/argon2/CMakeFiles
/argon2-avx2.dir/arch/x86_64/lib/argon2-avx2.c.o
[  2
%] Building ASM object 
CMakeFiles/xmrig-asm.dir/
src/crypto/cn/asm/cn_main_loop.S.o
cc: error: unrecognized
 command-line option ‘-maes’
cc: error: unrecognized
 command-line option ‘-maes’
cc: error: unrecognized
 command-line option ‘-maes’
make[2]: 
*** [src/3rdparty
/argon2/CMakeFiles
/argon2-sse2.dir
/build.make:76: src/3rdparty/argon2/
CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o] Error 1
make[
2]:
 *** [src/3rdparty/
argon2/CMakeFiles
/argon2-avx2.dir/build.make:7
6: src
/3rdparty/argon2/
CMakeFiles
/argon2-avx2.
dir/arch
/x86_ 
64/lib
/argon2-avx2.c.o] Error 1
make[2] 
: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:76: src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.
o] Error 1
make[1]: 
*** [CMakeFiles/Makefile2:286: src/3rdparty/argon2/CMakeFiles/argon2-avx2.dir/all] Error 2
make[1]: 
*** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:208: src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/all] 
Error 2
make[1]: *** [
CMakeFiles/Makefile
2:368: src/3rdparty/
libethash/CMakeFiles/ethash.dir/all]
 Error 2
[  2
%] Building ASM o
bject CMakeFiles
/xmrig-asm.dir/sr
c/cr
ypto/
cn/asm/CryptonightR_template.S.o
/home/ubuntu
/xmrig/src/crypto/cn/asm/cn_main_loop.S: Assembler messages:
/home/ubuntu/xmrig/src/crypto/cn/asm/cn_main_loop.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/ubuntu/xmrig/src/crypto/cn/asm/cn_main_loop.S:25: Warning: alignment too large:p
 63 assumed

as: out of memory allocating 9223372036854841462 bytes after a total of 1
35168 bytes
make[2]:
 *** [CMakeFiles/xmrig-asm.dir/build.make:75: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/cn_main_loop.S.o] Erro
r 1
make[2]:
 *** Waiting for unfinished jobs....
/home/ubuntu/xmrig/src/crypto/cn/asm/
CryptonightR_template.S: Assembler messages:
/home/ubuntu/xmrig/src/crypto/cn/asm/CryptonightR_template.S:6: Error: unknown pseudo-op: `.intel_syntax'
/home/ubuntu/xmrig/src/crypto/cn/asm/CryptonightR_template.inc:13: Warning: alignment too large: 63 assumed
as: out of memory allocating 922
3372
0368
548
414
62 bytes after a total of 270
336 bytes
make[2]: *** [CMakeFiles/xmrig-asm.dir/build.make:88: CMakeFiles/xmrig-asm.dir/src/crypto/cn/asm/CryptonightR_template.S.o] Error 1
make[1]: 
*** [CMakeFiles/Makefile
2:148: CMakeFiles/xmrig-asm.dir/all] 
Error 2
make:
 *** 
[Makefile:
91:all]
 Error 2
ubuntu@ubuntu:                                               ~/  xmrig                                                         /build$ 

## Apetree100122 | 2024-01-02T12:11:43+00:00
ubuntu@ubuntu:~$ git clone 
https://github.com/xmrig/xmrig
ubuntu@ubuntu:~
$ mkdir xmrig/build 
&& cd xmrig/build
ubuntu@ubuntu:~/
xmrig/build$ cmake ..
CMake Deprecation
 Warning at CMakeLists.
txt:1 (cmake_
minimum_required):
  Compatibility with 
CMake < 3.5 will be removed from 
a future version of
CMake.

  Update the V
ERSION argument 
<min> value or use a  <max> 
suffix to tell
  CMake that the 
project does not need 
compatibility with older versions.


-- The C compiler identification is GNU
 1
3.2.
0-- The CXX compiler 
identification is
 GNU
 1
3.2.0
-- Detecting
 C compiler 
ABI info
-- Detecting
 C compile
 ABI info - 
done
-- Check for working C compiler: 
/usr/bin/cc -
skipped-- Detecting C c
ompile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Performing Test VAES_SUPPORTED
-- Performing Test VAES_SUPPORTED - Failed
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/riscv64-linux-gnu/libhwloc.so  
-- Found UV: /usr/lib/riscv64-linux-gnu/libuv.so  
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=ON
CMake Deprecation Warning at src/3rdparty/argon2/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Failed
-- Performing Test FEATURE_sse2_FLAG
-- Performing Test FEATURE_sse2_FLAG - Failed
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
-- Performing Test FEATURE_ssse3_FLAG - Failed
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Failed
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
-- Performing Test FEATURE_avx2_FLAG - Failed
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
-- Performing Test FEATURE_avx512f_FLAG - Failed
CMake Deprecation Warning at src/3rdparty/libethash/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


CMake Deprecation Warning at src/crypto/ghostrider/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Found OpenSSL: /usr/lib/riscv64-linux-gnu/libcrypto.so 
(found version 
"3.0.10")  
-- The AS
M compiler identification is
 GNU
-- Found assembler: /usr
/bin/cc
-- Configuring done (4.3s)-- Generating done (0.3s)- Build files havebeen 
written to: /home/ubuntu/xmrig/build

# Action History
- Created by: furkanonder | 2023-12-27T11:04:15+00:00
- Closed at: 2025-06-18T22:25:29+00:00
