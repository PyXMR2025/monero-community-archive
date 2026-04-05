---
title: '"Permission denied"'
source_url: https://github.com/xmrig/xmrig/issues/2689
author: Termin44l
assignees: []
labels: []
created_at: '2021-11-12T21:14:53+00:00'
updated_at: '2025-06-20T11:10:10+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:10:10+00:00'
---

# Original Description
Heyo! I'm trying to mine some Monero but I get the "my pool+port" Permission denied error. It's on a Windows 11 Home system. Antiviros not blocking it, It's turned off but just to be sure I added the exclousions to Bitdefender and the Windows Defender too. I'm running it with admin privileges too. Here is the config.json:
 
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
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
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
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "rx": [0, 1, 2, 3],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
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
        "enabled": true,
        "loader": null,
        "nvml": true,
        "astrobwt": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 3,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 0,
                "threads": 40,
                "blocks": 18,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 20,
                "blocks": 18,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 80,
                "blocks": 18,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 18,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 40,
                "blocks": 18,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "threads": 128,
                "blocks": 18,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 12288,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 12,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "XMR",
            "url": "gulf.moneroocean.stream:10128",
            "user": "44JJ9YPYvbbUwxtAwRQUura9Vh3XpKtNVVCo5EsctVPxiKrXDQvdiWrhYM4wSyRgGN4ENgM91GbVxgWuBxQYEuUKNDjgEHb",
            "pass": "passwd",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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
}


And the error
![InkedNévtelen](https://user-images.githubusercontent.com/75142376/141600063-b9a6c23f-b524-4dfc-965f-1762ba3a7b95.jpg)
:


# Discussion History
## Lonnegan | 2021-11-12T23:03:21+00:00
You need the MO fork of xmrig to use MoneroOcean in default mode (with algo switching). Please check the FAQ on MoneroOcean

# Action History
- Created by: Termin44l | 2021-11-12T21:14:53+00:00
- Closed at: 2025-06-20T11:10:10+00:00
