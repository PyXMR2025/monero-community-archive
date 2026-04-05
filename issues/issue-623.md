---
title: v2.6.2 Low Difficulty Share Rejected (AEON)
source_url: https://github.com/xmrig/xmrig/issues/623
author: DeadManWalkingTO
assignees: []
labels: []
created_at: '2018-05-09T21:41:50+00:00'
updated_at: '2018-06-17T18:02:26+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:02:26+00:00'
---

# Original Description
OS: Ubuntu 16.04 / Win7
CPU: Intel x64 / Arm x64
Xmrig: v2.6.2
Coin: AEON
Low Difficulty Share Rejected

Downgrade to v2.5.3 works fine!

Any suggestions?

Thank you!

# Discussion History
## xmrig | 2018-05-09T23:36:14+00:00
Algorithm options for AEON:
```json
{
    "algo": "cryptonight-lite",
    ...
    "pools": [
        {
            ...
            "variant": -1
        }
    ]
}
```
v2.6 supports config files from v2.5, if breaking changes in config file happen, major miner version will change to v3.
Thank you.

## 2010phenix | 2018-05-11T11:41:54+00:00
khm, strange... try 2.6.2 with TurtleCoin on (stratum+tcp://trtl.pool.mine2gether.com:1115)
used cn-lite/1 and try cn-lite/0 - confirm Share Rejected

# Action History
- Created by: DeadManWalkingTO | 2018-05-09T21:41:50+00:00
- Closed at: 2018-06-17T18:02:26+00:00
