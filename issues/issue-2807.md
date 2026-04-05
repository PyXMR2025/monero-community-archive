---
title: static build bug
source_url: https://github.com/xmrig/xmrig/issues/2807
author: CocoHall
assignees: []
labels:
- question
created_at: '2021-12-12T02:43:58+00:00'
updated_at: '2021-12-23T05:51:44+00:00'
type: issue
status: closed
closed_at: '2021-12-19T14:31:33+00:00'
---

# Original Description
if I compile xmrig with "-DBUILD_STATIC=ON",and the pool connected error, xmrig will show "Segmentation fault".But if I compile xmrig without "-DBUILD_STATIC=ON",it work well. 
My OS is centos7.

My steps are as follows：
1. sudo yum install -y epel-release
2. sudo yum install -y git make cmake3 gcc gcc-c++ libstdc++-static automake libtool autoconf
3. sudo yum install -y glibc-static
4. git clone https://github.com/xmrig/xmrig.git
5. mkdir xmrig/build
6. cd xmrig/scripts && ./build_deps.sh && cd ../build
7. cmake3 .. -DXMRIG_DEPS=scripts/deps -DBUILD_STATIC=ON
8. make -j$(nproc)


the result is follows:

 * ABOUT        xmrig/6.16.2 gcc/4.8.5
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz (2) 64-bit AES VM
                L2:0.5 MB L3:18.0 MB 2C/2T NUMA:1
 * MEMORY       0.5/3.7 GB (13%)
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      10.20.20.212:57788 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-12-11 21:29:44.589]  net      10.20.20.212:57788 connect error: "operation canceled"
Segmentation fault




# Discussion History
## Spudz76 | 2021-12-12T10:43:44+00:00
lol at gcc4

## CocoHall | 2021-12-12T13:56:49+00:00
Now I update gcc to version 9.3.1 on Centos7 ,and I also compile xmrig on Centos8 (gcc version  is 8.5), but the problem remains. ,

## Spudz76 | 2021-12-12T19:51:13+00:00
Yes that wasn't likely the problem, there have been about 3 posts regarding this issue.  It is still a mystery.

I just find it lol-able when CentOS has versions of everything from the 1990s

## Spudz76 | 2021-12-12T19:57:36+00:00
Something actual to check/try is to ensure you use the same compiler for the deps phase, so they definitely link correctly.

Sometimes, a system will have a default gcc/g++ (like 4) that is not the newer one unless you set `CC`/`CXX` in your environment or override it locally upon calling the script.  Such as:

```
cd /usr/src/xmrig/scripts/ && (CC=/usr/bin/gcc-9 CXX=/usr/bin/g++-9 ./build_deps.sh)
```

## xmrig | 2021-12-13T14:45:16+00:00
You can't create working static build without using specials libc optimized for it, for example musl libc. Official static builds use Alpine Linux, this system based on musl libc by default.
Thank you.

# Action History
- Created by: CocoHall | 2021-12-12T02:43:58+00:00
- Closed at: 2021-12-19T14:31:33+00:00
