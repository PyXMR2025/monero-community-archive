---
title: 'Error opening database: Failed to open lmdb environment: Operation not supported'
source_url: https://github.com/monero-project/monero/issues/2484
author: calvintam236
assignees: []
labels: []
created_at: '2017-09-19T21:37:32+00:00'
updated_at: '2017-09-22T06:21:04+00:00'
type: issue
status: closed
closed_at: '2017-09-22T06:21:04+00:00'
---

# Original Description
I build a docker image for `monerod` on Raspberry Pi 3, and it seems I got stuck at error `Error opening database: Failed to open lmdb environment: Operation not supported`. Any idea how to fix it?

Host OS: [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
Dokcerfile: [this branch](https://github.com/calvintam236/docker_monerod/tree/armhf)

Full log:
```console
2017-09-19 21:30:27.647	        76f45000	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.0.0-release)
2017-09-19 21:30:27.647	        76f45000	INFO 	daemon	src/daemon/main.cpp:281	Moving from main() into the daemonize now.
2017-09-19 21:30:27.647	        76f45000	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-09-19 21:30:27.647	        76f45000	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-09-19 21:30:27.648	        76f45000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-09-19 21:30:27.649	        75e88460	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2017-09-19 21:30:27.649	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2017-09-19 21:30:27.657	        74cff460	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2017-09-19 21:30:27.657	        75688460	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-09-19 21:30:27.657	        744ff460	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2017-09-19 21:30:27.706	        75688460	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2017-09-19 21:30:27.707	        75688460	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-09-19 21:30:27.707	        75e88460	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2017-09-19 21:30:27.707	        75e88460	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-09-19 21:30:27.742	        744ff460	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2017-09-19 21:30:27.742	        744ff460	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-09-19 21:30:28.132	        74cff460	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2017-09-19 21:30:28.132	        74cff460	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-09-19 21:30:28.133	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2017-09-19 21:30:28.133	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-09-19 21:30:28.133	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-09-19 21:30:28.133	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2017-09-19 21:30:28.133	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2017-09-19 21:30:28.133	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 107.152.130.98:18080
2017-09-19 21:30:28.133	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 107.152.130.98:18080
2017-09-19 21:30:28.133	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 161.67.132.39:18080
2017-09-19 21:30:28.134	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 161.67.132.39:18080
2017-09-19 21:30:28.134	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 163.172.182.165:18080
2017-09-19 21:30:28.134	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 163.172.182.165:18080
2017-09-19 21:30:28.134	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 195.154.123.123:28080
2017-09-19 21:30:28.134	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 195.154.123.123:28080
2017-09-19 21:30:28.134	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 198.74.231.92:18080
2017-09-19 21:30:28.134	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 198.74.231.92:18080
2017-09-19 21:30:28.134	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.172.165:28080
2017-09-19 21:30:28.134	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.172.165:28080
2017-09-19 21:30:28.134	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 212.83.175.67:18080
2017-09-19 21:30:28.134	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 212.83.175.67:18080
2017-09-19 21:30:28.134	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:530	Seed node: 5.9.100.248:18080
2017-09-19 21:30:28.134	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:395	Added seed node: 5.9.100.248:18080
2017-09-19 21:30:28.135	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:533	Number of seed nodes: 8
2017-09-19 21:30:28.136	        76f45000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-09-19 21:30:28.136	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:1883	Set limit-up to 2048 kB/s
2017-09-19 21:30:28.136	        76f45000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-19 21:30:28.136	        76f45000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-19 21:30:28.136	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:1897	Set limit-down to 8192 kB/s
2017-09-19 21:30:28.136	        76f45000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 4.40402e+06 kbps
2017-09-19 21:30:28.136	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:1919	Set limit-up to 2048 kB/s
2017-09-19 21:30:28.136	        76f45000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-19 21:30:28.136	        76f45000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:162	Setting LIMIT: 8.38861e+06 kbps
2017-09-19 21:30:28.136	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:1923	Set limit-down to 8192 kB/s
2017-09-19 21:30:29.582	        76f45000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-09-19 21:30:29.582	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:572	Binding on 0.0.0.0:18080
2017-09-19 21:30:29.582	        76f45000	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-09-19 21:30:29.582	        76f45000	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-09-19 21:30:29.583	        76f45000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-09-19 21:30:29.583	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:577	Net service bound to 0.0.0.0:18080
2017-09-19 21:30:29.583	        76f45000	DEBUG	net.p2p	src/p2p/net_node.inl:583	Attempting to add IGD port mapping.
2017-09-19 21:30:33.588	        76f45000	INFO 	net.p2p	src/p2p/net_node.inl:622	No IGD was found.
2017-09-19 21:30:33.588	        76f45000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-09-19 21:30:33.589	        76f45000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-09-19 21:30:33.589	        76f45000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:795	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-09-19 21:30:33.589	        76f45000	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-09-19 21:30:33.589	        76f45000	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:734	start accept
2017-09-19 21:30:33.589	        76f45000	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-09-19 21:30:33.589	        76f45000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-09-19 21:30:33.590	        76f45000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-09-19 21:30:33.590	        76f45000	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-09-19 21:30:34.077	        76f45000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /monerod/lmdb ...
2017-09-19 21:30:34.077	        76f45000	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: fast
2017-09-19 21:30:34.077	        76f45000	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: async
2017-09-19 21:30:34.077	        76f45000	DEBUG	cn	src/cryptonote_core/cryptonote_core.cpp:339	option: 1000
2017-09-19 21:30:35.429	        76f45000	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Failed to open lmdb environment: Operation not supported
2017-09-19 21:30:35.436	        76f45000	ERROR	cn	src/cryptonote_core/cryptonote_core.cpp:399	Error opening database: Failed to open lmdb environment: Operation not supported
2017-09-19 21:30:35.437	        76f45000	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-09-19 21:30:35.437	        76f45000	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-09-19 21:30:35.437	        76f45000	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-09-19 21:30:35.437	        76f45000	INFO 	net	src/p2p/net_node.h:250	Killing the net_node
2017-09-19 21:30:35.437	        76f45000	INFO 	net	src/p2p/net_node.h:254	Joined extra background net_node threads
2017-09-19 21:30:38.315	        76f45000	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#0 to 0.0.0.0
2017-09-19 21:30:38.315	        76f45000	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-09-19 21:30:38.780	        76f45000	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-09-19 21:30:38.787	        76f45000	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-09-19 21:30:38.787	        76f45000	DEBUG	miner	src/cryptonote_basic/miner.cpp:337	Not mining - nothing to stop
2017-09-19 21:30:38.787	        76f45000	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-09-19 21:30:38.787	        76f45000	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
```

# Discussion History
## hyc | 2017-09-19T21:50:38+00:00
Yes, don't use Docker.

What kind of filesystem is mounted on /monerod ?

## calvintam236 | 2017-09-19T22:01:19+00:00
I mounted the folder using `curlftpfs` (ftp). The local storage of the host don't have sufficient storage to store the whole blockchain.

## hyc | 2017-09-19T22:15:38+00:00
LMDB requires a local filesystem that supports mmap. You're going to have to run this on some other host.

# Action History
- Created by: calvintam236 | 2017-09-19T21:37:32+00:00
- Closed at: 2017-09-22T06:21:04+00:00
