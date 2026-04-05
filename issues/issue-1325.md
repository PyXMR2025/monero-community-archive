---
title: the xmrig v5.0.1 works fine with cn/r but crash with rx/o on my computer(including
  the log file)
source_url: https://github.com/xmrig/xmrig/issues/1325
author: befeiab
assignees: []
labels: []
created_at: '2019-11-28T06:03:21+00:00'
updated_at: '2021-04-12T15:27:11+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:27:11+00:00'
---

# Original Description
 * ABOUT        XMRig/5.0.1 gcc/8.2.1
 * LIBS         libuv/1.19.2 
 * HUGE PAGES   permission granted
 * CPU          Intel(R) Core(TM) i7-3612QM CPU @ 2.10GHz (1) x64 AES
                L2:1.0 MB L3:6.0 MB 4C/8T
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      rx.minexmr.com:4444 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-11-28 13:48:17.158] [rx.minexmr.com:4444] state: "host-lookup"
[2019-11-28 13:48:17.160] [rx.minexmr.com:4444] state: "connecting"
[2019-11-28 13:48:17.395] [rx.minexmr.com:4444] state: "connected"
[2019-11-28 13:48:17.738]  net  use pool rx.minexmr.com:4444  rx.minexmr.com
[2019-11-28 13:48:17.741]  net  new job from rx.minexmr.com:4444 diff 9000 algo rx/0 height 1352641
[2019-11-28 13:48:17.745]  rx   init dataset algo rx/0 (8 threads) seed 656ba2a2a6f10735...

# Discussion History
## befeiab | 2019-11-28T06:05:33+00:00
Maybe some exception is needed to support

## SChernykh | 2019-11-28T09:44:38+00:00
It looks like it fails to allocate memory for dataset. How much RAM do you have? Is any other memory-intensive software (like web-browser) running when you test it?

## befeiab | 2019-11-29T05:00:28+00:00
8GB,the RAM is enough

## aa-delite | 2019-12-05T12:55:05+00:00
Same here. I have null hashrate on ryzen 2200G (8gb ram) using 5.1.1. It does not crash, but mining nothing with null hashrate, using much RAM and intensive swapping to disk.
Can't fix it on that machine. Most my PCs works well, even ryzen 1xxx series.
I see you're using Intel CPU, so it's not only AMD issue i guess.

## aa-delite | 2019-12-06T00:14:30+00:00
Do you see 100% huge pages (green)? Something like that:
allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT

# Action History
- Created by: befeiab | 2019-11-28T06:03:21+00:00
- Closed at: 2021-04-12T15:27:11+00:00
