---
title: 'pool.supportxmr.com:3333 192.168.4.1 connection error: "Connection refused."'
source_url: https://github.com/xmrig/xmrig/issues/3331
author: moonman239
assignees: []
labels: []
created_at: '2023-09-12T23:29:24+00:00'
updated_at: '2025-06-18T22:21:19+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:21:19+00:00'
---

# Original Description
Hi all,

I'm trying to CPU mine on a Windows 11 computer, using the supportxmr pool. I'm using the pool URL "pool.supportxmr.com:3333" but am getting this error: ```pool.supportxmr.com:3333 192.168.4.1 connection error: "Connection refused."```

I've reset my DNS cache using ipconfig /flushdns, but the issue remains. 

Here's my config:

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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 8],
            [1, 10],
            [1, 12],
            [1, 14]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11],
            [1, 12],
            [1, 13],
            [1, 14],
            [1, 15]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7],
            [2, 8],
            [2, 9],
            [2, 10],
            [2, 11],
            [2, 12],
            [2, 13],
            [2, 14],
            [2, 15]
        ],
        "ghostrider": [
            [8, 0],
            [8, 2],
            [8, 4],
            [8, 6],
            [8, 8],
            [8, 10],
            [8, 12],
            [8, 14]
        ],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
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
            "url": "pool.supportxmr.com:3333",
            "user": "49fX4wus7ecVwzYCW5gGs1FBjzZNiu6dtboaKJqKU58v5xyU6U8LcNZ4DY7sdPJV7fQhJK8WK2qV5imhWHrNhhq2QrHGv4R",
            "pass": "rig0",
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

# Discussion History
## geekwilliams | 2023-09-13T02:03:23+00:00
Your config looks okay. Does the ip 192.168.4.1 actually appear in the error message? What is the rest of the output when you start xmrig?

## moonman239 | 2023-09-13T02:09:32+00:00
@geekwilliams Yes.
So, 192.168.4.1 is my router.
When I ran "nslookup pool.supportxmr.com" I got 
```
Non-authoritative answer
Address: 192.168.4.1
```

A networking guy I spoke with suggested my router was blocking me from accessing pool.supportxmr.com.

Apparently the router has "poisoned" my DNS.


Using a different pool seems to work.






## geekwilliams | 2023-09-13T02:58:25+00:00
Ah, ISP's will do that, especially with supportxmr since they're a pretty well known pool used by a lot of malware.  I would suggest maybe trying a different DNS configuration.  Google's DNS servers (8.8.8.8, 8.8.4.4) don't block supportxmr.com that I'm aware of.  If you're worried about privacy there are plenty of other providers.  

## ktwrd | 2025-04-29T01:50:38+00:00
> Ah, ISP's will do that, especially with supportxmr since they're a pretty well known pool used by a lot of malware. I would suggest maybe trying a different DNS configuration. Google's DNS servers (8.8.8.8, 8.8.4.4) don't block supportxmr.com that I'm aware of. If you're worried about privacy there are plenty of other providers.

@geekwilliams Google, Cloudflare, and Quad9 now block `pool.supportxmr.com` :/

# Action History
- Created by: moonman239 | 2023-09-12T23:29:24+00:00
- Closed at: 2025-06-18T22:21:19+00:00
