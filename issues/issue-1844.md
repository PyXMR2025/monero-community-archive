---
title: Build failure on Armbain GCC
source_url: https://github.com/xmrig/xmrig/issues/1844
author: grahamreeds
assignees: []
labels:
- bug
- arm
created_at: '2020-09-23T09:24:41+00:00'
updated_at: '2020-10-03T05:22:16+00:00'
type: issue
status: closed
closed_at: '2020-10-03T05:22:15+00:00'
---

# Original Description
Just grabbed latest and this what happens on Armbian on a NanoPi Fire3 building master.

[  1%] Built target ethash
[  4%] Built target argon2
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
/root/xmrig/src/crypto/randomx/randomx.cpp: In member function ‘void RandomX_ConfigurationBase::Apply()’:
/root/xmrig/src/crypto/randomx/randomx.cpp:341:32: error: invalid operands of types ‘void (randomx::JitCompilerA64::*)(randomx::Instruction&, uint32_t&)’ {aka ‘void (randomx::JitCompilerA64::*)(randomx::Instruction&, unsigned int&)’} and ‘bool’ to binary ‘operator<’
   INST_HANDLE2(CBRANCH, CBRANCH<true>, FSQRT_R);
                                ^
/root/xmrig/src/crypto/randomx/randomx.cpp:285:96: note: in definition of macro ‘JIT_HANDLE’
 E(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                               ^

/root/xmrig/src/crypto/randomx/randomx.cpp:341:3: note: in expansion of macro ‘INST_HANDLE2’
   INST_HANDLE2(CBRANCH, CBRANCH<true>, FSQRT_R);
   ^~~~~~~~~~~~
/root/xmrig/src/crypto/randomx/randomx.cpp:300:57: error: expected primary-expression before ‘;’ token
  for (; k < freq_sum; ++k) { JIT_HANDLE(func_name, prev); }
                                                         ^
/root/xmrig/src/crypto/randomx/randomx.cpp:341:3: note: in expansion of macro ‘INST_HANDLE2’
   INST_HANDLE2(CBRANCH, CBRANCH<true>, FSQRT_R);
   ^~~~~~~~~~~~
/root/xmrig/src/crypto/randomx/randomx.cpp:344:32: error: invalid operands of types ‘void (randomx::JitCompilerA64::*)(randomx::Instruction&, uint32_t&)’ {aka ‘void (randomx::JitCompilerA64::*)(randomx::Instruction&, unsigned int&)’} and ‘bool’ to binary ‘operator<’
   INST_HANDLE2(CBRANCH, CBRANCH<false>, FSQRT_R);
                                ^
/root/xmrig/src/crypto/randomx/randomx.cpp:285:96: note: in definition of macro ‘JIT_HANDLE’
 E(x, prev) randomx::JitCompilerA64::engine[k] = &randomx::JitCompilerA64::h_##x
                                                                               ^

/root/xmrig/src/crypto/randomx/randomx.cpp:344:3: note: in expansion of macro ‘INST_HANDLE2’
   INST_HANDLE2(CBRANCH, CBRANCH<false>, FSQRT_R);
   ^~~~~~~~~~~~
/root/xmrig/src/crypto/randomx/randomx.cpp:300:57: error: expected primary-expression before ‘;’ token
  for (; k < freq_sum; ++k) { JIT_HANDLE(func_name, prev); }
                                                         ^
/root/xmrig/src/crypto/randomx/randomx.cpp:344:3: note: in expansion of macro ‘INST_HANDLE2’
   INST_HANDLE2(CBRANCH, CBRANCH<false>, FSQRT_R);
   ^~~~~~~~~~~~
make[2]: *** [CMakeFiles/xmrig.dir/build.make:2351: CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:74: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
root@nanopifire3:~/xmrig/build#


# Discussion History
## xmrig | 2020-09-23T09:49:10+00:00
Fixed in dev branch.
Thank you.

## grahamreeds | 2020-09-23T10:00:15+00:00
Was just going to comment that v6.3.3 builds fine.

Can confirm that dev branch builds too.

## hlbcal | 2020-09-29T15:21:27+00:00
I have a tiny box that is using Amlogic S805 chip. 

Architecture:          armv7l
Byte Order:            Little Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):             1
Model:                 1
CPU max MHz:           1536.0000
CPU min MHz:           24.0000
BogoMIPS:              1.02
Flags:                 swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4

I have installed armbian as below:
Linux OneCloud 3.10.108 #17 SMP PREEMPT Fri Dec 7 15:58:12 MSK 2018 armv7l GNU/Linux

My compilation is fail. Wondering if this is doable my hardware or not?

Thanks in advance.
Chen Wei


## grahamreeds | 2020-09-29T15:25:43+00:00
Have you tried building the dev branch?

This has been fixed there.


On Tue, 29 Sep 2020, 16:21 hlbcal, <notifications@github.com> wrote:

> I have a tiny box that is using Amlogic S805 chip.
>
> Architecture: armv7l
> Byte Order: Little Endian
> CPU(s): 4
> On-line CPU(s) list: 0-3
> Thread(s) per core: 1
> Core(s) per socket: 4
> Socket(s): 1
> Model: 1
> CPU max MHz: 1536.0000
> CPU min MHz: 24.0000
> BogoMIPS: 1.02
> Flags: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4
>
> I have installed armbian as below:
> Linux OneCloud 3.10.108 #17 <https://github.com/xmrig/xmrig/issues/17>
> SMP PREEMPT Fri Dec 7 15:58:12 MSK 2018 armv7l GNU/Linux
>
> My compilation is fail. Wondering if this is doable my hardware or not?
>
> Thanks in advance.
> Chen Wei
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1844#issuecomment-700779527>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABGL3HAA55YXNAXR5NEOHB3SIH3QPANCNFSM4RWZLZVA>
> .
>


## hlbcal | 2020-09-29T15:34:27+00:00
> Have you tried building the dev branch? This has been fixed there.
> […](#)
> On Tue, 29 Sep 2020, 16:21 hlbcal, ***@***.***> wrote: I have a tiny box that is using Amlogic S805 chip. Architecture: armv7l Byte Order: Little Endian CPU(s): 4 On-line CPU(s) list: 0-3 Thread(s) per core: 1 Core(s) per socket: 4 Socket(s): 1 Model: 1 CPU max MHz: 1536.0000 CPU min MHz: 24.0000 BogoMIPS: 1.02 Flags: swp half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 I have installed armbian as below: Linux OneCloud 3.10.108 #17 <#17> SMP PREEMPT Fri Dec 7 15:58:12 MSK 2018 armv7l GNU/Linux My compilation is fail. Wondering if this is doable my hardware or not? Thanks in advance. Chen Wei — You are receiving this because you authored the thread. Reply to this email directly, view it on GitHub <[#1844 (comment)](https://github.com/xmrig/xmrig/issues/1844#issuecomment-700779527)>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ABGL3HAA55YXNAXR5NEOHB3SIH3QPANCNFSM4RWZLZVA> .

Yes, I did. It failed. 

## hlbcal | 2020-09-29T15:42:56+00:00
Below are the commands I used.

git clone https://github.com/xmrig/xmrig.git

mkdir xmrig/build && cd xmrig/build

cmake .. -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_MSR=OFF -DWITH_ADL=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF

make -j$(nproc)

Unfortunately, it failed.

## grahamreeds | 2020-09-29T15:45:40+00:00
And the errors were?

On Tue, 29 Sep 2020, 16:43 hlbcal, <notifications@github.com> wrote:

> Below are the commands I used.
>
> git clone https://github.com/xmrig/xmrig.git
>
> mkdir xmrig/build && cd xmrig/build
>
> cmake .. -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_MSR=OFF
> -DWITH_ADL=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF
> -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF
>
> make -j$(nproc)
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1844#issuecomment-700793258>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABGL3HB6HAZXGJPPSWLBDRTSIH6BBANCNFSM4RWZLZVA>
> .
>


## hlbcal | 2020-09-29T15:57:27+00:00
> And the errors were?
> […](#)
> On Tue, 29 Sep 2020, 16:43 hlbcal, ***@***.***> wrote: Below are the commands I used. git clone https://github.com/xmrig/xmrig.git mkdir xmrig/build && cd xmrig/build cmake .. -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_MSR=OFF -DWITH_ADL=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF make -j$(nproc) — You are receiving this because you authored the thread. Reply to this email directly, view it on GitHub <[#1844 (comment)](https://github.com/xmrig/xmrig/issues/1844#issuecomment-700793258)>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ABGL3HB6HAZXGJPPSWLBDRTSIH6BBANCNFSM4RWZLZVA> .

Pls see the attached. Thanks again!

[xmrig_make_log.txt](https://github.com/xmrig/xmrig/files/5300318/xmrig_make_log.txt)


## ph4r05 | 2020-09-30T17:28:17+00:00
Same problem here, 

Compiling with:

```bash
cmake .. -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_NVML=OFF -DWITH_MSR=OFF -DWITH_ADL=OFF -DCMAKE_BUILD_TYPE=Release -DWITH_HWLOC=OFF -DWITH_CN_LITE=OFF -DWITH_CN_HEAVY=OFF -DWITH_CN_PICO=OFF -DARM_TARGET=8
make -j4
```

error:
```
[  8%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b_sse41.c.o
cc: error: unrecognized command line option ‘-msse4.1’
```

Probable culprit:

`./cmake/randomx.cmake`:
```cmake
    if (CMAKE_C_COMPILER_ID MATCHES GNU OR CMAKE_C_COMPILER_ID MATCHES Clang)
        set_source_files_properties(src/crypto/randomx/blake2/blake2b_sse41.c PROPERTIES COMPILE_FLAGS -msse4.1)
    endif()
```

After commenting out all 3 lines in the cmake file, compilation finishes fine.


## ph4r05 | 2020-09-30T18:12:49+00:00
Note: PR #1860 fixes the compilation for me. 

## xmrig | 2020-10-03T05:22:15+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.3.5

# Action History
- Created by: grahamreeds | 2020-09-23T09:24:41+00:00
- Closed at: 2020-10-03T05:22:15+00:00
