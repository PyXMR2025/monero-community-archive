---
title: Segmentation Fault
source_url: https://github.com/xmrig/xmrig/issues/1158
author: tunes0710
assignees: []
labels:
- bug
created_at: '2019-09-03T06:56:50+00:00'
updated_at: '2019-12-22T19:26:27+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:26:27+00:00'
---

# Original Description
I upgraded from 3.1.0 to 3.1.1 and noticed after an hour or so the pool showed this worker as offline

[2019-09-03 06:09:41.606] no active pools, stop mining
[2019-09-03 06:11:41.802] [loki-eu.luxor.tech:9999] connect error: "host is unreachable"
[2019-09-03 06:11:41.802] [loki-eu.luxor.tech:9999] connect error: "operation canceled"
Segmentation fault


Restarted and all seems to be ok so far
 * ABOUT        XMRig/3.1.1 gcc/5.4.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * CPU          Intel(R) Core(TM) i3-7100 CPU @ 3.90GHz (1) x64 AES
                L2:0.5 MB L3:3.0 MB 2C/4T NUMA:1
 * DONATE       2%
 * ASSEMBLY     auto:intel


Are there any logs that it creates which I can post to help find what caused this issue?


# Discussion History
## xmrig | 2019-09-03T07:22:47+00:00
It's strange, looks like `onConnect` called twice, both errors has same timestamp, what OS do you use?
Thank you.

## tunes0710 | 2019-09-03T07:41:19+00:00
This is running on a FreePBX machine

 cat /etc/os-release
NAME="Sangoma Linux"
VERSION="7 (Core)"
ID="sangoma"
ID_LIKE="centos rhel fedora"
VERSION_ID="7"
PRETTY_NAME="Sangoma Linux 7 (Core)"


## xmrig | 2019-09-03T08:35:50+00:00
Please check this commit https://github.com/xmrig/xmrig/commit/a8c2e908a2b24b5773ed90b0d386bea1b24bf40d if I guess right, miner will not crash, but you will see error like `connect error: "invalid state: 4"`, in additional you can rebuild miner with cmake option `-DWITH_DEBUG_LOG=ON`.
Thank you.

## tunes0710 | 2019-09-04T04:26:52+00:00
I'll give it a go, although since restarting, that miner hasn't crashed again.

Although another miner (linux again) did crash with 
xmrig: src/unix/getaddrinfo.c:125: uv__getaddrinfo_done: Assertion `0' failed.
Aborted (core dumped)

This one is on Ubuntu
NAME="Ubuntu"
VERSION="19.04 (Disco Dingo)"


## xmrig | 2019-09-04T05:00:33+00:00
libuv version? need to know what exactly on line 125.
Thank you.

## tunes0710 | 2019-09-09T05:30:03+00:00
> Please check this commit [a8c2e90](https://github.com/xmrig/xmrig/commit/a8c2e908a2b24b5773ed90b0d386bea1b24bf40d) if I guess right, miner will not crash, but you will see error like `connect error: "invalid state: 4"`, in additional you can rebuild miner with cmake option `-DWITH_DEBUG_LOG=ON`.
> Thank you.

Hiya,
I'm trying to build from the commit you suggested. At first I was getting the HWLOC issue, but installed hwloc-devel to sort that.

However now it's giving me this error...


` cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 4.8.5
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib64/libhwloc.so
-- Found UV: /usr/lib64/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- argon2: detecting feature 'sse2'...
-- Performing Test FEATURE_sse2_NOFLAG
-- Performing Test FEATURE_sse2_NOFLAG - Success
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- Performing Test FEATURE_ssse3_NOFLAG
-- Performing Test FEATURE_ssse3_NOFLAG - Failed
-- Performing Test FEATURE_ssse3_FLAG
-- Performing Test FEATURE_ssse3_FLAG - Success
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- Performing Test FEATURE_xop_NOFLAG
-- Performing Test FEATURE_xop_NOFLAG - Failed
-- Performing Test FEATURE_xop_FLAG
-- Performing Test FEATURE_xop_FLAG - Success
-- argon2: feature 'xop' detected!
-- argon2: detecting feature 'avx2'...
-- Performing Test FEATURE_avx2_NOFLAG
-- Performing Test FEATURE_avx2_NOFLAG - Failed
-- Performing Test FEATURE_avx2_FLAG
-- Performing Test FEATURE_avx2_FLAG - Success
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- Performing Test FEATURE_avx512f_NOFLAG
-- Performing Test FEATURE_avx512f_NOFLAG - Failed
-- Performing Test FEATURE_avx512f_FLAG
-- Performing Test FEATURE_avx512f_FLAG - Failed
CMake Error at src/3rdparty/argon2/CMakeLists.txt:80 (target_sources):
  Unknown CMake command "target_sources".
`

Line 80 of that file is
`    target_sources(argon2 PRIVATE arch/x86_64/lib/argon2-arch.c arch/x86_64/lib/cpu-flags.c)`


## gxk001 | 2019-09-10T07:33:39+00:00
> > Please check this commit [a8c2e90](https://github.com/xmrig/xmrig/commit/a8c2e908a2b24b5773ed90b0d386bea1b24bf40d) if I guess right, miner will not crash, but you will see error like `connect error: "invalid state: 4"`, in additional you can rebuild miner with cmake option `-DWITH_DEBUG_LOG=ON`.
> > Thank you.
> 
> Hiya,
> I'm trying to build from the commit you suggested. At first I was getting the HWLOC issue, but installed hwloc-devel to sort that.
> 
> However now it's giving me this error...
> 
> `cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a -- The C compiler identification is GNU 4.8.5 -- The CXX compiler identification is GNU 4.8.5 -- Check for working C compiler: /usr/bin/cc -- Check for working C compiler: /usr/bin/cc -- works -- Detecting C compiler ABI info -- Detecting C compiler ABI info - done -- Check for working CXX compiler: /usr/bin/c++ -- Check for working CXX compiler: /usr/bin/c++ -- works -- Detecting CXX compiler ABI info -- Detecting CXX compiler ABI info - done -- Looking for syslog.h -- Looking for syslog.h - found -- Found HWLOC: /usr/lib64/libhwloc.so -- Found UV: /usr/lib64/libuv.a -- Looking for __builtin___clear_cache -- Looking for __builtin___clear_cache - found -- argon2: detecting feature 'sse2'... -- Performing Test FEATURE_sse2_NOFLAG -- Performing Test FEATURE_sse2_NOFLAG - Success -- argon2: feature 'sse2' detected! -- argon2: detecting feature 'ssse3'... -- Performing Test FEATURE_ssse3_NOFLAG -- Performing Test FEATURE_ssse3_NOFLAG - Failed -- Performing Test FEATURE_ssse3_FLAG -- Performing Test FEATURE_ssse3_FLAG - Success -- argon2: feature 'ssse3' detected! -- argon2: detecting feature 'xop'... -- Performing Test FEATURE_xop_NOFLAG -- Performing Test FEATURE_xop_NOFLAG - Failed -- Performing Test FEATURE_xop_FLAG -- Performing Test FEATURE_xop_FLAG - Success -- argon2: feature 'xop' detected! -- argon2: detecting feature 'avx2'... -- Performing Test FEATURE_avx2_NOFLAG -- Performing Test FEATURE_avx2_NOFLAG - Failed -- Performing Test FEATURE_avx2_FLAG -- Performing Test FEATURE_avx2_FLAG - Success -- argon2: feature 'avx2' detected! -- argon2: detecting feature 'avx512f'... -- Performing Test FEATURE_avx512f_NOFLAG -- Performing Test FEATURE_avx512f_NOFLAG - Failed -- Performing Test FEATURE_avx512f_FLAG -- Performing Test FEATURE_avx512f_FLAG - Failed CMake Error at src/3rdparty/argon2/CMakeLists.txt:80 (target_sources): Unknown CMake command "target_sources".`
> 
> Line 80 of that file is
> ` target_sources(argon2 PRIVATE arch/x86_64/lib/argon2-arch.c arch/x86_64/lib/cpu-flags.c)`

**(target_sources): Unknown CMake command "target_sources"**

upgrade cmake > 3.6.1

cat ./3rdparty/argon2/CMakeLists.txt | more
cmake_minimum_required(VERSION 2.6) --> needs attention

## xmrig | 2019-09-14T13:42:47+00:00
cmake issue fixed https://github.com/xmrig/xmrig/commit/179ef31b80f2cc42c948b629689f00e547b483f6 another solution is disable Argon2 algorithm by `-DWITH_ARGON2=OFF`.

# Action History
- Created by: tunes0710 | 2019-09-03T06:56:50+00:00
- Closed at: 2019-12-22T19:26:27+00:00
