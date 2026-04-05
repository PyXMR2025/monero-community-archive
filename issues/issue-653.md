---
title: mac 10.13.3 xmrig does not work
source_url: https://github.com/xmrig/xmrig/issues/653
author: Cydmi
assignees: []
labels: []
created_at: '2018-05-28T06:42:38+00:00'
updated_at: '2018-05-28T07:03:07+00:00'
type: issue
status: closed
closed_at: '2018-05-28T07:03:07+00:00'
---

# Original Description
`./xmrig -c ./config.json`
My configuration.
> {

    "algo": "cryptonight-heavy",
    "api": {
        "port": 0,
        "access-token": null,
        "worker-id": null,
        "ipv6": false,
        "restricted": true
    },
    "av": 0,
    "background": true,
    "colors": true,
    "cpu-priority": null,
    "donate-level": 5,
    "log-file": "xmr.log",
    "max-cpu-usage": 75,
    "pools": [{
            "url": "pool.supportxmr.com:80",
            "user": "my address",
            "pass": "Mx",
            "keepalive": true,
            "nicehash": false
        }],
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "syslog": false,
    "threads": null
}
xmr.log
>[2018-05-28 14:22:07]  * VERSIONS:     XMRig/2.6.2 libuv/1.19.2 clang/9.1.0
[2018-05-28 14:22:07]  * CPU:          Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz (1) x64 AES-NI
[2018-05-28 14:22:07]  * CPU L2/L3:    0.5 MB/3.0 MB
[2018-05-28 14:22:07]  * THREADS:      1, cryptonight-heavy, av=0, donate=5%
[2018-05-28 14:22:07]  * POOL #1:      pool.supportxmr.com:80
[2018-05-28 14:22:07]  * COMMANDS:     hashrate, pause, resume

# Discussion History
## snipeTR | 2018-05-28T06:49:19+00:00
Background false
Threads "all"

## Cydmi | 2018-05-28T07:03:03+00:00
thank you! @snipeTR 

# Action History
- Created by: Cydmi | 2018-05-28T06:42:38+00:00
- Closed at: 2018-05-28T07:03:07+00:00
