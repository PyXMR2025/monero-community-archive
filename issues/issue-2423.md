---
title: Possible to reduce number of cores being used and/or core or thread % usage?
source_url: https://github.com/xmrig/xmrig/issues/2423
author: ScotterMonk
assignees: []
labels: []
created_at: '2021-06-03T15:03:33+00:00'
updated_at: '2025-06-20T11:11:54+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:11:54+00:00'
---

# Original Description
Hi. Is there a parameter in the config file or available via command line to reduce CPU and GPU usage down some from 100%? I want to use my computer for other stuff while mining. Also, the default 100% causes more heat and noise than is practical for my situation. AMD 5800X w/Windows 64. 

Please note the "rx" param I added to the "cpu" section below but it is not making a difference. All 8 cores and 16 threads are being used.

Help?

Here's the config file I'm using:

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
        "max-threads-hint": 100,
		"rx": [1, 2, 3, 4],
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 5,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "wownero.xyz:4555",
            "user": "Wo4oviDdn4Tbf6Hhb93KW7hTcLoMMfFDkJSfb2HvzfKNTtBJABcv8fe8upuUznfg2W8kFQgTP6A3ueQMwSNobPJ51NCmq5qD5",
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
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "retries": 5,
    "retry-pause": 5,
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
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}


# Discussion History
## ghost | 2021-06-03T19:09:35+00:00
Yes you need make first run and then reopen config.json and look for something like this at CPU column 
"argon2": [0, 1, 2, 3],
"astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
 
Then you can adjust how many threads you want to use .

I saw you at your rx  but
It's supposed to be "rx/wow": [0, 1, 2, 3],

This is your config.json for 8 thread

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
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,                                                                                                                                "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-heavy": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite": [0, 1, 2, 3, 4, 5, 6, 7],                                                                                                                   "cn-pico": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/upx2": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/wow",
            "coin": null,
            "url": "wownero.xyz:4555",
            "user": "Wo4oviDdn4Tbf6Hhb93KW7hTcLoMMfFDkJSfb2HvzfKNTtBJABcv8fe8upuUznfg2W8kFQgTP6A3ueQMwSNobPJ51NCmq5qD5",
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

## ScotterMonk | 2021-06-03T20:04:31+00:00
YES! 
It worked. 
Thank you!

## Fleettelematicssystem | 2021-06-07T22:25:49+00:00
will this change in real time, or will you open xmrig.exe again?

## Spudz76 | 2021-06-08T00:29:54+00:00
It reloads on file change while running.

# Action History
- Created by: ScotterMonk | 2021-06-03T15:03:33+00:00
- Closed at: 2025-06-20T11:11:54+00:00
