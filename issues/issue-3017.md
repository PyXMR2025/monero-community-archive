---
title: opencl   disabled (no suitable configuration found)
source_url: https://github.com/xmrig/xmrig/issues/3017
author: SasaNa1982
assignees: []
labels: []
created_at: '2022-04-10T17:57:58+00:00'
updated_at: '2024-04-05T18:30:34+00:00'
type: issue
status: closed
closed_at: '2022-04-10T18:29:46+00:00'
---

# Original Description
Can you help me? I have this problem with xmrig:

 * ABOUT        XMRig/6.17.0 gcc/11.2.0
 * LIBS         libuv/1.43.0 OpenSSL/1.1.1m hwloc/2.7.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 5 3600 6-Core Processor (1) 64-bit AES
                L2:3.0 MB L3:32.0 MB 6C/12T NUMA:1
 * MEMORY       5.0/15.9 GB (31%)
                DIMM_A0: <empty>
                DIMM_A1: 8 GB DDR4 @ 3200 MHz F4-3200C16-8GIS
                DIMM_B0: <empty>
                DIMM_B1: 8 GB DDR4 @ 3200 MHz F4-3200C16-8GIS
 * MOTHERBOARD  Gigabyte Technology Co., Ltd. - B450M S2H V2
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      my.bugminer.org:3032 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3380.6)
 * OPENCL GPU   #0 11:00.0 Radeon RX550/550 Series (gfx803) 1206 MHz cu:8 mem:1792/2048 MB
 * CUDA         disabled
[2022-04-10 19:41:48.112]  net      use pool my.bugminer.org:3032  89.40.11.196
[2022-04-10 19:41:48.112]  net      new job from my.bugminer.org:3032 diff 32768 algo ghostrider height 4513
[2022-04-10 19:41:48.113]  msr      to access MSR registers Administrator privileges required.
[2022-04-10 19:41:48.113]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2022-04-10 19:41:49.452]  cpu      use profile  ghostrider  (6 threads) scratchpad 2048 KB
[2022-04-10 19:41:49.452]  opencl   disabled (no suitable configuration found)
[2022-04-10 19:41:49.574]  cpu      GhostRider algo 1: cn/fast (2 MB)
[2022-04-10 19:41:49.574]  cpu      GhostRider algo 2: cn/lite (1 MB)
[2022-04-10 19:41:49.574]  cpu      GhostRider algo 3: cn/dark (512 KB)
[2022-04-10 19:41:49.576]  cpu      READY threads 12/12 (48) huge pages 100% 48/48 memory 98304 KB (124 ms)


config.json is:

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
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "astrobwt/v2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
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
            [1, 2],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 11]
        ],
        "cn-lite": [
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
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 64,
                "threads": [-1, -1]
            }
        ],
        "astrobwt/v2": [
            {
                "index": 0,
                "intensity": 1024,
                "threads": [-1]
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 96,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 800,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 992,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 992,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 2097152,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 128,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": true
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
            "algo": "ghostrider",
            "coin": null,
            "url": "my.bugminer.org:3032",
            "user": "Bj78o2cBJKa7njGt1Uog89XHnk6gnqihQs",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
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

# Discussion History
## SChernykh | 2022-04-10T18:02:55+00:00
GhostRider is supported only on CPU, so opencl is disabled.

## SasaNa1982 | 2022-04-10T18:29:46+00:00
ok thanks. i remember it now 

## ghost | 2024-04-05T18:30:33+00:00
> GhostRider is supported only on CPU, so opencl is disabled.

its possible to mine ghostrider on gpu, its not the best but also not the worst. Can reduce memory all the way. Some cards do quite well for the watts. 

Is it not possible to enable for people who want this?

Otherwise the only option is wildrig

# Action History
- Created by: SasaNa1982 | 2022-04-10T17:57:58+00:00
- Closed at: 2022-04-10T18:29:46+00:00
