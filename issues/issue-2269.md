---
title: FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
source_url: https://github.com/xmrig/xmrig/issues/2269
author: cluelessbob
assignees: []
labels: []
created_at: '2021-04-15T15:44:18+00:00'
updated_at: '2021-06-26T18:06:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I start xmrig in windows 10 using admin privileges and it does not apply the MSR mod. I've tried starting it from a cmd window started with admin privileges but I get the same error. This error doesn't happen when I run it in ubuntu.

**To Reproduce**
Right click, run as administrator

**Expected behavior**
MSR mod applied, hasrate will not be low

**Required data**
cannot set MSR 0xc0011020 to 0x0004480000000000
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

    "pools": [
        {
            "algo": "rx/o",
            "coin": "monero",
            "url": "xmrvsbeast.com:4242",
            "user": "",
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

**Additional context**
Xmrig go brrrr

# Discussion History
## SChernykh | 2021-04-15T15:47:08+00:00
Check if you have Secure Boot disabled in BIOS. Also if you have docker installed it can conflict with MSR mod.

## cluelessbob | 2021-04-15T17:35:22+00:00
> Check if you have Secure Boot disabled in BIOS. Also if you have docker installed it can conflict with MSR mod.

Docker is not installed and secure boot is disabled but issue persists.

## Sub-Cool | 2021-06-26T18:06:26+00:00
I have the same issue, and I also don't have docker installed and secure boot is disabled. Does anyone know what to do?

# Action History
- Created by: cluelessbob | 2021-04-15T15:44:18+00:00
