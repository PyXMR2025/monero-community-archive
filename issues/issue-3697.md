---
title: Struggling here. msr cache QoS can only be enabled when all mining threads
  have affinity set
source_url: https://github.com/xmrig/xmrig/issues/3697
author: jekv2
assignees: []
labels: []
created_at: '2025-08-24T14:46:21+00:00'
updated_at: '2025-08-24T22:24:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am having a tough time here.

I enabled "cache_qos": true,

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
        "cache_qos": true,
        "numa": true,
        "scratchpad_prefetch_mode": 2
    },

And when I run sudo ./xmrig

[2025-08-24 09:41:45.690]  msr      cache QoS can only be enabled when all mining threads have affinity set
[2025-08-24 09:41:45.690]  msr      register values for "ryzen_1Ah_zen5" preset have been set successfully (0 ms)
[2025-08-24 09:41:45.690]  randomx  init dataset algo rx/0 (32 threads) seed 1dc5dbac121f6456...
[2025-08-24 09:41:45.783]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (94 ms)
[2025-08-24 09:41:46.349]  randomx  dataset ready (565 ms)
[2025-08-24 09:41:46.349]  cpu      use profile  rx  (32 threads) scratchpad 2048 KB
[2025-08-24 09:41:46.361]  cpu      READY threads 32/32 (32) huge pages 100% 32/32 memory 65536 KB


Mainly
msr      cache QoS can only be enabled when all mining threads have affinity set

How may I fix this?

<img width="1214" height="633" alt="Image" src="https://github.com/user-attachments/assets/5aafbd67-8923-43d9-8d4c-78c9fa83152c" />



# Discussion History
## SChernykh | 2025-08-24T17:33:48+00:00
The auto-generated config sets affinity for all threads. You probably have `"rx": [-1, -1, ...` in config.json. Delete this line and run XMRig again.

## jekv2 | 2025-08-24T18:03:04+00:00
> The auto-generated config sets affinity for all threads. You probably have `"rx": [-1, -1, ...` in config.json. Delete this line and run XMRig again.

That was the problem! Thanks!

Are there any tweaks I may do for this ryzen 9 9950x?

I get 27255 or so, but on benchmark it's in the 28000's.

Bench
<img width="1214" height="718" alt="Image" src="https://github.com/user-attachments/assets/7faf2fb2-93dc-42be-80ce-36b93b2fd9cb" />


With config below.
<img width="1526" height="497" alt="Image" src="https://github.com/user-attachments/assets/8d1e5c57-6964-48ea-a4e8-71b5bf9f1fa9" />

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
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "fast",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": true,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": true,
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
    "donate-level": 1,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "XMR",
            "url": "stratum+tcp://BLANKED
            "user": BLANKED,
            "pass": BLANKED,
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

## SChernykh | 2025-08-24T18:34:53+00:00
Your benchmark is testing `rx/wow`, it's a different algorithm.

## jekv2 | 2025-08-24T19:09:25+00:00
> Your benchmark is testing `rx/wow`, it's a different algorithm.

Should I use rx/wow instead to mine?

Now I don't know how the config picks rx.

## SChernykh | 2025-08-24T22:24:46+00:00
Monero uses RandomX (rx). rx/wow is Wownero's algorithm (another coin).

# Action History
- Created by: jekv2 | 2025-08-24T14:46:21+00:00
