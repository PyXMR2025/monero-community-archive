---
title: '"failed to load OpenCL runtime" error with latest AMD drivers on ubuntu 18.04
  (kawpow)'
source_url: https://github.com/xmrig/xmrig/issues/2510
author: BugerDread
assignees: []
labels: []
created_at: '2021-08-06T09:46:23+00:00'
updated_at: '2025-06-20T11:11:21+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:11:21+00:00'
---

# Original Description
**Describe the bug**
Decided to update my kawpow miner (using AMD polaris cards) running:
- xmrig 6.12.0
- ubuntu 18.04 using 5.4.0-48 kernel (hwe)
- amdgpu-pro - Version: 20.10-1048554

.. to the latest - that means kernel 5.4.0-80, xmrig 6.13.1 and amdgpu-pro-21.30-1286092 for now

After that I got just "failed to load OpenCL runtime" OpenCL error in xmrig (no matter if I used 6.12.0 or 6.13.1). Tried also previous drives as 21.20, 20.50, 20.40 - all the same result.

Then I found #1975 and tried to locate libOpenCL.so on my system ... and I found it is installed as libOpenCL.so.1 - so put the path to it into xmrig config into opencl "loader" - like this:
```
 "opencl": {
        "enabled": true,
        "cache": true,
        "loader": "/opt/amdgpu-pro/lib/x86_64-linux-gnu/libOpenCL.so.1",
        "platform": "AMD",
        "adl": true,

```
... and woala - xmrig was able to detect opencl devices and finally started to mine.

For some reason it strarted to mine using only one gpu (there are 3 in this miner) and crashed every time I was trying to stop it using crtl+c, but this was solved by installing previous version of amd drives (amdgpu-pro-21.20-1274019) - so I expect this is driver bug, not xmrig.

**To Reproduce**
Install xmrig on fully updated ubuntu 18.04 hwe with recent amd drivers amdgpu-pro-21.20 (or 21.30 but these caused the only-one-gpu-mining problem for me) and try to mine kawpow on polaris cards

**Expected behavior**
Xmrig should detect the libOpenCL.so.1 without need to add the path into config, or the need to add such path for new drivers should be mentioned in readme

**Required data**
Miner log as text or screenshot
```
$ xmrig-6.13.1/xmrig -c xmrig.json.bak 
 * ABOUT        XMRig/6.13.1 gcc/7.5.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) 64-bit -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.0/2.8 GB (35%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      kawpow.eu.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled (failed to load OpenCL runtime)
 * CUDA         disabled
[2021-08-06 11:32:20.808]  net      use pool kawpow.eu.nicehash.com:3385  172.65.200.133
[2021-08-06 11:32:20.848] [kawpow.eu.nicehash.com:3385] incompatible/disabled algorithm "kawpow" detected, reconnect
[2021-08-06 11:32:20.848]  net      no active pools, stop mining
[2021-08-06 11:32:24.703]  signal   Ctrl+C received, exiting
```
Config file or command line (without wallets)
```
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
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
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
                "intensity": 192,
                "worksize": 1,
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 192,
                "worksize": 1,
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 192,
                "worksize": 1,
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 768,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 448,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
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
            },
            {
                "index": 1,
                "intensity": 224,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
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
                "intensity": 1792,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 952,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
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
            },
            {
                "index": 1,
                "intensity": 952,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
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
                "intensity": 768,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 448,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
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
                "intensity": 1792,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 952,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
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
                "intensity": 8388608,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 3670016,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 8388608,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 2,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 2,
                "intensity": 512,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 512,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 2,
                "intensity": 512,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "kawpow",
            "coin": null,
            "url": "kawpow.eu.nicehash.com:3385",
            "user": "RREEMMOOVVEEDD.m04",
            "pass": "x",
            "rig-id": null,
            "nicehash": true,
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

```
OS: [e.g. Windows], For GPU related issues: information about GPUs and driver version
```
ubuntu 18.04 hwe
Linux m04 5.4.0-80-generic #90~18.04.1-Ubuntu SMP Tue Jul 13 19:40:02 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
amdgpu-pro 21.20-1274019
2x RX470 + RX460 4GB
```

**Additional context**
Kawpowminer (https://github.com/RavenCommunity/kawpowminer) works without problems / needs to tweak paths, but xmrig is faster


# Discussion History
## Spudz76 | 2021-08-06T16:38:04+00:00
Interesting.  Most other miners (PhoenixMiner for one) require 20.30-1109583 maximum since every newer driver broke stuff.  Wouldn't be surprised if the same applied here, especially for < Vega.

20.30 works for me with Nano Fury / Hawaii / Polaris.

# Action History
- Created by: BugerDread | 2021-08-06T09:46:23+00:00
- Closed at: 2025-06-20T11:11:21+00:00
