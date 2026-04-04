---
title: Maximum duration of network split
source_url: https://github.com/monero-project/monero/issues/1580
author: ghost
assignees: []
labels:
- invalid
created_at: '2017-01-15T16:46:04+00:00'
updated_at: '2017-10-03T21:30:23+00:00'
type: issue
status: closed
closed_at: '2017-10-03T21:30:23+00:00'
---

# Original Description
Let's say a transatlantic cable goes down and the mining network splits for x length of time, leading to two independent chains. The cable is then repaired.

What is the maximum age of a chain root that we'll accept as taking precedence over ours even if it does have more work? Should we set this at an upper limit like 1-2 weeks of age?

# Discussion History
## moneromooo-monero | 2017-08-08T11:48:00+00:00
If the other is valid, and has more work, then the other will be accepted. Setting an upper limit means a hard fork that is unresolvable, essentially making the two networks entirely separate. Either both keep going (with a lot of noise) and no commerce is possible (via monero) between the two patrs, or one dies, and the users have to manually delete and resync.


## moneromooo-monero | 2017-10-03T21:19:49+00:00
I'm not sure there's a point to this. If this was asking for a "please don't resolve forks after an arbitrary time has passed without resolution", then no, unless new research shows it to be a good idea.

For now,

+invalid


# Action History
- Created by: ghost | 2017-01-15T16:46:04+00:00
- Closed at: 2017-10-03T21:30:23+00:00
