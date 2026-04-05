---
title: Log block reorgs
source_url: https://github.com/Cuprate/cuprate/issues/485
author: hinto-janai
assignees: []
labels:
- C-request
- E-easy
- E-help-wanted
created_at: '2025-05-23T13:02:05+00:00'
updated_at: '2025-08-05T18:16:21+00:00'
type: issue
status: closed
closed_at: '2025-08-05T18:16:21+00:00'
---

# Original Description
## Feature
Log blockchain reorganizations (with `INFO` level) similar to `monerod`:
```
###### REORGANIZE on height: 3415899 of 3415899 with cum_difficulty 458756629111791853
 alternative blockchain size: 2 with cum_difficulty 458757260229599716
----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3415899
id:        <5234cdf68226b798c2b5dbd630e537011d3d37525248de21f662fe0b6512d7ca>
PoW:        <795876025553dfeb9fd4b88eeb253a1e8832317cefc04a9f1197fd0000000000>
difficulty:        631078125715
REORGANIZE SUCCESS! on height: 3415899, new blockchain size: 3415901
```

# Discussion History
## Boog900 | 2025-05-23T20:49:07+00:00
this is logged at `info` level already: https://github.com/Cuprate/cuprate/blob/ce7a04f2d964875a95530b4cb2cb9522f6fce2f4/binaries/cuprated/src/blockchain/manager/handler.rs#L436-L446

I have already had a couple successful reorgs and seen the message.

# Action History
- Created by: hinto-janai | 2025-05-23T13:02:05+00:00
- Closed at: 2025-08-05T18:16:21+00:00
