---
title: 'Segfault Arch linux '
source_url: https://github.com/xmrig/xmrig/issues/2303
author: ghost
assignees: []
labels: []
created_at: '2021-04-23T11:55:41+00:00'
updated_at: '2021-04-25T19:19:09+00:00'
type: issue
status: closed
closed_at: '2021-04-25T19:19:08+00:00'
---

# Original Description
**Describe the bug**
I enabled opencl using the package opencl-amd from the aur. 

**To Reproduce**
install opencl-amd,
enable opencl,
segfault

#LOG FILE
```
 * ABOUT        XMRig/6.8.2 gcc/5.4.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 3 3200G with Radeon Vega Graphics (1) 64-bit AES
                L2:2.0 MB L3:4.0 MB 4C/4T NUMA:1
 * MEMORY       12.7/13.7 GB (93%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2400 MHz CMK16GX4M2A2400C16  
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2400 MHz CMK16GX4M2A2400C16  
 * MOTHERBOARD  Gigabyte Technology Co., Ltd. - A320M-S2H-CF
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-us-east1.nanopool.org:14433 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-04-22 21:53:28.595]  config   configuration saved to: ".config/xmrig.json"
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.0 AMD-APP (3246.0)
 * OPENCL GPU   #0 0b:00.0 AMD Ryzen 3 3200G with Radeon Vega Graphics (gfx902:xnack+) 1250 MHz cu:11 mem:5947/6997 MB
 * OPENCL GPU   #1 03:00.0 Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (gfx1012:xnack+) 1900 MHz cu:11 mem:6949/8176 MB
 * CUDA         disabled
[2021-04-22 21:53:28.986]  net      use pool xmr-us-east1.nanopool.org:14433 TLSv1.2 192.99.69.170
[2021-04-22 21:53:28.986]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2021-04-22 21:53:28.986]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2345322
[2021-04-22 21:53:28.986]  cpu      use argon2 implementation AVX2
[2021-04-22 21:53:28.994]  msr      register values for "ryzen_17h" preset have been set successfully (8 ms)
[2021-04-22 21:53:30.194]  randomx  init dataset algo rx/0 (4 threads) seed 15564c3122550436...
[2021-04-22 21:53:30.598]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (404 ms)
[2021-04-22 21:53:39.600]  randomx  dataset ready (9001 ms)
[2021-04-22 21:53:39.600]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-04-22 21:53:39.601]  opencl   use profile  rx  (4 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 0b:00.0 |       128 |     8 |    256 | AMD Ryzen 3 3200G with Radeon Vega Graphics (gfx902:xnack+)
|  1 |   0 | 0b:00.0 |       128 |     8 |    256 | AMD Ryzen 3 3200G with Radeon Vega Graphics (gfx902:xnack+)
|  2 |   1 | 03:00.0 |       128 |     8 |    256 | Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (gfx1012:xnack+)
|  3 |   1 | 03:00.0 |       128 |     8 |    256 | Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (gfx1012:xnack+)
[2021-04-22 21:53:39.606]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (5 ms)
 * ABOUT        XMRig/6.8.2 gcc/5.4.0
 * LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Ryzen 3 3200G with Radeon Vega Graphics (1) 64-bit AES
                L2:2.0 MB L3:4.0 MB 4C/4T NUMA:1
 * MEMORY       11.5/13.7 GB (84%)
                DIMM 0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2400 MHz CMK16GX4M2A2400C16  
                DIMM 0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2400 MHz CMK16GX4M2A2400C16  
 * MOTHERBOARD  Gigabyte Technology Co., Ltd. - A320M-S2H-CF
 * DONATE       5%
 * ASSEMBLY     auto:ryzen
 * POOL #1      xmr-us-east1.nanopool.org:14433 coin monero
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-04-22 21:54:29.322]  config   configuration saved to: ".config/xmrig.json"
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.0 AMD-APP (3246.0)
 * OPENCL GPU   #0 0b:00.0 AMD Ryzen 3 3200G with Radeon Vega Graphics (gfx902:xnack+) 1250 MHz cu:11 mem:5947/6997 MB
 * OPENCL GPU   #1 03:00.0 Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (gfx1012:xnack+) 1900 MHz cu:11 mem:6949/8176 MB
 * CUDA         disabled
[2021-04-22 21:54:29.724]  net      use pool xmr-us-east1.nanopool.org:14433 TLSv1.2 142.44.242.100
[2021-04-22 21:54:29.724]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2021-04-22 21:54:29.724]  net      new job from xmr-us-east1.nanopool.org:14433 diff 480045 algo rx/0 height 2345322
[2021-04-22 21:54:29.724]  cpu      use argon2 implementation AVX2
[2021-04-22 21:54:29.732]  msr      0xc0011020:0x0206800000000000 -> 0x0000000000000000
[2021-04-22 21:54:29.732]  msr      0xc0011022:0x0000000000510000 -> 0x0000000001510000
[2021-04-22 21:54:29.732]  msr      0xc001102b:0x000000002000cc16 -> 0x000000002000cc16
[2021-04-22 21:54:29.732]  msr      0xc0011021:0x0000000000000040 -> 0x0000000000000040
[2021-04-22 21:54:29.732]  msr      register values for "ryzen_17h" preset have been set successfully (8 ms)
[2021-04-22 21:54:30.932]  randomx  init dataset algo rx/0 (4 threads) seed 15564c3122550436...
[2021-04-22 21:54:31.332]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (400 ms)
[2021-04-22 21:54:40.375]  randomx  dataset ready (9043 ms)
[2021-04-22 21:54:40.375]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-04-22 21:54:40.375]  opencl   use profile  rx  (4 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 0b:00.0 |       128 |     8 |    256 | AMD Ryzen 3 3200G with Radeon Vega Graphics (gfx902:xnack+)
|  1 |   0 | 0b:00.0 |       128 |     8 |    256 | AMD Ryzen 3 3200G with Radeon Vega Graphics (gfx902:xnack+)
|  2 |   1 | 03:00.0 |       128 |     8 |    256 | Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (gfx1012:xnack+)
|  3 |   1 | 03:00.0 |       128 |     8 |    256 | Navi 14 [Radeon RX 5500/5500M / Pro 5500M] (gfx1012:xnack+)
[2021-04-22 21:54:40.381]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (6 ms)
```
#CONFIG
```json
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
        "huge-pages-jit": true,
        "hw-aes": false,
        "priority": 1,
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
            [1, 1]
        ],
        "cn-heavy": [
            [1, 0]
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
        "rx": [0, 1, 2, 3],
        "rx/wow": [0, 1, 2, 3],
        "cn/0": false,
        "cn-lite/0": false,
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
                "intensity": 256,
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
                "index": 0,
                "intensity": 480,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 480,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 240,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 240,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 968,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 968,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 968,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 968,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 480,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 480,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 2883584,
                "worksize": 256,
                "threads": [-1]
            },
            {
                "index": 1,
                "intensity": 2883584,
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
                "gcn_asm": false,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 128,
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
        "loader": null,
        "nvml": true
    },
    "log-file": "xmrig.log",
    "donate-level": 5,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "xmr-us-east1.nanopool.org:14433",
            "user": null,
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
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
    "verbose": 1,
    "watch": true,
    "pause-on-battery": false
}
```
 - Config file or command line (without wallets)
 - OS: Arch linux 5.11.15-zen1-2-zen




# Discussion History
## ghost | 2021-04-25T19:19:08+00:00
Solved, Disabled internal graphic

# Action History
- Created by: ghost | 2021-04-23T11:55:41+00:00
- Closed at: 2021-04-25T19:19:08+00:00
