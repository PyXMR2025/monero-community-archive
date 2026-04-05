---
title: Compiling error on arm
source_url: https://github.com/xmrig/xmrig/issues/215
author: entick
assignees: []
labels: []
created_at: '2017-11-22T06:56:29+00:00'
updated_at: '2017-11-23T14:37:06+00:00'
type: issue
status: closed
closed_at: '2017-11-23T14:37:06+00:00'
---

# Original Description
[  2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
cc: error: unrecognized command line option ‘-maes’
src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make:62: recipe for target 'src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o' failed
make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
CMakeFiles/Makefile2:122: recipe for target 'src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all' failed
make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

Raspberry pi 2 m. B, Raspbian os, gcc7.

# Discussion History
## xmrig | 2017-11-22T08:23:20+00:00

Please use arm branch, ARM support currently not merged into master branch. Also please check issue #94 for more details.
Thank you.

> On 22 Nov 2017, at 09:56, Ivan Kudryashov <notifications@github.com> wrote:
> 
> [ 2%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
> cc: error: unrecognized command line option ‘-maes’
> src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/build.make:62: recipe for target 'src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o' failed
> make[2]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o] Error 1
> CMakeFiles/Makefile2:122: recipe for target 'src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all' failed
> make[1]: *** [src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/all] Error 2
> Makefile:83: recipe for target 'all' failed
> make: *** [all] Error 2
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


## entick | 2017-11-22T17:27:35+00:00
When im trying to clone arm branche, i get the same err. In the proposed issue, I could not find a solution

## gennadicho | 2017-11-22T23:47:55+00:00
@entick you not switch to the arm. Do "git clone https://github.com/xmrig/xmrig ; cd xmrig ; git fetch origin arm ; git checkout arm ; cmake . ; make" and all be ok. 

## xmrig | 2017-11-23T14:37:06+00:00
Merge this issue with #216

# Action History
- Created by: entick | 2017-11-22T06:56:29+00:00
- Closed at: 2017-11-23T14:37:06+00:00
