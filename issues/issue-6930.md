---
title: monero-blockchain-prune failure + specify logfile
source_url: https://github.com/monero-project/monero/issues/6930
author: lkjhkj
assignees: []
labels: []
created_at: '2020-10-23T05:54:39+00:00'
updated_at: '2021-10-06T03:10:23+00:00'
type: issue
status: closed
closed_at: '2021-10-06T03:10:23+00:00'
---

# Original Description
Trying to use the `monero-blockchain-prune`, aborted the process in the middle of the job, then start it again and get this:
```
I Initializing source blockchain (BlockchainDB)
I Loading blockchain from folder "/home/user/nodes/monero/datadir/lmdb" ...
W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
I source blockchain storage initialized OK
I Loading blockchain from folder "/home/user/nodes/monero/datadir/lmdb-pruned" ...
W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
W Attempt to get timestamp from height 2213733 failed -- timestamp not in db
E Exception at [Pruning error], what=Attempt to get timestamp from height 2213733 failed -- timestamp not in db
```
`--log-level=4` is basically this spanning for 3500 lines:
```
T BlockchainLMDB::height
T BlockchainLMDB::get_block_blob_from_height
```
Does that mean that all's in vain and I'll have to start from the beginning?
(The node is running on a VPS with SSD, not HDD.)

Another question: how to specify the logfile for `monero-blockchain-prune`? 

# Discussion History
## moneromooo-monero | 2020-10-24T11:56:50+00:00
It looks like you'll have to restart, yes. You might be better off syncing from monerod again with --prune-blockchain, this will not break if it dies in the middle, and will also be faster than using monero-blockchain-prune on a fully synced DB. Looks like you can't change log file name with this tool.

## lkjhkj | 2020-10-24T12:35:48+00:00
As per commit message of https://github.com/monero-project/monero/commit/b750fb27b0f20e9443827732b69a504a76036430, the `monerod --prune-blockchain` does not actually make the DB smaller, but only prevents further growth, so if my intention was to compress the DB, would it make sense to use use that flag? Or did anything change in this relation since then? 

## moneromooo-monero | 2020-10-24T14:25:55+00:00
If you want to compress, monerod --prune-blockchain would not help on an already synced chain. However, a combination of --prune-blockchain and mdb_copy should do what you want. 
monerod --prune-blockchain on a full already synced chain is about the same as monero-blockchain-prune though I think.

# Action History
- Created by: lkjhkj | 2020-10-23T05:54:39+00:00
- Closed at: 2021-10-06T03:10:23+00:00
