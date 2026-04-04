---
title: lazy fetching of the monero blockchain
source_url: https://github.com/monero-project/monero/issues/9399
author: milahu
assignees: []
labels:
- question
- feature
- low priority
- discussion
created_at: '2024-07-15T15:49:41+00:00'
updated_at: '2024-07-17T00:14:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
i assume that 90% of the blockchain are never used
because most transactions i see (event horizon) are only some weeks old
so the full monero blockchain of currently 90GB is mostly a waste of disk space

why no lazy fetching?
let me use a "shallow clone" of the blockchain
and only when a transaction requires deeper access to the blockchain
then fetch to the required depth
and maybe later delete the deep end of the chain to free disk space


# Discussion History
## selsta | 2024-07-16T22:15:33+00:00
I don't think this has a realistic chance of being implemented. It would require a lot of work regarding how this could be implemented in a secure way, and it would also increase load on the network. If someone does not have enough storage for a pruned blockchain it's best that they use a remote node.

# Action History
- Created by: milahu | 2024-07-15T15:49:41+00:00
