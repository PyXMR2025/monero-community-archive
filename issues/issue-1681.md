---
title: AMD OpenCL mining of RYO not working
source_url: https://github.com/xmrig/xmrig/issues/1681
author: jsonnentag
assignees: []
labels:
- duplicate
- wontfix
created_at: '2020-05-19T21:58:12+00:00'
updated_at: '2020-05-20T01:55:33+00:00'
type: issue
status: closed
closed_at: '2020-05-20T01:55:32+00:00'
---

# Original Description
I went through the "wizard" and filled everything out to mine at ryo.miner.rocks and pasted it into a JSON file.  All I get is an error from the pool saying the algorithm is unknown and a login error (6).  It worked perfectly fine with "xmrig-amd-2.14.6-msvc-win64" (but that wasn't compatible with updated AMD drivers).  Now with updated video drivers the old miner version doesn't work and the new supposedly functional version has other problems connecting to the pool.

[2020-05-19 14:56:12.942] [ryo.miner.rocks:30172] unknown algorithm, make sure you set "algo" or "coin" option
[2020-05-19 14:56:12.945] [ryo.miner.rocks:30172] login error code: 6

-----
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
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 192,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 448,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 960,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 960,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 448,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "ryo.miner.rocks:30172",
            "user": "RYoLsj3piQ2BvXd4P6QJk1EqweJNaLSm8Ey7ZLynW1rHFbsnSwpAPXjDsyRBuqXzYh12W47BYDucS5J754Bv79uj1XVeYjeYXQc",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true
}

# Discussion History
## jsonnentag | 2020-05-19T21:59:57+00:00
AND YES, I do know that what is pasted above STILL has "null" in the ALGO and COIN variables.  Every time I set them it sets it back to null again!  I pasted in the results of the modifications seen when the "wizard" results are used.  The wizard original has "cn/gpu" in it.  After running it disappeared!

## xmrig | 2020-05-20T01:55:32+00:00
https://github.com/xmrig/xmrig/issues/1665#issuecomment-621651021

# Action History
- Created by: jsonnentag | 2020-05-19T21:58:12+00:00
- Closed at: 2020-05-20T01:55:32+00:00
