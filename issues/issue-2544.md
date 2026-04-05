---
title: '[S390X] cc: Error：unrecognized command line option ‘-maes’'
source_url: https://github.com/xmrig/xmrig/issues/2544
author: lem0nb
assignees: []
labels: []
created_at: '2021-08-17T15:00:48+00:00'
updated_at: '2023-10-22T05:59:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
S390X cannot execute binary file: Exec format error

**To Reproduce**
[root@PC WWW]# ./xmrig
-bash: ./xmrig: cannot execute binary file: Exec format error


**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows] Redhat
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2021-08-17T23:29:42+00:00
This is not Intel-compatible so you can't run the release.  Compile yourself on the machine in question.

## lem0nb | 2021-08-18T05:20:05+00:00
> 
> 
> This is not Intel-compatible so you can't run the release. Compile yourself on the machine in question.

CMake Error at /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:108 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:315 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:187 (find_package)


-- Configuring incomplete, errors occurred!
See also "/root/xmrig/build/CMakeFiles/CMakeOutput.log".
See also "/root/xmrig/build/CMakeFiles/CMakeError.log".



Something Wrong


## lem0nb | 2021-08-18T05:47:49+00:00
> 
> 
> This is not Intel-compatible so you can't run the release. Compile yourself on the machine in question.

cc: Error：unrecognized command line option ‘-maes’
cc: Error：unrecognized command line option ‘-maes’
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/arch/x86_64/lib/argon2-avx512f.c.o] Error 1
make[1]: *** [src/3rdparty/argon2/CMakeFiles/argon2-avx512f.dir/all] Error 2
make[1]: *** Waiting....
make[2]: *** [src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/arch/x86_64/lib/argon2-sse2.c.o] Error 1
make[1]: *** [src/3rdparty/argon2/CMakeFiles/argon2-sse2.dir/all] Error 2
make: *** [all] Error 2


## DeeDeeRanged | 2021-08-21T12:00:23+00:00
You do have all the neccessary build packages installed? It seems to me libuv1-dev or similar for your S390X Unix/Linux is missing.
Are you using the Basic or Advanced build instructions?

## Spudz76 | 2021-08-21T16:22:26+00:00
There may not be proper support for generic CPUs (since ARM is the only other supported CPU family... not-ARM means amd64 by default).  These run some form of IBM CPU.

## DeeDeeRanged | 2021-08-21T18:39:29+00:00
If he has ubuntu installed it might be possible to find the gcc compiler options needed. I did have a look but most of it is gobbledeegook for me. gcc -maes is for x86 only as you already stated. I wish him the best of luck.

## lem0nb | 2021-08-22T09:58:48+00:00
> 
> 
> You do have all the neccessary build packages installed? It seems to me libuv1-dev or similar for your S390X Unix/Linux is missing.
> Are you using the Basic or Advanced build instructions?

I used yum to instaall them

## lem0nb | 2021-08-22T09:59:33+00:00
> If he has ubuntu installed it might be possible to find the gcc compiler options needed. I did have a look but most of it is gobbledeegook for me. gcc -maes is for x86 only as you already stated. I wish him the best of luck.

Only Red Hat or Arch OS

## adozenlines | 2021-08-28T16:10:37+00:00
Might need to get your hands on https://www.ibm.com/support/pages/xl-cc-runtime-linux-z-systems-12

## Randname666 | 2023-10-22T05:59:20+00:00
Can't be done without patching cmake scripts and randomx.cpp. There are too many thing coupled with ARM/x86 JIT.

# Action History
- Created by: lem0nb | 2021-08-17T15:00:48+00:00
