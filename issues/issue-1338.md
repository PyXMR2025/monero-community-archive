---
title: 'config.json<offset:1680>: "Invalid value." RandomX with monero'
source_url: https://github.com/xmrig/xmrig/issues/1338
author: smzwsz
assignees: []
labels:
- question
created_at: '2019-11-30T15:02:27+00:00'
updated_at: '2019-12-22T19:40:44+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:40:44+00:00'
---

# Original Description

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
        "memory-pool": false,
        "max-threads-hint": 50,
        "asm": true,
        "argon2-impl": null,
	"rx/0": [-1, -1, -1, -1],
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
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": null,
            "coin": "monero",
            "url": "192.168.10.58:9999",
            "user": "1",
            "pass": "x",
            "rig-id": null,
            "nicehash": ture,
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
    "watch": true
}


How To resolve

# Discussion History
## xmrig | 2019-11-30T18:33:13+00:00
`"nicehash": ture,` should be `true`, also if on another end is xmrig-proxy don't need change this option, it will be done automatically.
Thank you.

## smzwsz | 2019-12-01T03:24:46+00:00
Yes ,it's my mistake
But," end of file" now

## norsehealer | 2019-12-03T03:17:29+00:00
```
"self-select": null
}
],
"print-time": 60,
```

the `]` should be `{`

# Action History
- Created by: smzwsz | 2019-11-30T15:02:27+00:00
- Closed at: 2019-12-22T19:40:44+00:00
