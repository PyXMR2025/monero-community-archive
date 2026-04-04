---
title: Testnet not syncing (searching on port 18080, not 28080)
source_url: https://github.com/monero-project/monero/issues/3283
author: ghost
assignees: []
labels: []
created_at: '2018-02-17T22:02:24+00:00'
updated_at: '2018-02-19T16:18:09+00:00'
type: issue
status: closed
closed_at: '2018-02-19T16:18:09+00:00'
---

# Original Description
Built from source @ commit 4f80c50

./monerod --testnet

https://paste.fedoraproject.org/paste/saEwKma8NWdOyWlDM5l4cA

# Discussion History
## moneromooo-monero | 2018-02-17T22:24:46+00:00
Is it fixed by https://github.com/monero-project/monero/pull/3196 ?

## ghost | 2018-02-17T23:40:42+00:00
#3196 did not fix it. This issue includes the latest PRs (up till 4f80c50).

## moneromooo-monero | 2018-02-18T11:37:59+00:00
Does reverting https://github.com/monero-project/monero/pull/3170 fix it ?

## rodentrabies | 2018-02-18T15:11:07+00:00
That's on me. I'm really sorry but it seems like I accidentally removed an assignment to `m_testnet` at line 265 in `p2p/net_node.inl` during rebase. I will PR the fix in a few minutes.

## ghost | 2018-02-19T16:18:09+00:00
Fixed with #3290. I'm closing this.

# Action History
- Created by: ghost | 2018-02-17T22:02:24+00:00
- Closed at: 2018-02-19T16:18:09+00:00
