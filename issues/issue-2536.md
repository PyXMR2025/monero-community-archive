---
title: 'monerod: sync stuck'
source_url: https://github.com/monero-project/monero/issues/2536
author: ghost
assignees: []
labels: []
created_at: '2017-09-26T20:38:27+00:00'
updated_at: '2022-05-05T08:32:40+00:00'
type: issue
status: closed
closed_at: '2017-10-24T10:56:25+00:00'
---

# Original Description
Ubuntu (16.04.3 LTS), native build of master branch (due to bug #2521 to have fix #2492)

Sync process stuck on one point.
I tried to start monerod with "--block-sync-size 1" and "--block-sync-size 20"
I tried with different internet access links (including good one), results are the same.

Logs are full of stuff like this:

2017-09-26 10:09:24.755 [P2P2] WARN net.p2p src/p2p/net_node.inl:722 [212.83.172.165:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-26 10:09:24.755 [P2P0] WARN net.p2p src/p2p/net_node.inl:771 [212.83.172.165:28080 OUT] COMMAND_HANDSHAKE Failed
2017-09-26 10:09:25.257 [P2P9] WARN net.p2p src/p2p/net_node.inl:1594 [212.83.175.67:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-09-26 10:09:26.071 [P2P8] INFO global src/cryptonote_protocol/cryptonote_protocol_handler.inl:305 [207.244.103.152:18080 OUT] Sync data returned a new top block candidate: 1358593 -> 1407453 [Your node is 48860 blocks (67 days) behind]
SYNCHRONIZATION started
2017-09-26 10:09:30.631 [P2P4] ERROR verify src/cryptonote_core/blockchain.cpp:3401 Block with id: has at least one transaction (id: <4e9f0f57c64b6caa7fcb2faaee7aabb6fd00ea31a9fb9d7b77d9f34ef56d3c2d>) with wrong inputs.
2017-09-26 10:09:30.632 [P2P4] ERROR verify src/cryptonote_core/blockchain.cpp:3404 Block with id added as invalid because of wrong inputs in transactions
2017-09-26 10:09:33.878 [P2P9] ERROR verify src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = , height 1358594, parent in alt 0, parent in main 0 (parent , current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)
2017-09-26 10:09:38.998 [P2P4] WARN net.p2p src/p2p/net_node.inl:743 [50.53.99.93:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
2017-09-26 10:09:38.999 [P2P0] WARN net.p2p src/p2p/net_node.inl:771 [50.53.99.93:18080 OUT] COMMAND_HANDSHAKE Failed
2017-09-26 10:09:42.488 [P2P8] ERROR verify src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = , height 1358594, parent in alt 0, parent in main 0 (parent , current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)
2017-09-26 10:09:44.788 [P2P6] ERROR net.cn src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021 [176.9.2.145:8180 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-09-26 10:09:47.245 [P2P4] ERROR net.cn src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021 [91.213.203.48:18080 OUT] Got block with unknown parent which was not requested - querying block hashes

# Discussion History
## moneromooo-monero | 2017-09-26T21:01:17+00:00
Can you please restart with `--log-level 1,\*verify\*:DEBUG` and post the log again ? It looks like you're being given the right data, but can't accept it, which hints at a previous error. Also search the log for that previous error, if any.

There's also some very weird stuff, like: , id = , 
There should have been a hash written there, but there isn't. Makes me wonder if the build is bad somehow.

## ghost | 2017-09-27T09:25:35+00:00
> Can you please restart with --log-level 1,\*verify\*:DEBUG and post the log again ?

I don't see much difference in log output with ```--log-level 1,\*verify\*:DEBUG``` added (also tried ```*verify*:DEBUG```; I don't undestand correct syntax for --log-level)

```
Use the "help" command to see the list of available commands.
**********************************************************************

2017-09-27 08:59:42.172 [P2P1]  WARN    net.dns src/common/dns_utils.cpp:483    WARNING: no two valid MoneroPulse DNS checkpoint records were received                                                                                                    
2017-09-27 08:59:43.256 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [5.14.249.222:18080 OUT] Sync data returned a new top block candidate: 1358593 -> 1408136 [Your node is 49543 blocks (68 days) behind]    
SYNCHRONIZATION started                                                                                                      
2017-09-27 08:59:55.476 [P2P4]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3401 Block with id: <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42> has at least one transaction (id: <4e9f0f57c64b6caa7fcb2faaee7aabb6fd00ea31a9fb9d7b77d9f34ef56d3c2d>) with wrong inputs.                                                                                     
2017-09-27 08:59:55.477 [P2P4]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3404 Block with id <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42> added as invalid because of wrong inputs in transactions                         
2017-09-27 08:59:55.983 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = <a2fb4f1f3be520e889d5d92d67b649be5516bf76bf48c4d1370bfdd36cfa3ca1>, height 1358594, parent in alt 0, parent in main 0 (parent <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42>, current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)                                                                     
2017-09-27 08:59:57.279 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [163.172.255.58:18080 OUT] Sync data returned a new top block candidate: 1358593 -> 1408136 [Your node is 49543 blocks (68 days) behind]  
SYNCHRONIZATION started                                                                                                      
2017-09-27 09:00:07.810 [P2P9]  WARN    net.p2p src/p2p/net_node.inl:743        [148.251.128.163:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.                                                 
2017-09-27 09:00:07.810 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [148.251.128.163:18080 OUT] COMMAND_HANDSHAKE Failed                                                                                                                      
2017-09-27 09:00:08.582 [P2P2]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = <a2fb4f1f3be520e889d5d92d67b649be5516bf76bf48c4d1370bfdd36cfa3ca1>, height 1358594, parent in alt 0, parent in main 0 (parent <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42>, current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)                                                                     
2017-09-27 09:00:09.036 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [178.63.96.4:18080 OUT] Got block with unknown parent which was not requested - querying block hashes                                     
2017-09-27 09:00:14.168 [P2P2]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [23.253.207.166:18080 OUT] Got block with unknown parent which was not requested - querying block hashes                                  
2017-09-27 09:00:30.224 [P2P1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = <a2fb4f1f3be520e889d5d92d67b649be5516bf76bf48c4d1370bfdd36cfa3ca1>, height 1358594, parent in alt 0, parent in main 0 (parent <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42>, current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)                                                                     
2017-09-27 09:00:30.709 [P2P6]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = <a2fb4f1f3be520e889d5d92d67b649be5516bf76bf48c4d1370bfdd36cfa3ca1>, height 1358594, parent in alt 0, parent in main 0 (parent <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42>, current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)                                                                     
2017-09-27 09:00:33.744 [P2P7]  WARN    net.p2p src/p2p/net_node.inl:743        [128.68.82.77:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.                                                    
2017-09-27 09:00:33.744 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [128.68.82.77:18080 OUT] COMMAND_HANDSHAKE Failed                                                                                                                         
2017-09-27 09:00:35.974 [P2P6]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [163.172.157.163:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-09-27 09:00:36.047 [P2P2]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:928     returned not all requested objects (context.m_requested_objects.size()=1), dropping connection
2017-09-27 09:00:39.775 [P2P9]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = <a2fb4f1f3be520e889d5d92d67b649be5516bf76bf48c4d1370bfdd36cfa3ca1>, height 1358594, parent in alt 0, parent in main 0 (parent <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42>, current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)
2017-09-27 09:00:40.795 [P2P1]  WARN    net.p2p src/p2p/net_node.inl:743        [50.53.99.93:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
2017-09-27 09:00:40.796 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [50.53.99.93:18080 OUT] COMMAND_HANDSHAKE Failed
2017-09-27 09:00:43.690 [P2P3]  WARN    net.p2p src/p2p/net_node.inl:743        [52.161.26.137:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
2017-09-27 09:00:43.690 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [52.161.26.137:18080 OUT] COMMAND_HANDSHAKE Failed
2017-09-27 09:00:45.902 [P2P9]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [163.172.157.163:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-09-27 09:00:52.696 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:743        [23.95.228.72:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
2017-09-27 09:00:52.696 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [23.95.228.72:18080 OUT] COMMAND_HANDSHAKE Failed
2017-09-27 09:00:55.842 [P2P1]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [163.172.157.163:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-09-27 09:01:02.103 [P2P9]  WARN    net.p2p src/p2p/net_node.inl:722        [153.192.34.103:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-27 09:01:02.103 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [153.192.34.103:18080 OUT] COMMAND_HANDSHAKE Failed
2017-09-27 09:01:04.485 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:743        [116.220.83.145:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
2017-09-27 09:01:04.485 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [116.220.83.145:18080 OUT] COMMAND_HANDSHAKE Failed
2017-09-27 09:01:04.713 [P2P2]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [163.172.157.163:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
```

> Also search the log for that previous error, if any.

Logs are basically from beginning.
This time I included ```Use the "help" command to see the list of available commands.``` that appears on start.

> There's also some very weird stuff, like: , id = ,

I'm sorry, my fault. Github markdown just cut it.



## ghost | 2017-09-27T09:30:29+00:00
> Also search the log for that previous error, if any.

The only thing I can think of is that I use the same lmdb as in bug #2521.
Can state of local blockhain DB cause this problem?

## moneromooo-monero | 2017-09-27T10:34:55+00:00
Sorry, the \ were to avoid github munging the * which it usually does. I guess I escaped twice and did not notice. And github munging explains the missing id, OK.

I think I know what's going on here: one of the txes is still in your pool, so isn't added to the m_blocks_txs_check, which is then causing the failure. This will need fixing. In the meantime, try this:

mdb_drop -s txpool_meta ~/.bitmonero/lmdb
mdb_drop -s txpool_blob ~/.bitmonero/lmdb

The source for mdb_drop is http://highlandsun.com/hyc/mdb_drop.c

Build with:

copy mdb_drop.c in monero's external/db_drivers/liblmdb
cd external/db_drivers/liblmdb
make
gcc mdb_drop.c -o mdb_drop liblmdb.a -lpthread


## ghost | 2017-09-27T18:00:14+00:00
> mdb_drop -s txpool_meta ~/.bitmonero/lmdb
mdb_drop -s txpool_blob ~/.bitmonero/lmdb

Those actions have helped. Now sync process continues. Thank you.

> This will need fixing.

So issue remains open.

## moneromooo-monero | 2017-09-29T20:35:44+00:00
Should be fixed by https://github.com/monero-project/monero/pull/2552

## webworxs | 2017-10-02T12:40:39+00:00
Hi, I have a similar problem, the only difference is I'm running under Windows 7 64x. 
 Please see this thread for details https://forum.getmonero.org/5/support/88676/monero-sync-is-stuck  Can anybody help me get this issue sorted?  I need to access my wallet urgently.

## moneromooo-monero | 2017-10-02T14:01:38+00:00
And are you using the patch in 2552 ?

## webworxs | 2017-10-02T16:23:29+00:00
I didn't realise the Windows build was there too, my mistake.  Replaced all my local files with the ones contained in the tarball located here https://build.getmonero.org/builders/monero-static-win64/builds/2417
I still can't sync, the chain height remains at the same level.  Here is my log:


## webworxs | 2017-10-02T16:32:02+00:00
    2017-10-02 16:07:19.717	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.723	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.729	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.731	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.742	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.751	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.755	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.760	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.762	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.767	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.771	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.775	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.781	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.787	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.791	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.796	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.801	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.805	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.812	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.814	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.819	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.823	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.829	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.832	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.838	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.842	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.847	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.851	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.856	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.862	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.867	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.879	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.885	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.891	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.896	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.898	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.904	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.911	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.913	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.919	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.922	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.927	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.930	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.935	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.940	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.944	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.955	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.962	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.967	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.978	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.985	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.990	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.995	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:19.998	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.003	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.006	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.011	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.016	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.021	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.025	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.030	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.035	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.039	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.046	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.048	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.054	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.059	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.063	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.069	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.074	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.078	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.084	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.091	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.095	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.101	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.105	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.111	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.115	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.125	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.130	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.136	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.143	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.149	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.155	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.161	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.164	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.172	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.178	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.181	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.187	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.192	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.198	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.207	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.213	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.219	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.223	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.227	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.232	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.236	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.244	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.247	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.257	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.263	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.269	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.274	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.279	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.282	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.287	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.290	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.296	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.300	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.305	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.308	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.312	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.318	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.322	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.328	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.332	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.340	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.345	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.348	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.353	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.357	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.362	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.366	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.370	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.374	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.378	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.382	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.388	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.394	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.396	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.401	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.404	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.407	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.411	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.416	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.419	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.423	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.426	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.431	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.434	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.438	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.443	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.448	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.453	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.458	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.461	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.466	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.472	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.476	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.481	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.487	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.490	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.495	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.500	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.504	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.509	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.512	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.516	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.520	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.522	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.527	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.531	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.535	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.540	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.543	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[46.200.133.159:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:07:20.544	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.545	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[82.198.13.42:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:07:20.545	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[78.131.52.231:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:07:20.546	[P2P2]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[71.61.181.231:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-02 16:07:20.551	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[71.61.181.231:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:07:20.552	[P2P2]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[71.61.181.231:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-02 16:07:20.552	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
    2017-10-02 16:07:20.626	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
    2017-10-02 16:07:20.627	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:184	Node stopped.
    2017-10-02 16:07:20.628	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
    2017-10-02 16:07:20.629	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
    2017-10-02 16:07:25.052	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
    2017-10-02 16:07:25.118	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
    2017-10-02 16:07:25.118	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
    2017-10-02 16:12:05.708	9516	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2017-10-02 16:12:05.708	9516	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,*verify*:DEBUG
    2017-10-02 16:12:05.708	9516	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-69ce33f2)
    2017-10-02 16:12:05.708	9516	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
    2017-10-02 16:12:05.709	9516	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
    2017-10-02 16:12:05.716	9516	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
    2017-10-02 16:12:13.876	9516	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
    2017-10-02 16:12:13.876	9516	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
    2017-10-02 16:12:13.877	9516	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
    2017-10-02 16:12:13.879	9516	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
    2017-10-02 16:12:13.879	9516	INFO 	global	src/daemon/core.h:73	Initializing core...
    2017-10-02 16:12:13.880	9516	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:320	Loading blockchain from folder F:\BackupsDontDelete\bitmonero\lmdb ...
    2017-10-02 16:12:14.139	9516	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:418	Loading checkpoints
    2017-10-02 16:13:05.347	9516	WARN 	net.dns	src/common/dns_utils.cpp:483	WARNING: no two valid MoneroPulse DNS checkpoint records were received
    2017-10-02 16:13:05.349	9516	INFO 	global	src/daemon/core.h:78	Core initialized OK
    2017-10-02 16:13:05.349	9516	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
    2017-10-02 16:13:05.352	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
    2017-10-02 16:13:05.405	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
    2017-10-02 16:13:05.516	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[85.92.236.73:64354 INC] Sync data returned a new top block candidate: 1390008 -> 1411128 [Your node is 21120 blocks (29 days) behind] 
    SYNCHRONIZATION started
    2017-10-02 16:13:06.032	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[85.92.236.73:64354 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:13:06.407	[P2P8]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1257	[1;33m
    **********************************************************************
    The daemon will start synchronizing with the network. This may take a long time to complete.
    
    You can set the level of process detailization* through "set_log <level|categories>" command*,
    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)
    
    Use the "help" command to see the list of available commands.
    **********************************************************************
    [0m
    2017-10-02 16:13:07.518	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1532	[0.0.0.0:0 OUT] back ping connect failed to 85.92.236.73:18080
    2017-10-02 16:13:07.598	[P2P8]	WARN 	net.dns	src/common/dns_utils.cpp:483	WARNING: no two valid MoneroPulse DNS checkpoint records were received
    2017-10-02 16:13:08.803	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[103.208.86.41:18080 OUT] Sync data returned a new top block candidate: 1390008 -> 1411969 [Your node is 21961 blocks (30 days) behind] 
    SYNCHRONIZATION started
    2017-10-02 16:13:25.821	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:743	[46.4.82.71:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:13:25.822	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:771	[46.4.82.71:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:13:38.278	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:215	Output does not exist! amount = 50000000000
    2017-10-02 16:13:38.278	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3056	Failed to get output keys for tx with amount = 0.050000000000 and count indexes 5
    2017-10-02 16:13:38.279	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2662	Failed to check ring signature for tx <daea08855e3b8ea8f7e70e466d3e8034952ca817e1ab1f6e8c43e4bf73579ef4>  vin key with k_image: <cdfd71d784428021b97041b0d7ac2e285204158b0dd2e03d6779d27c655bf59d>  sig_index: 4
    2017-10-02 16:13:38.279	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3393	Block with id: <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66> has at least one transaction (id: <daea08855e3b8ea8f7e70e466d3e8034952ca817e1ab1f6e8c43e4bf73579ef4>) with wrong inputs.
    2017-10-02 16:13:38.279	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3397	Block with id <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66> added as invalid because of wrong inputs in transactions
    2017-10-02 16:13:38.331	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:215	Output does not exist! amount = 50000000000
    2017-10-02 16:13:38.332	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3056	Failed to get output keys for tx with amount = 0.050000000000 and count indexes 5
    2017-10-02 16:13:38.332	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2662	Failed to check ring signature for tx <daea08855e3b8ea8f7e70e466d3e8034952ca817e1ab1f6e8c43e4bf73579ef4>  vin key with k_image: <cdfd71d784428021b97041b0d7ac2e285204158b0dd2e03d6779d27c655bf59d>  sig_index: 4
    2017-10-02 16:13:38.332	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2665	  *pmax_used_block_height: 1188554
    2017-10-02 16:13:39.303	[P2P0]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:13:45.296	[P2P0]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[136.243.102.157:8180 OUT] Sync data returned a new top block candidate: 1390008 -> 1411970 [Your node is 21962 blocks (30 days) behind] 
    SYNCHRONIZATION started
    2017-10-02 16:13:47.927	[P2P7]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:13:53.069	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[211.159.138.158:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:13:54.764	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:13:57.170	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[139.59.96.215:18080 OUT] Sync data returned a new top block candidate: 1390008 -> 1411970 [Your node is 21962 blocks (30 days) behind] 
    SYNCHRONIZATION started
    2017-10-02 16:14:04.361	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.59.49.7:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:14:31.259	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:14:31.260	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:797	[176.31.117.66:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:14:33.241	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[163.172.255.58:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:14:41.498	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:797	[119.23.217.78:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:14:48.140	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:722	[212.3.125.187:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-02 16:14:48.140	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:771	[212.3.125.187:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:15:18.421	[P2P4]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:15:18.422	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:797	[37.59.49.7:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:15:35.810	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[91.121.86.165:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:15:36.032	[P2P4]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:15:37.784	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:743	[94.215.121.147:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:15:37.785	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:771	[94.215.121.147:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:15:39.907	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:1532	[0.0.0.0:0 OUT] back ping connect failed to 180.254.20.76:18080
    2017-10-02 16:15:41.905	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[46.200.133.159:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:15:48.102	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[13.80.144.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:16:00.557	[P2P0]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:16:00.558	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[211.159.138.158:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:16:02.665	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:16:02.666	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:797	[139.59.96.215:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:16:35.401	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:16:35.402	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:797	[139.59.213.181:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:16:35.907	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-02 16:16:35.907	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-02 16:16:37.833	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[37.59.49.7:28080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:16:44.303	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
    2017-10-02 16:16:44.304	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:797	[50.35.75.28:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:16:49.382	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:17:04.081	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:17:08.081	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:797	[82.200.204.104:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-02 16:17:18.153	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:722	[50.100.224.64:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-02 16:17:18.154	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:771	[50.100.224.64:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:17:23.629	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1653	[81.10.172.138:60831 INC] COMMAND_HANDSHAKE came, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:17:31.962	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:743	[61.68.132.21:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:17:31.963	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:771	[61.68.132.21:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:17:42.443	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:722	[84.20.120.186:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-02 16:17:42.444	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:771	[84.20.120.186:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:17:43.662	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:743	[168.235.70.221:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:17:43.663	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:771	[168.235.70.221:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:17:44.065	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:17:44.066	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:797	[188.221.65.43:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:17:44.818	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[82.247.184.64:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:17:47.165	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=80), dropping connection
    2017-10-02 16:17:47.166	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:797	[46.200.133.159:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:17:52.312	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:17:54.093	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:743	[195.154.182.94:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:17:54.094	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:771	[195.154.182.94:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:17:55.072	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:743	[96.255.38.79:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:17:55.073	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:771	[96.255.38.79:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:17:59.261	[P2P0]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[85.228.140.173:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:18:16.673	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1532	[0.0.0.0:0 OUT] back ping connect failed to 178.128.14.170:18080
    2017-10-02 16:18:43.202	[P2P0]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:18:43.248	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-02 16:18:43.249	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-02 16:18:52.281	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[88.198.184.41:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:18:52.288	[P2P4]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[88.198.184.41:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-02 16:18:53.963	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:18:58.802	[P2P0]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[13.80.144.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:19:01.984	[P2P4]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:19:01.985	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:797	[51.15.59.117:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:19:09.237	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[24.214.62.101:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:19:16.193	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:19:16.194	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:797	[211.159.138.158:38681 INC] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:19:25.754	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[5.44.168.124:52718 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-6, LEVIN_ERROR_CONNECTION_HANDLER_NOT_DEFINED)
    2017-10-02 16:19:27.431	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:1532	[0.0.0.0:0 OUT] back ping connect failed to 5.44.168.124:18080
    2017-10-02 16:19:54.927	[P2P0]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[13.80.144.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:02.299	[P2P0]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:09.491	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:15.252	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[24.214.62.101:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:18.304	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:21.348	[P2P0]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:28.286	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
    2017-10-02 16:20:30.609	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:38.144	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:42.365	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[141.226.246.13:40468 INC] Sync data returned a new top block candidate: 1390008 -> 1411973 [Your node is 21965 blocks (30 days) behind] 
    SYNCHRONIZATION started
    2017-10-02 16:20:48.050	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:52.828	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:56.142	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:20:59.039	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:03.929	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:04.045	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:09.138	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:10.904	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
    2017-10-02 16:21:17.589	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:18.094	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[24.214.62.101:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:19.251	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:20.826	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1557	[69.18.23.72:18080 OUT] back ping invoke wrong response "OK" from69.18.23.72:18080, hsh_peer_id=17405647899807795423, rsp.peer_id=11132740707485580209
    2017-10-02 16:21:28.523	[P2P4]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:30.074	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:33.874	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:35.138	[P2P7]	WARN 	net	contrib/epee/include/net/abstract_tcp_server2.inl:511	send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
    2017-10-02 16:21:35.138	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:696	[178.128.14.170:10797 INC] Failed to do_send()
    2017-10-02 16:21:35.145	[P2P9]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:561	[178.128.14.170:10797 INC] Failed to do_send
    2017-10-02 16:21:35.147	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:797	[178.128.14.170:10797 INC] COMMAND_TIMED_SYNC invoke failed. (-1, LEVIN_ERROR_CONNECTION)
    2017-10-02 16:21:35.147	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:814	[178.128.14.170:10797 INC] COMMAND_TIMED_SYNC Failed
    2017-10-02 16:21:35.148	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:814	[85.228.140.173:18080 OUT] COMMAND_TIMED_SYNC Failed
    2017-10-02 16:21:41.343	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:743	[24.130.13.138:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:21:41.343	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:771	[24.130.13.138:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:21:41.572	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:42.660	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1532	[0.0.0.0:0 OUT] back ping connect failed to 138.186.191.1:18080
    2017-10-02 16:21:46.559	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:722	[176.31.105.53:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-02 16:21:46.560	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:771	[176.31.105.53:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:21:48.851	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:50.010	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <f600661e0b62975f5a64d1e7bbeeda2696d27ec4e2718469f01149767d4867c4>, height 1390009, parent in alt 0, parent in main 0 (parent <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66>, current top <63038ebb94c531c6a5421bd3498a3db9efa6e2849754c9d2053092f475d50be5>, chain height 1390008)
    2017-10-02 16:21:54.081	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[13.80.144.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:55.021	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:56.421	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:21:57.760	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:743	[96.241.216.66:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:21:57.761	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:771	[96.241.216.66:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:22:03.833	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:22:07.490	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
    2017-10-02 16:22:15.181	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[107.167.93.58:57464 INC] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:22:22.509	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:22:47.202	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[50.79.174.253:60572 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:22:47.273	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1557	[69.18.23.72:18080 OUT] back ping invoke wrong response "OK" from69.18.23.72:18080, hsh_peer_id=17405647899807795423, rsp.peer_id=11132740707485580209
    2017-10-02 16:22:51.737	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:797	[121.75.62.241:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:22:56.081	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1532	[0.0.0.0:0 OUT] back ping connect failed to 66.25.11.24:18080
    2017-10-02 16:22:59.184	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:722	[82.208.180.250:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-02 16:22:59.184	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:771	[82.208.180.250:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:23:07.113	[P2P9]	WARN 	net.p2p	src/p2p/net_node.inl:743	[209.183.228.217:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-02 16:23:07.114	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:771	[209.183.228.217:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-02 16:23:34.978	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=60), dropping connection
    2017-10-02 16:23:34.979	[P2P2]	WARN 	net.p2p	src/p2p/net_node.inl:797	[13.80.144.211:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:23:38.899	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.902	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.905	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.911	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.913	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.915	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.918	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.921	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.924	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.927	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.931	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.936	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.940	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.942	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.945	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.949	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.952	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.956	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.959	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.962	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.967	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.970	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.974	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.977	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.980	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.984	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.988	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.991	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.994	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:38.998	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.003	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.007	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.009	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.011	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.013	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.015	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.016	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.018	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.021	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.025	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.033	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.037	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.040	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.043	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.047	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.051	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.055	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.058	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.060	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.063	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.067	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.071	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.075	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.078	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.080	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.084	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.088	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.091	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.095	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.099	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.103	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.106	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.110	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.113	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.117	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.122	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.125	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.129	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.133	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.137	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.140	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.143	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.147	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.151	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.155	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.158	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.163	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.166	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.169	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.174	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.177	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.181	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.185	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.188	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.192	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.195	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:23:39.199	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    
    2017-10-02 16:28:21.051	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.055	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.057	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.061	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.065	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.066	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[188.27.65.227:44190 INC] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:28:21.067	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[163.172.255.55:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-02 16:28:21.069	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.070	[P2P5]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[92.60.60.250:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-02 16:28:21.074	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.075	[P2P5]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[92.60.60.250:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-02 16:28:21.077	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[92.60.60.250:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-02 16:28:21.078	[P2P5]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[92.60.60.250:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-02 16:28:21.079	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
    2017-10-02 16:28:22.065	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
    2017-10-02 16:28:22.066	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:184	Node stopped.
    2017-10-02 16:28:22.068	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
    2017-10-02 16:28:22.068	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...

## moneromooo-monero | 2017-10-02T16:32:27+00:00
That bit below says you seem to have a corrupt db. It might be a bug which occured earlier. I'm afraid the only way out is to resync from scratch.


2017-10-02 16:13:38.278 [P2P9] ERROR verify src/cryptonote_core/blockchain.cpp:215 Output does not exist! amount = 50000000000
2017-10-02 16:13:38.278 [P2P9] ERROR verify src/cryptonote_core/blockchain.cpp:3056 Failed to get output keys for tx with amount = 0.050000000000 and count indexes 5
2017-10-02 16:13:38.279 [P2P9] ERROR verify src/cryptonote_core/blockchain.cpp:2662 Failed to check ring signature for tx vin key with k_image: sig_index: 4
2017-10-02 16:13:38.279 [P2P9] ERROR verify src/cryptonote_core/blockchain.cpp:3393 Block with id: <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66> has at least one transaction (id: ) with wrong inputs.
2017-10-02 16:13:38.279 [P2P9] ERROR verify src/cryptonote_core/blockchain.cpp:3397 Block with id <5f2013420db2f52e1374dc370ae4f31a5f7c9d5c46acfd8a50fb58eedd0cfd66> added as invalid because of wrong inputs in transactions


## webworxs | 2017-10-03T14:06:03+00:00
I'm still not succeeding.  I started from scratch.  The problem I have now is that I have to constantly restart the daemon in order to continue with the syncing.  Have a look at the error log below.  I'm not sure if it is related to the issue described in this thread or not.  I removed a lot of the repetitive line entries from my new log, but last night the daemon created a log file close to 300MB.

    2017-10-03 13:45:25.866	7500	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
    2017-10-03 13:45:25.866	7500	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,*verify*:DEBUG
    2017-10-03 13:45:25.866	7500	INFO 	global	src/daemon/main.cpp:283	Monero 'Helium Hydra' (v0.11.0.0-69ce33f2)
    2017-10-03 13:45:25.866	7500	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
    2017-10-03 13:45:25.866	7500	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
    2017-10-03 13:45:25.866	7500	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
    2017-10-03 13:45:33.163	7500	WARN 	net.p2p	src/p2p/net_node.inl:1982	UPnP device was found but not recognized as IGD.
    2017-10-03 13:45:33.163	7500	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
    2017-10-03 13:45:33.163	7500	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
    2017-10-03 13:45:33.163	7500	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
    2017-10-03 13:45:33.163	7500	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
    2017-10-03 13:45:33.163	7500	INFO 	global	src/daemon/core.h:73	Initializing core...
    2017-10-03 13:45:33.163	7500	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:320	Loading blockchain from folder f:\backupsdontdelete\bitmonero_cleanchain\lmdb ...
    2017-10-03 13:45:33.477	7500	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:418	Loading checkpoints
    2017-10-03 13:45:35.549	7500	WARN 	net.dns	src/common/dns_utils.cpp:483	WARNING: no two valid MoneroPulse DNS checkpoint records were received
    2017-10-03 13:45:35.549	7500	INFO 	global	src/daemon/core.h:78	Core initialized OK
    2017-10-03 13:45:35.549	7500	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
    2017-10-03 13:45:35.549	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
    2017-10-03 13:45:35.580	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
    2017-10-03 13:45:36.581	[P2P7]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1257	[1;33m
    **********************************************************************
    The daemon will start synchronizing with the network. This may take a long time to complete.
    
    You can set the level of process detailization* through "set_log <level|categories>" command*,
    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)
    
    Use the "help" command to see the list of available commands.
    **********************************************************************
    [0m
    2017-10-03 13:45:37.363	[P2P7]	WARN 	net.dns	src/common/dns_utils.cpp:483	WARNING: no two valid MoneroPulse DNS checkpoint records were received
    2017-10-03 13:45:41.852	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:722	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-03 13:45:41.852	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:771	[212.83.172.165:28080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:45:42.775	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[212.83.175.67:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:45:43.792	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[89.70.224.210:18080 OUT] Sync data returned a new top block candidate: 1224320 -> 1231302 [Your node is 6982 blocks (9 days) behind] 
    SYNCHRONIZATION started
    2017-10-03 13:45:46.485	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[89.70.224.210:18080 OUT]  Synced 1224340/1231302[0m
    2017-10-03 13:45:46.594	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[81.225.68.97:18080 OUT] Sync data returned a new top block candidate: 1224340 -> 1411722 [Your node is 187382 blocks (260 days) behind] 
    SYNCHRONIZATION started
    2017-10-03 13:45:47.171	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[89.70.224.210:18080 OUT]  Synced 1224360/1411722[0m
    2017-10-03 13:45:48.101	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[89.70.224.210:18080 OUT]  Synced 1224380/1411722[0m
    2017-10-03 13:45:49.353	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224400/1411722[0m
    2017-10-03 13:45:49.665	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[89.70.224.210:18080 OUT]  Synced 1224420/1411722[0m
    2017-10-03 13:45:53.198	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[37.153.231.94:18080 OUT]  Synced 1224440/1411722[0m
    2017-10-03 13:45:53.824	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[37.153.231.94:18080 OUT]  Synced 1224460/1411722[0m
    2017-10-03 13:45:53.949	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[37.153.231.94:18080 OUT]  Synced 1224480/1411722[0m
    2017-10-03 13:45:54.090	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[37.153.231.94:18080 OUT]  Synced 1224500/1411722[0m
    2017-10-03 13:45:54.168	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[37.153.231.94:18080 OUT]  Synced 1224520/1411722[0m
    2017-10-03 13:45:56.837	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224540/1411722[0m
    2017-10-03 13:45:59.688	[P2P7]	WARN 	net.p2p	src/p2p/net_node.inl:722	[94.224.64.74:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-03 13:45:59.688	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:771	[94.224.64.74:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:46:01.402	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[174.51.32.34:18080 OUT] Sync data returned a new top block candidate: 1224540 -> 1412248 [Your node is 187708 blocks (260 days) behind] 
    SYNCHRONIZATION started
    2017-10-03 13:46:03.725	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224560/1412248[0m
    2017-10-03 13:46:06.996	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[49.88.121.83:18080 OUT] Sync data returned a new top block candidate: 1224560 -> 1412614 [Your node is 188054 blocks (261 days) behind] 
    SYNCHRONIZATION started
    2017-10-03 13:46:07.979	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224580/1412614[0m
    2017-10-03 13:46:09.525	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[36.236.23.53:18080 OUT] Sync data returned a new top block candidate: 1224580 -> 1412615 [Your node is 188035 blocks (261 days) behind] 
    SYNCHRONIZATION started
    2017-10-03 13:46:12.022	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224600/1412615[0m
    2017-10-03 13:46:12.115	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224620/1412615[0m
    2017-10-03 13:46:12.240	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224640/1412615[0m
    2017-10-03 13:46:12.334	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224660/1412615[0m
    2017-10-03 13:46:12.412	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224680/1412615[0m
    2017-10-03 13:46:12.520	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224700/1412615[0m
    2017-10-03 13:46:12.629	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224720/1412615[0m
    2017-10-03 13:46:12.692	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224740/1412615[0m
    2017-10-03 13:46:15.434	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224760/1412615[0m
    2017-10-03 13:46:15.499	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224780/1412615[0m
    2017-10-03 13:46:15.577	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224800/1412615[0m
    2017-10-03 13:46:15.670	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224820/1412615[0m
    2017-10-03 13:46:15.701	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[178.132.3.215:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:46:33.090	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224840/1412615[0m
    2017-10-03 13:46:33.993	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224860/1412615[0m
    2017-10-03 13:46:41.400	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224880/1412615[0m
    2017-10-03 13:46:46.562	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224900/1412615[0m
    2017-10-03 13:46:49.188	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224920/1412615[0m
    2017-10-03 13:46:49.992	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224940/1412615[0m
    2017-10-03 13:46:50.103	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224960/1412615[0m
    2017-10-03 13:46:50.201	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[81.225.68.97:18080 OUT]  Synced 1224980/1412615[0m
    2017-10-03 13:47:17.278	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[46.10.1.165:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:48:04.687	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
    2017-10-03 13:48:04.687	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:797	[49.88.121.83:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:48:04.780	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-03 13:48:04.780	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-03 13:48:05.186	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[81.225.68.97:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:48:05.438	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:48:06.406	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:48:07.909	[P2P2]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[89.70.224.210:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:48:08.143	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[162.210.173.15:18080 OUT] Sync data returned a new top block candidate: 1224980 -> 1412616 [Your node is 187636 blocks (260 days) behind] 
    SYNCHRONIZATION started
    2017-10-03 13:48:12.496	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225000/1412616[0m
    2017-10-03 13:48:12.558	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225020/1412616[0m
    2017-10-03 13:48:12.621	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225040/1412616[0m
    2017-10-03 13:48:12.683	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225060/1412616[0m
    2017-10-03 13:48:12.777	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225080/1412616[0m
    2017-10-03 13:48:12.839	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225100/1412616[0m
    2017-10-03 13:48:12.901	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225120/1412616[0m
    2017-10-03 13:48:12.979	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225140/1412616[0m
    2017-10-03 13:48:13.120	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225160/1412616[0m
    2017-10-03 13:48:13.229	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225180/1412616[0m
    2017-10-03 13:48:13.291	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225200/1412616[0m
    2017-10-03 13:48:13.416	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225220/1412616[0m
    2017-10-03 13:48:13.463	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225240/1412616[0m
    2017-10-03 13:48:13.541	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225260/1412616[0m
    2017-10-03 13:48:13.603	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225280/1412616[0m
    2017-10-03 13:48:13.800	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225300/1412616[0m
    2017-10-03 13:48:13.862	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225320/1412616[0m
    2017-10-03 13:48:58.592	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1150	[1;33m[162.210.173.15:18080 OUT]  Synced 1225340/1412616[0m
    2017-10-03 13:48:58.607	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3410	Block with id: <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196> has at least one transaction (id: <0951c466150a0843c2d88e31e76f384ec3e42d066c2e9e251a391595b7271eaf>) with wrong inputs.
    2017-10-03 13:48:58.607	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3413	Block with id <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196> added as invalid because of wrong inputs in transactions
    2017-10-03 13:48:59.231	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[46.105.99.42:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:49:00.232	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-03 13:49:00.232	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-03 13:49:00.996	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:00.996	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:797	[36.236.23.53:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:49:02.119	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[89.70.224.210:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:49:04.789	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:743	[70.112.253.65:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:49:04.789	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:771	[70.112.253.65:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:49:11.856	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:12.387	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.51.32.34:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:49:14.385	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:15.104	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:18.520	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:49:21.728	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.51.32.34:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:49:26.061	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:26.340	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-03 13:49:26.340	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-03 13:49:29.600	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:743	[52.161.26.137:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:49:29.600	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:771	[52.161.26.137:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:49:34.331	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:34.955	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:722	[207.181.247.171:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-03 13:49:34.955	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:771	[207.181.247.171:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:49:42.722	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:49:42.935	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:49:52.779	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:53.295	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:49:55.635	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:49:59.114	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:743	[107.150.61.138:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:49:59.114	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:771	[107.150.61.138:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:50:02.127	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:05.703	[P2P7]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:50:06.218	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-03 13:50:06.218	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-03 13:50:07.203	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:08.034	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:08.549	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[95.172.167.228:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:50:09.563	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-03 13:50:09.563	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-03 13:50:21.626	[P2P3]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:50:23.093	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:23.186	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:23.734	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:743	[176.214.125.123:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:50:23.734	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:771	[176.214.125.123:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:50:25.497	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:25.856	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:27.369	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:27.931	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:743	[59.72.63.23:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:50:27.931	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:771	[59.72.63.23:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:50:29.272	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:30.848	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[94.23.41.130:18080 OUT] Sync data returned a new top block candidate: 1225340 -> 1412617 [Your node is 187277 blocks (260 days) behind] 
    SYNCHRONIZATION started
    2017-10-03 13:50:31.193	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:32.020	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:41.920	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
    2017-10-03 13:50:43.137	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:45.370	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:46.337	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:47.148	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:48.866	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:49.584	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:50.458	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:50:51.567	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:06.397	[P2P6]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:51:07.286	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:07.474	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:09.570	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:12.066	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:12.721	[P2P8]	WARN 	net.p2p	src/p2p/net_node.inl:1594	[71.206.102.9:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:51:12.737	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[71.206.102.9:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-03 13:51:13.408	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:15.547	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:15.796	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:16.748	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:17.918	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:37.279	[P2P3]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:51:37.892	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:38.063	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:41.216	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:42.792	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:43.244	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:54.942	[P2P8]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:51:55.145	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-03 13:51:55.145	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-03 13:51:55.410	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:55.426	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:56.471	[P2P8]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:59.342	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:51:59.686	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:02.041	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:03.931	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:04.149	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:10.529	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:928	returned not all requested objects (context.m_requested_objects.size()=20), dropping connection
    2017-10-03 13:52:10.903	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:11.184	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:1160	Failed to connect to any of seed peers, trying fallback seeds
    2017-10-03 13:52:11.184	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:1171	Failed to connect to any of seed peers, continuing without seeds
    2017-10-03 13:52:11.933	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:14.070	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.113.52.36:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:14.788	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:14.991	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:15.430	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:16.210	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:20.703	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:722	[107.167.185.136:29671 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
    2017-10-03 13:52:20.703	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:771	[107.167.185.136:29671 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:52:25.809	[P2P3]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:52:25.809	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:797	[71.120.188.112:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:52:28.196	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:28.773	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:29.303	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:29.397	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:31.035	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:52:31.175	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.113.52.36:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:32.285	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:32.924	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:34.767	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:36.363	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:743	[183.111.172.85:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:52:36.363	[P2P6]	WARN 	net.p2p	src/p2p/net_node.inl:771	[183.111.172.85:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:52:36.878	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:38.050	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:39.832	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[97.101.8.136:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:47.073	[P2P5]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:52:50.224	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:50.598	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:51.160	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:52.816	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:55.617	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:52:56.647	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:17.349	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:1437	Block recognized as orphaned and rejected, id = <e065da5dfb8555789e47e04bf455d2901f744314f663c3e13ce03f82a090f80f>, height 1225341, parent in alt 0, parent in main 0 (parent <50bc721dd3e5705785c475e294a659da3ed2c57e9d6b4820ef0de52a590e7196>, current top <c35a3145ee40cc15d3c1e92591860e76cbc09776decf9cf138a20f7acde0ca40>, chain height 1225340)
    2017-10-03 13:53:17.957	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:19.829	[P2P3]	WARN 	net.p2p	src/p2p/net_node.inl:743	[91.223.147.88:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:53:19.829	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:771	[91.223.147.88:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:53:20.422	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:20.578	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:22.358	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.113.52.36:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:22.748	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:743	[85.25.118.57:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
    2017-10-03 13:53:22.748	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:771	[85.25.118.57:18080 OUT] COMMAND_HANDSHAKE Failed
    2017-10-03 13:53:23.045	[P2P3]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:23.232	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[174.110.172.211:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:24.451	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:25.012	[P2P6]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[121.145.177.33:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.044	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[108.61.179.111:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.538	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.539	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.554	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.554	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.554	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.554	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.554	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.554	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.570	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.585	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.585	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.585	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.585	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.585	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.585	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.601	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.601	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.601	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.601	[P2P9]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:26.601	[P2P1]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:53:28.707	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    
    
    2017-10-03 13:55:04.389	[P2P5]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:55:04.389	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:55:04.405	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[47.203.136.41:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 13:55:04.405	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[37.153.231.94:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-03 13:55:04.405	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:55:04.405	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[37.153.231.94:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-03 13:55:04.405	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:55:04.421	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[37.153.231.94:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-03 13:55:04.436	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:55:04.436	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[37.153.231.94:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-03 13:55:04.452	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:55:04.452	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[37.153.231.94:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-03 13:55:04.452	[P2P7]	ERROR	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021	[37.153.231.94:18080 OUT] Got block with unknown parent which was not requested - querying block hashes
    2017-10-03 13:55:04.452	[P2P7]	ERROR	net	contrib/epee/include/net/levin_protocol_handler_async.h:289	[37.153.231.94:18080 OUT] [levin_protocol] -->> start_outer_call failed
    2017-10-03 13:55:04.452	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
    2017-10-03 13:55:05.452	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
    2017-10-03 13:55:05.452	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:184	Node stopped.
    2017-10-03 13:55:05.452	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
    2017-10-03 13:55:05.452	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
    2017-10-03 13:55:09.456	[SRV_MAIN]	WARN 	net.p2p	src/p2p/net_node.inl:2025	UPnP device was found but not recognized as IGD.
    2017-10-03 13:55:09.456	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
    2017-10-03 13:55:09.612	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
    2017-10-03 13:55:09.612	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully




## moneromooo-monero | 2017-10-03T14:29:04+00:00
Can you do another log with: --log-level 1,\*p2p\*:DEBUG,net.cn:DEBUG please ?
And put if on fpaste.org, easier to deal with than here.

## webworxs | 2017-10-03T17:11:39+00:00
Quite a large log file, so I'm only sharing the part that got generated where I noticed syncing got stuck.

    7b44369e70d8538f	129.232.206.233:18080 	last_seen: d0.h0.m4.s6
    b3ad9d4aa47699ff	69.85.97.228:18080 	last_seen: d0.h0.m5.s26
    b404bc992f25be8e	163.172.10.45:18080 	last_seen: d0.h0.m6.s55
    adc070226321cfcc	163.172.157.163:18080 	last_seen: d0.h0.m7.s9
    c4f64922af1d8b4a	62.4.21.85:18082 	last_seen: d0.h0.m13.s41
    56cc2fb0e5551cd9	94.140.125.242:18080 	last_seen: d0.h0.m15.s26
    3b4b8a4c63c927c7	111.169.20.131:18080 	last_seen: d0.h0.m16.s45
    ce9d66188f193e3d	82.68.145.73:18080 	last_seen: d0.h0.m19.s32
    176230c51ec28e39	217.237.182.62:18080 	last_seen: d0.h0.m27.s28
    25b08a017104f361	173.76.16.190:18080 	last_seen: d0.h0.m28.s50
    a874186097ef480	109.172.57.53:18080 	last_seen: d0.h0.m30.s48
    cbf9a992f57d2d49	82.3.225.61:18080 	last_seen: d0.h0.m32.s5
    481e7dcdf1d71dd4	86.127.18.199:18080 	last_seen: d0.h0.m34.s9
    5a14618f0a8ea1ed	107.191.99.191:18080 	last_seen: d0.h0.m36.s20
    43d70fbe2e3c90f	72.196.127.33:18080 	last_seen: d0.h0.m39.s23
    c6a4b70bed74ded	2.36.223.191:18080 	last_seen: d0.h0.m39.s25
    f20adf385db0461f	91.121.86.165:18080 	last_seen: d0.h0.m39.s25
    bce9dc0ef2e047a5	94.23.206.130:28080 	last_seen: d0.h0.m39.s41
    7df1d1e8e10abf40	165.227.95.198:18080 	last_seen: d0.h0.m40.s38
    688fcc29ec12f99e	5.2.67.20:18080 	last_seen: d0.h0.m40.s39
    6920c3de2bbdf087	119.246.245.94:18080 	last_seen: d0.h0.m41.s41
    42da4e12f40e40aa	81.92.168.220:18080 	last_seen: d0.h0.m42.s41
    fc98c4d96732c40b	82.60.47.40:18080 	last_seen: d0.h0.m43.s37
    3ab622a3065b2be8	81.225.68.97:18080 	last_seen: d0.h0.m43.s58
    1f12818c87d61a5d	104.140.244.186:18080 	last_seen: d0.h0.m44.s22
    636da63f8f996279	109.95.117.121:18080 	last_seen: d0.h0.m45.s47
    d3de8403f8fd0d93	99.238.32.151:18080 	last_seen: d0.h0.m47.s7
    e1d5b8bf8b20bdac	45.34.77.146:18080 	last_seen: d0.h0.m47.s23
    9e7ce643b6ce0b41	74.96.145.78:18080 	last_seen: d0.h0.m47.s48
    2f6e2659e8852121	72.221.78.248:18080 	last_seen: d0.h0.m48.s12
    504b07edfd7c1ff9	58.179.175.51:18080 	last_seen: d0.h0.m51.s49
    20f1a9fd0a8de757	185.14.233.156:18080 	last_seen: d0.h0.m52.s28
    5a59a9e81eb0d785	24.62.212.231:18080 	last_seen: d0.h0.m53.s14
    9b7e8e3a35023aa0	188.4.251.182:18080 	last_seen: d0.h0.m53.s31
    5922f56f556d9bda	185.147.80.2:18080 	last_seen: d0.h0.m54.s35
    80d9a20b6b416346	138.197.186.253:18080 	last_seen: d0.h0.m56.s27
    a8379f857054c9be	77.247.178.141:18080 	last_seen: d0.h0.m56.s43
    77da15feb61d5411	37.59.52.83:18080 	last_seen: d0.h0.m59.s43
    b135312b3ae3700d	174.138.32.58:18080 	last_seen: d0.h1.m0.s24
    acb00ab99d05006d	37.59.97.122:18080 	last_seen: d0.h1.m0.s54
    94119d8cb7a72d2b	37.59.55.60:28080 	last_seen: d0.h1.m1.s2
    2cf7400af7a30a44	86.106.102.174:18080 	last_seen: d0.h1.m3.s9
    be941b977e70b9a5	1.161.49.177:18080 	last_seen: d0.h1.m4.s48
    5928824145aed1b	199.188.101.223:18080 	last_seen: d0.h1.m5.s41
    3ee6cc377e4aa763	50.100.224.64:18080 	last_seen: d0.h1.m6.s8
    407fe015d592c273	213.136.85.203:18080 	last_seen: d0.h1.m11.s51
    16b98dc6429f40af	59.102.106.30:18080 	last_seen: d0.h1.m13.s3
    e2be3e796a346da3	185.51.62.60:18080 	last_seen: d0.h1.m14.s0
    38f84af956534216	31.131.0.3:18080 	last_seen: d0.h1.m15.s50
    dab4179660a3b342	147.135.221.30:18080 	last_seen: d0.h1.m17.s1
    85aac47791f8fc26	92.249.119.52:18080 	last_seen: d0.h1.m18.s25
    df4c2677b45ae47b	169.232.246.108:18080 	last_seen: d0.h1.m26.s0
    55d554c5c5fa53e8	5.9.153.50:18080 	last_seen: d0.h1.m26.s39
    5ea4a5a0ed847109	86.158.144.44:18080 	last_seen: d0.h1.m27.s53
    95b9f536450510bd	50.71.143.89:18080 	last_seen: d0.h1.m31.s20
    3e7f81f679ebdcb5	212.175.35.221:18080 	last_seen: d0.h1.m31.s26
    84c96ee44df32c0e	77.120.98.228:18080 	last_seen: d0.h1.m33.s54
    2fe00c86c5550a61	39.108.186.175:18080 	last_seen: d0.h1.m34.s28
    76896a871d238197	52.191.161.211:18080 	last_seen: d0.h1.m35.s52
    f81b1f6a6274ff3b	174.109.188.140:18080 	last_seen: d0.h1.m35.s59
    9c7f3c95dd8bc137	138.197.182.111:18080 	last_seen: d0.h1.m38.s46
    3055a7fbeb255715	95.85.54.170:18080 	last_seen: d0.h1.m40.s15
    1f78b5da73ec9233	164.132.45.243:18080 	last_seen: d0.h1.m47.s44
    ecd88219374d9919	45.47.113.115:18080 	last_seen: d0.h1.m48.s50
    1a01f272d3ea043a	73.225.240.234:18080 	last_seen: d0.h1.m49.s12
    99c2a3b5f63a7ee3	87.98.218.138:18080 	last_seen: d0.h1.m49.s48
    9b7b72898a124a90	93.103.13.198:18080 	last_seen: d0.h1.m55.s15
    14cdf89fa3f53cab	188.254.32.245:18080 	last_seen: d0.h1.m56.s59
    987f745f0a03058	94.23.8.105:18080 	last_seen: d0.h1.m57.s53
    8e7d653d316181b3	45.76.28.209:18080 	last_seen: d0.h2.m0.s43
    23c07c443f62c4da	94.215.121.147:18080 	last_seen: d0.h2.m1.s46
    6feb9cebe69dd8e6	193.239.230.125:18080 	last_seen: d0.h2.m4.s4
    8c26d6dda3198c37	103.10.61.55:18080 	last_seen: d0.h2.m6.s2
    39a378c0a7e05d0a	109.230.231.222:18080 	last_seen: d0.h2.m7.s38
    90482624fb34e91a	37.59.97.165:18080 	last_seen: d0.h2.m9.s12
    53ef3a9783766774	136.159.7.132:18080 	last_seen: d0.h2.m11.s13
    787cb519a9cea8e1	86.151.154.212:18080 	last_seen: d0.h2.m14.s40
    53b52d39d5abb138	172.89.238.183:18080 	last_seen: d0.h2.m18.s11
    37c278fead435d86	5.189.167.173:18080 	last_seen: d0.h2.m19.s7
    8facfb0518c38cff	96.44.132.21:18080 	last_seen: d0.h2.m24.s40
    17eb86af60f915d7	84.193.156.231:18080 	last_seen: d0.h2.m25.s11
    37126f18397e05d8	176.37.175.123:18080 	last_seen: d0.h2.m25.s34
    d3c9bcd84f1eafd7	46.160.39.178:18080 	last_seen: d0.h2.m30.s18
    308be490d6c0508e	136.243.88.145:8180 	last_seen: d0.h2.m31.s3
    b61eca2929f4cf7e	91.121.246.32:18080 	last_seen: d0.h2.m31.s33
    d6d151b0deb58061	73.82.122.122:18080 	last_seen: d0.h2.m32.s58
    ba165642a57268d2	188.165.214.76:18080 	last_seen: d0.h2.m37.s14
    783db078f70ee714	192.140.242.107:18080 	last_seen: d0.h2.m37.s26
    8c3a972a1bcf76fe	88.99.6.198:18080 	last_seen: d0.h2.m42.s50
    61607217b2b87453	199.168.97.90:18080 	last_seen: d0.h2.m44.s33
    862db74ae740a3c5	88.198.184.41:18080 	last_seen: d0.h2.m44.s58
    1528e31ba768f64	2.235.34.72:18080 	last_seen: d0.h2.m46.s0
    7aea0f42c9ea1e91	104.168.164.173:18080 	last_seen: d0.h2.m46.s34
    e698d1284a679409	81.207.66.80:18080 	last_seen: d0.h2.m47.s3
    ef9a141f57e639e6	178.85.112.187:18080 	last_seen: d0.h2.m47.s15
    542fb0f24d746361	86.103.207.2:18080 	last_seen: d0.h2.m47.s49
    5a7d46a8fc78ec9c	89.187.130.10:18080 	last_seen: d0.h2.m48.s5
    af73d1064550b3ba	201.51.14.123:18080 	last_seen: d0.h2.m51.s57
    d8a89bafcd886108	92.91.128.128:18080 	last_seen: d0.h2.m53.s3
    eccfbdc936870e14	104.245.102.179:18080 	last_seen: d0.h2.m54.s35
    b4c89f9540050699	172.104.150.49:18080 	last_seen: d0.h2.m54.s53
    ed5d4bb306331c08	141.105.55.3:18080 	last_seen: d0.h2.m54.s57
    9c006b0f32d993b8	85.175.250.37:18080 	last_seen: d0.h2.m57.s36
    9ec38975c444d167	173.255.240.75:18080 	last_seen: d0.h3.m4.s50
    4c2ef6a79947761d	75.110.5.213:18080 	last_seen: d0.h3.m4.s52
    99cae2b4ad3cb092	87.92.44.196:18080 	last_seen: d0.h3.m6.s36
    b6902fe5cadb5175	93.136.99.98:18080 	last_seen: d0.h3.m8.s45
    5b35a292e6719d3f	141.239.160.81:18080 	last_seen: d0.h3.m8.s48
    8b287ae9aed3036	213.239.211.107:18080 	last_seen: d0.h3.m9.s43
    50fe4b4a55d0f556	92.30.189.93:18080 	last_seen: d0.h3.m11.s53
    1236a10fb24f5b3f	213.80.114.52:18080 	last_seen: d0.h3.m12.s5
    19b7f87468a7ee8e	109.202.33.29:18080 	last_seen: d0.h3.m14.s38
    5b50a15338801bf1	130.180.41.246:18080 	last_seen: d0.h3.m14.s49
    3060d776923baf7a	37.59.56.102:28080 	last_seen: d0.h3.m15.s21
    22045c2f5efa88a7	46.10.1.165:18080 	last_seen: d0.h3.m16.s24
    f7d97d35ab3c8c05	149.202.171.122:18080 	last_seen: d0.h3.m19.s38
    e574621000822683	84.86.135.179:18080 	last_seen: d0.h3.m20.s40
    632fc9bae7b7d95c	95.213.252.202:18080 	last_seen: d0.h3.m22.s14
    9d4210554e9cfe61	188.244.41.208:18080 	last_seen: d0.h3.m24.s24
    252d33a5caebbf89	138.197.182.102:18080 	last_seen: d0.h3.m26.s6
    3caf3ef593afd2f7	173.34.179.157:18080 	last_seen: d0.h3.m32.s1
    ce5a4292b7fe34e1	219.88.232.152:18080 	last_seen: d0.h3.m33.s11
    44c45fd2a3d4264d	198.204.247.170:18080 	last_seen: d0.h3.m35.s17
    3e1584f76b26e4d9	186.237.53.216:18080 	last_seen: d0.h3.m37.s15
    1106d5f02b727b5f	188.165.254.85:18080 	last_seen: d0.h3.m37.s24
    c499cbcd115b6b12	85.204.97.16:18080 	last_seen: d0.h3.m40.s58
    5ee72814c5d6fdac	185.198.57.145:18080 	last_seen: d0.h3.m41.s16
    d150aa7e9636e642	93.185.217.251:18080 	last_seen: d0.h3.m43.s28
    137f24c4c327c9e1	72.181.172.198:18080 	last_seen: d0.h3.m44.s54
    9df3f2b72fda58c1	94.130.129.89:18080 	last_seen: d0.h3.m47.s10
    4d5456d3d2ac8e2f	91.121.164.186:18080 	last_seen: d0.h3.m47.s42
    2e77671584b41a28	109.190.168.192:18080 	last_seen: d0.h3.m49.s22
    bc9bed2b587bb247	89.236.238.176:18080 	last_seen: d0.h3.m50.s15
    39b47544a40836ce	72.49.220.63:18080 	last_seen: d0.h3.m51.s18
    f1095cd77e73e7fc	5.228.78.45:18080 	last_seen: d0.h3.m55.s27
    60f3539f6ce938ce	110.200.79.6:18080 	last_seen: d0.h3.m56.s18
    18427cf2e4ac9b79	80.9.68.207:18080 	last_seen: d0.h4.m0.s55
    319ac46776517ecc	5.39.5.45:18080 	last_seen: d0.h4.m0.s58
    732d7091ade7b979	83.95.185.77:18080 	last_seen: d0.h4.m1.s3
    ed8e1b2d8f731a5b	84.27.112.62:18080 	last_seen: d0.h4.m1.s52
    2d36b895003750b2	61.6.6.182:18080 	last_seen: d0.h4.m5.s27
    51c9c1137785d35d	62.210.36.142:18080 	last_seen: d0.h4.m5.s36
    5314eefe43e605f8	47.196.165.202:18080 	last_seen: d0.h4.m6.s1
    7af350228f7c557e	77.198.96.69:18080 	last_seen: d0.h4.m8.s30
    2ee76f0e6290e4f8	72.183.124.56:18080 	last_seen: d0.h4.m8.s52
    96d9751ba5b751d0	212.71.252.81:18080 	last_seen: d0.h4.m12.s53
    104c2518a0ae5c8a	213.141.150.206:18080 	last_seen: d0.h4.m18.s23
    7ab54e750ea63539	83.215.219.237:18080 	last_seen: d0.h4.m22.s49
    732bbffc8617f03e	83.233.208.247:18080 	last_seen: d0.h4.m23.s49
    6133abcc068dce5e	85.166.187.34:18080 	last_seen: d0.h4.m26.s21
    ca6d20f13e2784e2	41.87.195.208:18080 	last_seen: d0.h4.m26.s51
    18a448d5d8383a23	185.161.208.217:18080 	last_seen: d0.h4.m28.s15
    8153cd3f5fa00c2b	190.16.90.150:18080 	last_seen: d0.h4.m29.s43
    56ab06b520e95845	183.77.75.114:18080 	last_seen: d0.h4.m30.s41
    4b15d592ca1fa66c	45.125.194.34:18080 	last_seen: d0.h4.m34.s7
    5220fae783ea34fd	212.129.13.151:18080 	last_seen: d0.h4.m34.s34
    831aa23679624095	5.9.78.35:18080 	last_seen: d0.h4.m35.s36
    c8cc9611b0d63b47	51.255.29.10:18080 	last_seen: d0.h4.m36.s7
    219954ee39f1d9dc	65.28.245.227:18080 	last_seen: d0.h4.m38.s46
    3f733577e3507416	37.59.97.171:18080 	last_seen: d0.h4.m39.s48
    1937973eeb455183	163.172.14.142:18080 	last_seen: d0.h4.m39.s54
    4fad470e4eb9ee4b	155.94.209.114:18080 	last_seen: d0.h4.m46.s36
    f198dacc96e3e4f5	85.194.238.131:18080 	last_seen: d0.h4.m48.s26
    2d2b711519523362	95.211.244.210:18080 	last_seen: d0.h4.m48.s42
    2977fd9c241825d0	112.211.219.102:18080 	last_seen: d0.h4.m51.s23
    14a7bcc7cf8255d3	49.88.121.83:18080 	last_seen: d0.h4.m54.s22
    55aa446c20e26d9e	70.77.131.187:18080 	last_seen: d0.h4.m55.s17
    97b02617ffd1a22a	85.25.118.57:18080 	last_seen: d0.h4.m55.s23
    69aabd285d322bfb	78.183.142.70:18080 	last_seen: d0.h4.m56.s7
    6cd22c9af303f144	165.227.12.81:18080 	last_seen: d0.h4.m59.s34
    2fcc92915364353b	136.159.7.128:18080 	last_seen: d0.h5.m4.s1
    1e3eb02925418b06	118.32.218.216:18080 	last_seen: d0.h5.m4.s15
    e14c9c7e22a166dd	165.227.213.187:18080 	last_seen: d0.h5.m5.s58
    685535805cdf0a2c	78.224.252.87:18080 	last_seen: d0.h5.m7.s18
    6599e70919564799	91.48.152.35:18080 	last_seen: d0.h5.m7.s48
    581029ae5b2d0c07	74.65.92.101:18080 	last_seen: d0.h5.m8.s46
    553a485b74426b3f	149.202.171.183:18080 	last_seen: d0.h5.m9.s31
    48231223b294dfe9	5.200.23.99:18800 	last_seen: d0.h5.m12.s40
    92668be0f0996134	37.187.24.170:18080 	last_seen: d0.h5.m16.s52
    9eae3917bf2e7dc8	37.59.44.193:28080 	last_seen: d0.h5.m21.s15
    b510097472e4a235	96.18.147.252:18080 	last_seen: d0.h5.m21.s38
    83d8b34d4c577d71	125.33.208.155:18080 	last_seen: d0.h5.m24.s45
    8ec14ca931e6bae3	92.222.180.113:18080 	last_seen: d0.h5.m25.s35
    fb2d4dc8597bf8ba	212.129.13.124:18080 	last_seen: d0.h5.m26.s37
    4982f5cd436e0b79	123.170.66.166:18080 	last_seen: d0.h5.m27.s39
    ce5a71ff04675bd8	84.250.167.34:18080 	last_seen: d0.h5.m31.s26
    1ef32a5e8adff949	73.187.177.189:18080 	last_seen: d0.h5.m33.s47
    55c9f2077ba750d5	45.77.98.24:18080 	last_seen: d0.h5.m36.s41
    d0d26caf0943b2f4	111.92.240.126:18080 	last_seen: d0.h5.m37.s37
    7b38c4cbe2cd227f	66.70.204.193:18080 	last_seen: d0.h5.m40.s7
    203a62f59dacbcac	94.130.9.194:8180 	last_seen: d0.h5.m40.s10
    eadefac7c395d5f7	198.100.144.155:18080 	last_seen: d0.h5.m47.s18
    c53fd6e9e0c8fe29	181.137.177.132:18080 	last_seen: d0.h5.m49.s55
    25c0120e7b54afeb	77.120.29.195:18080 	last_seen: d0.h5.m50.s22
    d5aa0c606f1e3f15	80.172.224.52:18080 	last_seen: d0.h5.m53.s10
    d3e47ab046f655c1	208.87.220.8:18080 	last_seen: d0.h5.m53.s13
    ed496600e472603c	140.121.171.38:18080 	last_seen: d0.h5.m54.s21
    ecb523024c7ab5d6	175.211.101.26:18080 	last_seen: d0.h5.m54.s43
    b0adf6ea81b105cf	220.180.98.75:18080 	last_seen: d0.h5.m56.s19
    d2040a214d26a291	125.126.109.162:18080 	last_seen: d0.h5.m56.s32
    f373bbe819bed4f5	120.60.143.175:18080 	last_seen: d0.h5.m59.s34
    7749ad69b290fab3	95.79.211.72:18080 	last_seen: d0.h6.m0.s32
    c281e60acf71f93b	89.252.28.26:18080 	last_seen: d0.h6.m1.s40
    9137180722685c84	138.197.182.108:18080 	last_seen: d0.h6.m10.s26
    40810e66136dc556	163.172.255.54:18080 	last_seen: d0.h6.m11.s16
    adb0a06d62456bf1	178.27.208.189:18080 	last_seen: d0.h6.m12.s54
    e879dfbd6247cee9	70.26.53.81:18080 	last_seen: d0.h6.m15.s21
    b99e81e8406a7c62	46.105.99.42:18080 	last_seen: d0.h6.m16.s23
    4bcef7d533db39c1	37.59.97.168:18080 	last_seen: d0.h6.m16.s40
    f8887d9ba3cd85b	173.255.235.69:18080 	last_seen: d0.h6.m16.s49
    20b382d7282f6724	163.172.24.66:18080 	last_seen: d0.h6.m17.s25
    bd52d5e9408688b7	136.243.102.157:8180 	last_seen: d0.h6.m17.s29
    e0c41772850f3969	47.158.71.131:18080 	last_seen: d0.h6.m17.s31
    2951efefcc6189cf	51.15.64.38:18080 	last_seen: d0.h6.m20.s8
    cf7cadeb39ea7118	50.82.45.123:18080 	last_seen: d0.h6.m22.s34
    619956a3fd20198e	37.153.231.94:18080 	last_seen: d0.h6.m22.s40
    e105cf8441a0944a	89.137.21.238:18080 	last_seen: d0.h6.m23.s0
    4ea189246ba0f548	138.68.29.3:18080 	last_seen: d0.h6.m23.s48
    cd79550ed0c401f9	52.51.118.175:18080 	last_seen: d0.h6.m25.s54
    8cd9351ce091f864	59.110.50.157:18080 	last_seen: d0.h6.m25.s54
    9354a3fbdaf661e0	211.110.153.205:18080 	last_seen: d0.h6.m26.s20
    d4240af13ff19014	31.209.59.179:18080 	last_seen: d0.h6.m26.s30
    83d1c360a533ee7e	71.198.213.2:18080 	last_seen: d0.h6.m28.s1
    3d74f48f4c6c2376	91.121.2.76:18080 	last_seen: d0.h6.m28.s56
    109ec61bd63b1e1	5.9.66.144:18080 	last_seen: d0.h6.m34.s36
    3c917c68faa3512f	78.102.134.69:18080 	last_seen: d0.h6.m35.s38
    6ab21a2196b11e19	203.162.53.155:18080 	last_seen: d0.h6.m36.s24
    14328a7d05b8f785	60.205.216.122:18080 	last_seen: d0.h6.m38.s4
    f64b93ebf9cfe4a4	85.212.205.101:18080 	last_seen: d0.h6.m42.s48
    fab96cccf45ba799	14.202.86.152:18080 	last_seen: d0.h6.m44.s24
    d17264a25b5d724a	174.108.46.49:18080 	last_seen: d0.h6.m44.s29
    a20b152ae8237b8c	173.26.121.169:18080 	last_seen: d0.h6.m44.s48
    73b047488a68ecf9	73.141.228.123:18080 	last_seen: d0.h6.m49.s52
    64489c0a54808080	46.105.103.169:28080 	last_seen: d0.h6.m51.s48
    58769f99e429575f	194.135.74.242:18080 	last_seen: d0.h6.m52.s7
    119f3acb980bb139	72.174.128.244:18080 	last_seen: d0.h6.m57.s12
    26a60a6aef6094dd	107.4.235.25:18080 	last_seen: d0.h6.m58.s20
    dab22679b6fdeed4	223.132.249.175:18080 	last_seen: d0.h6.m58.s32
    c74835a6672b8c51	24.226.189.136:18080 	last_seen: d0.h6.m58.s38
    1b6be1665782adda	36.232.130.155:18080 	last_seen: d0.h7.m1.s30
    8729c5bca3adb4d7	108.28.160.132:18080 	last_seen: d0.h7.m3.s28
    780d9e8efacd87a5	99.101.94.101:18080 	last_seen: d0.h7.m11.s16
    80beab3428c02ba2	46.185.226.67:18080 	last_seen: d0.h7.m12.s35
    bff275febfd4f108	91.121.82.47:18080 	last_seen: d0.h7.m17.s39
    e26d6381faf2cc1e	188.221.188.61:18080 	last_seen: d0.h7.m18.s46
    6255bd26a5d1aabb	5.230.146.26:18080 	last_seen: d0.h7.m18.s57
    48016f94493f3ff7	27.253.5.110:18080 	last_seen: d0.h7.m23.s51
    2e036a83e8f36e91	109.193.32.49:18080 	last_seen: d0.h7.m24.s14
    f5aeb2b9777888a4	105.100.30.220:18080 	last_seen: d0.h7.m24.s39
    
    2017-10-03 17:05:53.863	[P2P8]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:308	Remote blockchain height: 1412708, id: <4a1a205a081317ca26ce1974388e40ba60cb6c349cadbb96a6a5b86e5921401c>
    2017-10-03 17:05:53.863	[P2P8]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:311	[52.80.93.130:18080 OUT] requesting callback
    2017-10-03 17:05:53.863	[P2P8]	DEBUG	net.p2p	src/p2p/net_node.inl:757	[52.80.93.130:18080 OUT]  COMMAND_HANDSHAKE INVOKED OK
    2017-10-03 17:05:53.863	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:98	[52.80.93.130:18080 OUT] callback fired
    2017-10-03 17:05:53.863	[P2P7]	DEBUG	net.p2p	src/p2p/net_node.inl:975	[52.80.93.130:18080 OUT] CONNECTION HANDSHAKED OK.
    2017-10-03 17:05:53.863	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:106	[52.80.93.130:18080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=31
    2017-10-03 17:05:53.863	[P2P7]	INFO 	net.p2p	src/p2p/net_node.inl:984	Connecting to 178.238.236.143:18080(last_seen: d0.h4.m30.s41)...
    2017-10-03 17:05:53.863	[P2P7]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#37 to 0.0.0.0 currently we have sockets count:10
    2017-10-03 17:05:54.051	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[138.197.190.111:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:05:54.051	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[138.197.190.111:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[138.197.190.111:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[138.197.190.111:18080 OUT]  adding span: 20 at height 1319779, 4.64961 seconds, 144.526 kB/s, size now 63.4797 MB
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[138.197.190.111:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[138.197.190.111:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:05:54.066	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[138.197.190.111:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[138.197.190.111:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.119208
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[138.197.190.111:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[138.197.190.111:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[138.197.190.111:18080 OUT]  checking for gap
    2017-10-03 17:05:54.066	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[138.197.190.111:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:05:54.066	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[138.197.190.111:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:05:54.175	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[52.80.93.130:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:54.193	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[52.80.93.130:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:54.224	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[138.197.190.111:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:54.271	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[138.197.190.111:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:55.308	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:05:55.308	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 1534399 bytes worth of blocks
    2017-10-03 17:05:55.308	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320379 - 1320398[0m
    2017-10-03 17:05:55.308	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320379, 3.84741 seconds, 398.813 kB/s, size now 64.3021 MB
    2017-10-03 17:05:55.308	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:05:55.308	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:05:55.308	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:05:55.308	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9919 lrh 1330317, chain 1319418
    2017-10-03 17:05:55.323	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:05:55.323	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:05:55.323	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320399: 1320399/20
    2017-10-03 17:05:55.323	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320399/20 (1320399 - 1320418)
    2017-10-03 17:05:55.323	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320399, first hash <d41a640c128feb1032368a1407c1244f80771446a75548bb8abade588c32909b>
    2017-10-03 17:05:55.323	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[185.31.136.69:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:55.542	[P2P7]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#37 to 0.0.0.0
    2017-10-03 17:05:55.542	[P2P7]	INFO 	net.p2p	src/p2p/net_node.inl:999	[0.0.0.0:0 OUT] Connect failed to 178.238.236.143:18080
    2017-10-03 17:05:55.542	[P2P7]	DEBUG	net.p2p	src/p2p/net_node.inl:1935	PEER EVICTED FROM GRAY PEER LIST IP address: 178.238.236.143 Peer ID: 11255901847557656725
    2017-10-03 17:05:56.431	[P2P7]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:05:56.431	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 725782 bytes worth of blocks
    2017-10-03 17:05:56.431	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320399 - 1320418[0m
    2017-10-03 17:05:56.431	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320399, 1.1076 seconds, 655.273 kB/s, size now 64.9943 MB
    2017-10-03 17:05:56.446	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:05:56.446	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:05:56.446	[P2P7]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:05:56.446	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9899 lrh 1330317, chain 1319418
    2017-10-03 17:05:56.446	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:05:56.446	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:05:56.446	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320419: 1320419/20
    2017-10-03 17:05:56.446	[P2P7]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320419/20 (1320419 - 1320438)
    2017-10-03 17:05:56.446	[P2P7]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320419, first hash <b33e5ba4c3ebae52350278dd56cc1963217461cbe5697de03f42c6aaf04c04e0>
    2017-10-03 17:05:56.446	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[185.31.136.69:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:56.556	[P2P7]	DEBUG	net.p2p	src/p2p/net_node.inl:1298	STARTED PEERLIST IDLE HANDSHAKE
    2017-10-03 17:05:56.556	[P2P7]	DEBUG	net.p2p	src/p2p/net_node.inl:1313	FINISHED PEERLIST IDLE HANDSHAKE
    2017-10-03 17:05:57.289	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1562	[52.80.93.130:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=1319417, m_total_height=1412708
    2017-10-03 17:05:57.289	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[52.80.93.130:18080 OUT]  request_missing_objects: check 0, force_next_span 0, m_needed_objects 10000 lrh 1329416, chain 1319418
    2017-10-03 17:05:57.289	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[52.80.93.130:18080 OUT]  checking for gap
    2017-10-03 17:05:57.289	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[52.80.93.130:18080 OUT]  span size is 0
    2017-10-03 17:05:57.289	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[52.80.93.130:18080 OUT]  span from 1319419: 1320439/20
    2017-10-03 17:05:57.289	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[52.80.93.130:18080 OUT]  span: 1320439/20 (1320439 - 1320458)
    2017-10-03 17:05:57.289	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[52.80.93.130:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320439, first hash <6a2a5828f7754e10cb6e551ae80f3309bf945f007edbd02efe1b761a796744bc>
    2017-10-03 17:05:57.320	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[52.80.93.130:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:57.507	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1344	[52.80.93.130:18080 OUT] REMOTE PEERLIST: TIME_DELTA: -55, remote peerlist size=250
    2017-10-03 17:05:57.507	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1345	[52.80.93.130:18080 OUT] REMOTE PEERLIST: 9540cfbebcc3c8cb	177.198.158.130:18080 	last_seen: d0.h0.m1.s30
    7b44369e70d8538f	129.232.206.233:18080 	last_seen: d0.h0.m4.s14
    b3ad9d4aa47699ff	69.85.97.228:18080 	last_seen: d0.h0.m5.s34
    b404bc992f25be8e	163.172.10.45:18080 	last_seen: d0.h0.m7.s3
    adc070226321cfcc	163.172.157.163:18080 	last_seen: d0.h0.m7.s17
    c4f64922af1d8b4a	62.4.21.85:18082 	last_seen: d0.h0.m13.s49
    56cc2fb0e5551cd9	94.140.125.242:18080 	last_seen: d0.h0.m15.s34
    3b4b8a4c63c927c7	111.169.20.131:18080 	last_seen: d0.h0.m16.s53
    ce9d66188f193e3d	82.68.145.73:18080 	last_seen: d0.h0.m19.s40
    176230c51ec28e39	217.237.182.62:18080 	last_seen: d0.h0.m27.s36
    25b08a017104f361	173.76.16.190:18080 	last_seen: d0.h0.m28.s58
    a874186097ef480	109.172.57.53:18080 	last_seen: d0.h0.m30.s56
    cbf9a992f57d2d49	82.3.225.61:18080 	last_seen: d0.h0.m32.s13
    481e7dcdf1d71dd4	86.127.18.199:18080 	last_seen: d0.h0.m34.s17
    5a14618f0a8ea1ed	107.191.99.191:18080 	last_seen: d0.h0.m36.s28
    43d70fbe2e3c90f	72.196.127.33:18080 	last_seen: d0.h0.m39.s31
    c6a4b70bed74ded	2.36.223.191:18080 	last_seen: d0.h0.m39.s33
    f20adf385db0461f	91.121.86.165:18080 	last_seen: d0.h0.m39.s33
    bce9dc0ef2e047a5	94.23.206.130:28080 	last_seen: d0.h0.m39.s49
    7df1d1e8e10abf40	165.227.95.198:18080 	last_seen: d0.h0.m40.s46
    688fcc29ec12f99e	5.2.67.20:18080 	last_seen: d0.h0.m40.s47
    6920c3de2bbdf087	119.246.245.94:18080 	last_seen: d0.h0.m41.s49
    42da4e12f40e40aa	81.92.168.220:18080 	last_seen: d0.h0.m42.s49
    fc98c4d96732c40b	82.60.47.40:18080 	last_seen: d0.h0.m43.s45
    3ab622a3065b2be8	81.225.68.97:18080 	last_seen: d0.h0.m44.s6
    1f12818c87d61a5d	104.140.244.186:18080 	last_seen: d0.h0.m44.s30
    636da63f8f996279	109.95.117.121:18080 	last_seen: d0.h0.m45.s55
    d3de8403f8fd0d93	99.238.32.151:18080 	last_seen: d0.h0.m47.s15
    e1d5b8bf8b20bdac	45.34.77.146:18080 	last_seen: d0.h0.m47.s31
    9e7ce643b6ce0b41	74.96.145.78:18080 	last_seen: d0.h0.m47.s56
    2f6e2659e8852121	72.221.78.248:18080 	last_seen: d0.h0.m48.s20
    504b07edfd7c1ff9	58.179.175.51:18080 	last_seen: d0.h0.m51.s57
    20f1a9fd0a8de757	185.14.233.156:18080 	last_seen: d0.h0.m52.s36
    5a59a9e81eb0d785	24.62.212.231:18080 	last_seen: d0.h0.m53.s22
    9b7e8e3a35023aa0	188.4.251.182:18080 	last_seen: d0.h0.m53.s39
    5922f56f556d9bda	185.147.80.2:18080 	last_seen: d0.h0.m54.s43
    80d9a20b6b416346	138.197.186.253:18080 	last_seen: d0.h0.m56.s35
    a8379f857054c9be	77.247.178.141:18080 	last_seen: d0.h0.m56.s51
    77da15feb61d5411	37.59.52.83:18080 	last_seen: d0.h0.m59.s51
    b135312b3ae3700d	174.138.32.58:18080 	last_seen: d0.h1.m0.s32
    acb00ab99d05006d	37.59.97.122:18080 	last_seen: d0.h1.m1.s2
    94119d8cb7a72d2b	37.59.55.60:28080 	last_seen: d0.h1.m1.s10
    2cf7400af7a30a44	86.106.102.174:18080 	last_seen: d0.h1.m3.s17
    be941b977e70b9a5	1.161.49.177:18080 	last_seen: d0.h1.m4.s56
    5928824145aed1b	199.188.101.223:18080 	last_seen: d0.h1.m5.s49
    3ee6cc377e4aa763	50.100.224.64:18080 	last_seen: d0.h1.m6.s16
    407fe015d592c273	213.136.85.203:18080 	last_seen: d0.h1.m11.s59
    16b98dc6429f40af	59.102.106.30:18080 	last_seen: d0.h1.m13.s11
    e2be3e796a346da3	185.51.62.60:18080 	last_seen: d0.h1.m14.s8
    38f84af956534216	31.131.0.3:18080 	last_seen: d0.h1.m15.s58
    dab4179660a3b342	147.135.221.30:18080 	last_seen: d0.h1.m17.s9
    85aac47791f8fc26	92.249.119.52:18080 	last_seen: d0.h1.m18.s33
    df4c2677b45ae47b	169.232.246.108:18080 	last_seen: d0.h1.m26.s8
    55d554c5c5fa53e8	5.9.153.50:18080 	last_seen: d0.h1.m26.s47
    5ea4a5a0ed847109	86.158.144.44:18080 	last_seen: d0.h1.m28.s1
    95b9f536450510bd	50.71.143.89:18080 	last_seen: d0.h1.m31.s28
    3e7f81f679ebdcb5	212.175.35.221:18080 	last_seen: d0.h1.m31.s34
    84c96ee44df32c0e	77.120.98.228:18080 	last_seen: d0.h1.m34.s2
    2fe00c86c5550a61	39.108.186.175:18080 	last_seen: d0.h1.m34.s36
    76896a871d238197	52.191.161.211:18080 	last_seen: d0.h1.m36.s0
    f81b1f6a6274ff3b	174.109.188.140:18080 	last_seen: d0.h1.m36.s7
    9c7f3c95dd8bc137	138.197.182.111:18080 	last_seen: d0.h1.m38.s54
    3055a7fbeb255715	95.85.54.170:18080 	last_seen: d0.h1.m40.s23
    1f78b5da73ec9233	164.132.45.243:18080 	last_seen: d0.h1.m47.s52
    ecd88219374d9919	45.47.113.115:18080 	last_seen: d0.h1.m48.s58
    1a01f272d3ea043a	73.225.240.234:18080 	last_seen: d0.h1.m49.s20
    99c2a3b5f63a7ee3	87.98.218.138:18080 	last_seen: d0.h1.m49.s56
    9b7b72898a124a90	93.103.13.198:18080 	last_seen: d0.h1.m55.s23
    14cdf89fa3f53cab	188.254.32.245:18080 	last_seen: d0.h1.m57.s7
    987f745f0a03058	94.23.8.105:18080 	last_seen: d0.h1.m58.s1
    8e7d653d316181b3	45.76.28.209:18080 	last_seen: d0.h2.m0.s51
    23c07c443f62c4da	94.215.121.147:18080 	last_seen: d0.h2.m1.s54
    6feb9cebe69dd8e6	193.239.230.125:18080 	last_seen: d0.h2.m4.s12
    8c26d6dda3198c37	103.10.61.55:18080 	last_seen: d0.h2.m6.s10
    39a378c0a7e05d0a	109.230.231.222:18080 	last_seen: d0.h2.m7.s46
    90482624fb34e91a	37.59.97.165:18080 	last_seen: d0.h2.m9.s20
    53ef3a9783766774	136.159.7.132:18080 	last_seen: d0.h2.m11.s21
    787cb519a9cea8e1	86.151.154.212:18080 	last_seen: d0.h2.m14.s48
    53b52d39d5abb138	172.89.238.183:18080 	last_seen: d0.h2.m18.s19
    37c278fead435d86	5.189.167.173:18080 	last_seen: d0.h2.m19.s15
    8facfb0518c38cff	96.44.132.21:18080 	last_seen: d0.h2.m24.s48
    17eb86af60f915d7	84.193.156.231:18080 	last_seen: d0.h2.m25.s19
    37126f18397e05d8	176.37.175.123:18080 	last_seen: d0.h2.m25.s42
    d3c9bcd84f1eafd7	46.160.39.178:18080 	last_seen: d0.h2.m30.s26
    308be490d6c0508e	136.243.88.145:8180 	last_seen: d0.h2.m31.s11
    b61eca2929f4cf7e	91.121.246.32:18080 	last_seen: d0.h2.m31.s41
    d6d151b0deb58061	73.82.122.122:18080 	last_seen: d0.h2.m33.s6
    ba165642a57268d2	188.165.214.76:18080 	last_seen: d0.h2.m37.s22
    783db078f70ee714	192.140.242.107:18080 	last_seen: d0.h2.m37.s34
    8c3a972a1bcf76fe	88.99.6.198:18080 	last_seen: d0.h2.m42.s58
    61607217b2b87453	199.168.97.90:18080 	last_seen: d0.h2.m44.s41
    862db74ae740a3c5	88.198.184.41:18080 	last_seen: d0.h2.m45.s6
    1528e31ba768f64	2.235.34.72:18080 	last_seen: d0.h2.m46.s8
    7aea0f42c9ea1e91	104.168.164.173:18080 	last_seen: d0.h2.m46.s42
    e698d1284a679409	81.207.66.80:18080 	last_seen: d0.h2.m47.s11
    ef9a141f57e639e6	178.85.112.187:18080 	last_seen: d0.h2.m47.s23
    542fb0f24d746361	86.103.207.2:18080 	last_seen: d0.h2.m47.s57
    5a7d46a8fc78ec9c	89.187.130.10:18080 	last_seen: d0.h2.m48.s13
    af73d1064550b3ba	201.51.14.123:18080 	last_seen: d0.h2.m52.s5
    d8a89bafcd886108	92.91.128.128:18080 	last_seen: d0.h2.m53.s11
    eccfbdc936870e14	104.245.102.179:18080 	last_seen: d0.h2.m54.s43
    b4c89f9540050699	172.104.150.49:18080 	last_seen: d0.h2.m55.s1
    ed5d4bb306331c08	141.105.55.3:18080 	last_seen: d0.h2.m55.s5
    9c006b0f32d993b8	85.175.250.37:18080 	last_seen: d0.h2.m57.s44
    9ec38975c444d167	173.255.240.75:18080 	last_seen: d0.h3.m4.s58
    4c2ef6a79947761d	75.110.5.213:18080 	last_seen: d0.h3.m5.s0
    99cae2b4ad3cb092	87.92.44.196:18080 	last_seen: d0.h3.m6.s44
    b6902fe5cadb5175	93.136.99.98:18080 	last_seen: d0.h3.m8.s53
    5b35a292e6719d3f	141.239.160.81:18080 	last_seen: d0.h3.m8.s56
    8b287ae9aed3036	213.239.211.107:18080 	last_seen: d0.h3.m9.s51
    50fe4b4a55d0f556	92.30.189.93:18080 	last_seen: d0.h3.m12.s1
    1236a10fb24f5b3f	213.80.114.52:18080 	last_seen: d0.h3.m12.s13
    19b7f87468a7ee8e	109.202.33.29:18080 	last_seen: d0.h3.m14.s46
    5b50a15338801bf1	130.180.41.246:18080 	last_seen: d0.h3.m14.s57
    3060d776923baf7a	37.59.56.102:28080 	last_seen: d0.h3.m15.s29
    22045c2f5efa88a7	46.10.1.165:18080 	last_seen: d0.h3.m16.s32
    f7d97d35ab3c8c05	149.202.171.122:18080 	last_seen: d0.h3.m19.s46
    e574621000822683	84.86.135.179:18080 	last_seen: d0.h3.m20.s48
    632fc9bae7b7d95c	95.213.252.202:18080 	last_seen: d0.h3.m22.s22
    9d4210554e9cfe61	188.244.41.208:18080 	last_seen: d0.h3.m24.s32
    252d33a5caebbf89	138.197.182.102:18080 	last_seen: d0.h3.m26.s14
    3caf3ef593afd2f7	173.34.179.157:18080 	last_seen: d0.h3.m32.s9
    ce5a4292b7fe34e1	219.88.232.152:18080 	last_seen: d0.h3.m33.s19
    44c45fd2a3d4264d	198.204.247.170:18080 	last_seen: d0.h3.m35.s25
    3e1584f76b26e4d9	186.237.53.216:18080 	last_seen: d0.h3.m37.s23
    1106d5f02b727b5f	188.165.254.85:18080 	last_seen: d0.h3.m37.s32
    c499cbcd115b6b12	85.204.97.16:18080 	last_seen: d0.h3.m41.s6
    5ee72814c5d6fdac	185.198.57.145:18080 	last_seen: d0.h3.m41.s24
    d150aa7e9636e642	93.185.217.251:18080 	last_seen: d0.h3.m43.s36
    137f24c4c327c9e1	72.181.172.198:18080 	last_seen: d0.h3.m45.s2
    9df3f2b72fda58c1	94.130.129.89:18080 	last_seen: d0.h3.m47.s18
    4d5456d3d2ac8e2f	91.121.164.186:18080 	last_seen: d0.h3.m47.s50
    2e77671584b41a28	109.190.168.192:18080 	last_seen: d0.h3.m49.s30
    bc9bed2b587bb247	89.236.238.176:18080 	last_seen: d0.h3.m50.s23
    39b47544a40836ce	72.49.220.63:18080 	last_seen: d0.h3.m51.s26
    f1095cd77e73e7fc	5.228.78.45:18080 	last_seen: d0.h3.m55.s35
    60f3539f6ce938ce	110.200.79.6:18080 	last_seen: d0.h3.m56.s26
    18427cf2e4ac9b79	80.9.68.207:18080 	last_seen: d0.h4.m1.s3
    319ac46776517ecc	5.39.5.45:18080 	last_seen: d0.h4.m1.s6
    732d7091ade7b979	83.95.185.77:18080 	last_seen: d0.h4.m1.s11
    ed8e1b2d8f731a5b	84.27.112.62:18080 	last_seen: d0.h4.m2.s0
    2d36b895003750b2	61.6.6.182:18080 	last_seen: d0.h4.m5.s35
    51c9c1137785d35d	62.210.36.142:18080 	last_seen: d0.h4.m5.s44
    5314eefe43e605f8	47.196.165.202:18080 	last_seen: d0.h4.m6.s9
    7af350228f7c557e	77.198.96.69:18080 	last_seen: d0.h4.m8.s38
    2ee76f0e6290e4f8	72.183.124.56:18080 	last_seen: d0.h4.m9.s0
    96d9751ba5b751d0	212.71.252.81:18080 	last_seen: d0.h4.m13.s1
    104c2518a0ae5c8a	213.141.150.206:18080 	last_seen: d0.h4.m18.s31
    7ab54e750ea63539	83.215.219.237:18080 	last_seen: d0.h4.m22.s57
    732bbffc8617f03e	83.233.208.247:18080 	last_seen: d0.h4.m23.s57
    6133abcc068dce5e	85.166.187.34:18080 	last_seen: d0.h4.m26.s29
    ca6d20f13e2784e2	41.87.195.208:18080 	last_seen: d0.h4.m26.s59
    18a448d5d8383a23	185.161.208.217:18080 	last_seen: d0.h4.m28.s23
    8153cd3f5fa00c2b	190.16.90.150:18080 	last_seen: d0.h4.m29.s51
    56ab06b520e95845	183.77.75.114:18080 	last_seen: d0.h4.m30.s49
    4b15d592ca1fa66c	45.125.194.34:18080 	last_seen: d0.h4.m34.s15
    5220fae783ea34fd	212.129.13.151:18080 	last_seen: d0.h4.m34.s42
    831aa23679624095	5.9.78.35:18080 	last_seen: d0.h4.m35.s44
    c8cc9611b0d63b47	51.255.29.10:18080 	last_seen: d0.h4.m36.s15
    219954ee39f1d9dc	65.28.245.227:18080 	last_seen: d0.h4.m38.s54
    3f733577e3507416	37.59.97.171:18080 	last_seen: d0.h4.m39.s56
    1937973eeb455183	163.172.14.142:18080 	last_seen: d0.h4.m40.s2
    4fad470e4eb9ee4b	155.94.209.114:18080 	last_seen: d0.h4.m46.s44
    f198dacc96e3e4f5	85.194.238.131:18080 	last_seen: d0.h4.m48.s34
    2d2b711519523362	95.211.244.210:18080 	last_seen: d0.h4.m48.s50
    2977fd9c241825d0	112.211.219.102:18080 	last_seen: d0.h4.m51.s31
    14a7bcc7cf8255d3	49.88.121.83:18080 	last_seen: d0.h4.m54.s30
    55aa446c20e26d9e	70.77.131.187:18080 	last_seen: d0.h4.m55.s25
    97b02617ffd1a22a	85.25.118.57:18080 	last_seen: d0.h4.m55.s31
    69aabd285d322bfb	78.183.142.70:18080 	last_seen: d0.h4.m56.s15
    6cd22c9af303f144	165.227.12.81:18080 	last_seen: d0.h4.m59.s42
    2fcc92915364353b	136.159.7.128:18080 	last_seen: d0.h5.m4.s9
    1e3eb02925418b06	118.32.218.216:18080 	last_seen: d0.h5.m4.s23
    e14c9c7e22a166dd	165.227.213.187:18080 	last_seen: d0.h5.m6.s6
    685535805cdf0a2c	78.224.252.87:18080 	last_seen: d0.h5.m7.s26
    6599e70919564799	91.48.152.35:18080 	last_seen: d0.h5.m7.s56
    581029ae5b2d0c07	74.65.92.101:18080 	last_seen: d0.h5.m8.s54
    553a485b74426b3f	149.202.171.183:18080 	last_seen: d0.h5.m9.s39
    48231223b294dfe9	5.200.23.99:18800 	last_seen: d0.h5.m12.s48
    92668be0f0996134	37.187.24.170:18080 	last_seen: d0.h5.m17.s0
    9eae3917bf2e7dc8	37.59.44.193:28080 	last_seen: d0.h5.m21.s23
    b510097472e4a235	96.18.147.252:18080 	last_seen: d0.h5.m21.s46
    83d8b34d4c577d71	125.33.208.155:18080 	last_seen: d0.h5.m24.s53
    8ec14ca931e6bae3	92.222.180.113:18080 	last_seen: d0.h5.m25.s43
    fb2d4dc8597bf8ba	212.129.13.124:18080 	last_seen: d0.h5.m26.s45
    4982f5cd436e0b79	123.170.66.166:18080 	last_seen: d0.h5.m27.s47
    ce5a71ff04675bd8	84.250.167.34:18080 	last_seen: d0.h5.m31.s34
    1ef32a5e8adff949	73.187.177.189:18080 	last_seen: d0.h5.m33.s55
    55c9f2077ba750d5	45.77.98.24:18080 	last_seen: d0.h5.m36.s49
    d0d26caf0943b2f4	111.92.240.126:18080 	last_seen: d0.h5.m37.s45
    7b38c4cbe2cd227f	66.70.204.193:18080 	last_seen: d0.h5.m40.s15
    203a62f59dacbcac	94.130.9.194:8180 	last_seen: d0.h5.m40.s18
    eadefac7c395d5f7	198.100.144.155:18080 	last_seen: d0.h5.m47.s26
    c53fd6e9e0c8fe29	181.137.177.132:18080 	last_seen: d0.h5.m50.s3
    25c0120e7b54afeb	77.120.29.195:18080 	last_seen: d0.h5.m50.s30
    d5aa0c606f1e3f15	80.172.224.52:18080 	last_seen: d0.h5.m53.s18
    d3e47ab046f655c1	208.87.220.8:18080 	last_seen: d0.h5.m53.s21
    ed496600e472603c	140.121.171.38:18080 	last_seen: d0.h5.m54.s29
    ecb523024c7ab5d6	175.211.101.26:18080 	last_seen: d0.h5.m54.s51
    b0adf6ea81b105cf	220.180.98.75:18080 	last_seen: d0.h5.m56.s27
    d2040a214d26a291	125.126.109.162:18080 	last_seen: d0.h5.m56.s40
    f373bbe819bed4f5	120.60.143.175:18080 	last_seen: d0.h5.m59.s42
    7749ad69b290fab3	95.79.211.72:18080 	last_seen: d0.h6.m0.s40
    c281e60acf71f93b	89.252.28.26:18080 	last_seen: d0.h6.m1.s48
    9137180722685c84	138.197.182.108:18080 	last_seen: d0.h6.m10.s34
    40810e66136dc556	163.172.255.54:18080 	last_seen: d0.h6.m11.s24
    adb0a06d62456bf1	178.27.208.189:18080 	last_seen: d0.h6.m13.s2
    e879dfbd6247cee9	70.26.53.81:18080 	last_seen: d0.h6.m15.s29
    b99e81e8406a7c62	46.105.99.42:18080 	last_seen: d0.h6.m16.s31
    4bcef7d533db39c1	37.59.97.168:18080 	last_seen: d0.h6.m16.s48
    f8887d9ba3cd85b	173.255.235.69:18080 	last_seen: d0.h6.m16.s57
    20b382d7282f6724	163.172.24.66:18080 	last_seen: d0.h6.m17.s33
    bd52d5e9408688b7	136.243.102.157:8180 	last_seen: d0.h6.m17.s37
    e0c41772850f3969	47.158.71.131:18080 	last_seen: d0.h6.m17.s39
    2951efefcc6189cf	51.15.64.38:18080 	last_seen: d0.h6.m20.s16
    cf7cadeb39ea7118	50.82.45.123:18080 	last_seen: d0.h6.m22.s42
    619956a3fd20198e	37.153.231.94:18080 	last_seen: d0.h6.m22.s48
    e105cf8441a0944a	89.137.21.238:18080 	last_seen: d0.h6.m23.s8
    4ea189246ba0f548	138.68.29.3:18080 	last_seen: d0.h6.m23.s56
    cd79550ed0c401f9	52.51.118.175:18080 	last_seen: d0.h6.m26.s2
    8cd9351ce091f864	59.110.50.157:18080 	last_seen: d0.h6.m26.s2
    9354a3fbdaf661e0	211.110.153.205:18080 	last_seen: d0.h6.m26.s28
    d4240af13ff19014	31.209.59.179:18080 	last_seen: d0.h6.m26.s38
    83d1c360a533ee7e	71.198.213.2:18080 	last_seen: d0.h6.m28.s9
    3d74f48f4c6c2376	91.121.2.76:18080 	last_seen: d0.h6.m29.s4
    109ec61bd63b1e1	5.9.66.144:18080 	last_seen: d0.h6.m34.s44
    3c917c68faa3512f	78.102.134.69:18080 	last_seen: d0.h6.m35.s46
    6ab21a2196b11e19	203.162.53.155:18080 	last_seen: d0.h6.m36.s32
    14328a7d05b8f785	60.205.216.122:18080 	last_seen: d0.h6.m38.s12
    f64b93ebf9cfe4a4	85.212.205.101:18080 	last_seen: d0.h6.m42.s56
    fab96cccf45ba799	14.202.86.152:18080 	last_seen: d0.h6.m44.s32
    d17264a25b5d724a	174.108.46.49:18080 	last_seen: d0.h6.m44.s37
    a20b152ae8237b8c	173.26.121.169:18080 	last_seen: d0.h6.m44.s56
    73b047488a68ecf9	73.141.228.123:18080 	last_seen: d0.h6.m50.s0
    64489c0a54808080	46.105.103.169:28080 	last_seen: d0.h6.m51.s56
    58769f99e429575f	194.135.74.242:18080 	last_seen: d0.h6.m52.s15
    119f3acb980bb139	72.174.128.244:18080 	last_seen: d0.h6.m57.s20
    26a60a6aef6094dd	107.4.235.25:18080 	last_seen: d0.h6.m58.s28
    dab22679b6fdeed4	223.132.249.175:18080 	last_seen: d0.h6.m58.s40
    c74835a6672b8c51	24.226.189.136:18080 	last_seen: d0.h6.m58.s46
    1b6be1665782adda	36.232.130.155:18080 	last_seen: d0.h7.m1.s38
    8729c5bca3adb4d7	108.28.160.132:18080 	last_seen: d0.h7.m3.s36
    780d9e8efacd87a5	99.101.94.101:18080 	last_seen: d0.h7.m11.s24
    80beab3428c02ba2	46.185.226.67:18080 	last_seen: d0.h7.m12.s43
    bff275febfd4f108	91.121.82.47:18080 	last_seen: d0.h7.m17.s47
    e26d6381faf2cc1e	188.221.188.61:18080 	last_seen: d0.h7.m18.s54
    6255bd26a5d1aabb	5.230.146.26:18080 	last_seen: d0.h7.m19.s5
    48016f94493f3ff7	27.253.5.110:18080 	last_seen: d0.h7.m23.s59
    2e036a83e8f36e91	109.193.32.49:18080 	last_seen: d0.h7.m24.s22
    f5aeb2b9777888a4	105.100.30.220:18080 	last_seen: d0.h7.m24.s47
    
    2017-10-03 17:05:58.272	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:05:58.272	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 2765828 bytes worth of blocks
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320419 - 1320438[0m
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320419, 1.8252 seconds, 1515.35 kB/s, size now 67.632 MB
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:05:58.287	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9879 lrh 1330317, chain 1319418
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320439: 1320459/20
    2017-10-03 17:05:58.287	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320459/20 (1320459 - 1320478)
    2017-10-03 17:05:58.287	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320459, first hash <324137a9baa6a5dbfad3f988ac97978e73a0cdf732c4d7de8099c98bb6e2d352>
    2017-10-03 17:05:58.365	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1344	[185.31.136.69:18080 OUT] REMOTE PEERLIST: TIME_DELTA: -3, remote peerlist size=250
    2017-10-03 17:05:58.365	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1345	[185.31.136.69:18080 OUT] REMOTE PEERLIST: b1f5452787b77988	98.150.213.255:18080 	last_seen: d0.h0.m0.s21
    828be90e10b62f87	144.76.60.48:18080 	last_seen: d0.h0.m0.s22
    23e90f729ee96b9	213.47.28.64:18080 	last_seen: d0.h0.m0.s22
    37c278fead435d86	5.189.167.173:18080 	last_seen: d0.h0.m0.s22
    9e5f0f8c248c1ad3	82.161.134.181:18080 	last_seen: d0.h0.m0.s22
    1d4e47929320d76	82.221.101.184:18080 	last_seen: d0.h0.m0.s22
    e43d99df254f089	109.145.98.117:18080 	last_seen: d0.h0.m0.s56
    b6460be89daf9f45	24.34.70.3:18080 	last_seen: d0.h0.m2.s54
    912e9a519a0722ff	116.86.176.43:18080 	last_seen: d0.h0.m3.s55
    b29ff7b3e5c92492	117.198.78.168:18080 	last_seen: d0.h0.m4.s17
    ce3422caa427318f	217.182.11.212:18080 	last_seen: d0.h0.m5.s49
    9313fc8cab4d3c56	37.232.145.10:18080 	last_seen: d0.h0.m6.s2
    3908ce98d2dbb0f9	94.130.30.4:18080 	last_seen: d0.h0.m7.s1
    9894e67ee9d504f8	212.24.96.18:18080 	last_seen: d0.h0.m7.s56
    3ca1198fba2e27f9	97.71.49.49:18080 	last_seen: d0.h0.m8.s13
    1641c7e7e322c846	62.102.148.152:30997 	last_seen: d0.h0.m10.s16
    fba238c7928da3b4	61.121.34.11:18080 	last_seen: d0.h0.m11.s14
    51c9c1137785d35d	62.210.36.142:18080 	last_seen: d0.h0.m11.s25
    9de1507fd58cf0e2	51.15.43.172:18080 	last_seen: d0.h0.m11.s45
    badf62ae7e49eb3a	88.99.37.213:18080 	last_seen: d0.h0.m16.s21
    c5a039a77bfc2f74	178.84.32.140:18080 	last_seen: d0.h0.m17.s37
    d4a2ce7cf8aca94c	163.172.218.237:18080 	last_seen: d0.h0.m20.s7
    fa2a058ba7b96151	86.0.118.245:18080 	last_seen: d0.h0.m20.s42
    dab4179660a3b342	147.135.221.30:18080 	last_seen: d0.h0.m20.s54
    a31f59c0715a9946	45.79.111.224:18080 	last_seen: d0.h0.m21.s55
    4bb0cd79d807d65	108.180.97.116:18080 	last_seen: d0.h0.m27.s8
    ff24eec7f69dc6f7	194.145.207.253:18080 	last_seen: d0.h0.m27.s37
    5062f2304cc41d4d	188.231.147.112:18080 	last_seen: d0.h0.m27.s42
    5a7d46a8fc78ec9c	89.187.130.10:18080 	last_seen: d0.h0.m28.s15
    a7eddc8ee6034dfc	71.191.88.63:18080 	last_seen: d0.h0.m29.s16
    d5aa0c606f1e3f15	80.172.224.52:18080 	last_seen: d0.h0.m29.s27
    2d37d86b237b135d	46.146.79.41:18080 	last_seen: d0.h0.m30.s35
    c21beb08e7776e3d	84.195.146.185:18080 	last_seen: d0.h0.m31.s37
    5a59a9e81eb0d785	24.62.212.231:18080 	last_seen: d0.h0.m32.s18
    319ac46776517ecc	5.39.5.45:18080 	last_seen: d0.h0.m33.s18
    b4b4dc5703559870	195.114.211.27:18080 	last_seen: d0.h0.m35.s39
    19924597535bb9cc	73.253.213.43:18080 	last_seen: d0.h0.m35.s43
    84c96ee44df32c0e	77.120.98.228:18080 	last_seen: d0.h0.m36.s11
    5df058cb527ff14c	104.56.164.125:18080 	last_seen: d0.h0.m39.s8
    4982f5cd436e0b79	123.170.64.211:18080 	last_seen: d0.h0.m40.s3
    b87822b50e363920	85.218.38.96:18080 	last_seen: d0.h0.m40.s44
    bc9f97756f08206c	169.239.128.104:18080 	last_seen: d0.h0.m46.s36
    41d952b55ea152c8	94.23.41.130:28080 	last_seen: d0.h0.m46.s51
    ea31323319309da	68.144.206.118:18080 	last_seen: d0.h0.m50.s40
    d72526e34ab07caf	75.131.22.226:18080 	last_seen: d0.h0.m51.s28
    1b00e456a53dc415	158.69.255.67:18080 	last_seen: d0.h0.m53.s33
    ec46b1cc9e2a0c41	89.92.52.159:18080 	last_seen: d0.h0.m55.s27
    d5aba2530e083b0f	41.253.109.160:18080 	last_seen: d0.h0.m56.s38
    41c5467397ac8164	144.76.71.113:18080 	last_seen: d0.h0.m58.s31
    196c44bbb1994698	91.121.2.76:28080 	last_seen: d0.h1.m0.s11
    1f12818c87d61a5d	104.140.244.186:18080 	last_seen: d0.h1.m0.s19
    299cd4962bfeff3d	155.94.243.106:18080 	last_seen: d0.h1.m0.s38
    2951efefcc6189cf	51.15.64.38:18080 	last_seen: d0.h1.m1.s16
    38984c15cf1110b4	176.9.77.211:18080 	last_seen: d0.h1.m2.s46
    58bcbb433bb73a3e	45.76.143.44:18080 	last_seen: d0.h1.m6.s15
    92e13909c84edf42	91.121.110.134:18080 	last_seen: d0.h1.m6.s51
    f70c8200fb5f6688	24.21.66.105:18080 	last_seen: d0.h1.m8.s21
    ee8b327d173ec761	103.224.119.152:18080 	last_seen: d0.h1.m9.s9
    6f734693667d01d0	23.224.45.26:18080 	last_seen: d0.h1.m11.s19
    be8b25bcc0064ea8	81.232.173.143:18080 	last_seen: d0.h1.m11.s56
    3359989e98335b77	5.147.192.189:18080 	last_seen: d0.h1.m13.s47
    95ad3cebdb1adbbe	52.56.156.27:18080 	last_seen: d0.h1.m15.s6
    f94c9bb2003221c7	138.201.126.98:18080 	last_seen: d0.h1.m15.s39
    36f2601ecb981976	119.18.33.62:18080 	last_seen: d0.h1.m17.s51
    dabda3dc9c45420a	195.245.104.209:18080 	last_seen: d0.h1.m19.s33
    f8b16d6bb2b89c70	96.253.110.173:18080 	last_seen: d0.h1.m21.s30
    2f8bf0be7e860c	85.214.212.113:18080 	last_seen: d0.h1.m28.s16
    4982f5cd436e0b79	123.170.73.20:18080 	last_seen: d0.h1.m34.s0
    d36abeeb8658e0f	91.200.38.242:18080 	last_seen: d0.h1.m34.s48
    ea9c9f94afe6b39c	93.104.211.115:18080 	last_seen: d0.h1.m35.s4
    64bab67e0a57c33e	41.162.83.24:18080 	last_seen: d0.h1.m35.s48
    89e19cea8c3ee48b	122.108.251.145:18080 	last_seen: d0.h1.m39.s34
    16b9c0c93bf03a6b	172.104.84.238:18080 	last_seen: d0.h1.m40.s20
    1c7709b5a72f721d	79.73.75.43:18080 	last_seen: d0.h1.m43.s18
    e2d0037789610b76	62.49.92.9:18080 	last_seen: d0.h1.m46.s15
    525a56ef59cf406a	79.72.215.171:18080 	last_seen: d0.h1.m47.s46
    f0ac17ce3adea12f	62.4.143.197:18080 	last_seen: d0.h1.m48.s34
    9dc8f2f01af3be54	71.93.206.181:18080 	last_seen: d0.h1.m49.s18
    b0adf6ea81b105cf	220.180.98.75:18080 	last_seen: d0.h1.m51.s14
    2b78ddf9fe4b2b08	76.112.176.185:18080 	last_seen: d0.h1.m52.s54
    f994f10ad4baa93d	164.132.166.19:18080 	last_seen: d0.h1.m53.s2
    330605a8ebafc3fc	199.231.85.122:18080 	last_seen: d0.h1.m54.s20
    f0b4ec6d564bdd77	41.60.129.119:18080 	last_seen: d0.h1.m55.s43
    95e807344adddae5	5.196.121.161:18080 	last_seen: d0.h1.m57.s41
    43bad988c835df07	192.228.160.224:18080 	last_seen: d0.h2.m0.s18
    ae19f8c577de447e	138.201.141.12:18080 	last_seen: d0.h2.m1.s19
    fb1e0f8d6eae32b1	163.172.255.56:18080 	last_seen: d0.h2.m3.s2
    cf9faa9594fedd6	103.90.155.2:18080 	last_seen: d0.h2.m4.s33
    a82bd3fc62d4a144	217.226.221.4:18080 	last_seen: d0.h2.m6.s21
    d6ab8ebc5c727a76	23.239.11.154:18080 	last_seen: d0.h2.m6.s55
    336be6e3ded8b584	92.236.54.2:18080 	last_seen: d0.h2.m9.s6
    cbdca433290b4a9b	189.231.106.248:18080 	last_seen: d0.h2.m9.s35
    c8ac171fc905ad4e	139.226.143.79:18080 	last_seen: d0.h2.m10.s43
    5f66fc2d8c404d9f	72.213.194.19:18080 	last_seen: d0.h2.m11.s0
    b524152e2e0c0045	47.203.136.41:18080 	last_seen: d0.h2.m11.s26
    8ac88d0ab57f8cb3	24.245.3.230:18080 	last_seen: d0.h2.m12.s47
    c50bac7940ff819	80.218.67.117:18080 	last_seen: d0.h2.m14.s9
    1e1f67d5ce5174f5	147.251.235.27:18080 	last_seen: d0.h2.m16.s12
    ffae9840a29bd50b	37.59.43.136:28080 	last_seen: d0.h2.m16.s37
    2808a025b6ee08b9	62.210.252.134:18080 	last_seen: d0.h2.m17.s34
    8b6aced1f655255d	144.76.60.212:18080 	last_seen: d0.h2.m19.s25
    137f24c4c327c9e1	72.181.172.198:18080 	last_seen: d0.h2.m22.s38
    6869dada230b0b27	213.240.194.123:18080 	last_seen: d0.h2.m23.s7
    cd22708fb411206d	149.202.171.137:18080 	last_seen: d0.h2.m29.s3
    f1f596dc814a3f57	123.198.210.180:18080 	last_seen: d0.h2.m30.s16
    555a093ef7deac19	85.204.96.68:18080 	last_seen: d0.h2.m33.s50
    585fcc82fe350257	200.117.248.123:18080 	last_seen: d0.h2.m33.s54
    fdf9f3be57177549	163.172.255.60:18080 	last_seen: d0.h2.m37.s15
    644faed10be7f9c6	118.34.38.59:18080 	last_seen: d0.h2.m44.s30
    53ef3a9783766774	136.159.7.132:18080 	last_seen: d0.h2.m44.s32
    6033c604ab40961c	73.236.122.140:18080 	last_seen: d0.h2.m44.s47
    1ebdb531dfd4e2a4	86.28.85.104:18080 	last_seen: d0.h2.m45.s7
    98829f2cf2913db4	191.19.77.229:18080 	last_seen: d0.h2.m45.s33
    c33f1cf47bb013df	46.4.120.155:8180 	last_seen: d0.h2.m45.s58
    9b5769281ca172f9	188.234.15.18:18080 	last_seen: d0.h2.m47.s57
    4d5456d3d2ac8e2f	91.121.164.186:18080 	last_seen: d0.h2.m48.s40
    73b047488a68ecf9	73.141.228.123:18080 	last_seen: d0.h2.m49.s41
    badf77555604a2b8	81.174.173.59:18080 	last_seen: d0.h2.m50.s52
    c4f64922af1d8b4a	62.4.21.85:18082 	last_seen: d0.h2.m51.s8
    cdc966e5fe3b7304	150.140.129.220:18080 	last_seen: d0.h2.m51.s49
    e5df2dffb81e5ae1	76.22.12.199:18080 	last_seen: d0.h2.m52.s50
    9393fb7dfc2e7ec3	94.23.206.130:18080 	last_seen: d0.h2.m56.s8
    162609c896a32a0f	207.244.103.152:18080 	last_seen: d0.h2.m57.s9
    61607217b2b87453	199.168.97.90:18080 	last_seen: d0.h2.m59.s8
    5184f81dca700372	208.167.248.174:18080 	last_seen: d0.h2.m59.s42
    ab3e49a1dc7b834	46.59.79.102:18080 	last_seen: d0.h3.m0.s18
    ca44b536a174f7ae	148.251.51.113:18180 	last_seen: d0.h3.m2.s43
    e63c14325a8b80dc	100.38.72.134:18080 	last_seen: d0.h3.m5.s46
    2ff028b79ca7dff3	163.172.72.186:18080 	last_seen: d0.h3.m8.s18
    4257f183c70f452	24.212.186.14:18080 	last_seen: d0.h3.m11.s50
    9941d6870361ec41	69.139.124.100:18080 	last_seen: d0.h3.m16.s40
    8e42ecc9af6fe427	93.108.179.21:18080 	last_seen: d0.h3.m19.s20
    d1e773c9df9d331b	37.10.71.249:18080 	last_seen: d0.h3.m22.s0
    c4e41921ec9b198f	74.216.93.205:18080 	last_seen: d0.h3.m24.s34
    a0b9c26d2181a188	137.74.164.88:18080 	last_seen: d0.h3.m25.s1
    4c2ef6a79947761d	75.110.5.213:18080 	last_seen: d0.h3.m27.s13
    ac12a99c16720921	24.156.246.30:18080 	last_seen: d0.h3.m30.s36
    86e49505a50873de	165.227.184.90:18080 	last_seen: d0.h3.m31.s38
    334603e974cd30c6	49.255.189.62:18080 	last_seen: d0.h3.m31.s46
    1be16cbf1cbfb3cc	119.23.217.78:18080 	last_seen: d0.h3.m36.s58
    6599e70919564799	91.48.152.35:18080 	last_seen: d0.h3.m40.s41
    6f318312dda09645	80.101.109.52:18080 	last_seen: d0.h3.m42.s25
    b5beda96ebcf948e	2.27.59.255:18080 	last_seen: d0.h3.m42.s52
    1cd1c36c642c9223	51.255.113.103:18080 	last_seen: d0.h3.m44.s34
    5b50a15338801bf1	130.180.41.246:18080 	last_seen: d0.h3.m44.s53
    dc3bc939fdee9142	82.255.104.50:18080 	last_seen: d0.h3.m46.s30
    f69a359367a14540	177.189.209.101:18080 	last_seen: d0.h3.m47.s20
    1bf4af0d040e69f3	13.228.170.37:18080 	last_seen: d0.h3.m50.s38
    76e2bc06d293fcc8	207.154.201.52:18080 	last_seen: d0.h3.m51.s40
    c9f474296ad54da5	90.146.225.146:18080 	last_seen: d0.h3.m52.s30
    f9a1fbc7c150ea4a	83.34.161.68:18080 	last_seen: d0.h3.m56.s10
    407fe015d592c273	213.136.85.203:18080 	last_seen: d0.h3.m56.s45
    b61eca2929f4cf7e	91.121.246.32:18080 	last_seen: d0.h3.m57.s5
    39f566ae70c87ba6	220.81.29.123:18080 	last_seen: d0.h3.m57.s15
    b073e9902e21cb89	192.110.160.146:18080 	last_seen: d0.h3.m59.s26
    acb4d13c5316cf0b	50.7.154.20:18080 	last_seen: d0.h4.m2.s24
    1ef1661498ffe042	2.92.197.205:18080 	last_seen: d0.h4.m2.s26
    89b0771d6ac7263d	86.129.222.188:38080 	last_seen: d0.h4.m3.s4
    b72b6497e0ed0966	91.224.140.213:18080 	last_seen: d0.h4.m3.s45
    5108d8b942ec2879	31.223.172.5:18080 	last_seen: d0.h4.m5.s18
    4f0c5c9231a16555	86.6.55.34:18080 	last_seen: d0.h4.m7.s1
    7676951c4cb1d09a	176.9.147.178:8180 	last_seen: d0.h4.m9.s45
    767587ef049a4e25	67.20.227.235:18080 	last_seen: d0.h4.m17.s35
    90cd2391692adc28	200.203.146.119:18080 	last_seen: d0.h4.m20.s4
    9ebba8944daa4d25	213.136.76.65:18080 	last_seen: d0.h4.m21.s6
    581029ae5b2d0c07	74.65.92.101:18080 	last_seen: d0.h4.m23.s11
    b75f4d3ecac6089c	163.172.174.140:18080 	last_seen: d0.h4.m24.s16
    849fc3a7f9b24429	62.122.211.5:18080 	last_seen: d0.h4.m25.s54
    e35ae64fd5aa51b4	45.34.77.146:18080 	last_seen: d0.h4.m27.s20
    5724e7ce1ac3644f	47.201.39.177:18080 	last_seen: d0.h4.m27.s28
    9c94dd263bc2dc7b	198.255.38.242:18080 	last_seen: d0.h4.m30.s3
    bbf44e8c1ef53267	46.147.193.21:18080 	last_seen: d0.h4.m32.s45
    ac00d0c7f88455f8	93.103.157.176:18080 	last_seen: d0.h4.m33.s37
    ba365865bdbcfa7d	217.182.89.160:18080 	last_seen: d0.h4.m34.s4
    80d9a20b6b416346	138.197.186.253:18080 	last_seen: d0.h4.m34.s14
    20ccef9737c5abf5	79.110.248.248:18080 	last_seen: d0.h4.m34.s33
    b8e60c0d91313a79	94.158.191.34:18080 	last_seen: d0.h4.m35.s23
    226bb911ebb52948	45.63.14.175:18080 	last_seen: d0.h4.m35.s24
    176cce39ce8cbe00	2.83.59.219:18080 	last_seen: d0.h4.m38.s58
    4c9f65c6e4e9aa94	23.95.228.72:18080 	last_seen: d0.h4.m40.s30
    d730bd619f7261e5	46.183.145.69:18080 	last_seen: d0.h4.m41.s32
    5843bcad1c8d6045	191.53.48.26:18080 	last_seen: d0.h4.m42.s33
    9ed237aa8e39d171	70.77.102.148:18080 	last_seen: d0.h4.m50.s18
    95ea00fa320cdcc2	85.169.230.177:18080 	last_seen: d0.h4.m52.s32
    ce5a4292b7fe34e1	219.88.232.152:18080 	last_seen: d0.h4.m53.s1
    c74835a6672b8c51	24.226.189.136:18080 	last_seen: d0.h4.m53.s3
    7ab54e750ea63539	83.215.219.237:18080 	last_seen: d0.h4.m53.s17
    ff33e99f4a6802d6	84.210.24.94:18080 	last_seen: d0.h4.m54.s0
    9dd667f9cc65c755	94.5.124.81:18080 	last_seen: d0.h4.m58.s44
    eb60ffb4ddc80ae2	94.62.143.4:18080 	last_seen: d0.h5.m0.s19
    11ee2daab220deb3	103.208.86.41:18080 	last_seen: d0.h5.m1.s15
    d5f21065b24413c8	50.113.87.201:18080 	last_seen: d0.h5.m3.s14
    1d50bc3c3ffeaea	73.157.212.136:18080 	last_seen: d0.h5.m4.s16
    8e7d653d316181b3	45.76.28.209:18080 	last_seen: d0.h5.m5.s18
    2fcc92915364353b	136.159.7.128:18080 	last_seen: d0.h5.m12.s19
    542fb0f24d746361	86.103.185.111:18080 	last_seen: d0.h5.m12.s25
    cfbb017d92e113f8	124.217.216.42:18080 	last_seen: d0.h5.m12.s28
    ec3a77412de684b7	41.212.105.210:18080 	last_seen: d0.h5.m16.s3
    d24a3a86582d39dc	81.101.138.211:18080 	last_seen: d0.h5.m17.s32
    225ccd807f2e2379	24.130.13.138:18080 	last_seen: d0.h5.m20.s9
    b510097472e4a235	96.18.147.252:18080 	last_seen: d0.h5.m22.s58
    bbe825aa3c5775fc	176.140.90.240:18080 	last_seen: d0.h5.m24.s22
    70d157aa87e3c8a7	82.74.167.90:18080 	last_seen: d0.h5.m25.s23
    c7a58c5be11ea1ce	62.45.247.171:18080 	last_seen: d0.h5.m27.s26
    40810e66136dc556	163.172.255.54:18080 	last_seen: d0.h5.m29.s59
    90c249e7a994f07b	176.194.149.94:18080 	last_seen: d0.h5.m32.s30
    5b35a292e6719d3f	141.239.160.81:18080 	last_seen: d0.h5.m32.s38
    dc9bf32273f5e6bb	212.159.108.40:18080 	last_seen: d0.h5.m34.s16
    e07cb4e067b7d95d	79.229.162.144:18080 	last_seen: d0.h5.m34.s51
    f38e49cb8398e9f	37.59.97.193:18080 	last_seen: d0.h5.m35.s40
    edb7e02cd21d6ebe	193.142.30.83:18080 	last_seen: d0.h5.m35.s41
    b2de57c0f3ecd57d	71.61.185.155:18080 	last_seen: d0.h5.m37.s44
    a5e02d0cb97bb5f0	72.50.221.9:18080 	last_seen: d0.h5.m42.s4
    eb5aa317d7b47bf9	103.240.246.20:18080 	last_seen: d0.h5.m48.s57
    f43f44b3185eaf5c	121.44.183.166:18080 	last_seen: d0.h5.m51.s29
    542ae66f1db62767	167.88.8.173:18080 	last_seen: d0.h5.m51.s58
    b1c4cc7fe68b0d7c	144.76.68.145:18080 	last_seen: d0.h5.m51.s58
    6a3210f0a2fd796d	116.251.193.251:18080 	last_seen: d0.h5.m51.s58
    4c7ac4c534384409	80.101.102.8:18080 	last_seen: d0.h5.m54.s18
    fab96cccf45ba799	14.202.86.152:18080 	last_seen: d0.h5.m54.s55
    6ab21a2196b11e19	203.162.53.155:18080 	last_seen: d0.h5.m55.s17
    808247c42859f8bb	59.46.80.202:18080 	last_seen: d0.h5.m55.s54
    db71ae6cec6c60d9	188.114.88.92:18080 	last_seen: d0.h5.m57.s37
    ff8e6618998d6e99	146.185.156.9:18080 	last_seen: d0.h5.m57.s40
    dbbc9f191dd777ef	94.60.9.138:18080 	last_seen: d0.h5.m58.s54
    269e0625e663f5c7	146.71.76.65:18080 	last_seen: d0.h6.m0.s32
    11ba61f9d712a7f7	118.190.133.167:18080 	last_seen: d0.h6.m0.s47
    8105c8a4bce7c4d1	138.197.182.97:18080 	last_seen: d0.h6.m3.s53
    f4599e5ff1f3f14a	73.176.9.254:18080 	last_seen: d0.h6.m4.s54
    c6a4b70bed74ded	2.36.223.191:18080 	last_seen: d0.h6.m5.s5
    aded26eee5334219	144.76.234.9:18080 	last_seen: d0.h6.m5.s8
    e7298b0d27382722	35.185.245.116:18080 	last_seen: d0.h6.m6.s0
    60b0168fc754f8e5	58.18.7.251:18080 	last_seen: d0.h6.m8.s8
    e0e93e56e57c214b	139.199.212.232:18080 	last_seen: d0.h6.m10.s1
    ef8d074a446c689f	123.249.35.45:18080 	last_seen: d0.h6.m10.s12
    9f5487e6a2605538	80.79.243.213:18080 	last_seen: d0.h6.m11.s41
    1a9fc41666d4e084	67.173.252.20:18080 	last_seen: d0.h6.m12.s51
    ccfdb59d54d248d4	100.40.29.40:18080 	last_seen: d0.h6.m15.s12
    5aa94ddf9f75a37e	171.243.97.178:18080 	last_seen: d0.h6.m15.s28
    119f3acb980bb139	72.174.128.244:18080 	last_seen: d0.h6.m19.s17
    7c4636242d7cced0	165.227.134.118:18080 	last_seen: d0.h6.m22.s56
    7f700908b32a3db3	62.176.6.94:18080 	last_seen: d0.h6.m28.s26
    c68a8ac74490d94e	35.165.221.21:18083 	last_seen: d0.h6.m35.s0
    6e7e8a8d1a04ad48	68.71.79.139:18080 	last_seen: d0.h6.m36.s33
    6690157e3dc88f55	37.59.43.136:18080 	last_seen: d0.h6.m38.s5
    fdb939dbd7b9671	121.75.62.241:18080 	last_seen: d0.h6.m40.s42
    62f4c557ea01aec0	37.59.53.25:18080 	last_seen: d0.h6.m42.s28
    d6e4c5f6e1d55e03	178.235.204.182:18080 	last_seen: d0.h6.m44.s36
    e513495116db09d4	65.60.174.160:18080 	last_seen: d0.h6.m47.s9
    919a7fc7d7640774	5.79.109.73:18080 	last_seen: d0.h6.m51.s0
    
    2017-10-03 17:05:58.864	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[138.197.190.111:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[138.197.190.111:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[138.197.190.111:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[138.197.190.111:18080 OUT]  adding span: 20 at height 1319779, 4.79821 seconds, 140.05 kB/s, size now 68.2728 MB
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[138.197.190.111:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[138.197.190.111:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:05:58.864	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[138.197.190.111:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[138.197.190.111:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.114572
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[138.197.190.111:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[138.197.190.111:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[138.197.190.111:18080 OUT]  checking for gap
    2017-10-03 17:05:58.864	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[138.197.190.111:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:05:58.864	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[138.197.190.111:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:05:58.880	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[138.197.190.111:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:05:59.098	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1344	[138.197.190.111:18080 OUT] REMOTE PEERLIST: TIME_DELTA: -2, remote peerlist size=250
    2017-10-03 17:05:59.098	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1345	[138.197.190.111:18080 OUT] REMOTE PEERLIST: f8b16d6bb2b89c70	96.253.110.173:18080 	last_seen: d0.h0.m0.s2
    cb36e279c5332dfb	69.139.1.150:18080 	last_seen: d0.h0.m0.s43
    81d00dea3ae605c3	107.9.208.164:18080 	last_seen: d0.h0.m0.s44
    3c4cc2f19b6b36f0	84.253.125.186:18080 	last_seen: d0.h0.m0.s44
    59d456cd732a4f92	104.223.103.222:18080 	last_seen: d0.h0.m0.s44
    578bf4dfccf35f3d	162.210.173.15:18080 	last_seen: d0.h0.m0.s44
    6033c604ab40961c	73.236.122.140:18080 	last_seen: d0.h0.m0.s44
    2e036a83e8f36e91	109.193.32.49:18080 	last_seen: d0.h0.m0.s45
    5922f56f556d9bda	185.147.80.2:18080 	last_seen: d0.h0.m0.s45
    2f6e2659e8852121	72.221.78.248:18080 	last_seen: d0.h0.m2.s58
    5524982f207f0c0e	194.67.222.73:18080 	last_seen: d0.h0.m3.s44
    1772b0a9790776dc	165.227.133.10:18080 	last_seen: d0.h0.m7.s12
    ee270f57ef203971	175.180.78.183:18080 	last_seen: d0.h0.m7.s57
    1fdc598d3eab0f20	78.46.223.90:18080 	last_seen: d0.h0.m8.s17
    95ea00fa320cdcc2	85.169.230.177:18080 	last_seen: d0.h0.m9.s10
    e1b6124b08471679	185.198.57.52:18080 	last_seen: d0.h0.m13.s58
    afee6b656ced4514	188.98.209.69:18080 	last_seen: d0.h0.m14.s41
    bc9bed2b587bb247	89.236.238.176:18080 	last_seen: d0.h0.m14.s50
    7a0fdf5da776ec2e	149.202.86.182:18080 	last_seen: d0.h0.m14.s56
    a9181f4cbc03bb1f	96.48.250.65:18080 	last_seen: d0.h0.m15.s53
    28d085d6b0222ed5	104.223.2.240:18080 	last_seen: d0.h0.m16.s9
    1551034e4c8074e3	94.100.221.211:18080 	last_seen: d0.h0.m16.s49
    67c45979bd0ff1e1	84.85.102.113:18080 	last_seen: d0.h0.m16.s54
    e2be3e796a346da3	185.51.62.60:18080 	last_seen: d0.h0.m17.s49
    a3f480e9cd196e3f	90.149.55.202:18080 	last_seen: d0.h0.m19.s6
    407fe015d592c273	213.136.85.203:18080 	last_seen: d0.h0.m21.s8
    c3641979d20fe446	197.97.221.117:18080 	last_seen: d0.h0.m21.s56
    edf77c7ce1a0d41a	183.152.50.230:18080 	last_seen: d0.h0.m24.s18
    e698d1284a679409	81.207.66.80:18080 	last_seen: d0.h0.m24.s22
    401e4aade517c918	86.41.255.71:18080 	last_seen: d0.h0.m26.s14
    7fb9ac311fd9342f	86.127.189.158:18080 	last_seen: d0.h0.m27.s51
    e322fcfec11e896	62.210.104.31:18080 	last_seen: d0.h0.m29.s47
    b90a6a9630fd7c15	138.197.182.114:18080 	last_seen: d0.h0.m29.s47
    20ccef9737c5abf5	79.110.248.248:18080 	last_seen: d0.h0.m30.s53
    c493883456f813d1	138.197.98.191:18080 	last_seen: d0.h0.m30.s54
    d306bccdc5061f72	173.214.164.137:18080 	last_seen: d0.h0.m31.s56
    ce5577c8ad6ae944	137.74.1.223:18080 	last_seen: d0.h0.m32.s10
    a8a7c8bc696e7a77	188.165.214.76:28080 	last_seen: d0.h0.m32.s57
    98829f2cf2913db4	191.19.77.229:18080 	last_seen: d0.h0.m33.s56
    c8e9053014f5701f	79.70.229.203:18080 	last_seen: d0.h0.m33.s57
    52b2866866993af5	90.157.250.17:18080 	last_seen: d0.h0.m37.s38
    4671785848cb0a3e	195.182.153.250:18080 	last_seen: d0.h0.m38.s20
    376830762323be74	113.108.127.84:18080 	last_seen: d0.h0.m39.s9
    5dc68fa93e9e73ff	2.222.33.81:18080 	last_seen: d0.h0.m40.s33
    2943031c4d17c0c4	85.25.74.163:18080 	last_seen: d0.h0.m40.s34
    5cb7fad7ed3c772b	82.22.49.50:18080 	last_seen: d0.h0.m41.s29
    7565296db9b94bcf	163.172.68.146:18080 	last_seen: d0.h0.m42.s35
    2a8934ce51cfa0dd	45.77.79.9:18080 	last_seen: d0.h0.m42.s36
    9c7d478b5c2961	190.77.194.232:18080 	last_seen: d0.h0.m42.s52
    119f3acb980bb139	72.174.128.244:18080 	last_seen: d0.h0.m43.s31
    ac12f01e650ada56	37.48.81.27:18080 	last_seen: d0.h0.m43.s52
    1f12818c87d61a5d	104.140.244.186:18080 	last_seen: d0.h0.m44.s33
    6529f7dd55a4f0c6	176.9.17.19:18080 	last_seen: d0.h0.m44.s56
    a277ebbc5838b252	24.163.106.7:18080 	last_seen: d0.h0.m44.s57
    7b61525c63f9fe53	139.59.59.176:18080 	last_seen: d0.h0.m44.s58
    3908ce98d2dbb0f9	94.130.30.4:18080 	last_seen: d0.h0.m46.s5
    235b282274c6bb57	51.15.81.24:18080 	last_seen: d0.h0.m46.s5
    77a6bcad56e00714	91.145.6.222:18080 	last_seen: d0.h0.m47.s5
    bc71e5b46126603c	144.217.130.9:18080 	last_seen: d0.h0.m47.s5
    380dc190366f9d65	78.90.203.18:18080 	last_seen: d0.h0.m49.s51
    c5a039a77bfc2f74	178.84.32.140:18080 	last_seen: d0.h0.m51.s30
    f8fcb6116176eac4	176.58.121.188:18080 	last_seen: d0.h0.m51.s33
    762cd8a661c315e	94.38.155.159:18080 	last_seen: d0.h0.m52.s6
    3ad962854dd01eb8	66.70.176.29:18080 	last_seen: d0.h0.m56.s50
    5a59a9e81eb0d785	24.62.212.231:18080 	last_seen: d0.h0.m58.s17
    c1fb5d4dbe6e9561	86.31.241.94:18080 	last_seen: d0.h0.m58.s38
    d9a3df859356f7b	185.100.85.141:18080 	last_seen: d0.h1.m0.s37
    ae919696062fdb21	202.5.19.11:18080 	last_seen: d0.h1.m1.s20
    ed1bca56082feb85	116.93.119.79:18080 	last_seen: d0.h1.m1.s37
    c18397c26e3f342d	176.31.117.82:28080 	last_seen: d0.h1.m1.s53
    553a485b74426b3f	149.202.171.183:18080 	last_seen: d0.h1.m2.s4
    9b5769281ca172f9	188.234.15.18:18080 	last_seen: d0.h1.m6.s17
    d72526e34ab07caf	75.131.22.226:18080 	last_seen: d0.h1.m9.s50
    210539b802dfd89e	1.164.241.17:18080 	last_seen: d0.h1.m10.s21
    b092047d86ba8c01	76.184.103.66:18080 	last_seen: d0.h1.m10.s56
    f3eb3ff519cebdf8	103.204.76.111:18080 	last_seen: d0.h1.m12.s7
    35971cf459a4cf31	78.63.249.31:18080 	last_seen: d0.h1.m12.s37
    20b50fb98dc7d2d	124.160.224.28:18080 	last_seen: d0.h1.m12.s57
    f70c8200fb5f6688	24.21.66.105:18080 	last_seen: d0.h1.m14.s30
    bf96ca3406da7843	162.213.38.245:18080 	last_seen: d0.h1.m17.s22
    b3ad9d4aa47699ff	69.85.97.228:18080 	last_seen: d0.h1.m18.s36
    8fa25e7a36cbe0dd	39.72.15.43:18080 	last_seen: d0.h1.m19.s27
    4c997c9190bdd186	85.17.184.227:18080 	last_seen: d0.h1.m19.s29
    adf07bdabc41ff26	80.32.137.224:18080 	last_seen: d0.h1.m20.s30
    80a905c4f1d3efa4	188.165.254.85:28080 	last_seen: d0.h1.m21.s3
    ee00d5163b4c9db6	2.218.9.73:18080 	last_seen: d0.h1.m23.s13
    dabda3dc9c45420a	195.245.104.209:18080 	last_seen: d0.h1.m23.s54
    4636e5ff62530030	81.153.182.25:18080 	last_seen: d0.h1.m27.s4
    9fb61f30fb8fc638	109.230.199.72:18080 	last_seen: d0.h1.m29.s4
    83255d70124b92f0	91.121.169.22:18080 	last_seen: d0.h1.m30.s29
    9dd667f9cc65c755	94.5.124.81:18080 	last_seen: d0.h1.m30.s29
    df91d542f2c3dfe4	212.22.210.68:18080 	last_seen: d0.h1.m31.s35
    fb2cc899c0e899b6	192.99.200.183:18080 	last_seen: d0.h1.m33.s22
    39a378c0a7e05d0a	109.230.231.222:18080 	last_seen: d0.h1.m35.s39
    5ea4a5a0ed847109	86.158.144.44:18080 	last_seen: d0.h1.m36.s5
    17eb86af60f915d7	84.193.156.231:18080 	last_seen: d0.h1.m36.s35
    5312dd09639a236	207.154.248.198:18080 	last_seen: d0.h1.m37.s38
    f2c1b1d24dea2167	173.212.253.154:18080 	last_seen: d0.h1.m38.s17
    6f3a6a77ce83b522	65.34.150.170:18080 	last_seen: d0.h1.m39.s45
    14cdf89fa3f53cab	188.254.32.245:18080 	last_seen: d0.h1.m40.s45
    c06ab67eed9f23d6	37.59.97.72:18080 	last_seen: d0.h1.m48.s22
    c729171e9486f64e	68.104.18.62:18080 	last_seen: d0.h1.m48.s44
    94cb62e71c28bbdb	179.214.35.219:18080 	last_seen: d0.h1.m55.s53
    b1f5452787b77988	98.150.213.255:18080 	last_seen: d0.h1.m58.s35
    6d07c8dc01ce345a	223.132.249.175:18080 	last_seen: d0.h1.m59.s16
    3494b1d3fe2ca17b	81.100.231.241:18080 	last_seen: d0.h2.m0.s18
    cc048d66f501386a	124.104.114.92:18080 	last_seen: d0.h2.m1.s20
    7b6f735e808db742	218.11.97.194:18080 	last_seen: d0.h2.m1.s32
    489b8aba5eb819e8	73.252.210.102:18080 	last_seen: d0.h2.m2.s24
    42e8bc5ad64eaf67	46.71.243.142:18080 	last_seen: d0.h2.m3.s28
    315ce9d382e1591	83.83.197.54:18080 	last_seen: d0.h2.m5.s15
    d08dcd8df58ce023	73.147.11.139:18080 	last_seen: d0.h2.m5.s36
    334603e974cd30c6	49.255.189.62:18080 	last_seen: d0.h2.m11.s49
    e500a531e3762ae6	58.221.49.11:18080 	last_seen: d0.h2.m13.s12
    f959e379d33c7c25	84.75.94.209:18080 	last_seen: d0.h2.m16.s49
    e7a53ab5b4f2a197	83.86.155.137:18080 	last_seen: d0.h2.m18.s22
    aaa832ecbec660a6	78.47.62.223:18080 	last_seen: d0.h2.m22.s27
    306a476a89ee1b2d	201.139.111.131:18080 	last_seen: d0.h2.m22.s36
    9de1507fd58cf0e2	51.15.43.172:18080 	last_seen: d0.h2.m22.s50
    1a9fc41666d4e084	67.173.252.20:18080 	last_seen: d0.h2.m23.s4
    9c94dd263bc2dc7b	198.255.38.242:18080 	last_seen: d0.h2.m23.s17
    9b2d74c586bf4a31	94.199.76.97:18080 	last_seen: d0.h2.m24.s20
    96890e7b13d7c6da	80.254.179.108:18080 	last_seen: d0.h2.m25.s43
    e6ee4c015b7be258	149.202.171.165:18080 	last_seen: d0.h2.m26.s44
    196c44bbb1994698	91.121.2.76:28080 	last_seen: d0.h2.m27.s40
    2808a025b6ee08b9	62.210.252.134:18080 	last_seen: d0.h2.m29.s35
    68ed0dbffb12f6f9	81.96.238.206:18080 	last_seen: d0.h2.m29.s58
    82f4afdafdcc7171	193.95.229.129:18080 	last_seen: d0.h2.m30.s59
    446bf59581337ee9	14.3.137.183:18080 	last_seen: d0.h2.m33.s6
    deef1b213318438b	185.161.172.224:18080 	last_seen: d0.h2.m33.s27
    76925aeb5bfd878a	37.59.56.102:18080 	last_seen: d0.h2.m33.s44
    32b162ce08b788b6	75.71.60.129:18080 	last_seen: d0.h2.m35.s39
    56cc2fb0e5551cd9	94.140.125.242:18080 	last_seen: d0.h2.m36.s12
    cc4af39ba7d810e1	176.9.32.173:18080 	last_seen: d0.h2.m37.s24
    badf77555604a2b8	81.174.173.59:18080 	last_seen: d0.h2.m42.s23
    be8b25bcc0064ea8	81.232.173.143:18080 	last_seen: d0.h2.m46.s40
    a0c640d507a37f1e	24.107.26.159:18080 	last_seen: d0.h2.m51.s23
    2ee76f0e6290e4f8	72.183.124.56:18080 	last_seen: d0.h2.m51.s53
    ed018c37f3e78a9d	147.231.254.151:18080 	last_seen: d0.h2.m55.s13
    ecb523024c7ab5d6	175.211.101.26:18080 	last_seen: d0.h2.m58.s49
    77de528d8f67ef01	101.164.5.3:18080 	last_seen: d0.h3.m0.s7
    8b287ae9aed3036	213.239.211.107:18080 	last_seen: d0.h3.m0.s10
    d487e5ff7f226f4e	98.181.9.159:18080 	last_seen: d0.h3.m9.s30
    6db60492f0c1128e	118.241.167.170:18080 	last_seen: d0.h3.m10.s50
    2e77671584b41a28	109.190.168.192:18080 	last_seen: d0.h3.m11.s35
    39b2e7da6e52a7e5	184.90.194.245:18080 	last_seen: d0.h3.m11.s45
    d5aba2530e083b0f	41.253.118.90:18080 	last_seen: d0.h3.m12.s40
    76474c46bada563a	219.203.88.148:18080 	last_seen: d0.h3.m14.s41
    26f0d3062e75b753	37.97.183.120:18080 	last_seen: d0.h3.m14.s48
    fb2d4dc8597bf8ba	212.129.13.124:18080 	last_seen: d0.h3.m15.s0
    c1ccda65e5d6827b	68.46.208.41:18080 	last_seen: d0.h3.m16.s11
    581029ae5b2d0c07	74.65.92.101:18080 	last_seen: d0.h3.m17.s32
    314bb3eeec4e1573	136.243.94.27:8180 	last_seen: d0.h3.m17.s36
    a43e968c36ee978a	176.9.147.141:18080 	last_seen: d0.h3.m18.s58
    39b47544a40836ce	72.49.220.63:18080 	last_seen: d0.h3.m19.s31
    732bbffc8617f03e	83.233.208.247:18080 	last_seen: d0.h3.m20.s38
    84c96ee44df32c0e	77.120.98.228:18080 	last_seen: d0.h3.m21.s2
    a5c380f9d2aa63c3	47.20.163.52:18080 	last_seen: d0.h3.m22.s44
    f6de6763f06b1878	217.248.89.130:18080 	last_seen: d0.h3.m22.s46
    39f566ae70c87ba6	220.81.29.123:18080 	last_seen: d0.h3.m24.s41
    5a8e050141a66de	108.161.20.152:18080 	last_seen: d0.h3.m33.s32
    ddc73539c0e65691	138.201.235.152:20001 	last_seen: d0.h3.m34.s36
    7af350228f7c557e	77.198.96.69:18080 	last_seen: d0.h3.m35.s15
    9cec186a2dba7662	176.9.0.89:8180 	last_seen: d0.h3.m36.s45
    51c9c1137785d35d	62.210.36.142:18080 	last_seen: d0.h3.m37.s14
    b979718595e616d6	121.145.177.33:18080 	last_seen: d0.h3.m37.s18
    43bad988c835df07	192.228.160.224:18080 	last_seen: d0.h3.m39.s24
    1ef1661498ffe042	2.92.197.205:18080 	last_seen: d0.h3.m41.s1
    27aa6d363e7bb2db	164.132.112.34:18080 	last_seen: d0.h3.m44.s8
    2a041b48a485d185	77.40.18.166:18080 	last_seen: d0.h3.m45.s6
    199a179a3352d4c5	178.17.173.2:18080 	last_seen: d0.h3.m45.s21
    387dc51790bf18b	14.202.234.102:18080 	last_seen: d0.h3.m46.s27
    23e90f729ee96b9	213.47.28.64:18080 	last_seen: d0.h3.m51.s54
    eb95d7a4d3557b33	47.54.197.122:18080 	last_seen: d0.h3.m56.s7
    60b0168fc754f8e5	58.18.7.251:18080 	last_seen: d0.h3.m57.s9
    64bab67e0a57c33e	41.162.83.24:18080 	last_seen: d0.h4.m0.s27
    a40b133b606fefeb	66.130.94.243:18080 	last_seen: d0.h4.m0.s50
    c6d0ea10ce262a42	67.86.33.30:18080 	last_seen: d0.h4.m1.s36
    e07cb4e067b7d95d	79.229.162.144:18080 	last_seen: d0.h4.m6.s37
    a7eddc8ee6034dfc	71.191.88.63:18080 	last_seen: d0.h4.m8.s38
    9123064e8a508e01	95.80.201.102:18080 	last_seen: d0.h4.m9.s17
    70d157aa87e3c8a7	82.74.167.90:18080 	last_seen: d0.h4.m10.s42
    4f0c5c9231a16555	86.6.55.34:18080 	last_seen: d0.h4.m11.s20
    2864cf0e31cffe32	149.202.171.14:18080 	last_seen: d0.h4.m15.s4
    23cc6e8a6bde5dee	13.124.98.129:18080 	last_seen: d0.h4.m18.s18
    257e3424e4e46e09	163.172.74.101:18080 	last_seen: d0.h4.m18.s54
    4191007ec0e09c5d	163.172.255.51:18080 	last_seen: d0.h4.m19.s49
    dc9bf32273f5e6bb	212.159.108.40:18080 	last_seen: d0.h4.m20.s21
    c294f9fbd45a3052	94.46.164.183:18080 	last_seen: d0.h4.m21.s16
    65f0a6fed846d980	109.110.34.6:18080 	last_seen: d0.h4.m25.s44
    cdd4ddc299cf27e5	94.233.95.126:18080 	last_seen: d0.h4.m27.s0
    a9d3119bf19a096	84.47.47.162:18080 	last_seen: d0.h4.m29.s33
    90c249e7a994f07b	176.194.149.94:18080 	last_seen: d0.h4.m32.s40
    2c88d7f712f9c8c9	104.168.164.173:18080 	last_seen: d0.h4.m34.s19
    19376c8ab4313b0	188.68.43.46:18080 	last_seen: d0.h4.m35.s20
    3d41873332c104d0	94.231.191.152:18080 	last_seen: d0.h4.m36.s37
    3ab622a3065b2be8	81.225.68.97:18080 	last_seen: d0.h4.m37.s30
    bb00c84ef41924e1	110.141.193.133:18080 	last_seen: d0.h4.m37.s41
    e715dd65da365762	107.167.185.136:29671 	last_seen: d0.h4.m38.s10
    920a62e5a321f746	88.99.189.188:18080 	last_seen: d0.h4.m38.s45
    89b0771d6ac7263d	86.129.222.188:38080 	last_seen: d0.h4.m40.s10
    ba8933a78e1cc3a8	172.245.161.133:18080 	last_seen: d0.h4.m41.s12
    d0d26caf0943b2f4	111.92.240.126:18080 	last_seen: d0.h4.m41.s44
    6478ac9cdab77002	93.73.200.57:18080 	last_seen: d0.h4.m41.s51
    767587ef049a4e25	67.20.227.235:18080 	last_seen: d0.h4.m43.s52
    d8a89bafcd886108	92.91.128.128:18080 	last_seen: d0.h4.m44.s56
    e898635d8e36afd6	163.172.77.155:18080 	last_seen: d0.h4.m45.s7
    55c9f2077ba750d5	45.77.98.24:18080 	last_seen: d0.h4.m47.s12
    290d4d82d945329d	92.162.165.172:18080 	last_seen: d0.h4.m47.s31
    4fdd022a90853609	81.53.96.14:18080 	last_seen: d0.h4.m47.s59
    1528e31ba768f64	2.235.34.72:18080 	last_seen: d0.h4.m49.s19
    b54424e7c2489dc9	188.165.214.95:28080 	last_seen: d0.h4.m49.s31
    ea9c9f94afe6b39c	93.104.211.115:18080 	last_seen: d0.h4.m50.s20
    8d6c10de04afa466	64.91.248.147:18080 	last_seen: d0.h4.m52.s27
    94119d8cb7a72d2b	37.59.55.60:28080 	last_seen: d0.h4.m59.s51
    30052ada4f592876	144.139.100.121:18080 	last_seen: d0.h5.m0.s12
    78c741cf33fb6490	195.113.91.76:18080 	last_seen: d0.h5.m0.s52
    76b88aff42badef0	198.100.147.123:18080 	last_seen: d0.h5.m1.s36
    7aac206e051a4891	137.74.173.114:18080 	last_seen: d0.h5.m3.s21
    7ccabb87b67bd8af	213.32.95.118:18080 	last_seen: d0.h5.m4.s20
    49c17cd4542a83f5	88.99.58.143:18080 	last_seen: d0.h5.m5.s43
    c4e41921ec9b198f	74.216.93.205:18080 	last_seen: d0.h5.m8.s11
    e1d4a21f9d59f22b	84.27.112.62:18080 	last_seen: d0.h5.m9.s45
    61607217b2b87453	199.168.97.90:18080 	last_seen: d0.h5.m16.s11
    5d424b2661af65cd	37.59.45.174:28080 	last_seen: d0.h5.m17.s18
    abc5b99622986606	213.211.42.221:18080 	last_seen: d0.h5.m18.s40
    94d7fd2cbffba59a	149.202.57.12:32870 	last_seen: d0.h5.m24.s46
    b87a4d42cf287da3	62.64.217.14:18080 	last_seen: d0.h5.m31.s11
    a49f0d6a377560f9	37.59.52.83:18080 	last_seen: d0.h5.m31.s20
    df3dba346336a9b1	202.53.50.224:18080 	last_seen: d0.h5.m36.s44
    ee5b0e61ed7803ff	62.210.124.152:18080 	last_seen: d0.h5.m39.s41
    330605a8ebafc3fc	199.231.85.122:18080 	last_seen: d0.h5.m42.s53
    b5c05726f86b5d5c	89.72.56.52:18080 	last_seen: d0.h5.m45.s58
    ce5a71ff04675bd8	84.250.167.34:18080 	last_seen: d0.h5.m49.s13
    8569351813ea23be	91.113.238.123:18080 	last_seen: d0.h5.m49.s33
    787cb519a9cea8e1	86.151.154.212:18080 	last_seen: d0.h5.m50.s36
    5d9a434a13c783e8	24.253.157.250:18080 	last_seen: d0.h5.m51.s32
    6dd0207ca5a755ca	140.113.119.101:18080 	last_seen: d0.h5.m52.s50
    b510097472e4a235	96.18.147.252:18080 	last_seen: d0.h5.m55.s9
    53ef3a9783766774	136.159.7.132:18080 	last_seen: d0.h5.m56.s24
    2dcb0c8314a5cb2d	96.43.143.250:18080 	last_seen: d0.h5.m59.s10
    7faab1b4397f0b44	54.36.101.254:18080 	last_seen: d0.h5.m59.s16
    a42670ea8d875343	77.27.181.59:18080 	last_seen: d0.h5.m59.s23
    b6902fe5cadb5175	93.136.99.98:18080 	last_seen: d0.h6.m0.s46
    90cd2391692adc28	200.203.146.119:18080 	last_seen: d0.h6.m3.s59
    df39a9fd2b3d20df	93.181.131.60:18080 	last_seen: d0.h6.m5.s0
    ab3e49a1dc7b834	46.59.79.102:18080 	last_seen: d0.h6.m5.s0
    e63c14325a8b80dc	100.38.72.134:18080 	last_seen: d0.h6.m5.s18
    78067652f51eff6	163.172.110.205:18080 	last_seen: d0.h6.m6.s7
    6704cf6c9a299988	94.233.26.52:18080 	last_seen: d0.h6.m11.s27
    
    2017-10-03 17:05:59.208	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:05:59.208	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 1051764 bytes worth of blocks
    2017-10-03 17:05:59.208	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320459 - 1320478[0m
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320459, 0.920402 seconds, 1142.72 kB/s, size now 68.635 MB
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:05:59.223	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9839 lrh 1330317, chain 1319418
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320479: 1320479/20
    2017-10-03 17:05:59.223	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320479/20 (1320479 - 1320498)
    2017-10-03 17:05:59.223	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320479, first hash <6bda048a6848c6fdab6e3059582976e7f0fd5f39a860276ef3a125f5026936d5>
    2017-10-03 17:06:00.970	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[5.196.26.63:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:00.970	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[5.196.26.63:18080 OUT]  downloaded 2908886 bytes worth of blocks
    2017-10-03 17:06:00.970	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[5.196.26.63:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320199 - 1320218[0m
    2017-10-03 17:06:00.970	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[5.196.26.63:18080 OUT]  adding span: 20 at height 1320199, 24.9708 seconds, 116.491 kB/s, size now 71.4091 MB
    2017-10-03 17:06:00.970	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[5.196.26.63:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:00.986	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[5.196.26.63:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:00.986	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[5.196.26.63:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:00.986	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[5.196.26.63:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.101164
    2017-10-03 17:06:00.986	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[5.196.26.63:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:00.986	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[5.196.26.63:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:00.986	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[5.196.26.63:18080 OUT]  checking for gap
    2017-10-03 17:06:00.986	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[5.196.26.63:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:00.986	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[5.196.26.63:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:01.142	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[5.196.26.63:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:01.204	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[5.196.26.63:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:01.392	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[5.196.26.63:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:01.485	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[52.80.93.130:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[52.80.93.130:18080 OUT]  downloaded 930557 bytes worth of blocks
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[52.80.93.130:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320439 - 1320458[0m
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[52.80.93.130:18080 OUT]  adding span: 20 at height 1320439, 4.19641 seconds, 221.751 kB/s, size now 72.2966 MB
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[52.80.93.130:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[52.80.93.130:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:01.485	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[52.80.93.130:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[52.80.93.130:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.197387
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[52.80.93.130:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[52.80.93.130:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[52.80.93.130:18080 OUT]  checking for gap
    2017-10-03 17:06:01.485	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[52.80.93.130:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:01.485	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[52.80.93.130:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:01.579	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[5.196.26.63:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:01.626	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[5.196.26.63:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:02.016	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1344	[5.196.26.63:18080 OUT] REMOTE PEERLIST: TIME_DELTA: 1, remote peerlist size=250
    2017-10-03 17:06:02.016	[P2P6]	DEBUG	net.p2p	src/p2p/net_node.inl:1345	[5.196.26.63:18080 OUT] REMOTE PEERLIST: 17d6c4d82d86a26a	74.72.146.83:18080 	last_seen: d0.h0.m0.s3
    b1f5452787b77988	98.150.213.255:18080 	last_seen: d0.h0.m0.s54
    f81b1f6a6274ff3b	174.109.188.140:18080 	last_seen: d0.h0.m0.s54
    ec8ba49442d7f75f	73.240.230.172:18080 	last_seen: d0.h0.m0.s54
    aeb8539062f1be09	97.101.8.136:18080 	last_seen: d0.h0.m0.s54
    44f337cadc19b07d	73.230.165.139:18080 	last_seen: d0.h0.m0.s54
    21238b67e7684396	74.98.188.121:18080 	last_seen: d0.h0.m0.s54
    464d50dfd427f8bf	202.130.34.124:18080 	last_seen: d0.h0.m0.s57
    980b0849dabc7983	64.185.238.66:18080 	last_seen: d0.h0.m3.s8
    c7149ff6db48b228	124.170.83.44:18080 	last_seen: d0.h0.m4.s12
    de00bc63fcd975f6	5.9.2.145:18080 	last_seen: d0.h0.m7.s19
    75c8ef4cd387878a	45.76.140.175:18080 	last_seen: d0.h0.m8.s35
    c17f4ee2888a5bbb	75.163.94.61:18080 	last_seen: d0.h0.m10.s58
    291816cce1ba25bd	179.105.102.137:18080 	last_seen: d0.h0.m12.s54
    6f8649e0328cd6a5	172.249.163.164:18080 	last_seen: d0.h0.m13.s8
    1a1a950477603c8	46.4.81.146:18080 	last_seen: d0.h0.m13.s9
    47b0016d3d4d03e7	73.42.193.98:18080 	last_seen: d0.h0.m14.s10
    efb1e521c1e3f874	185.16.60.191:18080 	last_seen: d0.h0.m14.s35
    25dd180c027f9227	24.120.235.185:18080 	last_seen: d0.h0.m14.s39
    bf96ca3406da7843	162.213.38.245:18080 	last_seen: d0.h0.m15.s29
    14d131dc93a542c0	185.86.151.113:18080 	last_seen: d0.h0.m16.s19
    9dc8f2f01af3be54	71.93.206.181:18080 	last_seen: d0.h0.m18.s23
    611be970fd97d2b9	104.56.164.125:18080 	last_seen: d0.h0.m19.s10
    39433c727d788092	5.2.67.110:18080 	last_seen: d0.h0.m19.s48
    9894e67ee9d504f8	212.24.96.18:18080 	last_seen: d0.h0.m22.s43
    988c76e4423ec5c	167.88.115.253:18080 	last_seen: d0.h0.m23.s54
    3d74f48f4c6c2376	91.121.2.76:18080 	last_seen: d0.h0.m23.s57
    9c7d478b5c2961	190.77.194.232:18080 	last_seen: d0.h0.m26.s25
    3d861ec94cb21f9a	13.65.248.21:18080 	last_seen: d0.h0.m28.s10
    ace1cfb23347582	75.186.75.143:18080 	last_seen: d0.h0.m29.s11
    ce5a4292b7fe34e1	219.88.232.152:18080 	last_seen: d0.h0.m29.s37
    1ae4f10b4565732	62.4.21.85:18081 	last_seen: d0.h0.m31.s54
    4fad470e4eb9ee4b	155.94.209.114:18080 	last_seen: d0.h0.m34.s5
    67c45979bd0ff1e1	84.85.102.113:18080 	last_seen: d0.h0.m36.s46
    3b4b8a4c63c927c7	111.169.20.131:18080 	last_seen: d0.h0.m38.s54
    711fd780efc6f581	37.48.71.140:27030 	last_seen: d0.h0.m40.s30
    8153cd3f5fa00c2b	190.16.90.150:18080 	last_seen: d0.h0.m40.s56
    77a6bcad56e00714	91.145.6.222:18080 	last_seen: d0.h0.m42.s11
    555a093ef7deac19	85.204.96.68:18080 	last_seen: d0.h0.m42.s37
    a2c4fcd0884905ae	188.221.65.43:18080 	last_seen: d0.h0.m43.s30
    90167a0d03a033fa	66.119.107.185:18080 	last_seen: d0.h0.m44.s22
    4c2ef6a79947761d	75.110.5.213:18080 	last_seen: d0.h0.m45.s48
    2c0782a9b97253f7	73.252.200.173:18080 	last_seen: d0.h0.m48.s57
    1b00e456a53dc415	158.69.255.67:18080 	last_seen: d0.h0.m51.s23
    745304fd876e32a6	188.4.251.182:18080 	last_seen: d0.h0.m52.s5
    3ee6cc377e4aa763	50.100.224.64:18080 	last_seen: d0.h0.m53.s27
    2fe00c86c5550a61	39.108.186.175:18080 	last_seen: d0.h0.m54.s9
    1a508fcdf43e1e3d	24.6.94.73:18080 	last_seen: d0.h0.m54.s24
    c489256412cf2efa	107.167.87.242:18080 	last_seen: d0.h0.m56.s33
    b6850897c834b65a	103.10.61.54:18080 	last_seen: d0.h0.m57.s44
    e0e93e56e57c214b	139.199.212.232:18080 	last_seen: d0.h0.m57.s58
    8d76c152d7f55de	108.26.200.113:18080 	last_seen: d0.h0.m59.s14
    3ab622a3065b2be8	81.225.68.97:18080 	last_seen: d0.h0.m59.s43
    95b9f536450510bd	50.71.143.89:18080 	last_seen: d0.h0.m59.s52
    8d75c983062d6c6d	193.106.160.20:18080 	last_seen: d0.h1.m3.s1
    3b39b8fa8a8a94cf	82.202.212.108:18080 	last_seen: d0.h1.m6.s10
    137f24c4c327c9e1	72.181.172.198:18080 	last_seen: d0.h1.m6.s17
    1551034e4c8074e3	94.100.221.211:18080 	last_seen: d0.h1.m7.s27
    5dc68fa93e9e73ff	2.222.33.81:18080 	last_seen: d0.h1.m8.s24
    96873d0df71c1505	86.122.200.156:18080 	last_seen: d0.h1.m9.s48
    d6fa50bb91f993d6	24.150.243.164:18080 	last_seen: d0.h1.m11.s8
    c48d4d26a54aa70a	62.212.72.235:18080 	last_seen: d0.h1.m11.s16
    92668be0f0996134	37.187.24.170:18080 	last_seen: d0.h1.m11.s33
    626b494e2a158ca0	84.56.223.33:18080 	last_seen: d0.h1.m11.s53
    a2584214551780cf	43.224.249.185:18080 	last_seen: d0.h1.m12.s39
    3ddea280a5a48f35	138.68.135.254:18080 	last_seen: d0.h1.m15.s39
    dd027fd24246c6e8	188.68.54.82:18080 	last_seen: d0.h1.m16.s43
    e9f5faa9f57e43a2	45.50.165.90:18080 	last_seen: d0.h1.m21.s27
    868464ccaf7de86c	82.67.207.20:18080 	last_seen: d0.h1.m25.s8
    5108d8b942ec2879	31.223.172.5:18080 	last_seen: d0.h1.m25.s14
    e752a260f80c426f	72.208.166.195:18080 	last_seen: d0.h1.m28.s26
    faa4286b88d25b4c	163.172.251.247:18080 	last_seen: d0.h1.m30.s36
    b5fe8f6aebfd125b	148.251.8.83:18080 	last_seen: d0.h1.m31.s37
    da75fd32106ac517	72.161.180.172:18080 	last_seen: d0.h1.m35.s53
    86983b97ed4f5aa4	75.156.178.140:18080 	last_seen: d0.h1.m36.s11
    ea222abf4560902e	68.6.210.3:18080 	last_seen: d0.h1.m36.s39
    ec267721f440a06	98.216.123.23:18080 	last_seen: d0.h1.m37.s2
    5d874ea8470b0c6c	65.183.221.14:18080 	last_seen: d0.h1.m37.s7
    6b98bb6c8c200413	185.28.102.232:18080 	last_seen: d0.h1.m39.s10
    99cae2b4ad3cb092	87.92.44.196:18080 	last_seen: d0.h1.m41.s16
    76b1ff06d4324823	73.172.21.53:18080 	last_seen: d0.h1.m42.s23
    eaf17624bd390615	98.151.228.175:18080 	last_seen: d0.h1.m45.s16
    9424ad2ad73ea2fa	68.43.170.74:18080 	last_seen: d0.h1.m46.s43
    8a9084ca2b2d2af1	203.198.91.199:18080 	last_seen: d0.h1.m52.s3
    7fc1da07a35d79e6	221.215.81.37:18080 	last_seen: d0.h1.m54.s11
    da85719d1b56a987	197.87.181.237:18080 	last_seen: d0.h1.m54.s35
    987f745f0a03058	94.23.8.105:18080 	last_seen: d0.h1.m55.s28
    ce9d66188f193e3d	82.68.145.73:18080 	last_seen: d0.h1.m56.s18
    dd43a9c266421fb	172.104.140.81:18080 	last_seen: d0.h2.m1.s4
    9ae5929d65c9d4f3	178.233.15.118:18080 	last_seen: d0.h2.m1.s23
    a499d8943515f345	83.251.191.132:18080 	last_seen: d0.h2.m1.s43
    59982cc8398e20b4	188.27.64.68:18080 	last_seen: d0.h2.m1.s50
    fb1e0f8d6eae32b1	163.172.255.56:18080 	last_seen: d0.h2.m6.s33
    1a9fc41666d4e084	67.173.252.20:18080 	last_seen: d0.h2.m8.s18
    b5feb8e9e531d030	108.61.179.111:18080 	last_seen: d0.h2.m11.s23
    7b38c4cbe2cd227f	66.70.204.193:18080 	last_seen: d0.h2.m12.s24
    53ef3a9783766774	136.159.7.132:18080 	last_seen: d0.h2.m14.s29
    945e9e3023d9d9bc	91.197.57.198:18080 	last_seen: d0.h2.m15.s37
    c4fca13955a54ce3	108.45.127.126:18080 	last_seen: d0.h2.m21.s3
    e2d0037789610b76	62.49.92.9:18080 	last_seen: d0.h2.m21.s55
    3ba7afb983587b17	192.99.5.175:18080 	last_seen: d0.h2.m22.s5
    532eaca7bbcddf79	85.146.27.146:18080 	last_seen: d0.h2.m22.s22
    347fb0410b621dfe	24.189.233.30:18080 	last_seen: d0.h2.m23.s6
    dac4d34bd87943c0	162.253.65.69:18080 	last_seen: d0.h2.m24.s6
    d9be8d877308f15f	13.58.170.247:18080 	last_seen: d0.h2.m24.s8
    e13d9b9ec2ef176e	121.11.21.250:18080 	last_seen: d0.h2.m25.s9
    a874186097ef480	109.172.57.53:18080 	last_seen: d0.h2.m26.s10
    ce6d879d513fef17	94.63.210.214:18080 	last_seen: d0.h2.m26.s52
    3254fe88430051e8	99.150.228.240:18080 	last_seen: d0.h2.m31.s46
    52b29b6687996513	113.110.44.176:18080 	last_seen: d0.h2.m33.s54
    6adc95a9d1bd91dd	192.81.219.211:18080 	last_seen: d0.h2.m36.s3
    398372a2c118eb93	62.212.72.244:18080 	last_seen: d0.h2.m38.s10
    c6a69b25495a2570	95.183.51.117:18080 	last_seen: d0.h2.m40.s17
    55c9f2077ba750d5	45.77.98.24:18080 	last_seen: d0.h2.m41.s17
    15a4a9c5f4e050a	5.103.137.146:18080 	last_seen: d0.h2.m41.s18
    d3c9bcd84f1eafd7	46.160.39.178:18080 	last_seen: d0.h2.m42.s27
    2b7b751fcf8a0a72	138.68.255.32:18080 	last_seen: d0.h2.m43.s8
    cde251696518b00f	68.36.53.114:18080 	last_seen: d0.h2.m44.s32
    b62ab38ee39f5279	47.144.40.119:18080 	last_seen: d0.h2.m44.s33
    2808a025b6ee08b9	62.210.252.134:18080 	last_seen: d0.h2.m44.s41
    f06ced1cd13bcd4e	87.207.68.87:18080 	last_seen: d0.h2.m45.s40
    f8887d9ba3cd85b	173.255.235.69:18080 	last_seen: d0.h2.m46.s13
    224c5927427355be	89.92.52.159:18080 	last_seen: d0.h2.m46.s31
    5062f2304cc41d4d	188.231.147.112:18080 	last_seen: d0.h2.m47.s50
    e98b5d67a0a90ffb	188.68.36.247:18080 	last_seen: d0.h2.m48.s51
    831aa23679624095	5.9.78.35:18080 	last_seen: d0.h2.m53.s10
    b29ff7b3e5c92492	117.198.78.168:18080 	last_seen: d0.h2.m55.s12
    d6f5cc9f390d1445	24.230.234.25:18080 	last_seen: d0.h2.m55.s22
    ec3a77412de684b7	41.212.105.210:18080 	last_seen: d0.h2.m59.s21
    ba1dc84feee56e66	150.117.171.208:18080 	last_seen: d0.h2.m59.s32
    ee956f3f81b82d69	82.198.13.42:18080 	last_seen: d0.h2.m59.s35
    afe6085006548792	109.87.138.116:18080 	last_seen: d0.h3.m2.s2
    5071ff42ad2723c1	58.177.128.113:18080 	last_seen: d0.h3.m6.s38
    3f7a3b39d0670fd9	163.172.169.196:18080 	last_seen: d0.h3.m7.s7
    1ebc2b9d025cdec4	104.140.244.186:18080 	last_seen: d0.h3.m7.s32
    b135312b3ae3700d	174.138.32.58:18080 	last_seen: d0.h3.m10.s37
    43bad988c835df07	192.228.160.224:18080 	last_seen: d0.h3.m10.s43
    b0dc64a697502ba0	94.224.64.74:18080 	last_seen: d0.h3.m10.s47
    5f771751021cebb6	50.79.174.253:18080 	last_seen: d0.h3.m11.s30
    362ca162cb8610ff	86.235.233.205:18080 	last_seen: d0.h3.m12.s17
    60b0168fc754f8e5	58.18.7.251:18080 	last_seen: d0.h3.m12.s29
    53b52d39d5abb138	172.89.238.183:18080 	last_seen: d0.h3.m13.s16
    4c6c70e221247730	72.133.226.79:18080 	last_seen: d0.h3.m16.s43
    762cd8a661c315e	94.38.155.159:18080 	last_seen: d0.h3.m17.s48
    b073e9902e21cb89	192.110.160.146:18080 	last_seen: d0.h3.m18.s26
    5739e1482d23b518	94.23.8.105:28080 	last_seen: d0.h3.m19.s48
    f1621bf8c1e6fec2	96.95.112.237:18080 	last_seen: d0.h3.m21.s22
    688fcc29ec12f99e	5.2.67.20:18080 	last_seen: d0.h3.m21.s26
    2eeb2912dfead1f7	163.172.18.61:18081 	last_seen: d0.h3.m22.s7
    319ac46776517ecc	5.39.5.45:18080 	last_seen: d0.h3.m22.s53
    610f7b7de7ff0e3a	89.142.218.229:18080 	last_seen: d0.h3.m23.s43
    9656d6fb1ffef3a6	70.95.219.136:18080 	last_seen: d0.h3.m23.s54
    47126932995f402e	93.114.160.234:18080 	last_seen: d0.h3.m24.s43
    1dfed0cb69ed1552	119.6.87.81:18080 	last_seen: d0.h3.m25.s20
    ee7638812a92502c	163.172.20.17:18081 	last_seen: d0.h3.m27.s6
    6da619e7cb771ed0	61.164.253.41:18080 	last_seen: d0.h3.m28.s4
    c4f64922af1d8b4a	62.4.21.85:18082 	last_seen: d0.h3.m29.s36
    22dbaf0ec54f9037	82.2.0.57:18080 	last_seen: d0.h3.m29.s44
    a8a7c8bc696e7a77	188.165.214.76:28080 	last_seen: d0.h3.m31.s16
    4795210fed3aa06d	86.246.236.165:18080 	last_seen: d0.h3.m35.s35
    76474c46bada563a	219.203.88.148:18080 	last_seen: d0.h3.m40.s45
    56cc2fb0e5551cd9	94.140.125.242:18080 	last_seen: d0.h3.m40.s46
    56ab06b520e95845	183.77.75.114:18080 	last_seen: d0.h3.m44.s9
    c294f9fbd45a3052	94.46.164.183:18080 	last_seen: d0.h3.m46.s57
    463fb2eba9a2b5e	51.15.58.213:18080 	last_seen: d0.h3.m49.s32
    75f6e37beb721a7b	163.172.132.213:18080 	last_seen: d0.h3.m49.s33
    849fc3a7f9b24429	62.122.211.5:18080 	last_seen: d0.h3.m49.s39
    13d2cfb4eb84d895	45.32.240.37:18080 	last_seen: d0.h3.m50.s32
    6262541d9630e554	85.175.194.153:18080 	last_seen: d0.h3.m51.s32
    349a2f054016039d	88.99.216.194:18080 	last_seen: d0.h3.m53.s41
    5aa94ddf9f75a37e	171.243.97.178:18080 	last_seen: d0.h3.m54.s54
    a1f269d298be21d5	85.10.205.19:18080 	last_seen: d0.h3.m55.s52
    a0c640d507a37f1e	24.107.26.159:18080 	last_seen: d0.h3.m57.s52
    b61eca2929f4cf7e	91.121.246.32:18080 	last_seen: d0.h4.m3.s15
    4f76f7cbdc81fa23	100.38.216.231:18080 	last_seen: d0.h4.m3.s32
    b0adf6ea81b105cf	220.180.98.75:18080 	last_seen: d0.h4.m4.s15
    ab8ad57e665839ce	163.172.164.240:18080 	last_seen: d0.h4.m4.s30
    32f0bdc7516821e1	188.167.131.6:18080 	last_seen: d0.h4.m5.s35
    d5aa0c606f1e3f15	80.172.224.52:18080 	last_seen: d0.h4.m7.s19
    27e0df6f8fabd64b	23.234.15.224:18080 	last_seen: d0.h4.m11.s58
    83d8b34d4c577d71	125.33.208.155:18080 	last_seen: d0.h4.m13.s32
    c6226c2cc5e19581	173.79.138.225:18080 	last_seen: d0.h4.m14.s8
    f43f44b3185eaf5c	121.44.183.166:18080 	last_seen: d0.h4.m18.s30
    5724e7ce1ac3644f	47.201.39.177:18080 	last_seen: d0.h4.m18.s48
    632fc9bae7b7d95c	95.213.252.202:18080 	last_seen: d0.h4.m19.s54
    8488318b5e255db1	76.106.23.47:18080 	last_seen: d0.h4.m20.s41
    387dc51790bf18b	14.202.234.102:18080 	last_seen: d0.h4.m20.s54
    619956a3fd20198e	37.153.231.94:18080 	last_seen: d0.h4.m24.s16
    cde722aa09ff43b8	78.208.60.125:18080 	last_seen: d0.h4.m24.s44
    de62da11ae031bda	107.191.99.175:18080 	last_seen: d0.h4.m25.s59
    98d364d859245a	108.82.116.166:18080 	last_seen: d0.h4.m27.s19
    2429c495b0f477b3	91.121.175.87:18080 	last_seen: d0.h4.m30.s59
    4a983638e752ed68	149.202.171.138:18080 	last_seen: d0.h4.m33.s35
    1c0dd22a771bf50b	94.65.127.148:18080 	last_seen: d0.h4.m36.s26
    ccfdb59d54d248d4	100.40.29.40:18080 	last_seen: d0.h4.m39.s22
    4bcef7d533db39c1	37.59.97.168:18080 	last_seen: d0.h4.m43.s16
    be8b25bcc0064ea8	81.232.173.143:18080 	last_seen: d0.h4.m46.s17
    a7eddc8ee6034dfc	71.191.88.63:18080 	last_seen: d0.h4.m46.s42
    3c917c68faa3512f	78.102.134.69:18080 	last_seen: d0.h4.m46.s48
    c9f474296ad54da5	90.146.225.146:18080 	last_seen: d0.h4.m47.s7
    cd1964f740d01cd4	86.134.72.100:18080 	last_seen: d0.h4.m47.s43
    40682509fe1bd13f	62.141.41.85:18080 	last_seen: d0.h4.m48.s53
    dd770ac8aa7e3e2f	138.201.84.199:18080 	last_seen: d0.h4.m51.s55
    ef75b8254ab30513	94.199.76.97:18080 	last_seen: d0.h4.m54.s3
    fbbbda95cdfbcfc0	89.236.238.176:18080 	last_seen: d0.h4.m54.s29
    38d27f4a639d8789	83.86.252.192:18080 	last_seen: d0.h4.m55.s33
    4dc8f89101e162d4	73.32.250.180:18080 	last_seen: d0.h4.m56.s12
    1e1f67d5ce5174f5	147.251.235.27:18080 	last_seen: d0.h4.m57.s14
    f18ceb7e9a3dd099	69.119.35.223:18080 	last_seen: d0.h4.m58.s11
    2ca97397e6e0f5c6	90.221.146.243:18080 	last_seen: d0.h5.m0.s36
    d13f6a6f9b672150	144.178.141.55:18080 	last_seen: d0.h5.m4.s3
    638f514ac8c49271	101.166.236.38:18080 	last_seen: d0.h5.m10.s47
    e322fcfec11e896	62.210.104.31:18080 	last_seen: d0.h5.m18.s22
    e1d4a21f9d59f22b	84.27.112.62:18080 	last_seen: d0.h5.m23.s1
    290d4d82d945329d	92.162.165.172:18080 	last_seen: d0.h5.m28.s4
    9d1d4a4b6b91dff0	88.99.173.12:18080 	last_seen: d0.h5.m28.s31
    7749ad69b290fab3	95.79.211.72:18080 	last_seen: d0.h5.m30.s53
    b5c05726f86b5d5c	89.72.56.52:18080 	last_seen: d0.h5.m30.s56
    858530f9aa26ab8c	163.172.128.113:18080 	last_seen: d0.h5.m32.s19
    81d1c38ecdee39e4	109.110.34.6:18080 	last_seen: d0.h5.m33.s24
    4a1b1031b7aa348c	95.215.19.16:18080 	last_seen: d0.h5.m34.s26
    60dee45059d19709	94.23.217.34:18080 	last_seen: d0.h5.m39.s49
    89e19cea8c3ee48b	122.108.251.145:18080 	last_seen: d0.h5.m40.s14
    a9d3119bf19a096	84.47.47.162:18080 	last_seen: d0.h5.m41.s30
    8facfb0518c38cff	96.44.132.21:18080 	last_seen: d0.h5.m42.s32
    a05be77de5ddebc	24.194.140.176:18080 	last_seen: d0.h5.m43.s2
    f161315ab62763c2	188.192.251.169:18080 	last_seen: d0.h5.m43.s2
    f82c542ac8651cb0	62.210.104.31:18082 	last_seen: d0.h5.m45.s5
    fa683aeb2f79e8e6	114.76.223.133:18080 	last_seen: d0.h5.m45.s33
    3060d776923baf7a	37.59.56.102:28080 	last_seen: d0.h5.m46.s56
    df4c2677b45ae47b	169.232.246.108:18080 	last_seen: d0.h5.m47.s21
    b404bc992f25be8e	163.172.10.45:18080 	last_seen: d0.h5.m49.s34
    648ccdd85bf24495	217.208.5.3:18080 	last_seen: d0.h5.m50.s27
    330605a8ebafc3fc	199.231.85.122:18080 	last_seen: d0.h5.m53.s34
    56e97c6f22d9a2bf	90.75.214.107:18080 	last_seen: d0.h5.m53.s50
    8e42ecc9af6fe427	93.108.179.21:18080 	last_seen: d0.h5.m57.s1
    1e3eb02925418b06	118.32.218.216:18080 	last_seen: d0.h5.m58.s16
    6ee657ba34041826	178.137.57.41:18080 	last_seen: d0.h5.m59.s7
    1a5cae15cffc5cd0	175.32.126.12:18080 	last_seen: d0.h6.m0.s17
    c9abe4b563d38f78	185.81.157.207:18080 	last_seen: d0.h6.m10.s15
    acb00ab99d05006d	37.59.97.122:18080 	last_seen: d0.h6.m12.s45
    40810e66136dc556	163.172.255.54:18080 	last_seen: d0.h6.m15.s7
    f48c2350d3c2b71f	62.210.161.249:18080 	last_seen: d0.h6.m16.s16
    2c8dcb8f580775b3	92.254.233.9:18080 	last_seen: d0.h6.m17.s56
    cfbb017d92e113f8	124.217.216.42:18080 	last_seen: d0.h6.m19.s8
    31520075fc0ee986	67.193.246.113:18080 	last_seen: d0.h6.m19.s25
    f2c1b1d24dea2167	173.212.253.154:18080 	last_seen: d0.h6.m29.s0
    abe17d276ed9d0ba	124.168.64.161:18080 	last_seen: d0.h6.m29.s39
    97946352e962eac4	50.79.174.253:18082 	last_seen: d0.h6.m30.s14
    7c2a1eb538de1a54	146.90.225.24:18080 	last_seen: d0.h6.m33.s52
    
    2017-10-03 17:06:02.468	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[52.80.93.130:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:03.154	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 1360840 bytes worth of blocks
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320479 - 1320498[0m
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320479, 3.93121 seconds, 346.163 kB/s, size now 73.5944 MB
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:03.154	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9819 lrh 1330317, chain 1319418
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320499: 1320499/20
    2017-10-03 17:06:03.154	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320499/20 (1320499 - 1320518)
    2017-10-03 17:06:03.154	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320499, first hash <66cf01e9cf78340066eb4efe9e1fdc48938b2ad9da1cfa64330ce34581c79db4>
    2017-10-03 17:06:03.154	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[185.31.136.69:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:03.217	[RPC1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#40 to 0.0.0.0 currently we have sockets count:2
    2017-10-03 17:06:03.217	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:72	HTTP [127.0.0.1] GET /getinfo
    2017-10-03 17:06:03.217	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:99	/getinfo processed with 0/3/0ms
    2017-10-03 17:06:03.217	[RPC0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#39 to 127.0.0.1
    2017-10-03 17:06:03.217	[RPC1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#41 to 0.0.0.0 currently we have sockets count:2
    2017-10-03 17:06:03.217	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:72	HTTP [127.0.0.1] GET /json_rpc
    2017-10-03 17:06:03.217	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:117	/json_rpc[hard_fork_info] processed with 0/0/0ms
    2017-10-03 17:06:03.217	[RPC0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#40 to 127.0.0.1
    2017-10-03 17:06:03.217	[RPC1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#42 to 0.0.0.0 currently we have sockets count:2
    2017-10-03 17:06:03.217	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:72	HTTP [127.0.0.1] GET /mining_status
    2017-10-03 17:06:03.217	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:89	/mining_status processed with 0/0/0ms
    2017-10-03 17:06:03.217	[RPC0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#41 to 127.0.0.1
    2017-10-03 17:06:03.451	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[52.80.93.130:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[52.80.93.130:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[52.80.93.130:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[52.80.93.130:18080 OUT]  adding span: 20 at height 1319779, 1.9656 seconds, 341.875 kB/s, size now 74.2352 MB
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[52.80.93.130:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[52.80.93.130:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:03.451	[P2P2]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[52.80.93.130:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[52.80.93.130:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.383524
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[52.80.93.130:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[52.80.93.130:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[52.80.93.130:18080 OUT]  checking for gap
    2017-10-03 17:06:03.451	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[52.80.93.130:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:03.451	[P2P2]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[52.80.93.130:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:04.201	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:04.201	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 719438 bytes worth of blocks
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320499 - 1320518[0m
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320499, 1.0618 seconds, 677.563 kB/s, size now 74.2805 MB
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:04.216	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9799 lrh 1330317, chain 1319418
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320519: 1320519/20
    2017-10-03 17:06:04.216	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320519/20 (1320519 - 1320538)
    2017-10-03 17:06:04.216	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320519, first hash <2ae3ac58924d33cf56c4c32f517010212800add6bf5981cb3504ab74c5a292ff>
    2017-10-03 17:06:04.903	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[52.80.93.130:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:04.903	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[52.80.93.130:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:06:04.903	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[52.80.93.130:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:06:04.903	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[52.80.93.130:18080 OUT]  adding span: 20 at height 1319779, 1.4518 seconds, 462.865 kB/s, size now 74.9213 MB
    2017-10-03 17:06:04.918	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[52.80.93.130:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:04.918	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[52.80.93.130:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:04.918	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[52.80.93.130:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:04.918	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[52.80.93.130:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.484732
    2017-10-03 17:06:04.918	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[52.80.93.130:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:04.918	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[52.80.93.130:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:04.918	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[52.80.93.130:18080 OUT]  checking for gap
    2017-10-03 17:06:04.918	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[52.80.93.130:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:04.918	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[52.80.93.130:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:05.137	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[138.197.190.111:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:05.137	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[138.197.190.111:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:06:05.137	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[138.197.190.111:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:06:05.137	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[138.197.190.111:18080 OUT]  adding span: 20 at height 1319779, 6.27221 seconds, 107.138 kB/s, size now 74.9213 MB
    2017-10-03 17:06:05.137	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[138.197.190.111:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:05.137	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[138.197.190.111:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:05.137	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[138.197.190.111:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:05.152	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[138.197.190.111:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.177683
    2017-10-03 17:06:05.152	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[138.197.190.111:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:05.152	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[138.197.190.111:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:05.152	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[138.197.190.111:18080 OUT]  checking for gap
    2017-10-03 17:06:05.152	[P2P9]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[138.197.190.111:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:05.152	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[138.197.190.111:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:05.152	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[138.197.190.111:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:05.511	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 943302 bytes worth of blocks
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320519 - 1320538[0m
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320519, 1.2948 seconds, 728.529 kB/s, size now 75.1801 MB
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:05.511	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9779 lrh 1330317, chain 1319418
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320539: 1320539/20
    2017-10-03 17:06:05.511	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320539/20 (1320539 - 1320558)
    2017-10-03 17:06:05.511	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320539, first hash <ffd436b0eda696c8fde6e3b80f0f061c64f45b41121541d35e12d4e64bee0ca1>
    2017-10-03 17:06:06.603	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 873706 bytes worth of blocks
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320539 - 1320558[0m
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320539, 1.092 seconds, 800.095 kB/s, size now 76.0133 MB
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:06.603	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9759 lrh 1330317, chain 1319418
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320559: 1320559/20
    2017-10-03 17:06:06.603	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320559/20 (1320559 - 1320578)
    2017-10-03 17:06:06.603	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320559, first hash <4468dbd880b37ad6bdfa195c565f70f3a3b02ea4a3038d38f183eb6ab80289f1>
    2017-10-03 17:06:06.759	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[52.80.93.130:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[52.80.93.130:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[52.80.93.130:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[52.80.93.130:18080 OUT]  adding span: 20 at height 1319779, 1.8408 seconds, 365.052 kB/s, size now 76.6541 MB
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[52.80.93.130:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[52.80.93.130:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:06.759	[P2P2]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[52.80.93.130:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[52.80.93.130:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.386704
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[52.80.93.130:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[52.80.93.130:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[52.80.93.130:18080 OUT]  checking for gap
    2017-10-03 17:06:06.759	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[52.80.93.130:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:06.775	[P2P2]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[52.80.93.130:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:06.884	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[5.196.26.63:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[5.196.26.63:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[5.196.26.63:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[5.196.26.63:18080 OUT]  adding span: 20 at height 1319779, 5.89781 seconds, 113.939 kB/s, size now 76.6541 MB
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[5.196.26.63:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[5.196.26.63:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:06.884	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[5.196.26.63:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[5.196.26.63:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.149393
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[5.196.26.63:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[5.196.26.63:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[5.196.26.63:18080 OUT]  checking for gap
    2017-10-03 17:06:06.884	[P2P3]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[5.196.26.63:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:06.884	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[5.196.26.63:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:06.884	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:758	[5.196.26.63:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
    2017-10-03 17:06:07.695	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[185.31.136.69:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[185.31.136.69:18080 OUT]  downloaded 656146 bytes worth of blocks
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[185.31.136.69:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1320559 - 1320578[0m
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[185.31.136.69:18080 OUT]  adding span: 20 at height 1320559, 1.092 seconds, 600.865 kB/s, size now 76.639 MB
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[185.31.136.69:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[185.31.136.69:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:07.695	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[185.31.136.69:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[185.31.136.69:18080 OUT]  request_missing_objects: check 1, force_next_span 0, m_needed_objects 9739 lrh 1330317, chain 1319418
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[185.31.136.69:18080 OUT]  checking for gap
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1396	[185.31.136.69:18080 OUT]  span size is 0
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1411	[185.31.136.69:18080 OUT]  span from 1320579: 1320579/20
    2017-10-03 17:06:07.695	[P2P6]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[185.31.136.69:18080 OUT]  span: 1320579/20 (1320579 - 1320598)
    2017-10-03 17:06:07.695	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[185.31.136.69:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=20 / 20 from 1320579, first hash <40629bd556d5a7a35578502034fb758b3e8b073faff003cd67ed5455138f5b40>
    2017-10-03 17:06:08.210	[P2P2]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:834	[52.80.93.130:18080 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks, 0 txes)
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:856	[52.80.93.130:18080 OUT]  downloaded 671990 bytes worth of blocks
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:945	[1;33m[52.80.93.130:18080 OUT]  Got NEW BLOCKS inside of handle_response_get_objects: size: 20, blocks: 1319779 - 1319798[0m
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:950	[52.80.93.130:18080 OUT]  adding span: 20 at height 1319779, 1.4352 seconds, 468.219 kB/s, size now 77.2799 MB
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:980	[52.80.93.130:18080 OUT]  lock m_sync_lock, adding blocks to chain...
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:999	[52.80.93.130:18080 OUT]  next span in the queue has blocks 1319439-1319458, we need 1319418
    2017-10-03 17:06:08.210	[P2P2]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1028	[52.80.93.130:18080 OUT]  parent was requested, we'll get back to it
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1256	[52.80.93.130:18080 OUT]  next span is scheduled for 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa, speed 1, ours 0.507484
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1275	[52.80.93.130:18080 OUT]  we should download it as this span was requested long ago
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1344	[52.80.93.130:18080 OUT]  request_missing_objects: check 1, force_next_span 1, m_needed_objects 0 lrh 0, chain 1319418
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1354	[52.80.93.130:18080 OUT]  checking for gap
    2017-10-03 17:06:08.210	[P2P2]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1435	[52.80.93.130:18080 OUT]  span: 1309658/20 (1309658 - 1309677)
    2017-10-03 17:06:08.210	[P2P2]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1468	[52.80.93.130:18080 OUT] -->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=20, txs.size()=0requested blocks count=0 / 20 from 1309658, first hash <195f0e4ba5fca1aa654ebd3bb78e5438ca78705751251b3ec36f0a13e91d032f>
    2017-10-03 17:06:08.288	[RPC1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#43 to 0.0.0.0 currently we have sockets count:2
    2017-10-03 17:06:08.288	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:72	HTTP [127.0.0.1] GET /stop_daemon
    2017-10-03 17:06:08.288	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[152.168.114.234:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 17:06:08.288	[RPC0]	WARN 	net.p2p	src/p2p/net_node.inl:797	[78.203.110.56:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
    2017-10-03 17:06:08.288	[RPC0]	DEBUG	net.p2p	src/p2p/net_node.inl:698	[node] Stop signal sent
    2017-10-03 17:06:08.288	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:634	net_service loop stopped.
    2017-10-03 17:06:08.288	[RPC0]	DEBUG	net.cn	src/rpc/core_rpc_server.h:98	/stop_daemon processed with 0/1/0ms
    2017-10-03 17:06:08.288	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
    2017-10-03 17:06:08.288	10228	DEBUG	net.p2p	src/p2p/net_node.inl:698	[node] Stop signal sent
    2017-10-03 17:06:08.288	[RPC0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#42 to 127.0.0.1
    2017-10-03 17:06:08.553	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
    2017-10-03 17:06:08.553	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:184	Node stopped.
    2017-10-03 17:06:08.553	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
    2017-10-03 17:06:08.553	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#43 to 0.0.0.0
    2017-10-03 17:06:08.553	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
    2017-10-03 17:06:09.147	9900	INFO 	net.p2p	src/p2p/net_node.inl:615	Thread monitor number of peers - done
    2017-10-03 17:06:09.147	[SRV_MAIN]	DEBUG	net.p2p	src/p2p/net_node.inl:1996	Attempting to delete IGD port mapping.
    2017-10-03 17:06:13.181	[SRV_MAIN]	WARN 	net.p2p	src/p2p/net_node.inl:2025	UPnP device was found but not recognized as IGD.
    2017-10-03 17:06:13.184	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
    2017-10-03 17:06:13.185	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[185.31.136.69:18080 4120ee14-8039-3ae4-0ff7-c5ebe4cd9caa OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.185	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#8 to 0.0.0.0
    2017-10-03 17:06:13.186	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[78.203.110.56:18080 b7ab830c-0af8-202d-9080-52975a7f37a0 OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.186	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#32 to 0.0.0.0
    2017-10-03 17:06:13.187	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[138.197.190.111:18080 e45cd6a7-39f2-364a-f283-ccc22cb57544 OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.187	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#1 to 0.0.0.0
    2017-10-03 17:06:13.187	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[152.168.114.234:18080 02695343-a720-efe2-e4bf-a080a3df3b5e OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.188	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#35 to 0.0.0.0
    2017-10-03 17:06:13.188	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[5.196.26.63:18080 64b906aa-68ca-6055-ef82-1b934a9eedcd OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.188	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#4 to 0.0.0.0
    2017-10-03 17:06:13.189	[SRV_MAIN]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1673	Target height decreasing from 1412708 to 0
    2017-10-03 17:06:13.189	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[52.80.93.130:18080 1c7228f4-9733-9b4b-f8ea-483eeae0eac4 OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.189	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#36 to 0.0.0.0
    2017-10-03 17:06:13.190	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[72.208.166.195:18080 2684412d-b306-3a39-57bc-771ecc5766a5 OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.190	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#25 to 0.0.0.0
    2017-10-03 17:06:13.191	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1765	[14.3.137.183:18080 f710b6fd-c4b6-fb75-1957-610d91942f04 OUT] CLOSE CONNECTION
    2017-10-03 17:06:13.191	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#20 to 0.0.0.0
    2017-10-03 17:06:13.194	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
    2017-10-03 17:06:13.428	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
    2017-10-03 17:06:13.428	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully

## moneromooo-monero | 2017-10-03T17:17:12+00:00
This doesn't show the start, so I can't tell which P2P messages were sent to those peers. If it's too large, note that I mentioned placing it on fpaste.org.

## webworxs | 2017-10-03T17:37:54+00:00
Have to work on my skim-reading ability.  Here you go:
https://paste.fedoraproject.org/paste/r7TpMlP02mlMN8wx95svEQ

## moneromooo-monero | 2017-10-03T17:43:01+00:00
Thanks, exactly what I need. It'll be a while now looking for clues.

## moneromooo-monero | 2017-10-03T18:12:54+00:00
Try the branch at https://github.com/moneromooo-monero/bitmonero/tree/ktest

If you know how to use git, then just apply the last patch. If not, just clone that branch and use that.

Run this with --log-level 1,\*p2p\*:DEBUG,net.cn:DEBUG too please.

## moneromooo-monero | 2017-10-10T11:48:29+00:00
ping

## moneromooo-monero | 2017-10-24T10:44:24+00:00
No reply, I can't recall what the problem was as the paste has timed out ,and sync fixes are now in 0.11.1.0, closing. Reopen if still not fixed in 0.11.1.0.

+resolved

## Paul1804 | 2022-04-27T10:44:07+00:00
What can I do in this case ?
I use 'Oxygen Orion' (v0.17.3.0-release)

2022-04-27 08:03:38.495 [P2P9]  WARNING net.p2p src/p2p/net_node.inl:1231       [20.200.83.5:18080 OUT] COMMAND_HANDSHAKE Failed
2022-04-27 08:03:39.389 [P2P3]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:977     Including transaction <b11c03ea49fa5190e1578f12d2d329772046d9de5cdf53a032339446f8df13cc>
2022-04-27 08:03:40.086 [P2P9]  INFO    net.p2p src/p2p/net_node.inl:1429       [20.200.83.5:18080 OUT] Failed to HANDSHAKE with peer [::ffff:20.200.83.5]:18080
2022-04-27 08:03:40.442 [P2P3]  ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:777   Setting timer on a shut down object
2022-04-27 08:03:40.574 [P2P9]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:336     [20.200.83.5:18080 OUT] [levin_protocol] -->> start_outer_call failed
2022-04-27 08:03:43.295 [P2P3]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2917    [20.200.83.5:18080 OUT] [0] state: closed in state before_handshake
2022-04-27 08:03:46.601 [P2P3]  INFO    net.p2p src/p2p/net_node.inl:2718       [20.200.83.5:18080 6cfe7c2d-1372-4459-9b4d-0633b5b4e043 OUT] CLOSE CONNECTION
2022-04-27 08:04:11.639 [P2P9]  INFO    net.p2p src/p2p/net_node.inl:2699       [162.218.65.112:18380 522681b4-3d0a-4104-ac27-8576f0e47d28 OUT] NEW CONNECTION


## selsta | 2022-04-30T10:10:53+00:00
@Paul1804 you have to explain in more detail what issues you have.

## Paul1804 | 2022-05-05T08:32:40+00:00
Oh, sorry ! All is working.. But I have another question. Why daemon, which I wrote is fall ? 
What wrong ?

[Unit]
Description=Monerod

[Service]
User=monero
Group=monero
ExecStart=/home/monero/monero/monerod  
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target

...and this bitmonero.log

2022-05-05 08:11:39.496 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2022-05-05 08:11:39.497     7f5bb67fc700        INFO    global  contrib/epee/include/console_handler.h:383  EOF on stdin, exiting
2022-05-05 08:11:39.524 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:81     p2p net loop stopped
2022-05-05 08:11:39.555 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping core RPC server...
2022-05-05 08:11:39.563 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:228       Node stopped.
2022-05-05 08:11:39.658 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2022-05-05 08:11:39.682 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:91     Deinitializing p2p...
2022-05-05 08:11:40.596 [SRV_MAIN]      INFO    global  src/daemon/core.h:102   Deinitializing core...
2022-05-05 08:11:40.653 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2022-05-05 08:11:40.654 [SRV_MAIN]      INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully


# Action History
- Created by: ghost | 2017-09-26T20:38:27+00:00
- Closed at: 2017-10-24T10:56:25+00:00
