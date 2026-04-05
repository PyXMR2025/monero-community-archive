---
title: Issue with trying to compile xmrig with Intel Clear Linux
source_url: https://github.com/xmrig/xmrig/issues/1542
author: agentpatience
assignees: []
labels:
- question
created_at: '2020-02-09T04:42:35+00:00'
updated_at: '2021-01-14T01:01:20+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:41:59+00:00'
---

# Original Description
I have installed GCC and HWloc package for clear linux but I get this error when I try to run "cmake .." to configure compiler with xmrig.

-- Looking for syslog.h - found
CMake Error at /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find HWLOC (missing: HWLOC_LIBRARY HWLOC_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindHWLOC.cmake:25 (find_package_handle_standard_args)
  src/backend/cpu/cpu.cmake:30 (find_package)
  src/backend/backend.cmake:1 (include)
  CMakeLists.txt:37 (include)


-- Configuring incomplete, errors occurred!



# Discussion History
## agentpatience | 2020-02-09T04:57:59+00:00
jeff@clr-bd71aad388f64c998025694e7c636eeb~/xmrig/build $ whereis hwloc
hwloc: /usr/share/hwloc /usr/share/man/man7/hwloc.7

## xmrig | 2020-02-09T10:27:26+00:00
I am not familiar with clear linux, but you need hwloc-dev or hwloc-devel or something like that, as alternative you can build own hwloc (use examples for Ubuntu https://xmrig.com/docs/miner/ubuntu-build) or build miner without hwloc `-DWITH_HWLOC=OFF`.
Thank you.

## agentpatience | 2020-02-09T14:46:39+00:00
Thanks this resolved the hwloc error:
 (installing sudo swupd bundle-add devpkg-hwloc) 

but now I am trying to find the bundle for UV as I get this error now:

-- Found HWLOC: /usr/lib64/libhwloc.so  
CMake Error at /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find UV (missing: UV_LIBRARY UV_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
  cmake/FindUV.cmake:25 (find_package_handle_standard_args)
  CMakeLists.txt:175 (find_package)


## agentpatience | 2020-02-09T14:50:52+00:00
Solved with sudo swupd bundle-add devpkg-libuv now:
Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
CMake Error at cmake/OpenSSL.cmake:23 (message):
  OpenSSL NOT found: use `-DWITH_TLS=OFF` to build without TLS support
Call Stack (most recent call first):
  CMakeLists.txt:180 (include)


-- Configuring incomplete, errors occurred!

## agentpatience | 2020-02-09T15:04:57+00:00
solved with sudo swupd bundle-add devpkg-openssl

cmake .. completed without error. I will post my benchmarks later.


## ValoWaking | 2020-02-09T22:39:35+00:00
did u use icc compiler? I'm interest Visual Studio vs GCC (ICC) on Clear linux...

## agentpatience | 2020-02-09T23:13:06+00:00
I am using GCC only for now... I will have some benchmarks soon.

## agentpatience | 2020-02-10T00:11:17+00:00
Manjaro - 11314 h/S avg
Clear Linux - 11116 h/s avg :(

## ValoWaking | 2020-02-10T01:38:06+00:00
> 
> 
> Manjaro - 11314 h/S avg
> Clear Linux - 11116 h/s avg :(

Amazing! Manjaro faster than Clear Linux!?
Did you try something from BSD? OpenBSD, FreeBSD etc...

## ValoWaking | 2020-02-10T01:42:04+00:00
How do you run tests? Are you using virtual machine, or install OS directly?

## agentpatience | 2020-02-10T02:46:15+00:00
Server install the tests used GCC as the default compiler. Manjaro seems a little faster. I will try FreeBSD next.

Sent from my iPhone

> On Feb 9, 2020, at 8:42 PM, ValoWaking <notifications@github.com> wrote:
> 
> ﻿
> How do you run tests? Are you using virtual machine, or install OS directly?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## ValoWaking | 2020-02-15T17:22:28+00:00
> 
> Server install the tests used GCC as the default compiler. Manjaro seems a little faster. I will try FreeBSD next.
> […](#)
> Sent from my iPhone
> On Feb 9, 2020, at 8:42 PM, ValoWaking ***@***.***> wrote: ﻿ How do you run tests? Are you using virtual machine, or install OS directly? — You are receiving this because you authored the thread. Reply to this email directly, view it on GitHub, or unsubscribe.

did u try BSD OS?

## agentpatience | 2020-02-24T21:22:29+00:00
Yes. On E5-2699 V4 I get marginally better performance with Manjaro.

FreeBSD 12.1   - 16648 h/S
Manjaro 18.1.5   - 16908  h/S

## ValoWaking | 2020-02-24T22:01:11+00:00
I will try OpenBSD with xfce. The most performance i have with Linux Mint (Debian edition). But i never tried Manjaro

## agentpatience | 2020-02-25T00:47:48+00:00
I get comparable results with Clear Linux however the system seems quicker with Clear Linux under mining load. FWIW I used GCC 9.2 to build xmrig in all OS tests.

Sent from my iPhone

> On Feb 24, 2020, at 5:01 PM, ValoWaking <notifications@github.com> wrote:
> 
> ﻿
> I will try OpenBSD with xfce. The most performance i have with Linux Mint (Debian edition). But i never tried Manjaro
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub, or unsubscribe.


## agentpatience | 2020-02-25T18:40:57+00:00
Clear Linux on dual 2699 V4 - 16559 h/S

# Action History
- Created by: agentpatience | 2020-02-09T04:42:35+00:00
- Closed at: 2020-08-28T16:41:59+00:00
