---
title: miner unexpectedly slows down
source_url: https://github.com/xmrig/xmrig/issues/2193
author: sectorKS
assignees: []
labels:
- question
created_at: '2021-03-19T15:33:41+00:00'
updated_at: '2021-04-12T13:54:56+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:54:56+00:00'
---

# Original Description
Hello,

I sometimes notice strange behavior of miner. Miner is running normally and then all of sudden it slows down to few H/s. It happens rarely but I noticed it couple of times already. I noticed this on windows builds only, v6.9.0 and v6.10.0 running on Win10 on different PCs. Once it slows down it stays at low essentially 0 speed and needs to be restarted.
On linux it does not occur.

Example log:

>  * ABOUT        XMRig/6.9.0 MSVC/2019
>  * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
>  * HUGE PAGES   permission granted
>  * 1GB PAGES    unavailable
>  * CPU          Intel(R) Core(TM) i3-9100 CPU @ 3.60GHz (1) 64-bit AES
>                 L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
>  * MEMORY       2.0/7.8 GB (26%)
>                 DIMM1: 8 GB DDR4 @ 2400 MHz M378A1K43CB2-CTD    
>                 DIMM3: <empty>
>  ..
>  * ASSEMBLY     auto:intel
>  * POOL #1      xmrpool.eu:5555 algo auto
>  * COMMANDS     hashrate, pause, resume, results, connection
>  * OPENCL       disabled
>  * CUDA         disabled
> ..
> **[2021-03-19 15:16:01.447]  miner    speed 10s/60s/15m 1856.2 1854.6 1853.5 H/s max 2112.5 H/s (NORMAL HASH SPEED)**
> [2021-03-19 15:16:12.016]  cpu      accepted (26252/0) diff 46197 (52 ms)
> [2021-03-19 15:16:17.497]  cpu      accepted (26253/0) diff 46197 (88 ms)
> [2021-03-19 15:16:23.890]  net      new job from xmrpool.eu:5555 diff 46197 algo rx/0 height 2320456
> [2021-03-19 15:17:18.298]  cpu      accepted (26254/0) diff 46197 (37 ms)
> ..
> [2021-03-19 15:21:07.174]  cpu      accepted (26259/0) diff 46197 (42 ms)
> **[2021-03-19 15:21:07.799]  miner    speed 10s/60s/15m 1852.7 1853.5 1852.3 H/s max 2112.5 H/s (NORMAL HASH SPEED)**
> [2021-03-19 15:21:18.579]  net      new job from xmrpool.eu:5555 diff 32431 algo rx/0 height 2320457
> [2021-03-19 15:21:20.657]  cpu      accepted (26260/0) diff 32431 (56 ms)
> ..
> [2021-03-19 15:25:47.110]  cpu      accepted (26275/0) diff 43242 (37 ms)
> [2021-03-19 15:25:56.165]  cpu      accepted (26276/0) diff 43242 (74 ms)
> **[2021-03-19 15:26:14.258]  miner    speed 10s/60s/15m 1851.9 1854.1 1852.4 H/s max 2112.5 H/s (NORMAL HASH SPEED)**
> [2021-03-19 15:26:43.621]  net      new job from xmrpool.eu:5555 diff 63865 algo rx/0 height 2320459
> [2021-03-19 15:26:54.197]  net      new job from xmrpool.eu:5555 diff 63865 algo rx/0 height 2320460
> [2021-03-19 15:27:48.617]  net      new job from xmrpool.eu:5555 diff 31933 algo rx/0 height 2320460
> [2021-03-19 15:28:13.055]  cpu      accepted (26277/0) diff 31933 (43 ms)
> [2021-03-19 15:28:24.179]  cpu      accepted (26278/0) diff 31933 (36 ms)
> [2021-03-19 15:28:41.631]  net      new job from xmrpool.eu:5555 diff 31933 algo rx/0 height 2320461
> [2021-03-19 15:28:50.509]  cpu      accepted (26279/0) diff 31933 (52 ms)
> [2021-03-19 15:28:51.044]  cpu      accepted (26280/0) diff 31933 (40 ms)
> [2021-03-19 15:28:51.061]  cpu      accepted (26281/0) diff 31933 (37 ms)
> [2021-03-19 15:28:53.618]  net      new job from xmrpool.eu:5555 diff 47900 algo rx/0 height 2320461
> [2021-03-19 15:29:32.379]  cpu      accepted (26282/0) diff 47900 (37 ms)
> [2021-03-19 15:29:58.616]  net      new job from xmrpool.eu:5555 diff 28039 algo rx/0 height 2320461
> [2021-03-19 15:30:00.000]  cpu      accepted (26283/0) diff 28039 (54 ms)
> [2021-03-19 15:30:07.043]  cpu      accepted (26284/0) diff 28039 (74 ms)
> [2021-03-19 15:30:19.237]  cpu      accepted (26285/0) diff 28039 (52 ms)
> [2021-03-19 15:30:38.404]  net      new job from xmrpool.eu:5555 diff 28039 algo rx/0 height 2320462
> **[2021-03-19 15:31:21.522]  miner    speed 10s/60s/15m 2.33 515.0 1763.8 H/s max 2112.5 H/s (!!! SLOW HASH SPEED !!!)**
> [2021-03-19 15:32:08.628]  net      new job from xmrpool.eu:5555 diff 17145 algo rx/0 height 2320462
> [2021-03-19 15:32:49.796]  net      new job from xmrpool.eu:5555 diff 17145 algo rx/0 height 2320463
> [2021-03-19 15:33:13.627]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320463
> [2021-03-19 15:33:18.273]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320464
> [2021-03-19 15:33:24.576]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320465
> [2021-03-19 15:35:09.187]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320466
> **[2021-03-19 15:36:32.652]  miner    speed 10s/60s/15m 2.32 2.64 1125.1 H/s max 2112.5 H/s (!!! SLOW HASH SPEED !!!)**
> [2021-03-19 15:39:09.926]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320466
> **[2021-03-19 15:41:43.930]  miner    speed 10s/60s/15m 2.72 2.79 484.4 H/s max 2112.5 H/s (!!! SLOW HASH SPEED !!!)**
> [2021-03-19 15:42:25.753]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320467
> [2021-03-19 15:44:51.214]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320468
> **[2021-03-19 15:46:55.606]  miner    speed 10s/60s/15m 2.73 2.69 2.74 H/s max 2112.5 H/s (!!! SLOW HASH SPEED !!!)**
> [2021-03-19 15:48:51.691]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320468
> [2021-03-19 15:49:35.655]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320469
> [2021-03-19 15:49:44.527]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320470
> **[2021-03-19 15:52:07.266]  miner    speed 10s/60s/15m 2.92 2.68 2.71 H/s max 2112.5 H/s (!!! SLOW HASH SPEED !!!)**
> [2021-03-19 15:53:24.457]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320471
> [2021-03-19 15:56:34.616]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320472
> **[2021-03-19 15:57:20.253]  miner    speed 10s/60s/15m 2.43 2.57 2.64 H/s max 2112.5 H/s (!!! SLOW HASH SPEED !!!)**
> [2021-03-19 15:58:31.425]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320473
> [2021-03-19 15:58:37.055]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320474
> [2021-03-19 16:01:56.101]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320475
> [2021-03-19 16:02:31.268]  net      new job from xmrpool.eu:5555 diff 9600 algo rx/0 height 2320476
> **[2021-03-19 16:02:33.245]  miner    speed 10s/60s/15m 2.71 2.50 2.59 H/s max 2112.5 H/s (!!! SLOW HASH SPEED !!!)**
> [2021-03-19 16:03:23.418]  cpu      accepted (26286/0) diff 9600 (58 ms)

Anyone else having this problem?



# Discussion History
## SChernykh | 2021-03-19T15:41:57+00:00
Turn off `RunFullMemoryDiagnostic` task in Windows Task Scheduler: https://www.reddit.com/r/MoneroMining/comments/ijal60/randomx_stability_troubleshooting_guide/

## sectorKS | 2021-03-19T16:18:27+00:00
Many thanks. I was not aware of this.

# Action History
- Created by: sectorKS | 2021-03-19T15:33:41+00:00
- Closed at: 2021-04-12T13:54:56+00:00
