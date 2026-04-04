---
title: Is there method to return tx hash, or entire tx, using tx_id?
source_url: https://github.com/monero-project/monero/issues/1978
author: moneroexamples
assignees: []
labels: []
created_at: '2017-04-15T05:26:46+00:00'
updated_at: '2017-04-15T22:46:50+00:00'
type: issue
status: closed
closed_at: '2017-04-15T22:46:50+00:00'
---

# Original Description
Method: 
```
uint64_t BlockchainLMDB::add_transaction_data(const crypto::hash& blk_hash, const transaction& tx, const crypto::hash& tx_hash)
```
https://github.com/monero-project/monero/blob/master/src/blockchain_db/lmdb/db_lmdb.cpp#L744

returns uint64_t `tx_id` of a transaction. But what if I have the `tx_id`, and what to return corresponding tx? Currently one can get txs based on their hashs. Hash is much larger than tx_id (32 vs 8 bytes) and using `tx_id` in external databases to identify a tx can save a lot of space.

Is there some method that gets tx_hash, or entire tx, using `tx_id`? Cant find anything, but maybe looking in wrong place?


# Discussion History
## moneromooo-monero | 2017-04-15T07:33:15+00:00
tx_id is badly named here, it's an index, and it's internal to the LMDB implementation of the monero blockchain.


## hyc | 2017-04-15T16:31:39+00:00
But you don't really need a special method to look it up, if you already have the blockchain DB open yourself. Just use mdb_cursor_get().

## moneroexamples | 2017-04-15T22:46:50+00:00
@hyc yes, I can read it myself, though was hoping for some original monero function for it, because there are functions returning tx_id having a tx_hash (tx_exist()), so I thought there would be something opposite as well.

# Action History
- Created by: moneroexamples | 2017-04-15T05:26:46+00:00
- Closed at: 2017-04-15T22:46:50+00:00
