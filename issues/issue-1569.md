---
title: rejected (0/1) diff 25000 "low difficulty share"
source_url: https://github.com/xmrig/xmrig/issues/1569
author: krazydan
assignees: []
labels: []
created_at: '2020-02-26T22:11:13+00:00'
updated_at: '2020-08-29T04:54:21+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:54:21+00:00'
---

# Original Description
i keep getting rejected (0/1) diff 25000 "low difficulty share" when i start mining xmr 

i dont know what is causing this to happen , ive followed steps and its not working.

Here is my settings, im running latest xmrig-nvidia and i have a 2070 super
{
    "algo": "cryptonight",
    "api": {
        "port": 0,
        "access-token": null,
        "id": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "background": false,
    "colors": true,
    "cuda-bfactor": 6,
    "cuda-bsleep": 25,
    "cuda-max-threads": 64,
    "donate-level": 1,
    "log-file": null,
    "pools": [
        {
            "url": "xmrpool.eu:3333",
            "user": "",
            "pass": "x",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "variant": -1,
            "enabled": true,
            "tls": false,
            "tls-fingerprint": null
        }
    ],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "threads": [
        {
            "index": 0,
            "threads": 26,
            "blocks": 120,
            "bfactor": 6,
            "bsleep": 25,
            "sync_mode": 3,
            "affine_to_cpu": false
        }
    ],
    "user-agent": null,
    "syslog": false,
    "watch": true
}

# Discussion History
## 2010phenix | 2020-02-26T23:27:09+00:00
it's old config
use field coin "monero"
and algo us remember now "rx/0"

## SChernykh | 2020-02-27T10:29:03+00:00
xmrig-nvidia is not updated anymore and it doesn't support RandomX. Use the latest XMRig with CUDA plugin.

# Action History
- Created by: krazydan | 2020-02-26T22:11:13+00:00
- Closed at: 2020-08-29T04:54:21+00:00
