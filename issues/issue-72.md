---
title: 'TODO: Save block content hash and # of txs in `mdb_block_info` in next DB
  migration'
source_url: https://github.com/seraphis-migration/monero/issues/72
author: jeffro256
assignees: []
labels: []
created_at: '2025-07-25T19:50:10+00:00'
updated_at: '2025-07-26T19:35:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
To support efficient header-only sync in the future, save the block content hash https://github.com/seraphis-migration/monero/blob/f3083d5ce9df934b79af601c2ddc63650fc87348/src/cryptonote_basic/cryptonote_format_utils.cpp#L1871-L1892 and number of transactions in the block in `mdb_block_info`. This would allow the node to serve the block hashing blob https://github.com/seraphis-migration/monero/blob/f3083d5ce9df934b79af601c2ddc63650fc87348/src/cryptonote_basic/cryptonote_format_utils.cpp#L1725-L1732 by just copying the block header, block content hash, and number of transactions. By contrast, to do this today, would require the node to de-serialize the whole block, including the miner transaction, and transaction hashes list, and calculate the transaction hash tree hash. Merging this change in with the current FCMP++ database migration (v5 -> v6) prevents the need to migrate again in the future.

We could also remove the number of transactions from the block hashing blob for headers of major version >= 17, and not store the number of transactions in `mdb_block_info`. I personally don't know why the number of transactions is stored directly in the block hashing blob. Maybe it made the original author feel safer about hash collisions with the transaction hash tree code (which previously had bugs)? Would be nice to know the intention before removing it...

This change would add an additional 32 + 8 = 40 bytes per block to the DB.

# Discussion History
## j-berman | 2025-07-25T20:28:27+00:00
Imo that kind of migration would be fine in the future when we have client code that would benefit from it. It would run pretty fast, and people would be excited about it too. It's also not too difficult for users to avoid downtime from a migration if it's a requirement: copy the db manually, run the migration pointing to the copy, get that separate copy synced, then restart pointing to the copy.

> We could also remove the number of transactions from the block hashing blob for headers of major version >= 17

This sounds reasonable to me. Maybe @cryptozoidberg has thoughts?

## cryptozoidberg | 2025-07-26T19:35:08+00:00
> 
> > We could also remove the number of transactions from the block hashing blob for headers of major version >= 17
> 
> This sounds reasonable to me. Maybe [@cryptozoidberg](https://github.com/cryptozoidberg) has thoughts?

Should be all right, i honestly don't remember now why number of transactions was  originally included there

# Action History
- Created by: jeffro256 | 2025-07-25T19:50:10+00:00
