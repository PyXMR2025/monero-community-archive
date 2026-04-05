---
title: xmrig not getting any jobs mining aeon and xmr
source_url: https://github.com/xmrig/xmrig/issues/300
author: akicked
assignees: []
labels: []
created_at: '2017-12-28T07:13:47+00:00'
updated_at: '2021-07-11T22:42:44+00:00'
type: issue
status: closed
closed_at: '2017-12-29T22:52:55+00:00'
---

# Original Description
Hello, im mining aeon on hashvaultpro pool. Everything was working normally until a few days miner disappeared from pool dashboard. Same results for xmr or aeon on different pools.
Sorry if this matter was already discussed in a past issue, or if i havent provided enough information.

root@*******desktop:/home/triadica/xmrig/build# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.3 LTS
Release:	16.04
Codename:	xenial



root@*******desktop:/home/triadica/xmrig/build# ./xmrig -o pool.supportxmr.com:3333 -u 4AjhoGSjw2kaVKJArdBJdB3zUGhMwLn4cLFpR3XJYYs6Jn7kweXBq36YGDtYbhYWSW9ovfVMnCrBjFGaovqeYx3jCu6jD8K -p ala -k  --max-cpu-usage=50 --donate-level=1
 * VERSIONS:     XMRig/2.4.3 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, disabled
 * CPU:          Intel(R) Core(TM) i3-4170 CPU @ 3.70GHz (1) x64 AES-NI
 * CPU L2/L3:    0.5 MB/3.0 MB
 * THREADS:      1, cryptonight, av=1, donate=1%
 * POOL #1:      pool.supportxmr.com:3333
 * COMMANDS:     hashrate, pause, resume
[2017-12-28 08:55:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:19] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:19] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:19] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:20] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:55:29] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:56:10] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:56:11] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:56:29] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:56:30] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:56:31] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:56:32] [pool.supportxmr.com:3333] connect error: "connection timed out"
[2017-12-28 08:57:29] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:58:29] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s

root@******desktop:/home/triadica/xmrig/build# ./xmrig -a cryptonight-lite -o pool.aeon.hashvault.pro:5555 -u WmteFqRaovXTphNG7hcRhZPwn44VuSUdZ5vkTTpEkAxvVmpjXdMsMmbLp8mBr65fBr5yVSiFAULoZAyLmxRhJRrj28EyYHnuF -p ala1 -k --max-cpu-usage=50  --donate-level=1 
 * VERSIONS:     XMRig/2.4.3 libuv/1.8.0 gcc/7.1.0
 * HUGE PAGES:   available, disabled
 * CPU:          Intel(R) Core(TM) i3-4170 CPU @ 3.70GHz (1) x64 AES-NI
 * CPU L2/L3:    0.5 MB/3.0 MB
 * THREADS:      1, cryptonight-lite, av=2, donate=1%
 * POOL #1:      pool.aeon.hashvault.pro:5555
 * COMMANDS:     hashrate, pause, resume
[2017-12-28 08:38:36] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:38:38] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:38:38] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:38:38] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:01] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:01] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:01] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:01] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:01] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:01] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:39:02] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2017-12-28 08:41:30] [pool.aeon.hashvault.pro:5555] connect error: "connection timed out"




# Discussion History
## xmrig | 2017-12-28T07:45:54+00:00
Miner not connected to pool, if miner connected you should see messages **use pool** and **new job from**. Maybe your internet provider block stratum traffic.
Thank you.

## akicked | 2017-12-28T07:49:49+00:00
Actually this problem ocurred after our office had some connection issues, though everything is okay with the connection now. We are changing ISP tomorrow, so i'l keep the issue open until then.
Thanks for the quick reply.

## akicked | 2017-12-29T22:52:55+00:00
Switched to a different network and everything is ok, guess local network admin blocked stratum traffic like You said. Thanks.

## mousakefa62 | 2021-07-11T22:42:44+00:00
Is this message being extracted and connected to the pool?

Thanks for the tips

[2021-07-12 03:06:47.766]  net      new job from rx.unmineable.com:3333 diff 100
001 algo rx/0 height 2402726
[2021-07-12 03:07:02.799]  net      new job from rx.unmineable.com:3333 diff 100
001 algo rx/0 height 2402726
[2021-07-12 03:07:17.792]  net      new job from rx.unmineable.com:3333 diff 100
001 algo rx/0 height 2402726
[2021-07-12 03:07:32.777]  net      new job from rx.unmineable.com:3333 diff 100
001 algo rx/0 height 2402726
[2021-07-12 03:07:34.072]  net      new job from rx.unmineable.com:3333 diff 100
001 algo rx/0 height 2402726
[2021-07-12 03:07:46.010]  miner    speed 10s/60s/15m n/a n/a 0.01 H/s max 0.11
H/s

# Action History
- Created by: akicked | 2017-12-28T07:13:47+00:00
- Closed at: 2017-12-29T22:52:55+00:00
