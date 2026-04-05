---
title: Unable to set algo/coin
source_url: https://github.com/xmrig/xmrig/issues/1292
author: minerlady49
assignees: []
labels: []
created_at: '2019-11-16T19:08:19+00:00'
updated_at: '2023-09-15T07:29:26+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:41:10+00:00'
---

# Original Description
When I set the algo/coin to cn/r and monero I am unable to run the miner

# Discussion History
## xmrig | 2019-11-16T19:13:50+00:00
Please provide more details, for example error and config file, please note config must be valid JSON, so `"coin": "monero",` is OK, but `"coin": monero,` not OK.
Thank you.

## minerlady49 | 2019-11-16T19:29:23+00:00
Using the updated xmrig 5.0.0 config/json file lines 53 and 54. Changed as you specified which resolved that issue, but now am receiving error "connection refused". Here's my config file:

```json
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx": [0, 1, 2, 3, 4, 5],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD"
    },
    "cuda": {
        "enabled": true,
        "loader": null,
        "nvml": true,
        "cn": [
            {
                "index": 0,
                "threads": 22,
                "blocks": 138,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 10,
                "blocks": 138,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 46,
                "blocks": 138,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 138,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 22,
                "blocks": 138,
                "bfactor": 6,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/gpu": [
            {
                "index": 0,
                "threads": 22,
                "blocks": 138,
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
                "blocks": 92,
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
                "blocks": 92,
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
            "algo": "cn/r",
            "coin": "monero",
            "url": "supportxmr.com:8080",
            "user": "hidden",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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







## xmrig | 2019-11-16T19:36:48+00:00
Change `supportxmr.com:8080` to `pool.supportxmr.com:8080`.
Thank you.

## minerlady49 | 2019-11-16T19:38:25+00:00
Thank you! Long night, sorry for the oversight.

## thom58 | 2023-09-15T07:27:40+00:00
 I changed coins on xmrig 6.20.0 but my miner is not running. is there something wrong with my JSON file? 

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
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2]
        ],
        "rx": [0, 2],
        "rx/arq": [0, 1, 2, 3],
        "rx/wow": [0, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "odo",
            "coin": null,
            "url": "stratum+tcp://pool.dgb256.online:8083",
            "user": "hidden",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
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
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}**

## SChernykh | 2023-09-15T07:29:26+00:00
> "algo": "odo",

XMRig doesn't have this algo.

# Action History
- Created by: minerlady49 | 2019-11-16T19:08:19+00:00
- Closed at: 2020-02-09T10:41:10+00:00
