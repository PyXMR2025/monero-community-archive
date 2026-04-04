---
title: monerod exits without any indication why when run in a non interactive terminal
source_url: https://github.com/monero-project/monero/issues/4258
author: MicahZoltu
assignees: []
labels: []
created_at: '2018-08-14T18:39:29+00:00'
updated_at: '2018-10-26T09:33:08+00:00'
type: issue
status: closed
closed_at: '2018-10-26T09:33:08+00:00'
---

# Original Description
When I start monerod, it goes from doing what appears to be startup logic to doing what appears to be shutdown logic.  There is no obvious indicator what triggers the change.

* Deleting the contents of `--data-dir` does not resolve the issue.
* Full command:
```
/app/monerod --data-dir /app/data --rpc-bind-ip 0.0.0.0 --confirm-external-bind --restricted-rpc --log-level 1
```
```
2018-08-14 18:32:32.983	    7f73926f4bc0	INFO 	global	src/daemon/main.cpp:282	Monero 'Lithium Luna' (v0.12.3.0-release)
2018-08-14 18:32:32.984	    7f73926f4bc0	INFO 	daemon	src/daemon/main.cpp:284	Moving from main() into the daemonize now.
2018-08-14 18:32:32.985	    7f73926f4bc0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-08-14 18:32:32.985	    7f73926f4bc0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-08-14 18:32:32.986	    7f73926f4bc0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-08-14 18:32:32.987	    7f73926f4bc0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-08-14 18:32:32.987	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:1875	Set limit-up to 2048 kB/s
2018-08-14 18:32:32.987	    7f73926f4bc0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-08-14 18:32:32.988	    7f73926f4bc0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-08-14 18:32:32.988	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:1888	Set limit-down to 8192 kB/s
2018-08-14 18:32:32.988	    7f73926f4bc0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-08-14 18:32:32.989	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:1910	Set limit-up to 2048 kB/s
2018-08-14 18:32:32.989	    7f73926f4bc0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-08-14 18:32:32.989	    7f73926f4bc0	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-08-14 18:32:32.989	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:1914	Set limit-down to 8192 kB/s
2018-08-14 18:32:33.073	    7f738f71b700	INFO 	net.p2p	src/p2p/net_node.inl:457	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-08-14 18:32:33.073	    7f7390f1e700	INFO 	net.p2p	src/p2p/net_node.inl:457	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2018-08-14 18:32:33.170	    7f738ff1c700	INFO 	net.p2p	src/p2p/net_node.inl:457	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2018-08-14 18:32:52.990	    7f73926f4bc0	WARN 	net.p2p	src/p2p/net_node.inl:472	dns_threads[1] timed out, sending interrupt
2018-08-14 18:32:52.990	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:495	DNS seed node lookup either timed out or failed, falling back to defaults
2018-08-14 18:32:52.991	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 107.152.130.98:18080
2018-08-14 18:32:52.991	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 161.67.132.39:18080
2018-08-14 18:32:52.992	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 163.172.182.165:18080
2018-08-14 18:32:52.992	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 195.154.123.123:18080
2018-08-14 18:32:52.992	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 198.74.231.92:18080
2018-08-14 18:32:52.992	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 212.83.172.165:18080
2018-08-14 18:32:52.992	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 212.83.175.67:18080
2018-08-14 18:32:52.992	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:357	Added seed node: 5.9.100.248:18080
2018-08-14 18:32:52.998	    7f73926f4bc0	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:910	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-08-14 18:32:52.998	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:546	Binding on 0.0.0.0:18080
2018-08-14 18:32:52.999	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:551	Net service bound to 0.0.0.0:18080
2018-08-14 18:32:57.008	    7f73926f4bc0	INFO 	net.p2p	src/p2p/net_node.inl:2016	No IGD was found.
2018-08-14 18:32:57.008	    7f73926f4bc0	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-08-14 18:32:57.010	    7f73926f4bc0	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-08-14 18:32:57.010	    7f73926f4bc0	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:910	Set server type to: 1 from name: RPC, prefix_name = RPC
2018-08-14 18:32:57.010	    7f73926f4bc0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 0.0.0.0:18081
2018-08-14 18:32:57.011	    7f73926f4bc0	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-08-14 18:32:57.011	    7f73926f4bc0	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-08-14 18:32:57.012	    7f73926f4bc0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /app/data/lmdb ...
2018-08-14 18:32:57.016	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     1073741824
2018-08-14 18:32:57.016	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      73728
2018-08-14 18:32:57.017	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 1073668096
2018-08-14 18:32:57.017	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-08-14 18:32:57.017	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.0001  Percent threshold: 0.8000
2018-08-14 18:32:57.018	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-08-14 18:32:57.018	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     1073741824
2018-08-14 18:32:57.018	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      73728
2018-08-14 18:32:57.018	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 1073668096
2018-08-14 18:32:57.019	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-08-14 18:32:57.019	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.0001  Percent threshold: 0.8000
2018-08-14 18:32:57.019	    7f73926f4bc0	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4426	Loading precomputed blocks (198276 bytes)
2018-08-14 18:32:57.021	    7f73926f4bc0	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4437	precomputed blocks hash: <0924bc1c47aae448321fde949554be192878dd800e6489379865218f84eacbca>, expected 0924bc1c47aae448321fde949554be192878dd800e6489379865218f84eacbca
2018-08-14 18:32:57.093	    7f73926f4bc0	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:4474	6196 block hashes loaded
2018-08-14 18:32:57.100	    7f73926f4bc0	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:441	Blockchain initialized. last block: 0, d2232.h13.m32.s57 time ago, current difficulty: 1
2018-08-14 18:32:57.106	    7f73926f4bc0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:526	Loading checkpoints
2018-08-14 18:32:57.107	    7f73926f4bc0	INFO 	checkpoints	src/checkpoints/checkpoints.cpp:220	Blockchain checkpoints file not found
2018-08-14 18:32:57.109	    7f73926f4bc0	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     1073741824
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      73728
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 1073668096
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.0001  Percent threshold: 0.8000
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:564	[check_and_resize_for_batch] checking DB size
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:528	DB map size:     1073741824
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:529	Space used:      73728
2018-08-14 18:32:57.109	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:530	Space remaining: 1073668096
2018-08-14 18:32:57.110	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:531	Size threshold:  0
2018-08-14 18:32:57.110	    7f73926f4bc0	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:533	Percent used: 0.0001  Percent threshold: 0.8000
2018-08-14 18:32:57.110	    7f73926f4bc0	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-08-14 18:32:57.110	    7f73926f4bc0	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-08-14 18:32:57.110	    7f73926f4bc0	INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:89	Run net_service loop( 2 threads)...
2018-08-14 18:32:57.110	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-08-14 18:32:57.135	[SRV_MAIN]	INFO 	daemon	src/daemon/daemon.cpp:173	Starting ZMQ server...
2018-08-14 18:32:57.135	[SRV_MAIN]	INFO 	daemon	src/daemon/daemon.cpp:177	ZMQ server started at 127.0.0.1:18082.
2018-08-14 18:32:57.135	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-08-14 18:32:57.136	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:611	Run net_service loop( 10 threads)...
2018-08-14 18:32:57.136	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:617	net_service loop stopped.
2018-08-14 18:32:57.136	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-08-14 18:32:58.149	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-08-14 18:32:58.150	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-08-14 18:32:58.150	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-08-14 18:32:58.151	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-08-14 18:32:58.151	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:249	Killing the net_node
2018-08-14 18:32:58.151	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:253	Joined extra background net_node threads
2018-08-14 18:33:02.156	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:2059	No IGD was found.
2018-08-14 18:33:02.163	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-08-14 18:33:02.187	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-08-14 18:33:02.187	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
```

# Discussion History
## MicahZoltu | 2018-08-14T19:37:47+00:00
I was running from a non-interactive terminal, so I needed to include `--non-interactive`.

Recommend leaving this issue open and changing it to a bug that the log does not give any indication as to why it is shutting down, it just silently fails.  Recommend adding a log line saying:
> Shutting down due to non interactive terminal, run with `--non-interactive` or use an interactive terminal

## moneromooo-monero | 2018-08-14T20:00:06+00:00
Did it actually crash ? It doens't seem to based on the report, but the title says it did.


## MicahZoltu | 2018-08-14T20:15:33+00:00
No, exit code `0`.  I'll update the title.

## moneromooo-monero | 2018-10-20T09:21:01+00:00
https://github.com/monero-project/monero/pull/4670

## moneromooo-monero | 2018-10-26T09:25:54+00:00
+resolved

# Action History
- Created by: MicahZoltu | 2018-08-14T18:39:29+00:00
- Closed at: 2018-10-26T09:33:08+00:00
