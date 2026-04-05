---
title: Dev donation unpauses
source_url: https://github.com/xmrig/xmrig/issues/1300
author: jagerman
assignees: []
labels:
- bug
created_at: '2019-11-18T20:19:41+00:00'
updated_at: '2020-02-09T10:41:28+00:00'
type: issue
status: closed
closed_at: '2020-02-09T10:41:28+00:00'
---

# Original Description
If xmrig is paused and the donation timer kicks in then xmrig unpauses mining for the dev donation, then returns to the configured pool.

The internal state, however, isn't quite right: the "p" key to pause doesn't work (presumably because it thinks it is already paused) and hitting "r" print "resumed" (though its already mining).

A couple of potential ideas:
- the donation mining should just not start when currently paused
- pausing should also pause the donation timer

# Discussion History
## xmrig | 2019-11-18T20:54:54+00:00
Confirmed. Thank you.

## xmrig | 2019-11-22T18:24:48+00:00
What algorithm do yo mine? I start fixing this issue, and yes miner connects to donation and then switch back to user pool, but it not unpause miner, so is only negative impact I lose this donation round, proper fix however required a lot of changes.

Miner handle donation job like regular user job (with some extra logic, but it not important in this case), and regular jobs not unpause the miner (CPU, GPU is still idle).
Thank you.

# Action History
- Created by: jagerman | 2019-11-18T20:19:41+00:00
- Closed at: 2020-02-09T10:41:28+00:00
