---
title: cannot set msr 0xc0011020 to 0x00000000000000000
source_url: https://github.com/xmrig/xmrig/issues/3405
author: mrgarvj
assignees: []
labels: []
created_at: '2024-01-22T11:38:59+00:00'
updated_at: '2024-01-24T16:46:16+00:00'
type: issue
status: closed
closed_at: '2024-01-24T16:46:15+00:00'
---

# Original Description
**Describe the bug**
Issue Description:
I am encountering a problem while attempting to set Model Specific Register (MSR) 0xc0011020 to the value 0x00000000000000000 on an AMD Ryzen 3 5300U processor while using the xmrig application. The operation fails with an error message, and I am unable to successfully modify the MSR.

Details:

Processor: AMD Ryzen 3 5300U
MSR in question: 0xc0011020
Desired value: 0x00000000000000000
Application: xmrig

**Required data**
 - Miner log as text or screenshot - 
![image](https://github.com/xmrig/xmrig/assets/151378629/a2c47035-f7bb-4b18-95a0-ec73a0552afd)
 - {
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
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
        "argon2": [0, 2, 4, 6],
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
            [1, 4],
            [1, 6]
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
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2]
        ],
        "rx": [0, 2],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 2, 4, 6],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn": [
            {
                "index": 0,
                "intensity": 480,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 120,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 984,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 984,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 480,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 984,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 1572864,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 64,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
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
            "algo": null,
            "coin": null,
            "url": "donate.v2.xmrig.com:3333",
            "user": "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "sni": false,
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
    "pause-on-battery": true,
    "pause-on-active": false
}
 - OS: Windows 11



# Discussion History
## SChernykh | 2024-01-22T12:16:57+00:00
You're running inside a VM (virtual machine). Turn off any virtualization options and secure boot in BIOS, also turn off Core Isolation/Memory integrity in Windows, or you'll keep getting this error.

## mrgarvj | 2024-01-23T15:08:17+00:00
ohk let me try this

## mrgarvj | 2024-01-24T16:46:15+00:00
it worked thanks
(But only by turning off Memory Isolation)

# Action History
- Created by: mrgarvj | 2024-01-22T11:38:59+00:00
- Closed at: 2024-01-24T16:46:15+00:00
