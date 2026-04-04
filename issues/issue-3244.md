---
title: Stopped syncing after "BLOCK ADDED AS INVALID"
source_url: https://github.com/monero-project/monero/issues/3244
author: MoroccanMalinois
assignees: []
labels: []
created_at: '2018-02-08T12:31:10+00:00'
updated_at: '2018-03-05T21:41:39+00:00'
type: issue
status: closed
closed_at: '2018-03-05T21:41:39+00:00'
---

# Original Description
Using current master with #3231, monerod stopped syncing (Happened twice, each time trying to sync from scratch). There is this `ERROR` a few lines after the last `BLOCK SUCCESSFULLY ADDED`

> 2018-02-08 07:38:29.445 [P2P7]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3417 Block with id: <e4dd4928c856c5446b5d2a5c5c2f63a448d224b0abd63ed895b86487044cc380> has at least one transaction (id: <f245881276e90a0319e09fa82b6dc18746626ab80f52edac60b865e5757d5245>) with wrong inputs.
> 2018-02-08 07:38:29.452 [P2P7]  INFO    blockchain      src/cryptonote_core/blockchain.cpp:2160 BLOCK ADDED AS INVALID: <e4dd4928c856c5446b5d2a5c5c2f63a448d224b0abd63ed895b86487044cc380>
> , prev_id=<3661a80e3387231e47800fb28dc638ee11ba0590aa522049519470707b291019>, m_invalid_blocks count=1
> 2018-02-08 07:38:29.455 [P2P7]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3420 Block with id <e4dd4928c856c5446b5d2a5c5c2f63a448d224b0abd63ed895b86487044cc380> added as invalid because of wrong inputs in transactions
> 2018-02-08 07:38:29.456 [P2P7]  INFO    txpool  src/cryptonote_core/tx_pool.cpp:299     Transaction added to pool: txid <f245881276e90a0319e09fa82b6dc18746626ab80f52edac60b865e5757d5245> bytes: 1495 fee/byte: 1.33779e+07
> 2018-02-08 07:38:29.457 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1105    [195.201.8.253:18080 OUT] Block verification failed, dropping connection

Another run:

> 2018-02-05 19:55:41.656 [P2P3]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3417 Block with id: <1f956b6995fd784ead48de4bad9b847ce1dcc5e35d03402bd7cbec5c9c59799b> has at least one transaction (id: <82342bcff7a4df4c9a37a8ab1750a39e1fbf1650289b68c823a0839232ac53a2>) with wrong inputs.
> 2018-02-05 19:55:41.656 [P2P3]  INFO    blockchain      src/cryptonote_core/blockchain.cpp:2160 BLOCK ADDED AS INVALID: <1f956b6995fd784ead48de4bad9b847ce1dcc5e35d03402bd7cbec5c9c59799b>
> , prev_id=<bf94053e8869763dddaa2f634828a09d28a4689a114fa198329e5b96d5b510a1>, m_invalid_blocks count=1
> 2018-02-05 19:55:41.656 [P2P3]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3420 Block with id <1f956b6995fd784ead48de4bad9b847ce1dcc5e35d03402bd7cbec5c9c59799b> added as invalid because of wrong inputs in transactions
> 2018-02-05 19:55:41.656 [P2P3]  INFO    txpool  src/cryptonote_core/tx_pool.cpp:299     Transaction added to pool: txid <82342bcff7a4df4c9a37a8ab1750a39e1fbf1650289b68c823a0839232ac53a2> bytes: 514 fee/byte: 2.00683e+08
> 2018-02-05 19:55:41.656 [P2P3]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1105    [94.209.12.249:18080 OUT] Block verification failed, dropping connection

Here's a sample of the current log. 

> 2018-02-08 11:57:02.972	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[223.95.79.59:20080 OUT] **Sync data returned a new top block candidate: 1128036 -> 1505076** [Your node is 377040 blocks (523 days) behind] 
> SYNCHRONIZATION started
> 2018-02-08 11:57:02.973	[P2P0]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:313	Remote blockchain height: 1505076, id: <bae12338c71a5b0a0c62159b87d5d388b8d8db34e85c5d869d3b67571f8ecb95>
> 2018-02-08 11:57:03.014	[P2P6]	INFO 	net.p2p	src/p2p/net_node.inl:1720	[122.226.181.85:58984 f8f9c6d4-8510-19d1-ff3d-941ab0a96643 INC] NEW CONNECTION
> 2018-02-08 11:57:03.520	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[92.63.251.85:18080 OUT] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
> 2018-02-08 11:57:04.117	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1735	[122.226.181.85:58984 f8f9c6d4-8510-19d1-ff3d-941ab0a96643 INC] CLOSE CONNECTION
> 2018-02-08 11:57:05.193	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[92.63.251.85:18080 OUT] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
> 2018-02-08 11:57:05.196	[P2P8]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1212	[223.95.79.59:20080 OUT]  kicking idle peer
> 2018-02-08 11:57:05.196	[P2P8]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1212	[80.241.216.213:37802 INC]  kicking passive peer
> 2018-02-08 11:57:05.197	[P2P5]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1722	**Target height decreasing from 1505076 to 1010016**
> 2018-02-08 11:57:05.197	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1735	[223.95.79.59:20080 13bc3340-7c52-367b-ee07-dc245d478b2d OUT] CLOSE CONNECTION
> 2018-02-08 11:57:05.197	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1735	[80.241.216.213:37802 ab96ab79-b0cb-f7c5-441f-85642c8f92f0 INC] CLOSE CONNECTION
> 2018-02-08 11:57:06.005	[P2P5]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[31.209.5.117:44542 INC] Received NOTIFY_REQUEST_CHAIN (29 blocks
> 2018-02-08 11:57:07.578	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[31.209.5.117:44542 INC] Received NOTIFY_REQUEST_CHAIN (29 blocks
> 2018-02-08 11:57:09.221	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[31.209.5.117:44542 INC] Received NOTIFY_REQUEST_CHAIN (29 blocks
> 2018-02-08 11:57:09.475	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[178.32.193.206:18080 OUT] Received NOTIFY_REQUEST_CHAIN (28 blocks
> 2018-02-08 11:57:09.904	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[121.206.131.83:59174 INC] Received NOTIFY_REQUEST_CHAIN (26 blocks
> 2018-02-08 11:57:10.665	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[50.35.81.181:18080 OUT] Received NOTIFY_REQUEST_CHAIN (28 blocks
> 2018-02-08 11:57:11.089	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[174.80.107.189:18080 OUT] Received NOTIFY_REQUEST_CHAIN (30 blocks
> 2018-02-08 11:57:11.274	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[159.89.185.133:18080 OUT] Received NOTIFY_REQUEST_CHAIN (30 blocks
> 2018-02-08 11:57:11.473	[P2P7]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[31.209.5.117:44542 INC] Received NOTIFY_REQUEST_CHAIN (29 blocks
> 2018-02-08 11:57:11.975	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:902	[0.0.0.0:0 OUT] Connect failed to 97.127.0.151:18080
> 2018-02-08 11:57:13.581	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[31.209.5.117:44542 INC] Received NOTIFY_REQUEST_CHAIN (29 blocks
> 2018-02-08 11:57:14.465	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[31.209.5.117:44542 INC] Received NOTIFY_REQUEST_CHAIN (29 blocks
> 2018-02-08 11:57:16.956	[P2P5]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1231	[31.209.5.117:44542 INC] Received NOTIFY_REQUEST_CHAIN (29 blocks
> 2018-02-08 11:57:16.977	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:902	[0.0.0.0:0 OUT] Connect failed to 67.181.22.36:18080
> 2018-02-08 11:57:17.094	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1720	[142.196.94.57:18080 3c2cb7f7-a46c-e1c8-16ed-39879c677b42 OUT] NEW CONNECTION
> 2018-02-08 11:57:18.262	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1720	[142.196.94.57:63523 5750931e-0fc8-b6ab-3e41-0e6cf24f7cb6 INC] NEW CONNECTION

It resumes syncing if I restart monerod.

# Discussion History
## moneromooo-monero | 2018-02-08T15:22:01+00:00
Can you paste a few dozen lines extra before the first line in those ?

## moneromooo-monero | 2018-02-08T15:48:12+00:00
And if you run again, please add log with DEBUG level.

## MoroccanMalinois | 2018-02-08T15:49:30+00:00
Sure:  https://pastebin.mozilla.org/9077601 and https://pastebin.mozilla.org/9077603

## iDunk5400 | 2018-02-08T17:19:50+00:00
In your first paste, on line 116, there seems to be a peer stuck on a v4 fork (or an alternative v5 fork) past the v5 hardfork height (1288616). Maybe you are getting transactions from that peer with outputs that are invalid this side of the fork.

## moneromooo-monero | 2018-02-08T17:22:05+00:00
Can you please try with this patch (it just adds logs):

```
From be67bcd5cc4d9acd1b94c307ab3041083aa7cbaa Mon Sep 17 00:00:00 2001
From: moneromooo-monero <moneromooo-monero@users.noreply.github.com>
Date: Thu, 8 Feb 2018 17:18:18 +0000
Subject: [PATCH] blockchain: debug logs

---
 src/cryptonote_core/blockchain.cpp | 5 +++++
 1 file changed, 5 insertions(+)

diff --git a/src/cryptonote_core/blockchain.cpp b/src/cryptonote_core/blockchain.cpp
index 178479f..49807ec 100644
--- a/src/cryptonote_core/blockchain.cpp
+++ b/src/cryptonote_core/blockchain.cpp
@@ -2301,6 +2301,7 @@ void Blockchain::on_new_tx_from_block(const cryptonote::transaction &tx)
   {
     TIME_MEASURE_START(a);
     m_blocks_txs_check.push_back(get_transaction_hash(tx));
+MINFO("Adding new tx from block: " << get_transaction_hash(tx) << ", now " << m_blocks_txs_check.size() << " txids in vector");
     TIME_MEASURE_FINISH(a);
     if(m_show_time_stats)
     {
@@ -3331,6 +3332,7 @@ leave:
 // XXX old code adds miner tx here
 
   size_t tx_index = 0;
+MINFO("Going through " << bl.tx_hashes.size() << " txes");
   // Iterate over the block's transaction hashes, grabbing each
   // from the tx_pool and validating them.  Each is then added
   // to txs.  Keys spent in each are added to <keys> by the double spend check.
@@ -3412,6 +3414,7 @@ leave:
     {
       // ND: if fast_check is enabled for blocks, there is no need to check
       // the transaction inputs, but do some sanity checks anyway.
+      MINFO("checking m_blocks_txs_check, size " <<m_blocks_txs_check.size() << ", tx_index " << tx_index << ", tx_id " << tx_id << ", el " << (tx_index >= m_blocks_txs_check.size() ? "-" : epee::string_tools::pod_to_hex(m_blocks_txs_check[tx_index])));
       if (tx_index >= m_blocks_txs_check.size() || memcmp(&m_blocks_txs_check[tx_index++], &tx_id, sizeof(tx_id)) != 0)
       {
         MERROR_VER("Block with id: " << id << " has at least one transaction (id: " << tx_id << ") with wrong inputs.");
@@ -3430,6 +3433,7 @@ leave:
     cumulative_block_size += blob_size;
   }
 
+  MINFO("clearing m_blocks_txs_check");
   m_blocks_txs_check.clear();
 
   TIME_MEASURE_START(vmt);
@@ -3709,6 +3713,7 @@ bool Blockchain::cleanup_handle_incoming_blocks(bool force_sync)
   TIME_MEASURE_FINISH(t1);
   m_blocks_longhash_table.clear();
   m_scan_table.clear();
+  MINFO("clearing m_blocks_txs_check");
   m_blocks_txs_check.clear();
   m_check_txin_table.clear();
 
-- 
2.9.5

```

## MoroccanMalinois | 2018-02-08T17:47:19+00:00
Sure

## MoroccanMalinois | 2018-02-09T13:09:32+00:00
https://paste.fedoraproject.org/paste/FY2xyPqkmsXmxdbp89p4ig

## moneromooo-monero | 2018-02-09T17:15:31+00:00
Try https://github.com/moneromooo-monero/bitmonero/tree/lajfka

## MoroccanMalinois | 2018-02-10T15:07:58+00:00
Looks similar https://paste.fedoraproject.org/paste/UQ6oJafl8PtkDCpuHFdWhw

## moneromooo-monero | 2018-02-10T19:34:19+00:00
OK, I added more logs in https://github.com/moneromooo-monero/bitmonero/tree/lajfka

## MoroccanMalinois | 2018-02-13T03:20:14+00:00
Segfault for this time (sorry no backtrace) https://paste.fedoraproject.org/paste/ERf0My0Evd9Z1lMWcXnPxQ

## moneromooo-monero | 2018-02-13T09:55:36+00:00
That crash appears to be unrelated, and fixed by https://github.com/monero-project/monero/pull/3248

## moneromooo-monero | 2018-02-18T19:20:03+00:00
Any luck ?

## MoroccanMalinois | 2018-02-18T22:00:50+00:00
Nope, it finished syncing successfully. Trying another run (it's on a very slow server)

## MoroccanMalinois | 2018-02-19T03:19:58+00:00
This is with the same commits as before (didn't update to last master) with  commit from #3248 in addition https://paste.fedoraproject.org/paste/i5Dt5ymQUdpYqd1FIIWIeg

## moneromooo-monero | 2018-02-19T09:28:09+00:00
I added a commit to the branch which should fix it.

## moneromooo-monero | 2018-02-21T17:56:29+00:00
That's not a good fix actually, looking again.

## moneromooo-monero | 2018-02-21T19:54:00+00:00
I think I have it :)
https://github.com/moneromooo-monero/bitmonero/tree/syncfail
This replaces lajfka altogether.

## moneromooo-monero | 2018-02-23T15:49:09+00:00
I'll PR it now as I understand why it failed, and why this fixes it. Hopefully that fixes it for you :)


## MoroccanMalinois | 2018-03-02T18:01:35+00:00
Thanks mooo, synced twice OK (one with the version before hyc's review, and the last one). 

## moneromooo-monero | 2018-03-02T18:05:22+00:00
Excellent, thanks for confirming!

## MoroccanMalinois | 2018-03-05T21:41:39+00:00
Fixed by #3308 

# Action History
- Created by: MoroccanMalinois | 2018-02-08T12:31:10+00:00
- Closed at: 2018-03-05T21:41:39+00:00
