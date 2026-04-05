---
title: cpu.cmake is not properly configured on the arm branch for armv7 and some specification
  display errors
source_url: https://github.com/xmrig/xmrig/issues/295
author: limitfan
assignees: []
labels:
- arm
created_at: '2017-12-26T06:46:28+00:00'
updated_at: '2018-01-11T08:43:23+00:00'
type: issue
status: closed
closed_at: '2018-01-11T08:43:23+00:00'
---

# Original Description
I installed termux which is a great tool for touching the TUI of Linux environment on Android. 
Some minor errors are found when I build xmrig for armv7a and arm64-v8a android devices.
The sub cmakefile cpu.cmake is not properly configured on the arm branch.
The following image is the version without any parameter tuning or further optimization.
 ![nexus 5](https://i.loli.net/2017/12/26/5a41ed55672f7.png)
The following image running on the exynos 8890 variant version of S7 edge displays some erroneous CPU specifications.
 ![s7 edge ](https://i.loli.net/2017/12/26/5a41ed66450a7.png)

And one more question remaining is that how to port this miner on s390x arch when SIMD instructions are not properly available with certain virtualization technology.



# Discussion History
## xmrig | 2017-12-28T08:22:17+00:00
It known issue, runtime CPU detection and configuration still lacks for ARM.
About s390x I have no access to such hardware, if mining code available somewhere it might help.
Thank you.

## limitfan | 2017-12-28T10:24:46+00:00
Hi, thank you for your concern about these minor issues.
It's really relatively meaningless to implement a miner on s390x arch which
is surely built for centralized transaction processings.
If you want to have a try on these machines, you can check here:
https://linuxone20.cloud.marist.edu/cloud/#/register
It provides free trials of these virtualized machines with high Unix
benchmark and pystone score.

On Thu, Dec 28, 2017 at 4:22 PM, xmrig <notifications@github.com> wrote:

> It known issue, runtime CPU detection and configuration still lacks for
> ARM.
> About s390x I have no access to such hardware, if mining code available
> somewhere it might help.
> Thank you.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/295#issuecomment-354249581>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/ABsr--bFACM__cr9x7OZX9GzKXO3hmcQks5tE0-8gaJpZM4RMi3u>
> .
>


## davidtavarez | 2018-01-04T18:48:47+00:00
@limitfan can you share how do you did it? thanks.

## limitfan | 2018-01-05T03:15:19+00:00
@davidtavarez I did it by following these steps:

1. Install [Termux ](https://termux.com/)on your android devices.

2. Open Termux and use the same build instruction as [this](https://github.com/xmrig/xmrig/wiki/Ubuntu-Build) with some minor changes.

```
apt update
apt install git  cmake libuv-dev 
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake .. -DWITH_HTTPD=OFF
make
```
If you can build xmrig binary without any problem, you can run it the same way as you did in a Linux environment. Termux just turned headless Linux computing in most cases into a touchable one. 

## davidtavarez | 2018-01-05T12:49:15+00:00
Cool, man. It works!

Now I can do something like `Process proc = Runtime.getRuntime().exec("xrmig");` 

## limitfan | 2018-01-05T14:27:27+00:00
@davidtavarez You may have a try with this method which maybe is invalid on higher Android versions and ldding xmrig binary reveals its dependency.
The recommended and canonical way is to build with Android's official NDK cross platform toolchain to generate a lib and package it into an apk.

## cmorsucci | 2018-01-10T16:49:21+00:00
@limitfan is there a guide to be able to compile with NDK and be able to put it in my Android app?

## limitfan | 2018-01-11T03:57:54+00:00
@cmorsucci It's currently not available and not profitable for implementing such a miner which will destablize mobile users' experience of your Android apps. Some altcoin uses your cpu model to credit your hashrate without actually hashing anything for a period of time. If your app got numbers of active users, you will easily find more suitable ways for generating additional incomes.

## cmorsucci | 2018-01-11T08:31:21+00:00
I understand .. but I want to try to incorporate it in one of my apps, is there a mini guide on how to compile it with ndk?

## limitfan | 2018-01-11T08:38:17+00:00
@cmorsucci Build it in similar way in accordance with [xmrig's Windows platform build](https://github.com/xmrig/xmrig/wiki/Windows-Build).

## cmorsucci | 2018-01-11T08:41:57+00:00
mmm ok, you're not helping me like that ..

## limitfan | 2018-01-11T08:43:23+00:00
You are causing too much trouble and didn't help me solve my original issue.
Thank you for your reading and I will close this issue for now.

# Action History
- Created by: limitfan | 2017-12-26T06:46:28+00:00
- Closed at: 2018-01-11T08:43:23+00:00
