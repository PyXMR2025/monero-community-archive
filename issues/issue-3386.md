---
title: 'All threds fail on a Rasberry Pi 4 '
source_url: https://github.com/xmrig/xmrig/issues/3386
author: NastroukaPro
assignees: []
labels: []
created_at: '2023-12-22T19:23:02+00:00'
updated_at: '2025-06-18T22:26:30+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:26:30+00:00'
---

# Original Description
**Describe the bug**
When starting Xmrig on a Rasberry Pi 4 it tries to run the Ghostrider test but all threads fail and nothing happens.
When Ctrl + C is pressed, it shows a Segmentation fault.

**To Reproduce**
Install Xmrig from the Pi app store

**Expected behaviour**
Ghostrider test is passed successfully

**Required data**
 - OS: Rasbian Bookworm
 - For GPU-related issues: Arm64

**Output**
````
 * ABOUT        XMRig/6.19.2-mo1 gcc/12.2.0
 * LIBS         libuv/1.44.2 OpenSSL/3.0.11 hwloc/2.9.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A72 (1) 64-bit -AES
                L2:1.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.4/3.7 GB (11%)
 * DONATE       1%
 * POOL #1      pool.hashvault.pro:443 algo auto
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume, 's' results, 'c' connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-12-22 19:11:29.112]  config   configuration saved to: "/home/npro/.xmrig.json"
[2023-12-22 19:11:29.113]  benchmk   STARTING ALGO PERFORMANCE CALIBRATION (with 10 seconds round) 
[2023-12-22 19:11:29.113]  benchmk   Algo ghostrider Preparation 
[2023-12-22 19:11:29.113]  cpu      use profile  ghostrider  (4 threads) scratchpad 2048 KB
[2023-12-22 19:11:31.403]  cpu      thread #2 self-test failed
[2023-12-22 19:11:31.414]  cpu      thread #1 self-test failed
[2023-12-22 19:11:31.437]  cpu      thread #0 self-test failed
[2023-12-22 19:11:31.438]  cpu      thread #3 self-test failed
[2023-12-22 19:11:31.438]  cpu      disabled (failed to start threads)
[2023-12-22 19:12:29.147]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s avg n/a H/s
[2023-12-22 19:13:29.185]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s avg n/a H/s
[2023-12-22 19:14:14.751]  signal   Ctrl+C received, exiting
Segmentation fault
```


**Json config**




```

{
    "http": {
        "enabled": true,
        "host": "0.0.0.0",
        "port": 62448,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "pool.hashvault.pro:443",
            "user": "(Wallet was here)",
            "pass": "npro-rpi",
            "keepalive": true,
            "tls": true
        }
    ]
}
```


# Discussion History
## SChernykh | 2023-12-22T20:01:14+00:00
This is MoneroOcean version, report this bug to them. If you can reproduce this bug using the original XMRig, please edit your post.

## NastroukaPro | 2023-12-22T20:03:31+00:00
Ok thanks


## AxolDad | 2024-03-29T23:48:25+00:00
Having the same issue.


# Action History
- Created by: NastroukaPro | 2023-12-22T19:23:02+00:00
- Closed at: 2025-06-18T22:26:30+00:00
