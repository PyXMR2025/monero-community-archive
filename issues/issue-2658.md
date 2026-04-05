---
title: 'Xmrig keeps finding jobs but won''t accept them '
source_url: https://github.com/xmrig/xmrig/issues/2658
author: NaroticGA
assignees: []
labels: []
created_at: '2021-10-29T09:12:02+00:00'
updated_at: '2025-06-20T11:10:40+00:00'
type: issue
status: closed
closed_at: '2025-06-20T11:10:40+00:00'
---

# Original Description
Anyone help me figure this out, not sure what i seem to be doing wrong
![97BE5532-CA51-4EDC-BC30-8FEA1DD42A64](https://user-images.githubusercontent.com/88416702/139409102-2eb689fa-bb0a-496d-9d11-6db0dc5db581.jpeg)
.  
That the image of the code in action but this is the actual code.  Also, followed this video https://www.youtube.com/watch?v=lV9cj32Ftvw , initially i tried it with SHIB to see if it would work tried it with RVN too still, no workers shows on unmieable and no jobs being taken. 
{
    "api": {
        "id": null,
        "worker-id":null
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "astrobwt": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-heavy": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-pico": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/upx2": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "cn-lite/0": false,
        "cn/0": false
    },
    "cuda": {
        "enabled": false,
        "loader": null,
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
            "url": "rx.unmineable.com:13333",
            "user": "RVN:RJSXSuZqEYajvMT35BUmLAxktZvPgbAp7N.MBP",
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
        "ipv6": true,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}

# Discussion History
## 8lecramm | 2021-10-29T17:29:42+00:00
This looks like a connection/network problem.
You get the same job again and again.
If you don't have problems with your local network, try to connect to a different port (3333).

## Spudz76 | 2021-10-29T22:43:21+00:00
You need smaller job difficulty, like `45000` (1500H/s * 30s)

`100001` diffculty it is giving you is for 3333.3667H/s minimum.

Good pools have variable difficulty which will lower itself to your speed.  Some pools have another port for slower miners, or a way to force diff with something added to the password string.  Like I said you need 45000 to match your hashrate, or you will very rarely get paid anything for your work (the accepts).  You want an accept about every 30 seconds therefore the difficulty-math is your hashrate times 30 (how many hashes you can check per 30s).

If you don't have a result to send within each 60s it will hang up on you for idling, which is why the connection keeps breaking.

## NaroticGA | 2021-10-30T02:14:15+00:00
Thanks guys ima leave this up for anyone with the same problem

## Chowdary1999 | 2021-10-31T21:36:46+00:00
if you are using cpu to mine on Mac you need to specify "algo" : "rx/0", and also with unminable port 443 and 3333 works better for some reason.

# Action History
- Created by: NaroticGA | 2021-10-29T09:12:02+00:00
- Closed at: 2025-06-20T11:10:40+00:00
