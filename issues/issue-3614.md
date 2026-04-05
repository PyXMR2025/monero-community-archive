---
title: Low share difficulty when setting difficulty via password section
source_url: https://github.com/xmrig/xmrig/issues/3614
author: BonhomieBG
assignees: []
labels: []
created_at: '2025-01-07T21:21:53+00:00'
updated_at: '2025-06-16T19:35:10+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:35:10+00:00'
---

# Original Description
I want to mine Blobfish, it use kawpow algo. The mining pool i'm mining on support static difficulty with password set to d=difficulty. I set it but it doesn't work, I got a lot of rejected share. with normal var difficulty, it work fine. How do I fix it? Thank you.

My config setting
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
    "colors": false,
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
        "argon2-impl": null
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
                "intensity": 768,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 768,
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
                "intensity": 768,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 1920,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 12582912,
                "worksize": 256,
                "threads": [1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 768,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 27712,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 7552,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "kawpow",
            "coin": null,
            "url": "us-east.mining4people.com:23438",
            "user": "Ssjk5MVvxfLUzcMJw5wQbuUuptKWFv8MMx.BG",
            "pass": "d=0.1",
            "rig-id": null,
            "nicehash": false,
            "keepalive":false,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
            
        }
    ],
    "retries": 10,
    "retry-pause": 50,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "tls": {
        "enabled": true,
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

# Discussion History
# Action History
- Created by: BonhomieBG | 2025-01-07T21:21:53+00:00
- Closed at: 2025-06-16T19:35:10+00:00
