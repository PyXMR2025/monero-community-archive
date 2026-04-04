---
title: 'daemon: monerod crash on LMDB resize'
source_url: https://github.com/monero-project/monero/issues/3230
author: iDunk5400
assignees: []
labels: []
created_at: '2018-02-03T13:52:34+00:00'
updated_at: '2018-02-16T13:24:11+00:00'
type: issue
status: closed
closed_at: '2018-02-16T13:24:11+00:00'
---

# Original Description
I have been experiencing regular monerod crashes during initial blockchain download on both Linux and Windows with master ed67e5c. The crash always happens on LMDB mapsize increase, at random points. I have not been able to complete a full sync in about 10 attempts.
```
2018-01-30 22:39:42.332 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167    [76.171.98.53:18080 OUT]  Synced 87712/1498836
2018-01-30 22:39:42.483 [P2P0]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:763     [94.23.23.52:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-01-30 22:39:42.485 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:557  [check_and_resize_for_batch] checking DB size
2018-01-30 22:39:42.485 [P2P6]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:611  [get_estimated_batch_size] m_height: 87712  block_start: 87212  block_stop: 87711
2018-01-30 22:39:42.485 [P2P6]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:649  estimated average block size for batch: 35498
2018-01-30 22:39:42.486 [P2P6]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:564  calculated batch size: 798705024
2018-01-30 22:39:42.486 [P2P6]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:573  increase size: 798705024
2018-01-30 22:39:42.486 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:521  DB map size:     2147483648
2018-01-30 22:39:42.486 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:522  Space used:      1492205568
2018-01-30 22:39:42.486 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:523  Space remaining: 655278080
2018-01-30 22:39:42.486 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:524  Size threshold:  798705024
2018-01-30 22:39:42.486 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:526  Percent used: 0.6949  Percent threshold: 0.8000
2018-01-30 22:39:42.486 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:532  Threshold met (size-based)
2018-01-30 22:39:42.486 [P2P6]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:581  [batch] DB resize needed
2018-01-30 22:39:42.527 [P2P6]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:497  LMDB Mapsize increased.  Old: 2048MiB, New: 2809MiB
2018-01-30 22:39:42.529 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash bf422b79212fdae6dc9a701c48976c07f6d103dcfcba98e2bb10dce9732a3bb2 not found in db
2018-01-30 22:39:42.529 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash a56d8295059db344cb2f49f1bd6b8a0905fd776ade9c0a9b05946447d7539ebf not found in db
2018-01-30 22:39:42.529 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash 3878f5e89c46b33c1d60924f5590209967318d2f58884b3152391d3a2c3ec6be not found in db
2018-01-30 22:39:42.529 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash 322691f00c21a01a6250a5e737ba39568e180ff0870dadc7c503b8b6e43f8d8f not found in db
2018-01-30 22:39:42.529 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash ef66bef76dd202b87ba8552201250e7f18bc72410df782fb6d6d741b31da7764 not found in db
2018-01-30 22:39:42.529 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash b874e44d110eadedbf83f38fb380d2e9c2d08989411d56ec428d4cf8e1fe6417 not found in db
2018-01-30 22:39:42.530 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash 311c6860030ce08f1ce4648f88e8f47161468b14b0b550e06c592cca837b21b1 not found in db
2018-01-30 22:39:42.530 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash 4a4b585a14b0e1086f6195c3392587663f0abea80ca7986bbc971967f8260b25 not found in db
2018-01-30 22:39:42.530 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash 06a7192c886bc7a35c648690afb1a87b4f853b73a463022d60e28cbb9c4e7e9a not found in db
2018-01-30 22:39:42.530 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash bf422b79212fdae6dc9a701c48976c07f6d103dcfcba98e2bb10dce9732a3bb2 not found in db
2018-01-30 22:39:42.530 [P2P6]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2080 transaction with hash a56d8295059db344cb2f49f1bd6b8a0905fd776ade9c0a9b05946447d7539ebf not found in db

Thread 34 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fff8ebfb700 (LWP 12635)]
__memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:35
35      ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S: No such file or directory.
(gdb) bt
#0  __memcpy_sse2_unaligned () at ../sysdeps/x86_64/multiarch/memcpy-sse2-unaligned.S:35
#1  0x0000555555d77163 in mdb_txn_renew0 (txn=0x7fff74020f90) at /home/user/monero/external/db_drivers/liblmdb/mdb.c:2949
#2  0x0000555555d772ba in mdb_txn_renew (txn=0x7fff74020f90) at /home/user/monero/external/db_drivers/liblmdb/mdb.c:2989
#3  0x0000555555b5c9a4 in cryptonote::lmdb_txn_renew (txn=0x7fff74020f90) at /home/user/monero/src/blockchain_db/lmdb/db_lmdb.cpp:427
#4  cryptonote::BlockchainLMDB::block_rtxn_start (this=0x55555684f7f0, mtxn=0x7fff8ebf8c90, mcur=0x7fff8ebf8c98) at /home/user/monero/src/blockchain_db/lmdb/db_lmdb.cpp:2763
#5  0x0000555555b5787c in cryptonote::BlockchainLMDB::height (this=0x55555684f7f0) at /home/user/monero/src/blockchain_db/lmdb/db_lmdb.cpp:2028
#6  0x0000555555b7fbe3 in cryptonote::Blockchain::get_current_blockchain_height (this=0x5555567b9218) at /home/user/monero/src/cryptonote_core/blockchain.cpp:303
```

# Discussion History
## iDunk5400 | 2018-02-03T22:36:22+00:00
Thanks, PR #3231 fixes the issue.

# Action History
- Created by: iDunk5400 | 2018-02-03T13:52:34+00:00
- Closed at: 2018-02-16T13:24:11+00:00
