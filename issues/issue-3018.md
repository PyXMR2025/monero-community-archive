---
title: ' opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram'
source_url: https://github.com/xmrig/xmrig/issues/3018
author: SasaNa1982
assignees: []
labels: []
created_at: '2022-04-10T18:28:33+00:00'
updated_at: '2025-06-20T11:06:14+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:06:14+00:00'
---

# Original Description
Can you help me? i have this other problem:

 * ABOUT        XMRig/6.16.2 gcc/10.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          AMD Ryzen 5 3600 6-Core Processor (1) 64-bit AES
                L2:3.0 MB L3:32.0 MB 6C/12T NUMA:1
 * MEMORY       3.7/15.9 GB (23%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 3200 MHz F4-3200C16-8GIS
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 3200 MHz F4-3200C16-8GIS
 * MOTHERBOARD  Gigabyte Technology Co., Ltd. - B450M S2H V2
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool-pay.com:26590 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.2 AMD-APP (3417.0)
 * OPENCL GPU   #0 11:00.0 Radeon RX550/550 Series (gfx803) 1206 MHz cu:8 mem:1792/2048 MB
 * CUDA         disabled
[2022-04-10 20:16:53.586]  net      use pool pool-pay.com:26590  5.9.95.125
[2022-04-10 20:16:53.586]  net      new job from pool-pay.com:26590 diff 5000 algo rx/graft (1 tx)
[2022-04-10 20:16:53.586]  cpu      use argon2 implementation AVX2
[2022-04-10 20:16:53.787]  msr      register values for "ryzen_17h" preset have been set successfully (201 ms)
[2022-04-10 20:16:53.787]  randomx  init dataset algo rx/graft (12 threads) seed aea8c9c6d5c0c049...
[2022-04-10 20:16:53.787]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2022-04-10 20:16:56.232]  randomx  dataset ready (2444 ms)
[2022-04-10 20:16:56.232]  cpu      use profile  rx  (11 threads) scratchpad 2048 KB
[2022-04-10 20:16:56.232]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 11:00.0 |       128 |     8 |    256 | Radeon RX550/550 Series (gfx803)
|  1 |   0 | 11:00.0 |       128 |     8 |    256 | Radeon RX550/550 Series (gfx803)
[2022-04-10 20:16:56.262]  cpu      READY threads 11/11 (11) huge pages 100% 11/11 memory 22528 KB (30 ms)
[2022-04-10 20:16:56.570]  opencl   GPU #0 compiling...
[2022-04-10 20:16:56.644]  cpu      accepted (1/0) diff 5000 (56 ms)
[2022-04-10 20:16:57.216]  cpu      accepted (2/0) diff 5000 (57 ms)
[2022-04-10 20:16:57.545]  cpu      accepted (3/0) diff 5000 (60 ms)
[2022-04-10 20:16:57.807]  cpu      accepted (4/0) diff 5000 (52 ms)
[2022-04-10 20:16:58.628]  cpu      accepted (5/0) diff 5000 (59 ms)
[2022-04-10 20:17:00.011]  cpu      accepted (6/0) diff 5000 (53 ms)
[2022-04-10 20:17:00.103]  cpu      accepted (7/0) diff 5000 (128 ms)
[2022-04-10 20:17:00.218]  cpu      accepted (8/0) diff 5000 (119 ms)
[2022-04-10 20:17:00.311]  cpu      accepted (9/0) diff 5000 (129 ms)
[2022-04-10 20:17:00.396]  cpu      accepted (10/0) diff 5000 (123 ms)
[2022-04-10 20:17:00.912]  cpu      accepted (11/0) diff 5000 (52 ms)
[2022-04-10 20:17:01.117]  cpu      accepted (12/0) diff 5000 (53 ms)
[2022-04-10 20:17:01.301]  cpu      accepted (13/0) diff 5000 (203 ms)
[2022-04-10 20:17:02.943]  cpu      accepted (14/0) diff 5000 (55 ms)
[2022-04-10 20:17:03.154]  cpu      accepted (15/0) diff 5000 (39 ms)
[2022-04-10 20:17:04.122]  cpu      accepted (16/0) diff 5000 (52 ms)
[2022-04-10 20:17:06.898]  cpu      accepted (17/0) diff 5000 (58 ms)
[2022-04-10 20:17:07.117]  cpu      accepted (18/0) diff 5000 (56 ms)
[2022-04-10 20:17:09.120]  cpu      accepted (19/0) diff 5000 (67 ms)
[2022-04-10 20:17:10.017]  cpu      accepted (20/0) diff 5000 (59 ms)
[2022-04-10 20:17:10.095]  cpu      accepted (21/0) diff 5000 (39 ms)
[2022-04-10 20:17:10.869]  cpu      accepted (22/0) diff 5000 (62 ms)
[2022-04-10 20:17:11.728]  cpu      accepted (23/0) diff 5000 (39 ms)
[2022-04-10 20:17:12.576]  cpu      accepted (24/0) diff 5000 (38 ms)
[2022-04-10 20:17:12.795]  cpu      accepted (25/0) diff 5000 (38 ms)
[2022-04-10 20:17:13.392]  cpu      accepted (26/0) diff 5000 (39 ms)
[2022-04-10 20:17:15.145]  cpu      accepted (27/0) diff 5000 (39 ms)
[2022-04-10 20:17:16.688]  cpu      accepted (28/0) diff 5000 (39 ms)
[2022-04-10 20:17:17.513]  opencl   GPU #0 compilation completed (20942 ms)
[2022-04-10 20:17:17.517]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-04-10 20:17:17.517]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2022-04-10 20:17:17.525]  opencl   thread #1 self-test failed
[2022-04-10 20:17:17.549]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-04-10 20:17:17.549]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2022-04-10 20:17:17.557]  opencl   thread #0 self-test failed
[2022-04-10 20:17:17.558]  opencl   disabled (failed to start threads)
[2022-04-10 20:17:17.630]  cpu      accepted (29/0) diff 5000 (68 ms)
[2022-04-10 20:17:20.676]  net      new job from pool-pay.com:26590 diff 10000 algo rx/graft (1 tx)
[2022-04-10 20:17:22.217]  cpu      accepted (30/0) diff 10000 (57 ms)
[2022-04-10 20:17:22.361]  cpu      accepted (31/0) diff 10000 (39 ms)

config.json:
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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
            [1, 10]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 8],
            [1, 10]
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
            [1, 10]
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
            [2, 10]
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
            [2, 10]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10]
        ],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool-pay.com:26590",
            "user": "Sasa1982",
            "pass": "x@worker1",
            "rig-id": "worker1",
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
}

# Discussion History
# Action History
- Created by: SasaNa1982 | 2022-04-10T18:28:33+00:00
- Closed at: 2025-06-20T11:06:14+00:00
