---
title: missing wiki source link
source_url: https://github.com/xmrig/xmrig/issues/2667
author: snipeTR
assignees: []
labels:
- bug
created_at: '2021-11-02T20:08:45+00:00'
updated_at: '2025-06-16T20:24:42+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:24:42+00:00'
---

# Original Description
page:https://xmrig.com/docs/algorithms
missing link
https://github.com/xmrig/xmrig/blob/master/src/crypto/common/Algorithm.cpp

# Discussion History
## Spudz76 | 2021-11-03T11:30:58+00:00
Also https://xmrig.com/docs/miner/build/ubuntu down in Advanced Build:

`5. cmake .. -DXMRIG_DEPS=scripts/deps`

should be

`5. cmake .. -DXMRIG_DEPS=../scripts/deps`

I have fix-splained that to several noobs :)

# Action History
- Created by: snipeTR | 2021-11-02T20:08:45+00:00
- Closed at: 2025-06-16T20:24:42+00:00
