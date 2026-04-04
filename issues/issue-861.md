---
title: max_out exceeded
source_url: https://github.com/monero-project/monero/issues/861
author: ManfredKarrer
assignees: []
labels: []
created_at: '2016-06-08T23:04:26+00:00'
updated_at: '2016-06-10T00:02:02+00:00'
type: issue
status: closed
closed_at: '2016-06-10T00:02:02+00:00'
---

# Original Description
I was missing incoming transactions to my wallet and got strange block heights (larger as on the explorer), so I deleted the data dir with the blockchain and started over again. After restart of bitmonerod (on Mac) i got that error: 
ERROR /DISTRIBUTION-BUILD/src/cryptonote_core/cryptonote_format_utils.cpp:148 max_out exceeded
It kept stuck for a while but then started syncing.

Edit: strange block heights -> was issues of blockexplorer (http://chainradar.com/xmr/blocks) on http://moneroblocks.info/ block height is like in bitmonerod.


# Discussion History
## moneroexamples | 2016-06-09T06:50:03+00:00
What do you mean by strange? Any exmaples?


## ManfredKarrer | 2016-06-09T10:23:36+00:00
@moneroexamples The height was lower at the blockexplorer (http://chainradar.com/xmr/blocks) than as the one at the bitmonerod. But was not an issue of bitmonerod, but of chainradar.
Now after a new sync of the complete blockchain I have all expected transactions in my wallet visible.
Seems before there was something locked up in the blockchain DB.


## moneromooo-monero | 2016-06-09T18:10:00+00:00
This can be ignored, and is fixed in master.


# Action History
- Created by: ManfredKarrer | 2016-06-08T23:04:26+00:00
- Closed at: 2016-06-10T00:02:02+00:00
