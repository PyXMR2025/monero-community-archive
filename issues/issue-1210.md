---
title: '[4.2.0-beta]  ocl  disabled (no suitable configuration found)'
source_url: https://github.com/xmrig/xmrig/issues/1210
author: LeChatNoir69
assignees: []
labels: []
created_at: '2019-09-30T20:23:54+00:00'
updated_at: '2019-10-08T03:07:33+00:00'
type: issue
status: closed
closed_at: '2019-10-08T03:07:33+00:00'
---

# Original Description
Hi,
Preparing next release of CryptoMac, I try to embed XMRig 4.2. CPU options are ok and I try to enable gnu ones.

I can't figure out how to configure gpu options. Still have this message :
 ocl  disabled (no suitable configuration found)

Maybe you can help ? I can't find lot of documentation around theses conf :(

Here is the log :

` * ABOUT        XMRig/4.2.0-beta clang/10.0.0
 * LIBS         libuv/1.26.0 hwloc/2.0.4
 * CPU          Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz (1) x64 AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * DONATE       4%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10001 algo auto
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume
 * HTTP API     127.0.0.1:40096 
[2019-09-30 22:06:02.721] configuration saved to: "/Users/lechat/Documents/minerConf.json"
 * OPENCL       #0 Apple/OpenCL 1.2 (Aug 20 2018 18:58:21)
 * OPENCL GPU   #0 n/a Iris Pro 1200MHz cu:40 mem:384/1536 MB
[2019-09-30 22:06:02.781] use pool gulf.moneroocean.stream:10001  95.179.220.100
[2019-09-30 22:06:02.781] new job from gulf.moneroocean.stream:10001 diff 1000 algo cn/r height 1934610
[2019-09-30 22:06:02.781]  cpu  use profile  cn  (3 threads) scratchpad 2048 KB
[2019-09-30 22:06:02.781]  ocl  disabled (no suitable configuration found)
[2019-09-30 22:06:03.231] "/Users/lechat/Documents/minerConf.json" was changed, reloading configuration
[2019-09-30 22:06:03.984]  ocl  disabled (no suitable configuration found)
[2019-09-30 22:06:04.663]  cpu  READY threads 3/3 (3) huge pages 0/3 0% memory 6144 KB (1883 ms)
[2019-09-30 22:06:04.844] accepted (1/0) diff 1000 (40 ms)
...`

Here is the config file :
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "127.0.0.1",
        "port": 40096,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "version": 1,
    "background": false,
    "colors": false,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4]
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
            [1, 3]
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
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx": [0, 2, 4],
        "rx/wow": [0, 2, 4, 6, 1, 3],
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": 0,
        "cn-pico": [
            {
                "index": 0,
                "intensity": 640,
                "worksize": 8,
                "strided_index": [0, 2],
                "threads": [-1],
                "unroll": 8
            }
        ],
        "cn/gpu": [
            {
                "index": 0,
                "intensity": 0,
                "worksize": 8,
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
                "dataset_host": true
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "intensity": 640,
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
    "donate-level": 4,
    "donate-over-proxy": 1,
    "log-file": "",
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10001",
            "user": "4443fX2feNtcjcbSX12cMNCrUXbNTzBuRSfseeAxyaKf59AdkihRmvnPptvPgxiWXYVqbi4gkXn7nddmbMpVzXiWGFAFM3t",
            "pass": "MBP",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
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
```

# Discussion History
## xmrig | 2019-09-30T21:49:23+00:00
Intel OpenCL implementation useless and broken, don't use it, but autoconfig should create profile `"cn/2"` for cn/r algorithm and this profile missing in your config, also missing `cn`, `cn-lite`, `cn-heavy`.
Thank you.

# Action History
- Created by: LeChatNoir69 | 2019-09-30T20:23:54+00:00
- Closed at: 2019-10-08T03:07:33+00:00
