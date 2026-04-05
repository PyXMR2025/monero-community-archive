---
title: how to reverse engineer a provided json to commandline?
source_url: https://github.com/xmrig/xmrig/issues/2332
author: esaruoho
assignees: []
labels: []
created_at: '2021-04-30T06:10:18+00:00'
updated_at: '2025-06-16T20:29:59+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:29:59+00:00'
---

# Original Description
Hi, I've been given a json, but I'd prefer to run it via commandline commands. Any ideas how to do it?
```
{
    "autosave": true,
    "donate-level": 1,
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "hw-aes": null,
        "priority": null,
        "asm": true,
        "max-threads-hint": 100,
        "max-cpu-usage": 100,
        "yield": false,
        "init": -1,
        "*": {
            "intensity": 2,
            "threads": 8,
            "affinity": -1
        }
    },
    "opencl": true,
    "cuda": true,
    "pools": [
        {
            "coin": "monero",
            "algo": "cn/gpu",
            "url": "168.235.86.33:3393",
            "user": "omitted",
            "pass": "x",
            "tls": false,
            "keepalive": true,
            "nicehash": false
        }
    ]
}
```


# Discussion History
# Action History
- Created by: esaruoho | 2021-04-30T06:10:18+00:00
- Closed at: 2025-06-16T20:29:59+00:00
