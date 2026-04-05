---
title: Wallet complains about double spends after some use
source_url: https://github.com/seraphis-migration/monero/issues/185
author: nahuhh
assignees: []
labels: []
created_at: '2025-10-20T17:03:43+00:00'
updated_at: '2025-12-17T00:17:17+00:00'
type: issue
status: closed
closed_at: '2025-12-17T00:17:17+00:00'
---

# Original Description
i have this issue from time-to-time. Sometimes can go days without encountering, others (like below) i can get lucky and have it happen quickly. Balance before and after rescan_spent differ, and the rescan shows that some spent KI are not being marked as spent.

1. Send txs
2. Double spend error (04:26 L35193)
3. rescan_spent (04:30 L43255)
4. cont sending txs
5. Double spend error (05:23 L112595)

Log level 2 from wallet-rpc attached
[double-spend.log.gz](https://github.com/user-attachments/files/23005467/double-spend.log.gz)

# Discussion History
## j-berman | 2025-10-22T01:05:23+00:00
Any chance you recall manually relaying `87260dbf8c3b0b5389946f55a2ff3ea4afa7b1c3ab9e979dd69c22142a7fe33c` from your node / might it have been one of those that failed from #163?

## j-berman | 2025-10-22T01:27:45+00:00
What's happening in the logs:

1) Wallet constructs tx `87260dbf8c3b0b5389946f55a2ff3ea4afa7b1c3ab9e979dd69c22142a7fe33c` and successfully submits it to the daemon (other tx hashes fit this too in the logs).
2) The wallet doesn't see the tx in the daemon's pool after 5 mins and marks it failed + marks the key image used in the tx as unspent.
3) Subsequent tx construction attempts use the key image from that tx.
4) Looks like the daemon has the tx in its pool still, and so any subsequent tx using that key image fails with a double spend error.
5) `rescan_spent` identifies the key image is spent and it gets marked spent, and the wallet stops using that output.
6) The tx eventually enters the chain in block 2858569, and the wallet identifies it there too.

Perhaps there is an issue with the incremental pool fetching logic. The daemon should have showed the wallet that the tx was added to its pool after step 1 during the refresh that occurs at `04:17:53.002`.

## nahuhh | 2025-10-22T01:58:05+00:00
> Any chance you recall manually relaying `87260dbf8c3b0b5389946f55a2ff3ea4afa7b1c3ab9e979dd69c22142a7fe33c` from your node / might it have been one of those that failed from #163?

Definitely not. I didn't touch anything while the test was running

> The wallet doesn't see the tx in the daemon's pool after 5 mins and marks it failed + marks the key image used in the tx as unspent.

Which is strange

## j-berman | 2025-12-04T03:34:23+00:00
Repeating @nahuhh's [comment here](https://github.com/seraphis-migration/monero/pull/253#issuecomment-3609638211):

> if the node which the wallet is connected to drops the tx, the wallet ends up in a bad state. Further spends from the wallet error as double spends, even though the node doesnt have the tx. This is currently impossible to reconcile w/o issuing a `rescan_spent`

This could explain [this sequence](https://github.com/seraphis-migration/monero/issues/185#issuecomment-3430133704) of events! If the daemon immediately drops the tx after step 1, that could explain the subsequent steps.

Then it's possible the tx may have gotten relayed back to the node from another node. Thus #253 may help prevent the tx from entering the node in the first place.

However, it's still possible for the tx to get removed from the node after submitting the tx successfully, and then relayed back to he node, so the wallet still would need to be able to handle that case.

It looks like the wallet's `accept_pool_tx_for_processing` may need to be modified for that edge case, and this circumstance tested/confirmed.

## j-berman | 2025-12-11T22:16:12+00:00
Tx removed from the node's in-memory container but still in the db explains why the node doesn't serve the tx to the wallet when the wallet refreshes, but the node still rejects double spends. Tx removed from the in-memory container but still in the db was caused by https://github.com/seraphis-migration/monero/issues/192#issuecomment-3628332952.

I think the original issue demonstrated in [these logs](https://github.com/seraphis-migration/monero/issues/185#issue-3533219789) is explained by that incorrect behavior in the node (fixed by #251), but I've still been able to repro a distinct cause of double spend errors in this case:

> it's still possible for the tx to get removed from the node after submitting the tx successfully, and then relayed back to he node, so the wallet still would need to be able to handle that case.

Working on that now.

## j-berman | 2025-12-17T00:17:17+00:00
Fixed by #251 and #261

# Action History
- Created by: nahuhh | 2025-10-20T17:03:43+00:00
- Closed at: 2025-12-17T00:17:17+00:00
