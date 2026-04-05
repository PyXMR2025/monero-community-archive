---
title: Hash rate does not recover after screenrecording
source_url: https://github.com/xmrig/xmrig/issues/3716
author: jekv2
assignees: []
labels: []
created_at: '2025-09-28T16:25:05+00:00'
updated_at: '2025-09-30T06:01:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Hash rate does not recover after screenrecording on Linux Mint

**To Reproduce**
Install Linux Mint, xmrig, simple screen recorder https://github.com/MaartenBaert/ssr .
Run xmrig to mine xmr, start the screen recording, you will see hash rate drop, stop screen recording and then you'll see hash rate does not recover, close xmrig, start it again, hash rate does not recover until a reboot/restart.

**Expected behavior**
For hash rate to recover to it's orginal hash rate.

**Required data**
 - XMRig version
    * ABOUT        XMRig/6.24.0 gcc/13.3.0 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.0.13 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          AMD Ryzen 9 9950X 16-Core Processor (1) 64-bit AES
                L2:16.0 MB L3:64.0 MB 16C/32T NUMA:1
 * MEMORY       1.3/31.0 GB (4%)
                DIMM_A0: <empty>
                DIMM_A1: 16 GB DDR5 @ 6200 MHz F5-6800J3445G16G              
                DIMM_B0: <empty>
                DIMM_B1: 16 GB DDR5 @ 6200 MHz F5-6800J3445G16G              
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - TUF GAMING B850-PLUS WIFI
 * DONATE       1%
 * ASSEMBLY     ryzen
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - {
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
        "1gb-pages": true,
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
        "asm": "ryzen",
        "argon2-impl": null,
        "argon2": [0, 12, 1, 13, 2, 14, 3, 15, 4, 16, 5, 17, 6, 18, 7, 19, 8, 20, 9, 21, 10, 22],
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
            [1, 11]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 6],
            [1, 7],
            [1, 8]
        ],
        "cn-lite": [
            [1, 0],
            [1, 12],
            [1, 1],
            [1, 13],
            [1, 2],
            [1, 14],
            [1, 3],
            [1, 15],
            [1, 4],
            [1, 16],
            [1, 5],
            [1, 17],
            [1, 6],
            [1, 18],
            [1, 7],
            [1, 19],
            [1, 8],
            [1, 20],
            [1, 9],
            [1, 21],
            [1, 10],
            [1, 22],
            [1, 11],
            [1, 23]
        ],
        "cn-pico": [
            [2, 0],
            [2, 12],
            [2, 1],
            [2, 13],
            [2, 2],
            [2, 14],
            [2, 3],
            [2, 15],
            [2, 4],
            [2, 16],
            [2, 5],
            [2, 17],
            [2, 6],
            [2, 18],
            [2, 7],
            [2, 19],
            [2, 8],
            [2, 20],
            [2, 9],
            [2, 21],
            [2, 10],
            [2, 22],
            [2, 11],
            [2, 23]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 12],
            [2, 1],
            [2, 13],
            [2, 2],
            [2, 14],
            [2, 3],
            [2, 15],
            [2, 4],
            [2, 16],
            [2, 5],
            [2, 17],
            [2, 6],
            [2, 18],
            [2, 7],
            [2, 19],
            [2, 8],
            [2, 20],
            [2, 9],
            [2, 21],
            [2, 10],
            [2, 22],
            [2, 11],
            [2, 23]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7],
            [8, 8],
            [8, 9],
            [8, 10],
            [8, 11]
        ],
        "rx": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15, 31],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 25, 26, 27, 28, 29, 30, 31],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow"
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
        "nvml": true,
        "cn": [
            {
                "index": 0,
                "threads": 34,
                "blocks": 24,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 18,
                "blocks": 24,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 70,
                "blocks": 24,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 64,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 64,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 64,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 16384,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 16,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 16,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 16,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "XMR",
            "url": "BLANKED",
            "user": "BLANKED",
            "pass": "BLANKED",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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
        "ip_version": 0,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

 - OS: Linux Mint 22.1
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
[Add any other context about the problem here.] 

Found out by mistake.

https://github.com/xmrig/xmrig/issues/3706#issuecomment-3343830801

<img width="1214" height="667" alt="Image" src="https://github.com/user-attachments/assets/73f925e7-f901-40f3-8a01-a449aeea67da" />
<img width="371" height="313" alt="Image" src="https://github.com/user-attachments/assets/86294047-94ac-4dbe-9449-1b265d7ee426" />


# Discussion History
## SChernykh | 2025-09-29T15:17:25+00:00
This has to do not with XMRig itself, but with your OS's settings. Things like power options or background processes that keep running after you finish the recording.

## jekv2 | 2025-09-30T06:01:36+00:00
> This has to do not with XMRig itself, but with your OS's settings. Things like power options or background processes that keep running after you finish the recording.

What and how would I find out what it is?

# Action History
- Created by: jekv2 | 2025-09-28T16:25:05+00:00
