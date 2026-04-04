---
title: 'Unable to use two daemons with a single DB '
source_url: https://github.com/monero-project/monero/issues/4486
author: msgmaxim
assignees: []
labels: []
created_at: '2018-10-02T04:49:14+00:00'
updated_at: '2018-12-13T13:09:14+00:00'
type: issue
status: closed
closed_at: '2018-12-13T13:09:14+00:00'
---

# Original Description
PR #1748 seems to suggest that two daemons can share the same database. This in not the case, at least not with the current version on master branch.

As far as I can tell the problem can be reduced to the following scenario:

0. Daemons A and B both synced with the network.
1. Daemon A receives tx A, saves it to DB and updates its state (namely `m_txs_by_fee_and_receive_time`). At the same time daemon B will ignore this tx as it sees it in the database.
2. Daemon B receives tx B, saves it to DB and updates its state.
3. When, say, daemon A receives a block with transactions A and B, it cannot find tx B in its `m_txs_by_fee_and_receive_time` and thus fails to add the block. Likewise, daemon B would not able to find tx A, even though both transactions are recorded in the DB.

I don't see anything in the codebase that attempts to keep `m_txs_by_fee_and_receive_time` and the database in sync.


# Discussion History
## moneromooo-monero | 2018-10-02T10:55:00+00:00
There is nothing that does indeed. I guess we should treat these as non fatal where appropriate.

## hyc | 2018-10-02T13:35:02+00:00
It was true at that time. In particular, it will be true as long as all data is accessed directly from LMDB and no info is cached locally in monerod's memory.

## moneromooo-monero | 2018-10-31T14:55:04+00:00
https://github.com/monero-project/monero/pull/4768 fixes it for me.
The two daemons will mine a different set of txes, but I don't think that's a problem.

## moneromooo-monero | 2018-12-13T13:03:14+00:00
+resolved


# Action History
- Created by: msgmaxim | 2018-10-02T04:49:14+00:00
- Closed at: 2018-12-13T13:09:14+00:00
