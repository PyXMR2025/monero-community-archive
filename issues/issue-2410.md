---
title: Pause-on-active option doesn't pause
source_url: https://github.com/xmrig/xmrig/issues/2410
author: nelsonblaha
assignees: []
labels: []
created_at: '2021-05-26T02:54:10+00:00'
updated_at: '2021-05-26T13:10:37+00:00'
type: issue
status: closed
closed_at: '2021-05-26T13:10:37+00:00'
---

# Original Description
**Describe the bug**
Pause-on-active doesn't pause

**To Reproduce**
Run 16.12.1 on ubuntu 18.04 with pause-on-active set in config.json and via command line with `./xmrig --pause-on-active 300`

**Expected behavior**
xmrig will pause when mouse is moved

**Required data**
 - Miner log as text or screenshot
 ```$ ./xmrig --pause-on-active 300
 * ABOUT        XMRig/6.12.1 gcc/9.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz (1) 64-bit AES
                L2:1.5 MB L3:12.0 MB 6C/12T NUMA:1
 * MEMORY       30.7/31.4 GB (98%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      miners.dero.network:3333 coin dero
 * COMMANDS     hashrate, pause, resume, results, connection
[2021-05-25 21:52:55.870]  net      use pool miners.dero.network:3333  52.136.112.140
[2021-05-25 21:52:55.870]  net      new job from miners.dero.network:3333 diff 7500 algo astrobwt height 5826621
[2021-05-25 21:52:55.870]  cpu      use profile  astrobwt  (12 threads) scratchpad 20480 KB
[2021-05-25 21:52:55.967]  cpu      READY threads 12/12 (12) huge pages 0% 0/120 memory 245760 KB (97 ms)
[2021-05-25 21:53:00.729]  net      new job from miners.dero.network:3333 diff 7500 algo astrobwt height 5826622
[2021-05-25 21:53:24.936]  signal   Ctrl+C received, exiting
[2021-05-25 21:53:24.953]  cpu      stopped (17 ms)
```
 - Config file or command line (without wallets)
 ```
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
    // "cuda": {
    //   "enabled": true
    // },
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
        "argon2": [0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11],
        "argon2": [0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11],
        "astrobwt": [0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 6],
            [1, 1],
            [1, 7],
            [1, 2],
            [1, 8],
            [1, 3],
            [1, 9],
            [1, 4],
            [1, 10],
            [1, 5],
            [1, 11]
        ],
        "cn-pico": [
            [2, 0],
            [2, 6],
            [2, 1],
            [2, 7],
            [2, 2],
            [2, 8],
            [2, 3],
            [2, 9],
            [2, 4],
            [2, 10],
            [2, 5],
            [2, 11]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 6],
            [2, 1],
            [2, 7],
            [2, 2],
            [2, 8],
            [2, 3],
            [2, 9],
            [2, 4],
            [2, 10],
            [2, 5],
            [2, 11]
        ],
        "rx": [0, 1, 2, 3, 4, 5],
        "rx/wow": [0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
                    {
                    "algo": "astrobwt",
                    "coin": "dero",
                    "url": "miners.dero.network:3333",
                    "user": "redacted",
                    "rig_id": null,
                    "pass": "",
                    "nicehash": false,
                    "tls": false, /* Set to true if you are using an SSL port */
                    "tls-fingerprint": null,
                    },
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
    "pause-on-active": true
}
```
 - OS: Ubuntu 18.04
 
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2021-05-26T05:43:05+00:00
That option doesn't work on Linux (yet)  See also #2222 

## nelsonblaha | 2021-05-26T13:10:37+00:00
Nice, missed that, thanks

# Action History
- Created by: nelsonblaha | 2021-05-26T02:54:10+00:00
- Closed at: 2021-05-26T13:10:37+00:00
