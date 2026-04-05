---
title: Hi/problem
source_url: https://github.com/xmrig/xmrig/issues/208
author: xxlxxlxxl
assignees: []
labels:
- question
created_at: '2017-11-19T20:00:45+00:00'
updated_at: '2017-11-27T00:08:24+00:00'
type: issue
status: closed
closed_at: '2017-11-27T00:08:24+00:00'
---

# Original Description
hi, i open xmrig.exe
and it appear a error that says no login/password provided, i also provide a login password, but also says there is no wallet specified
can you help ?

# Discussion History
## xmrig | 2017-11-20T09:51:55+00:00
Add your wallet and optional on most pools password, to your config.json file.
Thank you.

## xxlxxlxxl | 2017-11-20T22:19:07+00:00
{
    "algo": "cryptonight",
    "av": 0,
    "background": false,
    "colors": true,
    "cpu-affinity": null,
    "cpu-priority": null,
    "donate-level": 5,
    "log-file": null,
    "max-cpu-usage": 1000000,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "syslog": false,
    "threads": null,
    "pools": [
        {
            "url": "pool.minemonero.pro:5555",
            "user": "wallet adress*",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        }
    ]
}



i make config like this is it ok?

and after how much hours payment are credited in my wallet?

# Action History
- Created by: xxlxxlxxl | 2017-11-19T20:00:45+00:00
- Closed at: 2017-11-27T00:08:24+00:00
