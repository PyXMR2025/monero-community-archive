---
title: version 2.5.2 SUMO Low diffficulty share error
source_url: https://github.com/xmrig/xmrig/issues/505
author: workboy
assignees: []
labels: []
created_at: '2018-04-05T17:53:03+00:00'
updated_at: '2018-11-05T13:20:35+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:20:35+00:00'
---

# Original Description
 new job from pool.sumo.spacepools.org:7777 diff 50000
[2018-04-06 01:46:55] rejected (0/1) diff 50000 "Low difficulty share" (404 ms)
[2018-04-06 01:46:59] rejected (0/2) diff 50000 "Low difficulty share" (411 ms)
[2018-04-06 01:47:00] new job from pool.sumo.spacepools.org:7777 diff 39474
[2018-04-06 01:47:03] rejected (0/3) diff 39474 "Low difficulty share" (411 ms)
[2018-04-06 01:47:04] rejected (0/4) diff 39474 "Low difficulty share" (1307 ms)


I use my xmrig-amd directly, all of which are Low diffficulty share error.
I changed my variant and used -1,0,1 separately, but nothing changed. He still existed.
So I used xmrig-proxy, but I still have this problem. I don't have any effective share.

Xmrig-amd version 2.5.2
Xmr-proxy version 2.5.2

**my xmrig-amd config:**
 {
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "donate-level": 5,
    "log-file": null,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "opencl-platform": 1,
    "threads": [
        {
            "index": 0,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 1,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 2,
            "intensity": 800,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 3,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 4,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 5,
            "intensity": 800,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 6,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 7,
            "intensity": 800,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 8,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 9,
            "intensity": 800,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 10,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        },
        {
            "index": 11,
            "intensity": 768,
            "worksize": 8,
            "affine_to_cpu": false
        }
    ],
    "pools": [
        {
            "url": "pool.sumo.spacepools.org:80",
            "user": "My Wallet",
            "pass": "x",
            "keepalive": true,
            "nicehash": false,
            "variant": -1 (0 , 1)
        }
    ],
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null
    }
}


**my xmrig-proxy config:**

{
    "algo": "cryptonight",
    "background": false,
    "colors": true,
    "retries": 5,
    "retry-pause": 5,
    "donate-level": 0,
    "syslog": false,
    "log-file": null,
    "access-log-file": null,
    "verbose": true,
    "pools": [
        {
            "url": "pool.sumo.spacepools.org:7777",
            "user": "My wallte",
            "pass": "x",
            "variant": -1 (0 , 1)
        }
    ],
    "bind": [
        "0.0.0.0:7777"
    ],
    "api": {
        "port": 8080,
        "access-token": null,
        "worker-id": null
    }
}

# Discussion History
## xmrig | 2018-04-05T18:59:57+00:00
Please check #476 and #482 new AMD miner will be available in hour.
Thank you.

## workboy | 2018-04-05T19:04:16+00:00
If I set algo to Cryptonight-Heavy on xmrig-proxy, but my miner is set up as Cryptonight, can the proxy configuration cover the local configuration? Is it able to work properly?

## xmrig | 2018-04-05T19:22:41+00:00
https://github.com/xmrig/xmrig-amd/releases/tag/v2.6.0-beta1 I just released new AMD miner with cryptonight-heavy support, proxy can't help if miner not support this algorithm.
Thank you.

## workboy | 2018-04-05T20:48:56+00:00
What time xmrig-proxy support for Cryptonight-Heavy and some other mining in software optimization

## workboy | 2018-04-05T21:35:14+00:00
Can you make rapid changes between SUMO and XMR through proxy? At present, proxy is not updated by SUMO.

## xmrig | 2018-04-05T21:41:05+00:00
It not small change, it required change a lot of things #487
Currently not possible make fastswitch between algorithms with different memory requirements.
Thank you.

## workboy | 2018-04-05T22:45:50+00:00
It may be possible to make a simple attempt, similar to the proxy timing reading configuration, and when xmrig finds the proxy changes, revise the configuration of the config and reboot the software, it is an amazing news for the users of more than hundreds of miners.

# Action History
- Created by: workboy | 2018-04-05T17:53:03+00:00
- Closed at: 2018-11-05T13:20:35+00:00
