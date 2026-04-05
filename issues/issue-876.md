---
title: Segmentation fault when start xmrig
source_url: https://github.com/xmrig/xmrig/issues/876
author: Kevinsss
assignees: []
labels: []
created_at: '2018-11-16T01:57:33+00:00'
updated_at: '2023-08-12T20:08:14+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:03:10+00:00'
---

# Original Description
OS:
```
#uname -ar
Linux S968128.domain 2.6.32-220.el6.i686 #1 SMP Tue Dec 6 16:15:40 GMT 2011 i686 i686 i386 GNU/Linux
#cat /etc/issue
CentOS release 6.2 (Final)
```
I had met errors when I start xmrig, the miner didn't work, below are the error messages.
```
 * ABOUT        XMRig/2.8.3 gcc/4.8.2
 * LIBS         libuv/1.24.1-dev OpenSSL/1.0.1e microhttpd/0.9.33
 * CPU          Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz (4) -x64 AES
 * CPU L2/L3    64.0 MB/0.0 MB
 * THREADS      4, cryptonight, donate=0%
 * POOL #1      sg.minexmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2018-11-16 09:51:44] use pool sg.minexmr.com:5555  139.99.120.73
[2018-11-16 09:51:44] new job from sg.minexmr.com:5555 diff 15000 algo cn/2
Segmentation fault (core dumped)
```
Anyone knows why?

# Discussion History
## ordtrogen | 2019-01-26T09:34:18+00:00
I get a similar result on my Raspberry Pi. I have successfully run xmrig before but after upgrading, and building a newer version, the segmentation fault began to appear


$ uname -ar
Linux piehole 4.20.3-1-ARCH #1 SMP Thu Jan 17 18:08:37 MST 2019 aarch64 GNU/Linux
$ cat /etc/issue
Arch Linux \r (\l)

$ ./xmrig -c ~/configTRTL.json
 * ABOUT        XMRig/2.10.0 gcc/8.2.1
 * LIBS         libuv/1.25.0 OpenSSL/1.1.1a microhttpd/0.9.62
 * CPU          Unknown (1) x64 AES
 * THREADS      4, cryptonight-lite, donate=1%
 * POOL #1      geo.atpool.party:3333 variant 1
 * POOL #2      trtl.cryptohispano.net:3333 variant 1
 * COMMANDS     hashrate, pause, resume
Otillåten instruktion (minnesutskrift skapad)



## ordtrogen | 2019-02-11T18:07:18+00:00
@Kevinsss :
Try it again on your machine. After the update to version 2.11, the segmentation fault disappeared for me and now everything runs fine.

And if it works, consider closing this issue.

## DeadManWalkingTO | 2019-03-17T14:56:39+00:00
Try [latest XMRig version](https://github.com/xmrig/xmrig/releases/latest) and feedback please.
Does the issue still exist?
Thank you!

## xmaci | 2019-12-15T13:15:32+00:00
Hi,
I have 6 ryzens and after the monero hard forkI got on 2 of them the "segmentation fault". OS: hiveOS & win10. I used the latest xmrig 5.2.0 version. I tried everything and can't solve it. Please help me. Thx.

## Sam2much96 | 2021-07-09T12:43:52+00:00
I had this issue on the recent xmrig. version 6.13. It happens whenever i run xmrig as $sudo and then shuts down the miner

## xmrig | 2021-07-09T14:35:46+00:00
@Sam2much96 Please check #2476 probably is your case too.
Thank you.


## PaulinaParangerHr | 2021-07-16T07:58:48+00:00
& mine.

## CMSHostingLLC | 2021-09-04T04:52:19+00:00
Same issue, I checked to see if I had latest as I downloaded and been running since august 14th and updated it, same error pops up... I am on an Apple Silicone Mac mini.

## Iohannulus | 2021-09-11T08:41:41+00:00
Same issue on MacBook Air M1

## jacmos3 | 2022-12-30T14:48:45+00:00
same on Mac mini M1

## NitoSTW | 2023-01-01T22:22:48+00:00
same m2 macbook air


## Unnameless | 2023-01-15T17:33:39+00:00
Why is this an issue? Is it because of the dependencies or libraries?

https://github.com/xmrig/xmrig/issues/3183

## katletkis | 2023-08-12T19:16:05+00:00
same issue on my mac pro m1

``` 
$ ./xmrig -V
XMRig 6.20.0
 built on Aug 12 2023 with clang 14.0.3 (clang-1403.0.22.14.1)
 features:

libuv/1.46.0
OpenSSL/3.1.2
hwloc/2.9.0

$ ./xmrig --bench=1M
 * ABOUT        XMRig/6.20.0 clang/14.0.3
 * LIBS         libuv/1.46.0 OpenSSL/3.1.2 hwloc/2.9.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       15.9/16.0 GB (99%)
 * DONATE       0%
 * POOL #1      benchmark algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-08-12 12:10:31.319]  bench    start benchmark hashes 1M algo rx/0
[2023-08-12 12:10:31.320]  cpu      use argon2 implementation default
[2023-08-12 12:10:31.320]  randomx  init dataset algo rx/0 (8 threads) seed 0000000000000000...
[2023-08-12 12:10:31.320]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2023-08-12 12:10:37.676]  randomx  dataset ready (6356 ms)
[2023-08-12 12:10:37.676]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2023-08-12 12:10:37.677]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (1 ms)
Segmentation fault: 11
```

## SChernykh | 2023-08-12T20:08:14+00:00
@katletkis see the latest comments in https://github.com/xmrig/xmrig/issues/3183

# Action History
- Created by: Kevinsss | 2018-11-16T01:57:33+00:00
- Closed at: 2019-08-02T13:03:10+00:00
