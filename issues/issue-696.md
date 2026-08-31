---
title: Tx-pool race(s)
source_url: https://github.com/Cuprate/cuprate/issues/696
author: Boog900
assignees:
- Boog900
labels:
- C-bug
created_at: '2026-08-30T17:35:22+00:00'
updated_at: '2026-08-30T17:35:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There are multiple tx-pool races that although not critical should really be fixed. 

*NOTE: These don't cause consensus issues. They make pool state momentarily inconsistent: we may drop a valid tx as invalid, or keep a spent tx in the pool (and re-relay it)*

## Txs can race with new blocks.

Because tx verification happens outside the tx-pool manger we could accept a tx as valid add it to the queue for a pool, then a new block comes in which spends one of the tx key images. At this point the pool could be told about the block before the tx causing the pool to add an already spent tx.

## Context cache could be inconsistent with the DB  

When verifying a tx the cache could be ahead or behind the DB.




# Discussion History
# Action History
- Created by: Boog900 | 2026-08-30T17:35:22+00:00
