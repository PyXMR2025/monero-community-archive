---
title: RPC get_bulk_payments pagination
source_url: https://github.com/monero-project/monero/issues/2158
author: 34ro
assignees: []
labels:
- proposal
created_at: '2017-07-08T05:55:37+00:00'
updated_at: '2019-01-30T22:38:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, I think get_bulk_payments api needs pagination.
As increase number of transfer, getting all transfer without omission is difficult.
To use "min_block_height" is not good way to get all transfer in some cases.
If some transfer relayting to my address are in one block, 
If many transfer exist after min_block_height, and so on.

Please give me opinion.
  

# Discussion History
## khantahirx | 2017-08-15T08:27:04+00:00
Can you address this more extensively so that i can try and write something for it ?

## dEBRUYNE-1 | 2018-01-08T12:37:58+00:00
+proposal

## 34ro | 2018-01-09T15:06:02+00:00
If we deposit/withdraw much time, the size of transaction data will up to infinity.
For preventing client application from getting memory overflow, we need pagination for `get_bulk_payments`.

## emesik | 2019-01-30T22:38:54+00:00
There's `min_block_height` parameter which serves that purpose. Just check the current blockchain height when querying for payments and keep that value at the client side. Next time you ask for new blocks only.

# Action History
- Created by: 34ro | 2017-07-08T05:55:37+00:00
