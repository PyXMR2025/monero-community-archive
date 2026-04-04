---
title: 'peer with bad top block below checkpoint '
source_url: https://github.com/monero-project/monero/issues/122
author: iamsmooth
assignees: []
labels:
- question
created_at: '2014-09-06T23:43:58+00:00'
updated_at: '2022-07-20T01:22:42+00:00'
type: issue
status: closed
closed_at: '2022-07-20T01:22:08+00:00'
---

# Original Description
2014-Sep-06 16:34:25.234589 [P2P1]Remote top block height: 202659, id: <78fbbca5edea204b3ff5e92fbe6413029a32849ccad434481cc9e2b944244845>

This peer is definitely below a checkpoint and probably has a block that is not on the main chain, so it is of no use to us, and in fact enough of those peers would fill our peer slots and stall the node. On the other hand, dropping it may prevent that peer from syncing, assuming it is not malicious or bugged (the latter appears to be the case after the 612 attack).

What should we do with it, if anything? Maybe drop if more than 1/2 of allowed max peers in that state or something.


# Discussion History
## iamsmooth | 2014-09-06T23:47:38+00:00
Maybe drop these after a timeout, if that doesn't already happen.


## dEBRUYNE-1 | 2018-01-08T12:49:36+00:00
+question

## Cactii1 | 2022-07-20T01:05:38+00:00
This looks like it has been fixed and this issue should be closed.

## selsta | 2022-07-20T01:22:42+00:00
The code has changed a lot since 2014, peers cycle now too so I don't think this is still an issue.

# Action History
- Created by: iamsmooth | 2014-09-06T23:43:58+00:00
- Closed at: 2022-07-20T01:22:08+00:00
