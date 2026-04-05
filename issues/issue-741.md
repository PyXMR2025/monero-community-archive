---
title: How did xmrig make the transition to c7 autonomously?
source_url: https://github.com/xmrig/xmrig/issues/741
author: ghost
assignees: []
labels:
- question
created_at: '2018-08-27T09:45:02+00:00'
updated_at: '2018-10-10T22:30:11+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:30:11+00:00'
---

# Original Description
I'm trying to find in the code how xmrig decided when to shift from cryptonote to cryptonote v1 at the last hardfark in april. I expected it to compare the block height to the number 1539500 to make the shift but couldn't find that number in the code. 

Which part of the code was responsible for that feature?

# Discussion History
## 2010phenix | 2018-08-28T13:20:54+00:00
man, don't be sooo lazy... use search or ask google

## Spudz76 | 2018-09-10T08:23:18+00:00
Job packets from pool have a version field.
New fork has a new version number, old has the old, pretty simple.  Nothing to do with block numbers at all.  If a pool or coin jumps back (as Electroneum did) the old version would also fall back just fine.  It's all about the pool or proxy and what it sends as version.

# Action History
- Created by: ghost | 2018-08-27T09:45:02+00:00
- Closed at: 2018-10-10T22:30:11+00:00
