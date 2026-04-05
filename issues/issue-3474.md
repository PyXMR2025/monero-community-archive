---
title: Im getting an Error when i try to mine on RX 470 Graphics card
source_url: https://github.com/xmrig/xmrig/issues/3474
author: MrDuckyQuack
assignees: []
labels: []
created_at: '2024-05-02T10:36:15+00:00'
updated_at: '2025-06-18T22:14:53+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:14:53+00:00'
---

# Original Description
Hello, im getting this error when i try to mine with my graphics card

`[2024-05-02 12:28:58.272]  net      use pool xmrig.nanswap.com:3333  51.15.19.228
[2024-05-02 12:28:58.273]  net      new job from xmrig.nanswap.com:3333 diff 10000 algo rx/0 height 3140050 (12 tx)
[2024-05-02 12:28:58.273]  cpu      use argon2 implementation AVX2
[2024-05-02 12:28:58.378]  msr      register values for "intel" preset have been set successfully (104 ms)
[2024-05-02 12:28:58.378]  randomx  init dataset algo rx/0 (4 threads) seed a562192734fced5f...
[2024-05-02 12:28:58.378]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2024-05-02 12:29:02.690]  randomx  dataset ready (4312 ms)
[2024-05-02 12:29:02.691]  cpu      use profile  rx  (3 threads) scratchpad 2048 KB
[2024-05-02 12:29:02.691]  opencl   use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       448 |     8 |    896 | Radeon (TM) RX 470 Graphics (Ellesmere)
|  1 |   0 | 01:00.0 |       448 |     8 |    896 | Radeon (TM) RX 470 Graphics (Ellesmere)
[2024-05-02 12:29:02.745]  cpu      READY threads 3/3 (3) huge pages 100% 3/3 memory 6144 KB (54 ms)
[2024-05-02 12:29:03.061]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2024-05-02 12:29:03.062]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2024-05-02 12:29:03.077]  opencl   thread #0 self-test failed
[2024-05-02 12:29:03.084]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2024-05-02 12:29:03.084]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2024-05-02 12:29:03.092]  opencl   thread #1 self-test failed
[2024-05-02 12:29:03.093]  opencl   disabled (failed to start threads)`


my config.json

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
        "platform": "AMD",
        "adl": true,
        "cn": [
            {
                "index": 0,
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
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 8388608,
                "worksize": 256,
                "threads": [-1],
                "unroll": 1
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
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmrig.nanswap.com:3333",
            "user": "nano_36md8essnzezafgu7aceba457wxjanwdstocmhm4dfyz7ktfd6ogccmosp8r",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "sni": false,
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

# Discussion History
## snipeTR | 2024-05-02T15:53:18+00:00
Kardo 
1 cüzdan adresin gözüküyor.
2 bu madenci cpu kullanıyor.

## MrDuckyQuack | 2024-05-02T16:37:54+00:00
> Kardo 1 cüzdan adresin gözüküyor. 2 bu madenci cpu kullanıyor.

1 sorun olurmu?
2 gpu ve cpu kullanmak istiyorum ama gpu da hata veriyor.

## Spudz76 | 2024-06-07T14:41:30+00:00
Needs minimum 3GB, have 896KB somehow.

# Action History
- Created by: MrDuckyQuack | 2024-05-02T10:36:15+00:00
- Closed at: 2025-06-18T22:14:53+00:00
