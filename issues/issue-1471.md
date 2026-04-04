---
title: Wrong balance on wallet reorg
source_url: https://github.com/monero-project/monero/issues/1471
author: moneromooo-monero
assignees: []
labels:
- bug
created_at: '2016-12-17T22:10:03+00:00'
updated_at: '2025-12-19T17:43:04+00:00'
type: issue
status: closed
closed_at: '2025-12-19T16:47:43+00:00'
---

# Original Description
When the wallet reorganizes, a few things conspire to produce a potentitally wrong resulting balance.

If a spent output's spend height is unknown, it's set to 0, so will not be reset to unspent if it was really spent after the reorg height. This happens if rescan_spent is called, since rescan_spent doesn't give any information about spend height. This is not stored in the blockchain, so a full rescan would be needed to get this information, which is impractical.

In turn, it means the only way to get a correct balance is to re-run rescan_spent after a reorg, but that will compound the problem for next reorg.

One could run an automatic rescan_spent, but the daemon might not be trusted, we don't have the flag in the detach function.


# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:29:00+00:00
+bug

## selsta | 2025-12-19T16:47:43+00:00
There was a lot of reorg related testing done recently on stressnet leading to some bugs being fixed, I assume this is resolved.

## selsta | 2025-12-19T17:42:53+00:00
According the to @j-berman this is not solved until https://github.com/monero-project/monero/pull/10081 is merged, but we have another issue open tracking this so I'll keep this one closed.

# Action History
- Created by: moneromooo-monero | 2016-12-17T22:10:03+00:00
- Closed at: 2025-12-19T16:47:43+00:00
