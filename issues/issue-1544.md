---
title: About xmrig in Windows Server 2008 R2 64 bit
source_url: https://github.com/xmrig/xmrig/issues/1544
author: dafeishaoji
assignees: []
labels: []
created_at: '2020-02-10T05:17:33+00:00'
updated_at: '2020-02-23T23:24:33+00:00'
type: issue
status: closed
closed_at: '2020-02-23T23:24:33+00:00'
---

# Original Description





I ran xmrig program on Windows Server 2008 R2 64 bit, and found that xmrig was automatically closed after running. Initially, I checked for MSR permission. Later, i banned MSR mode, and found that xmrig was automatically closed after running. Would you like to ask if other windows programs are needed?

my config.json is：

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
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "argon2": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn": [
            [1, 0],
            [1, 2],
            [1, 4]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 4],
            [1, 6],
            [1, 1],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3],
            [2, 4],
            [2, 5],
            [2, 6],
            [2, 7]
        ],
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx": [0, 2, 4],
        "rx/arq": [0, 1, 2, 3, 4, 5, 6, 7],
        "rx/wow": [0, 2, 4, 6, 1, 3],
        "cn/0": false,
        "cn-lite/0": false
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
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
    "donate-level": 5,
    "donate-over-proxy": 1,


    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xx ",
            "user": " xx",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false,
            "self-select": null
        }
    ],
    "print-time": 60,
    "health-print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "verbose": 0,
    "watch": true
}

# Discussion History
## 2010phenix | 2020-02-10T16:41:14+00:00
man LOL )),  add:
        "algo": null,
        "coin": null,
        "url": "xx ",
        "user": " xx",
 

# Action History
- Created by: dafeishaoji | 2020-02-10T05:17:33+00:00
- Closed at: 2020-02-23T23:24:33+00:00
