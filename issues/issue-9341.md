---
title: blockchain always gets corrupt
source_url: https://github.com/monero-project/monero/issues/9341
author: Lioxen
assignees: []
labels:
- daemon
- database
created_at: '2024-05-24T13:24:25+00:00'
updated_at: '2025-12-29T01:25:33+00:00'
type: issue
status: closed
closed_at: '2025-12-29T01:25:33+00:00'
---

# Original Description
My hardware is a Intel(R) Core(TM) i5 CPU 650  @ 3.20GHz, 8GB Ram and the blockchain is stored on a ssd (is brand new). 
I try to run a full node, but I fail constantly to fetch the blockchain. I run alternately into 2 errors, but both of them leave me with a corrupt blockchain. And the annoying thing is... this happens not in the beginning, no this happens after hours of fetching the blockchain. 

1. error
there you see nothing in the monerod.log expect that the monerod service restarts all the time, but in the syslog I see

systemd[1]:Starting monerod.service - Monero Full Node (Mainnet)...
monerod[22204]: 2024-05-24 09:32:12.537#011I Monero 'Fluorine Fermi' (v0.18.3.3-release)
monerod[22204]: Forking to background...
systemd[1]: Started monerod.service - Monero Full Node (Mainnet).
kernel: [79627.129234] monerod[22219]: segfault at 7f93c514e000 ip 00007fb60f72be96 sp 00007f93deaf7cf8 error 6 in libc.so.6[7fb60f6af000+155000] likely on CPU 1 (core 2, socket 0)
kernel: [79627.129252] Code: 16 c0 48 29 ce 48 ff c7 48 01 fe 48 8d 54 11 c0 0f 1f 40 00 0f 10 0e 0f 10 56 10 0f 10 5e 20 0f 10 66 30 48 83 ee c0 0f 29 0f <0f> 29 57 10 0f 29 5f 20 0f 29 67 30 48 83 ef c0 48 39 fa 77 d5 0f
systemd[1]: monerod.service: Main process exited, code=killed, status=11/SEGV
systemd[1]: monerod.service: Failed with result 'signal'.
systemd[1]: monerod.service: Consumed 6.428s CPU time.

to repair the blockchain is not possible, if I start 
monerod --db-salvage --data-dir=/var/lib/monero/.bitmonero  it end with a
Segmentation fault

2. error
WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	DB error attempting to fetch transaction index from hash 6e5e9c38659f05c4f3d1f55c1a802b1ff461a38e875210dbd11180487b1fd9c1: MDB_CORRUPTED: Located page was wrong type
ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1115	Exception at [core::handle_incoming_txs()], what=DB error attempting to fetch transaction index from hash 6e5e9c38659f05c4f3d1f55c1a802b1ff461a38e875210dbd11180487b1fd9c1: MDB_CORRUPTED: Located page was wrong type
WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4696	Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4827	Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2024-05-24 10:13:17.980	[P2P9]	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	DB error attempting to fetch transaction index from hash 6e5e9c38659f05c4f3d1f55c1a802b1ff461a38e875210dbd11180487b1fd9c1: MDB_CORRUPTED: Located page was wrong type
ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:1115	Exception at [core::handle_incoming_txs()], what=DB error attempting to fetch transaction index from hash 6e5e9c38659f05c4f3d1f55c1a802b1ff461a38e875210dbd11180487b1fd9c1: MDB_CORRUPTED: Located page was wrong type
WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4696	Exception at [add_new_block], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
ERROR	blockchain	src/cryptonote_core/blockchain.cpp:4827	Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid

to repair the blockchain after this error occurred is also not possible.  there I see this error over and over again

I'm quite sure, there is something wrong with my hardware. (but I do not know, what in the moment) 
I have some questions about the blockchain.

Why is it necessary to declare the hole data block for corrupt? I mean it takes hours, in my case days or sometime weeks to download the blockchain.  How can a simple incident corrupt 100GB of data in a split of a second?

Why there are not some kind of anchor or recovery points, where the software could roll back, if an accident occurs?

Why must the data stored in one huge file? 

I mean, I'm not the only one who has a problems with a corrupt blockchain. And always the only advice I read is, delete the data.mdb and start from the beginning(if recovery not working, what it never does in my case). Think of all the wasted time and energy and this because of the terrible data store design.
 


# Discussion History
## selsta | 2024-05-24T17:30:30+00:00
> to repair the blockchain is not possible, if I start

`--db-salvage` only works in limited situations.

> I'm quite sure, there is something wrong with my hardware.

If you really think your hardware is broken then it's better to use a remote node, you won't have a good experience otherwise.

> Why must the data stored in one huge file?

Using separate files won't help against broken hardware or other corruption issues.

> Why there are not some kind of anchor or recovery points, where the software could roll back, if an accident occurs?

If you are talking about snapshots, that would increase the size of the blockchain. Currently it is recommended to manually make backups.

> I mean, I'm not the only one who has a problems with a corrupt blockchain.

Most of the time it's due to people storing the blockchain on external storage and unplugging it during sync, or someone having issues with power loss during sync. There are ways where we could avoid that but it's a tradeoff between speed and reliability. We could set `--db-sync-mode safe` as the default, but that would slow sync down and decrease the lifespan of the disk due to more frequent writes.

## wassim-devel | 2025-11-11T16:43:40+00:00
> Using separate files won't help against broken hardware or other corruption issues.
@selsta 

I am late, but may I ask why? Database corruption happened to me multiple times and I always had to resync the entire database, it was due to powerloss or VM exit due to not enough RAM in the host system.
I am far from being the only one and I imagine that resyncing the entire database multiple times (or just one time) decreases far more the lifespan of the disk than enabling `--db-sync-mode safe` as default

Using separate files (or another way) for storing the blockchain would permit to avoid resyncing the entire database, and just resync the last file 

## nahuhh | 2025-11-11T17:23:09+00:00
>I am far from being the only one and I imagine that resyncing the entire database multiple times (or just one time) decreases far more the lifespan of the disk than enabling --db-sync-mode safe as default

`safe` is the default once fully synced

## wassim-devel | 2025-11-11T19:04:34+00:00
> `safe` is the default once fully synced

Okay I now understand why I don't have corruption issues when my database is fully synced

The problem however is that when you have a current electricity issue, and you relaunch your monero node in that particular moment, at that moment it's not fully synced, and the electricity (or RAM) issue could show up a second time in this particular moment, which leads to a database corruption. This happened to me unfortunately

I imagine the issue could be resolved by making multiple files as proposed by OP, or by another way. Monerod is the only project where I've seen that a small corruption in the end of file needs a full resync from scratch, it would help a lot of people if this was fixed in one way or another.



# Action History
- Created by: Lioxen | 2024-05-24T13:24:25+00:00
- Closed at: 2025-12-29T01:25:33+00:00
