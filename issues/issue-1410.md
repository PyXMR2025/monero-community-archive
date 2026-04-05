---
title: '[Minergate] Unknown algorithm'
source_url: https://github.com/xmrig/xmrig/issues/1410
author: WehrWolf92
assignees: []
labels:
- question
created_at: '2019-12-13T07:24:53+00:00'
updated_at: '2019-12-21T19:47:08+00:00'
type: issue
status: closed
closed_at: '2019-12-21T19:47:08+00:00'
---

# Original Description
Hey guys, i have the problem, that the xmrig doesn't work with the minergate-pool.

I want to start mining with my nVidia graphic card RTX 2070

I downloaded the XMRIG here (xmrig-nvidia-2.14.5-cuda10_1-win64.zip)
[https://github.com/xmrig/xmrig-nvidia/releases](url)

And thats the .bat from Minergate to start mining with my account
> xmrig-nvidia.exe -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u EMAIL  -p x

Ir i tried to change the "algo" in the .bat or the config.json to "rx/0" or "randomX", but there is the same failure, by changing it to "coin: monero" it has only 0.01 H/s ???

Before monero changed the algo to randomX i had round about 600 H/S


How can i change the options/config to mine normaly with my GraCa?

# Discussion History
## dedizones | 2019-12-13T07:54:55+00:00
Use v5.2.0 in config get true NVIDIA

Minegate and more pools use randomX

## WehrWolf92 | 2019-12-13T08:35:44+00:00
xD well, serious? just an outdated version?!

Thank you <3 Its working,

Is this correct if i just want to mine with GraCa only? 

> {
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
        "wrmsr": 6,
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
        "cn/0": false,
        "cn-lite/0": false
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
        "loader": null,
        "nvml": true,
        "cn": [
            {
                "index": 0,
                "threads": 30,
                "blocks": 108,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 14,
                "blocks": 108,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 60,
                "blocks": 108,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 108,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 30,
                "blocks": 108,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/gpu": [
            {
                "index": 0,
                "threads": 30,
                "blocks": 108,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 70,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 72,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": false
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
            "algo": null,
            "coin": null,
            "url": "xmr.pool.minergate.com:45700",
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

## dedizones | 2019-12-13T10:06:22+00:00
> "algo": null,
> "coin": null,
> 

I don't know "GraCa" but you want to see here the list of : https://xmrig.com/docs/algorithms

for randomX: https://github.com/xmrig/xmrig/issues/1204

## WehrWolf92 | 2019-12-13T10:34:01+00:00
GraCa, hm sorry, in germany we use this as a short word for graphic card :D 


## dedizones | 2019-12-13T10:51:59+00:00
ok ok, yes good for only nvidia card

use wizard ;) https://xmrig.com/wizard

# Action History
- Created by: WehrWolf92 | 2019-12-13T07:24:53+00:00
- Closed at: 2019-12-21T19:47:08+00:00
