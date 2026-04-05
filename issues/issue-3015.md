---
title: 'CPU usage not 100% '
source_url: https://github.com/xmrig/xmrig/issues/3015
author: qqiumax
assignees: []
labels: []
created_at: '2022-04-09T05:05:13+00:00'
updated_at: '2022-05-17T06:59:57+00:00'
type: issue
status: closed
closed_at: '2022-05-17T06:59:57+00:00'
---

# Original Description
My task manager says i only used 50% of CPU
here is my config.json:
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "127.0.0.1",
        "port": 56129,
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
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "astrobwt/v2": [0, 1, 2, 3],
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
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "us-west.minexmr.com:443",
            "user": "43DCyQ4BZwXE4pJ3keGaDf6N7Amxi9bx8GDb9ZFmTU55iJUMznf8Jw49ym8LCXEg7WgSNRNui2v2PK4Fy9saRXL9D1trU8K",
            "pass": null,
            "rig-id": "Administrator",
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "wss": false,
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
}
I have 2 cores, 4 threads, intel i5 6200U of CPU
lenovo motherboard

# Discussion History
## Spudz76 | 2022-04-09T11:24:22+00:00
3MB of cache only enough for 1.5 threads, so already 2 threads is too much.

Intel CPUs do not benefit from hyperthreads in RandomX, so 2 (the core count) is max anyway, and 50% usage is max.

## qqiumax | 2022-05-17T06:59:57+00:00
ok done

# Action History
- Created by: qqiumax | 2022-04-09T05:05:13+00:00
- Closed at: 2022-05-17T06:59:57+00:00
