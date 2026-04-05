---
title: DNS error
source_url: https://github.com/xmrig/xmrig/issues/431
author: bay1ts
assignees: []
labels: []
created_at: '2018-03-05T12:55:43+00:00'
updated_at: '2018-03-06T08:29:17+00:00'
type: issue
status: closed
closed_at: '2018-03-06T08:29:17+00:00'
---

# Original Description
DNS error: "unknown node or service",using pool pool.minexmr.com:7777.  Any suggestion?

# Discussion History
## bay1ts | 2018-03-05T13:19:40+00:00
sometimes it may be: connect error: "connection timed out"

## xmrig | 2018-03-05T13:50:35+00:00
Your ISP may block connection to pool. For DNS errors, check `ping pool.minexmr.com` or `nslookup pool.minexmr.com` if IP can't resolved, miner can't work too.

You can try use one of IP address of pool:
```
          94.130.164.60
          188.165.199.78
          176.9.50.126
          94.130.206.79
          94.23.212.204
          37.59.44.93
          91.121.87.10
          94.23.41.130
          78.46.91.134
          78.46.89.102
          37.59.45.174
          178.63.48.196
          176.31.117.82
          176.9.63.166
          176.9.53.68
          188.165.214.95
          37.59.54.205
          37.59.44.193
          91.121.2.76
          37.59.43.136
```

## bay1ts | 2018-03-06T08:29:17+00:00
That is not good.thanks for your work

# Action History
- Created by: bay1ts | 2018-03-05T12:55:43+00:00
- Closed at: 2018-03-06T08:29:17+00:00
