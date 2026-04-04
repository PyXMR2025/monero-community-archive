---
title: Crash in mdb_cursor_get while syncing
source_url: https://github.com/monero-project/monero/issues/724
author: laanwj
assignees: []
labels: []
created_at: '2016-03-14T10:00:38+00:00'
updated_at: '2016-03-16T07:32:13+00:00'
type: issue
status: closed
closed_at: '2016-03-16T07:32:13+00:00'
---

# Original Description
Up to three times now I've had crashes (SIGSEGV) during sync. 
- Progress is 678888/995957, but this appears to be happening randomly.
- This happens while catching up an old node. I've converted the old block chain using  `blockchain_export`/`blockchain_import`.
- System: `Ubuntu 14.04.4 LTS` VM, 64-bit, 8GB memory, 8 cores, still plenty of HD space left
- HEAD: 5843f89364691788843d3661a2b1cdb1651168da, compiled in `RelWithDebInfo` mode

gdb output (#1-#5):

```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffd30f8c700 (LWP 28657)]
bash: mail: command not found
0x00000000008122e1 in mdb_cursor_get (mc=0x7ffd181af840, key=0x7ffd30f89720, data=0x0, op=MDB_SET)
    at /home/ubuntu/bitmonero/external/db_drivers/liblmdb/mdb.c:6906
6906            if (mc->mc_txn->mt_flags & MDB_TXN_BLOCKED)
(gdb) bt
#0  0x00000000008122e1 in mdb_cursor_get (mc=0x7ffd181af840, key=0x7ffd30f89720, data=0x0, op=MDB_SET)
    at /home/ubuntu/bitmonero/external/db_drivers/liblmdb/mdb.c:6906
#1  0x00000000007fa83d in cryptonote::BlockchainLMDB::block_exists (this=0x2a3f140, h=...)
    at /home/ubuntu/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:1349
#2  0x000000000072599f in cryptonote::Blockchain::have_block (this=0x2a1abc0, id=...)
    at /home/ubuntu/bitmonero/src/cryptonote_core/blockchain.cpp:1847
#3  0x0000000000750c0c in cryptonote::core::have_block (this=<optimized out>, id=...)
    at /home/ubuntu/bitmonero/src/cryptonote_core/cryptonote_core.cpp:853
#4  0x000000000068e44d in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry (this=0x2a1aa10,
    command=<optimized out>, arg=..., context=...) at /home/ubuntu/bitmonero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:765
#5  0x000000000068474e in operator() (a3=..., a2=..., a1=2007, p=0x2a1aa10, this=0x7ffd30f89e40)
    at /usr/include/boost/bind/mem_fn_template.hpp:393
```

Full gdb traceback can be found here:
http://0bin.net/paste/pqduymi1W8k9cbZY#QkhwEmaE1oxMAJpke32hpEjeiXxhmMrhXm8qY-gqRQE


# Discussion History
## hyc | 2016-03-14T10:08:55+00:00
when it crashes there, can you "print *mc" and paste that output too?


## laanwj | 2016-03-14T10:12:36+00:00
Will do so when it happens again.


## hyc | 2016-03-14T10:27:19+00:00
So your current progress was 678888, but it crashed 3 times on the way to getting there? what block height did you start at?


## laanwj | 2016-03-14T10:49:24+00:00
Yesterday after the blockchain conversion the first log entry was:

```
2016-Mar-13 10:37:26.421405 Blockchain initialized. last block: 181714, d570.h18.m51.s49 time ago, current difficulty: 1194438309
```

Just noticed this in the log too (but no crash):

```
2016-Mar-14 11:31:45.412690 [P2P7]DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2016-Mar-14 11:31:45.414742 [P2P7]ERROR /home/ubuntu/bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:342 Exception at [connection<t_protocol_handler>::handle_read], what=DB error attempting to fetch block index from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
```

I suppose something went wrong in the conversion and it'd be better to start over.


## fluffypony | 2016-03-14T12:42:33+00:00
I'm seeing the `MDB_BAD_TXN` issue on freshly synced ARM as well, we're trying to figure out what's causing it. It's not your conversion, as I didn't convert.


## laanwj | 2016-03-15T07:07:28+00:00
I removed the `~/.bitmonero` directory and started completely from scratch. This seemed to go well, but at block 994383/997497, the issue happened again:

```
0x00000000008122e1 in mdb_cursor_get (mc=0x7fff780c8410, key=0x7fff966f7720, data=0x0, op=MDB_SET)
    at /home/ubuntu/bitmonero/external/db_drivers/liblmdb/mdb.c:6906
6906            if (mc->mc_txn->mt_flags & MDB_TXN_BLOCKED)
```

I have the following output

```
(gdb) print *mc
$1 = {mc_next = 0x7fff78000078, mc_backup = 0x7fff78000078, mc_xcursor = 0x0, mc_txn = 0x0, mc_dbi = 4, mc_db = 0x2a43c48, 
  mc_dbx = 0x2a41db0, mc_dbflag = 0x2a440b4 "\030\030", '\032' <repeats 15 times>, mc_snum = 4, mc_top = 3, 
  mc_flags = 524353, mc_pg = {0x7ffcbc4ef000, 0x7ffc375e2000, 0x7ffd90f0a000, 0x7ffd91f9b000, 0x18c1, 0x7fff7811b070, 
    0x7fff78000078, 0x0, 0x18f1, 0x7fff780be120, 0x7fff78000078, 0x0, 0x0, 0x7fff780c84f0, 0x7fff780c84f0, 0x7fff780c84f0, 
    0x1, 0x50, 0x74, 0x7fff780c8420, 0x7fff780c84b8, 0x0, 0x0, 0x7fff781ab508, 0xa, 0x7fff781ab538, 0xd6aafe0a6ceb0ea5, 
    0xc0, 0x1801, 0x7fff7811b070, 0x7fff78000078, 0x0}, mc_ki = {2, 66, 20, 9, 57632, 30731, 32767, 0, 120, 30720, 32767, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 34224, 30732, 32767, 0, 34224, 30732, 32767, 0, 34224, 30732, 32767, 0}}
```

Will keep the gdb session running in case there's more you want to debug.


## hyc | 2016-03-15T09:20:21+00:00
Thanks. are you on IRC?


## hyc | 2016-03-15T09:36:07+00:00
In frame 1:
  print m_cursors
  print *m_cursors
  print &m_wcursors
  print m_wcursors
  print m_txn
  print *m_txn


## hyc | 2016-03-15T09:36:56+00:00
(pretty sure this crash is already fixed in current master 240a50f3fb1e1c3526896b112c15cf4fc3d030ae)


## laanwj | 2016-03-15T11:04:27+00:00
Currently not on IRC, will be on later. Result:

```
(gdb) frame 1
#1  0x00000000007fa83d in cryptonote::BlockchainLMDB::block_exists (this=0x2a41790, h=...)
    at /home/ubuntu/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:1349
1349      auto get_result = mdb_cursor_get(m_cur_block_heights, &key, NULL, MDB_SET);
(gdb) print m_cursors
$2 = (const cryptonote::mdb_txn_cursors *) 0x2a418a0
(gdb) print *m_cursors
$3 = {m_txc_blocks = 0x0, m_txc_block_heights = 0x0, m_txc_block_hashes = 0x0, m_txc_block_timestamps = 0x0, 
  m_txc_block_sizes = 0x0, m_txc_block_diffs = 0x0, m_txc_block_coins = 0x0, m_txc_output_txs = 0x0, 
  m_txc_output_indices = 0x0, m_txc_output_amounts = 0x0, m_txc_output_keys = 0x0, m_txc_txs = 0x0, 
  m_txc_tx_heights = 0x0, m_txc_tx_unlocks = 0x0, m_txc_tx_outputs = 0x0, m_txc_spent_keys = 0x0, m_txc_hf_versions = 0x0}
(gdb) print &m_wcursors
$4 = (cryptonote::mdb_txn_cursors *) 0x2a418a0
(gdb) print m_wcursors
$5 = {m_txc_blocks = 0x0, m_txc_block_heights = 0x0, m_txc_block_hashes = 0x0, m_txc_block_timestamps = 0x0, 
  m_txc_block_sizes = 0x0, m_txc_block_diffs = 0x0, m_txc_block_coins = 0x0, m_txc_output_txs = 0x0, 
  m_txc_output_indices = 0x0, m_txc_output_amounts = 0x0, m_txc_output_keys = 0x0, m_txc_txs = 0x0, 
  m_txc_tx_heights = 0x0, m_txc_tx_unlocks = 0x0, m_txc_tx_outputs = 0x0, m_txc_spent_keys = 0x0, m_txc_hf_versions = 0x0}
(gdb) print m_txn
$6 = (MDB_txn *) 0x2a43b00
(gdb) print *m_txn
$7 = {mt_parent = 0x0, mt_child = 0x0, mt_next_pgno = 2119847, mt_txnid = 994387, mt_env = 0x2a41bf0, 
  mt_free_pgs = 0x7ffff7e97018, mt_loose_pgs = 0x0, mt_loose_count = 0, mt_spill_pgs = 0x0, mt_u = {
    dirty_list = 0x7ffff0eab010, reader = 0x7ffff0eab010}, mt_dbxs = 0x2a41cf0, mt_dbs = 0x2a43b88, 
  mt_dbiseqs = 0x2a44058, mt_cursors = 0x2a43fa8, 
  mt_dbflags = 0x2a440b0 "\b\030\032\032\030\030", '\032' <repeats 15 times>, mt_numdbs = 0, mt_flags = 1, 
  mt_dirty_room = 131071}
```


## laanwj | 2016-03-15T11:05:06+00:00
Ok, will try to upgrade to latest master and rebuild.


## hyc | 2016-03-15T13:43:28+00:00
Aside from the crash fix, there are some remaining glitches that I believe are cleaned up in https://github.com/monero-project/bitmonero/pull/727


## laanwj | 2016-03-16T07:30:28+00:00
Been running with #727 for almost a day no, no crashes.


# Action History
- Created by: laanwj | 2016-03-14T10:00:38+00:00
- Closed at: 2016-03-16T07:32:13+00:00
