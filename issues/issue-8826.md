---
title: Unable to prune
source_url: https://github.com/monero-project/monero/issues/8826
author: YuXiaoCoder
assignees: []
labels:
- bug
- more info needed
created_at: '2023-04-20T01:14:05+00:00'
updated_at: '2024-01-26T14:31:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I use the following command to run the node, the node version is 0.18.2.2
```bash
/opt/xmrmain/core/monerod --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18081 --p2p-bind-port=18080 --data-dir=/mnt/xmrmain/node --confirm-external-bind --log-level=1 --non-interactive --prune-blockchain
```
I want to further reduce the disk space occupied by monero-blockchain-prune
```bash
/opt/xmrmain/core/monero-blockchain-prune --data-dir=/mnt/xmrmain/node/ --copy-pruned-database
```

Got the following log error
```log
2023-04-19 13:50:11.520 I Starting...
2023-04-19 13:50:11.520 I Initializing source blockchain (BlockchainDB)
2023-04-19 13:50:11.525 I Loading blockchain from folder "/mnt/xmr/node/lmdb" ...
2023-04-19 13:50:11.526 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-04-19 13:50:16.136 I source blockchain storage initialized OK
2023-04-19 13:50:16.138 I Loading blockchain from folder "/mnt/xmr/node/lmdb-pruned" ...
2023-04-19 13:50:16.138 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2023-04-19 13:50:16.216 I pruned blockchain storage initialized OK
2023-04-19 13:50:16.250 I Pruning...
2023-04-19 13:50:16.251 I Copying blocks
2023-04-19 13:51:13.341 I LMDB Mapsize increased.  Old: 1024MiB, New: 1536MiB
2023-04-19 13:52:51.813 I LMDB Mapsize increased.  Old: 1536MiB, New: 2048MiB
2023-04-19 13:54:23.994 I LMDB Mapsize increased.  Old: 2048MiB, New: 2560MiB
2023-04-19 13:55:33.140 I Copying block_info
2023-04-19 13:55:48.256 I LMDB Mapsize increased.  Old: 2560MiB, New: 3072MiB
2023-04-19 13:56:21.605 I Copying block_heights
2023-04-19 13:57:01.853 I Copying txs_pruned
2023-04-19 13:57:06.346 I LMDB Mapsize increased.  Old: 3072MiB, New: 3585MiB
2023-04-19 13:57:23.929 I LMDB Mapsize increased.  Old: 3585MiB, New: 4097MiB
2023-04-19 13:57:44.809 I LMDB Mapsize increased.  Old: 4097MiB, New: 4610MiB
2023-04-19 13:58:08.152 I LMDB Mapsize increased.  Old: 4610MiB, New: 5122MiB
2023-04-19 13:58:34.897 I LMDB Mapsize increased.  Old: 5122MiB, New: 5635MiB
2023-04-19 13:59:55.301 I LMDB Mapsize increased.  Old: 5635MiB, New: 6147MiB
2023-04-19 14:01:32.416 I LMDB Mapsize increased.  Old: 6147MiB, New: 6660MiB
2023-04-19 14:02:57.525 I LMDB Mapsize increased.  Old: 6660MiB, New: 7172MiB
2023-04-19 14:04:14.976 I LMDB Mapsize increased.  Old: 7172MiB, New: 7684MiB
2023-04-19 14:05:06.933 I LMDB Mapsize increased.  Old: 7684MiB, New: 8196MiB
2023-04-19 14:05:54.620 I LMDB Mapsize increased.  Old: 8196MiB, New: 8708MiB
2023-04-19 14:06:46.277 I LMDB Mapsize increased.  Old: 8708MiB, New: 9220MiB
2023-04-19 14:07:38.369 I LMDB Mapsize increased.  Old: 9220MiB, New: 9732MiB
2023-04-19 14:08:31.686 I LMDB Mapsize increased.  Old: 9732MiB, New: 10244MiB
2023-04-19 14:09:18.969 I LMDB Mapsize increased.  Old: 10244MiB, New: 10756MiB
2023-04-19 14:10:06.318 I LMDB Mapsize increased.  Old: 10756MiB, New: 11268MiB
2023-04-19 14:10:58.611 I LMDB Mapsize increased.  Old: 11268MiB, New: 11781MiB
2023-04-19 14:11:52.006 I LMDB Mapsize increased.  Old: 11781MiB, New: 12293MiB
2023-04-19 14:12:47.392 I LMDB Mapsize increased.  Old: 12293MiB, New: 12805MiB
2023-04-19 14:13:42.413 I LMDB Mapsize increased.  Old: 12805MiB, New: 13317MiB
2023-04-19 14:14:40.557 I LMDB Mapsize increased.  Old: 13317MiB, New: 13830MiB
2023-04-19 14:15:41.921 I LMDB Mapsize increased.  Old: 13830MiB, New: 14342MiB
2023-04-19 14:16:46.818 I LMDB Mapsize increased.  Old: 14342MiB, New: 14854MiB
2023-04-19 14:17:51.209 I LMDB Mapsize increased.  Old: 14854MiB, New: 15366MiB
2023-04-19 14:18:56.972 I LMDB Mapsize increased.  Old: 15366MiB, New: 15879MiB
2023-04-19 14:20:03.512 I LMDB Mapsize increased.  Old: 15879MiB, New: 16391MiB
2023-04-19 14:21:40.624 I LMDB Mapsize increased.  Old: 16391MiB, New: 16903MiB
2023-04-19 14:23:32.665 I LMDB Mapsize increased.  Old: 16903MiB, New: 17415MiB
2023-04-19 14:25:20.799 I LMDB Mapsize increased.  Old: 17415MiB, New: 17927MiB
2023-04-19 14:27:09.011 I LMDB Mapsize increased.  Old: 17927MiB, New: 18439MiB
2023-04-19 14:28:21.919 I LMDB Mapsize increased.  Old: 18439MiB, New: 18952MiB
2023-04-19 14:29:00.555 I Copying txs_prunable_hash
2023-04-19 14:30:09.870 I LMDB Mapsize increased.  Old: 18952MiB, New: 19464MiB
2023-04-19 14:31:58.423 I LMDB Mapsize increased.  Old: 19464MiB, New: 19977MiB
2023-04-19 14:33:46.907 I LMDB Mapsize increased.  Old: 19977MiB, New: 20489MiB
2023-04-19 14:34:18.277 I Copying tx_indices
2023-04-19 14:35:23.987 I LMDB Mapsize increased.  Old: 20489MiB, New: 21001MiB
2023-04-19 14:36:54.061 I LMDB Mapsize increased.  Old: 21001MiB, New: 21513MiB
2023-04-19 14:38:25.463 I LMDB Mapsize increased.  Old: 21513MiB, New: 22025MiB
2023-04-19 14:39:57.358 I LMDB Mapsize increased.  Old: 22025MiB, New: 22537MiB
2023-04-19 14:41:29.392 I LMDB Mapsize increased.  Old: 22537MiB, New: 23049MiB
2023-04-19 14:43:00.269 I LMDB Mapsize increased.  Old: 23049MiB, New: 23561MiB
2023-04-19 14:44:30.411 I LMDB Mapsize increased.  Old: 23561MiB, New: 24073MiB
2023-04-19 14:44:50.043 I Copying tx_outputs
2023-04-19 14:45:58.673 I LMDB Mapsize increased.  Old: 24073MiB, New: 24585MiB
2023-04-19 14:47:53.884 I LMDB Mapsize increased.  Old: 24585MiB, New: 25097MiB
2023-04-19 14:49:19.937 I Copying output_txs
2023-04-19 14:49:28.210 I LMDB Mapsize increased.  Old: 25097MiB, New: 25609MiB
2023-04-19 14:50:07.566 I LMDB Mapsize increased.  Old: 25609MiB, New: 26121MiB
2023-04-19 14:50:50.289 I LMDB Mapsize increased.  Old: 26121MiB, New: 26633MiB
2023-04-19 14:52:01.642 I LMDB Mapsize increased.  Old: 26633MiB, New: 27145MiB
2023-04-19 14:53:39.033 I LMDB Mapsize increased.  Old: 27145MiB, New: 27657MiB
2023-04-19 14:55:09.696 I LMDB Mapsize increased.  Old: 27657MiB, New: 28169MiB
2023-04-19 14:56:41.637 I LMDB Mapsize increased.  Old: 28169MiB, New: 28681MiB
2023-04-19 14:58:14.614 I LMDB Mapsize increased.  Old: 28681MiB, New: 29193MiB                                                                                                   2023-04-19 15:00:14.620 I LMDB Mapsize increased.  Old: 29193MiB, New: 29705MiB
2023-04-19 15:00:50.815 I Copying output_amounts
2023-04-19 15:01:30.385 I LMDB Mapsize increased.  Old: 29705MiB, New: 30217MiB
2023-04-19 15:02:11.588 I LMDB Mapsize increased.  Old: 30217MiB, New: 30730MiB
2023-04-19 15:03:23.026 I LMDB Mapsize increased.  Old: 30730MiB, New: 31242MiB
2023-04-19 15:04:36.682 I LMDB Mapsize increased.  Old: 31242MiB, New: 31754MiB
2023-04-19 15:05:48.141 I LMDB Mapsize increased.  Old: 31754MiB, New: 32266MiB
2023-04-19 15:06:54.170 I LMDB Mapsize increased.  Old: 32266MiB, New: 32778MiB
2023-04-19 15:08:04.780 I LMDB Mapsize increased.  Old: 32778MiB, New: 33290MiB
2023-04-19 15:09:16.921 I LMDB Mapsize increased.  Old: 33290MiB, New: 33802MiB
2023-04-19 15:10:29.794 I LMDB Mapsize increased.  Old: 33802MiB, New: 34314MiB
2023-04-19 15:11:41.910 I LMDB Mapsize increased.  Old: 34314MiB, New: 34826MiB
2023-04-19 15:12:57.361 I LMDB Mapsize increased.  Old: 34826MiB, New: 35338MiB
2023-04-19 15:14:38.577 I LMDB Mapsize increased.  Old: 35338MiB, New: 35850MiB
2023-04-19 15:16:33.142 I LMDB Mapsize increased.  Old: 35850MiB, New: 36362MiB
2023-04-19 15:18:20.243 I LMDB Mapsize increased.  Old: 36362MiB, New: 36874MiB
2023-04-19 15:18:56.798 I LMDB Mapsize increased.  Old: 36874MiB, New: 37386MiB
2023-04-19 15:19:19.285 I LMDB Mapsize increased.  Old: 37386MiB, New: 37899MiB                                                                                                   2023-04-19 15:19:25.621 I Copying spent_keys
2023-04-19 15:20:15.066 I LMDB Mapsize increased.  Old: 37899MiB, New: 38411MiB
2023-04-19 15:21:47.458 I LMDB Mapsize increased.  Old: 38411MiB, New: 38923MiB
2023-04-19 15:23:19.651 I LMDB Mapsize increased.  Old: 38923MiB, New: 39435MiB
......
2023-04-19 15:55:01.514 I LMDB Mapsize increased.  Old: 85153MiB, New: 85667MiB
2023-04-19 15:56:00.529 I LMDB Mapsize increased.  Old: 85667MiB, New: 86181MiB
2023-04-19 15:56:54.920 I LMDB Mapsize increased.  Old: 86181MiB, New: 86693MiB
2023-04-19 15:57:58.519 I LMDB Mapsize increased.  Old: 86693MiB, New: 87208MiB
2023-04-19 15:59:00.415 I LMDB Mapsize increased.  Old: 87208MiB, New: 87720MiB
2023-04-19 16:00:07.311 I LMDB Mapsize increased.  Old: 87720MiB, New: 88234MiB
2023-04-19 16:01:02.352 I LMDB Mapsize increased.  Old: 88234MiB, New: 88748MiB
2023-04-19 16:02:08.029 I LMDB Mapsize increased.  Old: 88748MiB, New: 89262MiB
2023-04-19 16:02:44.561 E Exception at [Pruning error], what=Failed to write txs_prunable record: MDB_BAD_VALSIZE: Unsupported size of key/DB name/data, or wrong DUPFIXED size
```

# Discussion History
## selsta | 2023-04-20T05:56:22+00:00
Your initial command makes it seem like your node is already pruned, what's the size of your existing blockchain file?

Is `/mnt/` in your data-dir a network drive?

## YuXiaoCoder | 2023-04-20T09:18:26+00:00
@selsta Yes, I have prune before, and now the file size is 139G, I want to prune again, it is a local disk, not a network device

## moneromooo-monero | 2023-04-20T16:00:55+00:00
Is this repeatable ?
Looking at what can cause this error, it's not obvious what might be wrong.
In any case, a pruned DB should be about 60 GB, so if a pruned DB is at least 89 GB, something is already wrong somewhere.
If you can repeat it, then it may be worth trying with:
```
diff --git a/src/blockchain_utilities/blockchain_prune.cpp b/src/blockchain_utilities/blockchain_prune.cpp
index a78d7ada9..2afc7c5b4 100644
--- a/src/blockchain_utilities/blockchain_prune.cpp
+++ b/src/blockchain_utilities/blockchain_prune.cpp
@@ -665,7 +665,7 @@ int main(int argc, char* argv[])
   copy_table(env0, env1, "properties", 0, 0, BlockchainLMDB::compare_string);
   if (already_pruned)
   {
-    copy_table(env0, env1, "txs_prunable", MDB_INTEGERKEY, 0, BlockchainLMDB::compare_uint64);
+    copy_table(env0, env1, "txs_prunable", MDB_INTEGERKEY, MDB_APPEND, BlockchainLMDB::compare_uint64);
     copy_table(env0, env1, "txs_prunable_tip", MDB_INTEGERKEY | MDB_DUPSORT | MDB_DUPFIXED, 0, BlockchainLMDB::compare_uint64);
   }
   else
```
and see if that fixes it. This flag is used by monerod, and theoretically it should only just make it faster (so good anyway), but it also happens to bypass some of the code which could return that error, so would be a good way to rule out some of the possible causes.



## YuXiaoCoder | 2023-04-21T02:00:52+00:00
@moneromooo-monero I will try to prune again, this process may take a few hours, I will sync to here when I have the results

## YuXiaoCoder | 2023-04-21T17:41:19+00:00
I still cleaned the lmdb-pruned/ directory and re-executed the pruning command, still got the same error
```bash
2023-04-21 04:01:30.382 I LMDB Mapsize increased.  Old: 84127MiB, New: 84639MiB
2023-04-21 04:02:30.487 I LMDB Mapsize increased.  Old: 84639MiB, New: 85153MiB
2023-04-21 04:03:43.913 I LMDB Mapsize increased.  Old: 85153MiB, New: 85667MiB
2023-04-21 04:04:43.113 I LMDB Mapsize increased.  Old: 85667MiB, New: 86181MiB
2023-04-21 04:05:36.964 I LMDB Mapsize increased.  Old: 86181MiB, New: 86693MiB
2023-04-21 04:06:38.401 I LMDB Mapsize increased.  Old: 86693MiB, New: 87208MiB
2023-04-21 04:07:38.753 I LMDB Mapsize increased.  Old: 87208MiB, New: 87720MiB
2023-04-21 04:08:44.350 I LMDB Mapsize increased.  Old: 87720MiB, New: 88234MiB
2023-04-21 04:09:37.169 I LMDB Mapsize increased.  Old: 88234MiB, New: 88748MiB
2023-04-21 04:10:40.259 I LMDB Mapsize increased.  Old: 88748MiB, New: 89262MiB
2023-04-21 04:11:15.703 E Exception at [Pruning error], what=Failed to write txs_prunable record: MDB_BAD_VALSIZE: Unsupported size of key/DB name/data, or wrong DUPFIXED size
```

## moneromooo-monero | 2023-04-21T19:49:13+00:00
Could you put up the source db up for download somewhere if possible ?

## DeeDeeRanged | 2023-05-25T17:22:58+00:00
AFAIK when an existing db has been pruned the file size stays the same i.e if it is 140GB it stays 140GB only inside the db is pruned. I solved it by doing the same setup on another PC and added to monerod --prune-blockchain --sync-pruned-blocks.
Tried pruning the db last year and it didn't shrink the file size.
As I had a spare PC made an extra monero node with the extra --prune-blockchain and --sync-pruned-blocks on the command line and let it rebuild the db file, took abt 12 hours for the db to build, copied the file over to my main node and that worked.

At the moment my db file now is abt 61GB.


## jnitecki | 2024-01-26T14:31:28+00:00
There is clearly something wrong with monero-blockchain-prune tool. 
My scenario was similar to the above with identical effect (as far as I understood my predecessor).

1) Originally I synced the full blockchain - the size was 175G
2) Then I have discovered --prune-blockchain switch for monerod - run monerod with it for couple of days and database size stayed the same 
3) Then I have realized that using the --prune-blockchain in monerod will actually not make the file smaller - so fact that it stayed the same in point 2 was as expected
4) So in order to actually I have decided to run to run monero-blockchain-prune tool. At first is has failed with message that database is already pruned (indeed it was) and suggested to run with copy-pruned-database option, so I did so
5) Now that process monero-blockchain-prune with --copy-pruned-database is still running (since two weeks), and the new file is growing - it is already reached 126G (which is much more than I would expect from database after pruned blocks have been removed (I would assume the --copy-pruned-database should do that).  Based on last entry in the log: LMDB Mapsize increased. Old: 129383MiB, New; 129895MiB, it looks data is being just copied as it is (but then why this takes 2 weeks?)

I have started separate process on different machine where monerod was started from the beginning with --prune-database switch and there (I'm still on 90% of blockchain synchronization), my database if only 52G - clearly much less than also not yet completed effect of monero-blockchain-prune.......

I will let both processes to complete and will share the final result, but all signs show that monero-blockchain-prune simply does not work (at least not in the way I would expect).

# Action History
- Created by: YuXiaoCoder | 2023-04-20T01:14:05+00:00
