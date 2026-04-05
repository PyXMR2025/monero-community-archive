---
title: 'Build Error: error:template with C linkage， note: ‘extern "C"’ linkage started
  here '
source_url: https://github.com/xmrig/xmrig/issues/2978
author: avselang
assignees: []
labels:
- bug
created_at: '2022-03-19T02:53:49+00:00'
updated_at: '2022-04-03T07:49:28+00:00'
type: issue
status: closed
closed_at: '2022-04-03T07:49:16+00:00'
---

# Original Description
**Describe the bug**
When trying to build (using the steps in both basic and advanced build) I get a build error:error: template with C linkage

**To Reproduce**
On ubuntu-in-termux arm8 , try and build using the latest version and build instructions.

**Expected behavior**
Succesfull build.

**Required data**
 [ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o 
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/cl/OclSource.cpp.o 
 In file included from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                         
 /root/xmrig-C3/src/crypto/randomx/randomx.h:170:1: error: template with C linkage
  170 | template<typename T>                          | ^~~~~~~~                                
In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,                                   
from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,
from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                         
 /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here     33 | extern "C" {
      | ^~~~~~~~~~                              
In file included from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:48:
/root/xmrig-C3/src/crypto/astrobwt/AstroBWT.h:37:1: error: template with C linkage
   37 | template<Algorithm::Id ALGO>                  | ^~~~~~~~                                
In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,                                  
 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,
 from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here      33 | extern "C" {
      | ^~~~~~~~~~                              
In file included from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:48:                         
 /root/xmrig-C3/src/crypto/astrobwt/AstroBWT.h:40:1: error: template specialization with C linkage                                                  40 | template<>                                    | ^~~~~~~~
In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,                                  
 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:71:1: error: template with C linkage                  71 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,
                 from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:109:1: error: template with C linkage                109 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:132:1: error: template with C linkage                132 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:156:1: error: template with C linkage                156 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,
                 from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:246:1: error: template with C linkage                246 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:254:1: error: template with C linkage                254 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:390:1: error: template with C linkage                390 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,                                   from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,
                 from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:409:1: error: template with C linkage                409 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,                                   from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {                                  | ^~~~~~~~~~                              /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:453:1: error: template with C linkage                453 | template<size_t N>                            | ^~~~~~~~
In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,                                   from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {                                  | ^~~~~~~~~~                              /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:482:1: error: template specialization with C linkage                                                 482 | template<>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:504:1: error: template with C linkage                504 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {                                  | ^~~~~~~~~~
/root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:522:1: error: template with C linkage                522 | template<size_t N>
      | ^~~~~~~~                                In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,
                 from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,                                            from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:                          /usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here                                                  33 | extern "C" {
      | ^~~~~~~~~~                              /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:561:1: error: expected ‘}’ at end of input
  561 | } // namespace xmrig                          | ^                                       In file included from /root/xmrig-C3/src/crypto/randomx/intrin_portable.h:385,                                   from /root/xmrig-C3/src/crypto/randomx/randomx.h:36,
                 from /root/xmrig-C3/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:12: note: to match this ‘{’
   33 | extern "C" {                                  |            ^                            [ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_generic_cn_generator.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/opencl/generators/ocl_vega_cn_generator.cpp.o                                       make[2]: *** [CMakeFiles/xmrig.dir/build.make:1233: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o] Error 1                               make[2]: *** Waiting for unfinished jobs....    make[1]: *** [CMakeFiles/Makefile2:140: CMakeFiles/xmrig.dir/all] Error 2                       make: *** [Makefile:84: all] Error 2

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2022-03-19T04:12:14+00:00
gcc-9 is broken, use gcc-10

## avselang | 2022-03-20T03:13:15+00:00
> gcc-9 is broken, use gcc-10

how to upgrade gcc-10?
I upgrade to gcc-11,the error appear the same.
I use "sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 100 "command to upgrade,and "update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 100"
I cheak "gcc -v"
"Supported LTO compression algorithms: zlib zstd gcc version 11.1.0 (Ubuntu 11.1.0-1ubuntu1~20.04)".
When i build "-- The C compiler identification is GNU 11.1.0 
-- The CXX compiler identification is GNU 9.4.0 
-- Check for working C compiler: /bin/cc        
-- Check for working C compiler: /bin/cc -- works                                               
-- Detecting C compiler ABI info                
-- Detecting C compiler ABI info - done         
-- Detecting C compile features                 
-- Detecting C compile features - done          
-- Check for working CXX compiler: /bin/c++     
-- Check for working CXX compiler: /bin/c++ -- works"

## Spudz76 | 2022-03-20T07:13:28+00:00
If using the alternatives route, set `cc` and `c++`

gcc happens to work because cc is already linked to gcc which is then linked to gcc-11 however there is no c++ linked to g++ so that half doesn't work the same.

I generally use environment to set active compiler for cmake.  Like:
```
CC=/usr/bin/gcc-11 CXX=/usr/bin/g++-11 cmake ..
```

Hacking it with alternatives is not the right way, gcc-9 compiled every other component on the system and should remain the default "system compiler".

## avselang | 2022-03-20T09:06:17+00:00
> CC=/usr/bin/gcc-11 CXX=/usr/bin/g++-11 cmake ..

yes!successful,thank you!

## Spudz76 | 2022-03-22T20:12:25+00:00
A new package just dropped on focal-updates with version `9.4.0-1ubuntu1~20.04.1` that claims to fix this.  Previous version was same without the last `.1` (`9.4.0-1ubuntu1~20.04`)

Relevant [launchpad bug thread](https://bugs.launchpad.net/ubuntu/+source/gcc-9/+bug/1964260) -- it was crashing similarly in many other projects.

This will restore gcc-9 working properly (bug was upstream at Ubuntu).

# Action History
- Created by: avselang | 2022-03-19T02:53:49+00:00
- Closed at: 2022-04-03T07:49:16+00:00
