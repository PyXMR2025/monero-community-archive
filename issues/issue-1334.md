---
title: crash with Epyc es cpu
source_url: https://github.com/xmrig/xmrig/issues/1334
author: EicHub
assignees: []
labels:
- bug
- opcache
created_at: '2019-11-30T05:23:20+00:00'
updated_at: '2020-06-02T14:34:59+00:00'
type: issue
status: closed
closed_at: '2020-06-02T14:34:59+00:00'
---

# Original Description
* ABOUT        XMRig/5.0.1 gcc/9.2.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          AMD Eng Sample: 2S1405A3VIHF4_28/14_N (2) x64 AES
                L2:32.0 MB L3:128.0 MB 64C/128T NUMA:8
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      randomx-benchmark.xmrig.com:7777 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-11-30 13:19:42.487]  net  use pool randomx-benchmark.xmrig.com:7777  178.128.242.134
[2019-11-30 13:19:42.487]  net  new job from randomx-benchmark.xmrig.com:7777 diff 83350598 algo rx/0 height 1354352
[2019-11-30 13:19:42.487]  rx   init datasets algo rx/0 (128 threads) seed 9df22d829fdfc780...
[2019-11-30 13:19:42.518]  rx   #0 allocated 2080 MB huge pages 100% (28 ms)
[2019-11-30 13:19:42.518]  rx   #1 allocated 2080 MB huge pages 100% (30 ms)
[2019-11-30 13:19:42.518]  rx   #6 allocated 2080 MB huge pages 100% (29 ms)
[2019-11-30 13:19:42.518]  rx   #4 allocated 2080 MB huge pages 100% (30 ms)
[2019-11-30 13:19:42.518]  rx   #3 allocated 2080 MB huge pages 100% (31 ms)
[2019-11-30 13:19:42.518]  rx   #2 allocated 2080 MB huge pages 100% (31 ms)
[2019-11-30 13:19:42.518]  rx   #7 allocated 2080 MB huge pages 100% (32 ms)
[2019-11-30 13:19:42.674]  rx   #5 allocated 2080 MB huge pages 100% (182 ms)
[2019-11-30 13:19:42.674]  rx   #0 allocated  256 MB huge pages 100% +JIT (3 ms)
[2019-11-30 13:19:42.674]  rx   -- allocated 16896 MB huge pages 100% 8448/8448 (187 ms)
[2019-11-30 13:19:45.049]  rx   #0 dataset ready (2376 ms)
[2019-11-30 13:19:45.924]  rx   #2 dataset ready (869 ms)
[2019-11-30 13:19:45.924]  rx   #1 dataset ready (869 ms)
[2019-11-30 13:19:45.924]  rx   #7 dataset ready (870 ms)
[2019-11-30 13:19:46.424]  rx   #3 dataset ready (1374 ms)
[2019-11-30 13:19:46.456]  rx   #6 dataset ready (1409 ms)
[2019-11-30 13:19:46.471]  rx   #5 dataset ready (1420 ms)
[2019-11-30 13:19:46.471]  rx   #4 dataset ready (1420 ms)
[2019-11-30 13:19:46.471]  cpu  use profile  rx  (49 threads) scratchpad 2048 KB

How can i fix it?

# Discussion History
## EicHub | 2019-12-01T12:33:34+00:00
Numa false and use 20-25 thread it work, but hash only 17K

## xmrig | 2019-12-01T22:38:52+00:00
Disabling opcache in BIOS should fix the issue, not sure it possible on server motherboard, but please try https://github.com/xmrig/xmrig/pull/1348#issuecomment-560122919

## EicHub | 2019-12-02T00:49:19+00:00
Opcache option not found in my motherboard bios
But after I repeatedly turned it on many times, I was able to mine correctly after adjusting the CPU frequency, although the hashrate was not good。
However, after each restart of the server, it takes a lot of time to adjust and many times to start mining to work properly.

## SChernykh | 2019-12-30T10:19:21+00:00
@wyzdic XMRig 5.5.0 has a workaround for 1st gen Ryzen/Threadripper/EPYC crashes, you should be able to mine even with enabled Opcache.

# Action History
- Created by: EicHub | 2019-11-30T05:23:20+00:00
- Closed at: 2020-06-02T14:34:59+00:00
