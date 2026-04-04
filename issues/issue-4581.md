---
title: Database corrupted?
source_url: https://github.com/monero-project/monero/issues/4581
author: dawiepoolman
assignees: []
labels:
- invalid
created_at: '2018-10-13T15:44:40+00:00'
updated_at: '2018-10-13T16:16:51+00:00'
type: issue
status: closed
closed_at: '2018-10-13T16:16:51+00:00'
---

# Original Description
Hi guys

Still trying to sync my RPi..

I got this error recently after I closed and re-started a bash SSH session:

2018-10-13 15:07:31.566 [P2P4]  WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   **DB error attempting to fetch block index from hashMDB_CORRUPTED: Located page was wrong type**

Even after popping 500 blocks of the tip and re-tried it still stuck.

With --log-level 1 I also get

2018-10-13 15:41:02.508 [P2P2]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3784 Exception in cleanup_handle_incoming_blocks: **Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid**

Would the data.mdb be corrupted _again_?

Thx

# Discussion History
## dawiepoolman | 2018-10-13T15:50:51+00:00
./bin/monero-v0.12.3.0/monerod --rpc-bind-ip=192.168.1.10 --rpc-bind-port=4008 --confirm-external-bind **--db-salvage**

Not working either.  Produces:

2018-10-13 15:49:34.921 [P2P1]  ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:1224    **Exception at [core::handle_incoming_block()], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid**


## dawiepoolman | 2018-10-13T15:54:04+00:00
Stuff it.  I will just restart again.  No use crying over spilled milk.
It just a pity that the database seem to be very unstable and easily corrupted?

## dawiepoolman | 2018-10-13T16:00:51+00:00
Oh, I got to block 400k this time.  Not bad for a Pi in a week imo
:P

## hyc | 2018-10-13T16:07:13+00:00
The DB isn't unstable, your Pi and its power supply are. No software can compensate for broken hardware.

https://github.com/monero-project/monero/issues/4507#issuecomment-429553959

## hyc | 2018-10-13T16:12:38+00:00
+invalid

## dawiepoolman | 2018-10-13T16:13:13+00:00
That is true.  I cant claim that my hardware is cut out for the task.  I am seeing it as a personal challenge trying to try get the Pi to run the DB.  It has been running very stable and consistent for the last week.  Maybe is was related to the SSH session that was abruptly interrupted from my laptop side.

# Action History
- Created by: dawiepoolman | 2018-10-13T15:44:40+00:00
- Closed at: 2018-10-13T16:16:51+00:00
