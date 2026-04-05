---
title: Pruned node db larger than full node
source_url: https://github.com/seraphis-migration/monero/issues/212
author: j-berman
assignees: []
labels: []
created_at: '2025-10-31T18:10:03+00:00'
updated_at: '2025-11-04T21:52:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported by @nahuhh

> I wonder why my "pruned" node is 73gb
> Yeah. I swear my other nodes arent pruned, and they are 50gb
> I think it was a full testnet node before
> Pruned it when it was like 16gb

```
2025-10-31 18:04:13.847 [P2P3]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3631 Pruned blockchain in 39 ms: 0.406273 MB (0.558594 MB) pruned in 72 records (143/1497373 4096 byte pages), 72/72 pruned records
```

> I have logs like this, so its still pruning, but its huge.
> my non-pruned nodes are smaller, yeah

# Discussion History
## jeffro256 | 2025-11-04T21:44:25+00:00
@nahuhh: did you run `monero-blockchain-prune` binary, the `prune_blockchain` command, or the node with the `--prune-blockchain` CLI flag?

## nahuhh | 2025-11-04T21:47:56+00:00
Cli flag

note: i had an old testnet db, synced and migrated, then backed it up. Not pruned.
Then copied this backup, and used the copy to run a --prune-blockchain node, as the full node was taking up too much space.
this pruned node grew wildly.

i have since done 2 things:
1. To (try) to reproduce, ive repeated the above: used another exact copy of the db, andnpruned it with --prune-blockchain
2. Synced a new node from scratch with --prune-blockchain

both nodes seem to be reasonably sized at 24.4gb (copyied / old db), and 27.6gb (fresh sync)

# Action History
- Created by: j-berman | 2025-10-31T18:10:03+00:00
