---
title: Segmentation fault (core dumped)
source_url: https://github.com/xmrig/xmrig/issues/3299
author: Pol-Ruiz-3llideas
assignees: []
labels: []
created_at: '2023-07-13T09:19:07+00:00'
updated_at: '2025-06-18T22:46:37+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:46:37+00:00'
---

# Original Description
**Describe the bug**
I am trying to run the xmring program on a synology nas, which I think its operating system is freebsd, and I get the following error "Segmentation fault (core dumped)" I have put a more permissions to run, I have also tried to start it with sudo but I get the same error, I have also restarted several times the nas, but still does not work.

any help will be welcome

**To Reproduce**
try running xmring "xmrig-6.20.0-freebsd-static-x64.tar.gz" on a synology nas or freebsd operating system

**Expected behavior**
I was waiting for the xmrig application to work and start mining.

**Required data**
 - Miner log as text or screenshot: no log because the application has not been run yet
 - Config file or command line (without wallets)
 `ash-4.4# cat config.json
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
        "huge-pages": false,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "max-threads-hint": 100,
        "asm": true,
        "argon2-impl": null,
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": true,
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
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.supportxmr.com:3333",
            "user": "484gtMornmcfTsHKTCzTMp3dRYmp9vU39Z2VW3gVeg5m2K8Wrqdasav6cBYUzdLVGra2ACGwA3zkt7LVCK5wTwGsT9iBebB",
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

        "max-threads-hint": 100,
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
    "dns": {
        "ipv6": false,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}`
 - OS: freebsd (Synology DiskStation Manager (DSM))
 - For GPU related issues: no graphics card

**Additional context**
I don't know if it's really freebsd based or not, but I think it's the program that best suits the sysnology operating system if I'm not running the correct application for the synology operating system, could you tell me which version of the download repository I should download?

# Discussion History
## koitsu | 2023-07-17T02:02:49+00:00
Multiple things:

1. Synology NAS products use Linux,
2. You didn't state the exact model number of your NAS which makes it hard to tell you what CPU architecture to get,
3. You tried to actually execute/run a compressed tarball (re: "try running xmring "xmrig-6.20.0-freebsd-static-x64.tar.gz" on a synology nas or freebsd operating system"), which is not how this works.  You need to unpack the tgzball and use the executable it provides using something like `tar -zxvf xmrig-6.20.0-freebsd-static-x64.tar.gz" and then look at the contents.  The executable is called "xmrig".

# Action History
- Created by: Pol-Ruiz-3llideas | 2023-07-13T09:19:07+00:00
- Closed at: 2025-06-18T22:46:37+00:00
