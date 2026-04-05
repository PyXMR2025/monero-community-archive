---
title: 'thread #1 failed with error <randomx_prepare>:36 "invalid argument"'
source_url: https://github.com/xmrig/xmrig/issues/1341
author: Wra1th7
assignees: []
labels:
- CUDA
- randomx
created_at: '2019-11-30T20:52:14+00:00'
updated_at: '2021-04-12T15:17:01+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:17:01+00:00'
---

# Original Description
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
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/gpu": [0, 1, 2, 3],
        "rx": [0, 2],
        "rx/wow": [0, 1, 2, 3],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": "c:xxx/xx/xmrig-cuda.dll",
        "nvml": true,
        "cn": [
            {
                "index": 0,
                "threads": 50,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 50,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 24,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 24,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 98,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 98,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 128,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 50,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 50,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/gpu": [
            {
                "index": 0,
                "threads": 50,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            },
            {
                "index": 1,
                "threads": 50,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 10,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            },
            {
                "index": 1,
                "threads": 32,
                "blocks": 10,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "randomx-benchmark.xmrig.com:7777",
            "user": "XXXX",
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

Setup via auto-config, so not sure where the promblem could be...
2x GTX 1050

# Discussion History
## Wra1th7 | 2019-11-30T22:41:42+00:00
system has 8GB RAM, but dataset wont load as well


## Wra1th7 | 2019-12-09T06:52:28+00:00
Tried v5.1.1 but still get the same problem when I add "pool.supportxmr.com:7777" & xmr wallet address to auto config .json


# Action History
- Created by: Wra1th7 | 2019-11-30T20:52:14+00:00
- Closed at: 2021-04-12T15:17:01+00:00
