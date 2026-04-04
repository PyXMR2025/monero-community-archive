---
title: '[node] Stop signal sent'
source_url: https://github.com/monero-project/monero/issues/2508
author: calvintam236
assignees: []
labels: []
created_at: '2017-09-22T06:37:43+00:00'
updated_at: '2017-10-20T18:50:00+00:00'
type: issue
status: closed
closed_at: '2017-10-20T18:49:59+00:00'
---

# Original Description
I ran `monerod --data-dir /monerod --log-level 3`, and it won't start. Getting `[node] Stop signal sent`. Port 18080 is open, and forwarded to the host.

```console
2017-09-22 06:31:17.884	    7fa4eefc0740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-09-22 06:31:17.885	    7fa4eefc0740	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-09-22 06:31:17.885	    7fa4eefc0740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-09-22 06:31:17.885	    7fa4eefc0740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-09-22 06:31:17.887	    7fa4eefc0740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:136	Blockchain::Blockchain
2017-09-22 06:31:17.890	    7fa4eefc0740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-09-22 06:31:17.890	    7fa4eddad700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-09-22 06:31:17.891	    7fa4ed5ac700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-09-22 06:31:17.892	    7fa4ecdab700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-09-22 06:31:17.892	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
[1506061877] libunbound[1:0] info: warning: unsupported algorithm for trust anchor . DS IN
[1506061877] libunbound[1:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)
2017-09-22 06:31:17.893	    7fa4dffff700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-09-22 06:31:17.901	    7fa4ed5ac700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-09-22 06:31:17.901	    7fa4ed5ac700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-09-22 06:31:17.901	    7fa4eddad700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-09-22 06:31:17.902	    7fa4eddad700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-09-22 06:31:17.904	    7fa4dffff700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-09-22 06:31:17.904	    7fa4dffff700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-09-22 06:31:17.907	    7fa4ecdab700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-09-22 06:31:17.907	    7fa4ecdab700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-09-22 06:31:17.907	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-09-22 06:31:17.907	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-09-22 06:31:17.908	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-09-22 06:31:17.908	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-09-22 06:31:17.908	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-09-22 06:31:17.908	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-09-22 06:31:17.909	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-09-22 06:31:17.910	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-09-22 06:31:17.910	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-09-22 06:31:17.910	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-09-22 06:31:17.910	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-09-22 06:31:17.911	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-09-22 06:31:17.911	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-09-22 06:31:17.911	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-09-22 06:31:17.911	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-09-22 06:31:17.911	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-09-22 06:31:17.911	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-09-22 06:31:17.911	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-09-22 06:31:17.911	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-09-22 06:31:17.915	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-09-22 06:31:17.915	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-09-22 06:31:17.915	    7fa4eefc0740	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-09-22 06:31:17.916	    7fa4eefc0740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-09-22 06:31:17.917	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-09-22 06:31:17.917	    7fa4eefc0740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-22 06:31:17.917	    7fa4eefc0740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-22 06:31:17.917	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-09-22 06:31:17.918	    7fa4eefc0740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-09-22 06:31:17.918	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-09-22 06:31:17.918	    7fa4eefc0740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-22 06:31:17.918	    7fa4eefc0740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-22 06:31:17.918	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-09-22 06:31:17.918	    7fa4eefc0740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-09-22 06:31:17.919	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-09-22 06:31:17.919	    7fa4eefc0740	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-09-22 06:31:17.919	    7fa4eefc0740	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-09-22 06:31:17.919	    7fa4eefc0740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-09-22 06:31:17.919	    7fa4eefc0740	INFO 	net.p2p	src/p2p/net_node.inl:577	Net service bound to 0.0.0.0:18080
2017-09-22 06:31:17.919	    7fa4eefc0740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-09-22 06:31:17.920	    7fa4eefc0740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-09-22 06:31:17.920	    7fa4eefc0740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-09-22 06:31:17.920	    7fa4eefc0740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-09-22 06:31:17.920	    7fa4eefc0740	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-09-22 06:31:17.920	    7fa4eefc0740	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-09-22 06:31:17.920	    7fa4eefc0740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-09-22 06:31:17.920	    7fa4eefc0740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-09-22 06:31:17.920	    7fa4eefc0740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-09-22 06:31:17.921	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1070	BlockchainLMDB::BlockchainLMDB
2017-09-22 06:31:17.921	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1388	BlockchainLMDB::get_db_name
2017-09-22 06:31:17.922	    7fa4eefc0740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /monerod/lmdb ...
2017-09-22 06:31:17.922	    7fa4eefc0740	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-09-22 06:31:17.922	    7fa4eefc0740	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-09-22 06:31:17.922	    7fa4eefc0740	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-09-22 06:31:17.922	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1091	BlockchainLMDB::open
2017-09-22 06:31:17.923	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-09-22 06:31:17.923	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-09-22 06:31:17.923	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      73728
2017-09-22 06:31:17.923	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073668096
2017-09-22 06:31:17.923	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-09-22 06:31:17.924	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0001  Percent threshold: 0.8000
2017-09-22 06:31:17.924	    7fa4eefc0740	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 1
2017-09-22 06:31:17.924	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:17.924	    7fa4eefc0740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:288	Blockchain::init
2017-09-22 06:31:17.924	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.924	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-09-22 06:31:17.925	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:17.925	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3119	BlockchainLMDB::get_hard_fork_version
2017-09-22 06:31:17.925	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-09-22 06:31:17.925	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:17.925	    7fa4eefc0740	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:197	reorganizing from 1
2017-09-22 06:31:17.925	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1744	BlockchainLMDB::get_block_blob_from_height
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3119	BlockchainLMDB::get_hard_fork_version
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-09-22 06:31:17.926	    7fa4eefc0740	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:206	reorganization done
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3151	BlockchainLMDB::fixup
2017-09-22 06:31:17.926	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2671	BlockchainLMDB::set_batch_transactions
2017-09-22 06:31:17.927	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2677	batch transactions enabled
2017-09-22 06:31:17.927	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2545	BlockchainLMDB::batch_start
2017-09-22 06:31:17.927	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:553	BlockchainLMDB::check_and_resize_for_batch
2017-09-22 06:31:17.927	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	[check_and_resize_for_batch] checking DB size
2017-09-22 06:31:17.927	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-09-22 06:31:17.927	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-09-22 06:31:17.927	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      73728
2017-09-22 06:31:17.927	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073668096
2017-09-22 06:31:17.927	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-09-22 06:31:17.927	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0001  Percent threshold: 0.8000
2017-09-22 06:31:17.927	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2576	batch transaction: begin
2017-09-22 06:31:17.927	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1894	BlockchainLMDB::get_block_hash_from_height
2017-09-22 06:31:17.927	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2619	BlockchainLMDB::batch_stop
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2629	batch transaction: committing...
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2643	batch transaction: end
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1793	BlockchainLMDB::get_top_block_timestamp
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:17.928	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1770	BlockchainLMDB::get_block_timestamp
2017-09-22 06:31:17.928	    7fa4eefc0740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4137	Loading precomputed blocks (44480036 bytes)
2017-09-22 06:31:18.131	    7fa4eefc0740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4148	precomputed blocks hash: <d3ca80d50661684cde0e715d46d7c19704d2e216b21ed088af9fd4ef37ed4d65>, expected d3ca80d50661684cde0e715d46d7c19704d2e216b21ed088af9fd4ef37ed4d65
2017-09-22 06:31:18.131	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:18.201	    7fa4eefc0740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4178	1390001 block hashes loaded
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1626	BlockchainLMDB::for_all_txpool_txes
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:711	Blockchain::get_difficulty_for_next_block
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:18.201	    7fa4eefc0740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:388	Blockchain initialized. last block: 0, d1906.h1.m31.s17 time ago, current difficulty: 1
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:3441	Blockchain::update_next_cumulative_size_limit
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:1048	Blockchain::get_last_n_blocks_sizes
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1808	BlockchainLMDB::get_block_size
2017-09-22 06:31:18.201	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-09-22 06:31:18.202	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1626	BlockchainLMDB::for_all_txpool_txes
2017-09-22 06:31:18.202	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-09-22 06:31:18.202	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:18.202	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1626	BlockchainLMDB::for_all_txpool_txes
2017-09-22 06:31:18.202	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-09-22 06:31:18.202	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:18.202	    7fa4eefc0740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:421	Loading checkpoints
2017-09-22 06:31:18.202	    7fa4eefc0740	INFO 	checkpoints	src/cryptonote_basic/checkpoints.cpp:182	Blockchain checkpoints file not found
2017-09-22 06:31:26.173	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.org, skipping.
2017-09-22 06:31:26.174	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.org, skipping.
2017-09-22 06:31:58.986	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.net, skipping.
2017-09-22 06:31:58.986	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.net, skipping.
2017-09-22 06:31:58.986	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.co, skipping.
2017-09-22 06:31:58.986	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.co, skipping.
2017-09-22 06:31:58.986	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.se, skipping.
2017-09-22 06:31:58.987	    7fa4eefc0740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.se, skipping.
2017-09-22 06:31:58.987	    7fa4eefc0740	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2545	BlockchainLMDB::batch_start
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:553	BlockchainLMDB::check_and_resize_for_batch
2017-09-22 06:31:58.987	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	[check_and_resize_for_batch] checking DB size
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-09-22 06:31:58.987	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-09-22 06:31:58.987	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      73728
2017-09-22 06:31:58.987	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073668096
2017-09-22 06:31:58.987	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-09-22 06:31:58.987	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0001  Percent threshold: 0.8000
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2576	batch transaction: begin
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2619	BlockchainLMDB::batch_stop
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2629	batch transaction: committing...
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2643	batch transaction: end
2017-09-22 06:31:58.987	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2545	BlockchainLMDB::batch_start
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:553	BlockchainLMDB::check_and_resize_for_batch
2017-09-22 06:31:58.988	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	[check_and_resize_for_batch] checking DB size
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-09-22 06:31:58.988	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-09-22 06:31:58.988	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      73728
2017-09-22 06:31:58.988	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073668096
2017-09-22 06:31:58.988	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-09-22 06:31:58.988	    7fa4eefc0740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0001  Percent threshold: 0.8000
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2576	batch transaction: begin
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.988	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.989	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2619	BlockchainLMDB::batch_stop
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2629	batch transaction: committing...
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-09-22 06:31:58.990	    7fa4eefc0740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2643	batch transaction: end
2017-09-22 06:31:58.990	    7fa4eefc0740	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-09-22 06:31:58.990	    7fa4eefc0740	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-09-22 06:31:58.991	    7fa4eefc0740	INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:83	Run net_service loop( 2 threads)...
2017-09-22 06:31:58.991	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: RPC
2017-09-22 06:31:58.991	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: RPC
2017-09-22 06:31:58.991	[SRV_MAIN]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:838	Reiniting OK.
2017-09-22 06:31:58.991	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-09-22 06:31:58.992	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-09-22 06:31:58.992	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:668	Run net_service loop( 10 threads)...
2017-09-22 06:31:58.992	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.992	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.992	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.992	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.993	    7fa4deffd700	INFO 	net.p2p	src/p2p/net_node.inl:640	Thread monitor number of peers - start
2017-09-22 06:31:58.993	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.994	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.995	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.997	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.999	    7fa4df7fe700	DEBUG	net.p2p	src/p2p/net_node.inl:735	[node] Stop signal sent
2017-09-22 06:31:58.999	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.999	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: P2P
2017-09-22 06:31:58.999	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:828	JOINING all threads
2017-09-22 06:31:59.000	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:832	JOINING all threads - almost
2017-09-22 06:31:59.000	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:834	JOINING all threads - DONE
2017-09-22 06:31:59.000	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:674	net_service loop stopped.
2017-09-22 06:31:59.000	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2017-09-22 06:31:59.001	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
2017-09-22 06:31:59.002	[SRV_MAIN]	TRACE	miner	src/cryptonote_basic/miner.cpp:333	Miner has received stop signal
2017-09-22 06:31:59.003	[SRV_MAIN]	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-09-22 06:31:59.003	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:145	Node stopped.
2017-09-22 06:31:59.004	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-09-22 06:31:59.004	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:94	[sock -1] Socket destroyed without shutdown.
2017-09-22 06:31:59.004	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:98	[sock -1] Socket destroyed
2017-09-22 06:31:59.004	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-09-22 06:31:59.004	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-09-22 06:31:59.005	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
2017-09-22 06:31:59.993	    7fa4deffd700	INFO 	net.p2p	src/p2p/net_node.inl:655	Thread monitor number of peers - done
2017-09-22 06:31:59.994	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
2017-09-22 06:31:59.994	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:94	[sock -1] Socket destroyed without shutdown.
2017-09-22 06:31:59.994	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:98	[sock -1] Socket destroyed
2017-09-22 06:31:59.994	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/levin_protocol_handler_async.h:281	[0.0.0.0:0 OUT] ~async_protocol_handler()
2017-09-22 06:31:59.994	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-09-22 06:31:59.994	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-09-22 06:31:59.994	[SRV_MAIN]	TRACE	miner	src/cryptonote_basic/miner.cpp:333	Miner has received stop signal
2017-09-22 06:31:59.994	[SRV_MAIN]	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-09-22 06:31:59.994	[SRV_MAIN]	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:437	Blockchain::deinit
2017-09-22 06:31:59.995	[SRV_MAIN]	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:439	Stopping blockchain read/write activity
2017-09-22 06:31:59.995	[SRV_MAIN]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1294	BlockchainLMDB::close
2017-09-22 06:31:59.995	[SRV_MAIN]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1310	BlockchainLMDB::sync
2017-09-22 06:31:59.998	[SRV_MAIN]	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:457	Local blockchain read/write activity stopped successfully
2017-09-22 06:31:59.998	[SRV_MAIN]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1059	BlockchainLMDB::~BlockchainLMDB
2017-09-22 06:31:59.998	[SRV_MAIN]	TRACE	miner	src/cryptonote_basic/miner.cpp:333	Miner has received stop signal
2017-09-22 06:31:59.999	[SRV_MAIN]	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-09-22 06:32:00.008	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-09-22 06:32:00.008	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
```

# Discussion History
## moneromooo-monero | 2017-09-22T07:55:52+00:00
Are you using it with something like upstart or systemd ? I know you implied you did not, but better double check just in case. Otherwise, do you have write permissions to that directory ? Is monerod already running ?

## calvintam236 | 2017-09-22T17:31:34+00:00
I am not running it as a service, so not with `upstart` or `systemd`. I am sure it has write permissions, because I see `lmdb` folder, `bitmonero.log`, and `p2pstate.bin` were created by `monerod`

## moneromooo-monero | 2017-09-22T19:16:29+00:00
Then run a debug build this way:

gdb monerod
break nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::send_stop_signal
run --data-dir /monerod --log-level 3

After it's stopped in gdb:

bt

Then post the (probably multi-page) output here.


## radfish | 2017-09-24T19:32:42+00:00
Could you please also see if this also happens with `--detach`?

## calvintam236 | 2017-10-02T08:02:39+00:00
Tried. breakpoint doesn't work.

```console
GNU gdb (Debian 7.7.1+dfsg-5) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...done.
Function "nodetool::node_server<cryptonote::t_cryptonote_protocol_handlercryptonote::core>::send_stop_signal" not defined.
Breakpoint 1 (nodetool::node_server<cryptonote::t_cryptonote_protocol_handlercryptonote::core>::send_stop_signal) pending.
Starting program: /usr/local/bin/monerod --data-dir /monerod --log-level 3
warning: Error disabling address space randomization: Operation not permitted
2017-10-02 07:59:07.226	    7f2c92c94740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-02 07:59:07.233	    7f2c92c94740	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-10-02 07:59:07.233	    7f2c92c94740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-10-02 07:59:07.233	    7f2c92c94740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-10-02 07:59:07.234	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:136	Blockchain::Blockchain
2017-10-02 07:59:07.235	    7f2c92c94740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-10-02 07:59:07.236	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-10-02 07:59:07.237	    7f2c902ab700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-10-02 07:59:07.237	    7f2c90aac700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-10-02 07:59:07.237	    7f2c912ad700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
[1506931147] libunbound[7:0] info: warning: unsupported algorithm for trust anchor . DS IN
[1506931147] libunbound[7:0] warning: trust anchor . has no supported algorithms, the anchor is ignored (check if you need to upgrade unbound and openssl)
2017-10-02 07:59:07.239	    7f2c91aae700	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-10-02 07:59:07.258	    7f2c90aac700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-10-02 07:59:07.258	    7f2c90aac700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-10-02 07:59:07.259	    7f2c912ad700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-10-02 07:59:07.260	    7f2c912ad700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-10-02 07:59:07.262	    7f2c91aae700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-10-02 07:59:07.262	    7f2c91aae700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-10-02 07:59:07.264	    7f2c902ab700	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-10-02 07:59:07.264	    7f2c902ab700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-10-02 07:59:07.265	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-10-02 07:59:07.265	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-10-02 07:59:07.265	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-10-02 07:59:07.265	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-10-02 07:59:07.265	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-10-02 07:59:07.265	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-10-02 07:59:07.265	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-10-02 07:59:07.265	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-10-02 07:59:07.266	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-10-02 07:59:07.266	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-10-02 07:59:07.266	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-10-02 07:59:07.266	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-10-02 07:59:07.266	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-10-02 07:59:07.267	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-10-02 07:59:07.267	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-10-02 07:59:07.267	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-10-02 07:59:07.267	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-10-02 07:59:07.267	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-10-02 07:59:07.268	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-10-02 07:59:07.268	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-10-02 07:59:07.268	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-10-02 07:59:07.268	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-10-02 07:59:07.269	    7f2c92c94740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-10-02 07:59:07.269	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-10-02 07:59:07.269	    7f2c92c94740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-10-02 07:59:07.270	    7f2c92c94740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-10-02 07:59:07.270	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-10-02 07:59:07.270	    7f2c92c94740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-10-02 07:59:07.270	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-10-02 07:59:07.270	    7f2c92c94740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-10-02 07:59:07.270	    7f2c92c94740	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-10-02 07:59:07.271	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-10-02 07:59:07.272	    7f2c92c94740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-10-02 07:59:07.272	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-10-02 07:59:07.283	    7f2c92c94740	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-10-02 07:59:07.283	    7f2c92c94740	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-10-02 07:59:07.283	    7f2c92c94740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-10-02 07:59:07.283	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:577	Net service bound to 0.0.0.0:18080
2017-10-02 07:59:07.283	    7f2c92c94740	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-10-02 07:59:11.293	    7f2c92c94740	INFO 	net.p2p	src/p2p/net_node.inl:622	No IGD was found.
2017-10-02 07:59:11.293	    7f2c92c94740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-10-02 07:59:11.293	    7f2c92c94740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-10-02 07:59:11.293	    7f2c92c94740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-10-02 07:59:11.293	    7f2c92c94740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-10-02 07:59:11.294	    7f2c92c94740	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-10-02 07:59:11.294	    7f2c92c94740	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-10-02 07:59:11.294	    7f2c92c94740	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-10-02 07:59:11.294	    7f2c92c94740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-10-02 07:59:11.294	    7f2c92c94740	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-10-02 07:59:11.295	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1070	BlockchainLMDB::BlockchainLMDB
2017-10-02 07:59:11.296	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1388	BlockchainLMDB::get_db_name
2017-10-02 07:59:11.296	    7f2c92c94740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /monerod/lmdb ...
2017-10-02 07:59:11.296	    7f2c92c94740	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-10-02 07:59:11.296	    7f2c92c94740	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-10-02 07:59:11.296	    7f2c92c94740	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-10-02 07:59:11.296	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1091	BlockchainLMDB::open
2017-10-02 07:59:11.297	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1150	LMDB memory map size: 1073741824
2017-10-02 07:59:11.297	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-10-02 07:59:11.297	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-10-02 07:59:11.297	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      4096
2017-10-02 07:59:11.297	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073737728
2017-10-02 07:59:11.297	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-10-02 07:59:11.298	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0000  Percent threshold: 0.8000
2017-10-02 07:59:11.298	    7f2c92c94740	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 0
2017-10-02 07:59:11.299	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.299	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:288	Blockchain::init
2017-10-02 07:59:11.299	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.299	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.299	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.300	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3119	BlockchainLMDB::get_hard_fork_version
2017-10-02 07:59:11.300	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.300	    7f2c92c94740	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-10-02 07:59:11.305	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.314	    7f2c92c94740	INFO 	hardfork	src/cryptonote_basic/hardfork.cpp:194	The DB has no hard fork info, reparsing from start
2017-10-02 07:59:11.314	    7f2c92c94740	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:197	reorganizing from 1
2017-10-02 07:59:11.314	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.314	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.314	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.314	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3100	BlockchainLMDB::set_hard_fork_version
2017-10-02 07:59:11.314	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.315	    7f2c92c94740	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:206	reorganization done
2017-10-02 07:59:11.315	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.315	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.315	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.315	    7f2c92c94740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:342	Blockchain not loaded, generating genesis block.
2017-10-02 07:59:11.392	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:3455	Blockchain::add_new_block
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:2118	Blockchain::have_block
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1675	BlockchainLMDB::block_exists
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1686	Block with hash 418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3 not found in db
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:563	Blockchain::get_tail_id
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1945	BlockchainLMDB::top_block_hash
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-10-02 07:59:11.393	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:3100	Blockchain::handle_block_to_main_chain
2017-10-02 07:59:11.394	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-10-02 07:59:11.394	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:563	Blockchain::get_tail_id
2017-10-02 07:59:11.395	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1945	BlockchainLMDB::top_block_hash
2017-10-02 07:59:11.395	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.395	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:3030	Blockchain::check_block_timestamp
2017-10-02 07:59:11.395	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:3001	Blockchain::get_adjusted_time
2017-10-02 07:59:11.395	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.396	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:711	Blockchain::get_difficulty_for_next_block
2017-10-02 07:59:11.396	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.396	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.396	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.462	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:279	Blockchain::get_current_blockchain_height
2017-10-02 07:59:11.462	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.462	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:279	Blockchain::get_current_blockchain_height
2017-10-02 07:59:11.462	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.462	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.462	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:968	Blockchain::prevalidate_miner_transaction
2017-10-02 07:59:11.463	    7f2c92c94740	DEBUG	blockchain	src/cryptonote_core/blockchain.cpp:976	Miner tx hash: <c88ce9783b4f11190d7b9c17a69c1c52200f9faaee8e98dd07e6811175177139>
2017-10-02 07:59:11.463	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.463	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:995	Blockchain::validate_miner_transaction
2017-10-02 07:59:11.464	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:1048	Blockchain::get_last_n_blocks_sizes
2017-10-02 07:59:11.464	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.464	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.465	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-10-02 07:59:11.465	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2828	BlockchainLMDB::add_block
2017-10-02 07:59:11.465	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.465	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.465	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.466	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-10-02 07:59:11.466	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-10-02 07:59:11.466	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      24576
2017-10-02 07:59:11.466	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073717248
2017-10-02 07:59:11.467	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-10-02 07:59:11.467	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0000  Percent threshold: 0.8000
2017-10-02 07:59:11.467	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2749	BlockchainLMDB::block_txn_start
2017-10-02 07:59:11.467	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.468	    7f2c92c94740	TRACE	blockchain.db	src/blockchain_db/blockchain_db.cpp:107	null tx_hash_ptr - needed to compute: <c88ce9783b4f11190d7b9c17a69c1c52200f9faaee8e98dd07e6811175177139>
2017-10-02 07:59:11.468	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:753	BlockchainLMDB::add_transaction_data
2017-10-02 07:59:11.469	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.469	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2126	BlockchainLMDB::get_tx_count
2017-10-02 07:59:11.469	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:847	BlockchainLMDB::add_output
2017-10-02 07:59:11.469	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.469	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1987	BlockchainLMDB::num_outputs
2017-10-02 07:59:11.469	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:910	BlockchainLMDB::add_tx_amount_output_indices
2017-10-02 07:59:11.470	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:652	BlockchainLMDB::add_block
2017-10-02 07:59:11.470	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.470	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3100	BlockchainLMDB::set_hard_fork_version
2017-10-02 07:59:11.470	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.470	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-10-02 07:59:11.471	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.471	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:3441	Blockchain::update_next_cumulative_size_limit
2017-10-02 07:59:11.471	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:1048	Blockchain::get_last_n_blocks_sizes
2017-10-02 07:59:11.472	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.472	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.472	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.472	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-10-02 07:59:11.472	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1808	BlockchainLMDB::get_block_size
2017-10-02 07:59:11.473	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-10-02 07:59:11.473	    7f2c92c94740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:3418	+++++ BLOCK SUCCESSFULLY ADDED
id:	<418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3>
PoW:	<8a7b1a780e99eec31a9425b7d89c283421b2042a337d5700dfd4a7d6eb7bd774>
HEIGHT 0, difficulty:	1
block reward: 17.592186044415(17.592186044415 + 0.000000000000), coinbase_blob_size: 80, cumulative size: 80, 71(1/66)ms
2017-10-02 07:59:11.473	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:3151	BlockchainLMDB::fixup
2017-10-02 07:59:11.473	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2671	BlockchainLMDB::set_batch_transactions
2017-10-02 07:59:11.473	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2677	batch transactions enabled
2017-10-02 07:59:11.474	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2545	BlockchainLMDB::batch_start
2017-10-02 07:59:11.474	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:553	BlockchainLMDB::check_and_resize_for_batch
2017-10-02 07:59:11.475	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	[check_and_resize_for_batch] checking DB size
2017-10-02 07:59:11.475	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-10-02 07:59:11.475	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-10-02 07:59:11.476	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      69632
2017-10-02 07:59:11.476	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073672192
2017-10-02 07:59:11.477	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-10-02 07:59:11.477	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0001  Percent threshold: 0.8000
2017-10-02 07:59:11.477	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2576	batch transaction: begin
2017-10-02 07:59:11.477	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1894	BlockchainLMDB::get_block_hash_from_height
2017-10-02 07:59:11.477	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.477	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.478	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2619	BlockchainLMDB::batch_stop
2017-10-02 07:59:11.479	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2629	batch transaction: committing...
2017-10-02 07:59:11.479	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.479	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2643	batch transaction: end
2017-10-02 07:59:11.479	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-10-02 07:59:11.480	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1793	BlockchainLMDB::get_top_block_timestamp
2017-10-02 07:59:11.480	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.480	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1770	BlockchainLMDB::get_block_timestamp
2017-10-02 07:59:11.481	    7f2c92c94740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4137	Loading precomputed blocks (44480036 bytes)
2017-10-02 07:59:11.679	    7f2c92c94740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4148	precomputed blocks hash: <d3ca80d50661684cde0e715d46d7c19704d2e216b21ed088af9fd4ef37ed4d65>, expected d3ca80d50661684cde0e715d46d7c19704d2e216b21ed088af9fd4ef37ed4d65
2017-10-02 07:59:11.694	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.834	    7f2c92c94740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4178	1390001 block hashes loaded
2017-10-02 07:59:11.843	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1626	BlockchainLMDB::for_all_txpool_txes
2017-10-02 07:59:11.843	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:711	Blockchain::get_difficulty_for_next_block
2017-10-02 07:59:11.843	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.843	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.844	    7f2c92c94740	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:388	Blockchain initialized. last block: 0, d1916.h2.m59.s11 time ago, current difficulty: 1
2017-10-02 07:59:11.844	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-10-02 07:59:11.847	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:3441	Blockchain::update_next_cumulative_size_limit
2017-10-02 07:59:11.847	    7f2c92c94740	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:1048	Blockchain::get_last_n_blocks_sizes
2017-10-02 07:59:11.848	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:11.848	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.849	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.849	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2744	BlockchainLMDB::block_txn_start RO
2017-10-02 07:59:11.849	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1808	BlockchainLMDB::get_block_size
2017-10-02 07:59:11.849	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2776	BlockchainLMDB::block_txn_stop
2017-10-02 07:59:11.850	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1626	BlockchainLMDB::for_all_txpool_txes
2017-10-02 07:59:11.850	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.850	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.851	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1626	BlockchainLMDB::for_all_txpool_txes
2017-10-02 07:59:11.851	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2709	BlockchainLMDB::block_rtxn_start
2017-10-02 07:59:11.851	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:11.852	    7f2c92c94740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:421	Loading checkpoints
2017-10-02 07:59:11.852	    7f2c92c94740	INFO 	checkpoints	src/cryptonote_basic/checkpoints.cpp:182	Blockchain checkpoints file not found
2017-10-02 07:59:20.424	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.se, skipping.
2017-10-02 07:59:20.425	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.se, skipping.
2017-10-02 07:59:55.783	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.org, skipping.
2017-10-02 07:59:55.785	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.org, skipping.
2017-10-02 07:59:55.786	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.net, skipping.
2017-10-02 07:59:55.786	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.net, skipping.
2017-10-02 07:59:55.788	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.co, skipping.
2017-10-02 07:59:55.789	    7f2c92c94740	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.co, skipping.
2017-10-02 07:59:55.789	    7f2c92c94740	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-10-02 07:59:55.790	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2545	BlockchainLMDB::batch_start
2017-10-02 07:59:55.790	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:553	BlockchainLMDB::check_and_resize_for_batch
2017-10-02 07:59:55.790	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	[check_and_resize_for_batch] checking DB size
2017-10-02 07:59:55.791	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      69632
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073672192
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0001  Percent threshold: 0.8000
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2576	batch transaction: begin
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2619	BlockchainLMDB::batch_stop
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2629	batch transaction: committing...
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2643	batch transaction: end
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2545	BlockchainLMDB::batch_start
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:553	BlockchainLMDB::check_and_resize_for_batch
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:554	[check_and_resize_for_batch] checking DB size
2017-10-02 07:59:55.798	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:502	BlockchainLMDB::need_resize
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     1073741824
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      69632
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 1073672192
2017-10-02 07:59:55.798	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-10-02 07:59:55.799	    7f2c92c94740	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.0001  Percent threshold: 0.8000
2017-10-02 07:59:55.800	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2576	batch transaction: begin
2017-10-02 07:59:55.800	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.800	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.800	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.800	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.801	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.804	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.804	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.805	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.805	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.806	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.806	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.806	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.806	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.808	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.809	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.809	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.809	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.810	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.810	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.811	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.811	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.812	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.817	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.824	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.825	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1973	BlockchainLMDB::height
2017-10-02 07:59:55.825	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2619	BlockchainLMDB::batch_stop
2017-10-02 07:59:55.830	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2629	batch transaction: committing...
2017-10-02 07:59:55.830	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:312	mdb_txn_safe: destructor
2017-10-02 07:59:55.832	    7f2c92c94740	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2643	batch transaction: end
2017-10-02 07:59:55.833	    7f2c92c94740	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-10-02 07:59:55.834	    7f2c92c94740	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-10-02 07:59:55.834	    7f2c92c94740	INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:83	Run net_service loop( 2 threads)...
2017-10-02 07:59:55.836	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: RPC
2017-10-02 07:59:55.836	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:821	Run server thread name: RPC
2017-10-02 07:59:55.837	[SRV_MAIN]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:838	Reiniting OK.
2017-10-02 07:59:55.837	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-10-02 07:59:55.839	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-10-02 07:59:55.842	    7f2c8f492700	DEBUG	net.p2p	src/p2p/net_node.inl:735	[node] Stop signal sent
2017-10-02 07:59:55.843	    7f2c8ec91700	INFO 	net.p2p	src/p2p/net_node.inl:640	Thread monitor number of peers - start
2017-10-02 07:59:55.844	    7f2c8ec91700	INFO 	net.p2p	src/p2p/net_node.inl:655	Thread monitor number of peers - done
2017-10-02 07:59:55.847	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:668	Run net_service loop( 10 threads)...
2017-10-02 07:59:55.848	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:674	net_service loop stopped.
2017-10-02 07:59:55.848	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2017-10-02 07:59:55.848	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
2017-10-02 07:59:55.851	[SRV_MAIN]	TRACE	miner	src/cryptonote_basic/miner.cpp:333	Miner has received stop signal
2017-10-02 07:59:55.852	[SRV_MAIN]	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-10-02 07:59:55.852	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:145	Node stopped.
2017-10-02 07:59:55.861	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-10-02 07:59:55.862	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:94	[sock -1] Socket destroyed without shutdown.
2017-10-02 07:59:55.864	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:98	[sock -1] Socket destroyed
2017-10-02 07:59:55.867	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-10-02 07:59:55.875	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-10-02 07:59:55.876	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
2017-10-02 07:59:55.876	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
2017-10-02 07:59:55.877	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:94	[sock -1] Socket destroyed without shutdown.
2017-10-02 07:59:55.877	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:98	[sock -1] Socket destroyed
2017-10-02 07:59:55.879	[SRV_MAIN]	TRACE	net	contrib/epee/include/net/levin_protocol_handler_async.h:281	[0.0.0.0:0 OUT] ~async_protocol_handler()
2017-10-02 07:59:55.880	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-10-02 07:59:55.881	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-10-02 07:59:55.881	[SRV_MAIN]	TRACE	miner	src/cryptonote_basic/miner.cpp:333	Miner has received stop signal
2017-10-02 07:59:55.886	[SRV_MAIN]	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-10-02 07:59:55.887	[SRV_MAIN]	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:437	Blockchain::deinit
2017-10-02 07:59:55.887	[SRV_MAIN]	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:439	Stopping blockchain read/write activity
2017-10-02 07:59:55.888	[SRV_MAIN]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1294	BlockchainLMDB::close
2017-10-02 07:59:55.888	[SRV_MAIN]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1310	BlockchainLMDB::sync
2017-10-02 07:59:55.889	[SRV_MAIN]	TRACE	blockchain	src/cryptonote_core/blockchain.cpp:457	Local blockchain read/write activity stopped successfully
2017-10-02 07:59:55.889	[SRV_MAIN]	TRACE	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1059	BlockchainLMDB::~BlockchainLMDB
2017-10-02 07:59:55.892	[SRV_MAIN]	TRACE	miner	src/cryptonote_basic/miner.cpp:333	Miner has received stop signal
2017-10-02 07:59:55.892	[SRV_MAIN]	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-10-02 07:59:55.949	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-10-02 07:59:55.952	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
During startup program exited with code 1.
No stack.
```

## moneromooo-monero | 2017-10-02T13:56:33+00:00
If you can build your own monerod, then add this line as the first one in bool node_server<t_payload_net_handler>::send_stop_signal(), in src/p2p/net_node.inl:

try { throw "sending stop signal"; } catch(...){}

and try again. And make sure you're building with libunwind enabled (need libunwind header files).

## moneromooo-monero | 2017-10-15T13:30:23+00:00
ping

## calvintam236 | 2017-10-15T16:17:02+00:00
@moneromooo-monero I have a trouble compiling it on Raspberry Pi 3 model B, so please bear with me after. (ARMv7 and ARMv8 binary doesn't work as it is on ARMv7l)

Maybe the whole is caused by missing `--non-interactive` in args when running it inside `docker run -ti debian:stretch-slim`. I have to confirm that later after a successful compile.

## hyc | 2017-10-15T16:33:33+00:00
ARMv7 binaries should work fine on Pi 3. Compiling for ARMv8 requires you to disable AES support since Pi 3 CPU doesn't implement AES instructions.

## calvintam236 | 2017-10-20T18:49:59+00:00
@hyc sadly, neither armv7 or amrv8 versions works on pi. After several failure (OS kernel crashed..), I got a successful build. :) it looks fine now.

```console
root@35a9d24e73dd:~# ./linuxarm7
bash: ./linuxarm7: cannot execute binary file: Exec format error
root@35a9d24e73dd:~# ./linuxarm8
bash: ./linuxarm8: cannot execute binary file: Exec format error
root@35a9d24e73dd:~# uname -m
armv7l
```

# Action History
- Created by: calvintam236 | 2017-09-22T06:37:43+00:00
- Closed at: 2017-10-20T18:49:59+00:00
