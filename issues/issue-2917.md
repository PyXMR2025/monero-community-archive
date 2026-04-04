---
title: Monerod crashing when trying to resize db on Windows10
source_url: https://github.com/monero-project/monero/issues/2917
author: saxenadev
assignees: []
labels: []
created_at: '2017-12-13T10:04:45+00:00'
updated_at: '2018-01-04T13:24:28+00:00'
type: issue
status: closed
closed_at: '2018-01-04T13:24:28+00:00'
---

# Original Description
Monerod is crashing when trying to resize db. find detailed log below:

2017-12-13 09:43:14.253	7564	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-13 09:43:14.253	7564	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-13 09:43:14.253	7564	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-13 09:43:14.268	7564	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-13 09:43:25.402	7564	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-13 09:43:25.402	7564	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-13 09:43:25.418	7564	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-13 09:43:25.418	7564	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-13 09:43:25.418	7564	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-13 09:43:25.418	7564	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-12-13 09:44:51.153	5728	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-13 09:44:51.153	5728	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:TRACE
2017-12-13 09:44:51.153	5728	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-13 09:44:51.169	5728	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-12-13 09:44:51.169	5728	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-13 09:44:51.169	5728	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-13 09:44:51.169	5728	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:136	Blockchain::Blockchain
2017-12-13 09:44:51.169	5728	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-13 09:44:51.169	5728	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-12-13 09:44:51.169	6456	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-12-13 09:44:51.169	9976	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-12-13 09:44:51.169	6604	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-12-13 09:44:51.169	1108	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-12-13 09:44:51.669	6456	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-12-13 09:44:51.669	6456	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-12-13 09:44:51.685	1108	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-12-13 09:44:51.685	1108	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-12-13 09:44:51.685	6604	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-12-13 09:44:51.685	6604	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-12-13 09:44:51.685	9976	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-12-13 09:44:51.685	9976	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-12-13 09:44:51.685	5728	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-12-13 09:44:51.700	5728	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-12-13 09:44:51.700	5728	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-12-13 09:44:51.700	5728	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-12-13 09:44:51.700	5728	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-12-13 09:44:51.700	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-12-13 09:44:51.700	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-12-13 09:44:51.700	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-12-13 09:44:51.700	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-12-13 09:44:51.700	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-12-13 09:44:51.716	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-12-13 09:44:51.716	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-12-13 09:44:51.716	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-12-13 09:44:51.716	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-12-13 09:44:51.716	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-12-13 09:44:51.716	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-12-13 09:44:51.716	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-12-13 09:44:51.716	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-12-13 09:44:51.716	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-12-13 09:44:51.732	5728	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-12-13 09:44:51.732	5728	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-12-13 09:44:51.732	5728	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-12-13 09:44:51.732	5728	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-13 09:44:51.732	5728	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-12-13 09:44:51.732	5728	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:44:51.747	5728	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:44:51.747	5728	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-12-13 09:44:51.747	5728	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-13 09:44:51.747	5728	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-12-13 09:44:51.747	5728	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:44:51.747	5728	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:44:51.747	5728	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-12-13 09:44:51.778	5728	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-12-13 09:44:51.794	5728	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-12-13 09:44:51.794	5728	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-13 09:44:51.794	5728	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-13 09:44:51.810	5728	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-12-13 09:44:51.810	5728	INFO 	net.p2p	src/p2p/net_node.inl:577	[1;32mNet service bound to 0.0.0.0:18080[0m
2017-12-13 09:44:51.825	5728	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-12-13 09:44:54.017	5728	WARN 	net.p2p	src/p2p/net_node.inl:615	UPnP device was found but not recognized as IGD.
2017-12-13 09:44:54.017	5728	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-13 09:44:54.017	5728	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-13 09:44:54.017	5728	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-12-13 09:44:54.032	5728	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-13 09:44:54.032	5728	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-13 09:44:54.032	5728	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-13 09:44:54.032	5728	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-12-13 09:44:54.032	5728	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-13 09:44:54.032	5728	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-13 09:44:54.048	5728	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1070	BlockchainLMDB::BlockchainLMDB
2017-12-13 09:44:54.048	5728	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1388	BlockchainLMDB::get_db_name
2017-12-13 09:44:54.048	5728	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-12-13 09:44:54.048	5728	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-12-13 09:44:54.048	5728	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-12-13 09:44:54.063	5728	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-12-13 09:44:54.063	5728	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1091	BlockchainLMDB::open
2017-12-13 09:44:54.079	5728	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-12-13 09:44:54.095	5728	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     36676089856
2017-12-13 09:44:54.095	5728	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      28924506112
2017-12-13 09:44:54.095	5728	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 7751583744
2017-12-13 09:44:54.095	5728	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-12-13 09:44:54.110	5728	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.7886  Percent threshold: 0.8000
2017-12-13 09:44:54.110	5728	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 1398908
2017-12-13 09:48:20.413	13652	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-12-13 09:48:20.413	13652	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:TRACE
2017-12-13 09:48:20.429	13652	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-13 09:48:20.429	13652	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-12-13 09:48:20.429	13652	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-13 09:48:20.429	13652	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-13 09:48:20.429	13652	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:136	Blockchain::Blockchain
2017-12-13 09:48:20.429	13652	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-13 09:48:20.429	13652	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-12-13 09:48:20.429	1568	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-12-13 09:48:20.429	13360	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-12-13 09:48:20.429	2664	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-12-13 09:48:20.429	14024	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-12-13 09:48:26.323	13360	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-12-13 09:48:26.323	13360	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-12-13 09:48:26.338	14024	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-12-13 09:48:26.338	14024	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-12-13 09:48:28.823	1568	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-12-13 09:48:28.823	1568	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-12-13 09:48:28.839	2664	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-12-13 09:48:28.839	2664	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-12-13 09:48:28.839	13652	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-12-13 09:48:28.839	13652	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-12-13 09:48:28.854	13652	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-12-13 09:48:28.854	13652	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-12-13 09:48:28.854	13652	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-12-13 09:48:28.854	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-12-13 09:48:28.870	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-12-13 09:48:28.870	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-12-13 09:48:28.870	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-12-13 09:48:28.870	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-12-13 09:48:28.870	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-12-13 09:48:28.870	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-12-13 09:48:28.870	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-12-13 09:48:28.886	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-12-13 09:48:28.886	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-12-13 09:48:28.886	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-12-13 09:48:28.886	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-12-13 09:48:28.886	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-12-13 09:48:28.886	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-12-13 09:48:28.886	13652	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-12-13 09:48:28.886	13652	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-12-13 09:48:28.886	13652	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-12-13 09:48:28.901	13652	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-13 09:48:28.901	13652	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-12-13 09:48:28.901	13652	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:48:28.901	13652	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:48:28.901	13652	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-12-13 09:48:28.901	13652	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-13 09:48:28.901	13652	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-12-13 09:48:28.901	13652	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:48:28.901	13652	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-13 09:48:28.901	13652	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-12-13 09:48:28.933	13652	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-12-13 09:48:28.933	13652	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-12-13 09:48:28.933	13652	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-13 09:48:28.933	13652	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-13 09:48:28.933	13652	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-12-13 09:48:28.933	13652	INFO 	net.p2p	src/p2p/net_node.inl:577	[1;32mNet service bound to 0.0.0.0:18080[0m
2017-12-13 09:48:28.933	13652	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-12-13 09:48:31.064	13652	WARN 	net.p2p	src/p2p/net_node.inl:615	UPnP device was found but not recognized as IGD.
2017-12-13 09:48:31.064	13652	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-13 09:48:31.064	13652	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-13 09:48:31.064	13652	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-12-13 09:48:31.080	13652	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-13 09:48:31.080	13652	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-13 09:48:31.080	13652	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-13 09:48:31.096	13652	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-12-13 09:48:31.096	13652	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-13 09:48:31.096	13652	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-13 09:48:31.096	13652	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1070	BlockchainLMDB::BlockchainLMDB
2017-12-13 09:48:31.096	13652	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1388	BlockchainLMDB::get_db_name
2017-12-13 09:48:31.096	13652	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-12-13 09:48:31.096	13652	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-12-13 09:48:31.111	13652	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-12-13 09:48:31.111	13652	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-12-13 09:48:31.111	13652	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1091	BlockchainLMDB::open
2017-12-13 09:48:31.127	13652	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-12-13 09:48:31.127	13652	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     36676089856
2017-12-13 09:48:31.127	13652	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      28924506112
2017-12-13 09:48:31.127	13652	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 7751583744
2017-12-13 09:48:31.127	13652	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-12-13 09:48:31.127	13652	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.7886  Percent threshold: 0.8000
2017-12-13 09:48:31.142	13652	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 1398908

# Discussion History
## cavac | 2017-12-14T09:02:30+00:00
Same thing happens on Linux with monerod. I compiled this one myself from Github sources a couple of days ago.

Output:
`monero src/blockchain_db/lmdb/db_lmdb.cpp:580 [batch] DB resize needed
Segmentation fault (core dumped)`

Using Xubuntu 16.04 x64

## d4m4ri | 2017-12-16T21:00:56+00:00
Same on MAC (via Docker / Ubuntu (20G/8G RAM), assume its GIT HEAD.

Output:
2017-12-16 20:26:57.934	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1151	[198.16.155.84:18080 OUT]  Synced 186328/1466240
2017-12-16 20:26:59.987	[P2P6]	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:580	[batch] DB resize needed
user@puter ~/monero (master) $

## moneromooo-monero | 2017-12-23T17:17:26+00:00
Please post a stack trace of that crash. You might need to run "ulimit -c unlimited" and "echo core | sudo tee /proc/sys/kernel/core_pattern" first in order for a core to be generated.

## moneromooo-monero | 2017-12-26T11:17:26+00:00
Could be the same:
```
Thread 1 (Thread 0x40556c0 (LWP 1328)):
#0  0x0000000006e68765 in mdb_env_pick_meta (env=0x1155d380) at /home/user/src/bitmonero/external/db_drivers/liblmdb/mdb.c:4147
#1  0x0000000006e657f4 in mdb_env_sync (env=0x1155d380, force=1) at /home/user/src/bitmonero/external/db_drivers/liblmdb/mdb.c:2705
---Type <return> to continue, or q <return> to quit---
#2  0x0000000005b9a78e in cryptonote::BlockchainLMDB::sync (this=0x1152d220)
    at /home/user/src/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:1336
#3  0x0000000005b937ea in cryptonote::BlockchainLMDB::close (this=0x1152d220)
    at /home/user/src/bitmonero/src/blockchain_db/lmdb/db_lmdb.cpp:1321
#4  0x0000000004e8c440 in cryptonote::Blockchain::deinit (this=this@entry=0xffeffddb8)
    at /home/user/src/bitmonero/src/cryptonote_core/blockchain.cpp:480
#5  0x0000000004ec9e23 in cryptonote::core::deinit (this=this@entry=0xffeffdcc0)
    at /home/user/src/bitmonero/src/cryptonote_core/cryptonote_core.cpp:528
#6  0x00000000006b35b2 in do_replay_events<gen_chain_switch_1> (events=std::vector of length 146, capacity 256 = {...})
    at /home/user/src/bitmonero/tests/core_tests/chaingen.h:488
#7  0x0000000000565355 in main (argc=<optimized out>, argv=<optimized out>)
    at /home/user/src/bitmonero/tests/core_tests/chaingen_main.cpp:97
(gdb) li
4142	 */
4143	static MDB_meta *
4144	mdb_env_pick_meta(const MDB_env *env)
4145	{
4146		MDB_meta *const *metas = env->me_metas;
4147		return metas[ (metas[0]->mm_txnid < metas[1]->mm_txnid) ^
4148			((env->me_flags & MDB_PREVSNAPSHOT) != 0) ];
4149	}
4150	
4151	int ESECT
(gdb) print *env
$7 = {me_fd = 5, me_lfd = 4, me_mfd = 6, me_flags = 813760512, me_psize = 4096, me_os_psize = 4096, me_maxreaders = 126, 
  me_close_readers = 1, me_numdbs = 16, me_maxdbs = 22, me_pid = 1328, me_path = 0x1155d580 "/home/user/.bitmonero/fake/lmdb", 
  me_map = 0x0, me_txns = 0x402a000, me_metas = {0x395fe010, 0x395ff010}, me_pbuf = 0x115591d0, me_txn = 0x0, me_txn0 = 0x1155a210, 
  me_mapsize = 34359738368, me_size = 0, me_maxpg = 8126464, me_dbxs = 0x1155c050, me_dbflags = 0x1155c4b0, me_dbiseqs = 0x1155c520, 
  me_txkey = 1, me_pgoldest = 438, me_pgstate = {mf_pghead = 0x0, mf_pglast = 0}, me_dpages = 0x1162a230, me_free_pgs = 0x1227d048, 
  me_dirty_list = 0x11ef4160, me_maxfree_1pg = 509, me_nodemax = 2038, me_live_reader = 1, me_userctx = 0x0, me_assert_func = 0x0}
(gdb) print *env->me_metas 
$8 = (MDB_meta *) 0x395fe010
(gdb) print env->me_metas[0]->mm_txnid 
Cannot access memory at address 0x395fe090
```
This was while running core tests with valgrind, and I got:
```
2017-12-26 11:05:56.226	         40556c0	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:582	[batch] DB resize needed
==1328== Warning: set address range perms: large range [0x395fe000, 0x7f95fe000) (noaccess)
2017-12-26 11:05:56.237	         40556c0	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to set new mapsize: Invalid argument
2017-12-26 11:05:56.277	         40556c0	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:393	Failed to remove tx from txpool: Failed to set new mapsize: Invalid argument
2017-12-26 11:05:56.298	         40556c0	ERROR	verify	src/cryptonote_core/blockchain.cpp:3355	Block with id: <1850e020bf815f6244ac188fa16c712d21a8ca3cf9a0b08aa827e44d4dab56d5> has at least one unknown transaction with id: <e2a34eb76619fd820124d992b01c58edeebf48bd0def134aa634cab9823ccae8>
2017-12-26 11:05:56.341	         40556c0	ERROR	tests.core	tests/core_tests/chaingen.h:437	Exception at [replay_events_through_core], what=Block verification failed
2017-12-26 11:05:56.345	         40556c0	DEBUG	miner	src/cryptonote_basic/miner.cpp:354	Not mining - nothing to stop
==1328== Invalid read of size 8
==1328==    at 0x6E68765: mdb_env_pick_meta (mdb.c:4147)
==1328==    by 0x6E657F3: mdb_env_sync (mdb.c:2705)
==1328==    by 0x5B9A78D: cryptonote::BlockchainLMDB::sync() (db_lmdb.cpp:1336)
==1328==    by 0x5B937E9: cryptonote::BlockchainLMDB::close() (db_lmdb.cpp:1321)
==1328==    by 0x4E8C43F: cryptonote::Blockchain::deinit() (blockchain.cpp:480)
==1328==    by 0x4EC9E22: cryptonote::core::deinit() (cryptonote_core.cpp:528)
==1328==    by 0x6B35B1: bool do_replay_events<gen_chain_switch_1>(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings>, std::allocator<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> > >&) (chaingen.h:488)
==1328==    by 0x565354: main (chaingen_main.cpp:97)
==1328==  Address 0x395fe090 is not stack'd, malloc'd or (recently) free'd
==1328== 
==1328== 
==1328== Process terminating with default action of signal 11 (SIGSEGV): dumping core
==1328==  Access not within mapped region at address 0x395FE090
==1328==    at 0x6E68765: mdb_env_pick_meta (mdb.c:4147)
==1328==    by 0x6E657F3: mdb_env_sync (mdb.c:2705)
==1328==    by 0x5B9A78D: cryptonote::BlockchainLMDB::sync() (db_lmdb.cpp:1336)
==1328==    by 0x5B937E9: cryptonote::BlockchainLMDB::close() (db_lmdb.cpp:1321)
==1328==    by 0x4E8C43F: cryptonote::Blockchain::deinit() (blockchain.cpp:480)
==1328==    by 0x4EC9E22: cryptonote::core::deinit() (cryptonote_core.cpp:528)
==1328==    by 0x6B35B1: bool do_replay_events<gen_chain_switch_1>(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings>, std::allocator<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> > >&) (chaingen.h:488)
==1328==    by 0x565354: main (chaingen_main.cpp:97)
==1328==  If you believe this happened as a result of a stack
==1328==  overflow in your program's main thread (unlikely but
==1328==  possible), you can try to increase the size of the
==1328==  main thread stack using the --main-stacksize= flag.
==1328==  The main thread stack size used in this run was 8388608.
```
Note the "invalid argument" in the log.


## hyc | 2017-12-27T21:10:43+00:00
No, the EINVAL is because by default valgrind doesn't support such a large mmap. I've forgotten the constant you need to redefine for this, but you have to recompile valgrind yourself before it will work. This is a valgrind issue not an LMDB bug.

## moneromooo-monero | 2017-12-27T21:21:04+00:00
OK, I'm not 100% convinced because (1) the valgrind message above seems unrelated and appeared several times before without an EINVAL, (2) the resize func does set EINVAL if there's a txn active at the time, and (3) this is done with the fake testing DB, which is like half a GB only. But I'll try without valgrind tomorrow to see if I can still repro it.

## moneromooo-monero | 2017-12-28T17:59:50+00:00
More info (inlcuding traces) in https://github.com/monero-project/monero/pull/3019

## moneromooo-monero | 2018-01-04T13:17:45+00:00
Fixed by #3019 

+resolved

# Action History
- Created by: saxenadev | 2017-12-13T10:04:45+00:00
- Closed at: 2018-01-04T13:24:28+00:00
