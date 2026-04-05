---
title: probably commonconfig.cpp bug
source_url: https://github.com/xmrig/xmrig/issues/844
author: snipeTR
assignees: []
labels:
- bug
created_at: '2018-10-24T20:31:58+00:00'
updated_at: '2018-10-25T09:25:49+00:00'
type: issue
status: closed
closed_at: '2018-10-25T07:09:36+00:00'
---

# Original Description
commonconfig.cpp
line403     case PrintTimeKey:   /* --cpu-priority */


# Discussion History
## xmrig | 2018-10-25T07:09:36+00:00
Fixed, just wrong comment.
Thank you.

## snipeTR | 2018-10-25T09:17:35+00:00
Please add cpu priotry config commonconfig.cpp

## xmrig | 2018-10-25T09:25:49+00:00
`cpu-priority` is CPU miner option and placed in [core/Config.cpp](https://github.com/xmrig/xmrig/blob/master/src/core/Config.cpp#L335)

CommonConfig.cpp only for options shared between all miners and proxy.

# Action History
- Created by: snipeTR | 2018-10-24T20:31:58+00:00
- Closed at: 2018-10-25T07:09:36+00:00
