---
title: Unrecoverable "Transaction must abort, has a child, or is invalid" after a
  MDB_MAP_FULL error
source_url: https://github.com/monero-project/monero/issues/2168
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-07-12T08:07:56+00:00'
updated_at: '2017-09-02T12:33:29+00:00'
type: issue
status: closed
closed_at: '2017-09-02T12:33:29+00:00'
---

# Original Description
```
2017-07-12 07:41:29.928	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1067	[85.221.205.90:61033 INC]  Synced 612468/1352437
2017-07-12 07:41:35.957	[P2P8]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3383	Error adding block with hash: <ed913121d5ae4631128a493f47e1e55df3d3c1719672680a3c9791744f9e9bc6> to blockchain, what = Error adding spent key image to db transaction: MDB_MAP_FULL: Environment mapsize limit reached
2017-07-12 07:41:35.958	[P2P8]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:71	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
```

Syncing from scratch on a Mac Mini, with the default 200 block sync size. Restarting monerod worked just fine. I did not have logs beyond default.

Edit: to be clear, by unrecoverable, I mean the same MDB_BAD_TXN log line continued to happen indefinitely, until I exit monerod (about 20 minutes of it till I spotted it).

# Discussion History
## moneromooo-monero | 2017-09-02T12:33:29+00:00
This is probably fixed by https://github.com/monero-project/monero/pull/2372, which cleans up a txn if it fails to commit.

# Action History
- Created by: moneromooo-monero | 2017-07-12T08:07:56+00:00
- Closed at: 2017-09-02T12:33:29+00:00
