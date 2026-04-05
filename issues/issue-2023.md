---
title: Low hash rate on the R9 M375X 2GB
source_url: https://github.com/xmrig/xmrig/issues/2023
author: jonkiszp
assignees: []
labels:
- question
- opencl
created_at: '2021-01-05T09:11:29+00:00'
updated_at: '2021-01-10T01:05:09+00:00'
type: issue
status: closed
closed_at: '2021-01-10T01:05:09+00:00'
---

# Original Description
My GPU extracts very poorly, I do not know how to configure it to mine more efficiently and if it is possible at all.

```
 * ABOUT        XMRig/6.7.0 MSVC/2019
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-6820HQ CPU @ 2.70GHz (1) 64-bit AES VM
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       12.9/15.8 GB (82%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      pool.supportxmr.com:443 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3188.4)
 * OPENCL GPU   #0 01:00.0 AMD Radeon (TM) R9 M375X (Capeverde) 925 MHz cu:10 mem:1523/2048 MB
 * CUDA         disabled
[2021-01-05 10:00:53.772]  net      use pool pool.supportxmr.com:443 TLSv1.2 139.99.124.170
[2021-01-05 10:00:53.772]  net      fingerprint (SHA-256): "...."
[2021-01-05 10:00:53.773]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2267728
[2021-01-05 10:00:53.773]  cpu      use argon2 implementation AVX2
[2021-01-05 10:00:53.937]  msr      register values for "intel" preset has been set successfully (164 ms)
[2021-01-05 10:00:53.938]  randomx  init dataset algo rx/0 (8 threads) seed c90630bbd61902e1...
[2021-01-05 10:00:53.985]  randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (46 ms)
[2021-01-05 10:00:58.844]  randomx  dataset ready (4858 ms)
[2021-01-05 10:00:58.844]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-01-05 10:00:58.845]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |        96 |    32 |    192 | AMD Radeon (TM) R9 M375X (Capeverde)
|  1 |   0 | 01:00.0 |        96 |    32 |    192 | AMD Radeon (TM) R9 M375X (Capeverde)
[2021-01-05 10:00:58.862]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (18 ms)
[2021-01-05 10:00:59.305]  opencl   READY threads 2/2 (327 ms)
[2021-01-05 10:00:59.809]  cpu      accepted (1/0) diff 50000 (207 ms)
[2021-01-05 10:01:19.665]  cpu      accepted (2/0) diff 50000 (194 ms)
[2021-01-05 10:01:21.622]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2267729
[2021-01-05 10:01:27.876]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2267730
[2021-01-05 10:01:41.064]  net      new job from pool.supportxmr.com:443 diff 95715 algo rx/0 height 2267730
[2021-01-05 10:01:55.700]  net      new job from pool.supportxmr.com:443 diff 95715 algo rx/0 height 2267731
[2021-01-05 10:01:59.848]  opencl   #0 01:00.0   0W  0C    0RPM 0/0MHz
[2021-01-05 10:01:59.849]  miner    speed 10s/60s/15m 1227.4 1239.1 n/a H/s max 1279.0 H/s
[2021-01-05 10:02:41.111]  net      new job from pool.supportxmr.com:443 diff 50000 algo rx/0 height 2267731
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        0 |   292.8 |   292.3 |     n/a |
|        1 |        2 |   293.7 |   292.4 |     n/a |
|        2 |        4 |   294.6 |   296.9 |     n/a |
|        3 |        6 |   301.4 |   303.4 |     n/a |
|        - |        - |  1182.5 |  1185.0 |     n/a |
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a |     8.02 |      n/a | #0 01:00.0 AMD Radeon (TM) R9 M375X (Capeverde)
|        1 |       -1 |      n/a |     7.86 |      n/a | #0 01:00.0 AMD Radeon (TM) R9 M375X (Capeverde)
|        - |        - |      n/a |      n/a |      n/a |
[2021-01-05 10:02:43.837]  miner    speed 10s/60s/15m 1182.5 1185.0 n/a H/s max 1279.0 H/s
[2021-01-05 10:03:00.796]  opencl   #0 01:00.0   0W  0C    0RPM 0/0MHz
[2021-01-05 10:03:00.796]  miner    speed 10s/60s/15m 1239.4 1192.1 n/a H/s max 1279.0 H/s
```

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
        "argon2": [0, 2, 4, 6, 1, 3, 5],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 1],
            [1, 3],
            [1, 5]
        ],
        "cn-pico": [
            [2, 0],
            [2, 2],
            [2, 4],
            [2, 6],
            [2, 1],
            [2, 3],
            [2, 5]
        ],
        "rx": [0, 2, 4, 6],
        "rx/wow": [0, 2, 4, 6, 1, 3, 5],
        "cn/0": false,
        "cn-lite/0": false,
        "kawpow": false,
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
                "worksize": 1,
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 320,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 80,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 680,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 1000,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 320,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 2621440,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 96,
                "worksize": 32,
                "threads": [-1, -1],
                "bfactor": 8,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "pool.supportxmr.com:443",
            "user": "...",
            "pass": "",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
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
    "pause-on-battery": false
}
```

 - OS: Windows 10
 - For GPU related issues: R9 M375X Radeon Pro Software 04.12.2020

# Discussion History
## SChernykh | 2021-01-05T11:30:27+00:00
No, it's not possible to get higher hashrate on this GPU. RandomX is not for GPUs, try to use your GPU to mine something else.

# Action History
- Created by: jonkiszp | 2021-01-05T09:11:29+00:00
- Closed at: 2021-01-10T01:05:09+00:00
