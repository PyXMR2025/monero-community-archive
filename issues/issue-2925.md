---
title: '"bus error" when attempting to mine Uplexa (cn/upx2) with 128kb scratchpad
  on ARMv7 device '
source_url: https://github.com/xmrig/xmrig/issues/2925
author: hilga007
assignees: []
labels:
- bug
- duplicate
- arm
created_at: '2022-02-07T09:08:30+00:00'
updated_at: '2022-06-27T19:49:16+00:00'
type: issue
status: closed
closed_at: '2022-06-27T19:49:16+00:00'
---

# Original Description
**Describe the bug**
There is a "bus error" when attempting to mine Uplexa (xn/upx2) with 128kb scratchpad on ARMv7 device 

**To Reproduce**
Compile and install latest hwloc, libuv and libressl from their respective git. Compile xmrig 

**Expected behavior**
Expected behavior, even with this diminutive of a device, is for it mine Uplexa given the low RAM requirements and 128kb scratchpad. 

**Required data**

Config.json: 

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
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [0, 1, 2, 3],
        "cn-heavy": [0, 1, 2, 3],
        "cn-lite": [0, 1, 2, 3],
        "cn-pico": [0, 1, 2, 3],
        "cn/upx2": [0, 1, 2, 3],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3]
        ],
        "rx": [0, 1, 2, 3],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "cn/upx2",
            "coin": null,
            "url": "us.uplexa.herominers.com:1177",
            "user": "_hidden_",
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
    "health-print-time": 60,
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

I cannot get the actual log file contents, even though I have syslog set to "true" in  the config file so here is the error. 

 * ABOUT        XMRig/6.16.4 gcc/11.2.0
 * LIBS         libuv/1.43.0 LibreSSL/3.5.0 hwloc/2.8.0a1-git
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A7 (1) 32-bit -AES
                L2:0.0 MB L3:0.0 MB 4C/4T NUMA:1
 * MEMORY       0.2/0.9 GB (20%)
 * DONATE       1%
 * POOL #1      us.uplexa.herominers.com:1177 algo cn/upx2
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2022-02-07 00:53:13.621]  net      use pool us.uplexa.herominers.com:1177  116.202.226.168
[2022-02-07 00:53:13.622]  net      new job from us.uplexa.herominers.com:1177 diff 100001 algo cn/upx2 height 892561 (1 tx)
[2022-02-07 00:53:13.622]  cpu      use profile  cn/upx2  (4 threads) scratchpad 128 KB
Bus error






**Additional context**
Add any other context about the problem here.


# Discussion History
## Spudz76 | 2022-02-07T20:16:54+00:00
Suspecting this is due to alignment, but that's only a hunch.

## hilga007 | 2022-02-09T02:56:48+00:00
> Suspecting this is due to alignment, but that's only a hunch.

I better call myself a chiropractor and get in for an alignment then!

## Spudz76 | 2022-02-09T09:52:13+00:00
Awaiting real developer, I don't know the specifics well enough.

## hilga007 | 2022-02-10T05:03:50+00:00
> Awaiting real developer, I don't know the specifics well enough.

Agreed. I'm not a developer. I'm a nerd who has decided to dive straight into playing around with things. Whoops. 

I also don't know why it won't actually generate a log, which would be nice for helping to provide some more info 


## whitlocj1 | 2022-02-19T21:49:50+00:00
See my comment to #2926 

## benthetechguy | 2022-05-21T02:06:32+00:00
Duplicate of #2895 (and #2926)

## benthetechguy | 2022-06-27T19:19:54+00:00
Fixed in latest release. Can @xmrig @SChernykh please close this?

# Action History
- Created by: hilga007 | 2022-02-07T09:08:30+00:00
- Closed at: 2022-06-27T19:49:16+00:00
