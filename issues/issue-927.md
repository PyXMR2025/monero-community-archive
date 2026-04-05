---
title: Masari  cryptonight fast v2 AMD Threadripper
source_url: https://github.com/xmrig/xmrig/issues/927
author: IceFloe
assignees: []
labels:
- NUMA
created_at: '2019-02-07T04:04:24+00:00'
updated_at: '2019-08-02T12:40:09+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:40:09+00:00'
---

# Original Description
Hi all, any idea why with my Threadripper 2950X I can use only 8 threads and 16384 KB memory for Masari cryptonight fast v2? 

If I add more threads it is become unstable and produces less hashes.

 * ABOUT        XMRig/2.10.0 MSVC/2017
 * LIBS         libuv/1.24.1 OpenSSL/1.1.1a microhttpd/0.9.61
 * HUGE PAGES   available
 * CPU          AMD Ryzen Threadripper 2950X 16-Core Processor  (1) x64 AES
 * CPU L2/L3    8.0 MB/32.0 MB
 * THREADS      8, cryptonight, donate=1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      pool.masari.hashvault.pro:3333 variant msr
 * COMMANDS     hashrate, pause, resume
[2019-02-07 05:59:21] use pool pool.masari.hashvault.pro:3333  54.38.153.120
[2019-02-07 05:59:21] new job from pool.masari.hashvault.pro:3333 diff 30000 algo cn/half
[2019-02-07 05:59:21] READY (CPU) threads 8(8) huge pages 8/8 100% memory 16384 KB

```json
{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "asm": true,
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": 5,
    "donate-level": 1,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 100,
    "pools": [
        {
            "url": "****",
            "user": "***",
            "pass": "Desktop",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": "msr",
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        },
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true
        }
    ],
    "user-agent": null,
    "watch": false
}
```

# Discussion History
## IceFloe | 2019-02-07T16:16:02+00:00
@xmrig Are you here guys, can you help with some advice?


## xmrig | 2019-02-08T10:01:59+00:00
If autoconfig give you only 8 threads, it looks like bug, otherwise you can change threads count by hand, add 8 extra threads record, or simply use `"threads": 16,`.
Thank you.

## IceFloe | 2019-02-08T10:28:25+00:00
Thanks for response, autoconfig gives me 16 threads but they are not working properly, cpu produces less hashes for 16 than for 8. Looks like some memory issues. What do you think?

## IceFloe | 2019-02-08T17:16:15+00:00
@xmrig just wanna let you know there is a bug in my config or in your code, with jce miner I got 2500-2600 h/s will wait for xmr-stak to compare also, thx 

## ShaddyR | 2019-03-14T11:38:47+00:00
@IceFloe: advice - using "affine_to_cpu" option will increase HR


## IceFloe | 2019-03-14T11:48:27+00:00
Thx, it will increase to normal 2600?

## xmrig | 2019-07-29T02:14:55+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: IceFloe | 2019-02-07T04:04:24+00:00
- Closed at: 2019-08-02T12:40:09+00:00
