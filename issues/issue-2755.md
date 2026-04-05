---
title: End of file
source_url: https://github.com/xmrig/xmrig/issues/2755
author: TimyIsCool
assignees: []
labels: []
created_at: '2021-11-29T22:35:13+00:00'
updated_at: '2023-09-26T09:09:43+00:00'
type: issue
status: closed
closed_at: '2021-11-30T19:21:49+00:00'
---

# Original Description
**Describe the bug**
I get a end of file error when running the miner

**To Reproduce**
Steps to reproduce the behavior.
enter eu.flockpool.com:5555 in the config file
**Expected behavior**
Regular mining
**Required data**
![image](https://user-images.githubusercontent.com/74112751/143953487-b169359d-5e9f-4d90-b7b3-72f597234f25.png)
Windows 10, Latest miner

**Additional context**



# Discussion History
## Lonnegan | 2021-11-29T22:58:49+00:00
Can you post the whole config file, pls? Most of the time it is a missing comma or missing quotes or something like that in the json file.

## Spudz76 | 2021-11-29T23:43:25+00:00
That's a network end-of-file (more like end-of-stream)...

Probably being blocked try whitelisting.  Lots of things are blocking known pool sites lately.

## SChernykh | 2021-11-30T00:20:46+00:00
5555 is an SSL (TLS) port there, make sure you enable TLS in xmrig's config.

## TimyIsCool | 2021-11-30T16:17:54+00:00
> That's a network end-of-file (more like end-of-stream)...
> 
> Probably being blocked try whitelisting. Lots of things are blocking known pool sites lately.

how would i whitelist?

## TimyIsCool | 2021-11-30T16:19:38+00:00
> Can you post the whole config file, pls? Most of the time it is a missing comma or missing quotes or something like that in the json file.

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
        "argon2": [0, 1, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 1]
        ],
        "cn-heavy": [
            [1, 0]
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
            [8, 1]
        ],
        "rx": [0, 1],
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
        "adl": true,
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
            "algo": "ghostrider",
            "coin": null,
            "url": "stratum+tcps://eu.flockpool.com:5555",
            "user": "RUSMnMdWTKDcZNTHLaeoBVDrS8YsA6Afw2.CPU1",
            "pass": "[redacted]",
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

```

## Spudz76 | 2021-11-30T16:20:40+00:00
remove `stratum+tcps://`

set tls:true

## TimyIsCool | 2021-11-30T16:24:57+00:00
> remove `stratum+tcps://`
> 
> set tls:true

thank you, okay how would i set a cpu thread limit?

## Spudz76 | 2021-11-30T16:31:21+00:00
You're already limited since
```
        "ghostrider": [
            [8, 0],
            [8, 1]
        ],
```
that is two threads.

If you want less, remove one of those entries.

## TimyIsCool | 2021-11-30T16:41:19+00:00
> 

so just add
[8, 3] etc

## Spudz76 | 2021-11-30T17:07:20+00:00
Adding threads is the opposite of limiting.

The autoconfigurator already set the max workable threads, adding more would just hurt speed.

## TimyIsCool | 2021-11-30T19:21:31+00:00
> Adding threads is the opposite of limiting.
> 
> The autoconfigurator already set the max workable threads, adding more would just hurt speed.

The utoconfigurator doesnt have rtm as a option yet, I set it manually 

## TimyIsCool | 2021-11-30T19:21:49+00:00
Thanks for all the help guys

## Spudz76 | 2021-11-30T19:26:50+00:00
I meant the autoconfig that the app itself does, where it generated you those two threads.

## TimyIsCool | 2021-11-30T21:00:54+00:00
> I meant the autoconfig that the app itself does, where it generated you those two threads.

oh okay

## thom58 | 2023-09-25T06:56:14+00:00
can someone help it says "end of file" when i run the miner 


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
        "argon2": [0, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
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
            [8, 2]
        ],
        "rx": [0, 2],
        "rx/arq": [0, 1, 2, 3],
        "rx/wow": [0, 2, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
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
    "donate-level": 0,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "ghostrider",
            "coin": null,
            "url": "usa-east.raptoreumzone.com:3333",
            "user": "RQkhLTsTAxYdFpeo1ZuRtdf6PjBrwZcEMw",
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

## geekwilliams | 2023-09-25T08:45:38+00:00
Your config works for me. Are you running 6.20 with admin rights? Sometimes the miner gets hung up and you have to restart it, or it could be something with your ISP

## thom58 | 2023-09-26T09:09:43+00:00
> Your config works for me. Are you running 6.20 with admin rights? Sometimes the miner gets hung up and you have to restart it, or it could be something with your ISP

ya, I figured it out it was of the pool. it didn't work at that time. but tanks

# Action History
- Created by: TimyIsCool | 2021-11-29T22:35:13+00:00
- Closed at: 2021-11-30T19:21:49+00:00
