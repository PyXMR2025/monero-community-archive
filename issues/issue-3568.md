---
title: http-host /summary API broke after update
source_url: https://github.com/xmrig/xmrig/issues/3568
author: snex
assignees: []
labels:
- bug
created_at: '2024-10-23T06:49:17+00:00'
updated_at: '2025-06-16T18:51:59+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:51:58+00:00'
---

# Original Description
**Describe the bug**
The JSON output from /summary is broken. Seems like it just cuts off at a random spot in the output.

**To Reproduce**
Use --http-host 127.0.0.1 and --http-port 80 cmdline options, then do
`curl http://127.0.0.1/summary`

**Expected behavior**
Fully parsable JSON output.

**Required data**
 - XMRig version 6.22.1
 - Built from source on Ubuntu Linux
 - OS: Ubuntu 24.04 LTS

**Additional context**
Here is the output I get:
```json
{
    "id": "3564a4f0bab8b8af",
    "worker_id": "xmr-miner",
    "uptime": 309,
    "restricted": true,
    "resources": {
        "memory": {
            "free": 54803238912,
            "total": 67200200704,
            "resident_set_memory": 15728640
        },
        "load_average": [127.9, 126.65, 127.2],
        "hardware_concurrency": 128
    },
    "features": ["api", "asm", "http", "hwloc", "tls", "opencl", "cuda"],
    "results": {
        "diff_current": 2501436,
        "shares_good": 4,
        "shares_total": 4,
        "avg_time": 77,
        "avg_time_ms": 77274,
        "hashes_total": 10005744,
        "best": [8064317, 5554564, 2900700, 2708982, 0, 0, 0, 0, 0, 0],
        "error_log": []
    },
    "algo": "rx/0",
    "connection": {
        "pool": "127.0.0.1:3333",
        "ip": "127.0.0.1",
        "uptime": 309,
        "uptime_ms": 309097,
        "ping": 0,
        "failures": 0,
        "tls": null,
        "tls-fingerprint": null,
        "algo": "rx/0",
        "diff": 2501436,
        "accepted": 4,
        "rejected": 0,
        "avg_time": 77,
        "avg_time_ms": 77274,
        "hashes_total": 10005744,
        "error_log": []
    },
   "version": "6.22.1",
    "kind": "miner",
    "ua": "XMRig/6.22.1 (Linux x86_64) libuv/1.48.0 gcc/13.2.0",
    "cpu": {
        "brand": "AMD Ryzen Threadripper PRO 5995WX 64-Cores",
        "family": 25,
        "model": 8,
        "stepping": 2,
        "proc_info": 10489730,
        "aes": true,
        "avx2": true,
        "x64": true,
        "64_bit": true,
        "l2": 33554432,
        "l3": 268435456,
        "cores": 64,
        "threads": 128,
        "packages": 1,
        "nodes": 1,
        "backend": "hwloc/2.10.0",
        "msr": "ryzen_19h",
        "assembly": "ryzen",
        "arch": "x86_64",
        "flags": ["aes", "vaes", "avx", "avx2", "bmi2", "osxsave", "pdpe1gb", "sse2", "ssse3", "sse4.1", "popcnt", "cat_l3"]
    },
    "donate_level": 0,
    "paused": false,
    "algorithms": ["cn/0", "cn/1", "cn/2", "cn/r", "cn/fast", "cn/half", "cn/xao", "cn/rto", "cn/rwz", "cn/zls", "cn/double", "cn/ccx", "cn-lite/0", "cn-lite/1", "cn-heavy/0", "cn-heavy/tube", "cn-heavy/xhv", "cn-pico", "cn-pico/tlo", "cn/upx2", "rx/0", "rx/wow", "rx/arq", "rx/graft", "rx/sfx", "rx/yada", "argon2/chukwa", "argon2/chukwav2", "argon2/ninja", "ghostrider"],
    "hashrate": {
        "total": [20752.26, 20775.16, null],
        "highest": 20815.11,
        "threads": [
            [323.13, 323.81,
```

Notice how it just cuts off at the end.

# Discussion History
## snex | 2024-10-23T07:00:12+00:00
Strange update.. after about 10 minutes it started working normally.

## SChernykh | 2024-10-23T08:18:31+00:00
> Strange update.. after about 10 minutes it started working normally.

It seems that it started working as soon as 15-minute hashrate filled in. I will try to fix it today.

## SChernykh | 2024-10-23T09:44:41+00:00
#3569 should fix it.

## Cyrix126 | 2024-10-25T18:16:08+00:00
I can confirm #3569 fix this issue as well as #3363 (which seems to be the same problem).
I don't think it's from this update, since it has been reported before and I can reproduce this issue with 6.21.2, 6.21.3, 6.22.0. 
6.21.1 works however, glad there is now a fix for newer version.

# Action History
- Created by: snex | 2024-10-23T06:49:17+00:00
- Closed at: 2025-06-16T18:51:58+00:00
