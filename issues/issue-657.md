---
title: Pruning for Cuprate
source_url: https://github.com/Cuprate/cuprate/issues/657
author: Boog900
assignees:
- p4xxus
labels:
- C-proposal
created_at: '2026-07-23T18:03:16+00:00'
updated_at: '2026-07-25T14:17:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue documents a way to add pruning to Cuprate.

# Setting a pruned node.

monerod supports pruning a node while it is running. I don't think we need to support that. The 2 ways to make a node pruned should be a command line arg (i.e `--prune`) and a new config value in the main config file (`prune = true`).

Once a node is pruned it cannot be un-pruned so setting the prune config value to `prune = false` should do nothing. 

# Keeping track of pruning state

A metadata file should be added to the DB. This metadata file will hold 2 things: the database version and the pruning seed. 

This file should be located in the DB directory, its format should just be 12 bytes, the first 8 being the version, the next 4 the pruning seed. In `BlockchainDatabase::open_with_fjall_database` this file should be loaded before doing anything else, if not present the values of the version and pruning seed should be set to their default and a file should be created.

If the metadata file says the DB is not pruned and the config says it should be then prune the DB.

# Pruning the DB

Firstly we should change the prunable tapes type here: https://github.com/Cuprate/cuprate/blob/d57d59dde47125b80bc87c1b5cdcf200fccc78cd/storage/blockchain/src/database.rs#L135

to:

```rust
    pub(crate) prunable_blobs: Vec<Option<tapes::BlobTape>>,
```

When pruning we need to randomly generate a pruning stripe, we need to then update the metadata file with this stripe before doing anything. We then delete the tapes file for all other stripes from the one we selected. 

From the stripe we generate a pruning seed, which we then expose to the rest of Cuprate so it can pass it to P2P etc.

Where we currently use `prunable_blobs` we need to handle the case where data is requested for a tape we don't have, most likely we should just return an error.

# Tip blocks

monerod will store the top 5500 blocks unpruned, even if they are in a stripe we should prune, we need to handle this. 
A way to handle this is to make a new fjall keyspace for the prunable blobs of the txs in the top 5500 blocks and then when a new block is added we look at the block 5501 from the top and remove its txs from the new keyspace. 

All V2 prunable blobs should be added to this keyspace, if we are pruning, for simplicity. We need to fill this table in before pruning a non-pruned node too.

All places that look for prunable blobs will need to look in this new keyspace if they are close to the top of the chain.

# Make consistent

`BlockchainDatabase::make_consistent` is the way we currently make sure the tapes and fjall are in sync on startup. With pruning this is harder as prunable data could be missing from a new block in the tapes so cannot be added to fjall.

To fix this we need to pop some blocks from the tapes, up to where we have enough data. This probably looks like just always popping the top 5500 blocks from the tapes if we are pruned and the databases are out of sync. Then just having the tip prunable blob keyspace empty to repopulate with blocks once they are downloaded again.

# Discussion History
## p4xxus | 2026-07-24T20:02:03+00:00
I am working on it btw, just to avoid duplicate work

# Action History
- Created by: Boog900 | 2026-07-23T18:03:16+00:00
