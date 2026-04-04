---
title: batch resize loop stalls node
source_url: https://github.com/monero-project/monero/issues/3656
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-04-18T00:38:09+00:00'
updated_at: '2018-05-16T11:01:00+00:00'
type: issue
status: closed
closed_at: '2018-05-16T11:01:00+00:00'
---

# Original Description
```
4-18 00:34:36.626	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:36.627	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:36.627	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:36.627	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:36.627	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:36.627	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:36.859	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[185.175.252.32:51422 INC] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
2018-04-18 00:34:37.393	[P2P3]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[119.123.45.99:12080 40add7b8-bfda-be5f-0ae4-e09496365814 INC] NEW CONNECTION
2018-04-18 00:34:37.536	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[95.121.110.150:18080 OUT] Received NOTIFY_REQUEST_GET_OBJECTS (20 blocks, 0 txes)
2018-04-18 00:34:37.913	[P2P7]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[81.4.104.14:39020 INC] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:39.241	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash e6fd15f275a3c5046d969cbed0596a5f95773cc5f30d7e5c9649b8904df80a55 not found in db
2018-04-18 00:34:39.246	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[220.237.108.170:18080 OUT] Received NOTIFY_REQUEST_GET_OBJECTS (20 blocks, 0 txes)
2018-04-18 00:34:39.327	[P2P4]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:39.328	[P2P4]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:39.328	[P2P4]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:39.328	[P2P4]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:39.328	[P2P4]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:39.328	[P2P4]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:40.872	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[192.110.160.146:18080 a78f35ac-e745-a7b6-0704-34a1772f2fd2 OUT] CLOSE CONNECTION
2018-04-18 00:34:40.874	[P2P5]	INFO 	net	contrib/epee/include/net/levin_protocol_handler_async.h:174	[176.53.49.187:18080 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2018-04-18 00:34:40.874	[P2P5]	INFO 	net	contrib/epee/include/storages/levin_abstract_invoke2.h:122	Failed to invoke command 1001 return code -4
2018-04-18 00:34:40.875	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[5.9.48.66:51683 f562f8b8-532c-2b07-b71f-89d86db748e2 INC] CLOSE CONNECTION
2018-04-18 00:34:40.876	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[136.243.153.156:45770 733a6b62-fde5-b4b4-8023-1baa81a6c768 INC] CLOSE CONNECTION
2018-04-18 00:34:40.877	[P2P5]	WARN 	net.p2p	src/p2p/net_node.inl:715	[176.53.49.187:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-04-18 00:34:40.877	[P2P2]	WARN 	net.p2p	src/p2p/net_node.inl:764	[176.53.49.187:18080 OUT] COMMAND_HANDSHAKE Failed
2018-04-18 00:34:40.877	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:941	[176.53.49.187:18080 OUT] Failed to HANDSHAKE with peer 176.53.49.187:18080
2018-04-18 00:34:40.879	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[176.53.49.187:18080 e6fb50d3-f76e-0f4f-a217-1b8fb60f6a62 OUT] CLOSE CONNECTION
2018-04-18 00:34:40.893	[P2P8]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1563	[185.112.158.127:48340 INC]  we've reached this peer's blockchain height
2018-04-18 00:34:40.914	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[204.8.15.5:18080 4aa40d21-ac90-bb92-0394-c261ccca6b65 OUT] NEW CONNECTION
2018-04-18 00:34:41.831	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash e6fd15f275a3c5046d969cbed0596a5f95773cc5f30d7e5c9649b8904df80a55 not found in db
2018-04-18 00:34:41.839	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[192.99.200.183:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:41.852	[P2P5]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:313	Remote blockchain height: 1546634, id: <908dfe40010f8bbd442e538c8d65179d0f6f8133d3770e2fc6e4511d6a58396e>
2018-04-18 00:34:41.856	[P2P7]	ERROR	verify	src/cryptonote_core/blockchain.cpp:225	Output does not exist! amount = 0
2018-04-18 00:34:41.856	[P2P7]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3105	Failed to get output keys for tx with amount = 0.000000000000 and count indexes 7
2018-04-18 00:34:41.856	[P2P7]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2707	Failed to check ring signature for tx <e6fd15f275a3c5046d969cbed0596a5f95773cc5f30d7e5c9649b8904df80a55>  vin key with k_image: <20b908691076f606a04c7885be796b80e8bdfca8f0756d067d3080436d08c775>  sig_index: 0
2018-04-18 00:34:41.856	[P2P7]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2710	  *pmax_used_block_height: 0
2018-04-18 00:34:41.856	[P2P7]	INFO 	txpool	src/cryptonote_core/tx_pool.cpp:261	tx used wrong inputs, rejected
2018-04-18 00:34:41.856	[P2P7]	ERROR	verify	src/cryptonote_core/cryptonote_core.cpp:772	Transaction verification failed: <e6fd15f275a3c5046d969cbed0596a5f95773cc5f30d7e5c9649b8904df80a55>
2018-04-18 00:34:41.856	[P2P7]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:782	[81.4.104.14:39020 INC] Tx verification failed, dropping connection
2018-04-18 00:34:41.856	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:41.856	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:41.857	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:41.857	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:41.857	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:41.857	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:41.889	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[91.121.87.10:28080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:41.904	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[138.201.60.198:8180 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:41.915	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[178.63.48.196:28080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:41.926	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[66.228.41.201:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:41.944	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[192.110.160.146:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:41.950	[P2P3]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[188.165.214.95:28080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:41.961	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[204.8.15.5:59092 e8bcef4c-26db-1f55-5f38-3b0d2a05ec32 INC] NEW CONNECTION
2018-04-18 00:34:42.028	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[95.161.170.130:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:42.137	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[67.218.193.131:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:42.773	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[185.175.252.32:51422 INC] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
2018-04-18 00:34:43.855	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:1543	[0.0.0.0:0 OUT] back ping connect failed to 119.123.45.99:18080
2018-04-18 00:34:44.083	[P2P8]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:313	Remote blockchain height: 1553545, id: <ca8f8146f7789bf4a2544351d6bcb8b647fdf002b33db79bbe0855ad10f9df1b>
2018-04-18 00:34:44.089	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[204.8.15.5:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:44.168	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[163.172.255.56:18080 87d96dbf-99e6-2360-f5b3-ad3f517f5973 OUT] NEW CONNECTION
2018-04-18 00:34:44.369	[P2P1]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1602	[204.8.15.5:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=7243, m_start_height=1546302, m_total_height=1553545
2018-04-18 00:34:45.149	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[185.175.252.32:51422 INC] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
2018-04-18 00:34:45.445	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:45.445	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:45.445	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:45.445	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:45.445	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:45.446	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:45.731	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[192.99.200.183:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:45.785	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[178.63.48.196:28080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:45.807	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[66.228.41.201:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:45.818	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[192.110.160.146:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:45.822	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[188.165.214.95:28080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:45.836	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[138.201.60.198:8180 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:45.842	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[91.121.87.10:28080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:46.034	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[95.161.170.130:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:46.099	[P2P8]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[67.218.193.131:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:47.103	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[185.175.252.32:51422 INC] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
2018-04-18 00:34:47.939	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:47.942	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:47.942	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:47.942	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:47.942	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:47.942	[P2P8]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:50.552	[P2P4]	INFO 	net	contrib/epee/include/net/levin_protocol_handler_async.h:174	[163.172.255.56:18080 OUT] Timeout on invoke operation happened, command: 1001 timeout: 5000
2018-04-18 00:34:50.571	[P2P4]	INFO 	net	contrib/epee/include/storages/levin_abstract_invoke2.h:122	Failed to invoke command 1001 return code -4
2018-04-18 00:34:50.571	[P2P4]	WARN 	net.p2p	src/p2p/net_node.inl:715	[163.172.255.56:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-04-18 00:34:50.571	[P2P2]	WARN 	net.p2p	src/p2p/net_node.inl:764	[163.172.255.56:18080 OUT] COMMAND_HANDSHAKE Failed
2018-04-18 00:34:50.572	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:941	[163.172.255.56:18080 OUT] Failed to HANDSHAKE with peer 163.172.255.56:18080
2018-04-18 00:34:50.574	[P2P0]	INFO 	net	contrib/epee/include/net/levin_protocol_handler_async.h:238	[204.8.15.5:18080 OUT] Timeout on invoke operation happened, command: 1007 timeout: 5000
2018-04-18 00:34:50.574	[P2P0]	INFO 	net	contrib/epee/include/storages/levin_abstract_invoke2.h:122	Failed to invoke command 1007 return code -4
2018-04-18 00:34:50.574	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1605	[204.8.15.5:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2018-04-18 00:34:50.574	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[185.175.252.32:51422 INC] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
2018-04-18 00:34:50.584	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:50.585	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:50.585	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:50.585	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:50.585	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:50.585	[RPC1]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:51.096	[P2P8]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[174.138.31.231:57728 f1d6bed7-5393-f68e-208d-83c97fcd3f50 INC] NEW CONNECTION
2018-04-18 00:34:51.099	[P2P7]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[81.4.104.14:39020 0352affd-9388-1c04-b304-ce7bc2276229 INC] CLOSE CONNECTION
2018-04-18 00:34:51.100	[P2P3]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[204.8.15.5:59092 e8bcef4c-26db-1f55-5f38-3b0d2a05ec32 INC] CLOSE CONNECTION
2018-04-18 00:34:51.101	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1563	[136.243.153.156:18080 OUT]  we've reached this peer's blockchain height
2018-04-18 00:34:51.106	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[119.123.45.99:12080 40add7b8-bfda-be5f-0ae4-e09496365814 INC] CLOSE CONNECTION
2018-04-18 00:34:51.106	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[163.172.255.56:18080 87d96dbf-99e6-2360-f5b3-ad3f517f5973 OUT] CLOSE CONNECTION
2018-04-18 00:34:51.106	[P2P9]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[5.9.48.66:18070 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2018-04-18 00:34:51.360	[P2P0]	WARN 	net.p2p	src/p2p/net_node.inl:1671	[174.138.31.231:57728 INC] COMMAND_HANDSHAKE came, but process_payload_sync_data returned false, dropping connection.
2018-04-18 00:34:51.362	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1783	[174.138.31.231:57728 f1d6bed7-5393-f68e-208d-83c97fcd3f50 INC] CLOSE CONNECTION
2018-04-18 00:34:52.776	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash 537a62284b65f58919f535d2ac43110394bfc0ffaec542a0ae529efad4f3d762 not found in db
2018-04-18 00:34:53.090	[P2P9]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2087	transaction with hash 537a62284b65f58919f535d2ac43110394bfc0ffaec542a0ae529efad4f3d762 not found in db
2018-04-18 00:34:53.090	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:225	Output does not exist! amount = 0
2018-04-18 00:34:53.090	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:3105	Failed to get output keys for tx with amount = 0.000000000000 and count indexes 7
2018-04-18 00:34:53.090	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2707	Failed to check ring signature for tx <537a62284b65f58919f535d2ac43110394bfc0ffaec542a0ae529efad4f3d762>  vin key with k_image: <08d44886e599908e6cdbc44002af3de1e39becb46e877efda8a427914febd7ab>  sig_index: 0
2018-04-18 00:34:53.090	[P2P9]	ERROR	verify	src/cryptonote_core/blockchain.cpp:2710	  *pmax_used_block_height: 0
2018-04-18 00:34:53.091	[P2P9]	INFO 	txpool	src/cryptonote_core/tx_pool.cpp:261	tx used wrong inputs, rejected
2018-04-18 00:34:53.091	[P2P9]	ERROR	verify	src/cryptonote_core/cryptonote_core.cpp:772	Transaction verification failed: <537a62284b65f58919f535d2ac43110394bfc0ffaec542a0ae529efad4f3d762>
2018-04-18 00:34:53.091	[P2P9]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:782	[5.9.48.66:18070 OUT] Tx verification failed, dropping connection
2018-04-18 00:34:54.142	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:54.143	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:54.143	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:54.143	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:54.143	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:54.143	[RPC0]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:55.093	[P2P6]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[81.4.104.14:46238 691ce732-12b2-783f-fd33-b4435b2dfcc7 INC] NEW CONNECTION
2018-04-18 00:34:55.574	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:928	[0.0.0.0:0 OUT] Connect failed to 70.171.224.97:18080
2018-04-18 00:34:55.693	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[95.90.47.177:18080 b766e271-30a2-8969-2b21-df08d1ca7daf OUT] NEW CONNECTION
2018-04-18 00:34:56.048	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:763	[73.153.13.180:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (15 txes)
2018-04-18 00:34:56.332	[P2P5]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[185.175.252.32:51422 INC] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
2018-04-18 00:34:56.701	[P2P3]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:313	Remote blockchain height: 1553545, id: <ca8f8146f7789bf4a2544351d6bcb8b647fdf002b33db79bbe0855ad10f9df1b>
2018-04-18 00:34:56.718	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-04-18 00:34:56.718	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     82448465920
2018-04-18 00:34:56.718	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      49310928896
2018-04-18 00:34:56.718	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 33137537024
2018-04-18 00:34:56.718	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-04-18 00:34:56.718	[P2P7]	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.5981  Percent threshold: 0.8000
2018-04-18 00:34:57.077	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1768	[95.90.47.177:63667 9e531399-f376-6351-f764-32b28d3d5f0b INC] NEW CONNECTION
2018-04-18 00:34:57.451	[P2P0]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1602	[81.4.104.14:46238 INC] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=7243, m_start_height=1546302, m_total_height=1553545
2018-04-18 00:34:58.226	[P2P4]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:804	[185.175.252.32:51422 INC] Received NOTIFY_REQUEST_GET_OBJECTS (100 blocks, 0 txes)
^C
```

```
user@box:~/.bitmonero$ monerod status
Height: 1546303/1553545 (99.5%) on mainnet, mining at 173 H/s, net hash 372.14 MH/s, v7, up to date, 5(out)+4(in) connections, uptime 9d 21h 18m 36s
```

restarting fixes it

# Discussion History
## shigutso | 2018-04-18T13:20:48+00:00
this is major, I'm running monerod with `set_log 1,*p2p*:DEBUG,*queue*:DEBUG` (as recommended by @stoffu), will report here when my daemon hangs

## BigslimVdub | 2018-04-18T17:38:37+00:00
I am running aeond with logging since lack of hd space. I can report back if it hangs or locks up

## stoffu | 2018-04-18T19:21:30+00:00
I've made precompiled debug daemon binaries with some additional logging:

- ~~https://github.com/stoffu/monero/releases/tag/monero-debug-v0.1.0~~

**EDIT: some people reported that the debug-v0.1.0 binary crashes with the "illegal instruction" error, so please try an updated version:**

- https://github.com/stoffu/monero/releases/tag/monero-debug-v0.1.1


## BigslimVdub | 2018-04-19T01:06:25+00:00
![aeond lockup](https://user-images.githubusercontent.com/30030687/38965359-e78cb972-4341-11e8-86ea-79a78a29b520.PNG)
[AeonD lockup.txt](https://github.com/monero-project/monero/files/1926254/AeonD.lockup.txt)
![lockup system usage](https://user-images.githubusercontent.com/30030687/38965360-e7b1390a-4341-11e8-9677-cb1a78ac0899.PNG)

OK so my Daemon locked up on Aeon after about 7 hours when running the logging as above. I had been periodically checking it during the day with _status_ and it was fine. Checked again tonight and it looked like it was stuck so I went to check status again and nothing. 

I didn't close Daemon for a while  as I was copying the log file info over. I noticed the log file was getting bigger (as if daemon was still running) but the cmd window showed it was not. I checked for errors in the whole log file and it looks like the basic 406 block height error and incorrect minimum fee errors but no other errors. Note that on this same hardware I ran same daemon for over 3 days straight no issues no lockups (not using logging). I had to CTRL+C to close the daemon as it was unresponsive. I reopened and its running just fine. 

EDIT: 
It looks like original log and mine show Daemon locking up when either incorrect fee or incorrect ring size used. 

## BigslimVdub | 2018-04-20T00:36:40+00:00
[test.txt](https://github.com/monero-project/monero/files/1930192/test.txt)
@stoffu I ran your specific Daemon for Aeon and it crashed about 6 hours into running. It actually quit and force closed itself. After that I closed and opened the build Daemon (from 1.7.2) and its been running 13 hours no issues with no heavy logging as seen on the bottom half of the test.txt. It seems the daemon falls behind on blocks and then locks up/crashes when trying to catch back up. 

## Gingeropolous | 2018-04-20T03:29:49+00:00
its so glitchy though. I haven't seen it happen on my node since that instance I reported, and I saw it before on the same node like weeks ago. I'll try to grab a stack trace next time. 

## shigutso | 2018-04-20T14:25:34+00:00
my aeond just crashed

[log.txt](https://github.com/monero-project/monero/files/1932462/log.txt)


## shigutso | 2018-04-20T14:38:07+00:00
crashed again

[log2.txt](https://github.com/monero-project/monero/files/1932492/log2.txt)

edit: now monerod has crashed (log3.txt)

[log3.txt](https://github.com/monero-project/monero/files/1933018/log3.txt)



## BigslimVdub | 2018-04-20T18:55:38+00:00
I have noticed when running Monero gui I get 8out 0in but when running moneroD I get 8out 45in. I can not get gui to have only in connections. 

## moneromooo-monero | 2018-04-27T18:43:17+00:00
> edit: now monerod has crashed (log3.txt)

Do you have a stack trace for this crash ?


## shigutso | 2018-04-28T13:15:11+00:00
> Do you have a stack trace for this crash ?

I'll take a look on how to stack trace on Windows and will post here again when it crashes.
My Linux box didn't crash/hang yet.

## BigslimVdub | 2018-05-11T01:44:14+00:00
so, resolved?

## moneromooo-monero | 2018-05-11T17:38:02+00:00
The stall is likely fixed in release-0.12. The crash (if there is one) is not.

## shigutso | 2018-05-11T17:46:19+00:00
I think the crash had something to do with @stoffu's debug build, as the newest ones are not crashing anymore 

## Gingeropolous | 2018-05-16T03:04:17+00:00
@moneromooo-monero , the stall was with lithium luna binaries... or do you mean release-.12 the branch?

BRANCHES SO CONFUSING

## moneromooo-monero | 2018-05-16T10:27:51+00:00
v0.12.0.0 was stalling, release-0.12 now has the fixes for all known stalls and people who hit the bug now report it's fixed.

+resolved


# Action History
- Created by: Gingeropolous | 2018-04-18T00:38:09+00:00
- Closed at: 2018-05-16T11:01:00+00:00
