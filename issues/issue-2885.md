---
title: How too change difficulty in xmrig?
source_url: https://github.com/xmrig/xmrig/issues/2885
author: coldKorvo
assignees: []
labels: []
created_at: '2022-01-22T00:29:02+00:00'
updated_at: '2022-01-22T12:47:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
I cant mine any crypto because the difficulty is too high is there any way too change this Ill show the config.json here:

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
        "enabled": false,
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
            "url": "rx.unmineable.com:3333",
            "user": "TRX:TEKsUbixRWoTyfeX45hKkFMBE9R3HBbKuY.EEE",
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


# Discussion History
## lfaoro | 2022-01-22T12:47:41+00:00
as I understood, you can override the pool difficulty by setting the "user" param with the difficulty value of your choice after the address with `+value` -- e.g. `-u x+480000`

in your case: `"user": "TRX:TEKsUbixRWoTyfeX45hKkFMBE9R3HBbKuY.EEE+480000",`

try it out as I'm not 100% sure.

# Action History
- Created by: coldKorvo | 2022-01-22T00:29:02+00:00
