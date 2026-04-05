---
title: Opencl enabled, but (no suitable configuration found)
source_url: https://github.com/xmrig/xmrig/issues/2301
author: urimm
assignees: []
labels: []
created_at: '2021-04-23T00:23:24+00:00'
updated_at: '2024-04-05T18:28:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello,

Here is some issues with current version of Xmrig:
1. I have enabled the Opencl in config.json , but it wont enabling, until I write "--opencl" in "start.cmd" file
Here is the config.json config: 
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
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true,
        "cn/0": true,
        "cn-lite/0": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true,
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "donate.v2.xmrig.com:3333",
            "user": "YOUR_WALLET_ADDRESS",
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

2. But even if I write in "start.cmd" the "--opencl"  and my GPU's were recognized - it still disabling Opencl during the work process, with "no suitable configuration found"

Dont quite understand, why it dont load the configurationg of Opencl from config.json Maybe its just compatibility issue with my GPU's, if so, please add support of ATI HD 5970, HD 6990, HD 6970.

Thanks in advance.

![01](https://user-images.githubusercontent.com/83045219/115800357-1d55d480-a3e3-11eb-9c90-6ae6d35c4b35.jpg)

# Discussion History
## DeeDeeRanged | 2021-04-25T10:22:35+00:00
Your GPU's are probably to old. They even date before GCN1.0 probably need an AMD GPU from GCN 3.0 and upwards with at least 4GB upwards. If you want to seriously mine with a GPU you need 8GB+ vram.

## Spudz76 | 2021-04-25T13:07:23+00:00
Any driver newer than [this 15.11.1-beta one](https://www.amd.com/en/support/kb/release-notes/rn-rad-win-15-11-1-beta) will not work correctly for TeraScale or some GCN1.  DDU strip your system and install no newer than that driver.

## DeeDeeRanged | 2021-04-26T22:31:47+00:00
I must have been sleeping didn't notice he was using windows.

## ghost | 2024-04-05T18:27:58+00:00
Im getting this on 7900xtx windows. Is it too old? Basically driver issue? is xmrig using opencl for rocm?

# Action History
- Created by: urimm | 2021-04-23T00:23:24+00:00
