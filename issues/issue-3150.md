---
title: CLear Linux not building XMrig
source_url: https://github.com/xmrig/xmrig/issues/3150
author: agentpatience
assignees: []
labels:
- question
created_at: '2022-10-31T02:10:55+00:00'
updated_at: '2025-02-13T21:03:56+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:29:22+00:00'
---

# Original Description
I know know where is best to ask but when I try to compile xmrig on Clear Linux I get:
[100%] Linking CXX executable xmrig
/usr/bin/ld: cannot find -lstdc++: No such file or directory
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:3854: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:182: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:91: all] Error 2



# Discussion History
## Spudz76 | 2022-10-31T07:24:36+00:00
Tried to make a VM to try it out, but since Clear Linux is a total bitch and I don't have `pclmulqdq` it won't even boot, so good luck with that.

## Spudz76 | 2022-10-31T07:30:16+00:00
Nevermind one of my hypervisors did have the silly required instructions, install is progressing now...

## Spudz76 | 2022-10-31T07:57:59+00:00
Double nevermind, it just hangs at "Extracting required packs".  Garbage distro gonna garbage.

## SChernykh | 2022-10-31T08:04:35+00:00
> cannot find -lstdc++: No such file or directory

This is a standard C++ library and it should be available in any sane GCC installation. Something is wrong with your distro.

## Spudz76 | 2022-10-31T09:04:20+00:00
I got the VM install to finish but now it just locks up trying `swupd bundle-add c-basic`

It appears `libstdcpp` is already installed (server edition).

Really can't help if the crap distro won't even run.  Use Ubuntu like normal.

## ghost | 2022-11-21T17:08:32+00:00
clear linux bills itself as an optimized intel distro 

they have preloaded CFLAGS and CXXFLAGS with all kinds of interesting foo

so i did this (in addition to installing the dependencies)

export CFLAGS=""
export CXXFLAGS=""

mkdir build ; cd build ; cmake .. ; make

and got a good xmrig build

so the theory would be that there is a conflict between the optimizations that xmrig wants to do and the optimizations that clear linux has burdened everyone with by default.

## SChernykh | 2022-11-21T17:11:17+00:00
Compiler flags do nothing because XMRig already uses its own ASM code for many algorithms.

## leagueofsoups | 2025-02-13T21:03:54+00:00
Hello from 2025

For anyone who wants to experiment with calerlinux, to fix this error, just install the `c-basic-static` bundle, it contains /usr/lib64/libstdc++.a, this is not a .so, but a static library

# Action History
- Created by: agentpatience | 2022-10-31T02:10:55+00:00
- Closed at: 2022-12-13T14:29:22+00:00
