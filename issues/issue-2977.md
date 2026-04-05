---
title: Make commands fails on 64-bit ubutnu Pi4
source_url: https://github.com/xmrig/xmrig/issues/2977
author: HamburgerPlsdotexe
assignees: []
labels: []
created_at: '2022-03-18T20:41:29+00:00'
updated_at: '2022-03-20T13:42:26+00:00'
type: issue
status: closed
closed_at: '2022-03-20T13:39:28+00:00'
---

# Original Description
**Describe the bug**
after having git cloned the repo, cmaked and executing make afterwards, I get a make error at 10% in.

**To Reproduce**
run make after cmake

**Expected behavior**
No errors during make

**Required data**```
```

[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
In file included from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/home/ubuntu/xmrig/src/crypto/randomx/randomx.h:160:1: error: template with C linkage
  160 | template<typename T>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
In file included from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:48:
/home/ubuntu/xmrig/src/crypto/astrobwt/AstroBWT.h:37:1: error: template with C linkage
   37 | template<Algorithm::Id ALGO>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
In file included from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:48:
/home/ubuntu/xmrig/src/crypto/astrobwt/AstroBWT.h:40:1: error: template specialization with C linkage
   40 | template<>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:71:1: error: template with C linkage
   71 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:109:1: error: template with C linkage
  109 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:132:1: error: template with C linkage
  132 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:156:1: error: template with C linkage
  156 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:236:1: error: template with C linkage
  236 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:244:1: error: template with C linkage
  244 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:379:1: error: template with C linkage
  379 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:398:1: error: template with C linkage
  398 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:442:1: error: template with C linkage
  442 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:471:1: error: template specialization with C linkage
  471 | template<>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:493:1: error: template with C linkage
  493 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:511:1: error: template with C linkage
  511 | template<size_t N>
      | ^~~~~~~~
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:1: note: ‘extern "C"’ linkage started here
   33 | extern "C" {
      | ^~~~~~~~~~
/home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:550:1: error: expected ‘}’ at end of input
  550 | } // namespace xmrig
      | ^
In file included from /home/ubuntu/xmrig/src/crypto/randomx/intrin_portable.h:385,
                 from /home/ubuntu/xmrig/src/crypto/randomx/randomx.h:35,
                 from /home/ubuntu/xmrig/src/backend/cpu/CpuWorker.cpp:43:
/usr/lib/gcc/aarch64-linux-gnu/9/include/arm_acle.h:33:12: note: to match this ‘{’
   33 | extern "C" {
      |            ^
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1233: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:140: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```


**Additional context**
No additional context, willing to provide more if required


# Discussion History
## HamburgerPlsdotexe | 2022-03-19T11:13:08+00:00
bump

## HamburgerPlsdotexe | 2022-03-20T11:58:08+00:00
bump

## HamburgerPlsdotexe | 2022-03-20T13:42:26+00:00
Fixed it, had to remove gcc 9 and g++ 9 + everything that had to do with it and manually install versions 10 for both. Finally configure both with 

```
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 60
sudo update-alternatives --config g++

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 60
sudo update-alternatives --config gcc
```

start with a **fresh** build folder and do 
`cmake ..` 
`make`

# Action History
- Created by: HamburgerPlsdotexe | 2022-03-18T20:41:29+00:00
- Closed at: 2022-03-20T13:39:28+00:00
