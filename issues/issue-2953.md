---
title: Deamon failed to start - Error attempting to retrieve a block from the db
source_url: https://github.com/monero-project/monero/issues/2953
author: AntonSazonov
assignees: []
labels: []
created_at: '2017-12-18T06:25:58+00:00'
updated_at: '2019-01-18T09:42:22+00:00'
type: issue
status: closed
closed_at: '2017-12-21T17:38:43+00:00'
---

# Original Description
Blockchain was successfully downloaded ~ at 23-24 Gb.
Monerod crashing on Windows 10 with following log:

> 2017-12-18 06:34:53.600	10028	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-18 06:34:53.601	10028	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-12-18 06:34:53.601	10028	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-18 06:34:53.601	10028	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-18 06:34:53.601	10028	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-18 06:34:53.602	10028	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-12-18 06:34:53.602	11292	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-12-18 06:34:53.602	9464	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-12-18 06:34:53.603	1144	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-12-18 06:34:53.603	10280	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-12-18 06:34:55.777	10280	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-12-18 06:34:55.777	10280	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-12-18 06:34:55.814	11292	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-12-18 06:34:55.814	11292	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-12-18 06:34:55.816	9464	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-12-18 06:34:55.816	9464	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-12-18 06:34:55.944	1144	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-12-18 06:34:55.944	1144	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-12-18 06:34:55.945	10028	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-12-18 06:34:55.945	10028	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-12-18 06:34:55.945	10028	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-12-18 06:34:55.945	10028	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-12-18 06:34:55.945	10028	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-12-18 06:34:55.945	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-12-18 06:34:55.945	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-12-18 06:34:55.945	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-12-18 06:34:55.945	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-12-18 06:34:55.945	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-12-18 06:34:55.946	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-12-18 06:34:55.946	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-12-18 06:34:55.946	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-12-18 06:34:55.946	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-12-18 06:34:55.946	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-12-18 06:34:55.946	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-12-18 06:34:55.946	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-12-18 06:34:55.946	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-12-18 06:34:55.946	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-12-18 06:34:55.946	10028	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-12-18 06:34:55.947	10028	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-12-18 06:34:55.947	10028	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-12-18 06:34:55.948	10028	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-18 06:34:55.948	10028	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-12-18 06:34:55.948	10028	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 06:34:55.948	10028	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 06:34:55.948	10028	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-12-18 06:34:55.948	10028	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-18 06:34:55.948	10028	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-12-18 06:34:55.948	10028	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 06:34:55.948	10028	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 06:34:55.949	10028	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-12-18 06:34:55.950	10028	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-12-18 06:34:55.950	10028	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-12-18 06:34:55.950	10028	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-18 06:34:55.950	10028	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-18 06:34:55.951	10028	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-12-18 06:34:55.951	10028	INFO 	net.p2p	src/p2p/net_node.inl:577	[1;32mNet service bound to 0.0.0.0:18080[0m
2017-12-18 06:34:55.951	10028	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-12-18 06:34:57.104	10028	WARN 	net.p2p	src/p2p/net_node.inl:613	IGD was found but reported as not connected.
2017-12-18 06:34:57.104	10028	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-18 06:34:57.104	10028	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-18 06:34:57.105	10028	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-12-18 06:34:57.107	10028	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-18 06:34:57.107	10028	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-18 06:34:57.107	10028	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-18 06:34:57.108	10028	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-12-18 06:34:57.108	10028	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-18 06:34:57.108	10028	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-18 06:34:57.110	10028	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\bitmonero\lmdb ...
2017-12-18 06:34:57.111	10028	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-12-18 06:34:57.111	10028	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-12-18 06:34:57.111	10028	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-12-18 06:34:57.149	10028	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     31303054336
2017-12-18 06:34:57.150	10028	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      23867432960
2017-12-18 06:34:57.150	10028	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 7435621376
2017-12-18 06:34:57.150	10028	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-12-18 06:34:57.150	10028	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.7625  Percent threshold: 0.8000
2017-12-18 06:34:57.150	10028	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 1375108
2017-12-18 06:34:57.152	10028	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:197	reorganizing from 1365029
2017-12-18 06:34:57.225	10028	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Error attempting to retrieve a block from the db
2017-12-18 06:34:57.225	10028	FATAL	daemon	src/daemon/daemon.cpp:150	Uncaught exception! Error attempting to retrieve a block from the db
2017-12-18 06:34:57.225	10028	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-12-18 06:34:57.225	10028	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-12-18 06:34:57.225	10028	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-12-18 06:34:57.225	10028	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
2017-12-18 06:34:57.225	10028	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
2017-12-18 06:34:57.227	10028	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-12-18 06:34:57.227	10028	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-12-18 06:34:57.227	10028	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-12-18 06:34:57.342	10028	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-12-18 06:34:57.342	10028	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-12-18 06:34:57.342	10028	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully


# Discussion History
## moneromooo-monero | 2017-12-18T10:08:13+00:00
Did your computer crash or power down without normal shutdown ? Looks like the blockchain database is corrupted.

## AntonSazonov | 2017-12-18T16:00:30+00:00
No. This couldn't happen, because I have APC.
I thought about that too.

## moneromooo-monero | 2017-12-18T16:10:51+00:00
Try running monerod with --db-salvage, might help.

## AntonSazonov | 2017-12-18T16:20:50+00:00
Unfortunately.
`monerod.exe --log-level 2 --db-salvage --data-dir C:\bitmonero`

> 2017-12-18 16:16:40.405	1664	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-18 16:16:40.405	1664	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-12-18 16:16:40.405	1664	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-18 16:16:40.405	1664	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-18 16:16:40.406	1664	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-18 16:16:40.406	4228	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-12-18 16:16:40.406	1664	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-12-18 16:16:40.407	4736	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-12-18 16:16:40.407	5604	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-12-18 16:16:40.407	11928	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-12-18 16:16:42.711	4736	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-12-18 16:16:42.711	4736	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-12-18 16:16:42.768	11928	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-12-18 16:16:42.768	11928	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-12-18 16:16:42.847	4228	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-12-18 16:16:42.847	4228	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-12-18 16:16:42.859	5604	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-12-18 16:16:42.859	5604	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-12-18 16:16:42.859	1664	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-12-18 16:16:42.859	1664	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-12-18 16:16:42.859	1664	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-12-18 16:16:42.859	1664	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-12-18 16:16:42.859	1664	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-12-18 16:16:42.859	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-12-18 16:16:42.859	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-12-18 16:16:42.860	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-12-18 16:16:42.860	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-12-18 16:16:42.860	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-12-18 16:16:42.860	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-12-18 16:16:42.860	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-12-18 16:16:42.860	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-12-18 16:16:42.860	1664	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-12-18 16:16:42.860	1664	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-12-18 16:16:42.861	1664	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-18 16:16:42.861	1664	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-12-18 16:16:42.861	1664	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 16:16:42.861	1664	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 16:16:42.861	1664	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-12-18 16:16:42.861	1664	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-18 16:16:42.861	1664	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-12-18 16:16:42.861	1664	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 16:16:42.861	1664	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-18 16:16:42.861	1664	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-12-18 16:16:42.866	1664	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-12-18 16:16:42.866	1664	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-12-18 16:16:42.866	1664	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-18 16:16:42.867	1664	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-18 16:16:42.867	1664	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-12-18 16:16:42.867	1664	INFO 	net.p2p	src/p2p/net_node.inl:577	[1;32mNet service bound to 0.0.0.0:18080[0m
2017-12-18 16:16:42.867	1664	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-12-18 16:16:43.940	1664	WARN 	net.p2p	src/p2p/net_node.inl:613	IGD was found but reported as not connected.
2017-12-18 16:16:43.940	1664	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-18 16:16:43.940	1664	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-18 16:16:43.940	1664	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-12-18 16:16:43.941	1664	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-18 16:16:43.942	1664	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-18 16:16:43.942	1664	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-18 16:16:43.942	1664	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-12-18 16:16:43.942	1664	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-18 16:16:43.942	1664	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-18 16:16:43.942	1664	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\bitmonero\lmdb ...
2017-12-18 16:16:43.943	1664	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-12-18 16:16:43.943	1664	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-12-18 16:16:43.943	1664	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-12-18 16:16:43.963	1664	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     31303054336
2017-12-18 16:16:43.963	1664	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      23867432960
2017-12-18 16:16:43.963	1664	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 7435621376
2017-12-18 16:16:43.963	1664	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-12-18 16:16:43.963	1664	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.7625  Percent threshold: 0.8000
2017-12-18 16:16:43.964	1664	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 1375108
2017-12-18 16:16:43.965	1664	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:197	reorganizing from 1365029
2017-12-18 16:16:44.032	1664	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Error attempting to retrieve a block from the db
2017-12-18 16:16:44.032	1664	FATAL	daemon	src/daemon/daemon.cpp:150	Uncaught exception! Error attempting to retrieve a block from the db
2017-12-18 16:16:44.032	1664	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-12-18 16:16:44.032	1664	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-12-18 16:16:44.033	1664	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-12-18 16:16:44.033	1664	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
2017-12-18 16:16:44.033	1664	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
2017-12-18 16:16:44.034	1664	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-12-18 16:16:44.034	1664	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-12-18 16:16:44.035	1664	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-12-18 16:16:44.169	1664	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-12-18 16:16:44.169	1664	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-12-18 16:16:44.169	1664	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully


## moneromooo-monero | 2017-12-18T16:23:34+00:00
Please post the output of:

mdb_stat -a C:\bitmonero\lmdb


## AntonSazonov | 2017-12-18T16:28:16+00:00
Mm...  mdb_stat - what is it?

## AntonSazonov | 2017-12-18T16:37:16+00:00
A haw Windows 10 client and wallet.

## moneromooo-monero | 2017-12-18T16:45:25+00:00
It is a program. It's part of lmdb. If you don't have it, the source is in external/db_drivers/liblmdb, and you can do something like:

make -C external/db_drivers/liblmdb

and mdb_stat should be in external/db_drivers/liblmdb

## AntonSazonov | 2017-12-19T06:55:31+00:00
Output of: mdb_stat -a C:\bitmonero\lmdb
> Status of Main DB
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
  Entries: 1375108
Status of block_info
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1375108
Status of blocks
  Tree depth: 4
  Branch pages: 496
  Leaf pages: 111023
  Overflow pages: 34
  Entries: 1375108
Status of hf_versions
  Tree depth: 3
  Branch pages: 31
  Leaf pages: 6741
  Overflow pages: 0
  Entries: 1375108
Status of output_amounts
  Tree depth: 4
  Branch pages: 530
  Leaf pages: 80661
  Overflow pages: 0
  Entries: 23786782
Status of output_txs
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 23786782
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
  Entries: 20256958
Status of tx_indices
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 2856154
Status of tx_outputs
  Tree depth: 4
  Branch pages: 269
  Leaf pages: 60077
  Overflow pages: 2383
  Entries: 2856154
Status of txpool_blob
  Tree depth: 0
  Branch pages: 0
  Leaf pages: 0
  Overflow pages: 0
  Entries: 0
Status of txpool_meta
  Tree depth: 0
  Branch pages: 0
  Leaf pages: 0
  Overflow pages: 0
  Entries: 0
Status of txs
  Tree depth: 4
  Branch pages: 1062
  Leaf pages: 238487
  Overflow pages: 4340286
  Entries: 2856154

## moneromooo-monero | 2017-12-19T09:57:09+00:00
That looks ok. Can you apply this patch to monero, and try again please:

Paste this in a file, say, dberror.diff, then, while in the monero directory:

patch -p1 < dberror.diff

Then build again.

```
diff --git a/src/blockchain_db/lmdb/db_lmdb.cpp b/src/blockchain_db/lmdb/db_lmdb.cpp
index 07a0e67..6398d2d 100644
--- a/src/blockchain_db/lmdb/db_lmdb.cpp
+++ b/src/blockchain_db/lmdb/db_lmdb.cpp
@@ -1806,7 +1806,7 @@ cryptonote::blobdata BlockchainLMDB::get_block_blob_from_height(const uint64_t&
     throw0(BLOCK_DNE(std::string("Attempt to get block from height ").append(boost::lexical_cast<std::string>(height)).append(" failed -- block not in db").c_str()));
   }
   else if (get_result)
-    throw0(DB_ERROR("Error attempting to retrieve a block from the db"));
+    throw0(DB_ERROR(("Error attempting to retrieve a block from the db at height " + std::to_string(height) + ": " + mdb_strerror(get_result)).c_str()));
 
   blobdata bd;
   bd.assign(reinterpret_cast<char*>(result.mv_data), result.mv_size);
```

## AntonSazonov | 2017-12-20T18:53:34+00:00
Output of patched build: `monerod.exe --log-level 2 --db-salvage --data-dir C:\bitmonero`
> 2017-12-20 18:50:59.792	2100	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2017-12-20 18:50:59.793	2100	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-12-20 18:50:59.793	2100	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-12-20 18:50:59.793	2100	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-12-20 18:50:59.794	2100	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-12-20 18:50:59.794	3160	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-12-20 18:50:59.794	2100	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-12-20 18:50:59.795	2696	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-12-20 18:50:59.795	12556	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-12-20 18:50:59.795	3912	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-12-20 18:51:02.001	2696	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-12-20 18:51:02.002	2696	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-12-20 18:51:02.003	3160	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-12-20 18:51:02.003	3160	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-12-20 18:51:02.046	12556	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-12-20 18:51:02.046	12556	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-12-20 18:51:02.135	3912	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-12-20 18:51:02.135	3912	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-12-20 18:51:02.136	2100	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-12-20 18:51:02.136	2100	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-12-20 18:51:02.137	2100	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-20 18:51:02.137	2100	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-12-20 18:51:02.137	2100	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-20 18:51:02.137	2100	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-20 18:51:02.137	2100	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-12-20 18:51:02.137	2100	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+006 kbps
2017-12-20 18:51:02.138	2100	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-12-20 18:51:02.138	2100	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-20 18:51:02.138	2100	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+006 kbps
2017-12-20 18:51:02.138	2100	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-12-20 18:51:02.139	2100	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-12-20 18:51:02.139	2100	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-12-20 18:51:02.139	2100	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-20 18:51:02.139	2100	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-20 18:51:02.139	2100	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-12-20 18:51:02.139	2100	INFO 	net.p2p	src/p2p/net_node.inl:577	[1;32mNet service bound to 0.0.0.0:18080[0m
2017-12-20 18:51:02.139	2100	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-12-20 18:51:03.286	2100	WARN 	net.p2p	src/p2p/net_node.inl:613	IGD was found but reported as not connected.
2017-12-20 18:51:03.286	2100	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-12-20 18:51:03.286	2100	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-12-20 18:51:03.286	2100	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-12-20 18:51:03.288	2100	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-12-20 18:51:03.288	2100	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-12-20 18:51:03.289	2100	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-12-20 18:51:03.289	2100	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-12-20 18:51:03.289	2100	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-12-20 18:51:03.289	2100	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-12-20 18:51:03.290	2100	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder C:\bitmonero\lmdb ...
2017-12-20 18:51:03.292	2100	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-12-20 18:51:03.292	2100	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-12-20 18:51:03.292	2100	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-12-20 18:51:03.330	2100	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:518	DB map size:     31303054336
2017-12-20 18:51:03.330	2100	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:519	Space used:      23867432960
2017-12-20 18:51:03.330	2100	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:520	Space remaining: 7435621376
2017-12-20 18:51:03.331	2100	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:521	Size threshold:  0
2017-12-20 18:51:03.331	2100	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:523	Percent used: 0.7625  Percent threshold: 0.8000
2017-12-20 18:51:03.331	2100	DEBUG	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1219	Setting m_height to: 1375108
2017-12-20 18:51:03.332	2100	DEBUG	hardfork	src/cryptonote_basic/hardfork.cpp:197	reorganizing from 1365029
2017-12-20 18:51:03.410	2100	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Error attempting to retrieve a block from the db at height 1374781: MDB_CORRUPTED: Located page was wrong type
2017-12-20 18:51:03.411	2100	FATAL	daemon	src/daemon/daemon.cpp:150	Uncaught exception! Error attempting to retrieve a block from the db at height 1374781: MDB_CORRUPTED: Located page was wrong type
2017-12-20 18:51:03.411	2100	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-12-20 18:51:03.411	2100	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-12-20 18:51:03.411	2100	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-12-20 18:51:03.411	2100	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
2017-12-20 18:51:03.411	2100	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
2017-12-20 18:51:03.413	2100	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-12-20 18:51:03.413	2100	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-12-20 18:51:03.413	2100	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-12-20 18:51:03.526	2100	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-12-20 18:51:03.526	2100	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-12-20 18:51:03.526	2100	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully


## moneromooo-monero | 2017-12-20T20:53:00+00:00
That log shows:

2017-12-20 18:51:03.410 2100 WARN blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:72 Error attempting to retrieve a block from the db at height 1374781: MDB_CORRUPTED: Located page was wrong type

So your db is corrupted. If --db-salvage doesn't work, your only way out is to resync from scratch.
If you do this, please keep a copy of the current db (data.mdb) as hyc might want to have a look at it to see what is wrong with it.


## AntonSazonov | 2017-12-21T17:38:32+00:00
Ok. Thanks.

## Predikador | 2019-01-18T09:42:22+00:00
Please, help a noob, the same thing happens to AntonSazonov, I do not load the chain of electroneum blocks or with -db-salvage, but in my case if there was a sudden blackout. I'll find out if the source or plate fails. What I intend is to reinstall the entire chain and not do it, when executing "electroneumd.exe" it closes automatically for the error.

C:\Users\Javi y Carme\Downloads\electroneum-win-x64-v2.1.1.1>electroneumd.exe --db-salvage
2019-01-18 09:24:51.657 9320    INFO    global  src/daemon/main.cpp:280 Electroneum 'August 2018' (v2.1.1.1-a15d47f6)
2019-01-18 09:24:51.658 9320    INFO    global  src/daemon/protocol.h:56        Initializing cryptonote protocol...
2019-01-18 09:24:51.658 9320    INFO    global  src/daemon/protocol.h:61        Cryptonote protocol initialized OK
2019-01-18 09:24:51.659 9320    INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2019-01-18 09:24:52.926 9320    INFO    global  src/daemon/p2p.h:69     P2p server initialized OK
2019-01-18 09:24:52.927 9320    INFO    global  src/daemon/rpc.h:59     Initializing core rpc server...
2019-01-18 09:24:52.927 9320    INFO    global  contrib/epee/include/net/http_server_impl_base.h:70  Binding on 127.0.0.1:26968
2019-01-18 09:24:52.928 9320    INFO    global  src/daemon/rpc.h:64     Core rpc server initialized OK on port: 26968
2019-01-18 09:24:52.928 9320    INFO    global  src/daemon/core.h:74    Initializing core...
2019-01-18 09:24:52.930 9320    INFO    global  src/cryptonote_core/cryptonote_core.cpp:324     Loading blockchain from folder C:\ProgramData\electroneum\lmdb ...
2019-01-18 09:24:52.935 9320    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1156 LMDB memory map needs to be resized, doing that now.
2019-01-18 09:24:52.939 9320    INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:495  LMDB Mapsize increased.  Old: 36274MiB, New: 37298MiB
2019-01-18 09:24:52.942 9320    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:73   Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2019-01-18 09:24:52.942 9320    FATAL   daemon  src/daemon/daemon.cpp:151       Uncaught exception! Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2019-01-18 09:24:52.942 9320    INFO    global  src/daemon/rpc.h:91     Deinitializing rpc server...
2019-01-18 09:24:52.943 9320    INFO    global  src/daemon/p2p.h:91     Deinitializing p2p...
2019-01-18 09:24:52.954 9320    INFO    global  src/daemon/core.h:90    Deinitializing core...
2019-01-18 09:24:52.955 9320    ERROR   daemon  src/daemon/core.h:95    Failed to deinitialize core...
2019-01-18 09:24:52.956 9320    INFO    global  src/daemon/protocol.h:78        Stopping cryptonote protocol...
2019-01-18 09:24:52.956 9320    INFO    global  src/daemon/protocol.h:82        Cryptonote protocol stopped successfully


# Action History
- Created by: AntonSazonov | 2017-12-18T06:25:58+00:00
- Closed at: 2017-12-21T17:38:43+00:00
