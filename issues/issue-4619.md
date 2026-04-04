---
title: monero testnet can not run in backend
source_url: https://github.com/monero-project/monero/issues/4619
author: DinoStray
assignees: []
labels:
- invalid
created_at: '2018-10-16T14:04:48+00:00'
updated_at: '2018-10-16T14:33:06+00:00'
type: issue
status: closed
closed_at: '2018-10-16T14:33:06+00:00'
---

# Original Description
While I run:
monerod --testnet 
or
monerod
or
nohup monerod &
everything is OK.

But, while I run:
nohup monerod --testnet  &
the monerod exit with error.

error log:
2018-10-16 13:37:33,081 INFO  [default] Page size: 4096
[36m2018-10-16 13:37:34.084	    7f3deb2dc780	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.2-77ef8c1)
[0m[36m2018-10-16 13:37:34.084	    7f3deb2dc780	INFO 	daemon	src/daemon/main.cpp:289	Moving from main() into the daemonize now.
[0m[36m2018-10-16 13:37:34.084	    7f3deb2dc780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
[0m[36m2018-10-16 13:37:34.084	    7f3deb2dc780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:1929	Set limit-up to 2048 kB/s
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:1942	Set limit-down to 8192 kB/s
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:1964	Set limit-up to 2048 kB/s
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:1968	Set limit-down to 8192 kB/s
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=163.172.182.165, port=28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 163.172.182.165:28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=195.154.123.123, port=28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 195.154.123.123:28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.172.165, port=28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.172.165:28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.175.67, port=28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.175.67:28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=5.9.100.248, port=28080
[0m[36m2018-10-16 13:37:34.085	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 5.9.100.248:28080
[0m[36m2018-10-16 13:37:34.086	    7f3deb2dc780	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 2 from name: P2P, prefix_name = P2P
[0m[36m2018-10-16 13:37:34.086	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:571	Binding on 0.0.0.0:28080
[0m[36m2018-10-16 13:37:34.086	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:576	[1;32mNet service bound to 0.0.0.0:28080[0m
[0m[36m2018-10-16 13:37:38.091	    7f3deb2dc780	INFO 	net.p2p	src/p2p/net_node.inl:2070	No IGD was found.
[0m[36m2018-10-16 13:37:38.091	    7f3deb2dc780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
[0m[36m2018-10-16 13:37:38.091	    7f3deb2dc780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
[0m[36m2018-10-16 13:37:38.091	    7f3deb2dc780	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 1 from name: RPC, prefix_name = RPC
[0m[36m2018-10-16 13:37:38.091	    7f3deb2dc780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 0.0.0.0:28081
[0m[36m2018-10-16 13:37:38.091	    7f3deb2dc780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 28081
[0m[36m2018-10-16 13:37:38.091	    7f3deb2dc780	INFO 	global	src/daemon/core.h:86	Initializing core...
[0m[33m2018-10-16 13:37:38.091	    7f3deb2dc780	WARN 	cn	src/cryptonote_core/cryptonote_core.cpp:326	fluffy-blocks is obsolete, it is now default
[0m[36m2018-10-16 13:37:38.092	    7f3deb2dc780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder /root/.bitmoonero/testnet/testnet/lmdb ...
[0m[36m2018-10-16 13:37:38.092	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:544	DB map size:     1073741824
[0m[36m2018-10-16 13:37:38.092	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:545	Space used:      21454848
[0m[36m2018-10-16 13:37:38.092	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:546	Space remaining: 1052286976
[0m[36m2018-10-16 13:37:38.092	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:547	Size threshold:  0
[0m[36m2018-10-16 13:37:38.092	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:549	Percent used: 0.0200  Percent threshold: 0.9000
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2958	batch transaction mode already enabled, but asked to enable batch mode
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2961	batch transactions enabled
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:576	[check_and_resize_for_batch] checking DB size
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:544	DB map size:     1073741824
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:545	Space used:      21454848
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:546	Space remaining: 1052286976
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:547	Size threshold:  0
[0m[36m2018-10-16 13:37:38.123	    7f3deb2dc780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:549	Percent used: 0.0200  Percent threshold: 0.9000
[0m[36m2018-10-16 13:37:38.125	    7f3deb2dc780	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:445	Blockchain initialized. last block: 12839, d1489.h7.m32.s5 time ago, current difficulty: 218808
[0m[36m2018-10-16 13:37:38.125	    7f3deb2dc780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:585	Loading checkpoints
[0m[36m2018-10-16 13:37:38.125	    7f3deb2dc780	INFO 	global	src/daemon/core.h:92	Core initialized OK
[0m[36m2018-10-16 13:37:38.125	    7f3deb2dc780	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
[0m[36m2018-10-16 13:37:38.125	    7f3deb2dc780	INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:89	Run net_service loop( 2 threads)...
[0m[36m2018-10-16 13:37:38.125	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
[0m[36m2018-10-16 13:37:38.126	[SRV_MAIN]	INFO 	daemon	src/daemon/daemon.cpp:174	Starting ZMQ server...
[0m[36m2018-10-16 13:37:38.126	[SRV_MAIN]	INFO 	daemon	src/daemon/daemon.cpp:178	ZMQ server started at 127.0.0.1:28082.
[0m[36m2018-10-16 13:37:38.126	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
[0m[36m2018-10-16 13:37:38.126	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:636	Run net_service loop( 10 threads)...
[0m[36m2018-10-16 13:37:38.126	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:642	net_service loop stopped.
[0m[36m2018-10-16 13:37:38.126	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
[0m[36m2018-10-16 13:37:39.128	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
[0m[36m2018-10-16 13:37:39.129	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:190	Node stopped.
[0m[36m2018-10-16 13:37:39.129	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
[0m[36m2018-10-16 13:37:39.129	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
[0m[36m2018-10-16 13:37:39.129	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
[0m[36m2018-10-16 13:37:39.129	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
[0m[36m2018-10-16 13:37:43.134	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:2113	No IGD was found.
[0m[36m2018-10-16 13:37:43.135	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
[0m[36m2018-10-16 13:37:43.137	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
[0m[36m2018-10-16 13:37:43.137	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
[0m

# Discussion History
## moneromooo-monero | 2018-10-16T14:28:19+00:00
Input reaches EOF, so it stops, as expected.

Either use --detach or --non-interactive.

+invalid


# Action History
- Created by: DinoStray | 2018-10-16T14:04:48+00:00
- Closed at: 2018-10-16T14:33:06+00:00
