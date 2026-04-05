---
title: COMPILATION ERROR ARM/Neoverse-N1/aarch64 - HELP!!!
source_url: https://github.com/xmrig/xmrig/issues/2964
author: andres84
assignees: []
labels: []
created_at: '2022-03-12T16:49:29+00:00'
updated_at: '2022-03-12T21:24:39+00:00'
type: issue
status: closed
closed_at: '2022-03-12T20:58:06+00:00'
---

# Original Description
**Describe the bug**
**compile error**
**[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o**
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

**I try to compile on a machine with the following specifications:**
Architecture:  aarch64
CPU op-mode(s): 32-bit, 64-bit
Vendor ID: ARM
Model name: Neoverse-N1

**I appreciate the help, many thanks**



# Discussion History
## Spudz76 | 2022-03-12T16:53:06+00:00
What is compiler version?

## andres84 | 2022-03-12T16:53:11+00:00
**I use UBUNTU 20.04**

## andres84 | 2022-03-12T16:54:34+00:00
> What is compiler version?

v.6.16.4

## Spudz76 | 2022-03-12T16:55:37+00:00
From some paths looks like `gcc-9.x`

## andres84 | 2022-03-12T17:01:09+00:00
> gcc-9.x

no sir, in the compilation errors I don't see gcc-9.x, please can you explain how I should proceed, since the steps I perform are: sudo apt update

- sudo apt upgrade
- sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y
- git clone https://github.com/xmrig/xmrig.git
- cd xmrig

- mkdir build

- cd build

- cmake ..

- make

## andres84 | 2022-03-12T17:13:29+00:00
> From some paths looks like `gcc-9.x`

proceeded to install
- sudo apt-get update
- sudo apt-get install gcc-9-x86-64-linux-gnux32

but I still get the error when compiling

![image](https://user-images.githubusercontent.com/16921677/158027813-f3fa038e-8f94-48fd-b3be-537ae89e1bb8.png)


## andres84 | 2022-03-12T17:45:47+00:00
still not compiling - appreciate any help 



## hinto-janai | 2022-03-12T18:38:18+00:00
Try my script!
https://github.com/hinto-janaiyo/XMRig-Auto-Build

I don't know if ARM compiles stuff differently
but since it's the latest LTS Ubuntu it _probably_ should work!

## andres84 | 2022-03-12T19:30:07+00:00
> Try my script! https://github.com/hinto-janaiyo/XMRig-Auto-Build
> 
> I don't know if ARM compiles stuff differently but since it's the latest LTS Ubuntu it _probably_ should work!

**hi, thank you very much for your help, unfortunately the error persists**

![image](https://user-images.githubusercontent.com/16921677/158032018-5cf47423-d5fb-45aa-b25b-5234fceab988.png)

**apparently it finishes the configuration but does not create the xmrig executable, it just creates the config.json file**

![image](https://user-images.githubusercontent.com/16921677/158032136-8d8b6f92-870b-4a8c-b374-1051d146416b.png)

**I appreciate any help available to solve the compilation error, sorry for the inconvenience.**




## hinto-janai | 2022-03-12T20:34:07+00:00
Did you let the script download the build dependencies?
Still looks like you're using `gcc-9.x`
I think Ubuntu has `gcc-10.x`, that might fix your problem

## andres84 | 2022-03-12T20:57:54+00:00
> Did you let the script download the build dependencies? Still looks like you're using `gcc-9.x` I think Ubuntu has `gcc-10.x`, that might fix your problem

**Crack!!! eureka!!! solved, thank you very much for everything!!!**
![image](https://user-images.githubusercontent.com/16921677/158034733-456e0b36-29cb-4d64-a667-84ac663cb2b8.png)


## hinto-janai | 2022-03-12T21:24:39+00:00
Glad it worked :)

# Action History
- Created by: andres84 | 2022-03-12T16:49:29+00:00
- Closed at: 2022-03-12T20:58:06+00:00
