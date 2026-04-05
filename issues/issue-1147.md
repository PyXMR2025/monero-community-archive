---
title: failed to parse field "seed_hash" required by RandomX
source_url: https://github.com/xmrig/xmrig/issues/1147
author: jacksonkr
assignees: []
labels: []
created_at: '2019-08-29T11:27:39+00:00'
updated_at: '2019-08-29T17:50:30+00:00'
type: issue
status: closed
closed_at: '2019-08-29T17:46:42+00:00'
---

# Original Description
XMRig/3.1.0 MSVC windows 10

I can get `cn/r` but any of the `rx` algos error out. I tried adding a 'seed_hash' value to the json with no avail. How can I get random x to work?

**Config**
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
    "version": 1,
    "background": false,
    "colors": true,
    "randomx": {
        "init": -1,
        "numa": true
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
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
        "cn/gpu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "rx": [0, 2, 4, 6, 8, 10, 12, 14],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": "cn/r",
            "url": "nyc02.supportxmr.com:5555",
            "user": "xxxx",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null,
            "daemon": false
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "syslog": false,
    "user-agent": null,
    "watch": true
}
```

# Discussion History
## xmrig | 2019-08-29T11:31:03+00:00
#1111

## jacksonkr | 2019-08-29T17:46:41+00:00
Based on #1111 from @xmrig comment I was able to get benchmarking working fine for both `rx/wow` and `rx/liko`. It looks like I'll have to find a pool that supports rx.

bencharmk url:
randomx-benchmark.xmrig.com:7777

i9-9900 no overclocking

cn/r @ 330 h/s
rx/* @ 1900 h/s

# Action History
- Created by: jacksonkr | 2019-08-29T11:27:39+00:00
- Closed at: 2019-08-29T17:46:42+00:00
