---
title: HTTP not working in FreeBSD Jail when using sysrc and background:true
source_url: https://github.com/xmrig/xmrig/issues/1507
author: russoj88
assignees: []
labels: []
created_at: '2020-01-20T17:28:36+00:00'
updated_at: '2021-04-12T15:02:26+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:02:26+00:00'
---

# Original Description
I have a fresh install of FreeBSD 12.1.  I created a jail and installed xmrig using pkg.
With background:false, calling the binary in the terminal seems to work fine: `xmrig --config=/usr/local/etc/xmrig/config.json`.
With background:true, I cannot connect via http (using http://workers.xmrig.info/).  It does seem to be running (400% CPU), but no logs and unable to connect.
If I use sysrc, it also does not work, background true or false.

**To Reproduce**
Here is the config I am using:
```json
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": true,
        "host": "0.0.0.0",
        "port": 80,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": true,
    "colors": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": false,
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
            [1, 4],
            [1, 6]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 2]
        ],
        "cn-lite": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7]
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
        "rx": [0, 2, 4, 6],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD"
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": "/root/miner.log",
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "192.168.1.3:18081",
            "user": "",
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": true,
            "daemon-poll-interval": 1000
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
```

**Expected behavior**
Ability to connect via HTTP whether it's running in the background or not.


# Discussion History
# Action History
- Created by: russoj88 | 2020-01-20T17:28:36+00:00
- Closed at: 2021-04-12T15:02:26+00:00
