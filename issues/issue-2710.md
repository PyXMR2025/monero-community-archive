---
title: 'gulf.moneroocean.stream:10128 - connect error: "operation canceled"'
source_url: https://github.com/xmrig/xmrig/issues/2710
author: maikiro
assignees: []
labels: []
created_at: '2021-11-21T22:40:41+00:00'
updated_at: '2022-07-15T11:28:07+00:00'
type: issue
status: closed
closed_at: '2021-11-22T21:29:36+00:00'
---

# Original Description
**Describe the bug**
gulf.moneroocean.stream:10128 - connect error: "operation canceled"

I have tried all ports and no luck
I have also tried fr.moneroocean.stream:10128 - Works fine - But nothing going into wallet.
Disabled Firewall as well.

**To Reproduce**
Happens every time I try to use this pool.

**Expected behavior**
I expect to be apart of the pool to mine XMR

**Required data**
 - Miner log as text or screenshot - ![errors](https://user-images.githubusercontent.com/60181403/142781726-e9bb8bae-9c9f-4a85-b071-5ea914d96ef2.gif)
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
        "argon2": [0, 1, 2, 3, 4, 5],
        "astrobwt": [0, 1, 2, 3, 4, 5],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5]
        ],
        "rx": [0, 1, 2, 3, 4],
        "rx/wow": [0, 1, 2, 3, 4, 5],
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
            "algo": null,
            "coin": null,
            "url": "gulf.moneroocean.stream:10128",
            "user": "",
            "pass": "",
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
 - OS: Windows 11 - Running in Admin mode
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.




# Discussion History
## maikiro | 2021-11-21T22:41:11+00:00
![errors](https://user-images.githubusercontent.com/60181403/142781754-427458d9-b68d-4bae-abd8-e5ddd7823c3f.gif)


## Spudz76 | 2021-11-22T11:25:11+00:00
Firewall or ISP is blocking.

## Killer-Software | 2021-11-22T20:01:51+00:00
Hi everyone, 
so @Spudz76 how do we unblock it like can u tell me the steps for Linux actually I'm new to Linux so that's why.

## maikiro | 2021-11-22T21:29:36+00:00
I changed to Googles DNS and it now works...

Thanks for the reply and advice all.

## Spudz76 | 2021-11-22T22:28:48+00:00
@Killer-Software perhaps that way, use an unfiltered DNS instead of what your ISP provides

## SAMIYOUNES | 2022-07-15T11:28:07+00:00
hi guys i have the same problem
help me plz

# Action History
- Created by: maikiro | 2021-11-21T22:40:41+00:00
- Closed at: 2021-11-22T21:29:36+00:00
