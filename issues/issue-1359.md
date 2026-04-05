---
title: Can't compile on raspbian/raspberry
source_url: https://github.com/xmrig/xmrig/issues/1359
author: quantflares
assignees: []
labels:
- question
- arm
created_at: '2019-12-01T21:24:25+00:00'
updated_at: '2021-09-25T08:34:59+00:00'
type: issue
status: closed
closed_at: '2020-02-23T23:25:23+00:00'
---

# Original Description
First, during Cmake it says "problem with WITH_HWLOC"

I did the WITH_HWLOC "OFF"

but during "make"  
make[2]: *** No rule to make target '/usr/lib64/libuv.a', needed by 'xmrig'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2

any ideas?


# Discussion History
## xmrig | 2019-12-02T00:39:14+00:00
https://xmrig.com/docs/miner/ubuntu-build you need `libuv1-dev` package, but it fine build without WITH_HWLOC if you will get issues with atomic and gcc killed use search is issues.

Raspberry is no soo good for mining because it not support ARM Crypto extensions.
Thank you.

## quantflares | 2019-12-02T11:02:36+00:00
yeah, I know, but, with the new algorithm, it's more interesting especially when you have an army of small raspberry (me).
I would like to try to compile but i can't. can you try please to do that? simply using VirtualBox + raspbian buster lite? https://www.raspberrypi.org/downloads/raspbian/

thanks

## quantflares | 2019-12-02T13:12:26+00:00
just in case..
@xmrig just let me know if you are not going to do that, so don't have to wait 

## wll1rah | 2019-12-02T17:16:00+00:00
Not sure the RPI your using but the easiest way to compile on arm devices of any kind is to hjave arm64 compatible os.  GCC 8 is preferred for compiling or clang6
You can install all required dependences for v5.1 none should be missing especially if your using ubuntu server image. package for hwloc is libhwloc-dev.  If you need help just post back in here and I'll respond with an answer.
p.s. If you have any boards that have Mali GPU's that support OpenCL v2.0 or greater you can use that to mine as well.


## quantflares | 2019-12-02T17:57:05+00:00
@wll1rah 
no, i just have raspberry, (with raspbian installed)

By the way, i just need like list of instruction for raspbian,

or is it necessary to have ubuntu?

## JakeTrans | 2019-12-03T19:33:28+00:00
I was able to build xmrig on Raspbian using these instructions:

https://github.com/xmrig/xmrig/wiki/Ubuntu-Build

I know it's Ubuntu but it worked in a sense, can't run RandomX but I'm not sure if that is xmrig or the Pi (3b+) but the cryptonight side has always been fine for me (although low hash rates)

Hope this helps

## quantflares | 2019-12-03T22:28:48+00:00
hey @JakeTrans 
i had a couple of errors.

by the way, what results did you get with raspberry as Hashrate?



## Hans849 | 2019-12-04T04:43:47+00:00
o/
RPI4 2GB automatically switches to slow mode

![IMG_20191202_210809](https://user-images.githubusercontent.com/58386523/70113059-f533cd00-1657-11ea-91d4-71c6b987a463.png)

RPI4 4GB :)

![IMG_20191202_210755](https://user-images.githubusercontent.com/58386523/70113069-fd8c0800-1657-11ea-82df-c3a662b49ccd.png)


@1650Mhz

## wll1rah | 2019-12-05T02:53:38+00:00
ARM64 is the requirement.  it will work on ARMv7/l but it will be way slower.
On the RPI 4 with 2GB's try making a 2GB swap file on USB 3 flash drive.  This may let you enable enable fast mode.  I've gotten it work on 2GB boards with defyx which is a off shoot of randomx

## JakeTrans | 2019-12-05T18:55:37+00:00
@octapudus about 3 hash/sec on cryptonight, running using screen and lowest priority (I found a optimised RPi version that gave me six about two forks back and wasn't updated)

I built it just after the randomx fork, a while back I was missing some of the libraries have you installed them all?

Quick-edit just build successfully on a Orange pi running Armbian, haven't started the miner yet though

## xwry | 2020-01-20T22:00:06+00:00
> p.s. If you have any boards that have Mali GPU's that support OpenCL v2.0 or greater you can use that to mine as well.

I tried using Mali G52 with xmrig and it wasn't working. clinfo detects GPU and xmrig --print-platform detects it too but  
"xmrig --no-cpu --opencl"  gives me
"OPENCL disabled (selected OpenCL platform NOT found)" 
Am I doing something wrong ?

## wll1rah | 2020-01-21T01:12:49+00:00
> p.s. If you have any boards that have Mali GPU's that support OpenCL v2.0 or greater you can use that to mine as well.
> 
> I tried using Mali G52 with xmrig and it wasn't working. clinfo detects GPU and xmrig --print-platform detects it too but
> "xmrig --no-cpu --opencl"  gives me
> "OPENCL disabled (selected OpenCL platform NOT found)"
> Am I doing something wrong ?

I've got a VIM 3 and VIM 3L working with CN-Pico, Chukwa and varients don't work with GPU mining with Xmrig.
we need some more information to help you though.
What board you are using?  What algo your trying to mine? 
$ ls /etc/OpenCL/vendors/
$ cat /etc/OpenCL/vendors/*.icd
we need to know what driver it's using for OpenCL

## wll1rah | 2020-01-21T01:14:31+00:00
The Mali G31 I've mined with is the fastest for CN-Pico though not sure why either the G52 is superior but but hashes about 25% slower ~30 
ish versus ~45 ish

## xwry | 2020-01-21T23:12:06+00:00
> I've got a VIM 3 and VIM 3L working with CN-Pico, Chukwa and varients don't work with GPU mining with Xmrig.
> we need some more information to help you though.
> What board you are using? What algo your trying to mine?
> $ ls /etc/OpenCL/vendors/
> $ cat /etc/OpenCL/vendors/*.icd
> we need to know what driver it's using for OpenCL

> 

I've got the same boards :) VIM3 4GB and VIM3L, but currently only using VIM3 on CPU monero mining.
I think cn-pico would be best choice for GPU.
`VIM3$ ls /etc/OpenCL/vendors/`
`mali.icd`
`VIM3$ cat /etc/OpenCL/vendors/*.icd`
`libMali.so`
Ubuntu 18 xfce on EMMC / server on SD. 
Sorry for being noob-ish, I just don't know where to start.

## bassamanator | 2021-03-05T22:44:21+00:00
I tried the [guide](https://xmrig.com/docs/miner/build/ubuntu) that was posted above. Tried the basic and advanced build. I get errors in both.
> make[2]: *** [CMakeFiles/xmrig.dir/build.make:2364: CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:74: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2

I'm on Raspberry Pi OS 32 bit, do I need the 64bit version to do this?

Thanks.

## xiaopantt | 2021-09-25T08:34:59+00:00
I have a tvbox GT King pro with manjaro-arm64. At the same time, I successfully compiled xmrig. Then I tested the mining speed [coin=XMR]. But the speed is only 260 ~ 340h / s. I'm trying to find a way to start Mali G52 acceleration. Please give me some guidance.

# Action History
- Created by: quantflares | 2019-12-01T21:24:25+00:00
- Closed at: 2020-02-23T23:25:23+00:00
