---
title: xmrig proxy 2.6.2 [Stellite Coin] - PROBLEM
source_url: https://github.com/xmrig/xmrig/issues/691
author: drJoker228
assignees: []
labels: []
created_at: '2018-06-12T14:17:32+00:00'
updated_at: '2018-11-05T13:51:18+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:51:18+00:00'
---

# Original Description
Hello, before hard fork all was okay, now i have error.

What to do? Help please!
![capture](https://user-images.githubusercontent.com/39148634/41295961-7ad468a4-6e64-11e8-9277-efb7b5dd5ef3.PNG)


# Discussion History
## xmrig | 2018-06-14T11:41:18+00:00
Probably some or all miners not updated, proxy can't help if miner not support algorithm.
Thank you.

## nicsan85 | 2018-08-05T05:49:07+00:00
Dear Xmrig owner & Friends,
i need helo,

is it possible to mining Stellite (XTL) with XMrig Amd 2.7.3 ?

or did i put the wrong algo?
already put :
cryptonight
cryptonight-lite
cn-lite
cn-litev7
stellite
stellitev7

and the shares always reject : https://ibb.co/j345GK

heres the config :

    "algo": "cryptonight-lite",
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "background": false,
    "cache": true,
    "colors": true,
    "donate-level": 1,
    "log-file": null,
    "opencl-platform": 0,
    "opencl-loader": "OpenCL.dll",
    "pools": [
        {
            "url": "xtl.miningpool.id:8805",
            "user": "SEiStP7SMy1bvjkWc9dd1t2v1Et5q2DrmaqLqFTQQ9H7JKdZuATcPHUbUL3bRjxzxTDYitHsAPqF8Ee CLw3bW8ARe8rYc1eGiRC4Kww3e37HP",
            "pass": "JANGKRIKBOSS!!",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": 1
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "intensity": 1430,
            "worksize": 8,
            "strided_index": 1,
            "mem_chunk": 2,
            "comp_mode": true,
            "affine_to_cpu": false
        },

can anybody help me?

thanks in advance

# Action History
- Created by: drJoker228 | 2018-06-12T14:17:32+00:00
- Closed at: 2018-11-05T13:51:18+00:00
