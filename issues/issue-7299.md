---
title: Error during intial sync
source_url: https://github.com/monero-project/monero/issues/7299
author: savager
assignees: []
labels: []
created_at: '2021-01-09T06:10:00+00:00'
updated_at: '2021-01-09T15:31:44+00:00'
type: issue
status: closed
closed_at: '2021-01-09T15:31:44+00:00'
---

# Original Description
Ubuntu server VM. 16gb ram. 2 core. Freshly compiled. Ports forwarded, 

config:
```
data-dir=/home/username/.bitmonero

log-file=/home/username/.bitmonero/monero.log
log-level=1
max-log-file-size=0            # Prevent monerod from managing the log files; we want logrotate to take care of that

p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
p2p-bind-port=18080            # Bind to default port

rpc-bind-ip=0.0.0.0            # Bind to all interfaces
rpc-bind-port=18081            # Bind on default port
confirm-external-bind=1        # Open node (confirm)
restricted-rpc=1               # Prevent unsafe RPC calls
no-igd=1                       # Disable UPnP port mapping

db-sync-mode=safe

enforce-dns-checkpointing=1

out-peers=64              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
in-peers=1024             # The default is unlimited; we prefer to put a cap on this

limit-rate-up=1048576     # 1048576 kB/s == 1GB/s; a raise from default 2048 kB/s; contribute more to p2p network
limit-rate-down=1048576   # 1048576 kB/s == 1GB/s; a raise from default 8192 kB/s; allow for faster initial sync
```
```
2021-01-09 05:58:43.785	[P2P5]	INFO	perf.txpool	src/common/perf_timer.cpp:120	PERF             ----------
2021-01-09 05:58:43.785	[P2P5]	INFO	txpool	src/cryptonote_core/tx_pool.cpp:376	Transaction added to pool: txid <38356023a813743430346fcf77cbac0bde85dd5dd1172945917126617cb87e29> weight: 6696 fee/byte: 784050
2021-01-09 05:58:43.785	[P2P5]	INFO	perf.txpool	src/common/perf_timer.cpp:156	PERF      413    add_tx
2021-01-09 05:58:43.796	[P2P5]	INFO	perf.blockchain	src/common/perf_timer.cpp:120	PERF             ----------
2021-01-09 05:58:43.796	[P2P5]	INFO	perf.blockchain	src/common/perf_timer.cpp:156	PERF      116    get_next_long_term_block_weight
2021-01-09 05:58:43.798	[P2P5]	INFO	perf.blockchain	src/common/perf_timer.cpp:120	PERF             ----------
2021-01-09 05:58:43.798	[P2P5]	INFO	perf.blockchain	src/common/perf_timer.cpp:156	PERF      104    update_next_cumulative_weight_limit
2021-01-09 05:58:43.798	[P2P5]	INFO	blockchain	src/cryptonote_core/blockchain.cpp:4342	+++++ BLOCK SUCCESSFULLY ADDED
2021-01-09 05:58:43.798	[P2P5]	INFO	blockchain	src/cryptonote_core/blockchain.cpp:4342	id:	<60feb29853a39e8dc3519b67523b3ebe9a11755150ede674490ecd2061d88757>
2021-01-09 05:58:43.798	[P2P5]	INFO	blockchain	src/cryptonote_core/blockchain.cpp:4342	PoW:	<ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
2021-01-09 05:58:43.798	[P2P5]	INFO	blockchain	src/cryptonote_core/blockchain.cpp:4342	HEIGHT 81004, difficulty:	250803078
2021-01-09 05:58:43.798	[P2P5]	INFO	blockchain	src/cryptonote_core/blockchain.cpp:4342	block reward: 16.319131754545(16.313881754545 + 0.005250000000), coinbase_weight: 286, cumulative weight: 6982, 11(10/0)ms
2021-01-09 05:58:43.812	[P2P6]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:46	[51.79.58.92:4383 OUT] 10 bytes received for category command-1003 initiated by peer
2021-01-09 05:58:43.812	[P2P6]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:46	[51.79.58.92:4383 OUT] 38 bytes sent for category command-1003 initiated by peer
2021-01-09 05:58:43.814	[P2P1]	INFO	net.p2p	src/p2p/net_node.inl:1364	0Connect failed to 67.173.161.106:18080
2021-01-09 05:58:43.855	[P2P5]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1645	Synced 81005/2270517 (3%, 2189512 left) (0.093553 sec, 42.756512 blocks/sec), 79.371651 MB queued in 1267 spans, stripe 4 -> 4
2021-01-09 05:58:43.856	[P2P5]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:779	Setting timer on a shut down object
2021-01-09 05:58:48.857	[P2P1]	INFO	net.p2p	src/p2p/net_node.inl:1364	0Connect failed to 50.39.107.154:18080
2021-01-09 05:58:48.860	[SRV_MAIN]	INFO	net.p2p	src/p2p/net_node.inl:1030	net_service loop stopped.
2021-01-09 05:58:48.860	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:80	p2p net loop stopped
2021-01-09 05:58:48.861	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::system_error
2021-01-09 05:58:48.862	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2021-01-09 05:58:48.866	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x10a) [0x5651394593af]:__cxa_throw+0x10a) [0x5651394593af]
2021-01-09 05:58:48.866	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x48d) [0x56513943c021]:_ZN6detail6expect6throw_ESt10error_codePKcS3_j+0x48d) [0x56513943c021]
2021-01-09 05:58:48.867	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x1007) [0x5651394a1f3f]:_ZN10cryptonote3rpc9ZmqServer5serveEv+0x1007) [0x5651394a1f3f]
2021-01-09 05:58:48.867	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x11bcd) [0x7f74453d6bcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7f74453d6bcd]
2021-01-09 05:58:48.867	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x76db) [0x7f74446306db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f74446306db]
2021-01-09 05:58:48.868	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x3f) [0x7f744435971f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f744435971f]
2021-01-09 05:58:48.868	    7f73c4cf2700	INFO	stacktrace	src/common/stack_trace.cpp:172
2021-01-09 05:58:48.871	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:84	Stopping core RPC server...
2021-01-09 05:58:48.872	[SRV_MAIN]	INFO	global	src/daemon/daemon.cpp:227	Node stopped.
2021-01-09 05:58:48.872	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2021-01-09 05:58:48.874	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:90	Deinitializing p2p...
2021-01-09 05:58:48.874	[SRV_MAIN]	INFO	net	src/p2p/net_node.h:427	Killing the net_node
2021-01-09 05:58:48.874	[SRV_MAIN]	INFO	net	src/p2p/net_node.h:431	Joined extra background net_node threads```

# Discussion History
## moneromooo-monero | 2021-01-09T12:45:57+00:00
No sign of why it might have stopped. Are you using this with something like systemd which might have decided to stop it ?

## savager | 2021-01-09T15:24:50+00:00
AHH, default systemd timeout! Thanks.

## moneromooo-monero | 2021-01-09T15:31:44+00:00
systemd annoys one more person... :)

# Action History
- Created by: savager | 2021-01-09T06:10:00+00:00
- Closed at: 2021-01-09T15:31:44+00:00
