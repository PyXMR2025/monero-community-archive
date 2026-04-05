---
title: OPENCL failed with error CL_INVALID_BUFFER_SIZE_ - KAWPOW Algorithm
source_url: https://github.com/xmrig/xmrig/issues/2773
author: JoseAlmela
assignees: []
labels: []
created_at: '2021-12-02T18:23:31+00:00'
updated_at: '2021-12-02T19:07:24+00:00'
type: issue
status: closed
closed_at: '2021-12-02T19:07:24+00:00'
---

# Original Description
**Describe the bug**
When you mine using kawpow algorithm with amd GPU an error  occurs with OpenCL:
_error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 3355443200
[2021-12-02 19:09:41.210]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE_

**To Reproduce**
Launch XMRIG using the config provide here (kawpow, OpenCL only) 

**Expected behavior**
The hashrate should be bigger than N/A

**Required data**
 - Miner log as text or screenshot
![imagen](https://user-images.githubusercontent.com/12251493/144479409-04d67723-cedb-485d-bef3-71c37af57197.png)

 - Config file or command line (without wallets)
`{
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
        "enabled": false,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false
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
                "intensity": 128,
                "worksize": 1,
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 896,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 448,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 1792,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 1792,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 896,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 1792,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 7340032,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 192,
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
                "intensity": 448,
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
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "kawpow",
            "coin": null,
            "url": "rvn.2miners.com:16060",
            "user": "MYWALLET",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
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
}`
 - OS: Windows
 - For GPU related issues: information about GPUs and driver version.
Radeon Software 21.5.2
**Additional context**
I've rediced the intensity value in kawpow config with no success.


# Discussion History
## SChernykh | 2021-12-02T18:27:40+00:00
KawPow requires 3.25 GB memory for DAG, your GPU has 3 GB memory, you do the math.

## JoseAlmela | 2021-12-02T18:30:11+00:00
Overflow!!
Where can I find that information in the docs?
thank you very much.

# Action History
- Created by: JoseAlmela | 2021-12-02T18:23:31+00:00
- Closed at: 2021-12-02T19:07:24+00:00
