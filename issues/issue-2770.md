---
title: 'Request: Average hash rate http api'
source_url: https://github.com/xmrig/xmrig/issues/2770
author: Csordi
assignees: []
labels: []
created_at: '2021-12-01T22:19:07+00:00'
updated_at: '2021-12-02T19:05:47+00:00'
type: issue
status: closed
closed_at: '2021-12-02T19:05:46+00:00'
---

# Original Description
XMRig/6.16.1

It would be really nice if I can check the average hash rate with the http api.
Now I have to login every single PC if I want to know. Because this average hash rate is missing from the returned summary json

```
    "hashrate": {
        "total": [3447.31, 3445.19, 4223.13],
        "highest": 15062.78
    }

```

# Discussion History
## Spudz76 | 2021-12-01T23:12:15+00:00
use `/2/backends`

## Spudz76 | 2021-12-01T23:15:08+00:00
Also that's already averages in the array, like:
```
"total": [10s, 60s, 15m],
```

## Spudz76 | 2021-12-01T23:19:29+00:00
For all-time average you can use `/2/summary` items `results.hashes_total` divided by `uptime`

## Csordi | 2021-12-02T19:05:46+00:00
What I want to check is the all-time average. Because I use ghostrider algo and the hashrate is not stable at all. So I can not use 10sec/60sec/15 min average. The results.hashes_total / uptime gives the correct all-time average value. Thanks!

# Action History
- Created by: Csordi | 2021-12-01T22:19:07+00:00
- Closed at: 2021-12-02T19:05:46+00:00
