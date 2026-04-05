---
title: Include ppc64le CPU mining support
source_url: https://github.com/xmrig/xmrig/issues/2227
author: RunAIPilot
assignees: []
labels:
- need feedback
created_at: '2021-04-01T23:18:12+00:00'
updated_at: '2022-01-02T19:46:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Previously mining successfully on xmr-stak-power but getting updated xmrig for CPU mining seems unsupported.  CentOS 7 ppc64le CPU mining.  

 gcc --version
gcc (GCC) 8.3.1 20190311 (Red Hat 8.3.1-3)
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


# git clone https://github.com/xmrig/xmrig.git
Cloning into 'xmrig'...
remote: Enumerating objects: 34, done.
remote: Counting objects: 100% (34/34), done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 23265 (delta 8), reused 13 (delta 6), pack-reused 23231
Receiving objects: 100% (23265/23265), 9.31 MiB | 12.32 MiB/s, done.
Resolving deltas: 100% (17231/17231), done.

# mkdir xmrig/build && cd xmrig/build
# cmake ..
-- The C compiler identification is GNU 8.3.1
-- The CXX compiler identification is GNU 8.3.1
-- Check for working C compiler: /opt/rh/devtoolset-8/root/usr/bin/cc
-- Check for working C compiler: /opt/rh/devtoolset-8/root/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /opt/rh/devtoolset-8/root/usr/bin/c++
-- Check for working CXX compiler: /opt/rh/devtoolset-8/root/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib64/libhwloc.so
-- Found UV: /usr/lib64/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - not found
-- WITH_MSR=ON
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
-- The ASM compiler identification is GNU
-- Found assembler: /opt/rh/devtoolset-8/root/usr/bin/cc
-- Found OpenSSL: /usr/lib64/libcrypto.so (found version "1.0.2k")
-- Configuring done
-- Generating done
-- Build files have been written to: /home/root/xmrig/build
# make -j$(nproc)


Followed by pages of: 

/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:610: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:610: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:611: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:613: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:613: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:619: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:619: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:627: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:627: Error: unsupported relocation against r9
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:628: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:630: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:630: Error: unsupported relocation against r9
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:636: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:636: Error: unsupported relocation against r9
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:644: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:644: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:645: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:647: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:647: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:653: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:653: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:661: Error: unsupported relocation against rbp
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:661: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:662: Error: unsupported relocation against rbp
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:664: Error: unsupported relocation against rbp
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:664: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:670: Error: unsupported relocation against rbp
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:670: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:678: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:678: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:679: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:681: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:681: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:687: Error: unsupported relocation against rbx
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:687: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:695: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:695: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:696: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:698: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:698: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:704: Error: unsupported relocation against rsi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:704: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:712: Error: unsupported relocation against rdi
/home/root/xmrig/src/crypto/cn/asm/CryptonightR_template.S:712: Error: unsupported relocation against r9



# Discussion History
## SChernykh | 2021-04-02T07:04:22+00:00
Only x86 and ARM are supported, but you can try to run cmake with `-DWITH_ASM=OFF` and see what happens.

## SChernykh | 2021-04-02T08:07:11+00:00
You will also need https://github.com/xmrig/xmrig/pull/2229 to compile with `-DWITH_ASM=OFF`

## RunAIPilot | 2021-04-07T22:28:10+00:00
still no dice with -DWITH_ASM=OFF


## xmrig | 2021-04-12T13:37:26+00:00
We don't have ppc64le hardware and you didn't provide new errors with `-DWITH_ASM=OFF` so right now no future fixes possible.
Thank you.

## madobet | 2021-04-24T09:58:59+00:00
> 
> 
> We don't have ppc64le hardware and you didn't provide new errors with `-DWITH_ASM=OFF` so right now no future fixes possible.
> Thank you.

Tried with my power8 server (ppc64le), `cmake -DWITH_ASM=OFF .. && make` made the compilation started and then stopped at error:
```
/home/user/xmrig/src/backend/cpu/platform/BasicCpuInfo.cpp:29:13: fatal error: cpuid.h: No such file or directory
   29 | #   include <cpuid.h>
      |             ^~~~~~~~~
compilation terminated.
```
seems to be lack of the libcpuid which is only provided on x86/x86_64 platform.

## Spudz76 | 2021-04-25T02:19:51+00:00
Well it [falls back](https://github.com/xmrig/xmrig/blob/master/src/backend/cpu/cpu.cmake#L49) to assuming x86 when it doesn't find any other CPU it knows how to handle (which is literally ARM and that's all)

ARM or it's Intel compatible is how the logic works, which is how it ended up in x86-ish code.

Would need all of that stubbed out for ppc64le similar to how ARM support switches itself in.

## Zzmissu | 2021-04-29T09:11:42+00:00
Hi guys！ Is that problem resloved？ i have the same problem

## Spudz76 | 2021-04-30T18:41:08+00:00
![image](https://user-images.githubusercontent.com/2391234/116739765-52e55980-a9b1-11eb-9334-b12570b6f979.png)

## marcofariasmx | 2021-05-20T02:53:26+00:00
> We don't have ppc64le hardware and you didn't provide new errors with `-DWITH_ASM=OFF` so right now no future fixes possible.
> Thank you.

How can I help? I have access to a ppc64le Power9 server. Would be more than happy to run some tests and help out.

## marcofariasmx | 2021-06-04T05:45:10+00:00
> We don't have ppc64le hardware and you didn't provide new errors with `-DWITH_ASM=OFF` so right now no future fixes possible.
> Thank you.

Hello, I tried compiling with the suggested adjustments. I am running a ppc64le Power9 server with gcc 7.3.1. This is what I got:


![120751663-07512e80-c4ce-11eb-8307-e2c0fd794163](https://user-images.githubusercontent.com/41245794/136640365-9c2455d2-23f8-4115-9e73-d56eaa58e62d.png)


Please, let me help, I'd be more than happy to contribute, I just ask for some more guidance.

## Spudz76 | 2021-10-09T02:40:51+00:00
Interesting information [available here](https://gitlab.com/johnjmar/nettle/-/issues/1) where they speak of using the Power8/Power9 AES acceleration instructions, and some ASM to look at.  So that's a good sign since doing AES in software is at least 10x slower (they say 13.5x in their testing) and would essentially keep this wish as not worth doing (hashrate would probably be terrible).  It could still be terrible compared to other architectures, depending how the memory and cache latencies work out.  Some of those questions seem to be [answered here](https://github.com/nioroso-x3/xmr-stak-power/issues/5) and then there was a powerpc [xmrig here](https://github.com/nioroso-x3/xmrig) but it is 2113 commits behind current and also has no RandomX.

The kernels from the old fork might be a starting point to cross-port something.  xmr-stak internal miner kernel API is a bit different I think, but the older versions were very similar.  The core routines or ASM should still be wrappable into xmrig.  Old xmr-stak-power doesn't even have RandomX though.

At least maybe more promising than MIPS64.

Maybe see if it's possible to drag some of those PPC devs back to update stuff.  But it almost feels like performance sucked even on Power9 and thus it was abandoned.

## cyrozap | 2022-01-02T19:46:16+00:00
I've looked into this a bit, and it seems it'll be tricky because the build system will require some significant changes to sanely support another platform. Like @Spudz76 said, the way it currently works is that the CMake scripts check if the platform is Arm, and if not, it just assumes the platform is x86, so the build currently fails completely on ppc64le platforms even if you only want to use OpenCL/CUDA. There's also quite a lot of `#ifdef XMRIG_ARM`-type checks in the C++ code, as well, so it's difficult to tell at a glance what needs to be changed to support ppc64le.

IMO, the code should be refactored to move platform-specific code into their own source files as much as possible, then select the platform-specific files in the CMake scripts based on what platform the scripts identify is the target. That way, more platforms could be added in the future without having to touch a bunch of files unrelated to those platforms. These modifications could be made by a developer even without access to a POWER8/POWER9 system, so anyone familiar with the code should be able to make them. I'd do it myself, but I've only just begun to read and understand this code so it might be a while before I get around to it.

# Action History
- Created by: RunAIPilot | 2021-04-01T23:18:12+00:00
