---
title: xmrig cuda 6.8.2 crashes with Haven/XHV
source_url: https://github.com/xmrig/xmrig/issues/2116
author: Lonnegan
assignees: []
labels:
- bug
created_at: '2021-02-18T13:02:11+00:00'
updated_at: '2021-02-21T15:11:05+00:00'
type: issue
status: closed
closed_at: '2021-02-21T15:10:58+00:00'
---

# Original Description
**Describe the bug**
Mining Haven XHV with a NVIDIA GeForce GTX 1060 3GB (which can't mine ETH, ETC and RVN anymore due to DAG size) with xmrig cuda 6.8.2 is not working anymore. 6.8.1 has ran fine for days, 6.8.2 crashes within a few seconds without further info.

**To Reproduce**
Update to 6.8.2 from a perfectly working 6.8.1 and start the miner. It crashes within a few seconds. Same with a fresh config-file and it doesn't matter if cpu-mining is enabled or not.

**Expected behavior**
Running without crashes

**Required data**
 - just stops without further error

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
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": null,
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 8,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 0,
                "threads": 26,
                "blocks": 27,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 12,
                "blocks": 27,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 52,
                "blocks": 27,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 27,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 26,
                "blocks": 27,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 18432,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 18,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.hashvault.pro:443",
            "user": "....",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
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
    "watch": true,
    "pause-on-battery": false
}

 - Windows 10 Pro 20H2 with NVIDIA driver 461.40, NVIDIA GeForce GTX 1060 3GB and AMD Ryzen 5 5600X

# Discussion History
## SChernykh | 2021-02-18T13:50:06+00:00
https://github.com/xmrig/xmrig/pull/2117

## xmrig | 2021-02-21T15:10:58+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.9.0

# Action History
- Created by: Lonnegan | 2021-02-18T13:02:11+00:00
- Closed at: 2021-02-21T15:10:58+00:00
