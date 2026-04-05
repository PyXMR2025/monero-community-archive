---
title: ' DNS error: "unknown node or service" after updating'
source_url: https://github.com/xmrig/xmrig/issues/3500
author: FabioNevesRezende
assignees: []
labels: []
created_at: '2024-06-20T00:12:33+00:00'
updated_at: '2025-06-16T19:42:07+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:42:07+00:00'
---

# Original Description
**Describe the bug**
After updating from `6.21.0` to `6.21.3` my xmrig instance no more resolve the pool address that I always used

**To Reproduce**
- Run xmrig with the url "pool.hashvault.pro:80" in config.json

**Expected behavior**
The mining process to being:
![image](https://github.com/xmrig/xmrig/assets/42902918/e28b68cf-4b16-4f25-8800-1e3efca2940e)


**What actually happens:**
![image](https://github.com/xmrig/xmrig/assets/42902918/57eaade8-942e-4c07-876b-00faa6640a4a)

I don't think it is my DNS server problem since I can `ping pool.hashvault.pro` and it returns the IP.

**Required data**
 - 6.21.3
- Command: ./xmrig -t 2;
- Config:


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
        "argon2": [0, 1, 3],
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
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 2],
            [2, 1],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 2],
            [2, 1],
            [2, 3]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1]
        ],
        "rx": [0, 1],
        "rx/arq": [0, 2, 1, 3],
        "rx/wow": [0, 1, 3],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/keva": "rx/wow"
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "pool.hashvault.pro:80",
            "user": "myaddress",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "sni": false,
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


```

# Discussion History
## SChernykh | 2024-06-20T07:46:19+00:00
This has nothing to do with XMRig version (if you switch back to 6.21.0, it will be the same). Their DNS server is misconfigured (NXDOMAIN):
```
nslookup pool.hashvault.pro
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   pool.hashvault.pro
Address: [redacted]
Name:   pool.hashvault.pro
Address: [redacted]
** server can't find pool.hashvault.pro: NXDOMAIN
```

## frak | 2024-06-21T13:15:43+00:00
I am getting this issue as well, but oddly only on one machine on the same network as two others (one linux, one windows) which are able to resolve the DNS without any errors

# Action History
- Created by: FabioNevesRezende | 2024-06-20T00:12:33+00:00
- Closed at: 2025-06-16T19:42:07+00:00
