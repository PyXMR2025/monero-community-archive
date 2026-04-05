---
title: OpenGL error
source_url: https://github.com/xmrig/xmrig/issues/2279
author: Glucy-2
assignees: []
labels: []
created_at: '2021-04-18T03:42:11+00:00'
updated_at: '2021-04-30T12:40:51+00:00'
type: issue
status: closed
closed_at: '2021-04-30T12:40:51+00:00'
---

# Original Description
opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
opencl   thread #0 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE

log:
````python
 * ABOUT        XMRig/6.11.2 MSVC/2019
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz (1) 64-bit AES VM
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       16.8/23.9 GB (70%)
                DIMM_A0: 8 GB DDR4 @ 2667 MHz KHX2666C16/8G
                DIMM_A1: 8 GB DDR4 @ 2667 MHz KHX2666C16/8G
                ChannelB-DIMM0: <empty>
                DIMM_B1: 8 GB DDR4 @ 2667 MHz F4-3200C16-8GRKB
 * MOTHERBOARD  MSI - MS-7A63
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          disabled
 * OPENCL       #0 NVIDIA CUDA/OpenCL 1.2 CUDA 11.2.162
 * OPENCL GPU   #0 02:00.0 GeForce GTX 1060 6GB 1784 MHz cu:10 mem:1536/6144 MB
 * OPENCL GPU   #1 01:00.0 GeForce GTX 750 Ti 1137 MHz cu:5 mem:512/2048 MB
 * CUDA         11.0/11.2/6.4.0
 * NVML         11.461.92/461.92 press e for health report
 * CUDA GPU     #0 02:00.0 GeForce GTX 1060 6GB 1784/4004 MHz smx:10 arch:61 mem:5222/6144 MB
 * CUDA GPU     #1 01:00.0 GeForce GTX 750 Ti 1137/2900 MHz smx:5 arch:50 mem:1677/2048 MB
[2021-04-18 11:32:01.343]  net      use pool xmr.f2pool.com:13531  47.100.95.105
[2021-04-18 11:32:01.344]  net      new job from xmr.f2pool.com:13531 diff 65537 algo rx/0 height 2341736
[2021-04-18 11:32:01.344]  cpu      use argon2 implementation AVX2
[2021-04-18 11:32:01.344]  msr      service WinRing0_1_2_0 already exists
[2021-04-18 11:32:01.344]  msr      service path: "\??\D:\MAX_XiaoKui\AppData\Local\Temp\tmp8A2F.tmp"
[2021-04-18 11:32:01.359]  msr      register values for "intel" preset have been set successfully (15 ms)
[2021-04-18 11:32:01.360]  randomx  init dataset algo rx/0 (8 threads) seed ed3e9b30bff5b032...
[2021-04-18 11:32:01.705]  randomx  allocated 2336 MB (2080+256) huge pages 11% 128/1168 +JIT (345 ms)
[2021-04-18 11:32:06.063]  randomx  dataset ready (4358 ms)
[2021-04-18 11:32:06.064]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-04-18 11:32:06.067]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (2 ms)
[2021-04-18 11:32:06.543]  opencl   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   1 | 01:00.0 |        64 |     8 |    128 | GeForce GTX 750 Ti
[2021-04-18 11:32:06.760]  nvidia   use profile  rx  (1 thread) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | THREADS | BLOCKS | BF |  BS | MEMORY | NAME
|  0 |   1 | 01:00.0 |       320 |      32 |     10 |  8 |  25 |    640 | GeForce GTX 750 Ti
[2021-04-18 11:32:06.765]  opencl   GPU #1 compiling...
[2021-04-18 11:32:06.878]  opencl   GPU #1 compilation completed (111 ms)
[2021-04-18 11:32:06.882]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2021-04-18 11:32:06.884]  opencl   READY threads 1/1 (124 ms)
[2021-04-18 11:32:06.898]  opencl   error CL_MEM_OBJECT_ALLOCATION_FAILURE when calling clEnqueueNDRangeKernel for kernel execute_vm
[2021-04-18 11:32:06.901]  opencl   thread #0 failed with error CL_MEM_OBJECT_ALLOCATION_FAILURE
[2021-04-18 11:32:07.425]  nvidia   READY threads 1/1 (663 ms)
[2021-04-18 11:32:25.914]  net      new job from xmr.f2pool.com:13531 diff 65537 algo rx/0 height 2341737
[2021-04-18 11:32:28.100]  nvidia   accepted (1/0) diff 65537 (16 ms)
[2021-04-18 11:32:51.253]  net      new job from xmr.f2pool.com:13531 diff 65537 algo rx/0 height 2341738
[2021-04-18 11:33:06.330]  nvidia   #0 02:00.0 112W 71C 1961/4303 MHz fan0:57%
[2021-04-18 11:33:06.331]  nvidia   #1 01:00.0  24W 59C 1222/2900 MHz fan0:34%
[2021-04-18 11:33:06.331]  miner    speed 10s/60s/15m 1139.4 n/a n/a H/s max 1365.1 H/s
[2021-04-18 11:33:09.996]  cpu      accepted (2/0) diff 65537 (17 ms)
[2021-04-18 11:33:13.860]  cpu      accepted (3/0) diff 65537 (17 ms)
[2021-04-18 11:33:39.706]  cpu      accepted (4/0) diff 65537 (16 ms)
[2021-04-18 11:33:54.237]  net      new job from xmr.f2pool.com:13531 diff 65537 algo rx/0 height 2341739
[2021-04-18 11:34:06.371]  nvidia   #0 02:00.0 112W 70C 1961/4303 MHz fan0:57%
[2021-04-18 11:34:06.374]  nvidia   #1 01:00.0  25W 62C 1222/2900 MHz fan0:35%
[2021-04-18 11:34:06.379]  miner    speed 10s/60s/15m 1134.3 1084.6 n/a H/s max 1365.1 H/s
[2021-04-18 11:34:07.066]  cpu      accepted (5/0) diff 65537 (16 ms)
[2021-04-18 11:34:20.616]  cpu      accepted (6/0) diff 65537 (16 ms)
[2021-04-18 11:35:00.680]  net      new job from xmr.f2pool.com:13531 diff 65537 algo rx/0 height 2341740
[2021-04-18 11:35:03.918]  cpu      accepted (7/0) diff 65537 (23 ms)
[2021-04-18 11:35:06.418]  nvidia   #0 02:00.0 112W 70C 1961/4303 MHz fan0:56%
[2021-04-18 11:35:06.420]  nvidia   #1 01:00.0  25W 64C 1222/2900 MHz fan0:35%
[2021-04-18 11:35:06.424]  miner    speed 10s/60s/15m 1183.1 1165.3 n/a H/s max 1365.1 H/s
|    CPU # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |        1 |   256.8 |   230.0 |     n/a |
|        1 |        3 |   302.0 |   284.3 |     n/a |
|        2 |        5 |   249.6 |   224.4 |     n/a |
|        3 |        7 |   290.5 |   273.8 |     n/a |
|        - |        - |  1098.9 |  1012.6 |     n/a |
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a |      n/a |      n/a | #1 01:00.0 GeForce GTX 750 Ti
|        - |        - |      n/a |      n/a |      n/a |
|   CUDA # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |    93.51 |    93.43 |      n/a | #1 01:00.0 GeForce GTX 750 Ti
|        - |        - |    93.17 |    93.36 |      n/a |
````

GPU: 
GTX 750 Ti
GTX 1060

I edited the config file to only use GTX 750 Ti only.

config:
````json
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
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
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "rx": [1, 3, 5, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "NVIDIA",
        "adl": false,
        "astrobwt": [
            {
                "index": 1,
                "intensity": 64,
                "threads": [-1, -1]
            }
        ],
        "cn": [
            {
                "index": 1,
                "intensity": 160,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 1,
                "intensity": 80,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 1,
                "intensity": 360,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 1,
                "intensity": 1520,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 1,
                "intensity": 160,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 1,
                "intensity": 1310720,
                "worksize": 256,
                "threads": [-1]
            }
        ],
        "rx": [
            {
                "index": 1,
                "intensity": 64,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": true,
        "loader": null,
        "nvml": true,
        "astrobwt": [
            {
                "index": 1,
                "threads": 32,
                "blocks": 5,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn": [
            {
                "index": 1,
                "threads": 50,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-heavy": [
            {
                "index": 1,
                "threads": 24,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-lite": [
            {
                "index": 1,
                "threads": 100,
                "blocks": 15,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn-pico": [
            {
                "index": 1,
                "threads": 4,
                "blocks": 40,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "cn/2": [
            {
                "index": 1,
                "threads": 4,
                "blocks": 40,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "kawpow": [
            {
                "index": 1,
                "threads": 256,
                "blocks": 10240,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1
            }
        ],
        "rx": [
            {
                "index": 1,
                "threads": 32,
                "blocks": 10,
                "bfactor": 8,
                "bsleep": 25,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn/0": false,
        "cn-lite/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmr.f2pool.com:13531",
            "user": "485JjESK23j1ZZz9LqANPFYVTCq53KMhuJD2MYbiM93hGN6ivLVFXcGEwZtdenZARoLFXovgfzVSU5Qa7WbQfjoe3L8Sfma",
            "pass": "x",
            "rig-id": null,
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
````

# Discussion History
## SChernykh | 2021-04-18T08:28:59+00:00
You have 2 NVIDIA GPUs, why did you enable both OpenCL and CUDA in the config? Disable OpenCL and leave CUDA only.

## Glucy-2 | 2021-04-30T12:40:51+00:00
OK, thanks.

# Action History
- Created by: Glucy-2 | 2021-04-18T03:42:11+00:00
- Closed at: 2021-04-30T12:40:51+00:00
