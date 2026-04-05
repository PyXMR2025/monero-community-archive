---
title: '[BUG] ./xmrig: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29'' not
  found (required by ./xmrig)'
source_url: https://github.com/xmrig/xmrig/issues/2572
author: danuonuo
assignees: []
labels: []
created_at: '2021-09-04T14:36:16+00:00'
updated_at: '2021-09-06T22:07:26+00:00'
type: issue
status: closed
closed_at: '2021-09-06T22:07:26+00:00'
---

# Original Description
**Describe the bug**
When I try to compile it myself using the advanced compilation tutorial and then run it on other machines, it does not run and reports the following error:
**./xmrig: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found (required by ./xmrig)**

**To Reproduce**
Use the advanced compilation tutorial to complete the compilation and run it on another machine

**Expected behavior**
./xmrig: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found (required by ./xmrig)

**Required data**
 - Logs:**./xmrig: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found (required by ./xmrig)**
 - OS: Ubuntu20.04LTS

**I use the official tutorial**


# Discussion History
## Spudz76 | 2021-09-04T23:58:52+00:00
You have to compile on the machine it will run on, or at least the identical Linux Distro.  Otherwise set `-DBUILD_STATIC=ON` so it includes more libraries and is more portable (but that still might not work).

Also build the included deps (openssl/libuv/hwloc) with `./scripts/build_deps.sh` as those tend to work more guaranteed than any distro-provided dev packages.  May be required to do static build.

## danuonuo | 2021-09-05T01:46:58+00:00
> You have to compile on the machine it will run on, or at least the identical Linux Distro. Otherwise set `-DBUILD_STATIC=ON` so it includes more libraries and is more portable (but that still might not work).
> 
> Also build the included deps (openssl/libuv/hwloc) with `./scripts/build_deps.sh` as those tend to work more guaranteed than any distro-provided dev packages. May be required to do static build.

_1. sudo apt-get install git build-essential cmake automake libtool autoconf
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/scripts
4. ./build_deps.sh && cd ../build
5. cmake .. -DXMRIG_DEPS=scripts/deps
6. make -j$(nproc)_

Are these incorrent?Thanks.

## Spudz76 | 2021-09-05T02:08:55+00:00
Not if you're running it where you compiled it.  Copying the executable off to some other Linux won't work that way.

## danuonuo | 2021-09-05T02:11:43+00:00
> Not if you're running it where you compiled it. Copying the executable off to some other Linux won't work that way.

So what should I do if I want to compile xmrig to run on other linux?
Thanks.

## Spudz76 | 2021-09-06T02:09:03+00:00
Replace step 5 with: `cmake .. -DXMRIG_DEPS=../scripts/deps -DBUILD_STATIC=ON`

## danuonuo | 2021-09-06T22:07:23+00:00
> Replace step 5 with: `cmake .. -DXMRIG_DEPS=../scripts/deps -DBUILD_STATIC=ON`

OK,I will try.Thanks.

# Action History
- Created by: danuonuo | 2021-09-04T14:36:16+00:00
- Closed at: 2021-09-06T22:07:26+00:00
