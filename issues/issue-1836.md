---
title: memory leak - kawpow opencl
source_url: https://github.com/xmrig/xmrig/issues/1836
author: BugerDread
assignees: []
labels:
- bug
- opencl
- kawpow
created_at: '2020-09-15T20:32:04+00:00'
updated_at: '2020-10-03T05:22:35+00:00'
type: issue
status: closed
closed_at: '2020-10-03T05:22:34+00:00'
---

# Original Description
**Describe the bug**
xmrig mines normally but consumes more and more memory while mining kawpow on AMD GPUs, after few days all memory is used (on my 3 or 4GB rigs), when all memory + swap is used the miner crash or whole system becomes unresponsive

**To Reproduce**
mine kawpow with xmrig on ubuntu 18.04 with RX 460 / 470 / 570 / 560 GPUs (4GB GDDR5) and watch free memory (for example watch MemFree in /proc/meminfo)

here is chart of MemFree in /proc/meminfo for my rigs - there is constant downtrend of the free memory (and recoveries as I restarted the xmrig), the most right part of it looks wierd because I was trying to change different stuff to fix this and restarted the miners many times, but with no result

![image](https://user-images.githubusercontent.com/26651175/93259358-080b2e80-f7a0-11ea-8434-8a4f175d969a.png)

**Expected behavior**
xmrig shoud not use all ram + swap during few days

**Required data**
***rig bla01***
- Ubuntu 18.04.5 LTS
- 3GB RAM, 4GB swap
- Linux bla01 5.4.0-45-lowlatency #49~18.04.2-Ubuntu SMP PREEMPT Wed Aug 26 17:20:55 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
- amdgpu-pro 20.10-1048554
- xmrig info
```
 * ABOUT        XMRig/6.3.3 gcc/7.4.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) x64 -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.0/2.8 GB (35%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      kawpow.eu.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3075.10)
 * OPENCL GPU   #0 01:00.0 Radeon RX 570 Series (Ellesmere) 1340 MHz cu:32 mem:3839/4090 MB
 * OPENCL GPU   #1 04:00.0 Radeon RX 570 Series (Ellesmere) 1340 MHz cu:32 mem:3839/4090 MB
 * OPENCL GPU   #2 05:00.0 Radeon RX 570 Series (Ellesmere) 1340 MHz cu:32 mem:3839/4090 MB
 * OPENCL GPU   #3 06:00.0 Radeon RX 570 Series (Ellesmere) 1340 MHz cu:32 mem:3839/4090 MB
 * CUDA         disabled
[2020-09-15 21:53:32.803]  net      use pool kawpow.eu.nicehash.com:3385  172.65.200.133
[2020-09-15 21:53:32.841]  net      new job from kawpow.eu.nicehash.com:3385 diff 557M algo kawpow height 1409161
[2020-09-15 21:53:32.841]  opencl   use profile  kawpow  (4 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |   8388608 |   256 |   2559 | Radeon RX 570 Series (Ellesmere)
|  1 |   1 | 04:00.0 |   8388608 |   256 |   2559 | Radeon RX 570 Series (Ellesmere)
|  2 |   2 | 05:00.0 |   8388608 |   256 |   2559 | Radeon RX 570 Series (Ellesmere)
|  3 |   3 | 06:00.0 |   8388608 |   256 |   2559 | Radeon RX 570 Series (Ellesmere)
[2020-09-15 21:53:33.960]  opencl   READY threads 4/4 (1119 ms)
```
***rig m04***
- Ubuntu 18.04.5 LTS
- 4GB RAM + 2GB swap
- Linux m04 5.4.0-42-lowlatency #46~18.04.1-Ubuntu SMP PREEMPT Fri Jul 10 08:10:40 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
- amdgpu-pro 20.10-1048554
- xmrig info
```
 * ABOUT        XMRig/6.3.2 gcc/7.4.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) x64 -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       0.7/3.8 GB (19%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      kawpow.eu.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3075.10)
 * OPENCL GPU   #0 01:00.0 AMD Radeon (TM) RX 470 Graphics (Ellesmere) 1236 MHz cu:32 mem:3839/4090 MB
 * OPENCL GPU   #1 04:00.0 AMD Radeon (TM) RX 460 Graphics (Baffin) 1250 MHz cu:14 mem:3839/4090 MB
 * OPENCL GPU   #2 05:00.0 AMD Radeon (TM) RX 470 Graphics (Ellesmere) 1236 MHz cu:32 mem:3839/4090 MB
 * OPENCL GPU   #3 06:00.0 Radeon RX 570 Series (Ellesmere) 1268 MHz cu:32 mem:3839/4090 MB
 * CUDA         disabled
[2020-09-15 21:42:12.290]  net      use pool kawpow.eu.nicehash.com:3385  172.65.200.133
[2020-09-15 21:42:12.336]  net      new job from kawpow.eu.nicehash.com:3385 diff 557M algo kawpow height 1409150
[2020-09-15 21:42:12.336]  opencl   use profile  kawpow  (4 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |   8388608 |   256 |   2559 | AMD Radeon (TM) RX 470 Graphics (Ellesmere)
|  1 |   1 | 04:00.0 |   3670016 |   256 |   2559 | AMD Radeon (TM) RX 460 Graphics (Baffin)
|  2 |   2 | 05:00.0 |   8388608 |   256 |   2559 | AMD Radeon (TM) RX 470 Graphics (Ellesmere)
|  3 |   3 | 06:00.0 |   8388608 |   256 |   2559 | Radeon RX 570 Series (Ellesmere)
[2020-09-15 21:42:13.131]  opencl   READY threads 4/4 (795 ms)
```

***rig m07***
- Ubuntu 18.04.3 LTS
- 4GB RAM + 2GB swap
- Linux m07 5.0.0-25-generic #26~18.04.1-Ubuntu SMP Thu Aug 1 13:51:02 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
- amdgpu-pro 19.30-855429
- xmrig info
```
 * ABOUT        XMRig/6.3.0 gcc/5.4.0
 * LIBS         libuv/1.38.0 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) x64 -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       1.0/3.8 GB (28%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      kawpow.eu.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (2906.7)
 * OPENCL GPU   #0 01:00.0 Radeon RX 560 Series (Baffin) 1196 MHz cu:16 mem:3839/4090 MB
 * OPENCL GPU   #1 05:00.0 Radeon RX 560 Series (Baffin) 1196 MHz cu:16 mem:3839/4090 MB
 * OPENCL GPU   #2 06:00.0 Radeon RX 560 Series (Baffin) 1196 MHz cu:16 mem:3839/4090 MB
 * CUDA         disabled
[2020-09-15 21:47:01.938]  net      use pool kawpow.eu.nicehash.com:3385  172.65.200.133
[2020-09-15 21:47:01.977]  net      new job from kawpow.eu.nicehash.com:3385 diff 557M algo kawpow height 1409154
[2020-09-15 21:47:01.977]  opencl   use profile  kawpow  (3 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |   4194304 |   256 |   2559 | Radeon RX 560 Series (Baffin)
|  1 |   1 | 05:00.0 |   4194304 |   256 |   2559 | Radeon RX 560 Series (Baffin)
|  2 |   2 | 06:00.0 |   4194304 |   256 |   2559 | Radeon RX 560 Series (Baffin)
[2020-09-15 21:47:02.542]  opencl   READY threads 3/3 (564 ms)
```
***rig m08***
- Ubuntu 18.04.3 LTS
- 3GB RAM + 2GB swap
- Linux m08 5.0.0-37-generic #40~18.04.1-Ubuntu SMP Thu Nov 14 12:06:39 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
- amdgpu-pro 19.50-967956
- xmrig info
```
 * ABOUT        XMRig/6.3.3 gcc/7.5.0
 * LIBS         libuv/1.38.1 OpenSSL/1.1.1g hwloc/2.2.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM)2 CPU 6600 @ 2.40GHz (1) x64 -AES
                L2:4.0 MB L3:0.0 MB 2C/2T NUMA:1
 * MEMORY       0.7/2.8 GB (25%)
 * DONATE       1%
 * ASSEMBLY     auto:none
 * POOL #1      kawpow.eu.nicehash.com:3385 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     192.168.88.108:8899 
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3004.6)
 * OPENCL GPU   #0 01:00.0 AMD Radeon (TM) RX 460 Graphics (Baffin) 1236 MHz cu:14 mem:3839/4090 MB
 * OPENCL GPU   #1 04:00.0 AMD Radeon (TM) RX 460 Graphics (Baffin) 1236 MHz cu:14 mem:3839/4090 MB
 * OPENCL GPU   #2 05:00.0 AMD Radeon (TM) RX 460 Graphics (Baffin) 1236 MHz cu:14 mem:3839/4090 MB
 * OPENCL GPU   #3 06:00.0 AMD Radeon (TM) RX 460 Graphics (Baffin) 1236 MHz cu:14 mem:3839/4090 MB
 * CUDA         disabled
[2020-09-15 21:50:03.751]  net      use pool kawpow.eu.nicehash.com:3385  172.65.200.133
[2020-09-15 21:50:03.792]  net      new job from kawpow.eu.nicehash.com:3385 diff 557M algo kawpow height 1409156
[2020-09-15 21:50:03.792]  opencl   use profile  kawpow  (4 threads) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |   3670016 |   256 |   2559 | AMD Radeon (TM) RX 460 Graphics (Baffin)
|  1 |   1 | 04:00.0 |   3670016 |   256 |   2559 | AMD Radeon (TM) RX 460 Graphics (Baffin)
|  2 |   2 | 05:00.0 |   3670016 |   256 |   2559 | AMD Radeon (TM) RX 460 Graphics (Baffin)
|  3 |   3 | 06:00.0 |   3670016 |   256 |   2559 | AMD Radeon (TM) RX 460 Graphics (Baffin)
[2020-09-15 21:50:04.556]  opencl   READY threads 4/4 (764 ms)
```

example of config file (from m08):
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "192.168.88.108",
        "port": 8899,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1],
        "astrobwt": [0, 1],
        "cn": [
            [1, 0],
            [1, 1]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1]
        ],
        "rx": [0, 1],
        "rx/wow": [0, 1],
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
            },
            {
                "index": 3,
                "intensity": 192,
                "worksize": 1,
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn": [
            {
                "index": 0,
                "intensity": 448,
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
                "intensity": 448,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 448,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 168,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 168,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 168,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 168,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 952,
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
                "intensity": 952,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 952,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 952,
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
                "intensity": 952,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 952,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "intensity": 448,
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
                "intensity": 448,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 448,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "intensity": 3670016,
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
                "intensity": 3670016,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 3670016,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 192,
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
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 3,
                "intensity": 192,
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
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": true
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
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 3,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": true
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": true
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
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 3,
                "intensity": 192,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
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
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "kawpow",
            "coin": null,
            "url": "kawpow.eu.nicehash.com:3385",
            "user": "ADDRESS-REMOVED.m08",
            "pass": "x",
            "rig-id": null,
            "nicehash": true,
            "keepalive": true,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
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


**Additional context**
- this happends with xmrg downloaded as binary and also compiled from source on all my rigs
- same situation with older kernel / drivers
- amd drivers installed with --opencl=legacy --headless
- when xmrig is stopped (before it eats all the memory + swap) the memory is released

If you need more information I will be happy to help.


# Discussion History
## BugerDread | 2020-09-24T18:31:39+00:00
Here are charts showing again the same situation ("teploty" means "temperatures" in Czech, if temperatures go down instantly it usually signalize that miner stopped / crashed, if there are no data it means the linux crashed completely)
- bla01 used all memory and crashed completely
- m08 used all memory and xmirg crashed with:
```
xmrig: src/threadpool.c:329: uv__queue_done: Assertion `uv__has_active_reqs(req->loop)' failed. 
./start: line 8:  1679 Aborted                 (core dumped) ./xmrig
```
![image](https://user-images.githubusercontent.com/26651175/94184581-6c1aaa80-fea4-11ea-8b71-4509164e4bf0.png)

![image](https://user-images.githubusercontent.com/26651175/94184255-eeef3580-fea3-11ea-8d4b-a3a73e96de75.png)
![image](https://user-images.githubusercontent.com/26651175/94184275-f9113400-fea3-11ea-9290-c9b21710bf0b.png)
![image](https://user-images.githubusercontent.com/26651175/94184320-06c6b980-fea4-11ea-9333-20e91c13bf77.png)


## SChernykh | 2020-09-25T08:55:06+00:00
Can you try to compile and test dev branch with #1846 ?

## BugerDread | 2020-09-26T21:37:21+00:00
Yes, it seems that memory leak is fixed, thanks a lot!

## xmrig | 2020-10-03T05:22:34+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.3.5

# Action History
- Created by: BugerDread | 2020-09-15T20:32:04+00:00
- Closed at: 2020-10-03T05:22:34+00:00
