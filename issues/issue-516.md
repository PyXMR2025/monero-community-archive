---
title: 2.5.2 "Incorrect hashing protocol in use.  Please upgrade/fix your miner"  &
  "Low difficulty share"
source_url: https://github.com/xmrig/xmrig/issues/516
author: Maibaosoul
assignees: []
labels:
- question
created_at: '2018-04-08T02:32:50+00:00'
updated_at: '2018-10-26T10:38:58+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:16:37+00:00'
---

# Original Description
Xmrig 2.5.2
Xmr-proxy version 2.5.2

"Incorrect hashing protocol in use.  Please upgrade/fix your miner"  
 "Low difficulty share"

How to resolve?


proxy config:
{
    "access-log-file": null,
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null,
        "ipv6": true,
        "restricted": true
    },
    "background": false,
    "bind": [
        "0.0.0.0:9998",
        "[::]:9998"
    ],
    "colors": true,
    "custom-diff": 0,
    "donate-level": 1,
    "log-file": null,
    "mode": "nicehash",
    "pools": [
        {
            "url": "hk01.supportxmr.com:7777",
            "user": "guess",
            "pass": "hk",
            "variant": 0
        }
    ],
    "retries": 2,
    "retry-pause": -1,
    "reuse-timeout": 0,
    "user-agent": null,
    "verbose": true,
    "watch": true,
    "workers": true
}

xmrig config:

{
    "algo": "cryptonight",  // cryptonight (default) or cryptonight-lite
    "av": 0,                // algorithm variation, 0 auto select
    "background": false,    // true to run the miner in the background
    "colors": true,         // false to disable colored output    
    "cpu-affinity": null,   // set process affinity to CPU core(s), mask "0x3" for cores 0 and 1
    "cpu-priority": null,   // set process priority (0 idle, 2 normal to 5 highest)
    "donate-level": 1,      // donate level, mininum 1%
    "log-file": null,       // log all output to a file, example: "c:/some/path/xmrig.log"
    "max-cpu-usage": 50,    // maximum CPU usage for automatic mode, usually limiting factor is CPU cache not this option.  
    "print-time": 60,       // print hashrate report every N seconds
    "retries": 5,           // number of times to retry before switch to backup server
    "retry-pause": 5,       // time to pause between retries
    "safe": false,          // true to safe adjust threads and av settings for current CPU
    "threads": null,        // number of miner threads
    "pools": [
        {
            "url": "hk01.supportxmr.com:9998", // URL of mining server
            "user": "near",           // username for mining server
            "pass": "x",                     // password for mining server
            "keepalive": true,               // send keepalived for prevent timeout (need pool support)
            "nicehash": true,               // enable nicehash/xmrig-proxy support
            "variant": 0                    // algorithm PoW variant
        }
    ],
    "api": {
        "port": 0,                             // port for the miner API https://github.com/xmrig/xmrig/wiki/API
        "access-token": null,                  // access token for API
        "worker-id": null                      // custom worker-id for API
    }
}

# Discussion History
## ghost | 2018-04-08T03:22:43+00:00
+1

## JustHoldit | 2018-04-08T03:44:47+00:00
+1
[2018-04-07 23:30:45] new job from 127.0.0.1:5556 diff 5000
[2018-04-07 23:31:03] speed 2.5s/60s/15m 148.4 151.4 n/a H/s max: 157.9 H/s
[2018-04-07 23:31:05] rejected (0/6) diff 5000 "Incorrect hashing protocol in use.  Please upgrade/fix your miner" (100 ms)
[2018-04-07 23:31:09] rejected (0/7) diff 5000 "Incorrect hashing protocol in use.  Please upgrade/fix your miner" (99 ms)
[2018-04-07 23:31:12] new job from 127.0.0.1:5556 diff 5000
[2018-04-07 23:31:49] rejected (0/8) diff 5000 "Bad gateway" (0 ms)
[2018-04-07 23:31:51] new job from 127.0.0.1:5556 diff 5000
[2018-04-07 23:32:00] accepted (1/8) diff 5000 (32 ms)
[2018-04-07 23:32:02] new job from 127.0.0.1:5556 diff 15000
[2018-04-07 23:32:03] speed 2.5s/60s/15m 152.5 151.0 n/a H/s max: 157.9 H/s
[2018-04-07 23:32:11] accepted (2/8) diff 15000 (0 ms)
[2018-04-07 23:33:02] new job from 127.0.0.1:5556 diff 15000
[2018-04-07 23:33:03] speed 2.5s/60s/15m 149.2 150.0 n/a H/s max: 157.9 H/s


## ghost | 2018-04-08T04:29:32+00:00
We need auto variant, current -1 auto variant isn't working.

## xmrig | 2018-04-08T08:29:13+00:00
@Maibaosoul Why you set `"variant": 0`? For Monero you don't need touch this option at all, if you remove this option from file or set it to `-1` anything will work. Valid values for Monero is `-1` (autodetect) or `1`.

@JustHoldit You use proxy with custom diff, accepted shares in your log not really accepted by pool.

@MoonGem `variant=-1` not work in one case, if you don't mine Monero.

## Maibaosoul | 2018-04-08T14:07:20+00:00
I set variant values -1, but nothing changed.

## ego008 | 2018-04-08T14:35:05+00:00
I also encountered the same error,  it works fine in the past 30 days.

## xmrig | 2018-04-08T15:16:08+00:00
@ego008  Please read #482
@Maibaosoul if you use xmrig-proxy, you should change variant only on proxy side.

## tkalfaoglu | 2018-04-09T05:48:08+00:00
same here.. :(  

[2018-04-09 08:39:10] new job from pool.supportxmr.com:3333 diff 5000
[2018-04-09 08:39:37] speed 2.5s/60s/15m 78.6 78.7 n/a H/s max: 78.7 H/s
[2018-04-09 08:39:50] rejected (7/1) diff 5000 "IP Address currently banned for using an invalid mining protocol, please check your miner" (84 ms)
[2018-04-09 08:39:50] no active pools, stop mining
[2018-04-09 08:39:56] use pool pool.supportxmr.com:3333 94.130.12.27
[2018-04-09 08:39:56] new job from pool.supportxmr.com:3333 diff 5000
[2018-04-09 08:40:09] new job from pool.supportxmr.com:3333 diff 6977
[2018-04-09 08:40:37] speed 2.5s/60s/15m 78.7 71.0 n/a H/s max: 78.7 H/s


## tkalfaoglu | 2018-04-09T06:10:35+00:00
SOLVED: Simply install the current git version, then set the algorithm to:
"algo": "cryptonight-heavy"

## xmrig | 2018-04-11T20:23:08+00:00
`cryptonight-heavy` only usable for Sumokoin and Haven Protocol, for Monero algo is `cryptonight`.
Thank you.

## ghost | 2018-04-11T20:29:14+00:00
bugger - thanks

## ghost | 2018-04-13T18:20:24+00:00
still getting this issue :(
xmrig-proxy 2.5.2 - most clients 2.6.0 beta2 windows x64 gcc - 1 client 2.5.2 on linux, 1 client 2.5.2 on osx

**## goes along great for a while:**
`[2018-04-13 18:28:15] 1.00 kH/s, shares: 239/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:28:54] #000 accepted (240/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:28:55] #000 accepted (241/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:29:16] 2.00 kH/s, shares: 241/31 +2, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:29:39] #000 accepted (242/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:29:45] #000 accepted (243/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:30:11] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:30:16] 2.00 kH/s, shares: 243/31 +2, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:30:49] #000 accepted (244/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:31:17] 1.00 kH/s, shares: 244/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:32:03] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:32:06] #000 accepted (245/31+0) diff 60000 ip <IP> (16
ms)
[2018-04-13 18:32:17] 1.00 kH/s, shares: 245/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:32:24] #000 accepted (246/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:32:43] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:32:48] #000 accepted (247/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:32:51] #000 accepted (248/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:33:18] 3.00 kH/s, shares: 248/31 +3, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:33:24] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:34:12] #000 accepted (249/31+0) diff 60000 ip 127.0.0.1 (0 ms)
[2018-04-13 18:34:18] 1.00 kH/s, shares: 249/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:34:27] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:34:32] #000 accepted (250/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:34:44] #000 accepted (251/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:34:54] #000 accepted (252/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:35:18] 3.00 kH/s, shares: 252/31 +3, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:35:22] #000 accepted (253/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:35:49] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:36:15] #000 accepted (254/31+0) diff 60000 ip <IP> (16
ms)
[2018-04-13 18:36:19] 2.00 kH/s, shares: 254/31 +2, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:36:26] #000 accepted (255/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:36:44] #000 accepted (256/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:36:49] #000 accepted (257/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:37:01] #000 accepted (258/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:37:04] #000 accepted (259/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:37:10] #000 accepted (260/31+0) diff 60000 ip 127.0.0.1 (16 ms)
[2018-04-13 18:37:19] 6.00 kH/s, shares: 260/31 +6, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:37:47] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:38:20] 0.00 kH/s, shares: 260/31 +0, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:39:10] #000 accepted (261/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:39:20] 1.00 kH/s, shares: 261/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:39:47] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:40:02] #000 accepted (262/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:40:21] 1.00 kH/s, shares: 262/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:40:24] #000 accepted (263/31+0) diff 60000 ip <IP> (1 m
s)
[2018-04-13 18:41:21] 1.00 kH/s, shares: 263/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:41:21] #000 accepted (264/31+0) diff 60000 ip <IP> (15
ms)
[2018-04-13 18:41:58] #000 accepted (265/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:41:59] #000 accepted (266/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:42:21] 3.00 kH/s, shares: 266/31 +3, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:43:22] 0.00 kH/s, shares: 266/31 +0, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:44:09] #000 accepted (267/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:44:22] 1.00 kH/s, shares: 267/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:44:49] #000 accepted (268/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:45:08] #000 accepted (269/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:45:17] #000 accepted (270/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:45:23] 3.00 kH/s, shares: 270/31 +3, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:45:49] #000 accepted (271/31+0) diff 60000 ip <IP> (16
ms)
[2018-04-13 18:46:23] 1.00 kH/s, shares: 271/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:46:45] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:47:22] #000 accepted (272/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:47:23] 1.00 kH/s, shares: 272/31 +1, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:47:40] #000 accepted (273/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:47:51] #000 accepted (274/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:48:24] 2.00 kH/s, shares: 274/31 +2, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:48:35] #000 accepted (275/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:48:42] #000 accepted (276/31+0) diff 60000 ip <IP> (16
ms)
[2018-04-13 18:48:47] #000 accepted (277/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:48:59] #000 accepted (278/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:49:03] #000 accepted (279/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:49:14] #000 accepted (280/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:49:24] 6.00 kH/s, shares: 280/31 +6, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:50:25] 0.00 kH/s, shares: 280/31 +0, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:50:34] #000 accepted (281/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:50:47] #000 accepted (282/31+0) diff 60000 ip <IP> (17
ms)
[2018-04-13 18:50:48] #000 accepted (283/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:50:50] #000 accepted (284/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:50:52] #000 accepted (285/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:51:17] #000 accepted (286/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:51:23] #000 accepted (287/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:51:25] 7.00 kH/s, shares: 287/31 +7, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:51:48] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:51:59] #000 accepted (288/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:52:02] #000 accepted (289/31+0) diff 60000 ip <IP> (16
ms)
[2018-04-13 18:52:04] #000 accepted (290/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:52:10] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:52:13] #000 accepted (291/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:52:25] 4.00 kH/s, shares: 291/31 +4, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:52:40] #000 accepted (292/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:52:49] #000 accepted (293/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:52:52] #000 accepted (294/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:53:26] 3.00 kH/s, shares: 294/31 +3, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:53:48] #000 accepted (295/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:54:14] #000 accepted (296/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:54:20] #000 accepted (297/31+0) diff 60000 ip <IP> (21
ms)
[2018-04-13 18:54:26] 3.00 kH/s, shares: 297/31 +3, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:54:39] #000 accepted (298/31+0) diff 60000 ip <IP> (16
ms)
[2018-04-13 18:54:53] #000 accepted (299/31+0) diff 60000 ip 127.0.0.1 (0 ms)
[2018-04-13 18:55:27] 2.00 kH/s, shares: 299/31 +2, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:55:33] #000 accepted (300/31+0) diff 60000 ip 127.0.0.1 (0 ms)
[2018-04-13 18:55:42] #000 accepted (301/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:56:02] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:56:14] #000 accepted (302/31+0) diff 60000 ip <IP> (16
ms)
[2018-04-13 18:56:22] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:56:25] #000 accepted (303/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:56:27] 4.00 kH/s, shares: 303/31 +4, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:56:28] #000 accepted (304/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:56:41] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:57:19] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:57:24] #000 accepted (305/31+0) diff 60000 ip <IP> (1 m
s)
[2018-04-13 18:57:27] 2.00 kH/s, shares: 305/31 +2, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:57:39] #000 accepted (306/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:57:40] #000 accepted (307/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:58:03] #000 accepted (308/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:58:24] #000 accepted (309/31+0) diff 60000 ip <IP> (15
ms)
[2018-04-13 18:58:28] 4.00 kH/s, shares: 309/31 +4, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:59:08] #000 accepted (310/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:59:19] #000 accepted (311/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:59:23] #000 accepted (312/31+0) diff 60000 ip <IP> (3 m
s)
[2018-04-13 18:59:28] 3.00 kH/s, shares: 312/31 +3, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 18:59:34] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 18:59:41] #000 accepted (313/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:59:49] #000 accepted (314/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 18:59:49] #000 accepted (315/31+0) diff 60000 ip <IP> (0 m
s)
[2018-04-13 19:00:16] #000 accepted (316/31+0) diff 60000 ip <IP> (0 m
s)`

**## then things seem to go tits up without aparent reason:**
`[2018-04-13 19:00:23] #000 rejected (316/32+0) diff 60000 ip <IP> "Low
 difficulty share" (31 ms)
[2018-04-13 19:00:27] #000 rejected (316/33+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:00:27] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:00:29] 4.00 kH/s, shares: 316/33 +4, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 19:00:37] #000 rejected (316/34+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:00:37] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:00:47] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 19:00:51] #000 rejected (316/35+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:00:51] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:00:52] #000 rejected (316/36+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:00:52] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:01:05] #000 rejected (316/37+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:01:05] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:01:12] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 19:01:29] 0.00 kH/s, shares: 316/37 +0, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 19:01:30] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 19:02:09] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 19:02:13] #000 rejected (316/38+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:02:13] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:02:29] #000 rejected (316/39+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:02:29] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:02:29] 0.00 kH/s, shares: 316/39 +0, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 19:03:16] #000 rejected (316/40+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (5 ms)
[2018-04-13 19:03:16] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:03:18] #000 rejected (316/41+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:03:19] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:03:30] 0.00 kH/s, shares: 316/41 +0, upstreams: 1, miners: 14 (ma
x 15) +0/-0
[2018-04-13 19:03:37] #000 rejected (316/42+0) diff 60000 ip 127.0.0.1 "Incorrec
t hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:03:37] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:03:37] #000 new job from pool.supportxmr.com:7777 diff 60000
[2018-04-13 19:04:10] #000 rejected (316/43+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:04:10] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:04:18] #000 rejected (316/44+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:04:18] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:04:28] #000 rejected (316/45+0) diff 60000 ip <IP> "Inc
orrect hashing protocol in use.  Please upgrade/fix your miner" (0 ms)
[2018-04-13 19:04:29] [pool.supportxmr.com:7777] error: "Low difficulty share",
code: -1
[2018-04-13 19:04:30] 0.00 kH/s, shares: 316/45 +0, upstreams: 1, miners: 14 (ma
x 15) +0/-0`

## aahutsal | 2018-04-27T05:18:17+00:00
+1 need to get it fixed!

## ghost | 2018-07-01T19:32:40+00:00
+1

## tkalfaoglu | 2018-10-26T10:26:44+00:00
I'm having a similar issue.. Latest GIT version:
protocol: cryptonight
variant: -1

[2018-10-26 13:17:00] new job from pool.supportxmr.com:5555 diff 14280 algo cn/2
[2018-10-26 13:17:12] accepted (135/0) diff 14280 (112 ms)
[2018-10-26 13:17:13] accepted (136/0) diff 14280 (82 ms)
[2018-10-26 13:17:29] new job from pool.supportxmr.com:5555 diff 14280 algo cn/2
[2018-10-26 13:17:54] rejected (136/1) diff 14280 "IP Address currently banned for using an invalid mining protocol, please check your miner" (82 ms)
[2018-10-26 13:17:54] no active pools, stop mining
[2018-10-26 13:17:56] speed 10s/60s/15m 485.2 485.9 485.4 H/s max 493.9 H/s
[2018-10-26 13:18:01] [pool.supportxmr.com:5555] error: "IP Address currently banned for using an invalid mining protocol, please check your miner", code: -1
[2018-10-26 13:18:06] use pool pool.supportxmr.com:5555  212.232.25.155 
[2018-10-26 13:18:06] new job from pool.supportxmr.com:5555 diff 10000 algo cn/2
[2018-10-26 13:18:19] accepted (137/1) diff 10000 (112 ms)
[2018-10-26 13:18:27] accepted (138/1) diff 10000 (115 ms)




## snipeTR | 2018-10-26T10:38:12+00:00
Firewall, router, wrong diff, or banned poll for your ip.
Try" varriant 2"

# Action History
- Created by: Maibaosoul | 2018-04-08T02:32:50+00:00
- Closed at: 2018-10-10T22:16:37+00:00
