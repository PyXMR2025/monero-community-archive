---
title: opencl config not working on fedora 39
source_url: https://github.com/xmrig/xmrig/issues/3414
author: proof-of-reality
assignees: []
labels: []
created_at: '2024-01-30T16:55:22+00:00'
updated_at: '2025-06-18T22:16:50+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:16:50+00:00'
---

# Original Description
xmrig not detecting AMD GPU

![image](https://github.com/xmrig/xmrig/assets/43297242/c2106e58-a819-4adb-bc9f-9cb84a233225)

lspci output:
![image](https://github.com/xmrig/xmrig/assets/43297242/e40b84ea-0c05-469b-b4b2-7820607eda5b)

``` config.json
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
        "argon2": [0, 4, 1, 5, 2, 6, 3, 7],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1]
        ],
        "cn-lite": [
            [1, 0],
            [1, 4],
            [1, 1],
            [1, 5],
            [1, 2],
            [1, 6],
            [1, 3],
            [1, 7]
        ],
        "cn-pico": [
            [2, 0],
            [2, 4],
            [2, 1],
            [2, 5],
            [2, 2],
            [2, 6],
            [2, 3],
            [2, 7]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 4],
            [2, 1],
            [2, 5],
            [2, 2],
            [2, 6],
            [2, 3],
            [2, 7]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3]
        ],
        "rx": [0, 1, 2, 3],
        "rx/wow": [0, 4, 1, 5, 2, 6, 3, 7],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": true,
        "cache": true,
        "loader": "/opt/rocm-6.0.0/lib/libOpenCL.so",
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 0,
    "donate-over-proxy": 1,
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "127.0.0.1:18083",
            "user": "👀",
            "pass": null,
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        },
        {
            "algo": null,
            "coin": null,
            "url": "127.0.0.1:3333",
            "user": null,
            "pass": null,
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
## Redhawk18 | 2024-03-15T03:56:09+00:00
I had this problem to, after reading I found it's been broken for years and since randomx doesn't do well on gpu's no one cares to fix it.

## SChernykh | 2024-03-15T07:18:59+00:00
XMRig only detects what OpenCL says, so the problem is within your platform's OpenCL implementation.

# Action History
- Created by: proof-of-reality | 2024-01-30T16:55:22+00:00
- Closed at: 2025-06-18T22:16:50+00:00
