---
title: cant mine with openCL returns with error
source_url: https://github.com/xmrig/xmrig/issues/3186
author: unnaturalistic
assignees: []
labels: []
created_at: '2022-12-27T12:04:28+00:00'
updated_at: '2025-06-20T11:05:16+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:05:16+00:00'
---

# Original Description
**Describe the bug**
when using xmrig and set opencl to true in config.json and started the miner, met with this error:

> [2022-12-27 15:29:48.369]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 941938688
[2022-12-27 15:29:48.370]  opencl   thread #0 failed with error CL_INVALID_BUFFER_SIZE
[2022-12-27 15:29:48.382]  opencl   error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 941938688
[2022-12-27 15:29:48.383]  opencl   thread #1 failed with error CL_INVALID_BUFFER_SIZE
[2022-12-27 15:29:48.386]  cpu      READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (45 ms)
[2022-12-27 15:29:48.391]  opencl   thread #0 self-test failed
[2022-12-27 15:29:48.404]  opencl   thread #1 self-test failed
[2022-12-27 15:29:48.405]  opencl   disabled (failed to start threads)

**To Reproduce**
no description

**Expected behavior**
when set the opencl option in config.json expected to run as normal and mine with GPU

**Required data**
 - Miner log as text or screenshot
 - config file : 

> {
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "0.0.0.0",
        "port": 8080,
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
        "argon2": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2]
        ],
        "rx": [0, 1, 2, 3],
        "rx/wow": [0, 1, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": false,
        "loader": null,
        "platform": "AMD",
        "adl": false,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
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
            "url": "xmr.2miners.com:2222",
            "user": "wallet",
            "pass": "x",
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

 - OS: windows 10
 - gpu: AMD Radeon HD 5450

**Additional context**
no additional context


# Discussion History
## SChernykh | 2022-12-27T14:42:41+00:00
> AMD Radeon HD 5450

This GPU has only 512 MB RAM and you're trying to allocate almost 2 GB for OpenCL. Check your config.

## unnaturalistic | 2022-12-27T15:05:54+00:00
No it has 2gb of ram
And i checked my config there was no problem
I guess this gpu doesn't support the buffer size that xmrig is trying to use....?

## SChernykh | 2022-12-27T17:50:14+00:00
```
"opencl": {
"enabled": true,
"cache": false,
"loader": null,
"platform": "AMD",
"adl": false,
"cn-lite/0": false,
"cn/0": false
},
```
The config you posted doesn't show what xmrig generated for rx/0. You should reduce intensity there, make it 2 times smaller. Also, even if you make it work somehow, it will barely do 1 h/s on RandomX.

## Spudz76 | 2022-12-27T18:59:27+00:00
Antique GPUs based on the "tree" chips (Evergreen, Cedar, etc) must use antique 15.x drivers or they don't work.

# Action History
- Created by: unnaturalistic | 2022-12-27T12:04:28+00:00
- Closed at: 2025-06-20T11:05:16+00:00
