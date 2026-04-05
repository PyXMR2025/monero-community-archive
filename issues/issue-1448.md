---
title: OpenCL (AMD Radeon) System Crash
source_url: https://github.com/xmrig/xmrig/issues/1448
author: jacksonkr
assignees: []
labels:
- opencl
created_at: '2019-12-19T17:26:29+00:00'
updated_at: '2021-04-12T15:08:03+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:08:03+00:00'
---

# Original Description
The miner runs fine with opencl disabled, but when open cl is enabled I will get a hard system crash pretty early on. I've even tried disabling gpu mining with no success.

Any advice on how to get around this?

Windows 10
Radeon Software Version: 19.9.1
Graphics Chipset; AMD Radeon RX 5700 XT

**config.xml**
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": 2,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn": [
            {
                "index": 0,
                "intensity": 960,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 960,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 1920,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 1920,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 960,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/gpu": [
            {
                "index": 0,
                "intensity": 960,
                "worksize": 8,
                "threads": [-1, -1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 320,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 3,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "nyc02.supportxmr.com:7777",
            "user": "xxxxx",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}
```

# Discussion History
## dedizones | 2019-12-21T07:57:20+00:00
Look all issue :
https://github.com/xmrig/xmrig/issues/1417

https://github.com/xmrig/xmrig/issues/1352

https://github.com/xmrig/xmrig/issues/1346

## jacksonkr | 2019-12-21T14:04:38+00:00
@dedizones Only one of those offers any real solution, which is to roll back drivers and that still results in either a system crash or a gpu hashrate of 0/hs

## dedizones | 2019-12-22T05:05:00+00:00
> @dedizones Only one of those offers any real solution, which is to roll back drivers and that still results in either a system crash or a gpu hashrate of 0/hs

I am in the same case as you, I have my 280x on stand-by for 3 weeks ... I was told that the problem came from AMD but I do not believe it since on other algorithms no problem


## xmrig | 2019-12-22T18:48:38+00:00
In general use GPUs for RandomX is bad idea and GCN ASM not available for RX 5700 so even if it works it will be extremely slow.
Thank you.

# Action History
- Created by: jacksonkr | 2019-12-19T17:26:29+00:00
- Closed at: 2021-04-12T15:08:03+00:00
