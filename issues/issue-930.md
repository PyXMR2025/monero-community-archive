---
title: config.json <29> keeps sending missing colonafter a name object?
source_url: https://github.com/xmrig/xmrig/issues/930
author: johnsix12
assignees: []
labels: []
created_at: '2019-02-12T20:12:40+00:00'
updated_at: '2019-03-17T16:33:58+00:00'
type: issue
status: closed
closed_at: '2019-03-17T16:33:58+00:00'
---

# Original Description
what am i doing wrong?


# Discussion History
## johnsix12 | 2019-02-12T20:19:16+00:00
   "algo": { "cryptonight"},
    "api": {,
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id":,
        "ipv6": false,
        "restricted": true,
    }
    "asm": true,
    "autosave": true,
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 5,
    "huge-pages": true,
    "hw-aes": null,
    "log-file": null,
    "max-cpu-usage": 75,
    "pools": [
        {
            "url": { "xmr.2miners.com:2222" },
            "user": {  },
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": false,
            "variant": -1,
            "tls": false,
            "tls-fingerprint": null,
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "threads": [
        {
            "low_power_mode": 1,
            "affine_to_cpu": false,
            "asm": true,
        }
    ],
    "user-agent": null,
    "watch": false,
}

## 2010phenix | 2019-02-23T11:42:29+00:00
in first line you missing - {

## DeadManWalkingTO | 2019-03-17T16:14:54+00:00
I think this issue can be closed.
Thank you!

# Action History
- Created by: johnsix12 | 2019-02-12T20:12:40+00:00
- Closed at: 2019-03-17T16:33:58+00:00
