---
title: Segmentation fault (core dumped) on Ubuntu
source_url: https://github.com/xmrig/xmrig/issues/1196
author: XMRUSD
assignees: []
labels:
- bug
- opcache
created_at: '2019-09-26T13:57:34+00:00'
updated_at: '2021-07-11T04:05:52+00:00'
type: issue
status: closed
closed_at: '2019-10-18T20:42:37+00:00'
---

# Original Description
2 x AMD EPYC 7551P 32 core CPU
Dual socket Supermicro H11DSi
2 x 32gb Samsung ECC DDR4 

![affinity](https://user-images.githubusercontent.com/55839532/65688659-21681780-e031-11e9-9769-535dc0e6385c.PNG)
Windows 10 LTSC 2019 X64

![linux2](https://user-images.githubusercontent.com/55839532/65689028-bcf98800-e031-11e9-99a9-cab585af0d1a.PNG)
Ubuntu 19.04

In Windows I get "Unable to set affinity, Windows support only affinity up to 63", so I installed Ubuntu but get "Segmentation fault (core dumped)". 

I noticed on Ubuntu, NUMA is only at 1, while on Windows it was at 8.
Is there a way to change that?


# Discussion History
## xmrig | 2019-09-26T15:00:15+00:00
Try rebuild miner from source https://github.com/xmrig/xmrig/wiki/Ubuntu-Build

Run `lscpu` likely it show 8 NUMA nodes, but hwloc2 on Linux filter out nodes without memory, it known already reported issue, hwloc 1.11 (ubuntu stock version) will see all 8 nodes.
But please note DDR4 memory is limited to about 4000-6000 H/s per channel, so with 2 channels NUMA support will be useless anyway.

There was also few reports about crash on desktop first generation Zen CPUs, general recommendation revert to stock clocks and update BIOS, but it might hard in your case. 
Thank you.

## XMRUSD | 2019-09-27T01:24:30+00:00
![B0](https://user-images.githubusercontent.com/55839532/65734704-d46c5b80-e099-11e9-9cba-f279032b90ee.png)
**CPU #0-63 warning: "can't bind memory"**.......

![B2](https://user-images.githubusercontent.com/55839532/65734744-0aa9db00-e09a-11e9-9141-bdd1f74acc56.PNG)

After building from source I get a bunch of CPU warnings, can't bind to memory. Then failed to allocate RandomX dataset, switching to slow mode and Segmentation fault (core dumped).

The cpus are at stock clocks. Do I need more sticks of ddr4 memory or is the problem because i'm using engineering sample CPUs?


## xmrig | 2019-09-27T10:55:45+00:00
Disable NUMA support https://github.com/xmrig/xmrig/blob/master/src/config.json#L19 and try v4
You can't achieve maximum performance with current memory configuration, but why miner crash is still unknown.
Thank you.

## XMRUSD | 2019-09-27T12:50:59+00:00
I tried it with NUMA set to false on v4.1 and v3. Crash with the same results as above.

## xmrig | 2019-09-27T13:36:28+00:00
`cmake .. -DCMAKE_BUILD_TYPE=Debug`
`make`
`gdb xmrig`
`r`

After crash `bt` and show result.

If debug build not crash:
Change lines 19-23 to:
```
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wno-strict-aliasing")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -Ofast -g")

    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fexceptions -fno-rtti -Wno-strict-aliasing -Wno-class-memaccess")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Ofast -g")
```
Then:
`cmake .. -DCMAKE_BUILD_TYPE=Release` and `make`, etc.

## XMRUSD | 2019-09-27T14:25:26+00:00
![e1](https://user-images.githubusercontent.com/55839532/65776365-97d74900-e107-11e9-830b-637784d20e66.PNG)
![e2](https://user-images.githubusercontent.com/55839532/65776418-b63d4480-e107-11e9-9c3a-ea7b666a6f27.PNG)
![e3](https://user-images.githubusercontent.com/55839532/65776439-c3f2ca00-e107-11e9-97e5-ef7e02365dff.PNG)

I just start using Linux a couple of days ago. So I'm not sure what this stuff means.
Also thanks for helping though.

## theshadowpeople | 2019-11-13T04:16:16+00:00
Hello,
i have the same problem with my DUAL AMD EPYC CPU
https://github.com/xmrig/xmrig/issues/1266

Did you solve the problem ?

## XMRUSD | 2019-11-14T19:38:14+00:00
No, did not solve the problem. My guess is there might be something wrong with the engineering sample CPUs.

## xmrig | 2019-12-01T22:33:20+00:00
Disabling opcache in BIOS should fix the issue, not sure it possible on server motherboard, but please try https://github.com/xmrig/xmrig/pull/1348#issuecomment-560122919

## SChernykh | 2019-12-30T10:19:44+00:00
@XMRUSD XMRig 5.5.0 has a workaround for 1st gen Ryzen/Threadripper/EPYC crashes, you should be able to mine even with enabled Opcache.

## xq0404 | 2021-07-11T01:30:01+00:00
The problem seems to be OS-related.  It happened under Fedora and Ubuntu, but no problem under Windows 10.

# Action History
- Created by: XMRUSD | 2019-09-26T13:57:34+00:00
- Closed at: 2019-10-18T20:42:37+00:00
