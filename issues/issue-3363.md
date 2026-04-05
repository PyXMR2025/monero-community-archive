---
title: the API syntax is corrupted.
source_url: https://github.com/xmrig/xmrig/issues/3363
author: remusss1
assignees: []
labels:
- bug
created_at: '2023-11-20T13:41:29+00:00'
updated_at: '2025-06-16T19:15:29+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:15:28+00:00'
---

# Original Description
Hi, I am collecting from the xmrig source codes and faced with the problem of the corrupted syntax of the JSON API response (half of the json data is missing).
The assembly is going fine. I do not make any changes to the source code...

**How to reproduce the error:**
1. Run xmrig (it works fine).
2. Follow the link http://127.0.0.1:2030/1/summary - the page opens normally, the response is complete, the json is not broken.
3. I refresh the page and get a corrupted JSON response.

`{
    "id": "x",
    "worker_id": "x",
    "uptime": 4,
    "restricted": true,
    "resources": {
        "memory": {
            "free": 8300163072,
            "total": 17046507520,
            "resident_set_memory": 2469908480
        },
        "load_average": [0.0, 0.0, 0.0],
        "hardware_concurrency": 8
    },
    "features": ["api", "asm", "http", "hwloc", "tls", "opencl", "cuda"],
    "results": {
        "diff_current": 1357019,
        "shares_good": 0,
        "shares_total": 0,
        "avg_time": 0,
        "avg_time_ms": 0,
        "hashes_total": 0,
        "best": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "error_log": []
    },
    "algo": "rx/0",
    "connection": {
        "pool": "x",
        "ip": "x",
        "uptime": 4,
        "uptime_ms": 4587,
        "ping": 0,
        "failures": 0,
        "tls": null,
        "tls-fingerprint": null,
        "algo": "rx/0",
        "diff": 1357019,
        "accepted": 0,
        "rejected": 0,
        "avg_time": 0,
        "avg_time_ms": 0,
        "hashes_total": 0,
        "error_log": []
    },
    "version": "6.20.0",
    "kind": "x",
    "ua": "x/6.20.0 (Windows NT 10.0; Win64; x64) libuv/1.44.2 gcc/13.2.0",
    "cpu": {
        "brand": "Intel(R) Core(TM) i3-10105F CPU @ 3.70GHz",
        "family": 6,
        "model": 165,
        "stepping": 3,
        "proc_info": 656979,
        "aes": true,
        "avx2": true,
        "x64": true,
        "64_bit": true,
        "l2": 1048576,
        "l3": 6291456,
        "cores": 4,
        "threads": 8,
        "packages": 1,
        "nodes": 1,
        "backend": "hwloc/2.9.0",
        "msr": "intel",
        "assembly": "intel",
        "arch": "x86_64",
        "flags": ["aes", "avx", "avx2", "bmi2", "osxsave", "pdpe1gb", "sse2", "ssse3", "sse4.1", "popcnt", "vm"]
    },
    "donate_level": 1,
    "paused": false,
    "algorithms": ["cn/1", "cn/2", "cn/r", "cn/fast", "cn/half", "cn/xao", "cn/rto", "cn/rwz", "cn/zls", "cn/double", "cn/ccx", "cn-lite/1", "cn-heavy/0", "cn-heavy/tube", "cn-heavy/xhv", "cn-pico", "cn-pico/tlo", "cn/upx2", "rx/0", "rx/wow", "rx/arq", "rx/graft", "rx/sfx", "rx/keva", "argon2/chukwa", "argon2/chukwav2", "argon2/ninja", "ghostrider"],
    "hashrate": {
        "total": [null, null, null],
        "highest": null,
        "threads": [
            [`


# Discussion History
## SChernykh | 2023-11-20T14:39:51+00:00
I can't reproduce this. Which XMRig version do you run, which OS and browser do you use?

## remusss1 | 2023-11-20T14:44:11+00:00
xmrig 6.20.0
OS:  win 11 23h2 22631.2715
Microsoft Edge Версия 119.0.2151.72 

## remusss1 | 2023-11-20T14:49:58+00:00
here, the same problem, but I didn't understand how the author solved it...
https://github.com/xmrig/xmrig/issues/290

## SChernykh | 2023-11-20T14:53:29+00:00
You can try to use `xmrig-6.20.0-gcc-win64.zip` instead of `xmrig-6.20.0-msvc-win64.zip` (or vice versa) - maybe one of them will work.

## remusss1 | 2023-11-21T17:54:19+00:00
collected through VS 2022, everything is ok.

## rngnrs | 2024-02-23T10:01:28+00:00
Same issue with Alpine advanced build ([instruction](https://xmrig.com/docs/miner/build/alpine)), v6.21.0, gcc/13.2.1.
Issue is reproduced after connecting to a pool.
Config:
```
    ...
    "http": {
        "enabled": true,
        "host": "0.0.0.0",
        "port": 2030,
        "access-token": null,
        "restricted": true
    },
    ...
```
Response:
```
    ...
    "hashrate": {
        "total": [1276.23, null, null],
        "highest": 1278.05,
        "threads": [
            [322.6, 
```

I'm trying to use API with https://workers.xmrig.info/. This issue prevents updating the info - it corrupts JSON output at start/reload and following 15 minutes after.

## Cyrix126 | 2024-03-26T15:10:12+00:00
encountered exactly the same issue with 6.21.2 but not on 6.21.1 or 6.21.0
Using [reqwest](https://github.com/seanmonstar/reqwest) 0.12.2.

## Cyrix126 | 2024-04-15T03:19:21+00:00
It is also preventing to send benchmarks that completes before 15mn.
An error will occur at then end of the benchmark:
"Json unexpected end of file"

## hanai | 2024-04-25T04:55:39+00:00
> It is also preventing to send benchmarks that completes before 15mn. An error will occur at then end of the benchmark: "Json unexpected end of file"

same issue

## RobQuistNL | 2024-05-16T12:20:58+00:00
Same here, this looks very similar: https://github.com/xmrig/xmrig/pull/3407

Posted my output there too.

## stringhandler | 2024-07-29T11:32:35+00:00
Still receiving this on xmrig 6.21.3 

![image](https://github.com/user-attachments/assets/df8021f5-368f-48ee-983d-00362f33a767)



## SChernykh | 2024-07-29T15:15:25+00:00
Possible fix in #3518

## Cyrix126 | 2024-08-29T13:48:58+00:00
> Possible fix in #3518

The issue is still there with 22.0
```
    "hashrate": {
        "total": [null, null, null],
        "highest": null,
        "threads": [
            [% 
```

# Action History
- Created by: remusss1 | 2023-11-20T13:41:29+00:00
- Closed at: 2025-06-16T19:15:28+00:00
