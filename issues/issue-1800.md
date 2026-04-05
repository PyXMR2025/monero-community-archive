---
title: 'ARM8 compiling error '
source_url: https://github.com/xmrig/xmrig/issues/1800
author: ldmatev
assignees: []
labels:
- arm
created_at: '2020-08-05T07:10:36+00:00'
updated_at: '2022-07-15T19:16:23+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:51:02+00:00'
---

# Original Description
**Describe the bug**
Error during compiling on Android (Arm8) with termux 


**To Reproduce**
Install termux
Open termux
git clone https://github.com/xmrig/xmrig.git
cd xmrig && mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DARM_TARGET=8 -DWITH_OPENCL=OFF
-DWITH_CUDA=OFF -DWITH_HWLOC=OFF
make

**Expected behavior**
Compiling 100%

**Required
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp:51:49: error:
      use of undeclared identifier 'HWCAP_AES'
  ...getauxval(AT_HWCAP) & HWCAP_AES);
                           ^
1 error generated.
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1187: CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:137: CMakeFiles/xmrig-notls.dir/all] Error 2
**Additional context**
Add any other context about the problem here.


# Discussion History
## xmrig | 2020-08-05T09:57:25+00:00
What processor and android version are you using? Usually don't need specify `-DARM_TARGET=8`, if you try to build ARMv8 target on ARMv7 hardware result is undefined, this option suitable only if detection based on `CMAKE_SYSTEM_PROCESSOR` fails.

At your own risk you can replace `HWCAP_AES` with `(1 << 3)` or fully bypass runtime AES detection by `m_flags.set(FLAG_AES, true);` or `m_flags.set(FLAG_AES, false);` https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/platform/BasicCpuInfo_arm.cpp#L51

## ldmatev | 2020-08-05T12:26:46+00:00
> What processor and android version are you using? Usually don't need specify `-DARM_TARGET=8`, if you try to build ARMv8 target on ARMv7 hardware result is undefined, this option suitable only if detection based on `CMAKE_SYSTEM_PROCESSOR` fails.
> 
> At your own risk you can replace `HWCAP_AES` with `(1 << 3)` or fully bypass runtime AES detection by `m_flags.set(FLAG_AES, true);` or `m_flags.set(FLAG_AES, false);` https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/platform/BasicCpuInfo_arm.cpp#L51

Many thanks for your answer.
I'm using android 8.0 on Qualcomm Snapdragon 410 

I deleted previous dir.

I download again xmrig.

After:

Resolving deltas: 100% (14448/14448), done.
$ cd xmrig && mkdir build && cd build
$ cmake ..
-- The C compiler identification is Clang 10.0.1
-- The CXX compiler identification is Clang 10.0.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /data/data/com.termux/files/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /data/data/com.termux/files/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
CMake Error at /data/data/com.termux/files/usr/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:165 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /data/data/com.termux/files/usr/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:458 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:39 (include)


-- Configuring incomplete, errors occurred!
See also "/data/data/com.termux/files/home/xmrig/build/CMakeFiles/CMakeOutput.log".
$ cmake .. -DWITH_HWLOC=OFF
-- Found UV: /data/data/com.termux/files/usr/lib/libuv.so
-- Looking for _rotr
-- Looking for _rotr - not found
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=OFF
-- Found OpenSSL: /data/data/com.termux/files/usr/lib/libcrypto.so (found version "1.1.1g")
-- Configuring done
-- Generating done
-- Build files have been written to: /data/data/com.termux/files/home/xmrig/build

$ make
Scanning dependencies of target ethash
[  0%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  1%] Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/keccakf800.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  1%] Linking C static library libethash.a
[  1%] Built target ethash
Scanning dependencies of target cpuid
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[  4%] Linking C static library libcpuid.a
[  4%] Built target cpuid
Scanning dependencies of target argon2
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  6%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  7%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  7%] Linking C static library libargon2.a
[  7%] Built target argon2
Scanning dependencies of target xmrig
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Algorithm.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[  9%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/Coin.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/keccak.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/crypto/sha3.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/FileLogWriter.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Tags.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Signals.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
/data/data/com.termux/files/home/xmrig/src/base/kernel/config/BaseConfig.cpp:160:56: warning:
      adding 'int' to a string does not append to
      the string [-Wstring-plus-int]
  ...const char *v = OPENSSL_VERSION_TEXT + 8;
                     ~~~~~~~~~~~~~~~~~~~~~^~~
/data/data/com.termux/files/home/xmrig/src/base/kernel/config/BaseConfig.cpp:160:56: note:
      use array indexing to silence this warning
  ...const char *v = OPENSSL_VERSION_TEXT + 8;
                                          ^
                     &                    [  ]
1 warning generated.
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/Title.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
/data/data/com.termux/files/home/xmrig/src/base/kernel/Entry.cpp:87:56: warning:
      adding 'int' to a string does not append to
      the string [-Wstring-plus-int]
  ...const char *v = OPENSSL_VERSION_TEXT + 8;
                     ~~~~~~~~~~~~~~~~~~~~~^~~
/data/data/com.termux/files/home/xmrig/src/base/kernel/Entry.cpp:87:56: note:
      use array indexing to silence this warning
  ...const char *v = OPENSSL_VERSION_TEXT + 8;
                                          ^
                     &                    [  ]
1 warning generated.
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/NetworkState.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
clang-10: warning: argument unused during compilat

.....
Many other lines
...

 [ 76%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/AdvancedCpuInfo.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:34:
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:11:2: error:
      this header is for x86 only
#error this header is for x86 only
 ^
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:271:5: error:
      invalid output constraint '=a' in asm
    __cpuid(__leaf, __eax, __ebx, __ecx, __edx);
    ^
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:236:11: note:
      expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(...
          ^
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:286:5: error:
      invalid output constraint '=a' in asm
    __cpuid(__leaf, *__eax, *__ebx, *__ecx...
    ^
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:236:11: note:
      expanded from macro '__cpuid'
        : "=a"(__eax), "=r" (__ebx), "=c"(...
          ^
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:300:5: error:
      invalid output constraint '=a' in asm
    __cpuid_count(__leaf, __subleaf, *__ea...
    ^
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:243:11: note:
      expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(...
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:71:5: error:
      invalid output constraint '=a' in asm
    __cpuid_count(level, 0, output[0], out...
    ^
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:243:11: note:
      expanded from macro '__cpuid_count'
        : "=a"(__eax), "=r" (__ebx), "=c"(...
          ^
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:129:36: error:
      invalid output constraint '=a' in asm
    __asm__ __volatile__("xgetbv": "=a"(ea...
                                   ^
6 errors generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2058: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:159: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2
$ 

Thanks


## ldmatev | 2020-08-05T21:33:02+00:00
Ok, I installed ubuntu in termux.
Now i received this other error at 79%:

scope; did you mean ‘_mm_and_si128’?
  498 |             cx = _mm_aesenc_si128(cx, ax0;      |                  ~~~~~~~~~~~~~~~~^~~~~~~~
      |                  _mm_and_si128            /root/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_single_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = xmrig::Algorithm::CN_1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:                     /root/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here                                    /root/xmrig/src/crypto/cn/CryptoNight_arm.h:498:34: error: ‘_mm_aesenc_si128’ was not declared in this scope; did you mean ‘_mm_and_si128’?             498 |             cx = _mm_aesenc_si128(cx, ax0;      |                  ~~~~~~~~~~~~~~~~^~~~~~~~       |                  _mm_and_si128            /root/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = xmrig::Algorithm::CN_1; bool SOFT_AES = false; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:
/root/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here                                    /root/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope; did you mean ‘_mm_and_si128’?             670 |             cx0 = _mm_aesenc_si128(cx0, ax0);                                                     |                   ~~~~~~~~~~~~~~~~^~~~~~~~~~                                                      |                   _mm_and_si128           /root/xmrig/src/crypto/cn/CryptoNight_arm.h:671:35: error: ‘_mm_aesenc_si128’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
  671 |             cx1 = _mm_aesenc_si128(cx1, ax1);                                                     |                   ~~~~~~~~~~~~~~~~^~~~~~~~~~                                                /root/xmrig/src/crypto/cn/CryptoNight_arm.h: In instantiation of ‘void xmrig::cryptonight_double_hash(const uint8_t*, size_t, uint8_t*, cryptonight_ctx**, uint64_t) [with xmrig::Algorithm::Id ALGO = xmrig::Algorithm::CN_1; bool SOFT_AES = true; uint8_t = unsigned char; size_t = unsigned int; uint64_t = long long unsigned int]’:                     /root/xmrig/src/crypto/cn/CnHash.cpp:237:5:   required from here                                    /root/xmrig/src/crypto/cn/CryptoNight_arm.h:670:35: error: ‘_mm_aesenc_si128’ was not declared in this scope; did you mean ‘_mm_and_si128’?             670 |             cx0 = _mm_aesenc_si128(cx0, ax0);                                                     |                   ~~~~~~~~~~~~~~~~


## ldmatev | 2020-08-07T09:02:29+00:00
Hi, kindly reminder.


## offmarte | 2020-08-10T18:56:08+00:00
@ldmatev delete your build / release folder.
you don't need to install ubuntu.
**in termux do:**
- `pkg install apt` (if not installed already)
- `apt update`
- `apt install git build-essential cmake openssl clang` (just to make sure it's installed)
- then `apt update`
- `apt upgrade`
- `mkdir release && cd release`
- `cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_CUDA=Off -DWITH_OPENCL=Off -DWITH_HWLOC=Off`
- `make`

**EDIT:** pkg or apt wont find libssl-dev, try **openssl** and double check if **clang** is on _the newest version_

I've successfully built xmrig on my android 8.0 with snapdragon 615 armv8 device, It runs just fine but hashrate is 0 because my device only have 2GB RAM

## ldmatev | 2020-08-11T15:58:38+00:00
> @ldmatev delete your build / release folder.
> you don't need to install ubuntu.
> **in termux do:**
> 
> * `pkg install apt` (if not installed already)
> * `apt update`
> * `apt install git build-essential cmake openssl clang` (just to make sure it's installed)
> * then `apt update`
> * `apt upgrade`
> * `mkdir release && cd release`
> * `cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_CUDA=Off -DWITH_OPENCL=Off -DWITH_HWLOC=Off`
> * `make`
> 
> **EDIT:** pkg or apt wont find libssl-dev, try **openssl** and double check if **clang** is on _the newest version_
> 
> I've successfully built xmrig on my android 8.0 with snapdragon 615 armv8 device, It runs just fine but hashrate is 0 because my device only have 2GB RAM

Many thanks, other error:

root@localhost:~/xmrig/release# make              Scanning dependencies of target argon2            [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o                   cc: error: unrecognized command line option ‘-mae’make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:63: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1              make[1]: *** [CMakeFiles/Makefile2:185: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2      make: *** [Makefile:84: all] Error 2

## offmarte | 2020-08-11T23:13:58+00:00
try to disable argon2 (WITH_ARGON2) in CMakeLists.txt, you can disable it with the tag -DWITH_ARGON2=OFF, but it didn't always work -idk why-
i tried to build a generic executable for you, but it always fails in 100% due to libuv and i don't know how to disable it to not use libuv when compiling with dependencies.
i've successfully built it for local use tho

## ldmatev | 2020-08-12T08:56:19+00:00
> try to disable argon2 (WITH_ARGON2) in CMakeLists.txt, you can disable it with the tag -DWITH_ARGON2=OFF, but it didn't always work -idk why-
> i tried to build a generic executable for you, but it always fails in 100% due to libuv and i don't know how to disable it to not use libuv when compiling with dependencies.
> i've successfully built it for local use tho

Many thanks, it doesn't work.
I Tried to add in cmakelist file and also with 
cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_CUDA=Off -DWITH_OPENCL=Off -DWITH_HWLOC=Off -DWITH_ARGON2=OFF-
That add automarically this line:
DWITH_ARGON2:UNINITIALIZED=OFF
But i receive same error
root@localhost:~/xmrig/release# make              [  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o                   cc: error: unrecognized command line option ‘-mae’make[2]: ***[src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:63: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1              make[1]: *** [CMakeFiles/Makefile2:185: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2      make: *** [Makefile:84: all] Error 2              root@localhost:~/xmrig/release#

I can try to reinstall termux and repeat all steps with finger crossed 

## SChernykh | 2020-08-12T11:56:05+00:00
`unrecognized command line option ‘-mae’`

XMRig doesn't use such command line option for building, I think some files are changed or corrupt. You should sync everything from scratch

## ldmatev | 2020-08-13T05:58:38+00:00
> `unrecognized command line option ‘-mae’`
> 
> XMRig doesn't use such command line option for building, I think some files are changed or corrupt. You should sync everything from scratch

Yes. It's strange.
I reinstall again termux.
With command 

cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_CUDA=Off -DWITH_OPENCL=Off -DWITH_HWLOC=Off -DWITH_ARGON2=Off
I received:

[ 66%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/AdvancedCpuInfo.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo.cpp.o
clang-10: warning: argument unused during compilation: '-maes' [-Wunused-command-line-argument]
In file included from /data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:34:
/data/data/com.termux/files/usr/lib/clang/10.0.1/include/cpuid.h:11:2: error:
      this header is for x86 only
#error this header is for x86 only
 ^

So i tried:
cmake .. -DCMAKE_BUILD_TYPE=Release -DWITH_CUDA=Off -DWITH_OPENCL=Off -DWITH_HWLOC=Off -DWITH_ARGON2=Off -DARM_TARGET=8

So, new error:
c/crypto/common/VirtualMemory_unix.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
/data/data/com.termux/files/home/xmrig/src/backend/cpu/platform/BasicCpuInfo_arm.cpp:51:49: error:
      use of undeclared identifier 'HWCAP_AES'
  ...getauxval(AT_HWCAP) & HWCAP_AES);
                           ^
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1187: CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:137: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:103: all] Error 2

Thanks for your answers.

## m680 | 2021-01-15T11:25:27+00:00
Hello there, I Need some help to fix this issue with make :

root@raspberrypi:/home/pi/Desktop/xmrig/build# make
[  0%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
cc: error: unrecognized argument in option ‘-march=armv7l’
cc: note: valid arguments to ‘-march=’ are: armv2 armv2a armv3 armv3m armv4 armv4t armv5 armv5e armv5t armv5te armv6 armv6-m armv6j armv6k armv6s-m armv6t2 armv6z armv6zk armv7 armv7-a armv7-m armv7-r armv7e-m armv7ve armv8-a armv8-a+crc iwmmxt iwmmxt2 native
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2.dir/build.make:63: src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:129: src/3rdparty/argon2/CMakeFiles/argon2.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

root@raspberrypi:/home/pi/Desktop/xmrig/build# 

## jimbob1984 | 2021-05-26T11:42:49+00:00
> What processor and android version are you using? Usually don't need specify `-DARM_TARGET=8`, if you try to build ARMv8 target on ARMv7 hardware result is undefined, this option suitable only if detection based on `CMAKE_SYSTEM_PROCESSOR` fails.
> 
> At your own risk you can replace `HWCAP_AES` with `(1 << 3)` or fully bypass runtime AES detection by `m_flags.set(FLAG_AES, true);` or `m_flags.set(FLAG_AES, false);` https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/platform/BasicCpuInfo_arm.cpp#L51

Hi can you tell me how to edit the AES as per above i am a bit of a noob at this and i have got the install running up to 58% then same error. I am running an ARM8 processor on an andrion 8.1.0.

# Action History
- Created by: ldmatev | 2020-08-05T07:10:36+00:00
- Closed at: 2021-04-12T14:51:02+00:00
