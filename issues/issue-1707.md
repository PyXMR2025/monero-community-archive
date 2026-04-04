---
title: Wallet slowly rolling up all outputs into one
source_url: https://github.com/monero-project/monero/issues/1707
author: Snipa22
assignees: []
labels: []
created_at: '2017-02-11T05:16:01+00:00'
updated_at: '2017-10-26T16:52:38+00:00'
type: issue
status: closed
closed_at: '2017-10-26T16:52:38+00:00'
---

# Original Description
I assume this is expected and/or wanted functionality, but it's starting to get problematic as a pool-op.  At this point in time, I tend to have a single large output, which, as soon as it's spent, causes the wallet to not have enough available funds to multiple transactions.

I would assume that this is expected/wanted functionality, but it does cause issues for pool-ops, whom may be making 10-15-20 transactions at a time depending on the state of the pool.  Is there a good solution for this, or a good way to handle this going forwards?

# Discussion History
## moneromooo-monero | 2017-02-11T19:59:42+00:00
I see two ways to fix this:
- have a value threshold, where a second unnecessary input is added only if one is available under that threshold
- have a min outputs threshold, where a second unnecessary input is added only if the wallet has more outputs than this threshold


## moneromooo-monero | 2017-03-24T21:07:21+00:00
https://github.com/monero-project/monero/pull/1919 should help with this.

## moneromooo-monero | 2017-08-08T11:29:18+00:00
Wondering whether to keep this open or not. The settings above help, but they're not default, and I guess they're crude. Opinions ?

## Snipa22 | 2017-10-26T16:52:38+00:00
Sorry for not responding, looks like it helps deal with it without an issue.  We're good on our side.

# Action History
- Created by: Snipa22 | 2017-02-11T05:16:01+00:00
- Closed at: 2017-10-26T16:52:38+00:00
