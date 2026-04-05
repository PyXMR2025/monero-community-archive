---
title: 'MacOS: opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram'
source_url: https://github.com/xmrig/xmrig/issues/2188
author: mrsubtle
assignees: []
labels: []
created_at: '2021-03-16T21:12:17+00:00'
updated_at: '2021-04-12T13:55:52+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:55:52+00:00'
---

# Original Description
Trying to give XMRig a chance on my mac (OS 10.15.7) and I get an OpenCL error trying to mine RVN (kawpow) via 2miners.
```
[2021-03-16 16:03:44.408] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * ABOUT        XMRig/6.10.0 clang/12.0.0
 * LIBS         libuv/1.41.0 OpenSSL/1.0.2n hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       31.7/32.0 GB (99%)
                DIMM_A0: 16 GB DDR4 @ 2667 MHz MT40A2G8NEA-062E:J  
                DIMM_B0: 16 GB DDR4 @ 2667 MHz MT40A2G8NEA-062E:J  
 * MOTHERBOARD  Apple Inc. - Mac-E1008331FDC96864
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      rvn.2miners.com:6060 coin ravencoin
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     127.0.0.1:60057 
[2021-03-16 16:03:44.413] Error CL_INVALID_OPERATION when calling clGetDeviceInfo, param 0x4037
 * OPENCL       #0 Apple/OpenCL 1.2 (Jan  5 2021 23:17:05)
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 630 1150 MHz cu:24 mem:384/1536 MB
 * OPENCL GPU   #1 n/a AMD Radeon Pro 5500M Compute Engine 1450 MHz cu:24 mem:2044/8176 MB
 * CUDA         disabled
[2021-03-16 16:03:44.709]  net      use pool rvn.2miners.com:6060  51.89.96.116
[2021-03-16 16:03:44.709]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 1669768
[2021-03-16 16:03:44.709]  cpu      disabled (no suitable configuration found)
[2021-03-16 16:03:44.710]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   1 |     n/a |   6291456 |   256 |   2843 | AMD Radeon Pro 5500M Compute Engine
[2021-03-16 16:03:44.712]  opencl   GPU #1 compiling...
[2021-03-16 16:03:44.713]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Error returned by cvms_element_build_from_source
[2021-03-16 16:03:44.713]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-03-16 16:03:44.714]  opencl   thread #0 self-test failed
[2021-03-16 16:03:44.714]  opencl   disabled (failed to start threads)
[2021-03-16 16:04:03.759]  net      new job from rvn.2miners.com:6060 diff 4295M algo kawpow height 1669769
[2021-03-16 16:04:03.759]  cpu      disabled (no suitable configuration found)
[2021-03-16 16:04:44.986]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
```
And it just loops from there, trying to get blocks from the pool.
Issue seems to be two-fold (CPU issue and a GPU issue), the GPU fails with:
```
[2021-03-16 16:03:44.713]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
```

My config:
```
{
    "api": {
        "id": null,
        "worker-id": "RIG_2"
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
        "wrmsr": false,
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
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4]
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
        "rx": [0, 2, 4, 6, 8, 10],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 64,
                "threads": [-1, -1]
            },
            {
                "index": 1,
                "intensity": 256,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 1,
                "intensity": 768,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 1,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1920,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 1,
                "intensity": 768,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 1,
                "intensity": 6291456,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 320,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 384,
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
                "intensity": 384,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 384,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 384,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "kawpow",
            "coin": "RVN",
            "url": "rvn.2miners.com:6060",
            "user": "REDACTED",
            "pass": null,
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
    "pause-on-battery": false,
    "pause-on-active": false
}
```

Let me know if I need to provide more.

# Discussion History
## SChernykh | 2021-03-16T21:16:56+00:00
This is a driver problem, there's nothing we can do here. MacOS OpenCL has been in a very bad shape for a very long time.

# Action History
- Created by: mrsubtle | 2021-03-16T21:12:17+00:00
- Closed at: 2021-04-12T13:55:52+00:00
