---
title: settings for cpu mining
source_url: https://github.com/xmrig/xmrig/issues/2790
author: protopoloji
assignees: []
labels: []
created_at: '2021-12-04T15:54:57+00:00'
updated_at: '2025-06-20T11:08:00+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:08:00+00:00'
---

# Original Description
Hello, I have centos server with 64 cores and 256gb of ram. I can not set the configuration for all available memory and CPU cores.
I'm using the binary version of xmrig. Could you please help me for the configuration to use all the cores and ram available. I'm mining shiba inu. Thank you.


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
        "wrmsr": false,
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
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14],
            [1, 16],
            [1, 18],
            [1, 20],
            [1, 22],
            [1, 24],
            [1, 26],
            [1, 28],
            [1, 30],
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
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6]
        ],
        "rx": [0, 2, 4, 6],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
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
            "algo": null,
            "coin": null,
            "url": "rx.unmineable.com:3333",
            "user": "SHIB:0xF547100BAD4bb63fF59BDf743d27377C66ff21D2.enderulusoy",
            "pass": "xxx",
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
## Spudz76 | 2021-12-04T17:19:47+00:00
Looks like you have 8MB of cache, therefore 4 threads regardless what excess threads or RAM you have.

## protopoloji | 2021-12-04T17:22:10+00:00
I have 8 pyhsical cpus located. and more than 256gb of ram. Doesn't work ?

## Spudz76 | 2021-12-04T17:24:21+00:00
What CPUs.  The startup page of xmrig shows everything we'd need to give support but you've not shared that.

## protopoloji | 2021-12-04T17:25:37+00:00
I have 96cores


 * ABOUT        XMRig/6.16.2 gcc/5.4.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) Gold 6248R CPU @ 3.00GHz (2) 64-bit AES
                L2:48.0 MB L3:71.5 MB 48C/96T NUMA:2
 * MEMORY       28.8/503.4 GB (6%)
                PROC 1 DIMM 3: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 1 DIMM 4: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 1 DIMM 5: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 1 DIMM 6: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 1 DIMM 7: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 1 DIMM 8: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 1 DIMM 9: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 1 DIMM 10: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 3: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 4: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 5: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 6: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 7: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 8: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 9: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
                PROC 2 DIMM 10: 32 GB DDR4 @ 2666 MHz NOT AVAILABLE
 * MOTHERBOARD  HPE - ProLiant DL380 Gen10
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      rx.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled


## Spudz76 | 2021-12-04T17:43:43+00:00
Delete from `argon2-impl` line down to end of the thread definitions (`rx/keva` entry), then rerun so it autoconfigures again.

Note you will also have to remove the hanging comma off the `asm` line then to maintain valid JSON.

You must have copied that config file from some rig with 8MB of cache.

## protopoloji | 2021-12-04T18:03:06+00:00
thx but still using only 48cores  and 24gb of ram :( my total hashrate is 25000

## Spudz76 | 2021-12-04T18:24:59+00:00
48 cores is correct.  The hyperthreads don't do anything for RandomX due to shared cache path with the real-core.

EDIT: on Intels.  Ryzen fakethreads *do* help because they are wired separately to cache.

## Spudz76 | 2021-12-04T18:27:24+00:00
Also you've got the highest result if you submit a benchmark :)

https://xmrig.com/benchmark?cpu=Intel%28R%29+Xeon%28R%29+Gold+6248R+CPU+%40+3.00GHz

## Lonnegan | 2021-12-04T23:05:10+00:00
> I have 8 pyhsical cpus located. and more than 256gb of ram. Doesn't work ?

Why do you want xmrig to use all your RAM? The fewer accesses there are to the lame RAM, the faster the mining works. That's why xmrig sets your parameters so that the scratchpads fit completely into the cache of your CPUs and access to slow DRAM is not necessary. This is the way you achieve the highest hashrate!

# Action History
- Created by: protopoloji | 2021-12-04T15:54:57+00:00
- Closed at: 2025-06-20T11:08:00+00:00
