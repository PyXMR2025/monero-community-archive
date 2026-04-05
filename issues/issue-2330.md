---
title: Problem building for freebsd arm64
source_url: https://github.com/xmrig/xmrig/issues/2330
author: NoResponse13
assignees: []
labels:
- bug
created_at: '2021-04-29T17:57:05+00:00'
updated_at: '2021-12-19T15:43:57+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:43:57+00:00'
---

# Original Description
```
root@generic:~/xmrig/build # uname -a
FreeBSD generic 13.0-RELEASE FreeBSD 13.0-RELEASE #0 releng/13.0-n244733-ea31abc261f: Fri Apr  9 06:10:43 UTC 2021     root@releng1.nyi.freebsd.org:/usr/obj/usr/src/arm64.aarch64/sys/GENERIC  arm64
```

```
root@generic:~/xmrig/build # cmake ..
-- The C compiler identification is Clang 11.0.1
-- The CXX compiler identification is Clang 11.0.1
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
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/local/lib/libhwloc.so
-- Found UV: /usr/local/lib/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/local/lib/libcrypto.so (found version "1.1.1k")
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
```

```
root@generic:~/xmrig/build # make -j4
Scanning dependencies of target ethash
Scanning dependencies of target argon2
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
...
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o
/root/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp:31:13: fatal error: 'asm/hwcap.h' file not found
#   include <asm/hwcap.h>
            ^~~~~~~~~~~~~
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
1 error generated.
--- CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o ---
*** [CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o] Error code 1
...

```

# Discussion History
## RS102839 | 2021-04-30T16:02:17+00:00
You are getting further than people trying to build for the arm64 on the Mac M1, as at least your scripts are recognizing:
    
    -- Use ARM_TARGET=8 (aarch64)
    -- Performing Test XMRIG_ARM_CRYPTO
    -- Performing Test XMRIG_ARM_CRYPTO - Success

...watching this thread for hints on solving the M1 arm64 build problem. 

## Spudz76 | 2021-04-30T19:03:25+00:00
Disable OpenCL and CUDA (using cmake args `-DWITH_OPENCL=OFF -DWITH_CUDA=OFF`)

## NoResponse13 | 2021-05-01T10:00:36+00:00
> 
> 
> Disable OpenCL and CUDA (using cmake args `-DWITH_OPENCL=OFF -DWITH_CUDA=OFF`)

```
root@generic:~/xmrig/build # rm -rf ./*
root@generic:~/xmrig/build # ls
root@generic:~/xmrig/build #`
root@generic:~/xmrig/build # cmake .. -DWITH_OPENCL=OFF -DWITH_CUDA=OFF
-- The C compiler identification is Clang 11.0.1
-- The CXX compiler identification is Clang 11.0.1
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
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/local/lib/libhwloc.so
-- Found UV: /usr/local/lib/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Found OpenSSL: /usr/local/lib/libcrypto.so (found version "1.1.1k")
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
root@generic:~/xmrig/build #

```

```
root@generic:~/xmrig/build # make -j4
-- Use ARM_TARGET=8 (aarch64)
-- WITH_MSR=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
Scanning dependencies of target ethash
Scanning dependencies of target argon2
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  2%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
...
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
/root/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp:31:13: fatal error: 'asm/hwcap.h' file not found
#   include <asm/hwcap.h>
            ^~~~~~~~~~~~~
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
1 error generated.
--- CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o ---
*** [CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o] Error code 1

make[2]: stopped in /root/xmrig/build
In file included from /root/xmrig/src/core/config/ConfigTransform.cpp:20:
/root/xmrig/src/core/config/ConfigTransform.h:43:10: warning: private field 'm_opencl' is not used [-Wunused-private-field]
    bool m_opencl           = false;
         ^
1 warning generated.
1 error

make[2]: stopped in /root/xmrig/build
--- CMakeFiles/xmrig.dir/all ---
...

```

## Spudz76 | 2021-05-02T05:22:38+00:00
This might help that part, for FreeBSD 12 or higher (noting you have 13)
[arm64-fbsd-try1.patch.txt](https://github.com/xmrig/xmrig/files/6410808/arm64-fbsd-try1.patch.txt)


## NoResponse13 | 2021-05-03T03:47:07+00:00
patch workerd. but need append 
```
#   if __ARM_FEATURE_CRYPTO
-#   if !defined(__APPLE__)
+#   if !defined(__APPLE__) && !defined(__FreeBSD__)
    m_flags.set(FLAG_AES, getauxval(AT_HWCAP) & HWCAP_AES);
#   else
    m_flags.set(FLAG_AES, true);
#   endif
#   endif
```

only 2 warrnings
```
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
/root/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp:36:12: warning: 'HWCAP_AES' macro redefined [-Wmacro-redefined]
#   define HWCAP_AES (1 << 3)
           ^
/usr/include/machine/elf.h:98:9: note: previous definition is here
#define HWCAP_AES               0x00000008
        ^
...
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/hw/dmi/DmiBoard.cpp.o
In file included from /root/xmrig/src/hw/api/HwApi.cpp:26:
/root/xmrig/src/hw/dmi/DmiReader.h:35:1: warning: 'DmiReader' defined as a class here but previously declared as a struct; this is valid, but may result in linker errors under the Microsoft C++ ABI [-Wmismatched-tags]
class DmiReader
^
/root/xmrig/src/hw/api/HwApi.h:32:1: note: did you mean class here?
struct DmiReader;
^~~~~~
class
```


## SChernykh | 2021-05-03T07:58:56+00:00
@NoResponse13 This is because `getauxval` is not available on FreeBSD on ARM. Can you try this better fix: https://github.com/xmrig/xmrig/pull/2340 ?

## NoResponse13 | 2021-05-03T16:22:54+00:00
perfect

# Action History
- Created by: NoResponse13 | 2021-04-29T17:57:05+00:00
- Closed at: 2021-12-19T15:43:57+00:00
