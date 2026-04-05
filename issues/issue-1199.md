---
title: '[v4.1.0-beta] Xmrig hangs after a minute'
source_url: https://github.com/xmrig/xmrig/issues/1199
author: YetAnotherRussian
assignees: []
labels:
- bug
- opencl
created_at: '2019-09-27T13:48:34+00:00'
updated_at: '2021-04-12T15:54:01+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:54:01+00:00'
---

# Original Description
CPU: i3-9100F
GPU: RX570-4Gb
OS: Win10 1903

Running from cli:
xmrig.exe --donate-level 4 --no-cpu --opencl -a cn-lite/1 -o ... -u ... -p x --print-time=5

Jobs are received from pool, but no hashrate prints (all nulls) for about a minute, then driver hangs and gets restored.

AMD driver v. 19.9.2

Xmrig-AMD v2.14.6 works perfectly! Of course, w/o specific cli keys.

I checked the launch with config file, and xmrig-amd works perfectly with the same 2-thread-per-gpu config.

# Discussion History
## xmrig | 2019-09-27T14:01:28+00:00
Please show miner output from both versions.
Thank you.

## komatom | 2019-09-28T21:10:06+00:00
I also couln't get it to work with my miners, all are RX570 and RX580.. it compiles for each GPU but it doesn't actually start mining on RandomX(rx) with benchmark pool.

## xmrig | 2019-09-28T21:19:04+00:00
Compile may take very long time, depends of CPU, many minutes, once it completed miner should cache compilation result for future use.

## komatom | 2019-09-28T21:34:34+00:00
here is a screenshot of 8x rx580 rig.. after all the compilation completed, from time to time it mines with 12.3 hashes/s, this rig with xmrig-amd does 7300 hashes per second..

it looks like only one of the cards actually tries to mine.. driver is version 19.5.2

Also it crashes randomly, and takes whole rig with it, and needs hard reset

<img width="544" alt="rig" src="https://user-images.githubusercontent.com/42557814/65822655-906f8700-e250-11e9-89b9-a4a983995eb7.png">



## xmrig | 2019-09-28T21:58:02+00:00
Please show config file, you mention you try mine RandomX, but 7300 H/s not possible on 8 rx580.
Thank you. 

## komatom | 2019-09-28T22:10:05+00:00
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
    "version": 1,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1],
        "cn": [
            [1, 0]
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
        "cn/gpu": [0, 1],
        "rx": [0],
        "rx/wow": [0, 1],
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "url": "randomx-benchmark.xmrig.com:7777",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}

## xmrig | 2019-09-28T22:22:09+00:00
It not looks good, miner should fill `opencl` object in config, like it done in `cpu` object, I requested config for view generated result, but it missing.

## komatom | 2019-09-28T22:28:23+00:00
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
    "version": 1,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": false,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1],
        "cn": [
            [1, 0]
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
        "cn/gpu": [0, 1],
        "rx": [0],
        "rx/wow": [0, 1],
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "cn-heavy": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 4,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 5,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 6,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 7,
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
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 4,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 5,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 6,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 7,
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
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 4,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 5,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 6,
                "intensity": 1728,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 7,
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
            },
            {
                "index": 1,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 2,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 3,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 4,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 5,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 6,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            },
            {
                "index": 7,
                "intensity": 864,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/gpu": [
            {
                "index": 0,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            },
            {
                "index": 1,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            },
            {
                "index": 2,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            },
            {
                "index": 3,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            },
            {
                "index": 4,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            },
            {
                "index": 5,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            },
            {
                "index": 6,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            },
            {
                "index": 7,
                "intensity": 1728,
                "worksize": 8,
                "threads": [-1],
                "unroll": 1
            }
        ],
        "rx": [
            {
                "index": 0,
                "intensity": 864,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 864,
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
            },
            {
                "index": 3,
                "intensity": 864,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 4,
                "intensity": 448,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 5,
                "intensity": 864,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 6,
                "intensity": 864,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 7,
                "intensity": 864,
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
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 1,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 2,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 3,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 4,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 5,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 6,
                "intensity": 576,
                "worksize": 8,
                "threads": [-1, -1],
                "bfactor": 6,
                "gcn_asm": true,
                "dataset_host": false
            },
            {
                "index": 7,
                "intensity": 576,
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
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "url": "randomx-benchmark.xmrig.com:7777",
            "user": "YOUR_WALLET_ADDRESS",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}

## xmrig | 2019-09-28T22:54:11+00:00
On GPUs with 4 GB of memory (where `"intensity": 448`), try change `dataset_host` option to `true`, likely it helps.

Another option, run only one 1 thread on that GPUs `"threads": [-1],`, `intensity` can be increased.

I mark this issue as bug, due workaround of another AMD bug, miner use more memory that expected by autoconfig and 4 GB GPUs running out of memory.

## xmrig | 2019-09-29T16:00:18+00:00
@komatom can you confirm suggestions works for you or not.
Thank you.

## komatom | 2019-09-29T20:34:52+00:00
@xmrig I have done several tests with the settings with your recommendations

it turns out 1 thread but higher intesity is the best performing, each test was around 5 min long. And they run without need of the dataset_host enabled in that case..

1) Test 1 [dataset_host = true, threads 2, intesity 448]
- max  3290.6 h/s

2) Test 2 [dataset_host = true, theads 1, intesity 864]
- max 3618 h/s

3) Test 3 [dataset_host = false, threads 1, intesity 864]
- max 3650.9


## xmrig | 2019-09-30T01:41:38+00:00
Fixed in evo branch, now original configuration with 2 threads should work, however hashrate seems ok, according earlier reports https://github.com/SChernykh/RandomX_OpenCL/issues/5
Thank you.

## komatom | 2019-09-30T06:23:37+00:00
Thank you very much.. Can you point me out to the workaround issue that caused 4GB VRAM to not be enough on rx580 carads?

## xmrig | 2019-09-30T08:55:23+00:00
https://github.com/xmrig/xmrig/commit/6bc217e985d933223756237396fd9b80bde9e45c but this commit part of much larger refactoring https://github.com/xmrig/xmrig/commit/f60118ee79262d09e8042927574762753a80354c

AMD driver not release memory buffers bellow 1 GB, it some kind of optimization and not issue when use similar algorithms, memory not actually leak in this case, but if switch between very different algorithms in runtime (cn <-> rx <-> cn) it make GPU out of memory.

intesity 448 it about 896 MB of memory, but miner was increase buffer size to 1024 MB, so 1024 + 1024 + 2080 (RandomX dataset) is larger that 4 GB, now memory buffer shared between threads and this is already larger than 1 GB ((448 + 448) * 2 = ~1792 MB), so no extra unexpected memory required.

## komatom | 2019-09-30T20:51:04+00:00
@xmrig so I have built the latest evo branch. Should I expect autoconfig to set dataset_host to true or the workaround above was changed so 4GB can run. GPUs still can't run  out of the box..

I also rely on the command options instead of the config file, so each rig autoconfig can set the appropriate settings, without me having to enter a separate config.

it doesn't work on rigs with 8GB too.

here is the command line

xmrig.exe --opencl --no-cpu --http-port 80 -o randomx-benchmark.xmrig.com:7777  -u BENCHMARK.TEST -p x -k

I am not sure if we have applied a solution for this..

Thanks

## xmrig | 2019-10-02T04:49:47+00:00
https://github.com/xmrig/xmrig/releases/tag/v4.2.1-beta

## komatom | 2019-10-02T08:03:32+00:00

 * ABOUT        XMRig/4.2.1-beta MSVC/2017
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          Intel(R) Celeron(R) CPU G3930 @ 2.90GHz (1) x64 AES
                L2:0.5 MB L3:2.0 MB 2C/2T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      randomx-benchmark.xmrig.com:7777 algo auto
 * COMMANDS     hashrate, pause, resume
[2019-10-02 11:00:05.296] configuration saved to: "C:\Users\Anton\Desktop\xmrig-4.2.1-beta\config.json"
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (2841.5)
 * OPENCL GPU   #0 03:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
 * OPENCL GPU   #1 02:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
 * OPENCL GPU   #2 01:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
 * OPENCL GPU   #3 06:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
 * OPENCL GPU   #4 0a:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
 * OPENCL GPU   #5 05:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
 * OPENCL GPU   #6 08:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
 * OPENCL GPU   #7 07:00.0 Radeon RX 580 Series (Ellesmere) 1150MHz cu:36 mem:3840/4096 MB
[2019-10-02 11:00:05.443] use pool randomx-benchmark.xmrig.com:7777  178.128.242.134
[2019-10-02 11:00:05.444] new job from randomx-benchmark.xmrig.com:7777 diff 2951436 algo rx/0 height 1313071
[2019-10-02 11:00:05.446]  rx   init dataset algo rx/0 (2 threads) seed 1fada2b0e5787146...
[2019-10-02 11:00:05.446]  rx   #0 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-10-02 11:00:05.472]  rx   #0 allocate done huge pages 0/1168 0% +JIT (25 ms)
[2019-10-02 11:00:22.144]  rx   #0 init done 1/1 (16696 ms)
[2019-10-02 11:00:22.156]  ocl  use profile  rx  (16 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 03:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 03:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  2 |   1 | 02:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  3 |   1 | 02:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  4 |   2 | 01:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  5 |   2 | 01:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  6 |   3 | 06:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  7 |   3 | 06:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  8 |   4 | 0a:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
|  9 |   4 | 0a:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
| 10 |   5 | 05:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
| 11 |   5 | 05:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
| 12 |   6 | 08:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
| 13 |   6 | 08:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
| 14 |   7 | 07:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)
| 15 |   7 | 07:00.0 |  448 |  8 |  0 |  - |  8 |  896 | Radeon RX 580 Series (Ellesmere)


| OPENCL # | AFFINITY | 10s H/s | 60s H/s | 15m H/s |
|        0 |       -1 |     n/a |     n/a |     n/a | #0 03:00.0 Radeon RX 580 Series (Ellesmere)
|        1 |       -1 |     n/a |     n/a |     n/a | #0 03:00.0 Radeon RX 580 Series (Ellesmere)
|        2 |       -1 |     n/a |     n/a |     n/a | #1 02:00.0 Radeon RX 580 Series (Ellesmere)
|        3 |       -1 |     n/a |     n/a |     n/a | #1 02:00.0 Radeon RX 580 Series (Ellesmere)
|        4 |       -1 |     n/a |     n/a |     n/a | #2 01:00.0 Radeon RX 580 Series (Ellesmere)
|        5 |       -1 |     n/a |     n/a |     n/a | #2 01:00.0 Radeon RX 580 Series (Ellesmere)
|        6 |       -1 |     n/a |     n/a |     n/a | #3 06:00.0 Radeon RX 580 Series (Ellesmere)
|        7 |       -1 |     n/a |     n/a |     n/a | #3 06:00.0 Radeon RX 580 Series (Ellesmere)
|        8 |       -1 |     n/a |     n/a |     n/a | #4 0a:00.0 Radeon RX 580 Series (Ellesmere)
|        9 |       -1 |     n/a |     n/a |     n/a | #4 0a:00.0 Radeon RX 580 Series (Ellesmere)
|       10 |       -1 |     n/a |    23.3 |     n/a | #5 05:00.0 Radeon RX 580 Series (Ellesmere)
|       11 |       -1 |     n/a |    27.6 |     n/a | #5 05:00.0 Radeon RX 580 Series (Ellesmere)
|       12 |       -1 |     n/a |     n/a |     n/a | #6 08:00.0 Radeon RX 580 Series (Ellesmere)
|       13 |       -1 |     n/a |     n/a |     n/a | #6 08:00.0 Radeon RX 580 Series (Ellesmere)
|       14 |       -1 |     n/a |    23.9 |     n/a | #7 07:00.0 Radeon RX 580 Series (Ellesmere)
|       15 |       -1 |     n/a |    23.9 |     n/a | #7 07:00.0 Radeon RX 580 Series (Ellesmere)
|        - |        - |     n/a |    98.7 |     n/a |
[2019-10-02 11:02:28.743] speed 10s/60s/15m n/a 98.7 n/a H/s max n/a H/s
[2019-10-02 11:02:28.770] speed 10s/60s/15m n/a 98.7 n/a H/s max n/a H/s



## komatom | 2019-10-07T15:37:06+00:00
To continue on this issue, I have tested on the other rigs too, only 8GB GPUs work.. definetely 4GB VRAM is not enough

## minzak | 2019-12-02T16:13:17+00:00
@komatom 
> To continue on this issue, I have tested on the other rigs too, only 8GB GPUs work.. definetely 4GB VRAM is not enough

I have some RX580 with 4Gb and some with 8Gb.
Test is still actual?
How much your 580 get Hashes?


## komatom | 2019-12-02T22:18:56+00:00
@bizlevel more on the same issue is on https://github.com/xmrig/xmrig/issues/1336

rx580 gets around ~400/420 hash/s

# Action History
- Created by: YetAnotherRussian | 2019-09-27T13:48:34+00:00
- Closed at: 2021-04-12T15:54:01+00:00
