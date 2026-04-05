---
title: CPU Mining on Ubuntu much slower than on Windows?
source_url: https://github.com/xmrig/xmrig/issues/1464
author: To-Life
assignees: []
labels:
- question
created_at: '2019-12-26T10:07:00+00:00'
updated_at: '2020-01-05T13:09:08+00:00'
type: issue
status: closed
closed_at: '2020-01-05T13:09:08+00:00'
---

# Original Description
I have two PCs with same hardware and same OS ( windows 10 ), the hashrates of them are almost same on 1800H~2000H/s.

I want to know how about the performance on ubuntu, then I changed one from win10 to ubuntu 18.04, the hashrates is 950H~1050H/s, I'm quite surprised by this, I expected running directly on Linux to be at least a little bit faster; instead it's significantly slower.

so any ideas what I'm doing wrong? Thanks!

# Discussion History
## xmrig | 2019-12-26T18:08:16+00:00
You not shown miner log, so I guess it hugepages issue https://xmrig.com/docs/miner/hugepages
Thank you.

## To-Life | 2019-12-30T13:16:50+00:00
Both Ubuntu & windows already enable  Hugepages

###Ubuntu log :
* ABOUT        XMRig/5.4.0 gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-8500 CPU @ 3.00GHz (1) x64 AES
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       1.9/7.7 GB (25%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-30 21:09:24.515]  net  use pool xmr.f2pool.com:13531  203.107.32.162
[2019-12-30 21:09:24.515]  net  new job from xmr.f2pool.com:13531 diff 32768 algo rx/0 height 2000270
[2019-12-30 21:09:24.520]  msr  msr kernel module is not available
[2019-12-30 21:09:24.520]  rx   init dataset algo rx/0 (6 threads) seed 71c1d80e15c28703...
[2019-12-30 21:09:24.521]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2019-12-30 21:09:30.041]  rx   dataset ready (5520 ms)
[2019-12-30 21:09:30.041]  cpu  use profile  rx  (3 threads) scratchpad 2048 KB
[2019-12-30 21:09:30.082]  cpu  READY threads 3/3 (3) huge pages 100% 3/3 memory 6144 KB (40 ms)
[2019-12-30 21:09:38.744]  net  new job from xmr.f2pool.com:13531 diff 32768 algo rx/0 height 2000270
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   342.9 |     n/a |     n/a |
|        1 |        2 |   344.2 |     n/a |     n/a |
|        2 |        4 |   340.4 |     n/a |     n/a |
|        - |        - |  1027.4 |     n/a |     n/a |
[2019-12-30 21:10:05.277] speed 10s/60s/15m 1027.4 n/a n/a H/s max 1028.2 H/s

----------------------------------------------------------------------------------------------

###windows log :
* ABOUT        XMRig/5.1.0 MSVC/2017
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          Intel(R) Core(TM) i5-8500 CPU @ 3.00GHz (1) x64 AES
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       2.2/8.0 GB (28%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-30 21:15:14.604]  net  use pool xmr.f2pool.com:13531  203.107.32.162
[2019-12-30 21:15:14.605]  net  new job from xmr.f2pool.com:13531 diff 32768 algo rx/0 height 2000274
[2019-12-30 21:15:14.605]  rx   init dataset algo rx/0 (6 threads) seed 71c1d80e15c28703...
[2019-12-30 21:15:14.615]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (10 ms)
[2019-12-30 21:15:19.657]  rx   dataset ready (5042 ms)
[2019-12-30 21:15:19.657]  cpu  use profile  rx  (3 threads) scratchpad 2048 KB
[2019-12-30 21:15:19.700]  cpu  READY threads 3/3 (3) huge pages 100% 3/3 memory 6144 KB (43 ms)
[2019-12-30 21:15:32.365]  cpu  accepted (1/0) diff 32768 (27 ms)
[2019-12-30 21:16:03.855]  cpu  accepted (2/0) diff 32768 (28 ms)
[2019-12-30 21:16:15.652]  net  new job from xmr.f2pool.com:13531 diff 32768 algo rx/0 height 2000274
[2019-12-30 21:16:19.785] speed 10s/60s/15m 1942.9 n/a n/a H/s max 1942.9 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   624.7 |   624.5 |     n/a |
|        1 |        2 |   638.7 |   638.0 |     n/a |
|        2 |        4 |   663.0 |   662.3 |     n/a |
|        - |        - |  1926.4 |  1924.9 |     n/a |
[2019-12-30 21:16:29.681] speed 10s/60s/15m 1926.4 1924.9 n/a H/s max 1942.9 H/s

## SChernykh | 2019-12-30T16:21:10+00:00
@To-Life XMRig couldn't allocate dataset with huge pages on Ubuntu, increase `vm.nr_hugepages` to 1200.

## To-Life | 2019-12-31T02:17:39+00:00
@SChernykh changed to 1280 , hashrates up to 1400H, but still not arrive 1900H.

$ ./xmrig
* ABOUT        XMRig/5.4.0 gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-8500 CPU @ 3.00GHz (1) x64 AES
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       3.7/7.7 GB (47%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume
 * OPENCL       disabled
 * CUDA         disabled
[2019-12-31 10:12:11.026]  net  use pool xmr.f2pool.com:13531  47.101.30.124
[2019-12-31 10:12:11.026]  net  new job from xmr.f2pool.com:13531 diff 32768 algo rx/0 height 2000684
[2019-12-31 10:12:11.031]  msr  msr kernel module is not available
[2019-12-31 10:12:11.031]  rx   init dataset algo rx/0 (6 threads) seed 71c1d80e15c28703...
[2019-12-31 10:12:11.205]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (173 ms)
[2019-12-31 10:12:16.217]  rx   dataset ready (5013 ms)
[2019-12-31 10:12:16.217]  cpu  use profile  rx  (3 threads) scratchpad 2048 KB
[2019-12-31 10:12:16.258]  cpu  READY threads 3/3 (3) huge pages 100% 3/3 memory 6144 KB (40 ms)
[2019-12-31 10:12:39.028]  cpu  accepted (1/0) diff 32768 (26 ms)
[2019-12-31 10:12:56.859]  cpu  accepted (2/0) diff 32768 (25 ms)
[2019-12-31 10:13:16.257] speed 10s/60s/15m 1391.3 n/a n/a H/s max 1392.8 H/s

$ cat /proc/meminfo | grep Huge
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
HugePages_Total:    1280
HugePages_Free:      109
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:         2621440 kB


---------------------------------config.json
[config.json.txt](https://github.com/xmrig/xmrig/files/4011754/config.json.txt)


## SChernykh | 2019-12-31T08:30:02+00:00
I can see that you have affinity 0,2,4 for Ubuntu, this is usually wrong - try to regenerate config from scratch with latest XMRig (use https://xmrig.com/wizard)

## To-Life | 2020-01-05T13:09:08+00:00
thanks all, will take more testing.

# Action History
- Created by: To-Life | 2019-12-26T10:07:00+00:00
- Closed at: 2020-01-05T13:09:08+00:00
