---
title: Dust
source_url: https://github.com/monero-project/monero-site/issues/2
author: davidlatapie
assignees: []
labels: []
created_at: '2015-02-23T11:31:27+00:00'
updated_at: '2017-10-25T23:00:08+00:00'
type: issue
status: closed
closed_at: '2017-10-25T23:00:08+00:00'
---

# Original Description
**For Moneropedia entry**

Dust is a generic term given to amount of XMR so low that
1) they have no meaningful value
2) they are very expensive to spend (the transaction fees may be 50% or even 200% of the dust itself)
## The dangers of dust

The dust issue happens in every cryptocurrency and can be used as an attack vector, to bloat the blockchain (much like many 20 bytes files on a file system can bloat a filesystem by using many more clusters than necessary). Dust issue can be mitigated with smart fine-tuning. In the case of Monero, the original pool software had too low a threshold for payment, resulting on a lot of dust. Later, an dust attack was even perpetrated.
## The solution to dust

[MRL-0004](https://lab.monero.cc/pubs/MRL-0004.pdf) implements a solution for dealing with dust in an elegant way: new outputting rules. "No new dust will be created in the system, and dust will only be removed from the system over time"


# Discussion History
## QuickBASIC | 2017-08-31T12:19:43+00:00
@davidlatapie Is this a request to add a Moneropedia entry or was this intended for a different repo?

## QuickBASIC | 2017-10-21T21:32:20+00:00
+moneropedia

## QuickBASIC | 2017-10-25T18:42:07+00:00
There were two main reasons outputs were called dust:

- small outputs (typically well below the fee per kB)
- complex looking amounts, such 0.000013852456 that are from before RingCT was added.

The second issue is all but resolved with RingCT, since those outputs are slowly being used up and seeing a 0-mixin transaction is relatively rare nowadays.

The first issue was a much bigger problem before most pools started doing payouts at a certain threshold (some were even doing payouts per block), but less of an issue now. 

Because the issue is all but gone, I feel like adding a Dust page to the Moneropedia might be more confusing than helpful for new users.


## QuickBASIC | 2017-10-25T22:52:14+00:00
+stale
+resolved

# Action History
- Created by: davidlatapie | 2015-02-23T11:31:27+00:00
- Closed at: 2017-10-25T23:00:08+00:00
