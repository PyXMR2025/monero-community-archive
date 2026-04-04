---
title: blockchain corrupted?
source_url: https://github.com/monero-project/monero-gui/issues/3233
author: IndustrialOne
assignees: []
labels: []
created_at: '2020-11-13T17:23:49+00:00'
updated_at: '2020-11-14T16:25:42+00:00'
type: issue
status: closed
closed_at: '2020-11-14T09:20:19+00:00'
---

# Original Description
Log:

2020-11-13 17:15:56.076	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1593	Synced 305380/2229822 (13%, 1924442 left)
2020-11-13 17:15:56.841	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1593	Synced 305480/2229822 (13%, 1924342 left)
2020-11-13 17:15:57.391	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1593	Synced 305580/2229822 (13%, 1924242 left)
2020-11-13 17:15:57.461	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4329	Error adding block with hash: <3c9c049f830d9aaf0dbcc13a84f3405e6c86b316913bc1eda9eddf176270289b> to blockchain, what = Error adding spent key image to db transaction: MDB_CORRUPTED: Located page was wrong type
2020-11-13 17:15:57.464	[P2P6]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:15:57.466	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4533	Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:15:59.079	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4329	Error adding block with hash: <3c9c049f830d9aaf0dbcc13a84f3405e6c86b316913bc1eda9eddf176270289b> to blockchain, what = Error adding spent key image to db transaction: MDB_CORRUPTED: Located page was wrong type
2020-11-13 17:15:59.082	[P2P3]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:15:59.084	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4533	Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:05.597	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4329	Error adding block with hash: <3c9c049f830d9aaf0dbcc13a84f3405e6c86b316913bc1eda9eddf176270289b> to blockchain, what = Error adding spent key image to db transaction: MDB_CORRUPTED: Located page was wrong type
2020-11-13 17:16:05.602	[P2P3]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:05.604	[P2P3]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4533	Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:11.074	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4329	Error adding block with hash: <3c9c049f830d9aaf0dbcc13a84f3405e6c86b316913bc1eda9eddf176270289b> to blockchain, what = Error adding spent key image to db transaction: MDB_CORRUPTED: Located page was wrong type
2020-11-13 17:16:11.078	[P2P4]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:11.079	[P2P4]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4533	Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:12.575	[P2P2]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4329	Error adding block with hash: <3c9c049f830d9aaf0dbcc13a84f3405e6c86b316913bc1eda9eddf176270289b> to blockchain, what = Error adding spent key image to db transaction: MDB_CORRUPTED: Located page was wrong type
2020-11-13 17:16:12.578	[P2P2]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:12.580	[P2P2]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4533	Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:12.930	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4329	Error adding block with hash: <3c9c049f830d9aaf0dbcc13a84f3405e6c86b316913bc1eda9eddf176270289b> to blockchain, what = Error adding spent key image to db transaction: MDB_CORRUPTED: Located page was wrong type
2020-11-13 17:16:12.933	[P2P6]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:82	Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:12.934	[P2P6]	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4533	Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-11-13 17:16:14.715	6000	INFO	msgwriter	src/common/scoped_message_writer.h:102	Stop signal sent
2020-11-13 17:16:19.175	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:80	p2p net loop stopped
2020-11-13 17:16:19.221	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:84	Stopping core RPC server...
2020-11-13 17:16:19.225	[SRV_MAIN]	INFO	global	src/daemon/daemon.cpp:227	Node stopped.
2020-11-13 17:16:19.290	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2020-11-13 17:16:19.299	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:90	Deinitializing p2p...
2020-11-13 17:16:19.590	[SRV_MAIN]	INFO	global	src/daemon/core.h:94	Deinitializing core...
2020-11-13 17:18:19.093	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2020-11-13 17:18:19.094	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully

I tried --db-salvage, same messages. I do not want to redownload the entire thing every time a tiny spot gets corrupted, is there anything else I can do?

# Discussion History
## selsta | 2020-11-14T09:20:19+00:00
The blockchain does not corrupt itself unless you plug out the harddrive or turn off the computer during the initial sync. After the initial sync it switches to a safe sync mode so it should not happen after you initially synced up.

You can use a remote node if you don’t want to sync up.

Closing as there is no bug here.

## IndustrialOne | 2020-11-14T16:25:42+00:00
The USB stick I was using got corrupted. Nevertheless, why can't GUI Monero start from the last known good block and sync from there? Why do I have to start from the beginning? This is BS.

________________________________
From: selsta <notifications@github.com>
Sent: Saturday, November 14, 2020 2:20 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] blockchain corrupted? (#3233)


The blockchain does not corrupt itself unless you plug out the harddrive or turn off the computer during the initial sync. After the initial sync it switches to a safe sync mode so it should not happen after you initially synced up.

You can use a remote node if you don’t want to sync up.

Closing as there is no bug here.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3233#issuecomment-727173207>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4QIKYRVXUATZRJCWJDSPZDV7ANCNFSM4TU2ZUIA>.


# Action History
- Created by: IndustrialOne | 2020-11-13T17:23:49+00:00
- Closed at: 2020-11-14T09:20:19+00:00
