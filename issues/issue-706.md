---
title: 'DB corruption '
source_url: https://github.com/monero-project/monero/issues/706
author: iamsmooth
assignees: []
labels: []
created_at: '2016-03-07T08:59:35+00:00'
updated_at: '2016-12-16T15:03:09+00:00'
type: issue
status: closed
closed_at: '2016-12-16T15:03:09+00:00'
---

# Original Description
We've had several reports of DB corruption, mostly on Windows I think, that occur when the system crashes.

Perhaps this is due to less safe/async DB modes? If so we should consider switching those off after initial sync, when performance is most critical, so that later crashes don't corrupt the DB.


# Discussion History
## fluffypony | 2016-03-07T09:01:32+00:00
I've had DB corruption on OS X during normal shutdown on testnet and mainnet, as discussed on IRC. It was mostly solved by popping blocks, perhaps we should have a rollback strategy if the database is in an inconsistent state? Like rollback 30 blocks or something, and try again.


## iamsmooth | 2016-03-07T09:02:11+00:00
I think it is better to fix the DB so it doesn't corrupt. That's the purpose of a DB right?


## fluffypony | 2016-03-07T09:04:17+00:00
True - I think the readtxn changes make it more robust, since everything is wrapped in a transaction and rolls back if it fails or is interrupted? That was my understanding anyway.


## iamsmooth | 2016-03-07T09:04:59+00:00
Makes sense, maybe this is already fixed then.


## hyc | 2016-03-07T17:15:53+00:00
wrapping readtxns doesn't affect robustness, readtxns don't make changes anyway. What's important is to properly wrap write ops in an appropriate writetxn. I get the impression that reorgs are not using a batch properly to enclose all of their deletes/etc. so interrupting a reorg can leave things inconsistent.

To be more specific - I had an interrupted reorg, and on restart some particular txn could not be found any more and I had to wipe the entire DB and start over. I kind of wonder if maybe it should have simply succeeded since the txn it wanted to delete was already gone. That is, on restart, it still tried to do the reorg.


## iamsmooth | 2016-03-08T06:16:08+00:00
It's not really clear a reorg needs to be a single transaction (batch) to operate properly. As long as it is implemented as a sequence of pop_blocks followed by add_blocks, any sequence of these (assuming they are individually atomic transactions) should leave the db consistent.


## hyc | 2016-03-08T08:00:26+00:00
Yeah, I see. popping a block removes all of the block's transactions in a single DB writetxn anyway, so this shouldn't have been the cause of whatever problem I saw.


## hyc | 2016-03-19T12:51:53+00:00
I reproduced a corruption on the current 0.9.2, got a SEGV while syncing and then the DB was corrupted on next restart. The block_\* tables all have 165824 entries but the hf_versions table has only 165823, so hf_versions didn't get updated in the same DB txn as the block info.
[fail.txt](https://github.com/monero-project/bitmonero/files/180814/fail.txt)

Here's the loglevel 3 output right up to the crash:
[log.txt](https://github.com/monero-project/bitmonero/files/180815/log.txt)
It shows that the thread on P2P4 was starting a checkpoint check, while the thread on P2P3 was starting to add a new block. Unfortunately Blockchain::check_against_checkpoints() isn't taking the CRITICAL_REGION_LOCAL(m_blockchain_lock) so both threads wind up using the same write txn. Then one of them commits while the other thread is still using the txn, and SEGV happens. And the commit happened before add_block was done, so hf_versions didn't get updated in that txn.


## iamsmooth | 2016-04-08T01:45:33+00:00
Are all the known/reported sources of corruption fixed now?

Maybe we can close this issue and open another one specifically on the general issue of sync-vs-async?


## luigi1111 | 2016-12-15T17:58:51+00:00
@iamsmooth Yes let's do that (I assume that is still relevant).

## ghost | 2016-12-15T19:59:07+00:00
@hyc how should we proceed from here?

## hyc | 2016-12-16T02:22:33+00:00
I agree with @iamsmooth we can close this one and start a new issue.

As for a general solution - that's still not clear. My previous suggestion was that we still default to "fast" during initial sync, and step down to "safe" after the node is synchronized. Unfortunately

1. We still can't reliably tell when the node is sync'd - a previous patch for that actually just caused more spurious sync'd messages.
2. It doesn't really help those Windows users whose PCs crashed during syncing. (Then again, I'm not sure we should be trying to work around users with broken hardware.)

## luigi1111 | 2016-12-16T15:03:09+00:00
#1463 

# Action History
- Created by: iamsmooth | 2016-03-07T08:59:35+00:00
- Closed at: 2016-12-16T15:03:09+00:00
