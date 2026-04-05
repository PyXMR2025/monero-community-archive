---
title: RX470 KAWPOW low/invalid hashrate since apr.19
source_url: https://github.com/xmrig/xmrig/issues/2320
author: korlcek
assignees: []
labels: []
created_at: '2021-04-27T17:15:33+00:00'
updated_at: '2021-04-27T17:15:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
on apr.19 kawpow started working slower and slower and eventually stopped.
Now it's working with very low hashrate and report is showing invalid numbers.
At first I thought it might be a driver issue so I reinstalled everything (Win10) but still the same.
Tried different driver versions (20.4.2, 20.8.1, 21.4.1) all have the same problem.

I'm guessing it's the problem with implementation as at least one other miner (will not advertise) works normally.


```
[2021-04-27 18:37:16.567]  net      new job from kawpow.eu.nicehash.com:3385 diff 364M algo kawpow height 1729591
[2021-04-27 18:37:27.661]  opencl   #0 02:00.0  31W 39C    0RPM 1019/1700MHz
[2021-04-27 18:37:27.663]  opencl   #1 07:00.0  34W 52C    0RPM 1019/1700MHz
[2021-04-27 18:37:27.665]  opencl   #2 03:00.0  75W 59C 1951RPM 1019/1700MHz
[2021-04-27 18:37:27.681]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
| OPENCL # | AFFINITY | 10s  H/s | 60s  H/s | 15m  H/s |
|        0 |       -1 |      n/a | 514745.5 |      n/a | #0 02:00.0 Radeon (TM) RX 470 Graphics (Ellesmere)
|        1 |       -1 |      n/a | 514682.5 |      n/a | #1 07:00.0 Radeon (TM) RX 470 Graphics (Ellesmere)
|        2 |       -1 | 7815001.5 | 7829210.8 |      n/a | #2 03:00.0 Radeon (TM) RX 470 Graphics (Ellesmere)
|        - |        - |      n/a |      n/a |      n/a |
[2021-04-27 18:37:50.247]  miner    speed 10s/60s/15m n/a n/a n/a H/s max n/a H/s
```

# Discussion History
# Action History
- Created by: korlcek | 2021-04-27T17:15:33+00:00
