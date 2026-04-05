---
title: Unable to get Max CPU
source_url: https://github.com/xmrig/xmrig/issues/59
author: diggles9991
assignees: []
labels: []
created_at: '2017-08-14T12:02:26+00:00'
updated_at: '2017-08-17T14:30:41+00:00'
type: issue
status: closed
closed_at: '2017-08-17T14:30:41+00:00'
---

# Original Description
I cannot get XMRig to use Max CPU, keeps stopping around 37%.
My config file is below.

{
    "algo": "cryptonight",
    "av": 0,
    "background": true,
    "colors": true,
    "cpu-affinity": null,
    "donate-level": 1,
    "log-file": null,
    "max-cpu-usage": 100,
    "print-time": 60,
    "retries": 5,
    "retry-pause": 5,
    "safe": false,
    "syslog": false,
    "threads": null,
    "pools": [
        {
            "url": "xmr.pool.minergate.com:45560",
            "user": "diggles9991@gmail.com",
            "pass": "x",
            "keepalive": true,
            "nicehash": false
        }
    ]
}

# Discussion History
## stewis | 2017-08-15T13:22:07+00:00
What CPU model are you using?  As its size of your L3 (L2??) cache that determines number of threads and max processor load.

## xmrig | 2017-08-15T22:27:49+00:00
`max-cpu-usage` is option to limit maximum thread count and visible CPU load as well. Doesn't mater how many threads support your CPU, only matters how many cache in it. On most desktop CPUs 100% visible load impossibility, except AMD FX series.

Example: typical i7 8 threads, 8 MB cache, no need use more than 4 threads (50%) for `--av=1` and more than 2 (25%) for `--av=2`.

# Action History
- Created by: diggles9991 | 2017-08-14T12:02:26+00:00
- Closed at: 2017-08-17T14:30:41+00:00
