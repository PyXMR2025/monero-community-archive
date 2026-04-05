---
title: OpenCL | AMD Radeon RX580 | CL_INVALID_PROGRAM failed to start threads
source_url: https://github.com/xmrig/xmrig/issues/2556
author: Z33DD
assignees: []
labels: []
created_at: '2021-08-24T17:24:12+00:00'
updated_at: '2025-06-20T11:11:13+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:11:13+00:00'
---

# Original Description
This bug happen when I try use OpenCL with my AMD GPU, I'm in Arch Linux.

## XMRig log
```bash
$ xmrig --opencl -a rx/0 -o ca.monero.herominers.com:10191 -u MONERO_ADDR -k --tls
 * ABOUT        XMRig/6.14.1 gcc/11.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1k hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          AMD Opteron(tm) Processor 4122 (1) 64-bit -AES
                L2:2.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       7.5/7.8 GB (96%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      ca.monero.herominers.com:10191 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #1 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3302.5)
 * OPENCL GPU   #0 04:00.0 Radeon RX 580 Series (Ellesmere) 1360 MHz cu:36 mem:6745/8192 MB
 * CUDA         disabled
[2021-08-24 14:16:41.518]  net      use pool ca.monero.herominers.com:10191 TLSv1.2 168.119.69.50
[2021-08-24 14:16:41.518]  net      fingerprint (SHA-256): "92f09d7f6ed816236a62cecb0f4165d83f44f204374f7d0647545616ed833ea1"
[2021-08-24 14:16:41.519]  net      new job from ca.monero.herominers.com:10191 diff 120001 algo rx/0 height 2434238 (1 tx)
[2021-08-24 14:16:41.519]  cpu      use argon2 implementation SSE2
[2021-08-24 14:16:42.720]  randomx  init dataset algo rx/0 (4 threads) seed ba1705f92ec017a7...
[2021-08-24 14:16:42.720]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2021-08-24 14:17:14.524]  randomx  dataset ready (31804 ms)
[2021-08-24 14:17:14.531]  cpu      use profile  rx  (3 threads) scratchpad 2048 KB
[2021-08-24 14:17:14.536]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 04:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 04:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
[2021-08-24 14:17:14.576]  cpu      READY threads 3/3 (3) huge pages 0% 0/3 memory 6144 KB (41 ms)
[2021-08-24 14:17:16.199]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2021-08-24 14:17:16.199]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2021-08-24 14:17:16.203]  opencl   thread #0 self-test failed
[2021-08-24 14:17:16.247]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2021-08-24 14:17:16.248]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2021-08-24 14:17:16.253]  opencl   thread #1 self-test failed
[2021-08-24 14:17:16.253]  opencl   disabled (failed to start threads)
[2021-08-24 14:17:19.920]  signal   Ctrl+C received, exiting
[2021-08-24 14:17:19.932]  cpu      stopped (11 ms)
[2021-08-24 14:17:19.933]  opencl   stopped (1 ms)

~ took 41s
```

## clinfo output
```bash
$ clinfo -l
Platform #0: Clover
 `-- Device #0: Radeon RX 580 Series (POLARIS10, DRM 3.41.0, 5.13.12-arch1-1, LLVM 12.0.1)
Platform #1: AMD Accelerated Parallel Processing
 `-- Device #0: Ellesmere
```

## XMrig config file
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
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
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
        "loader": "/usr/lib/libOpenCL.so",
        "platform": "AMD",
        "adl": true,
        "astrobwt": [
            {
                "index": 0,
                "intensity": 256,
                "worksize": 1,
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
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
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 9437184,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
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
            "algo": "rx/0",
            "coin": "monero",
            "url": "ca.monero.herominers.com:10191",
            "user": "MONERO_ADDR",
            "pass": null,
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
}
```

# Discussion History
## Spudz76 | 2021-08-24T22:52:06+00:00
GPUs don't do RandomX and when they do it's a watt-wasting miracle anyway.  We could debug why it's not working however all that would do is prove you can burn energy for barely any payout.

You should run two installs of xmrig in different folders, with one configured for OpenCL enabled but CPU disabled, and the other CPU enabled with all GPU stuff disabled.  Use slightly different rig-id (I add `-nv` or `-amd` to ones on GPUs) and then point them both at MoneroOcean so you just get paid XMR for whatever your stuff is best at, and what that work is worth at the moment.  That way they can run different algos since they are quite different at various talents.

## Z33DD | 2021-08-24T23:14:31+00:00
@Spudz76 Thanks for you answer. But this error happens when the CPU is disabled too. I'm new to this mining stuff (but I in crypto for long time), what settings should I use to get profit with this AMD RX580?


## Spudz76 | 2021-08-25T19:45:14+00:00
I usually recompile my xmrig that is for GPUs with `-DWITH_RANDOMX=OFF` so that it can't.

Otherwise you have to keep setting `rx*` profiles it recreates to `false` to disable them all.

## DeeDeeRanged | 2021-09-03T09:54:25+00:00
Or OpenCL is not properly installed.

## Spudz76 | 2021-09-03T23:52:46+00:00
The stack looks okay, Clover (Mesa OpenCL) can sometimes get in the way but it is selecting the AMD proprietary ICD (platform index 1) at least.  It could be loading the vanilla amdgpu kernel module vs the proprietary one, such as if dkms failed to build and install, and that may not mesh well with the proprietary ICD.

Maybe it needs the standard set of mining environment vars:
```
export GPU_SINGLE_ALLOC_PERCENT=100
export GPU_USE_SYNC_OBJECTS=1
export GPU_MAX_ALLOC_PERCENT=100
export GPU_FORCE_64BIT_PTR=1
export GPU_MAX_HEAP_SIZE=100
```

And sometimes flipping the `GPU_FORCE_64BIT_PTR` to 0 helps beyond that but that may have been with something other than xmrig.

# Action History
- Created by: Z33DD | 2021-08-24T17:24:12+00:00
- Closed at: 2025-06-20T11:11:13+00:00
