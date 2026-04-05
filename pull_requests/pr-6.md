---
title: initial database code
source_url: https://github.com/Cuprate/cuprate/pull/6
author: SyntheticBird45
assignees: []
labels:
- A-storage
created_at: '2023-03-08T18:43:01+00:00'
updated_at: '2024-05-27T01:08:36+00:00'
type: pull_request
status: merged
closed_at: '2023-04-20T17:20:32+00:00'
merged_at: '2023-04-20T17:20:32+00:00'
---

# Original Description
Initial pull request for implementing database-related code. As specified in the crate, there is two storage engine planned. MDBX (Russian database with insane performance, used by reth) and HSE (Heterogeneous Storage Engine for Micron, optimized for ssd & random writes & reads)

- [x] Generic Cursors
- [x] DUPSORT & DUPFIXED support
- [x] All Tables 
- [x] DB Builder
- [x] Blockchain interfaces
- [ ] Txpool interfaces
- [x] MDBX Implementation
- [ ] Batch write
- [ ] Investigating async

# Discussion History
## Boog900 | 2023-04-19T17:52:06+00:00
This is not how you calculate the blocks hash, monero-rs has a method on `Block` called`.id` to get the blocks id (hash)

## Boog900 | 2023-04-19T17:59:27+00:00
typo `lock`

## Boog900 | 2023-04-19T18:01:28+00:00
i think this should be (height -1 )

## Boog900 | 2023-04-19T18:04:02+00:00
blk_height -1

## Boog900 | 2023-04-19T18:04:39+00:00
height -1 

## Boog900 | 2023-04-19T18:27:58+00:00
We will need a function `calculate_prunable_hash` to calculate the hash as v1 transactions don't have a prunable hash + miner txs use an empty hash: 

https://github.com/Cuprate/monero-rs/blob/b1c35403f4ed5933e67f69826fb371bc8189f3ef/src/blockdata/transaction.rs#L813

## Boog900 | 2023-04-19T18:31:47+00:00
can you update the comment to: 

```
// Checking to see if the database is pruned and inserting into table::txsprunabletip accordingly
```

## Boog900 | 2023-04-19T18:37:03+00:00
~~this needs to check if the input is a coinbase input~~

mb this does check 

## Boog900 | 2023-04-19T18:55:19+00:00
This comment should probably be changed to: 
```
/// `altblock` is a table that permits the storage of blocks from an alternative which may cause a re-org. These blocks can be fetch by their corresponding hash.
```

## Boog900 | 2023-04-19T18:56:08+00:00
can we call the table txspruned 

## Boog900 | 2023-04-19T18:59:48+00:00
This is defined in monero-rs


## Boog900 | 2023-04-20T15:20:03+00:00
This can never be true, as you are using the height of our chain not the height/ id of the block 

## Boog900 | 2023-04-20T15:27:41+00:00
this should be:
    /// `txp`: is a tuple containing the transaction and its prune-able blob.

## Boog900 | 2023-04-20T15:28:23+00:00
can we split the tx and the tx prunable blob into 2 arguments 

## Boog900 | 2023-04-20T15:33:28+00:00
Nit: we could do `Vec::with_capacity(capacity)` here


## Boog900 | 2023-04-20T15:38:36+00:00
this function name is a bit ambiguous 

## Boog900 | 2023-04-20T15:40:20+00:00
forgot to remove this? : )


## Boog900 | 2023-04-20T15:44:17+00:00
It may be good to add a comment here stating that you will be adding on the previous `num_rct_outs` in `add_block_data` 

## SyntheticBird45 | 2023-04-20T15:52:16+00:00
I think the height function is the issue. I'm returning the number of entries not the last block height. I should substract one to the result and it would corret everything

## Boog900 | 2023-04-20T15:56:38+00:00
the height function gets the blockchain height which is 1 more than the top blocks height as the blockchain counts from 1 but blocks count from 0, so I think the height function is correct but the main thing wrong with this is we are testing our own height not the incoming blocks 

## SyntheticBird45 | 2023-04-20T16:02:01+00:00
A `monero::blockdata::Transaction` represent 344 bytes in memory. I propose we suppose that this function is used with at least 4 requested txs. It make the capacity=1376.

## SyntheticBird45 | 2023-04-20T16:04:04+00:00
What name should we use ?
- is_built
- verify
- is_valid

## SyntheticBird45 | 2023-04-20T16:08:50+00:00
Alright I'll fix it. I though the blockchain height was the top blocks height

## SyntheticBird45 | 2023-04-20T16:18:34+00:00
Replaced the check with the blockhash table.

## Boog900 | 2023-04-20T16:25:58+00:00
`check_all_tables_exist` 


## Boog900 | 2023-04-20T16:29:36+00:00
If, for example, a peer needed a block we would need to call this function with all the tx hashes to get every tx in the block so i don't think a limit would be a good idea 

## SyntheticBird45 | 2023-04-20T16:31:48+00:00
It's just an arbritrary choice. There'll be no limit. I'm just conjecturing what would be the good capacity here

## Boog900 | 2023-04-20T16:35:05+00:00
the length of the inputted `hash_list`

## SyntheticBird45 | 2023-04-20T16:43:21+00:00
Oh alright I was thinking in bytes, but I forgot that the capacity is in monero::Transaction

# Action History
- Created by: SyntheticBird45 | 2023-03-08T18:43:01+00:00
- Merged at: 2023-04-20T17:20:32+00:00
