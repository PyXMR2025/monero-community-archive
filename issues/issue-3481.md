---
title: Vega 56 crash when using OpenCL
source_url: https://github.com/xmrig/xmrig/issues/3481
author: halbGefressen
assignees: []
labels: []
created_at: '2024-05-19T15:58:31+00:00'
updated_at: '2025-06-18T22:13:31+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:13:31+00:00'
---

# Original Description
When mining with XMRig 6.21.3 on Vega56, the GPU crashes after about 10 seconds.

Start xmrig with the following config: 

```
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
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
                "intensity": 896,
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
                "intensity": 14680064,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 896,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": false
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    }
```


 
Arch Linux, ROCm Core 6.0.2, AMDGPU 23.40



# Discussion History
## halbGefressen | 2024-05-19T16:12:49+00:00
Log: 

```
 * ABOUT        XMRig/6.21.3 gcc/13.2.1 (built for Linux x86-64, 64 bit)
 * LIBS         libuv/1.48.0 OpenSSL/3.2.1 hwloc/2.10.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-8600K CPU @ 3.60GHz (1) 64-bit AES
                L2:1.5 MB L3:9.0 MB 6C/6T NUMA:1
 * MEMORY       2.4/31.2 GB (8%)
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      xmrpool.eu:5555 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP.dbg (3602.0)
 * OPENCL GPU   #0 03:00.0 AMD Radeon RX Vega (gfx900:xnack-) 1590 MHz cu:56 mem:6949/8176 MB
 * CUDA         disabled
[2024-05-19 18:07:25.409]  net      use pool xmrpool.eu:5555  51.89.217.80
[2024-05-19 18:07:25.409]  net      new job from xmrpool.eu:5555 diff 60000 algo rx/0 height 3152515 (73 tx)
[2024-05-19 18:07:25.409]  cpu      use argon2 implementation AVX2
[2024-05-19 18:07:25.412]  msr      cannot read MSR 0x000001a4
[2024-05-19 18:07:25.412]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2024-05-19 18:07:25.412]  randomx  init dataset algo rx/0 (6 threads) seed b357e40629a64466...
[2024-05-19 18:07:25.412]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2024-05-19 18:07:27.575]  randomx  dataset ready (2163 ms)
[2024-05-19 18:07:27.575]  cpu      use profile  rx  (5 threads) scratchpad 2048 KB
[2024-05-19 18:07:27.575]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 03:00.0 |       896 |     8 |   1792 | AMD Radeon RX Vega (gfx900:xnack-)
|  1 |   0 | 03:00.0 |       896 |     8 |   1792 | AMD Radeon RX Vega (gfx900:xnack-)
[2024-05-19 18:07:27.594]  cpu      READY threads 5/5 (5) huge pages 0% 0/5 memory 10240 KB (19 ms)
[2024-05-19 18:07:28.105]  opencl   READY threads 2/2 (530 ms)

```

# Action History
- Created by: halbGefressen | 2024-05-19T15:58:31+00:00
- Closed at: 2025-06-18T22:13:31+00:00
