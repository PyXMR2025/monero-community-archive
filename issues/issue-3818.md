---
title: PawnIO is installed without any pop-ups or anything (Windows)
source_url: https://github.com/xmrig/xmrig/issues/3818
author: ViktorShahter
assignees: []
labels: []
created_at: '2026-05-23T19:15:44+00:00'
updated_at: '2026-07-03T19:44:22+00:00'
type: issue
status: closed
closed_at: '2026-07-03T19:44:22+00:00'
---

# Original Description
**Describe the bug**
After using XMRig on Windows 11 I noticed that PawnIO was installed (I didn't install it myself nor use any software that may depend on it). At the time, I thought that I possibly caught some malware that installed it and did a clean install of Windows 10. After running XMRig on freshly-installed OS PawnIO popped up again in app list. As it's described as replacement for WinRing0x64, now I'm pretty confident XMRig has something to do with it since it appeared after I ran XMRig.

I'm gonna check in VM soon to make sure I'm not insane.

**To Reproduce**
1. Install Windows
2. Unzip XMRig to some user-owned directory
3. (probably has nothing to do with this) Allow Locking pages in memory for Administrators through Local Security Policy
4. Run as administrator

**Expected behavior**
No additional software should be installed without explicit user consent.

**Required data**
 - XMRig version: https://github.com/xmrig/xmrig/releases/tag/v6.26.0
 - OS: Windows 10 LTSC 2021 and Windows 11 LTSC 2024

Will provide logs if necessary later, I don't think they're gonna tell much as there's no info about installation of anything.

Configuration:
```json
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
        // algo confs removed to shorten
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
    "donate-level": 3,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.hashvault.pro:443",
            "user": "...",
            "pass": "...",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": "420c7850e09b7c0bdcf748a7da9eb3647daf8515718f36d9ccfdd6b9ff834b14",
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
        "ip_version": 0,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": true,
    "pause-on-active": false
}
```

# Discussion History
## SChernykh | 2026-05-24T04:39:07+00:00
Try a fresh Windows install, unzip XMRig but delete WinRing0x64 and run XMRig without administrator privileges (so it can't physically install anything without you knowing). I can assure you there is no "PawnIO" references anywhere in XMRig's code, release binary, or WinRing0x64 itself.

## geekwilliams | 2026-05-24T04:44:44+00:00
👆👆👆 

Also make sure you're getting the binaries from this repo and not some other sketchy source.  

## ViktorShahter | 2026-05-25T13:23:09+00:00
> Also make sure you're getting the binaries from this repo and not some other sketchy source.

That's definitely not the issue, I got binaries from GH releases and verified them.

> Try a fresh Windows install, unzip XMRig but delete WinRing0x64 and run XMRig without administrator privileges

I would try but after I'll reproduce it in VM. Few hours in, so far nothing was installed.

## ViktorShahter | 2026-07-03T19:44:22+00:00
After more or less thorough testing nothing like that happened again. I guess it was some irreproducible coincidence. Sorry for inconvenience.

# Action History
- Created by: ViktorShahter | 2026-05-23T19:15:44+00:00
- Closed at: 2026-07-03T19:44:22+00:00
