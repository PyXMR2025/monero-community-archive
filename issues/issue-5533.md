---
title: '"output received" message pops up over and over, refresh has no effect'
source_url: https://github.com/monero-project/monero/issues/5533
author: aStableTripod
assignees: []
labels: []
created_at: '2019-05-10T15:07:44+00:00'
updated_at: '2019-05-10T15:31:42+00:00'
type: issue
status: closed
closed_at: '2019-05-10T15:31:42+00:00'
---

# Original Description
There seems to be a difference between the mechanism that makes the message pop up (which seems to include mempool txs) and the refresh command (which seems to not include them).

When you receive new outputs from a tx, you get the following message in the CLI wallet:

> Password needed (output received) - use the refresh command

If the tx is still in the mempool, "refresh" does nothing and the message pops up again and again, until it is included in a block, at which point it works as intended.

So either the message should not be displayed for mempool txs, or refresh should include mempool txs. Otherwise this behaviour makes it seem like the wallet is not working correctly, confusing people.



# Discussion History
## moneromooo-monero | 2019-05-10T15:17:23+00:00
Did you try this with current master ? AFAIK this is fixed.

## aStableTripod | 2019-05-10T15:31:39+00:00
You're right, this is fixed in master, my bad for not testing that in the first place.

# Action History
- Created by: aStableTripod | 2019-05-10T15:07:44+00:00
- Closed at: 2019-05-10T15:31:42+00:00
