---
title: wrong miner tx in block in logs
source_url: https://github.com/seraphis-migration/monero/issues/221
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-11-07T02:24:28+00:00'
updated_at: '2025-12-15T18:21:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported by a few people in the stressnet channel:

```
2025-11-07 02:12:18.998	I Synced 2870785/2870970 (99%, 185 left)
2025-11-07 02:12:19.109	E wrong miner tx in block: <fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596>, b.miner_tx.vin.size() != 1
2025-11-07 02:12:56.387	I Synced 2870788/2870970 (99%, 182 left)
2025-11-07 02:12:56.471	E wrong miner tx in block: <fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596>, b.miner_tx.vin.size() != 1
2025-11-07 02:13:20.441	I Synced 2870791/2870970 (99%, 179 left)
2025-11-07 02:13:20.537	E wrong miner tx in block: <fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596>, b.miner_tx.vin.size() != 1
```

The node who sends it gets banned.

# Discussion History
## jeffro256 | 2025-11-08T06:31:25+00:00
My node also receives this `fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596` transaction every several days.

## jeffro256 | 2025-11-08T06:31:49+00:00
I'll run a patch on my node which dumps the block 

Nov 14 edit: still running, it hasn't experienced one of these since i've been running the patch

## Cyrix126 | 2025-11-23T11:57:08+00:00
the same error (same block hash) was reported in 2020, so it's likely not related to recent changes.
https://github.com/monero-project/monero/issues/6419

## Boog900 | 2025-11-23T14:36:36+00:00
As a shot in the dark after seeing that this happened before stressnet I checked what the hash of a block with fields that are defaulted would be, and its this same hash: `fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596`

rust code with monero-oxide (we recently made the `miner_transaction` private to ensure it has a miner input so you need to either use an old version or  edit monero-oxide to make that field public):

```rust
  let block = Block {
    header: BlockHeader {
      hardfork_version: 0,
      hardfork_signal: 0,
      timestamp: 0,
      previous: [0; 32],
      nonce: 0,
    },
    miner_transaction: Transaction::<NotPruned>::V1 {
      prefix: TransactionPrefix {
        additional_timelock: Timelock::None,
        inputs: vec![],
        outputs: vec![],
        extra: vec![],
      },
      signatures: vec![],
    },
    transactions: vec![],
  };

  println!("{:?}", hex::encode(block.hash()));
```


## Cyrix126 | 2025-11-24T11:00:16+00:00
level 4 log catching it:

```
[P2P8]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:1612 Blockchain::get_current_cumulative_block_weight_limit
[P2P8]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:4989 Blockchain::add_new_block
[P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:407  mdb_txn_safe: destructor
[P2P8]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:3153 Blockchain::have_block_unlocked
[P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3747 BlockchainLMDB::block_exists
[P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3758 Block with hash fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596 not found in db
[P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:5891 BlockchainLMDB:: get_alt_block
[P2P8]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:820  Blockchain::get_tail_id
[P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:4258 BlockchainLMDB::top_block_hash
[P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:4288 BlockchainLMDB::height
[P2P8]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:4207 BlockchainLMDB::get_block_hash_from_height
[P2P8]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:2036 Blockchain::handle_alternative_block
[P2P8]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:1027   wrong miner tx in block: <fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596>, b.miner_tx.vin.size() != 1
[P2P8]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2043 Block with id: fb877ea3400f731c2b948e87655368f1c0486e3c114bb3f8f3839bec1b2f9596 (as alternative), but miner tx says height is 0.

```

EDIT: using this build: https://github.com/j-berman/monero/actions/runs/19531208476

# Action History
- Created by: j-berman | 2025-11-07T02:24:28+00:00
