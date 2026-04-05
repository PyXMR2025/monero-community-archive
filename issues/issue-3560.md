---
title: I get too many rejects using v6.12.2
source_url: https://github.com/xmrig/xmrig/issues/3560
author: ramp10er
assignees: []
labels: []
created_at: '2024-10-13T08:30:19+00:00'
updated_at: '2024-10-13T11:36:40+00:00'
type: issue
status: closed
closed_at: '2024-10-13T11:36:40+00:00'
---

# Original Description
Hi! I get too many rejects using **XMRIG v6.12.2**... My RANDOM X mode is set too light and using **XMRIG PROXY v6.21.1** as well. All the shares I submitted was all invalid shares. Other newer version does not work as well, but **XMRIG v5.0.1** works fine but not quite satisfied with the hash rate I've been getting since it does not have mode optimization for random x... I would like to know what's causing this behavior?!

**Below is the log result that I've been getting:**

 * ABOUT        XMRig/6.12.2 **MSVC/2019**
 * LIBS         **libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1**
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          AMD A10-6800K APU with Radeon(tm) HD Graphics (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       3.5/7.2 GB (48%)
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR3 @ 1600 MHz HX318C10F/8       
 * MOTHERBOARD  MSI - FM2-A55M-E33 (MS-7721)
 * DONATE       1%
 * ASSEMBLY     auto:bulldozer
 * POOL #1      127.0.0.1:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2024-10-12 18:14:04.694]  net      use pool 127.0.0.1:3333  127.0.0.1
[2024-10-12 18:14:04.694]  net      new job from 127.0.0.1:3333 diff 10000 algo rx/0 height 3257355
[2024-10-12 18:14:04.694]  cpu      use argon2 implementation SSSE3
[2024-10-12 18:14:04.694]  randomx  init dataset algo rx/0 (4 threads) seed bf513dbe52c22b09...
[2024-10-12 18:14:04.710]  randomx  fast RandomX mode disabled by config
[2024-10-12 18:14:04.710]  randomx  failed to allocate RandomX dataset, switching to slow mode (3 ms)
[2024-10-12 18:14:05.833]  randomx  dataset ready (1117 ms)
[2024-10-12 18:14:05.833]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2024-10-12 18:14:05.849]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (2 ms)
[2024-10-12 18:14:15.957]  net      new job from 127.0.0.1:3333 diff 5000 algo rx/0 height 3257355
[2024-10-12 18:14:16.644]  miner    speed 10s/60s/15m 1543.2 n/a n/a H/s max 1668.5 H/s
[2024-10-12 18:14:18.516]  net      new job from 127.0.0.1:3333 diff 10000 algo rx/0 height 3257356
[2024-10-12 18:14:21.979]  miner    speed 10s/60s/15m 1543.2 n/a n/a H/s max 1668.5 H/s
[2024-10-12 18:14:22.338]  cpu      rejected (0/1) diff 10000 "Invalid share" (71 ms)
[2024-10-12 18:14:22.369]  cpu      rejected (0/2) diff 10000 "Invalid share" (71 ms)
[2024-10-12 18:14:22.525]  cpu      rejected (0/3) diff 10000 "Invalid share" (71 ms)
[2024-10-12 18:14:22.785]  signal   SIGHUP received, exiting
[2024-10-12 18:14:22.785]  cpu      stopped (3 ms)

 I was thinking it has something to do with the version of **MSVC, OpenSSL or hwloc** since both XMRIG version that I have just mentioned above are both different with those category,

**Below is also an image of my redistributable versions:**

![Redis](https://github.com/user-attachments/assets/797be521-8ec4-41a0-b444-39507e972c7c)

By the way I am using WINDOWS 7 as my OS. Not quite sure if this was the reason as well.

I am not quite sure if all the xmrig versions that mining pool is endorsing are working for others, but I am quite sure they don't work for me except xmrig v5.+

Hope for your response and solution in the future...

# Discussion History
## SChernykh | 2024-10-13T09:19:56+00:00
If you get all invalid shares, your system is unstable because the same XMRig binary can produce valid shares on other systems.

## SChernykh | 2024-10-13T09:22:32+00:00
What hashrate do you get with v5.0.1? Can you find the latest XMRig version that still works for you?

## ramp10er | 2024-10-13T11:20:04+00:00
I get a hash rate around 200-400h/s with xmrig v5.0.1 or <= v5.11.1, but above those I always get an invalid share.  I just wish I could get the hash rate I get with newer ones which is around 4-6 kh/s that will be a big boost. 

## SChernykh | 2024-10-13T11:22:37+00:00
You need to run full dataset mode, not slow mode to get good hashrate. Best registered hashrate for your CPU is 894 h/s: https://xmrig.com/benchmark/2eF467 - and it uses v6.12.2 too, so this version should work with this CPU. Your system is probably unstable.

## ramp10er | 2024-10-13T11:36:22+00:00
Thanks! I'll try fix any errors on my system.

# Action History
- Created by: ramp10er | 2024-10-13T08:30:19+00:00
- Closed at: 2024-10-13T11:36:40+00:00
