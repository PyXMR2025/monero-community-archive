---
title: Centos 7 ARM (qemu) compilation error
source_url: https://github.com/xmrig/xmrig/issues/2596
author: Omnividente
assignees: []
labels: []
created_at: '2021-09-22T11:23:25+00:00'
updated_at: '2021-11-16T13:04:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello everyone, I'm trying to compile XMRIG for ARM. I get the following error:
```
cmake3 .. -DXMRIG_DEPS=scripts/deps -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -```
DWITH_CN_FEMTO=OFF -DWITH_ARGON2=OFF -DWITH_ASTROBWT=OFF -DWITH_KAWPOW=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_ADL=OFF -DWITH_BENCHMARK=OFF
-- The C compiler identification is GNU 9.4.0
-- The CXX compiler identification is GNU 9.4.0
-- Check for working C compiler: /usr/local/bin/gcc
-- Check for working C compiler: /usr/local/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/local/bin/g++
-- Check for working CXX compiler: /usr/local/bin/g++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=8 (aarch64)
-- Performing Test XMRIG_ARM_CRYPTO
-- Performing Test XMRIG_ARM_CRYPTO - Success
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /root/xmrig/scripts/deps/lib/libhwloc.a
-- Found UV: /root/xmrig/scripts/deps/lib/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- WITH_MSR=OFF
-- Found OpenSSL: /root/xmrig/scripts/deps/lib/libcrypto.a (found version "1.1.1l")
-- Configuring done
-- Generating done
-- Build files have been written to: /root/xmrig/build
```
```


make -j$(nproc)
...........................................................................................
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
In file included from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/root/xmrig/src/crypto/randomx/randomx.h:160:1: error: template with C linkage
  160 | template<typename T>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:69:1: error: template with C linkage
   69 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:102:1: error: template with C linkage
  102 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:121:1: error: template with C linkage
  121 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:145:1: error: template with C linkage
  145 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:219:1: error: template with C linkage
  219 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:227:1: error: template with C linkage
  227 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:348:1: error: template with C linkage
  348 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:367:1: error: template with C linkage
  367 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:380:1: error: template with C linkage
  380 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:409:1: error: template specialization with C linkage
  409 | template<>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:431:1: error: template with C linkage
  431 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:449:1: error: template with C linkage
  449 | template<size_t N>
      | ^~~~~~~~
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/root/xmrig/src/backend/cpu/CpuWorker.cpp:487:1: error: expected ‘}’ at end of input
  487 | } // namespace xmrig
      | ^
In file included from /root/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig/src/crypto/randomx/randomx.h:35,
                 from /root/xmrig/src/backend/cpu/CpuWorker.cpp:41:
/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h:33:12: note: to match this ‘{’
   33 | extern "C" {
      |            ^
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
make[2]: *** [CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
 

# Discussion History
## SChernykh | 2021-09-22T12:07:33+00:00
Something is wrong with you GCC install, specifcally with `/usr/local/lib/gcc/aarch64-unknown-linux-gnu/9.4.0/include/arm_acle.h`

## kckndrgn | 2021-11-16T13:04:49+00:00
I just had the same issue.  In the arm_acle.h file there are two  open curly brackets and one close bracket for the #ifdef __cplusplus logic.
I commented out the second open bracket (3lines) and xmrig was able to compile on my NanoPi M4 board.  
At line 101 comment out:
#ifdef __cplusplus
extern "C" {
#endif

gcc version is 9.4.0, running on a NanoPi M4.

Hope this helps

# Action History
- Created by: Omnividente | 2021-09-22T11:23:25+00:00
