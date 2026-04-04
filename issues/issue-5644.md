---
title: 'monerod: Failed to delete transaction prunable data'
source_url: https://github.com/monero-project/monero/issues/5644
author: ukfhVp0zms
assignees: []
labels: []
created_at: '2019-06-14T23:22:51+00:00'
updated_at: '2022-03-16T15:48:56+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:48:56+00:00'
---

# Original Description
Receiving an error when trying to prune blockchain data

Manjaro Linux

`~ >>> monerod --hide-my-port --prune-blockchain`
`2019-06-14 23:06:37.651 I Monero 'Boron Butterfly' (v0.14.1.0-release)`
`2019-06-14 23:06:37.651 I Initializing cryptonote protocol...`
`2019-06-14 23:06:37.651 I Cryptonote protocol initialized OK`
`2019-06-14 23:06:37.651 I Initializing p2p server...`
`2019-06-14 23:06:43.129 I p2p server initialized OK`
`2019-06-14 23:06:43.130 I Initializing core RPC server...`
`2019-06-14 23:06:43.130 I Binding on 127.0.0.1:18081`
`2019-06-14 23:06:43.141 I Generating SSL certificate`
`2019-06-14 23:06:43.243 I core RPC server initialized OK on port: 18081`
`2019-06-14 23:06:43.243 I Initializing core...`
`2019-06-14 23:06:43.243 I Loading blockchain from folder /home/xxx/.bitmonero/lmdb ...`
`2019-06-14 23:06:43.289 I Loading checkpoints`
`2019-06-14 23:06:43.653 I Pruning blockchain...`
`2019-06-14 23:08:04.046 W Failed to delete transaction prunable data: MDB_TXN_FULL: Transaction has too many dirty pages - transaction too big`
`2019-06-14 23:08:04.055 F Uncaught exception! Failed to delete transaction prunable data: MDB_TXN_FULL: Transaction has too many dirty pages - transaction too big`
`2019-06-14 23:08:04.105 I Deinitializing core RPC server...`
`2019-06-14 23:08:04.107 I Deinitializing p2p...`
`2019-06-14 23:08:08.111 I Deinitializing core...`
`2019-06-14 23:08:09.269 I Stopping cryptonote protocol...`
`2019-06-14 23:08:09.269 I Cryptonote protocol stopped successfully`

# Discussion History
## moneromooo-monero | 2019-06-15T09:07:51+00:00
I'll need to have checkpoints to commit db txns along the way. In the meantime, you can use monero-blockchain-prune, which should not have this problem.

## moneromooo-monero | 2019-06-15T09:51:57+00:00
https://github.com/monero-project/monero/pull/5647 should also fix it.

## BKdilse | 2019-06-20T07:28:11+00:00
I used monero-blockchain-prune to prune my DB, and it went through fine, however, once I restarted the daemon, I got some errors to do with tx/block not in DB (I didn't get a chance to note this, sorry), priority was to get my pool back up, as it would not sync past the last block it was on, even waited 15 mins.  I am currently re-synching from scratch, using --prune-blockchain.

## moneromooo-monero | 2019-06-20T09:07:52+00:00
If it was "Error retrieving blocks, missed X transactions for block with hash Y", then it's fine, it's old nodes not knowing you don't have that data and asking for it anyway.

## BKdilse | 2019-06-20T09:10:38+00:00
No, it wasn't that, sorry, i'm not being much help by not grabbing the logs, it was early in the morning, I was tired, and just wanted pool fixed :(

I was hoping someone else has experienced it, and had grabbed the error details.

## dwjorgeb | 2019-07-19T00:52:07+00:00
@moneromooo-monero I just had this same error, when pruning with the flag. 

Then pruned with the tool and everything seemed fine, but when rebooted the node it got stuck. 

No errors besides ```Error retrieving blocks, missed 14 transactions for block with hash: <4f058f1674bc7114f30745d06c292134f52c2fbcbe30d0048080946942b7503f>``` once, but it's stuck for 20 mins on the same block and won't sync.

Going to resync from scratch now

## moneromooo-monero | 2019-07-19T22:05:08+00:00
If it's stuck and won't sync, restart with --log-level 1 to see why it won't sync.

## moneromooo-monero | 2019-08-27T15:44:54+00:00
ping

That last message is normal, it's from nodes that don't know about pruning yet and asking you for data you don't have. It's silenced in current code. It should not wedge your node at all though. 
Run with --log-level 1, and get a stack trace (gdb PATHTOMONEROD PIDOFMONEROD, thread apply all bt).

# Action History
- Created by: ukfhVp0zms | 2019-06-14T23:22:51+00:00
- Closed at: 2022-03-16T15:48:56+00:00
