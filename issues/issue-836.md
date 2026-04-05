---
title: OSX Mining not recognized by supportxmr.com
source_url: https://github.com/xmrig/xmrig/issues/836
author: jacksonkr
assignees: []
labels: []
created_at: '2018-10-22T20:03:39+00:00'
updated_at: '2019-03-17T17:21:32+00:00'
type: issue
status: closed
closed_at: '2019-03-17T17:21:32+00:00'
---

# Original Description
I have a windows machine mining and a mac machine mining both using xmrig. The windows machine uses the pre-built software and for osx I built the packages manually (cmake). I noticed that on the support.xmr dashboard I see the mining of the windows machine but NOT the mac machine.

Machine:
2015 iMac i5-4690 AMD R9 m290x OSX 10.14

Supporxmr.com dashboard:
https://www.supportxmr.com/#/dashboard

config for cpu:
```
{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "asm": true,
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 5,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 75,
    "pools": [
        {
            "url": "nyc02.supportxmr.com:5555",
            "user": "xxxxx",
            "pass": "imac",
            "rig-id": "imacid",
            "nicehash": true,
            "keepalive": true,
            "variant": -1,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": false,
            "affine_to_cpu": false,
            "no_prefetch": true,
            "asm": "intel"
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": false,
            "no_prefetch": true,
            "asm": "intel"
        },
        {
            "low_power_mode": false,
            "affine_to_cpu": false,
            "no_prefetch": true,
            "asm": "intel"
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": false
}
```

config for gpu (amd)
```
{
	"algo": "cryptonight",
	"background": false,
	"colors": true,
	"donate-level": 5,
	"log-file": null,
	"print-time": 60,
	"retries": 5,
	"retry-pause": 5,
	"syslog": false,
	"opencl-platform": 0,
	"threads": [{
		"index": 0,
		"intensity": 512,
		"worksize": 8,
		"affine_to_cpu": false
	}],
	"pools": [{
		"url": "nyc02.supportxmr.com:5555",
		"user": "xxxxx",
		"pass": "imac",
		"keepalive": true,
		"nicehash": true
	}]
}
```

CPU Output
```
 * ABOUT        XMRig/2.8.3 clang/10.0.0
 * LIBS         libuv/1.23.2 microhttpd/0.9.59 
 * CPU          Intel(R) Core(TM) i5-4690 CPU @ 3.50GHz (1) x64 AES
 * CPU L2/L3    1.0 MB/6.0 MB
 * THREADS      3, cryptonight, donate=5%
 * ASSEMBLY     auto:intel
 * POOL #1      nyc02.supportxmr.com:5555 variant auto
 * COMMANDS     hashrate, pause, resume
[2018-10-22 14:01:48] use pool nyc02.supportxmr.com:5555  104.140.201.42 
[2018-10-22 14:01:48] new job from nyc02.supportxmr.com:5555 diff 10000 algo cn/2
[2018-10-22 14:01:48] READY (CPU) threads 3(3) huge pages 3/3 100% memory 6.0 MB
[2018-10-22 14:01:51] accepted (1/0) diff 10000 (94 ms)
[2018-10-22 14:02:04] new job from nyc02.supportxmr.com:5555 diff 18750 algo cn/2
| THREAD | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|      0 |       -1 |    55.2 |     n/a |     n/a |
|      1 |       -1 |    54.8 |     n/a |     n/a |
|      2 |       -1 |    55.2 |     n/a |     n/a |
[2018-10-22 14:02:15] speed 10s/60s/15m 165.2 n/a n/a H/s max 171.2 H/s
```

GPU is about the same ~200h/s

Why isn't this tracking on support.xmr? 

# Discussion History
## xmrig | 2018-10-24T03:04:28+00:00
supportxmr not support `rig-id` protocol extensions, so it should appear as `imac` not `imacid` in dashboard. Might be temporary pool issue, check other ports or location.
Thank you.

## jacksonkr | 2018-10-24T15:11:26+00:00
I'm using the same pool on both PC and mac yet the PC work is logged on supportxmr.com. How can I make sure that the work being done on the mac is getting accepted & payed?

Edit:
I also tried this on my macbook pro with the same results. It mines w no report on supportxmr.com

Edit:
I took a snapshot of the terminal output and it looks like
```
[2018-10-26 04:22:35] accepted (1830/0) diff 5670 (83 ms)
[2018-10-26 04:22:39] accepted (1831/0) diff 5670 (86 ms)
[2018-10-26 04:22:39] speed 10s/60s/15m 188.3 188.9 187.9 H/s max 196.0 H/s
[2018-10-26 04:23:08] accepted (1832/0) diff 5670 (320 ms)
[2018-10-26 04:23:14] new job from nyc02.supportxmr.com:5555 diff 5670 algo cn/2
[2018-10-26 04:23:39] speed 10s/60s/15m 188.3 188.9 187.9 H/s max 196.0 H/s
[2018-10-26 04:24:19] new job from nyc02.supportxmr.com:5555 diff 5670 algo cn/2
[2018-10-26 04:24:31] accepted (1833/0) diff 5670 (83 ms)
[2018-10-26 04:24:39] speed 10s/60s/15m 188.7 186.8 187.7 H/s max 196.0 H/s
[2018-10-26 04:24:40] accepted (1834/0) diff 5670 (82 ms)
[2018-10-26 04:25:09] accepted (1835/0) diff 5670 (198 ms)
[2018-10-26 04:25:39] speed 10s/60s/15m 190.2 188.6 187.5 H/s max 196.0 H/s
[2018-10-26 04:25:43] accepted (1836/0) diff 5670 (82 ms)
[2018-10-26 04:25:45] accepted (1837/0) diff 5670 (82 ms)
[2018-10-26 04:26:39] speed 10s/60s/15m 188.1 189.5 187.5 H/s max 196.0 H/s
[2018-10-26 04:27:22] accepted (1838/0) diff 5670 (83 ms)
[2018-10-26 04:27:28] accepted (1839/0) diff 5670 (137 ms)
[2018-10-26 04:27:39] speed 10s/60s/15m 187.0 189.5 187.5 H/s max 196.0 H/s
[2018-10-26 04:27:46] accepted (1840/0) diff 5670 (117 ms)
[2018-10-26 04:28:22] accepted (1841/0) diff 5670 (84 ms)
[2018-10-26 04:28:24] new job from nyc02.supportxmr.com:5555 diff 5670 algo cn/2
[2018-10-26 04:28:39] speed 10s/60s/15m 187.1 189.7 187.5 H/s max 196.0 H/s
```

I also took note that the invalid shares are at 22k of 1604k total shares if that relates at all.

## resistor4u | 2018-11-12T21:40:46+00:00
@jacksonkr curious. i don't have this issue with macbook pro.

could you share
1) what macbook pro model you're running?
2) did you build with gcc-8 (via homebrew) or apple's clang?
3) the config file you're using for the macbook?

## jacksonkr | 2018-11-13T18:58:50+00:00
@resistor4u 

MacBook Pro (Retina, 15-inch, Mid 2015)
gcc-8
The config above is the config I use

## DeadManWalkingTO | 2019-03-17T14:44:22+00:00
Does the issue still exist?
Please feedback.

Thank you!

## jacksonkr | 2019-03-17T17:21:32+00:00
As far as I know it still exists. It may be an issue with supportxmr.com reporting specifically so I'm going to close this until I have time to investigate further.

# Action History
- Created by: jacksonkr | 2018-10-22T20:03:39+00:00
- Closed at: 2019-03-17T17:21:32+00:00
