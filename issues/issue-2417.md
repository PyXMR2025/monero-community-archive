---
title: Bus error on ARMv7 devices
source_url: https://github.com/xmrig/xmrig/issues/2417
author: sugrob
assignees: []
labels:
- bug
- arm
created_at: '2021-06-01T05:33:30+00:00'
updated_at: '2022-06-27T19:49:45+00:00'
type: issue
status: closed
closed_at: '2022-06-27T19:49:45+00:00'
---

# Original Description
**Describe the bug**
Hi. When I try to run XMRig on any of my armv7 devices, always get a Bus error. Tested on Orange pi PC, one, Odroid C1.

 * ABOUT        XMRig/6.12.2 gcc/9.3.0
 * LIBS         libuv/1.34.2 OpenSSL/1.1.1f hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A7 (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.3/1.0 GB (32%)
 * DONATE       1%
 * POOL #1      pool.minexmr.com:4444 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-06-01 08:21:51.961]  net      use pool pool.minexmr.com:4444  94.130.165.85
[2021-06-01 08:21:51.961]  net      new job from pool.minexmr.com:4444 diff 75000 algo rx/0 height 2373444
[2021-06-01 08:21:51.961]  cpu      use argon2 implementation default
[2021-06-01 08:21:53.162]  randomx  init dataset algo rx/0 (4 threads) seed b513e39fad73b944...
[2021-06-01 08:21:53.162]  randomx  not enough memory for RandomX dataset
[2021-06-01 08:21:53.163]  randomx  failed to allocate RandomX dataset, switching to slow mode (0 ms)
Bus error

**To Reproduce**
All common steps
.. 
cmake .. -DARM_TARGET=7
make -j$(nproc)

and than run
./build/xmrig  -o pool.minexmr.com:4444 -u WALLET -t 1
I've  experimented with flags, but no result. Any way, all this flags works fine on Raspberry pi 3b+/4

I tried on Armbian and DietPi. Result is same - Bus error


# Discussion History
## Spudz76 | 2021-06-01T11:18:51+00:00
Not blaming directly, but those deps are pretty ancient.  Use `cd scripts && bash ./build_deps.sh` to generate the supported/ideal dep versions rather than using (old) distro ones.  When the three-package build cycle is done, you add `-DXMRIG_DEPS=../scripts/deps` assuming you're in a single-depth `build` subfolder.

## SChernykh | 2021-06-01T11:32:55+00:00
This is a 32-bit Cortex-A7 with only 1 GB memory, I will be surprised it would do more than 1 h/s even if it compiles and runs fine. RandomX is too heavy for this hardware.

## Spudz76 | 2021-06-01T11:41:12+00:00
Good point, I missed looking at which algo and how much RAM...

## sugrob | 2021-06-01T20:16:30+00:00
> This is a 32-bit Cortex-A7 with only 1 GB memory, I will be surprised it would do more than 1 h/s even if it compiles and runs fine. RandomX is too heavy for this hardware.

I found a way how to mine 112h/s on Raspberry Pi 4 and I want to make a comparing various ARM MicroPC, but many of them based on ARMV7.
And no, seems 1GB RAM is enough, because I have tested on RPI 3, 3B+ and 4 1GB and all of them works fine.

## SChernykh | 2021-06-01T20:21:51+00:00
Raspberry Pi 4 is 64-bit and 4-8 GB RAM, it runs at full speed with JIT compilation. 1 GB RAM means light mode: 10x slower. 32-bit means another 5x slowdown because it runs in RandomX VM interpreter mode.

## Mauker1 | 2022-03-11T15:12:24+00:00
> > This is a 32-bit Cortex-A7 with only 1 GB memory, I will be surprised it would do more than 1 h/s even if it compiles and runs fine. RandomX is too heavy for this hardware.
> 
> I found a way how to mine 112h/s on Raspberry Pi 4 and I want to make a comparing various ARM MicroPC, but many of them based on ARMV7. And no, seems 1GB RAM is enough, because I have tested on RPI 3, 3B+ and 4 1GB and all of them works fine.

Hey man, can you share how did you manage to get it running on a raspi 4? I have a 2gig and a 4gig one and I can't make it run :/ Same "bus error" here.

Edit: Ok, in my case the problem was that I was trying to run xmrig on a 32 bits OS instead of 64 bits one. When I switched it, I could run the miner no problem, getting around 100 H/s.

## benthetechguy | 2022-06-27T19:19:56+00:00
Fixed in latest release. Can @xmrig @SChernykh please close this?

# Action History
- Created by: sugrob | 2021-06-01T05:33:30+00:00
- Closed at: 2022-06-27T19:49:45+00:00
