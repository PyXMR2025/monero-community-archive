---
title: xmrig 2.5.1 and xmrig-proxy 2.5.0 pool loop didnt working
source_url: https://github.com/xmrig/xmrig/issues/478
author: adi3yz
assignees: []
labels:
- bug
created_at: '2018-03-25T22:31:06+00:00'
updated_at: '2018-04-10T09:22:25+00:00'
type: issue
status: closed
closed_at: '2018-04-10T09:22:25+00:00'
---

# Original Description
xmrig 2.5.0 pool loop work nice but 2.5.1 didnt
hope u can check that.. ty
or did i need use new config var setting for loop?

# Discussion History
## xmrig | 2018-03-26T03:14:47+00:00
Please explain you question, what loop?
Thank you.

## adi3yz | 2018-03-26T03:36:05+00:00
my config setting
    "algo": "cryptonight",
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 5,
    "log-file": null,
    "max-cpu-usage": 75,
    "print-time": 60,
    "retries": 6,
    "retry-pause": 5,
    "safe": false,

here when i run xmrig
* VERSIONS:     XMRig/2.5.1 libuv/1.19.2 gcc/7.3.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Core(TM) i7-4500U CPU @ 1.80GHz (1) x64 AES-NI
 * CPU L2/L3:    0.5 MB/4.0 MB
 * THREADS:      2, cryptonight, av=1, donate=5%
 * POOL #1:      192.168.1.99:7777
 * POOL #2:      pool.monero.hashvault.pro:5555
 * POOL #3:      cryptonight.eu.nicehash.com:3355
 * COMMANDS:     hashrate, pause, resume
[2018-03-26 11:27:44] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 11:28:46] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-03-26 11:29:46] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-03-26 11:30:46] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-03-26 11:31:46] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-03-26 11:32:46] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-03-26 11:33:46] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-03-26 11:34:46] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s

xmrig didnt change to second pool #2 as setting.. also didnt do retry connect pool #1


## xmrig | 2018-03-26T03:54:41+00:00
I confirm the bug, It very serious.
Thank you.

## adi3yz | 2018-03-26T06:06:27+00:00
just try new commit... i think it still bug.. or new version just support only 2 pool?
using same config above...
* VERSIONS:     XMRig/2.5.1 libuv/1.19.2 gcc/7.3.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Core(TM) i7-4500U CPU @ 1.80GHz (1) x64 AES-NI
 * CPU L2/L3:    0.5 MB/4.0 MB
 * THREADS:      2, cryptonight, av=1, donate=5%
 * POOL #1:      192.168.1.99:7777
 * POOL #2:      cryptonight.jp.nicehash.com:3355
 * POOL #3:      pool.monero.hashvault.pro:5555
 * COMMANDS:     hashrate, pause, resume
[2018-03-26 13:57:45] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:57:52] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:57:58] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:04] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:10] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:16] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:17] use pool pool.monero.hashvault.pro:5555 139.99.9.133
[2018-03-26 13:58:17] new job from pool.monero.hashvault.pro:5555 diff 20000
[2018-03-26 13:58:22] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:29] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:36] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:42] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:48] speed 2.5s/60s/15m 47.6 n/a n/a H/s max: 51.0 H/s
[2018-03-26 13:58:48] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:58:55] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:59:01] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:59:02] new job from pool.monero.hashvault.pro:5555 diff 20000
[2018-03-26 13:59:07] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:59:14] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:59:21] [192.168.1.99:7777] connect error: "connection refused"

## xmrig | 2018-03-26T06:20:43+00:00
It strange work fine for me.
```
 * POOL #1:      192.168.1.99:7777
 * POOL #2:      cryptonight.jp.nicehash.com:3355
 * POOL #3:      pool.monero.hashvault.pro:5555
 * API PORT:     4477
 * COMMANDS:     hashrate, pause, resume
[2018-03-26 13:17:54] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:01] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:08] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:14] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:21] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:28] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:29] use pool cryptonight.jp.nicehash.com:3355 161.202.120.201
[2018-03-26 13:18:29] new job from cryptonight.jp.nicehash.com:3355 diff 200007
[2018-03-26 13:18:30] new job from cryptonight.jp.nicehash.com:3355 diff 200007
[2018-03-26 13:18:35] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:41] [192.168.1.99:7777] connect error: "connection refused"
[2018-03-26 13:18:42] new job from cryptonight.jp.nicehash.com:3355 diff 200007
```

## xmrig | 2018-03-26T06:28:26+00:00
Can you connect for just only cryptonight.jp.nicehash.com:3355 without other pools? Possible connection is timeout and third pool used.

## adi3yz | 2018-03-26T07:33:00+00:00
i using new 2.5.2 release.. and 2 pool only, but i think that bug still happen
my config
{
    "algo": "cryptonight",
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 5,
    "log-file": null,
    "max-cpu-usage": 75,
    "print-time": 60,
    "retries": 3,
    "retry-pause": 5,
    "safe": false,

pool #1 using xmrig-proxy
pool #2 direct to xmr pool

new 2.5.2 release run log
 * VERSIONS:     XMRig/2.5.2 libuv/1.19.2 gcc/7.3.0
 * HUGE PAGES:   available, enabled
 * CPU:          Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz (1) x64 AES-NI
 * CPU L2/L3:    1.0 MB/8.0 MB
 * THREADS:      4, cryptonight, av=1, donate=5%
 * POOL #1:      192.168.1.99:7777
 * POOL #2:      pool.supportxmr.com:5555
 * COMMANDS:     hashrate, pause, resume
[2018-03-26 15:25:30] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:25:57] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:26:13] speed 2.5s/60s/15m n/a n/a n/a H/s max: n/a H/s
[2018-03-26 15:26:23] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:26:23] use pool pool.supportxmr.com:5555 45.125.194.34
[2018-03-26 15:26:23] new job from pool.supportxmr.com:5555 diff 10000
[2018-03-26 15:26:49] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:27:13] speed 2.5s/60s/15m 71.6 n/a n/a H/s max: 142.8 H/s
[2018-03-26 15:27:15] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:27:16] new job from pool.supportxmr.com:5555 diff 7229
[2018-03-26 15:27:30] accepted (1/0) diff 7229 (69 ms)
[2018-03-26 15:27:41] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:28:08] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:28:13] speed 2.5s/60s/15m 116.0 104.8 n/a H/s max: 142.8 H/s
[2018-03-26 15:28:16] new job from pool.supportxmr.com:5555 diff 5000
[2018-03-26 15:28:34] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:28:40] accepted (2/0) diff 5000 (68 ms)
[2018-03-26 15:28:45] new job from pool.supportxmr.com:5555 diff 5000
[2018-03-26 15:28:54] accepted (3/0) diff 5000 (64 ms)
[2018-03-26 15:29:01] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:29:09] accepted (4/0) diff 5000 (63 ms)
[2018-03-26 15:29:13] speed 2.5s/60s/15m 86.6 99.5 n/a H/s max: 142.8 H/s
[2018-03-26 15:29:16] new job from pool.supportxmr.com:5555 diff 5000
[2018-03-26 15:29:28] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:29:36] accepted (5/0) diff 5000 (57 ms)
[2018-03-26 15:29:41] new job from pool.supportxmr.com:5555 diff 5000
[2018-03-26 15:29:55] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:30:07] accepted (6/0) diff 5000 (59 ms)
[2018-03-26 15:30:08] accepted (7/0) diff 5000 (59 ms)
[2018-03-26 15:30:13] speed 2.5s/60s/15m 139.1 108.6 n/a H/s max: 142.8 H/s
[2018-03-26 15:30:16] new job from pool.supportxmr.com:5555 diff 5000
[2018-03-26 15:30:23] [192.168.1.99:7777] connect error: "connection timed out"
[2018-03-26 15:30:28] accepted (8/0) diff 5000 (67 ms)
[2018-03-26 15:30:35] accepted (9/0) diff 5000 (59 ms)



## tarris034 | 2018-03-26T08:37:52+00:00
Does this reconnect problem occur in 2.5.0 CPU/AMD/NV ?
Is it only when using with proxy ?
Is it only when using multiple pools ?

Asking because already updated all my miners to 2.5.0 CPU/AMD/NV but using only one pool and no proxy.

Should I be worried that miners won't be able to reconnect in some circumstances ?

## xmrig | 2018-03-26T08:48:56+00:00
For miners this bug affect only version v2.5.1, in v2.5.0 no reconnect problem. I just released v2.5.2 anyway, with the fix.
Thank you.

## plavirudar | 2018-03-26T11:01:37+00:00
@adi3yz  that doesn't seem to be a bug, it's trying to reconnect to pool1, while still submitting shares to pool 2. This was the behaviour prior to the bug.

## adi3yz | 2018-03-26T11:07:53+00:00
now i know how it should work.. tq all

# Action History
- Created by: adi3yz | 2018-03-25T22:31:06+00:00
- Closed at: 2018-04-10T09:22:25+00:00
