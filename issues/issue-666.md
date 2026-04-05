---
title: is xmrig can buid for ios platform？
source_url: https://github.com/xmrig/xmrig/issues/666
author: riverlj
assignees: []
labels:
- question
created_at: '2018-05-30T07:01:32+00:00'
updated_at: '2022-06-29T08:00:48+00:00'
type: issue
status: closed
closed_at: '2019-08-02T14:01:18+00:00'
---

# Original Description
is xmrig can buid for ios platform？

# Discussion History
## xmrig | 2018-05-30T08:58:46+00:00
It can be possible, since ARM CPUs is supported, but I can't help with how exactly do it.
Thank you.

## riverlj | 2018-06-14T03:59:25+00:00
I had completed buid for iOS, thanks.

## snipeTR | 2018-06-14T04:01:25+00:00
Linux=unix. Unix=ios

## resistor4u | 2018-11-09T11:15:40+00:00
@riverlj how did you compile it for ios? i was trying to build natively on my iphone with theos, but i'm not sure how to without cmake.

## Mila432 | 2018-11-09T12:30:47+00:00
@resistor4u what you need theos for?

## resistor4u | 2018-11-09T18:54:23+00:00
@Mila432 using iphone as the build host and build target. i've just copied small things like `libuv` and dropped in the build src dir., and theos helps make some of the necessary headers easily available. i've been using `clang` to build each piece and manually changing header locations, which is tedious and hasn't been very successful.

## resistor4u | 2018-11-10T08:06:01+00:00
Can we re-open this issue?

## xmrig | 2018-11-10T08:15:24+00:00
Sure, but I can't help you much, compile for ARM CPUs is possible, but without cmake it very complicated.
Thank you.

## snipeTR | 2018-11-10T10:42:49+00:00
If build docker and use this app :) 
https://tugboat-app.com
maybe your luck goes

## resistor4u | 2018-11-12T05:57:05+00:00
torture. how about building xmrig for ios from ubuntu 18?

## Mila432 | 2018-11-12T08:35:13+00:00
its very easy to compile xmrig for iOS
```
MacBook-Pro:build root$ ls -lat
total 1176
drwxr-xr-x  16 root  staff     512 Nov 12 09:31 CMakeFiles
-rwxr-xr-x   1 root  staff  533784 Nov 12 09:31 xmrig
drwxr-xr-x   7 root  staff     224 Nov 12 09:31 .
-rw-r--r--   1 root  staff    1409 Nov 12 09:31 cmake_install.cmake
-rw-r--r--   1 root  staff   44818 Nov 12 09:31 Makefile
-rw-r--r--   1 root  staff   15493 Nov 12 09:31 CMakeCache.txt
drwxr-xr-x  14 root  staff     448 Nov 12 09:30 ..
MacBook-Pro:build root$ otool -Vh xmrig 
Mach header
      magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
MH_MAGIC_64   ARM64        ALL  0x00     EXECUTE    17       1912   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE


## snipeTR | 2018-11-12T09:23:45+00:00
Any tutorial?

## Mila432 | 2018-11-12T13:37:04+00:00
compile libuv for ios , then just set host flag and use cmake .. and make 

## snipeTR | 2018-11-12T15:16:54+00:00
is it possible to explain in more detail and simplicity? Which interface in which mode which interface. can you write a manual?

## resistor4u | 2018-11-12T21:24:59+00:00
@Mila432 is it really necessary to compile libuv for iOS, or can we just put the headers into the SDK?

## Mila432 | 2018-11-12T21:25:41+00:00
@resistor4u you know that xmrig uses functions FROM libuv right? how does a header help here

## resistor4u | 2018-11-12T21:44:55+00:00
@Mila432 FML, i thought for some reason it would pull in those functions during processing - probably because i was still thinking about compiling it natively from SSH on the iphone.

## resistor4u | 2018-11-13T01:52:00+00:00
@Mila432 @xmrig @snipeTR  I am attaching two pastebins.

The first (https://pastebin.com/5ixV0Lcj) is of my cmake compilation; the second is the `make` output (https://pastebin.com/MvEdRiDV).

This is for latest `git clone` of xmrig. I use the leetal's [ios-cmake](https://github.com/leetal/ios-cmake). I am using `libuv` v. 1.9 from mapbox's [mason ](https://github.com/mapbox/mason), and used sinofool's [build-openssl-ios](https://github.com/sinofool/build-openssl-ios).

I cannot get the build to move past what you see in the pastebin. Please advise.

## resistor4u | 2018-11-25T04:18:52+00:00
@Mila432 @xmrig do you have any further guidance (or hints?) on this? i've tried multiple environments with different versions of `clang`, but everything fails.

## resistor4u | 2018-11-25T20:15:00+00:00
@Mila432 @xmrig @snipeTR ZOMFG why didn't you say it was simply setting `-DCMAKE_HOST_SYSTEM_PROCESSOR=aarch64 -DCMAKE_SYSTEM_PROCESSOR=aarch64`?!

I've successfully built and tested the dev branch of xmrig for iOS 10.2.1.
```
 * ABOUT        XMRig/2.8.5-dev clang/9.1.0
 * LIBS         libuv/2.0.0-dev
 * CPU          Unknown (1) x64 AES
 * THREADS      2, cryptonight, av=0, donate=2%
 * POOL #1      xmr.pool.minergate.com:45700 variant 2
 * COMMANDS     hashrate, pause, resume
[2018-11-25 13:11:20] READY (CPU) threads 2(2) huge pages 0/2 0% memory 4.0 MB
[2018-11-25 13:11:20] use pool xmr.pool.minergate.com:45700  136.243.102.157
[2018-11-25 13:11:20] new job from xmr.pool.minergate.com:45700 diff 1063 algo cn/2
[2018-11-25 13:11:44] new job from xmr.pool.minergate.com:45700 diff 1063 algo cn/2
[2018-11-25 13:11:47] accepted (1/0) diff 1063 (250 ms)
[2018-11-25 13:11:56] accepted (2/0) diff 1063 (176 ms)
| THREAD | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|      0 |       -1 |    25.3 |    25.2 |     n/a |
|      1 |       -1 |    25.3 |    25.3 |     n/a |
[2018-11-25 13:12:21] speed 10s/60s/15m 50.6 50.5 n/a H/s max 50.6 H/s
```
I have to run now, but I'll be back later and give the `cmake` settings, if you all will find this useful.

## ktalebian | 2022-03-05T09:22:26+00:00
@resistor4u can you provide a step by step instruction please? 

## UnixCro | 2022-06-29T08:00:48+00:00
> @Mila432 @xmrig @snipeTR ZOMFG why didn't you say it was simply setting `-DCMAKE_HOST_SYSTEM_PROCESSOR=aarch64 -DCMAKE_SYSTEM_PROCESSOR=aarch64`?!
> 
> I've successfully built and tested the dev branch of xmrig for iOS 10.2.1.
> 
> ```
>  * ABOUT        XMRig/2.8.5-dev clang/9.1.0
>  * LIBS         libuv/2.0.0-dev
>  * CPU          Unknown (1) x64 AES
>  * THREADS      2, cryptonight, av=0, donate=2%
>  * POOL #1      xmr.pool.minergate.com:45700 variant 2
>  * COMMANDS     hashrate, pause, resume
> [2018-11-25 13:11:20] READY (CPU) threads 2(2) huge pages 0/2 0% memory 4.0 MB
> [2018-11-25 13:11:20] use pool xmr.pool.minergate.com:45700  136.243.102.157
> [2018-11-25 13:11:20] new job from xmr.pool.minergate.com:45700 diff 1063 algo cn/2
> [2018-11-25 13:11:44] new job from xmr.pool.minergate.com:45700 diff 1063 algo cn/2
> [2018-11-25 13:11:47] accepted (1/0) diff 1063 (250 ms)
> [2018-11-25 13:11:56] accepted (2/0) diff 1063 (176 ms)
> | THREAD | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
> |      0 |       -1 |    25.3 |    25.2 |     n/a |
> |      1 |       -1 |    25.3 |    25.3 |     n/a |
> [2018-11-25 13:12:21] speed 10s/60s/15m 50.6 50.5 n/a H/s max 50.6 H/s
> ```
> 
> I have to run now, but I'll be back later and give the `cmake` settings, if you all will find this useful.

____

It looks like you're one of the few who got it right.  It would be really nice of you if you write a manual about it.  Every time I start xmrig `Illegal Instructions` I get nothing else.  No further information, which doesn't help me at all.


# Action History
- Created by: riverlj | 2018-05-30T07:01:32+00:00
- Closed at: 2019-08-02T14:01:18+00:00
