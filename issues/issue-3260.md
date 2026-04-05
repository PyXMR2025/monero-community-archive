---
title: zsh abort XMRIG
source_url: https://github.com/xmrig/xmrig/issues/3260
author: Stone-0211
assignees: []
labels: []
created_at: '2023-04-21T13:35:58+00:00'
updated_at: '2025-06-18T22:34:46+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:34:46+00:00'
---

# Original Description
I found out that zsh abort xmrig,how to fix it? I mine ETH with a graphics card on MacOS Ventura13.1
zsh's feedback is this:
 * ABOUT        XMRig/6.16.4 clang/12.0.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1i hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       10.5/16.0 GB (66%)
                DIMM_A0: 8 GB DDR4 @ 2667 MHz HMA81GS6CJR8N-VK    
                DIMM_B0: 8 GB DDR4 @ 2667 MHz HMA81GS6CJR8N-VK    
 * MOTHERBOARD  Apple Inc. - Mac-E1008331FDC96864
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      kp.unmineable.com:13333 algo kawpow
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       #0 Apple/OpenCL 1.2 (Nov  4 2022 20:34:07)
 * OPENCL GPU   #0 n/a Intel(R) UHD Graphics 630 1150 MHz cu:24 mem:384/1536 MB
 * OPENCL GPU   #1 n/a AMD Radeon Pro 5300M Compute Engine 1250 MHz cu:20 mem:1020/4080 MB
 * CUDA         disabled
[2023-04-21 21:24:35.236]  net      use pool kp.unmineable.com:13333  146.190.45.196
[2023-04-21 21:24:35.237]  net      new job from kp.unmineable.com:13333 diff 4295M algo kawpow height 2765239
[2023-04-21 21:24:35.238]  opencl   use profile  kawpow  (1 thread) scratchpad 32 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   1 |     n/a |     36864 |   256 |   4029 | AMD Radeon Pro 5300M Compute Engine
[2023-04-21 21:24:36.158]  opencl   GPU #1 compiling...
[2023-04-21 21:24:36.382]  opencl   GPU #1 compilation completed (225 ms)
[2023-04-21 21:24:36.382]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2023-04-21 21:24:36.382]  opencl   READY threads 1/1 (1146 ms)
[2023-04-21 21:24:36.813]  opencl   KawPow program for period 921746 compiled (431ms)
[2023-04-21 21:24:37.233]  opencl   KawPow program for period 921747 compiled (420ms)
[2023-04-21 21:24:43.352]  miner    KawPow light cache for epoch 368 calculated (6544ms)
zsh: abort      /Users/shuang/Stone/xmrig-6.18.0/xmrig

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

Below is my config.json

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
        "wrmsr": false,
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
        "cn-lite/0": false,
        "cn/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "cn": [
            {
                "index": 1,
                "intensity": 320,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-heavy": [
            {
                "index": 1,
                "intensity": 160,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "intensity": 192,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 800,
                "worksize": 8,
                "strided_index": [1, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1920,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/2": [
            {
                "index": 1,
                "intensity": 320,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "intensity": 384,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            },
            {
                "index": 1,
                "intensity": 1920,
                "worksize": 8,
                "strided_index": [2, 2],
                "threads": [-1, -1],
                "unroll": 8
            }
        ],
        "kawpow": [
            {
                "index": 1,
                "intensity": 36864,
                "worksize": 256,
                "threads": [-1],
                "unroll": 8
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
                "dataset_host": true
            },
            {
                "index": 1,
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
                "intensity": 384,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 1280,
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
                "intensity": 384,
                "worksize": 8,
                "threads": [-1],
                "bfactor": 6,
                "gcn_asm": false,
                "dataset_host": true
            },
            {
                "index": 1,
                "intensity": 896,
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
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "kawpow",
            "coin": null,
            "url": "kp.unmineable.com:13333",
            "user": "ETH:0xfe831a378e037726d0826a0c688d39722398a2a4.stone",
            "pass": "x",
            "rig-id": null,
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
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
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

This is the entire file
[xmrig-6.19.2 .zip](https://github.com/xmrig/xmrig/files/11296167/xmrig-6.19.2.zip)

how can i fix it?Please help me thanks!

# Discussion History
## DeeDeeRanged | 2023-04-24T09:20:58+00:00
What would the command line be without using the config.json file 

Mine would be something like this (XMR):
xmrig --http-host=0.0.0.0 --http-port=10050 --http-access-token="your_pw" --http-no-restricted -o ip-address:3333 -u x+50000

Why still mining ETH as this is not supported with xmrig?



## Stone-0211 | 2023-04-24T11:27:00+00:00
OK,it's like this:
[2023-04-24 19:27:27.479] unable to open "/Users/shuang/Downloads/xmrig-6.19.2 /config.json".
[2023-04-24 19:27:27.479] unable to open "/Users/shuang/.xmrig.json".
[2023-04-24 19:27:27.480] unable to open "/Users/shuang/.config/xmrig.json".
[2023-04-24 19:27:27.480] no valid configuration found, try https://xmrig.com/wizard

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.



## DeeDeeRanged | 2023-04-29T14:31:15+00:00
> OK,it's like this: [2023-04-24 19:27:27.479] unable to open "/Users/shuang/Downloads/xmrig-6.19.2 /config.json". [2023-04-24 19:27:27.479] unable to open "/Users/shuang/.xmrig.json". [2023-04-24 19:27:27.480] unable to open "/Users/shuang/.config/xmrig.json". [2023-04-24 19:27:27.480] no valid configuration found, try https://xmrig.com/wizard
> 
> Saving session... ...copying shared history... ...saving history...truncating history files... ...completed.

Thats is not what I actually asked. I meant how you actually start xmrig.

From the command line/terminal should be something like this.:
./xmrig --opencl -o kp.unmineable.com:13333 -u ETH:Your_Wallet.stone -p x -k -a kawpow
or
./xmrig -c config.json if your config.json is correct.

All in the same directory where you put xmrig
If I look at unmineable.com XMRig is not mentioned as a miner. I would suggest SRBMiner-MULTI if you cannot get XMRig working.



# Action History
- Created by: Stone-0211 | 2023-04-21T13:35:58+00:00
- Closed at: 2025-06-18T22:34:46+00:00
