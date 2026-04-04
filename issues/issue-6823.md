---
title: 'Error adding spent key image to db transaction: Cannot allocate memory'
source_url: https://github.com/monero-project/monero/issues/6823
author: hrumag
assignees: []
labels: []
created_at: '2020-09-17T10:44:51+00:00'
updated_at: '2022-02-19T04:06:01+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:06:01+00:00'
---

# Original Description
Hi all,

I'm running 0.16.0.3 armv7 monerod on a raspberry pi 3 (1GB Ram)
This message is often shown, the only way to solve is to restart monerod, but after some hours the error is shown again.

The first time I encountered the problem I thought it was a blockchain-corruption-related problem, so I decided to delete it entirely and start syncing it from scratch.
But the problem still persists.
I've been using the previous versions of monero and everything was ok.
Other tips: RAM usage is about 60% used and SWAP is 70% used.

`2020-09-17 10:32:40.839 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1583    Synced 1389299/2188594 (63%, 799295 left)
2020-09-17 10:33:36.402 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4083 Error adding block with hash: <13092735ace60779e6547f8cb640a118c1941c18b6901b61991d24584a49d8ec> to blockchain, what = Error adding spent key image to db transaction: Cannot allocate memory
2020-09-17 10:33:36.416 [P2P4]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-09-17 10:33:36.417 [P2P4]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4290 Exception at [add_new_block], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2020-09-17 10:33:46.106 [P2P4]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:46.566 [P2P4]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:51.964 [P2P4]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:51.982 [P2P4]  ERROR   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:95        Error in handle_invoke_map: DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:52.022 [P2P3]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:52.023 [P2P3]  ERROR   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:95        Error in handle_invoke_map: DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:57.439 [P2P0]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:57.445 [P2P0]  ERROR   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:95        Error in handle_invoke_map: DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:59.211 [P2P1]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:33:59.212 [P2P1]  ERROR   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:95        Error in handle_invoke_map: DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:34:04.365 [P2P5]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:34:04.366 [P2P9]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:34:04.367 [P2P9]  ERROR   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:95        Error in handle_invoke_map: DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:34:04.918 [P2P2]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:34:04.919 [P2P2]  ERROR   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:95        Error in handle_invoke_map: DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:34:07.270 [P2P1]  WARNING blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75   DB error attempting to fetch block index from hashCannot allocate memory
2020-09-17 10:34:07.271 [P2P1]  ERROR   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:95        Error in handle_invoke_map: DB error attempting to fetch block index from hashCannot allocate memory
`

Thank you for your help.

hrumag

# Discussion History
## selsta | 2022-02-19T04:06:01+00:00
You don't have enough RAM, that's why they are allocation errors.

# Action History
- Created by: hrumag | 2020-09-17T10:44:51+00:00
- Closed at: 2022-02-19T04:06:01+00:00
