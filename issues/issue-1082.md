---
title: xmrig-2.99.2-beta Algo-rx/loki dont work anymore (under WIN)
source_url: https://github.com/xmrig/xmrig/issues/1082
author: Cideg
assignees:
- xmrig
labels:
- bug
created_at: '2019-07-29T09:26:15+00:00'
updated_at: '2019-07-30T02:50:10+00:00'
type: issue
status: closed
closed_at: '2019-07-29T16:07:33+00:00'
---

# Original Description
hello together, with the new update, the algo rx / loki no longer works under win.

the following error message is displayed:
incompatible / disabled algorithm rx / loki detected, reconnect

many thanks

# Discussion History
## xmrig | 2019-07-29T09:49:26+00:00
Please show:

1. First lines from miner start.
2. Config file, without wallets.

Thank you.

## xmrig | 2019-07-29T10:01:26+00:00
Seems this issue happen because autoconfig fails, but I need requested above information to know why it exactly fails.
Thank you.

## Cideg | 2019-07-29T10:14:55+00:00
Thank you for your prompt reply

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
        "cn": [],
        "cn-heavy": [],
        "cn-lite": [],
        "cn-pico": [],
        "cn/gpu": [],
        "rx": [],
        "rx/wow": [],
        "cn/0": false,
        "cn-lite/0": false
    },
    "donate-level": 1,
    "donate-over-proxy": 1,
    "log-file": null,
    "pools": [
        {
            "algo": rx/loki,
            "url": "167.86.103.145:3993",
            "user": "",
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

First lines miner:
<a href="https://ibb.co/YfFY6HF"><img src="https://i.ibb.co/YfFY6HF/xmrig-299.jpg" alt="xmrig-299" border="0"></a>



### Version 2.99.1 works without problems
<a href="https://ibb.co/nRJq0tH"> <img src = "https://i.ibb.co/nRJq0tH/xmrig2.jpg" alt = "xmrig2" border = "0"> </ a>

## xmrig | 2019-07-29T11:04:02+00:00
~~Can you download **hwloc-win64-build-1.11.13.zip** from https://www.open-mpi.org/software/hwloc/v1.11/ and run `lstopo.exe topo.xml` then share resulting `topo.xml` somehow.~~
No longer required. Thank you.

## xmrig | 2019-07-29T12:33:35+00:00
Fixed, binaries for this fix https://download.xmrig.com/xmrig/2.99.3-evo/6b3b1c3fc412981e51892bafd62b3dc4c1f87e7d/
`cpu` object in config should be removed to allow autoconfig fill it again.
Thank you.

## xmrig | 2019-07-30T02:50:10+00:00
v2.99.3-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.3-beta

# Action History
- Created by: Cideg | 2019-07-29T09:26:15+00:00
- Closed at: 2019-07-29T16:07:33+00:00
