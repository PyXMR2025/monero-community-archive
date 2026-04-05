---
title: Xmrig crashs trying to enable OPENCL
source_url: https://github.com/xmrig/xmrig/issues/3323
author: mkkc
assignees: []
labels: []
created_at: '2023-08-29T15:12:32+00:00'
updated_at: '2025-06-18T22:33:32+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:33:32+00:00'
---

# Original Description
Hi, I want to enable OPENCL on my Intel server but xmrig allways finishs bad. Can someone help me please ?
Ubuntu 22.04 confirms nvidia driver but on xmrig running it warns "NVRM; NO NVIDIA GPU found."

        VGA compatible controller: Intel Corporation HD Graphics 630 (rev 04) (prog-if 00 [VGA controller])
	DeviceName:  Onboard IGD
	Subsystem: Lenovo HD Graphics 630
	Flags: bus master, fast devsel, latency 0, IRQ 126
	Memory at f6000000 (64-bit, non-prefetchable) [size=16M]
	Memory at e0000000 (64-bit, prefetchable) [size=256M]
	I/O ports at f000 [size=64]
	Expansion ROM at 000c0000 [virtual] [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: i915
	Kernel modules: i915

Output:
 NVRM; NO NVIDIA GPU found. 
 * ABOUT        XMRig/6.20.0 gcc/9.4.0
 * LIBS         libuv/1.44.2 OpenSSL/1.1.1s hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Core(TM) i5-7400 CPU @ 3.00GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       4.4/7.7 GB (58%)
                DIMM_A0: <empty>
                DIMM_A1: 8 GB DDR4 @ 2400 MHz HMA81GU6AFR8N-UH    
                DIMM_B0: <empty>
                DIMM_B1: <empty>
 * MOTHERBOARD  LENOVO - 3102
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      xmrpool.eu:5555 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled (failed to load ADL)
 * OPENCL       #0 Intel(R) OpenCL Graphics/OpenCL 3.0 
 * OPENCL GPU   #0 n/a Intel(R) HD Graphics 630 1000 MHz cu:23 mem:3136/6272 MB
 * CUDA         disabled
[2023-08-29 14:48:48.333]  net      use pool xmrpool.eu:5555  51.89.217.80
[2023-08-29 14:48:48.333]  net      new job from xmrpool.eu:5555 diff 60000 algo rx/0 height 2962541 (41 tx)
[2023-08-29 14:48:48.333]  cpu      use argon2 implementation AVX2
[2023-08-29 14:48:48.334]  msr      register values for "intel" preset have been set successfully (0 ms)
[2023-08-29 14:48:48.334]  randomx  init dataset algo rx/0 (4 threads) seed d4940fe71f46136f...
[2023-08-29 14:48:48.548]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (213 ms)
[2023-08-29 14:48:53.151]  randomx  dataset ready (4603 ms)
[2023-08-29 14:48:53.151]  cpu      use profile  rx  (3 threads) scratchpad 2048 KB
[2023-08-29 14:48:53.151]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 |     n/a |       320 |     8 |    640 | Intel(R) HD Graphics 630
[2023-08-29 14:48:53.174]  cpu      READY threads 3/3 (3) huge pages 100% 3/3 memory 6144 KB (24 ms)
[2023-08-29 14:48:54.010]  opencl   GPU #0 compiling...
free(): invalid pointer
Aborted

config.json
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
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
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
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2]
        ],
        "rx": [0, 1, 2],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "Intel",
        "adl": true,
        "cn": [
            {
                "index": 0,
                "intensity": 184,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 184,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 368,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 368,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 184,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 368,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 6029312,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
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
    "log-file": "/home/kelo/xmrig-6.20.0/xmrig.log",
    "donate-level": 5,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "monero",
            "url": "xmrpool.eu:5555",
            "user": "47JnmznQLZzVLRfccMmrzbYQjmdDeh8AhjW6Cp5jen3HPWT453vT6QPSjytSFp6X4TJ8SiAfcZJAhZd1xQPbzkb7LSZPSH3",
            "pass": "x",
            "rig-id": "test",
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
    "retries": 1,
    "retry-pause": 5,
    "print-time": 1800,
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
## SChernykh | 2023-08-29T17:36:30+00:00
> [2023-08-29 14:48:54.010] opencl GPU #0 compiling...
free(): invalid pointer
Aborted

This is a bug in Intel's OpenCL driver - it can't compile RandomX code. Even if you find some driver version that works, enabling OpenCL on an integrated GPU will only reduce your total hashrate.

TLDR: it's pointless to even try to fix it.

## mkkc | 2023-08-29T18:57:40+00:00
Thanks for your explanation. My only chance is to move this to Windows ?

# Action History
- Created by: mkkc | 2023-08-29T15:12:32+00:00
- Closed at: 2025-06-18T22:33:32+00:00
