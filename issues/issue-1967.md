---
title: epyc 7551 32 core CPU performance problem
source_url: https://github.com/xmrig/xmrig/issues/1967
author: WhoR3born
assignees: []
labels: []
created_at: '2020-12-06T15:53:44+00:00'
updated_at: '2021-04-12T14:33:14+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:33:14+00:00'
---

# Original Description
hi,
i have amd epyc 7551 32 core CPU
i checked benchmark https://xmrig.com/benchmark?cpu=AMD+EPYC+7551+32-Core+Processor
but im getting ~1970 H/s
i used config wizard. what should i do?

# Discussion History
## xmrig | 2020-12-06T16:04:29+00:00
Please show the miner log from the start.
Thank you.


## WhoR3born | 2020-12-06T16:09:35+00:00
Microsoft Windows [Version 10.0.17763.1577]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\ASrosTOS>cd C:\Users\ASrosTOS\Desktop\xmrig-6.6.2

C:\Users\ASrosTOS\Desktop\xmrig-6.6.2>xmrig.exe --av 7 --safe --max-cpu-usage 95 --cpu-priority 5
xmrig.exe: unknown option -- safe
 * ABOUT        XMRig/6.6.2 gcc/10.2.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1h hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD EPYC 7551 32-Core Processor (1) x64 AES
                L2:2.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       2.8/64.0 GB (4%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2020-12-06 16:02:30.476]  config   configuration saved to: "C:\Users\ASrosTOS\Desktop\xmrig-6.6.2\config.json"
 * OPENCL       disabled
 * CUDA         disabled
[2020-12-06 16:02:30.523]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.201.42
[2020-12-06 16:02:30.523]  net      fingerprint (SHA-256): "39a361115318e42377a8221cdbf9645d017e61f62ea58eefd8e9367dcdb3d88d"
[2020-12-06 16:02:30.539]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2246338
[2020-12-06 16:02:30.539]  cpu      use argon2 implementation AVX2
[2020-12-06 16:02:30.664]  msr      register values for "ryzen_17h" preset has been set successfully (135 ms)
[2020-12-06 16:02:30.664]  randomx  init dataset algo rx/0 (8 threads) seed 8889bccb4044d26e...
[2020-12-06 16:02:30.695]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (27 ms)
[2020-12-06 16:02:36.429]  randomx  dataset ready (5736 ms)
[2020-12-06 16:02:36.429]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2020-12-06 16:02:36.539]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (98 ms)
[2020-12-06 16:02:48.304]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2246339
[2020-12-06 16:02:56.320]  net      new job from pool.supportxmr.com:443 diff 63380 algo rx/0 height 2246339
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   461.6 |     n/a |     n/a |
|        1 |        2 |   460.4 |     n/a |     n/a |
|        2 |        4 |   462.2 |     n/a |     n/a |
|        3 |        6 |   462.1 |     n/a |     n/a |
|        - |        - |  1846.3 |     n/a |     n/a |
[2020-12-06 16:03:11.836]  miner    speed 10s/60s/15m 1846.3 n/a n/a H/s max 1874.8 H/s
[2020-12-06 16:03:33.148]  cpu      accepted (1/0) diff 63380 (23 ms)
[2020-12-06 16:03:37.445]  miner    speed 10s/60s/15m 1949.2 1869.1 n/a H/s max 1953.4 H/s
[2020-12-06 16:03:42.242]  cpu      accepted (2/0) diff 63380 (27 ms)
[2020-12-06 16:03:53.883]  cpu      accepted (3/0) diff 63380 (20 ms)
[2020-12-06 16:03:56.414]  net      new job from pool.supportxmr.com:443 diff 100620 algo rx/0 height 2246339
 - RESULTS
 * accepted         3 (100.0%)
 * pool-side hashes 190140 avg 63380
 * difficulty       100620
 * avg result time  29.5s
 - TOP 10
  # | DIFFICULTY | EFFORT % |
  1 |     225068 |    84.48 |
  2 |     181274 |   104.89 |
  3 |      80242 |   236.96 |
 - RESULTS
 * accepted         3 (100.0%)
 * pool-side hashes 190140 avg 63380
 * difficulty       100620
 * avg result time  31.1s
 - TOP 10
  # | DIFFICULTY | EFFORT % |
  1 |     225068 |    84.48 |
  2 |     181274 |   104.89 |
  3 |      80242 |   236.96 |
[2020-12-06 16:04:04.711]  signal   Ctrl+C received, exiting
[2020-12-06 16:04:04.711]  cpu      stopped (3 ms)

C:\Users\ASrosTOS\Desktop\xmrig-6.6.2>xmrig.exe --av 7 --safe --max-cpu-usage 95 --cpu-priority 5
xmrig.exe: unknown option -- safe
 * ABOUT        XMRig/6.6.2 gcc/10.2.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1h hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD EPYC 7551 32-Core Processor (1) x64 AES
                L2:2.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       2.8/64.0 GB (4%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:7777 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-12-06 16:04:38.340]  net      pool.supportxmr.com:7777 read error: "end of file"
[2020-12-06 16:04:44.372]  net      pool.supportxmr.com:7777 read error: "end of file"
[2020-12-06 16:04:47.348]  signal   Ctrl+C received, exiting

C:\Users\ASrosTOS\Desktop\xmrig-6.6.2>xmrig.exe --av 7 --safe --max-cpu-usage 95 --cpu-priority 5
xmrig.exe: unknown option -- safe
 * ABOUT        XMRig/6.6.2 gcc/10.2.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1h hwloc/2.2.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD EPYC 7551 32-Core Processor (1) x64 AES
                L2:2.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       2.8/64.0 GB (4%)
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.supportxmr.com:5555 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2020-12-06 16:05:19.279]  net      pool.supportxmr.com:5555 read error: "end of file"
[2020-12-06 16:05:25.293]  net      pool.supportxmr.com:5555 read error: "end of file"
[2020-12-06 16:05:31.315]  net      pool.supportxmr.com:5555 read error: "end of file"
[2020-12-06 16:05:36.353]  net      pool.supportxmr.com:5555 read error: "end of file"
[2020-12-06 16:05:37.478]  config   "C:\Users\ASrosTOS\Desktop\xmrig-6.6.2\config.json" was changed, reloading configuration
 * POOL #1      pool.supportxmr.com:443 algo auto
[2020-12-06 16:05:37.509]  net      use pool pool.supportxmr.com:443 TLSv1.2 104.140.201.42
[2020-12-06 16:05:37.509]  net      fingerprint (SHA-256): "39a361115318e42377a8221cdbf9645d017e61f62ea58eefd8e9367dcdb3d88d"
[2020-12-06 16:05:37.509]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2246339
[2020-12-06 16:05:37.509]  cpu      use argon2 implementation AVX2
[2020-12-06 16:05:37.634]  msr      register values for "ryzen_17h" preset has been set successfully (129 ms)
[2020-12-06 16:05:37.634]  randomx  init dataset algo rx/0 (8 threads) seed 8889bccb4044d26e...
[2020-12-06 16:05:37.665]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (27 ms)
[2020-12-06 16:05:43.665]  randomx  dataset ready (5993 ms)
[2020-12-06 16:05:43.665]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2020-12-06 16:05:43.775]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (106 ms)
[2020-12-06 16:05:43.853]  net      new job from pool.supportxmr.com:443 diff 88235 algo rx/0 height 2246339
[2020-12-06 16:05:59.243]  cpu      accepted (1/0) diff 88235 (33 ms)
[2020-12-06 16:06:43.947]  net      new job from pool.supportxmr.com:443 diff 60120 algo rx/0 height 2246339
[2020-12-06 16:06:45.056]  miner    speed 10s/60s/15m 1952.9 1920.3 n/a H/s max 1959.1 H/s
[2020-12-06 16:06:48.197]  cpu      accepted (2/0) diff 60120 (21 ms)
[2020-12-06 16:07:36.760]  cpu      accepted (3/0) diff 60120 (21 ms)
[2020-12-06 16:07:44.041]  net      new job from pool.supportxmr.com:443 diff 74431 algo rx/0 height 2246339
[2020-12-06 16:07:45.994]  cpu      accepted (4/0) diff 74431 (8 ms)
[2020-12-06 16:07:46.260]  miner    speed 10s/60s/15m 1956.7 1958.9 n/a H/s max 1970.3 H/s
[2020-12-06 16:08:44.151]  net      new job from pool.supportxmr.com:443 diff 68401 algo rx/0 height 2246339
[2020-12-06 16:08:47.558]  miner    speed 10s/60s/15m 1923.9 1901.1 n/a H/s max 1970.3 H/s
[2020-12-06 16:08:51.120]  net      new job from pool.supportxmr.com:443 diff 68401 algo rx/0 height 2246340


## xmrig | 2020-12-06T16:29:17+00:00
You use a virtual machine, with only 4 cores and 8 threads, the physical CPU has 32 cores and 64 threads, also virtual machine report only 8 MB of L3 cache, so autoconfig uses only 4 threads. You can run 8 threads (`-t 8`) it may increase hashrate.
Thank you.

## ahTy | 2021-01-11T08:29:52+00:00
> You use a virtual machine, with only 4 cores and 8 threads, the physical CPU has 32 cores and 64 threads, also virtual machine report only 8 MB of L3 cache, so autoconfig uses only 4 threads. You can run 8 threads (`-t 8`) it may increase hashrate.
> Thank you.

My cpu (E5 2620 V3) has 6 cores and 12 threads, but I can only use 6 threads when I work. I have added the parameter (-t 12), log printing still shows that there are 12 threads, but only 6 are used

## Spudz76 | 2021-01-13T20:39:25+00:00
@ahTy the E5 2620 V3 has 15M of cache
Can run 3 threads (of Heavy algo with 4M scratchpad size = 12M cache where 4 threads would overflow at 16M)
Can run 7 threads (of normal algo with 2M scratchpad size = 14M cache where 8 threads would overflow at 16M)
Can run 15 threads (of Lite algo with 1M scratchpad size = 15M cache, or full, but then you run out of threads first)
Pico algo can run way more than that (256K scratchpad size)

Most of the time the "fake" thread cores do not help, so you really have threads=cores or 6.

Non-cryptonight types may run differently (argon2, astrobwt) as they use resources differently than Cryptonight types.

And, no, system ram won't help.  We aren't just staying in cache because we're stupid.

## ahTy | 2021-01-14T02:22:56+00:00
> Heavy algo

How do i switch the ' Heavy algo' 'normal algo' 'Lite algo'?
I get the 'CPU.md' https://github.com/xmrig/xmrig/blob/master/doc/CPU.md
But it is not detailed at all. I don't know how i can switch

## Spudz76 | 2021-01-21T22:18:46+00:00
Join a pool that sends CN-Heavy (probably Haven) type jobs.  Whatever algo comes in the job is what the miner will switch to...
Easiest is to join MoneroOcean as they send whatever type of jobs fit your hardware and the profitability of the moment, but then payout as XMR always.  Note there is a special fork of xmrig/xmrig-cuda for use there that reports your hashrates per algo up to the pool so it can decide what algo is best to send.  It also re-enables CN-GPU which was removed from official miner for unknown reasons - it tends to be one of the most profitable algos on most of my garbage nVidia Fermi level hardware, when Haven does not win.  Also pretty good on AMD/OpenCL.

Otherwise you need to spin up your own Haven wallet and switch to a Haven pool, to get Haven jobs (and be paid in Haven, which you'd have to exchange unless you actually want to hold Haven coins for some reason).

# Action History
- Created by: WhoR3born | 2020-12-06T15:53:44+00:00
- Closed at: 2021-04-12T14:33:14+00:00
