---
title: 'read error: "end of file"'
source_url: https://github.com/xmrig/xmrig/issues/3237
author: waterghost-2046
assignees: []
labels: []
created_at: '2023-03-28T08:43:44+00:00'
updated_at: '2023-03-31T23:43:37+00:00'
type: issue
status: closed
closed_at: '2023-03-31T23:43:37+00:00'
---

# Original Description
**Describe the bug**
read error: "end of file"

**To Reproduce**
Run xmrig 6.19.1 with this config file

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 -  net      equihash.unmineable.com:4444 read error: "end of file"
 - Config file or command line (without wallets)
 - [config.txt](https://github.com/xmrig/xmrig/files/11087227/config.txt)
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
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-heavy": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-lite": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn-pico": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/upx2": [0, 1, 2, 3, 4, 5, 6, 7],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7]
        ],
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
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "rx/0",
            "coin": null,
            "url": "equihash.unmineable.com:4444",
            "user": "DOGE:D5gc6cSGFUNHaDD5nMMaNjCNHzdJy5jKJc.m11",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": true,
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
        "enabled": true,
        "protocols": null,
        "cert": "cert.pem",
        "cert_key": "cert_key.pem",
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

 - OS: macosx
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.



# Discussion History
## SChernykh | 2023-03-28T08:59:22+00:00
> equihash.unmineable.com:4444 read error: "end of file"

Because XMRig doesn't support equihash.

## waterghost-2046 | 2023-03-31T23:43:37+00:00
After hearing that, I tried it with the ramdomx algorithm and it works. Thank you.

# Action History
- Created by: waterghost-2046 | 2023-03-28T08:43:44+00:00
- Closed at: 2023-03-31T23:43:37+00:00
