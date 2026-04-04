---
title: '"Failed to parse transaction from blob"'
source_url: https://github.com/monero-project/monero/issues/2834
author: Esperulo
assignees: []
labels: []
created_at: '2017-11-17T02:53:49+00:00'
updated_at: '2017-11-28T02:22:26+00:00'
type: issue
status: closed
closed_at: '2017-11-28T02:22:26+00:00'
---

# Original Description
I'm getting this error message when running monerod.exe:

```
2017-11-17 02:49:08.270 5284    ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:102    Failed to parse transaction from blob
2017-11-17 02:49:08.270 5284    ERROR   txpool  src/cryptonote_core/tx_pool.cpp:1020    Failed to parse tx from txpool
2017-11-17 02:49:08.270 5284    ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:409     Failed to initialize memory pool
```

This seems to be the same as #2480. A "--drop-txpool" switch is mentioned there, but it's not recognized on my system. I'm running 0.11.1.0 under Windows 7 64.

# Discussion History
## moneromooo-monero | 2017-11-17T08:55:01+00:00
Did your computer crash before that ?

## Esperulo | 2017-11-17T13:06:42+00:00
You're correct; I'm having problems with the computer crashing, or rather shutting down. I run CHKDSK when that happens.

## moneromooo-monero | 2017-11-17T17:58:31+00:00
So your DB is corrupted. Try running with --db-salvage and see if that helps.

## Esperulo | 2017-11-17T18:47:07+00:00
I already tried that; I got the same error. I hope I don't have to download the database again. :-(

## moneromooo-monero | 2017-11-17T18:51:18+00:00
Maybe, if the last try does not work, you will have to.

Build mdb_drop from http://highlandsun.com/hyc/mdb_drop.c, and run it twice:

mdb_drop -d -s txpool_meta ~/.bitmonero/lmdb
mdb_drop -d -s txpool_blob ~/.bitmonero/lmdb

Then start monerod again.

## moneromooo-monero | 2017-11-19T12:33:36+00:00
Also, this is fixed in master, so you could run the chain with master once (this should clean out those corrupt txes), then revert to using 0.11.1.0. Do not run the master wallet, just master monerod, once.


## Esperulo | 2017-11-19T19:08:46+00:00
I switched to Linux to build monero-master. It requires boost-devel 1.58, but my distribution (CentOS 6) only has 1.41. Also, I tried to build mdb_drop.c as mentioned in #2480, but where am I supposed to find liblmdb.a?

## moneromooo-monero | 2017-11-19T19:19:14+00:00
If you have lmdb installed by your OS, the monero build won't build it by default. Otherwise, it's in external/db_drivers/lmdb, and you can do "make" there, to have it built if it's not. Otherwise you should be able to link it with the liblmdb installed by your OS.

## Esperulo | 2017-11-23T04:31:00+00:00
Sorry to keep you waiting.

```
# ls -F
bitmonero.log*  data.mdb*  lmdb/  lock.mdb*  p2pstate.bin*
# /opt/monero-fixed/external/db_drivers/liblmdb/mdb_drop -d -s txpool_meta ./lmdb/
mdb_open failed, error -30798 MDB_NOTFOUND: No matching key/data pair found
```
Running CentOS 6 64, but lmdb is on a Windows drive.

## moneromooo-monero | 2017-11-23T09:37:38+00:00
mdb_stat -a  ./lmdb/

## Esperulo | 2017-11-24T02:50:03+00:00
```
# /opt/monero-fixed/external/db_drivers/liblmdb/mdb_stat -a ./lmdb/
Status of Main DB
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 13
Status of block_heights
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1443985
Status of block_info
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1443985
Status of blocks
  Tree depth: 4
  Branch pages: 525
  Leaf pages: 117545
  Overflow pages: 34
  Entries: 1443985
Status of hf_versions
  Tree depth: 3
  Branch pages: 33
  Leaf pages: 7079
  Overflow pages: 0
  Entries: 1443985
Status of output_amounts
  Tree depth: 4
  Branch pages: 530
  Leaf pages: 80661
  Overflow pages: 0
  Entries: 25190434
Status of output_txs
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 25190434
Status of properties
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1
Status of spent_keys
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 21543127
Status of tx_indices
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 3350232
Status of tx_outputs
  Tree depth: 4
  Branch pages: 291
  Leaf pages: 65056
  Overflow pages: 2383
  Entries: 3350232
Status of txpool_blob
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 40
  Entries: 9
Status of txpool_meta
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 9
Status of txs
  Tree depth: 4
  Branch pages: 1083
  Leaf pages: 243309
  Overflow pages: 6825606
  Entries: 3350232
```

## Esperulo | 2017-11-28T02:22:26+00:00
I've re-downloaded the block chain. Closing.

# Action History
- Created by: Esperulo | 2017-11-17T02:53:49+00:00
- Closed at: 2017-11-28T02:22:26+00:00
