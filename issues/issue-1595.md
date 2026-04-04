---
title: Still getting stalling issue with easylogging++
source_url: https://github.com/monero-project/monero/issues/1595
author: ghost
assignees: []
labels: []
created_at: '2017-01-19T23:25:59+00:00'
updated_at: '2017-02-08T02:56:38+00:00'
type: issue
status: closed
closed_at: '2017-02-06T07:54:28+00:00'
---

# Original Description
Ubuntu 16.04, ARMv8, latest build from PR #1585 

```
nodey@odroidc2:~$ monero --detach
2017-01-19 23:07:44.845	      7f987e5000	INFO 	default	contrib/epee/src/mlog.cpp:141	Mew log categories: *:INFO
2017-01-19 23:07:44.846	      7f987e5000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-71ac698)
2017-01-19 23:07:44.847	      7f987e5000	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-19 23:07:44.847	      7f987e5000	INFO 	msgwriter	src/common/scoped_message_writer.h:94	Forking to background...
Forking to background...
nodey@odroidc2:~$ debug
2017-01-19 23:07:46.367	      7f987e5000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-19 23:07:46.367	      7f987e5000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-19 23:07:46.372	      7f987e5000	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-19 23:07:46.373	      7f987e5000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
2017-01-19 23:07:46.375	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-19 23:07:46.375	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-19 23:07:46.375	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-19 23:07:46.375	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-19 23:07:46.377	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-19 23:07:46.387	      7f987e5000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1210026
2017-01-19 23:07:47.854	      7f987e5000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-19 23:07:47.854	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-19 23:07:47.854	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-19 23:07:47.854	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-19 23:07:47.854	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-19 23:07:47.854	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-19 23:07:47.854	      7f987e5000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
^C
nodey@odroidc2:~$ monerod exit
2017-01-19 23:08:09.323	      7fa7857000	INFO 	default	contrib/epee/src/mlog.cpp:141	Mew log categories: *:INFO
^C
nodey@odroidc2:~$ top
```

`debug` is just an alias for `tail -f ~/.bitmonero/monero.log`

Couple of issues: 

1. The daemon stalls after LMDB init. Never starts P2P.
2. `monerod exit` is not exiting. Instead it keeps bouncing to line 141 in `contrib/epee/src/mlog.cpp`
3. Line 1335 in src/wallet/wallet_rpc_server.cpp enforces `mlog_set_log_level(2);` when everywhere else respects the user option - could this explain number 2 and possibly number 1?

My next steps:
1. Merge #1586 and re-test
2. Merge #1586 and #1587 and re-test
3. Custom tweak the log levels as before and re-test
4. Give up and keep running a clean build from before easylogger++ :(


# Discussion History
## ghost | 2017-01-20T00:52:02+00:00
First test: No change with #1586. Never gets to initialising P2P. Log level 2

```
nodey@odroidc2:~$ monero --detach
2017-01-20 00:50:05.227	      7fb0f62000	INFO 	default	contrib/epee/src/mlog.cpp:143	Mew log categories: *:INFO
2017-01-20 00:50:05.229	      7fb0f62000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-71ac698)
2017-01-20 00:50:05.231	      7fb0f62000	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-20 00:50:05.232	      7fb0f62000	INFO 	msgwriter	src/common/scoped_message_writer.h:94	Forking to background...
Forking to background...
nodey@odroidc2:~$ debug
2017-01-20 00:50:06.856	      7fb0f62000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-20 00:50:06.857	      7fb0f62000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-20 00:50:06.864	      7fb0f62000	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-20 00:50:06.865	      7fb0f62000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
2017-01-20 00:50:06.868	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-20 00:50:06.869	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-20 00:50:06.869	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-20 00:50:06.869	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-20 00:50:06.871	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-20 00:50:06.887	      7fb0f62000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1210026
2017-01-20 00:50:08.727	      7fb0f62000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-20 00:50:08.727	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-20 00:50:08.727	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-20 00:50:08.727	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-20 00:50:08.727	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-20 00:50:08.728	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-20 00:50:08.728	      7fb0f62000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
^C
nodey@odroidc2:~$ monerod exit
2017-01-20 00:50:34.084	      7f88358000	INFO 	default	contrib/epee/src/mlog.cpp:143	Mew log categories: *:INFO
^C
```

## ghost | 2017-01-20T01:19:20+00:00
No change with #1586 + #1587. Some extra info via #1587, but core never finishes initialising, and `monerod exit` still doesn't work. Log level 2.

```
nodey@odroidc2:~$ monero --detach
2017-01-20 01:16:59.205	      7f7c43a000	INFO 	default	contrib/epee/src/mlog.cpp:143	Mew log categories: *:INFO
2017-01-20 01:16:59.209	      7f7c43a000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-71ac698)
2017-01-20 01:16:59.210	      7f7c43a000	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-20 01:16:59.210	      7f7c43a000	INFO 	msgwriter	src/common/scoped_message_writer.h:94	Forking to background...
Forking to background...
nodey@odroidc2:~$ debug
2017-01-20 01:17:00.730	      7f7c43a000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-20 01:17:00.730	      7f7c43a000	INFO 	net.p2p	src/p2p/net_node.inl:1668	Set limit-up to 2048 kB/s
2017-01-20 01:17:00.730	      7f7c43a000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-20 01:17:00.730	      7f7c43a000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-20 01:17:00.730	      7f7c43a000	INFO 	net.p2p	src/p2p/net_node.inl:1672	Set limit-down to 8192 kB/s
2017-01-20 01:17:00.739	      7f7c43a000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-01-20 01:17:00.739	      7f7c43a000	INFO 	net.p2p	src/p2p/net_node.inl:525	Binding on 192.168.0.21:18080
2017-01-20 01:17:00.739	      7f7c43a000	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-20 01:17:00.739	      7f7c43a000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-20 01:17:00.739	      7f7c43a000	INFO 	net.p2p	src/p2p/net_node.inl:530	Net service bound to 192.168.0.21:18080
2017-01-20 01:17:01.931	      7f7c43a000	INFO 	net.p2p	src/p2p/net_node.inl:563	Added IGD port mapping.
2017-01-20 01:17:01.932	      7f7c43a000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-20 01:17:01.932	      7f7c43a000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-01-20 01:17:01.932	      7f7c43a000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-01-20 01:17:01.933	      7f7c43a000	WARN 	net.http	contrib/epee/include/net/http_server_impl_base.h:72	Binding on 127.0.0.1:18081
2017-01-20 01:17:01.933	      7f7c43a000	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-20 01:17:01.933	      7f7c43a000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-01-20 01:17:01.934	      7f7c43a000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-20 01:17:01.934	      7f7c43a000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-20 01:17:01.939	      7f7c43a000	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-20 01:17:01.940	      7f7c43a000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
2017-01-20 01:17:01.942	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-20 01:17:01.942	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-20 01:17:01.942	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-20 01:17:01.943	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-20 01:17:01.944	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-20 01:17:01.960	      7f7c43a000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1210026
2017-01-20 01:17:03.414	      7f7c43a000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-20 01:17:03.414	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-20 01:17:03.414	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-20 01:17:03.414	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-20 01:17:03.414	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-20 01:17:03.414	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-20 01:17:03.414	      7f7c43a000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
^C
nodey@odroidc2:~$ monerod exit
2017-01-20 01:17:38.163	      7f92493000	INFO 	default	contrib/epee/src/mlog.cpp:143	Mew log categories: *:INFO
^C
```

## moneromooo-monero | 2017-01-20T18:57:46+00:00
And, again, stack trace needed.

## ghost | 2017-01-20T21:07:40+00:00
Retard-level instructions please? (I'll also add them to the README.md and close that issue)

## moneromooo-monero | 2017-01-21T11:08:08+00:00
gdb /path/to/monerod `pidof monerod`
thread apply all bt


## ghost | 2017-01-22T02:17:54+00:00
@moneromooo-monero I'm afraid your instructions are a little too terse. I've typed them in as you have:

`gdb ~/monero/build/release/bin/monerod` but it won't accept `--debug` 

Then typing `pidof monerod` does nothing.

## ghost | 2017-01-22T02:23:32+00:00
I tried my best and came up with this. Hope it means something :)

```
(gdb) run
Starting program: /home/nodey/monero/build/release/bin/monerod 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
2017-01-22 02:21:19.018	      7fb7fef000	INFO 	default	contrib/epee/src/mlog.cpp:143	Mew log categories: *:INFO
2017-01-22 02:21:19.019	      7fb7fef000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-39aaea8)
2017-01-22 02:21:19.019	      7fb7fef000	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-22 02:21:19.020	      7fb7fef000	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-22 02:21:19.020	      7fb7fef000	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2017-01-22 02:21:19.022	      7fb7fef000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
[New Thread 0x7fb59311e0 (LWP 1070)]
[New Thread 0x7fb51311e0 (LWP 1071)]
[New Thread 0x7fb49311e0 (LWP 1072)]
[New Thread 0x7faffff1e0 (LWP 1073)]
2017-01-22 02:21:19.123	      7faffff1e0	INFO 	net.p2p	src/p2p/net_node.inl:441	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 5
[Thread 0x7faffff1e0 (LWP 1073) exited]
2017-01-22 02:21:19.130	      7fb49311e0	INFO 	net.p2p	src/p2p/net_node.inl:441	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 5
[Thread 0x7fb49311e0 (LWP 1072) exited]
2017-01-22 02:21:19.160	      7fb59311e0	INFO 	net.p2p	src/p2p/net_node.inl:441	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 7
[Thread 0x7fb59311e0 (LWP 1070) exited]
2017-01-22 02:21:19.565	      7fb51311e0	INFO 	net.p2p	src/p2p/net_node.inl:441	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 7
2017-01-22 02:21:19.566	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 104.209.250.32:18080
2017-01-22 02:21:19.567	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 107.150.50.58:18080
2017-01-22 02:21:19.567	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 111.74.67.155:18080
2017-01-22 02:21:19.568	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 169.47.8.204:18080
2017-01-22 02:21:19.568	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 192.241.188.13:18080
2017-01-22 02:21:19.569	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 31.209.59.179:18080
2017-01-22 02:21:19.569	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 45.55.18.61:18080
2017-01-22 02:21:19.569	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 45.56.66.130:18080
2017-01-22 02:21:19.570	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 46.83.25.231:18080
2017-01-22 02:21:19.570	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 59.167.111.178:18080
[Thread 0x7fb51311e0 (LWP 1071) exited]
2017-01-22 02:21:19.571	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 78.94.32.195:18080
2017-01-22 02:21:19.571	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:381	Added seed node: 94.177.227.118:18080
2017-01-22 02:21:19.575	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-22 02:21:19.575	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1640	Set limit-up to 2048 kB/s
2017-01-22 02:21:19.576	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 02:21:19.576	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 02:21:19.576	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1654	Set limit-down to 8192 kB/s
2017-01-22 02:21:19.577	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-22 02:21:19.577	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1676	Set limit-up to 2048 kB/s
2017-01-22 02:21:19.578	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 02:21:19.578	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 02:21:19.578	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1680	Set limit-down to 8192 kB/s
2017-01-22 02:21:19.595	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-01-22 02:21:19.596	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:525	Binding on 192.168.0.21:18080
2017-01-22 02:21:19.597	      7fb7fef000	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-22 02:21:19.597	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 02:21:19.598	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:530	Net service bound to 192.168.0.21:18080
2017-01-22 02:21:20.758	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:563	Added IGD port mapping.
2017-01-22 02:21:20.758	      7fb7fef000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-22 02:21:20.760	      7fb7fef000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-01-22 02:21:20.760	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-01-22 02:21:20.762	      7fb7fef000	WARN 	net.http	contrib/epee/include/net/http_server_impl_base.h:72	Binding on 127.0.0.1:18081
2017-01-22 02:21:20.763	      7fb7fef000	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-22 02:21:20.763	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-01-22 02:21:20.763	      7fb7fef000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-22 02:21:20.764	      7fb7fef000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-22 02:21:20.771	      7fb7fef000	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-22 02:21:20.773	      7fb7fef000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
2017-01-22 02:21:20.777	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 02:21:20.777	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 02:21:20.778	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 02:21:20.778	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 02:21:20.781	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-22 02:21:20.799	      7fb7fef000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1210026
2017-01-22 02:21:22.583	      7fb7fef000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-22 02:21:22.583	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-22 02:21:22.583	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 02:21:22.584	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 02:21:22.584	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 02:21:22.584	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 02:21:22.584	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
[New Thread 0x7faffff1e0 (LWP 1074)]
backtrace
quit
^C
Thread 1 "monerod" received signal SIGINT, Interrupt.
0x0000007fb7fa950c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
(gdb) backtrace
#0  0x0000007fb7fa950c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x0000007fb7fa27f4 in pthread_mutex_lock () from /lib/aarch64-linux-gnu/libpthread.so.0
#2  0x00000000004d198c in std::mutex::lock() ()
#3  0x000000000068c298 in el::base::Writer::initializeLogger(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, bool) [clone .constprop.2218] ()
#4  0x000000000068c6fc in el::base::Writer::construct(int, char const*, ...) [clone .constprop.2217] ()
#5  0x000000000054c5a0 in cryptonote::Blockchain::get_difficulty_for_next_block() ()
#6  0x000000000055a3cc in cryptonote::Blockchain::init(cryptonote::BlockchainDB*, bool, cryptonote::test_options const*) ()
#7  0x00000000005aa83c in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#8  0x0000000000531e08 in daemonize::t_daemon::run(bool) ()
#9  0x00000000005ed45c in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#10 0x00000000004b8778 in main ()
(gdb) 
```

## iDunk5400 | 2017-01-22T09:09:34+00:00
gdb /path/to/monerod \`pidof monerod\`
thread apply all bt

"gdb /path/to/monerod \`pidof monerod\`" is one command (note the backticks)
"thread apply all bt" is what you type into gdb

## moneromooo-monero | 2017-01-22T10:01:56+00:00
Ah, sorry. github parsed the backticks into some style gunk... What a stupid idea for a code related site...

## moneromooo-monero | 2017-01-22T10:03:11+00:00
So, instead of "backtrace", you're supposed to type "thread apply all bt"

## ghost | 2017-01-22T11:33:34+00:00
Ok thanks both of you

## ghost | 2017-01-22T13:46:19+00:00
Ok so building from #1599 fixes this issue. Little annoying that it's not clear why, but I'll roll with it.

Instead getting a new crash, for which I'll open a new issue.

## anonimal | 2017-01-22T14:00:00+00:00
>Ah, sorry. github parsed the backticks into some style gunk... What a stupid idea for a code related site...

Two possible solutions:

#### First (markdown)
\```bash
gdb test \`pidof test\`
\```

produces:

```bash
gdb test `pidof test`
```

#### Second (bash'ism)
Avoid backticks all-together:

gdb test $(pidof test)

-------
Just some thoughts!

## iDunk5400 | 2017-01-22T21:02:11+00:00
**Third**
Escape \`backticks\` with backslashes :)

## ghost | 2017-01-22T21:11:06+00:00
@moneromooo-monero Reopening because it's back again even with the latest set of merges (`daf6662`). Got a log and stack trace:

```
nodey@odroidc2:~$ gdb ~/monero/build/release/bin/monerod `pidof monerod`
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.04) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /home/nodey/monero/build/release/bin/monerod...(no debugging symbols found)...done.
(gdb) run
Starting program: /home/nodey/monero/build/release/bin/monerod 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
2017-01-22 20:23:53.071	      7fb7fef000	INFO 	default	contrib/epee/src/mlog.cpp:148	Mew log categories: *:DEBUG
2017-01-22 20:23:53.072	      7fb7fef000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-daf6662)
2017-01-22 20:23:53.073	      7fb7fef000	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-22 20:23:53.073	      7fb7fef000	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-22 20:23:53.073	      7fb7fef000	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2017-01-22 20:23:53.075	      7fb7fef000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
[New Thread 0x7fb59311e0 (LWP 1356)]
[New Thread 0x7fb51311e0 (LWP 1357)]
[New Thread 0x7fb49311e0 (LWP 1358)]
[New Thread 0x7faffff1e0 (LWP 1359)]
2017-01-22 20:23:53.173	      7fb59311e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 7
[Thread 0x7fb59311e0 (LWP 1356) exited]
2017-01-22 20:23:53.176	      7fb49311e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 1
[Thread 0x7fb49311e0 (LWP 1358) exited]
2017-01-22 20:23:53.178	      7faffff1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 1
[Thread 0x7faffff1e0 (LWP 1359) exited]
2017-01-22 20:23:53.480	      7fb51311e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 7
[Thread 0x7fb51311e0 (LWP 1357) exited]
2017-01-22 20:23:53.481	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 107.150.50.58:18080
2017-01-22 20:23:53.481	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 189.59.130.48:18080
2017-01-22 20:23:53.481	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 50.175.109.159:18080
2017-01-22 20:23:53.482	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 67.227.153.127:18080
2017-01-22 20:23:53.482	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 73.4.151.247:18080
2017-01-22 20:23:53.482	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 77.107.41.222:18080
2017-01-22 20:23:53.482	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 89.203.249.153:18080
2017-01-22 20:23:53.482	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 95.165.51.165:18080
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1694	Set limit-up to 2048 kB/s
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1708	Set limit-down to 8192 kB/s
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1730	Set limit-up to 2048 kB/s
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-22 20:23:53.484	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:1734	Set limit-down to 8192 kB/s
2017-01-22 20:23:53.493	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-01-22 20:23:53.493	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:534	Binding on 192.168.0.21:18080
2017-01-22 20:23:53.494	      7fb7fef000	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-22 20:23:53.494	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-22 20:23:53.494	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:539	Net service bound to 192.168.0.21:18080
2017-01-22 20:23:54.698	      7fb7fef000	INFO 	net.p2p	src/p2p/net_node.inl:572	Added IGD port mapping.
2017-01-22 20:23:54.698	      7fb7fef000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-22 20:23:54.699	      7fb7fef000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-01-22 20:23:54.699	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-01-22 20:23:54.699	      7fb7fef000	WARN 	net.http	contrib/epee/include/net/http_server_impl_base.h:72	Binding on 127.0.0.1:18081
2017-01-22 20:23:54.700	      7fb7fef000	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-22 20:23:54.700	      7fb7fef000	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
2017-01-22 20:23:54.700	      7fb7fef000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-22 20:23:54.700	      7fb7fef000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-22 20:23:54.705	      7fb7fef000	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-22 20:23:54.706	      7fb7fef000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
2017-01-22 20:23:54.709	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 20:23:54.709	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 20:23:54.709	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 20:23:54.709	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 20:23:54.710	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
2017-01-22 20:23:54.727	      7fb7fef000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1210026
2017-01-22 20:23:56.183	      7fb7fef000	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-22 20:23:56.183	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-22 20:23:56.183	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-22 20:23:56.183	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      9464995840
2017-01-22 20:23:56.184	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6641131520
2017-01-22 20:23:56.184	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-22 20:23:56.184	      7fb7fef000	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5877  Percent threshold: 0.8000
[New Thread 0x7faffff1e0 (LWP 1360)]
^C
Thread 1 "monerod" received signal SIGINT, Interrupt.
0x0000007fb7fa950c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
(gdb) thread apply all bt

Thread 6 (Thread 0x7faffff1e0 (LWP 1360)):
#0  0x0000007fb7fa630c in pthread_cond_wait@@GLIBC_2.17 () from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x000000000063377c in boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1344] ()
#2  0x000000000054ef98 in boost::asio::io_service::run() ()
#3  0x0000007fb7ab7cf8 in ?? () from /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0
#4  0x0000007fb7f9ffc4 in start_thread () from /lib/aarch64-linux-gnu/libpthread.so.0
#5  0x0000007fb7f18110 in ?? () from /lib/aarch64-linux-gnu/libc.so.6

Thread 1 (Thread 0x7fb7fef000 (LWP 1353)):
#0  0x0000007fb7fa950c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x0000007fb7fa27f4 in pthread_mutex_lock () from /lib/aarch64-linux-gnu/libpthread.so.0
#2  0x00000000004d19fc in std::mutex::lock() ()
#3  0x000000000068e7b8 in el::base::Writer::initializeLogger(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, bool) [clone .constprop.2220] ()
#4  0x000000000068ec1c in el::base::Writer::construct(int, char const*, ...) [clone .constprop.2219] ()
#5  0x000000000054e0b8 in cryptonote::Blockchain::get_difficulty_for_next_block() ()
#6  0x000000000055bebc in cryptonote::Blockchain::init(cryptonote::BlockchainDB*, bool, cryptonote::test_options const*) ()
#7  0x000000000059fed4 in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#8  0x00000000004fe048 in daemonize::t_daemon::run(bool) ()
#9  0x00000000005efad4 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#10 0x00000000004b8820 in main ()
(gdb) 
```

## moneromooo-monero | 2017-01-23T08:57:33+00:00
Do you have other threads ? They might be in some logging stuff too.

## ghost | 2017-01-23T22:04:05+00:00
How do I get other threads?

I've now built from #1622 `ad91ffe` and am now seeing the stall at an earlier stage. Have got the following stack trace with gdb:

```
nodey@odroidc2:~$ monero
2017-01-23 21:55:13.498	      7f8fac1000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-ad91ffe)
Forking to background...
nodey@odroidc2:~$ debug
2017-01-23 21:55:13.498	      7f8fac1000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-ad91ffe)
2017-01-23 21:55:13.502	      7f8fac1000	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-23 21:55:13.502	      7f8fac1000	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2017-01-23 21:55:13.503	      7f8fac1000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-01-23 21:55:15.089	      7f8fac1000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-23 21:55:15.089	      7f8fac1000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-01-23 21:55:15.090	      7f8fac1000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-23 21:55:15.090	      7f8fac1000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-23 21:55:15.110	      7f8fac1000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
^C
nodey@odroidc2:~$ monerod exit
^C
nodey@odroidc2:~$ debug
2017-01-23 21:55:13.498	      7f8fac1000	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-ad91ffe)
2017-01-23 21:55:13.502	      7f8fac1000	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-23 21:55:13.502	      7f8fac1000	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2017-01-23 21:55:13.503	      7f8fac1000	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-01-23 21:55:15.089	      7f8fac1000	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-23 21:55:15.089	      7f8fac1000	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-01-23 21:55:15.090	      7f8fac1000	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-23 21:55:15.090	      7f8fac1000	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-23 21:55:15.110	      7f8fac1000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
^C
nodey@odroidc2:~$ htop
nodey@odroidc2:~$ gdb ~/monero/build/release/bin/monerod `pidof monerod`
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.04) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "aarch64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /home/nodey/monero/build/release/bin/monerod...(no debugging symbols found)...done.
Attaching to program: /home/nodey/monero/build/release/bin/monerod, process 4693
[New LWP 4699]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
0x0000007f8fa7a50c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
(gdb) thread apply all bt

Thread 2 (Thread 0x7f8bc821e0 (LWP 4699)):
#0  0x0000007f8fa7730c in pthread_cond_wait@@GLIBC_2.17 () from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x000000000063c1a4 in boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] ()
#2  0x000000000054e9f8 in boost::asio::io_service::run() ()
#3  0x0000007f8f5edcf8 in ?? () from /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0
#4  0x0000007f8fa70fc4 in start_thread () from /lib/aarch64-linux-gnu/libpthread.so.0
#5  0x0000007f8f9e9110 in ?? () from /lib/aarch64-linux-gnu/libc.so.6

Thread 1 (Thread 0x7f8fac1000 (LWP 4693)):
#0  0x0000007f8fa7a50c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x0000007f8fa737f4 in pthread_mutex_lock () from /lib/aarch64-linux-gnu/libpthread.so.0
#2  0x00000000004d1be4 in std::mutex::lock() ()
#3  0x000000000068d578 in el::base::Writer::initializeLogger(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, bool) [clone .constprop.2215] ()
#4  0x000000000068d9dc in el::base::Writer::construct(int, char const*, ...) [clone .constprop.2214] ()
#5  0x000000000054db18 in cryptonote::Blockchain::get_difficulty_for_next_block() ()
#6  0x000000000055b904 in cryptonote::Blockchain::init(cryptonote::BlockchainDB*, bool, cryptonote::test_options const*) ()
#7  0x000000000058dd3c in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#8  0x00000000004fdaa8 in daemonize::t_daemon::run(bool) ()
#9  0x00000000004b8470 in main ()
(gdb) 
```

I wonder whether `get_difficulty_for_next_block()` is the culprit here...possibly using `__func__` rather than `__FUNCTION__`?

## moneromooo-monero | 2017-01-23T23:11:10+00:00
In void initializeLogger(const std::string& loggerId, bool lookup = true, bool needLock = true) {, there seems to be a lock taken in the else branch, and not released. Try adding:
                    if (needLock) m_logger->releaseLock();  
after:
                        m_proceed = m_logger->enabled(m_level);
                    }


No idea whether that's a good patch though, I'm curious to see if you get crashes (due to unlocking too much) after that.

## moneromooo-monero | 2017-01-23T23:11:57+00:00
And no, __func__ and __FUNCTION__ are interchangeable for the purposes of deadlock.

## ghost | 2017-01-24T12:23:06+00:00
Will test

## ghost | 2017-01-24T21:29:41+00:00
Afraid that hasn't produced any change. Still appears to be locking in exactly the same place. Backtrace looks the same as well.

```
Reading symbols from /home/nodey/monero/build/release/bin/monerod...(no debugging symbols found)...done.
Attaching to program: /home/nodey/monero/build/release/bin/monerod, process 2209
[New LWP 2215]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
0x0000007f7bb4350c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
(gdb) thread apply all bt

Thread 2 (Thread 0x7f77d4b1e0 (LWP 2215)):
#0  0x0000007f7bb4030c in pthread_cond_wait@@GLIBC_2.17 () from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x000000000063c1a4 in boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] ()
#2  0x000000000054e9f8 in boost::asio::io_service::run() ()
#3  0x0000007f7b6b6cf8 in ?? () from /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0
#4  0x0000007f7bb39fc4 in start_thread () from /lib/aarch64-linux-gnu/libpthread.so.0
#5  0x0000007f7bab2110 in ?? () from /lib/aarch64-linux-gnu/libc.so.6

Thread 1 (Thread 0x7f7bb8a000 (LWP 2209)):
#0  0x0000007f7bb4350c in __lll_lock_wait () from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x0000007f7bb3c7f4 in pthread_mutex_lock () from /lib/aarch64-linux-gnu/libpthread.so.0
#2  0x00000000004d1be4 in std::mutex::lock() ()
#3  0x000000000068d578 in el::base::Writer::initializeLogger(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, bool) [clone .constprop.2215] ()
#4  0x000000000068d9ec in el::base::Writer::construct(int, char const*, ...) [clone .constprop.2214] ()
#5  0x000000000054db18 in cryptonote::Blockchain::get_difficulty_for_next_block() ()
#6  0x000000000055b904 in cryptonote::Blockchain::init(cryptonote::BlockchainDB*, bool, cryptonote::test_options const*) ()
#7  0x000000000058dd3c in cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) ()
#8  0x00000000004fdaa8 in daemonize::t_daemon::run(bool) ()
#9  0x00000000004b8470 in main ()
(gdb) 
```

## ghost | 2017-01-24T23:40:48+00:00
@moneromooo-monero Any chance it's as simple as a type mismatch between `__func__` (a `const char*`) and what easylogger's function is expecting?

http://stackoverflow.com/questions/5065091/cwhat-is-the-type-of-the-file-macro

## moneromooo-monero | 2017-01-24T23:40:51+00:00
Describe exactly the command line(s) you are using. Since you usually run a daemon with --detach, you probably hit different code paths.

## moneromooo-monero | 2017-01-24T23:43:48+00:00
Explain the idea which made you say "Any chance it's as simple as a type mismatch between __func__ (const char*) and what easylogger's function is expecting?". Where, and why do you think a type difference might make a difference ? __func__ should be a const char* I think, same as __FUNCTION__. Describe what function you think is expecting another type.

## moneromooo-monero | 2017-01-24T23:47:08+00:00
Do you use GCC or CLANG ?

## vtnerd | 2017-01-24T23:47:30+00:00
Can you run this in valgrind? Just `apt-get install valgrind`, then run `valgrind <app command>`. I suspect uninitialized memory being the culprit here.

## ghost | 2017-01-24T23:53:36+00:00
I use gcc (Ubuntu/Linaro 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609

Well the easylogger++.h code is quite dense and packed with precompiler stuff which I don't understand. So I'm trying to follow through where usage of LOG_PRINT_L3 (which is the only one that gets passed `__file__`) and other log levels might differ. 

I know you've defined LOG_PRINT_L3 to be MTRACE so it makes *absolutely no sense* to me that switching out all LOG_PRINT_L3's in `/cryptonote_core/blockchain.cpp` for MDEBUG suddenly makes it work.

Now I'm just finishing a compile (takes about 90 minutes here) with all LOG_PRINT_L3's replaced by MTRACE and will report back in a sec.

@vtnerd Will try shortly - thanks!

Right, have just tested my `MTRACE` build:

LOG_PRINT_L3 - stalls
MTRACE - stalls
MDEBUG - runs

Why are MTRACE and MDEBUG behaving differently when passed `__func__`?

Now testing with valgrind.

@moneromooo-monero my config file (bitmonero.conf) reads as follows:

```
log-file=./monero.log
log-level=2
p2p-bind-ip=192.168.0.21 
p2p-bind-port=18080
max-concurrency=1
out-peers=64
```

Note this happens with log-level=0 or 2
 

## ghost | 2017-01-25T01:21:50+00:00
@vtnerd First run with valgrind below. Annoyingly it's not even reaching the stall point due to a crash (?) with upnpdiscover. Or maybe it is... o_O Will repeat with my working build (MDEBUG) tomorrow.

```
nodey@odroidc2:~$ valgrind ~/monero/build/release/bin/monerod --detach
==1535== Memcheck, a memory error detector
==1535== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==1535== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==1535== Command: /home/nodey/monero/build/release/bin/monerod --detach
==1535== 
2017-01-25 01:18:20.215	         6e74830	INFO 	default	contrib/epee/src/mlog.cpp:148	Mew log categories: *:DEBUG
2017-01-25 01:18:20.371	         6e74830	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-8d8f3bb)
2017-01-25 01:18:20.386	         6e74830	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-25 01:18:20.400	         6e74830	INFO 	msgwriter	src/common/scoped_message_writer.h:94	Forking to background...
Forking to background...
==1537== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1537==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1537==    by 0x4E5E6B: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x50801F: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x5013B3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x5EEBCF: daemonize::t_executor::create_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x4B8463: main (in /home/nodey/monero/build/release/bin/monerod)
==1537==  Address 0xffefff454 is on thread 1's stack
==1537==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1537== 
==1537== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1537==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1537==    by 0x4E5EAF: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x50801F: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x5013B3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x5EEBCF: daemonize::t_executor::create_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x4B8463: main (in /home/nodey/monero/build/release/bin/monerod)
==1537==  Address 0xffefff454 is on thread 1's stack
==1537==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1537== 
==1535== 
==1535== HEAP SUMMARY:
==1535==     in use at exit: 104,550 bytes in 442 blocks
==1535==   total heap usage: 4,183 allocs, 3,741 frees, 351,728 bytes allocated
==1535== 
==1536== 
==1536== HEAP SUMMARY:
==1536==     in use at exit: 104,550 bytes in 442 blocks
==1536==   total heap usage: 4,183 allocs, 3,741 frees, 351,728 bytes allocated
==1536== 
==1535== LEAK SUMMARY:
==1535==    definitely lost: 0 bytes in 0 blocks
==1535==    indirectly lost: 0 bytes in 0 blocks
==1535==      possibly lost: 0 bytes in 0 blocks
==1535==    still reachable: 104,550 bytes in 442 blocks
==1535==         suppressed: 0 bytes in 0 blocks
==1535== Rerun with --leak-check=full to see details of leaked memory
==1535== 
==1535== For counts of detected and suppressed errors, rerun with: -v
==1535== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
nodey@odroidc2:~$ ==1536== LEAK SUMMARY:
==1536==    definitely lost: 0 bytes in 0 blocks
==1536==    indirectly lost: 0 bytes in 0 blocks
==1536==      possibly lost: 0 bytes in 0 blocks
==1536==    still reachable: 104,550 bytes in 442 blocks
==1536==         suppressed: 0 bytes in 0 blocks
==1536== Rerun with --leak-check=full to see details of leaked memory
==1536== 
==1536== For counts of detected and suppressed errors, rerun with: -v
==1536== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
==1537== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1537==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1537==    by 0x4EA57F: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x4F514B: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x645A13: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x50169B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x5EEBCF: daemonize::t_executor::create_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x4B8463: main (in /home/nodey/monero/build/release/bin/monerod)
==1537==  Address 0xffeffe0b4 is on thread 1's stack
==1537==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1537== 
==1537== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1537==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1537==    by 0x66DEF7: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x4CE783: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x4F541F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x645A13: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x50169B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x5EEBCF: daemonize::t_executor::create_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1537==    by 0x4B8463: main (in /home/nodey/monero/build/release/bin/monerod)
==1537==  Address 0xffeffe054 is on thread 1's stack
==1537==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1537== 
ARM64 front end: load_store
disInstr(arm64): unhandled instruction 0x695157BA
disInstr(arm64): 0110'1001 0101'0001 0101'0111 1011'1010
==1537== valgrind: Unrecognised instruction at address 0x4c384d4.
==1537==    at 0x4C384D4: upnpDiscover (in /usr/lib/aarch64-linux-gnu/libminiupnpc.so.10)
==1537== Your program just tried to execute an instruction that Valgrind
==1537== did not recognise.  There are two possible reasons for this.
==1537== 1. Your program has a bug and erroneously jumped to a non-code
==1537==    location.  If you are running Memcheck and you just saw a
==1537==    warning about a bad jump, it's probably your program's fault.
==1537== 2. The instruction is legitimate but Valgrind doesn't handle it,
==1537==    i.e. it's Valgrind's fault.  If you think this is the case or
==1537==    you are not sure, please let us know and we'll try to fix it.
==1537== Either way, Valgrind will now raise a SIGILL signal which will
==1537== probably kill your program.
==1537== 
==1537== Process terminating with default action of signal 4 (SIGILL)
==1537==  Illegal opcode at address 0x4C384D4
==1537==    at 0x4C384D4: upnpDiscover (in /usr/lib/aarch64-linux-gnu/libminiupnpc.so.10)
==1537== 
==1537== HEAP SUMMARY:
==1537==     in use at exit: 8,300,646 bytes in 6,997 blocks
==1537==   total heap usage: 14,145 allocs, 7,148 frees, 13,593,449 bytes allocated
==1537== 
==1537== LEAK SUMMARY:
==1537==    definitely lost: 64 bytes in 4 blocks
==1537==    indirectly lost: 0 bytes in 0 blocks
==1537==      possibly lost: 263,268 bytes in 3,648 blocks
==1537==    still reachable: 8,037,314 bytes in 3,345 blocks
==1537==                       of which reachable via heuristic:
==1537==                         multipleinheritance: 4,368 bytes in 6 blocks
==1537==         suppressed: 0 bytes in 0 blocks
==1537== Rerun with --leak-check=full to see details of leaked memory
==1537== 
==1537== For counts of detected and suppressed errors, rerun with: -v
==1537== Use --track-origins=yes to see where uninitialised values come from
==1537== ERROR SUMMARY: 4 errors from 4 contexts (suppressed: 0 from 0)
```

## vtnerd | 2017-01-25T02:07:01+00:00
Previously you were not using the `--detach` option, can you do the same with valgrind?

## ghost | 2017-01-25T09:27:45+00:00
I'll try without detach but actually, I always use --detach, 'monero' on my command line is an alias for 'monerod --detach'. Apologies for the confusion. 

## moneromooo-monero | 2017-01-25T09:53:38+00:00
You might be able to bypass that error with --no-igd.

## ghost | 2017-01-25T10:41:40+00:00
Thanks - will try it

## ghost | 2017-01-25T22:35:46+00:00
Val grind with --no-igd but not --detach. Still stops at the same place. Hope this gives a bit more info.

```
nodey@odroidc2:~$ valgrind ~/monero/build/release/bin/monerod --no-igd
==1487== Memcheck, a memory error detector
==1487== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==1487== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==1487== Command: /home/nodey/monero/build/release/bin/monerod --no-igd
==1487== 
2017-01-25 22:33:41.499	         6e74830	INFO 	default	contrib/epee/src/mlog.cpp:148	Mew log categories: *:DEBUG
2017-01-25 22:33:41.661	         6e74830	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-8d8f3bb)
2017-01-25 22:33:41.675	         6e74830	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-25 22:33:41.680	         6e74830	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-25 22:33:41.683	         6e74830	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
==1487== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1487==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1487==    by 0x4E5E6B: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x50801F: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5013B3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5EEC9F: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1487==  Address 0xffefff464 is on thread 1's stack
==1487==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1487== 
==1487== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1487==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1487==    by 0x4E5EAF: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x50801F: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x6610AF: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5013B3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5EEC9F: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1487==  Address 0xffefff464 is on thread 1's stack
==1487==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1487== 
2017-01-25 22:33:41.774	         6e74830	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-01-25 22:33:44.074	         8a7d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 5
2017-01-25 22:33:44.112	         927d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 5
2017-01-25 22:33:44.156	         7a7d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 45
2017-01-25 22:33:44.254	         827d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 45
2017-01-25 22:33:44.306	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 103.195.4.216:18080
2017-01-25 22:33:44.323	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 104.136.43.125:18080
2017-01-25 22:33:44.325	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 104.4.81.66:18080
2017-01-25 22:33:44.329	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 107.150.50.58:18080
2017-01-25 22:33:44.331	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 107.2.145.214:18080
2017-01-25 22:33:44.333	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 109.111.78.107:18080
2017-01-25 22:33:44.335	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 114.215.106.22:18080
2017-01-25 22:33:44.337	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 118.148.120.23:18080
2017-01-25 22:33:44.339	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 119.46.113.253:18080
2017-01-25 22:33:44.342	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 120.27.36.164:18080
2017-01-25 22:33:44.344	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 123.206.43.17:18080
2017-01-25 22:33:44.346	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 124.171.83.133:18080
2017-01-25 22:33:44.348	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 128.199.179.100:18080
2017-01-25 22:33:44.350	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 137.74.1.223:18080
2017-01-25 22:33:44.352	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 138.68.29.3:18080
2017-01-25 22:33:44.355	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 160.16.122.177:18080
2017-01-25 22:33:44.357	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 163.172.76.47:18080
2017-01-25 22:33:44.359	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 173.168.81.122:18080
2017-01-25 22:33:44.361	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 173.214.160.97:18080
2017-01-25 22:33:44.367	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 173.247.232.234:18080
2017-01-25 22:33:44.370	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 188.116.170.69:18080
2017-01-25 22:33:44.372	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 192.99.33.78:18080
2017-01-25 22:33:44.374	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 198.27.64.122:18080
2017-01-25 22:33:44.376	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 202.159.133.15:18080
2017-01-25 22:33:44.378	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 216.189.155.205:18080
2017-01-25 22:33:44.381	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 220.175.222.155:18080
2017-01-25 22:33:44.383	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 223.223.176.56:18080
2017-01-25 22:33:44.385	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 24.62.107.19:18080
2017-01-25 22:33:44.387	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 37.59.21.58:18080
2017-01-25 22:33:44.389	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 37.59.53.25:18080
2017-01-25 22:33:44.391	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 45.46.85.168:18080
2017-01-25 22:33:44.393	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 45.55.18.61:18080
2017-01-25 22:33:44.396	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 5.1.91.108:18080
2017-01-25 22:33:44.398	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 50.157.173.168:18080
2017-01-25 22:33:44.400	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 50.183.55.164:18080
2017-01-25 22:33:44.402	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 54.91.73.59:18080
2017-01-25 22:33:44.404	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 59.167.111.178:18080
2017-01-25 22:33:44.406	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 64.137.185.205:18080
2017-01-25 22:33:44.408	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 69.145.243.210:18080
2017-01-25 22:33:44.411	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 73.176.170.180:18080
2017-01-25 22:33:44.413	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 75.161.57.25:18080
2017-01-25 22:33:44.415	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 76.100.210.173:18080
2017-01-25 22:33:44.417	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 79.113.158.142:18080
2017-01-25 22:33:44.419	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 79.119.184.102:18080
2017-01-25 22:33:44.421	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 88.99.37.213:18080
2017-01-25 22:33:44.424	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 93.81.9.135:18080
2017-01-25 22:33:44.426	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 94.177.227.118:18080
2017-01-25 22:33:44.428	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 94.246.96.27:18080
2017-01-25 22:33:44.430	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 96.242.116.51:18080
2017-01-25 22:33:44.432	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 98.207.130.174:18080
2017-01-25 22:33:44.519	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-25 22:33:44.531	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1694	Set limit-up to 2048 kB/s
2017-01-25 22:33:44.537	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:33:44.546	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:33:44.550	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1708	Set limit-down to 8192 kB/s
2017-01-25 22:33:44.552	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-25 22:33:44.556	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1730	Set limit-up to 2048 kB/s
2017-01-25 22:33:44.558	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:33:44.561	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:33:44.565	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1734	Set limit-down to 8192 kB/s
2017-01-25 22:33:45.071	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-01-25 22:33:45.075	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:534	Binding on 192.168.0.21:18080
==1487== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1487==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1487==    by 0x4EA57F: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4F514B: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x645A13: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x50169B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5EEC9F: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1487==  Address 0xffeffe0c4 is on thread 1's stack
==1487==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1487== 
2017-01-25 22:33:45.123	         6e74830	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-25 22:33:45.132	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
==1487== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1487==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1487==    by 0x66DEF7: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4CE783: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4F541F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x645A13: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x50169B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5EEC9F: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1487==  Address 0xffeffe064 is on thread 1's stack
==1487==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1487== 
2017-01-25 22:33:45.151	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:539	Net service bound to 192.168.0.21:18080
2017-01-25 22:33:45.157	         6e74830	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-25 22:33:45.167	         6e74830	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-01-25 22:33:45.172	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-01-25 22:33:45.188	         6e74830	WARN 	net.http	contrib/epee/include/net/http_server_impl_base.h:72	Binding on 127.0.0.1:18081
==1487== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1487==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1487==    by 0x4EA57F: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x55DFFB: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5017F7: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5EEC9F: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1487==  Address 0xffefff2b4 is on thread 1's stack
==1487==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1487== 
2017-01-25 22:33:45.201	         6e74830	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-25 22:33:45.212	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
==1487== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1487==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1487==    by 0x66DEF7: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4CE783: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x64BDA7: void boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::async_accept<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> > >(boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::implementation_type&, boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp>*, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >&) [clone .constprop.885] (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x55E2D7: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5017F7: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x5EEC9F: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1487==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1487==  Address 0xffefff1d4 is on thread 1's stack
==1487==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1487== 
2017-01-25 22:33:45.225	         6e74830	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-25 22:33:45.236	         6e74830	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-25 22:33:45.954	         6e74830	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-25 22:33:45.977	         6e74830	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
==1487== Warning: set address range perms: large range [0x3939c000, 0x3f939c000) (defined)
2017-01-25 22:33:46.075	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     16106127360
2017-01-25 22:33:46.079	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      10074075136
2017-01-25 22:33:46.082	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 6032052224
2017-01-25 22:33:46.085	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-25 22:33:46.147	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.6255  Percent threshold: 0.8000
2017-01-25 22:33:46.161	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:492	Threshold met (percent-based)
2017-01-25 22:33:46.165	         6e74830	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1094	LMDB memory map needs to be resized, doing that now.
==1487== Warning: set address range perms: large range [0x3939c000, 0x3f939c000) (noaccess)
==1487== Warning: set address range perms: large range [0x3939c000, 0x43939c000) (defined)
2017-01-25 22:33:46.202	         6e74830	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:444	LMDB Mapsize increased.  Old: 15360MiB, New: 16384MiB
2017-01-25 22:33:46.457	         6e74830	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1220141
2017-01-25 22:33:58.269	         6e74830	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-25 22:33:58.288	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-25 22:33:58.290	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     17179869184
2017-01-25 22:33:58.292	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      10074075136
2017-01-25 22:33:58.293	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 7105794048
2017-01-25 22:33:58.295	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-25 22:33:58.297	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5864  Percent threshold: 0.8000

```

## ghost | 2017-01-25T22:45:06+00:00
And valgrind on the working build (MDEBUG instead of LOG_PRINT_L3):

```
nodey@odroidc2:~$ valgrind ~/monero/build/release/bin/monerod --no-igd
==1632== Memcheck, a memory error detector
==1632== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==1632== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==1632== Command: /home/nodey/monero/build/release/bin/monerod --no-igd
==1632== 
2017-01-25 22:43:13.401	         6e74830	INFO 	default	contrib/epee/src/mlog.cpp:148	Mew log categories: *:DEBUG
2017-01-25 22:43:13.557	         6e74830	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-daf6662)
2017-01-25 22:43:13.572	         6e74830	INFO 	daemon	src/daemon/main.cpp:267	Moving from main() into the daemonize now.
2017-01-25 22:43:13.577	         6e74830	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-25 22:43:13.579	         6e74830	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x4F49B3: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x65CED7: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x5061D7: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x65CED7: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4EF31B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x625E47: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4BBC23: main (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xffefff464 is on thread 1's stack
==1632==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1632== 
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x4F49F7: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x65CED7: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x5061D7: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x65CED7: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4EF31B: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x625E47: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4BBC23: main (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xffefff464 is on thread 1's stack
==1632==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1632== 
2017-01-25 22:43:13.657	         6e74830	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-01-25 22:43:15.854	         7a7d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 45
2017-01-25 22:43:15.976	         927d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 5
2017-01-25 22:43:16.066	         8a7d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 5
2017-01-25 22:43:16.073	         827d1e0	INFO 	net.p2p	src/p2p/net_node.inl:450	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 45
2017-01-25 22:43:16.127	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 103.195.4.216:18080
2017-01-25 22:43:16.144	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 104.136.43.125:18080
2017-01-25 22:43:16.147	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 104.4.81.66:18080
2017-01-25 22:43:16.150	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 107.150.50.58:18080
2017-01-25 22:43:16.152	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 107.2.145.214:18080
2017-01-25 22:43:16.155	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 109.111.78.107:18080
2017-01-25 22:43:16.157	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 114.215.106.22:18080
2017-01-25 22:43:16.159	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 118.148.120.23:18080
2017-01-25 22:43:16.161	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 119.46.113.253:18080
2017-01-25 22:43:16.163	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 120.27.36.164:18080
2017-01-25 22:43:16.166	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 123.206.43.17:18080
2017-01-25 22:43:16.168	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 124.171.83.133:18080
2017-01-25 22:43:16.170	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 128.199.179.100:18080
2017-01-25 22:43:16.172	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 137.74.1.223:18080
2017-01-25 22:43:16.175	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 138.68.29.3:18080
2017-01-25 22:43:16.177	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 160.16.122.177:18080
2017-01-25 22:43:16.179	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 163.172.76.47:18080
2017-01-25 22:43:16.181	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 173.168.81.122:18080
2017-01-25 22:43:16.184	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 173.214.160.97:18080
2017-01-25 22:43:16.186	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 173.247.232.234:18080
2017-01-25 22:43:16.188	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 188.116.170.69:18080
2017-01-25 22:43:16.190	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 192.99.33.78:18080
2017-01-25 22:43:16.192	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 198.27.64.122:18080
2017-01-25 22:43:16.195	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 202.159.133.15:18080
2017-01-25 22:43:16.197	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 216.189.155.205:18080
2017-01-25 22:43:16.199	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 220.175.222.155:18080
2017-01-25 22:43:16.201	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 223.223.176.56:18080
2017-01-25 22:43:16.204	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 24.62.107.19:18080
2017-01-25 22:43:16.206	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 37.59.21.58:18080
2017-01-25 22:43:16.208	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 37.59.53.25:18080
2017-01-25 22:43:16.210	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 45.46.85.168:18080
2017-01-25 22:43:16.212	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 45.55.18.61:18080
2017-01-25 22:43:16.215	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 5.1.91.108:18080
2017-01-25 22:43:16.217	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 50.157.173.168:18080
2017-01-25 22:43:16.219	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 50.183.55.164:18080
2017-01-25 22:43:16.221	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 54.91.73.59:18080
2017-01-25 22:43:16.223	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 59.167.111.178:18080
2017-01-25 22:43:16.226	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 64.137.185.205:18080
2017-01-25 22:43:16.228	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 69.145.243.210:18080
2017-01-25 22:43:16.230	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 73.176.170.180:18080
2017-01-25 22:43:16.232	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 75.161.57.25:18080
2017-01-25 22:43:16.235	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 76.100.210.173:18080
2017-01-25 22:43:16.237	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 79.113.158.142:18080
2017-01-25 22:43:16.239	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 79.119.184.102:18080
2017-01-25 22:43:16.241	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 88.99.37.213:18080
2017-01-25 22:43:16.243	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 93.81.9.135:18080
2017-01-25 22:43:16.246	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 94.177.227.118:18080
2017-01-25 22:43:16.248	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 94.246.96.27:18080
2017-01-25 22:43:16.250	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 96.242.116.51:18080
2017-01-25 22:43:16.252	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 98.207.130.174:18080
2017-01-25 22:43:16.343	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-25 22:43:16.356	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1694	Set limit-up to 2048 kB/s
2017-01-25 22:43:16.361	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:43:16.366	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:43:16.370	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1708	Set limit-down to 8192 kB/s
2017-01-25 22:43:16.373	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 4.40402e+06 kbps
2017-01-25 22:43:16.377	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1730	Set limit-up to 2048 kB/s
2017-01-25 22:43:16.380	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:43:16.382	         6e74830	INFO 	net.throttle	src/p2p/network_throttle-detail.cpp:163	Setting LIMIT: 8.38861e+06 kbps
2017-01-25 22:43:16.386	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:1734	Set limit-down to 8192 kB/s
2017-01-25 22:43:16.888	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 2 from name: P2P, prefix_name = P2P
2017-01-25 22:43:16.892	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:534	Binding on 192.168.0.21:18080
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x4F7ADF: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x502C23: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x6415CB: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4EF603: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x625E47: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4BBC23: main (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xffeffe0c4 is on thread 1's stack
==1632==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1632== 
2017-01-25 22:43:16.940	         6e74830	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-25 22:43:16.949	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x669D2F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CCF4B: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x502EF7: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x6415CB: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4EF603: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x625E47: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4BBC23: main (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xffeffe064 is on thread 1's stack
==1632==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1632== 
2017-01-25 22:43:16.969	         6e74830	INFO 	net.p2p	src/p2p/net_node.inl:539	Net service bound to 192.168.0.21:18080
2017-01-25 22:43:16.974	         6e74830	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-25 22:43:16.983	         6e74830	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-01-25 22:43:16.989	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:794	Set server type to: 1 from name: RPC, prefix_name = RPC
2017-01-25 22:43:17.004	         6e74830	WARN 	net.http	contrib/epee/include/net/http_server_impl_base.h:72	Binding on 127.0.0.1:18081
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x4F7ADF: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x577D4B: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4EF75F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x625E47: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4BBC23: main (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xffefff2b4 is on thread 1's stack
==1632==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1632== 
2017-01-25 22:43:17.018	         6e74830	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-01-25 22:43:17.029	         6e74830	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=1
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x669D2F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CCF4B: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x647C77: void boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::async_accept<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> > >(boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::implementation_type&, boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp>*, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >&) [clone .constprop.885] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x578027: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4EF75F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x625E47: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4BBC23: main (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xffefff1d4 is on thread 1's stack
==1632==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1632== 
2017-01-25 22:43:17.042	         6e74830	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-25 22:43:17.053	         6e74830	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-25 22:43:17.162	         6e74830	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:233	Locking /home/nodey/.bitmonero/.daemon_lock
2017-01-25 22:43:17.186	         6e74830	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
==1632== Warning: set address range perms: large range [0x3939c000, 0x43939c000) (defined)
2017-01-25 22:43:17.280	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     17179869184
2017-01-25 22:43:17.283	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      10074075136
2017-01-25 22:43:17.287	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 7105794048
2017-01-25 22:43:17.290	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-25 22:43:17.353	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5864  Percent threshold: 0.8000
2017-01-25 22:43:17.609	         6e74830	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:197	reorganizing from 1220141
2017-01-25 22:43:25.561	         6e74830	INFO 	hardfork	src/cryptonote_core/hardfork.cpp:206	reorganization done
2017-01-25 22:43:25.580	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-25 22:43:25.582	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     17179869184
2017-01-25 22:43:25.583	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      10074075136
2017-01-25 22:43:25.585	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 7105794048
2017-01-25 22:43:25.587	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-25 22:43:25.589	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5864  Percent threshold: 0.8000
2017-01-25 22:43:26.138	         6e74830	INFO 	blockchain	src/cryptonote_core/blockchain.cpp:380	Blockchain initialized. last block: 1230219, d2.h4.m13.s54 time ago, current difficulty: 5779284003
==1632== Conditional jump or move depends on uninitialised value(s)
==1632==    at 0x62F470: cryptonote::core::update_checkpoints() [clone .part.127] [clone .constprop.953] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x5C7ECF: cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4EBA0F: daemonize::t_daemon::run(bool) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x625E53: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4BBC23: main (in /home/nodey/monero/build/release/bin/monerod)
==1632== 
2017-01-25 22:43:26.187	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:204	Blockchain checkpoints file not found
2017-01-25 22:43:27.589	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-25 22:43:27.591	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     17179869184
2017-01-25 22:43:27.593	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      10074075136
2017-01-25 22:43:27.595	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 7105794048
2017-01-25 22:43:27.597	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-25 22:43:27.599	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5864  Percent threshold: 0.8000
2017-01-25 22:43:27.612	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 233000 <4f69bec2af6c0852412bdd10c19e6af10c8d738fe2618b5511a98efd03ab477e>
2017-01-25 22:43:27.617	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 250000 <f59d31839bd909ec8830b4f7f66ff213f0bd006334c8523daee452725e5c7a79>
2017-01-25 22:43:27.620	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 300000 <0c1cd46df6ccff90ec4ab493281f2583c344cd62216c427628990fe9db1bb8b6>
2017-01-25 22:43:27.622	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 325000 <4260d56368267bc2a70dd58d73c5ecf23b4e4d96e63c29a868e4a679b0741c7f>
2017-01-25 22:43:27.625	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 350000 <74da79f6a136969abd6364bd3d37af273c408d6471e8ab598e80569b42415f86>
2017-01-25 22:43:27.628	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 375000 <c80c23e387585e12ffb6649d678e9ba328181797b9583a6d8911b77e25375737>
2017-01-25 22:43:27.631	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 400000 <1b2b0e7a30e59691491529a3d506d1ba3d6052d0f6b52198b7330b28a6f1b6ac>
2017-01-25 22:43:27.633	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 450000 <4d098b511ca97723e81737c448343cfd4e6dadb3d8a0e757c6e4d595e6e48357>
2017-01-25 22:43:27.636	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 500000 <2428f0dbe49796be05ed81b347f53e1f7f44aed0abf641446ec2b94cae066b02>
2017-01-25 22:43:27.639	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 550000 <c2e80a636438bd9f7a7ab432a6ad297e35540d80ff5b868bca098124cad2ff8c>
2017-01-25 22:43:27.641	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 600000 <f5828ebf7d7d1cb61762c4dfe3ccf4ecab2e1aad23e8113668d981713b7a54c5>
2017-01-25 22:43:27.644	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 650000 <1d567f2b491324375a825895c5e7b52857b38e4fed0e42c40909c2d52240b4e0>
2017-01-25 22:43:27.647	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 700000 <12be9b3d210b93f574d2526abb9c1ab2a881b479131fd0d4f7dac93875f503cd>
2017-01-25 22:43:27.650	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 800000 <2ced10aa85357ab6c14bb12b6b56d1dde28940820dda30911b73a5cc9a301760>
2017-01-25 22:43:27.653	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 850000 <00e2b557dde9fd4a9e2e3dd7ddac962f5ca475eb1095bc50aa757fd1218ab0a5>
2017-01-25 22:43:27.655	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 900000 <d9958d0e7dcf91a5a7b11de225927bf7efc6eb26240315ce12372be902cc1337>
2017-01-25 22:43:27.658	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913193 <5292d5d56f6ba4de33a58d9a34d263e2cb3c6fee0aed2286fd4ac7f36d53c85f>
2017-01-25 22:43:27.661	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913269 <f8302e6b8ba1c49aad9a854b8d6c79d8272c6239dcbba5a75ed0784c1d4f56a1>
2017-01-25 22:43:27.665	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:504	[check_and_resize_for_batch] checking DB size
2017-01-25 22:43:27.667	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:468	DB map size:     17179869184
2017-01-25 22:43:27.669	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:469	Space used:      10074075136
2017-01-25 22:43:27.670	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:470	Space remaining: 7105794048
2017-01-25 22:43:27.672	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:471	Size threshold:  0
2017-01-25 22:43:27.674	         6e74830	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:473	Percent used: 0.5864  Percent threshold: 0.8000
2017-01-25 22:43:27.678	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1 <771fbcd656ec1464d3a02ead5e18644030007a0fc664c0a964d30922821a8148>
2017-01-25 22:43:27.680	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 10 <c0e3b387e47042f72d8ccdca88071ff96bff1ac7cde09ae113dbb7ad3fe92381>
2017-01-25 22:43:27.683	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 100 <ac3e11ca545e57c49fca2b4e8c48c03c23be047c43e471e1394528b1f9f80b2d>
2017-01-25 22:43:27.686	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1000 <5acfc45acffd2b2e7345caf42fa02308c5793f15ec33946e969e829f40b03876>
2017-01-25 22:43:27.689	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 10000 <c758b7c81f928be3295d45e230646de8b852ec96a821eac3fea4daf3fcac0ca2>
2017-01-25 22:43:27.692	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 22231 <7cb10e29d67e1c069e6e11b17d30b809724255fee2f6868dc14cfc6ed44dfb25>
2017-01-25 22:43:27.694	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 29556 <53c484a8ed91e4da621bb2fa88106dbde426fe90d7ef07b9c1e5127fb6f3a7f6>
2017-01-25 22:43:27.697	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 50000 <0fe8758ab06a8b9cb35b7328fd4f757af530a5d37759f9d3e421023231f7b31c>
2017-01-25 22:43:27.700	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 80000 <a62dcd7b536f22e003ebae8726e9e7276f63d594e264b6f0cd7aab27b66e75e3>
2017-01-25 22:43:27.703	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202612 <bbd604d2ba11ba27935e006ed39c9bfdd99b76bf4a50654bc1e1e61217962698>
2017-01-25 22:43:27.705	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202613 <e2aa337e78df1f98f462b3b1e560c6b914dec47b610698b7b7d1e3e86b6197c2>
2017-01-25 22:43:27.708	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 202614 <c29e3dc37d8da3e72e506e31a213a58771b24450144305bcba9e70fa4d6ea6fb>
2017-01-25 22:43:27.711	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 205000 <5d3d7a26e6dc7535e34f03def711daa8c263785f73ec1fadef8a45880fde8063>
2017-01-25 22:43:27.713	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 220000 <9613f455933c00e3e33ac315cc6b455ee8aa0c567163836858c2d9caff111553>
2017-01-25 22:43:27.716	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 230300 <bae7a80c46859db355556e3a9204a337ae8f24309926a1312323fdecf1920e61>
2017-01-25 22:43:27.719	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 230700 <93e631240ceac831da1aebfc5dac8f722c430463024763ebafa888796ceaeedf>
2017-01-25 22:43:27.722	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 231350 <b5add137199b820e1ea26640e5c3e121fd85faa86a1e39cf7e6cc097bdeb1131>
2017-01-25 22:43:27.724	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 232150 <955de8e6b6508af2c24f7334f97beeea651d78e9ade3ab18fec3763be3201aa8>
2017-01-25 22:43:27.727	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 249380 <654fb0a81ce3e5caf7e3264a70f447d4bd07586c08fa50f6638cc54da0a52b2d>
2017-01-25 22:43:27.730	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 460000 <75037a7aed3e765db96c75bcf908f59d690a5f3390baebb9edeafd336a1c4831>
2017-01-25 22:43:27.733	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 500000 <2428f0dbe49796be05ed81b347f53e1f7f44aed0abf641446ec2b94cae066b02>
2017-01-25 22:43:27.735	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 600000 <f5828ebf7d7d1cb61762c4dfe3ccf4ecab2e1aad23e8113668d981713b7a54c5>
2017-01-25 22:43:27.738	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 700000 <12be9b3d210b93f574d2526abb9c1ab2a881b479131fd0d4f7dac93875f503cd>
2017-01-25 22:43:27.741	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 825000 <56503f9ad766774b575be3aff73245e9d159be88132c93d1754764f28da2ff60>
2017-01-25 22:43:27.743	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 900000 <d9958d0e7dcf91a5a7b11de225927bf7efc6eb26240315ce12372be902cc1337>
2017-01-25 22:43:27.746	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 913193 <5292d5d56f6ba4de33a58d9a34d263e2cb3c6fee0aed2286fd4ac7f36d53c85f>
2017-01-25 22:43:27.749	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1000000 <a886ef5149902d8342475fee9bb296341b891ac67c4842f47a833f23c00ed721>
2017-01-25 22:43:27.752	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1100000 <3fd720c5c8b3072fc1ccda922dec1ef25f9ed88a1e6ad4103d0fe00b180a5903>
2017-01-25 22:43:27.754	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1150000 <1dd16f626d18e1e988490dfd06de5920e22629c972c58b4d8daddea0038627b2>
2017-01-25 22:43:27.757	         6e74830	INFO 	checkpoints	src/cryptonote_core/checkpoints.cpp:105	CHECKPOINT PASSED FOR HEIGHT 1200000 <fa7d13a90850882060479d100141ff84286599ae39c3277c8ea784393f882d1f>
2017-01-25 22:43:27.766	         6e74830	INFO 	global	src/daemon/core.h:79	Core initialized OK
2017-01-25 22:43:27.769	         6e74830	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-01-25 22:43:27.773	         6e74830	INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:85	Run net_service loop( 2 threads)...
==1632== Thread 3:
==1632== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==1632==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==1632==    by 0x669927: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2067] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x61AED7: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4FEE77: epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1632==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1632==    by 0x495110F: thread_start (clone.S:89)
==1632==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==1632== 
2017-01-25 22:43:27.844	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: RPC
2017-01-25 22:43:27.852	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: RPC
2017-01-25 22:43:27.858	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-01-25 22:43:27.970	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-01-25 22:43:27.987	         ca7d1e0	INFO 	net.p2p	src/p2p/net_node.inl:602	Thread monitor number of peers - start
2017-01-25 22:43:28.007	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:630	Run net_service loop( 10 threads)...
==1632== Thread 8:
==1632== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==1632==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==1632==    by 0x669927: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2067] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x61AED7: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4FF507: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1632==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1632==    by 0x495110F: thread_start (clone.S:89)
==1632==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==1632== 
2017-01-25 22:43:28.034	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.041	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.045	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.051	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.056	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.061	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.066	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.071	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.076	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.081	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:820	Run server thread name: P2P
2017-01-25 22:43:28.084	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:827	JOINING all threads
2017-01-25 22:43:29.044	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1028	Considering connecting (out) to peer: 3630954930761173325 78.83.66.202:18080
2017-01-25 22:43:29.067	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2017-01-25 22:43:29.069	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x4F7ADF: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x633B27: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x635117: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1078] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x63651F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x63688B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4611] [clone .constprop.1073] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F558F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F429F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F7FDB: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x507EB3: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x61B097: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4FF507: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xcf7ba84 is on thread 8's stack
==1632==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1632== 
2017-01-25 22:43:29.093	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1028	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*, where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use "help" command to see the list of available commands.

Note: in case you need to interrupt the process, use "exit" command. Otherwise, the current progress won't be saved.
**********************************************************************
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x669D2F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x65CC1B: boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) [clone .constprop.2035] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x633D3B: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x635117: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1078] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x63651F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x63688B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4611] [clone .constprop.1073] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F558F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F429F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F7FDB: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x507EB3: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x61B097: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1632==  Address 0xcf7ba24 is on thread 8's stack
==1632==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1632== 
2017-01-25 22:43:29.208	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1603	[78.83.66.202:18080 4616607a-1574-683f-688a-2d7ad26cba08 OUT] NEW CONNECTION
2017-01-25 22:43:29.236	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:38559 <--> 78.83.66.202:18080
==1632== Thread 16:
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x513167: boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4C922F: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x61B097: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4FF507: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1632==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1632==    by 0x495110F: thread_start (clone.S:89)
==1632==  Address 0xf77c554 is on thread 16's stack
==1632==  in frame #1, created by boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (???:)
==1632== 
2017-01-25 22:43:29.619	[P2P8]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#2 to 0.0.0.0 currently we have sockets count:3
2017-01-25 22:43:29.621	[P2P8]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x669D2F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CCF4B: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x50261F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_accept(boost::system::error_code const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x507B83: boost::asio::detail::reactive_socket_accept_op<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::arg<1> (*)()> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4C9333: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x61B097: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4FF507: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1632==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1632==    by 0x495110F: thread_start (clone.S:89)
==1632==  Address 0xf77c344 is on thread 16's stack
==1632==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1632== 
2017-01-25 22:43:29.644	[P2P8]	INFO 	net.p2p	src/p2p/net_node.inl:1603	[78.83.66.202:48500 f0d27f39-cc23-e4f3-d6ee-2226432626f1 INC] NEW CONNECTION
2017-01-25 22:43:29.794	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[78.83.66.202:18080 OUT] Sync data returned a new top block candidate: 1230220 -> 1231780 [Your node is 1560 blocks (2 days) behind] 
SYNCHRONIZATION started
2017-01-25 22:43:29.808	[P2P8]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:270	 connection type P2P 192.168.0.21:18080 <--> 78.83.66.202:48500
2017-01-25 22:43:29.836	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1609	[78.83.66.202:48500 f0d27f39-cc23-e4f3-d6ee-2226432626f1 INC] CLOSE CONNECTION
2017-01-25 22:43:29.846	[P2P4]	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#0 to 78.83.66.202
2017-01-25 22:43:29.857	[P2P1]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:289	Remote blockchain height: 1231780, id: <0beffec97d8317411907071fe80964e351b21c49c14111cf86d7c34f686e74cd>
2017-01-25 22:43:29.942	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1028	Considering connecting (out) to peer: 8449248392124557971 109.190.141.183:18080
2017-01-25 22:43:29.951	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#3 to 0.0.0.0 currently we have sockets count:3
2017-01-25 22:43:29.958	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
2017-01-25 22:43:30.203	[P2P6]	INFO 	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1054	[78.83.66.202:18080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=1561, m_start_height=1230219, m_total_height=1231780
2017-01-25 22:43:31.557	[P2P6]	INFO 	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:983	78.83.66.202:18080 OUT-->>NOTIFY_REQUEST_GET_OBJECTS: blocks.size()=200, txs.size()=0requested blocks count=200 / 200
^C2017-01-25 22:43:34.129	         ca7d1e0	INFO 	net.p2p	src/p2p/net_node.inl:617	Thread monitor number of peers - done
2017-01-25 22:43:34.984	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#3 to 0.0.0.0
2017-01-25 22:43:34.992	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:900	[0.0.0.0:0 OUT] Connect failed to 109.190.141.183:18080
2017-01-25 22:43:34.995	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1047	Handshake failed
2017-01-25 22:43:35.009	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:944	Connecting to 93.137.213.2:18080(last_seen: d26.h12.m11.s37)...
2017-01-25 22:43:35.014	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:165	Spawned connection p2p#4 to 0.0.0.0 currently we have sockets count:3
2017-01-25 22:43:35.016	[P2P0]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:85	test, connection constructor set m_connection_type=2
==1632== Thread 8:
==1632== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1632==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1632==    by 0x4F7ADF: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x633B27: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x636B53: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_with_peer(nodetool::net_address const&, unsigned long) [clone .constprop.1068] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F8A1F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F42D3: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4F7FDB: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x507EB3: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x61B097: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4FF507: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1632==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1632==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1632==  Address 0xcf7bcd4 is on thread 8's stack
==1632==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1632== 
2017-01-25 22:43:40.050	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:957	[0.0.0.0:0 OUT] Connect failed to 93.137.213.2:18080
2017-01-25 22:43:40.067	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:831	JOINING all threads - almost
2017-01-25 22:43:40.072	[SRV_MAIN]	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:833	JOINING all threads - DONE
2017-01-25 22:43:40.076	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:636	net_service loop stopped.
2017-01-25 22:43:40.079	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2017-01-25 22:43:40.162	         c27d1e0	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#4 to 0.0.0.0
2017-01-25 22:43:40.171	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
2017-01-25 22:43:40.188	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:142	Node stopped.
2017-01-25 22:43:40.191	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2017-01-25 22:43:40.206	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#0 to 0.0.0.0
2017-01-25 22:43:40.234	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2017-01-25 22:43:40.237	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:242	Killing the net_node
2017-01-25 22:43:40.242	[SRV_MAIN]	INFO 	net	src/p2p/net_node.h:246	Joined extra background net_node threads
2017-01-25 22:43:40.716	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#2 to 0.0.0.0
2017-01-25 22:43:40.728	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:1609	[78.83.66.202:18080 4616607a-1574-683f-688a-2d7ad26cba08 OUT] CLOSE CONNECTION
2017-01-25 22:43:40.739	[SRV_MAIN]	INFO 	net.p2p	src/p2p/connection_basic.cpp:173	Destructing connection p2p#1 to 0.0.0.0
2017-01-25 22:43:40.774	[SRV_MAIN]	INFO 	global	src/daemon/core.h:90	Deinitializing core...
2017-01-25 22:43:40.796	[SRV_MAIN]	INFO 	txpool	src/cryptonote_core/tx_pool.cpp:742	Received signal to deactivate memory pool store
2017-01-25 22:43:40.814	[SRV_MAIN]	INFO 	txpool	src/cryptonote_core/tx_pool.cpp:765	Memory pool store deactivated successfully
==1632== Warning: set address range perms: large range [0x3939c000, 0x43939c000) (noaccess)
2017-01-25 22:43:40.886	[SRV_MAIN]	INFO 	cn	src/cryptonote_core/cryptonote_core.cpp:252	Blockchain directory successfully unlocked
2017-01-25 22:43:40.906	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2017-01-25 22:43:40.909	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
==1632== 
==1632== HEAP SUMMARY:
==1632==     in use at exit: 7,865,268 bytes in 1,182 blocks
==1632==   total heap usage: 157,501 allocs, 156,319 frees, 60,097,717 bytes allocated
==1632== 
==1632== LEAK SUMMARY:
==1632==    definitely lost: 815 bytes in 9 blocks
==1632==    indirectly lost: 6,295 bytes in 73 blocks
==1632==      possibly lost: 8,564 bytes in 105 blocks
==1632==    still reachable: 7,849,594 bytes in 995 blocks
==1632==         suppressed: 0 bytes in 0 blocks
==1632== Rerun with --leak-check=full to see details of leaked memory
==1632== 
==1632== For counts of detected and suppressed errors, rerun with: -v
==1632== Use --track-origins=yes to see where uninitialised values come from
==1632== ERROR SUMMARY: 663 errors from 14 contexts (suppressed: 0 from 0)

```

## ghost | 2017-01-25T23:26:10+00:00
Also noted multiple thread problems on exiting (`monerod exit`) the 'working' build:

```
nodey@odroidc2:~$ monerod exit
Stop signal sent
nodey@odroidc2:~$ ==1420== Thread 13:
==1420== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1420==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1420==    by 0x4F7ADF: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x633B27: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x636B53: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::check_connection_and_handshake_with_peer(nodetool::net_address const&, unsigned long) [clone .constprop.1068] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x4F8A1F: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::gray_peerlist_housekeeping() (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x4F42D3: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x4F7FDB: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x507EB3: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x61B097: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x4FF507: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1420==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1420==  Address 0xe27bcd4 is on thread 13's stack
==1420==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1420== 
==1420== Warning: client switching stacks?  SP change: 0xdd7abe0 --> 0xdb7a940
==1420==          to suppress, use: --max-stackframe=2097824 or greater
==1420== Thread 12:
==1420== Invalid write of size 8
==1420==    at 0x4849B88: memcpy (in /usr/lib/valgrind/vgpreload_memcheck-arm64-linux.so)
==1420==  Address 0xdd77890 is on thread 12's stack
==1420== 
==1420== Invalid read of size 8
==1420==    at 0x5EDD84: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd77ad0 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid read of size 8
==1420==    at 0x5EDD88: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd77ad8 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid write of size 8
==1420==    at 0x5EDDA0: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd77ad0 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid write of size 8
==1420==    at 0x5EDDA8: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd77ad8 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid read of size 4
==1420==    at 0x5E8980: aesb_single_round (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5EDD4F: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78640 is on thread 12's stack
==1420==  in frame #1, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid read of size 4
==1420==    at 0x5E8988: aesb_single_round (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5EDD4F: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78648 is on thread 12's stack
==1420==  in frame #1, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid write of size 4
==1420==    at 0x5E8A94: aesb_single_round (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5EDD4F: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78640 is on thread 12's stack
==1420==  in frame #1, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid write of size 4
==1420==    at 0x5E8A98: aesb_single_round (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5EDD4F: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78648 is on thread 12's stack
==1420==  in frame #1, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid read of size 8
==1420==    at 0x5EDD50: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78640 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid read of size 8
==1420==    at 0x5EDD54: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78648 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid write of size 8
==1420==    at 0x5EDD64: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78640 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid write of size 8
==1420==    at 0x5EDD7C: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd78648 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Invalid read of size 8
==1420==    at 0x5EDDFC: cn_slow_hash (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A63F3: cryptonote::get_block_longhash(cryptonote::block const&, crypto::hash&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A64B3: cryptonote::get_block_longhash(cryptonote::block const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5C9D5B: cryptonote::Blockchain::handle_block_to_main_chain(cryptonote::block const&, crypto::hash const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5CB5BF: cryptonote::Blockchain::add_new_block(cryptonote::block const&, cryptonote::block_verification_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x5A747F: cryptonote::core::handle_incoming_block(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, cryptonote::block_verification_context&, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x531EC7: cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x6480A7: int epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clone .constprop.863] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x64A07F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x529C77: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x50E4E7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==    by 0x513CFB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1420==  Address 0xdd77890 is on thread 12's stack
==1420==  in frame #0, created by cn_slow_hash (???:)
==1420== 
==1420== Warning: client switching stacks?  SP change: 0xdb7a940 --> 0xdd7abe0
==1420==          to suppress, use: --max-stackframe=2097824 or greater
==1420== Warning: set address range perms: large range [0x3939c000, 0x43939c000) (noaccess)
==1420== 
==1420== HEAP SUMMARY:
==1420==     in use at exit: 7,885,646 bytes in 1,142 blocks
==1420==   total heap usage: 747,214 allocs, 746,072 frees, 359,321,509 bytes allocated
==1420== 
==1420== LEAK SUMMARY:
==1420==    definitely lost: 1,167 bytes in 10 blocks
==1420==    indirectly lost: 27,941 bytes in 32 blocks
==1420==      possibly lost: 8,564 bytes in 105 blocks
==1420==    still reachable: 7,847,974 bytes in 995 blocks
==1420==         suppressed: 0 bytes in 0 blocks
==1420== Rerun with --leak-check=full to see details of leaked memory
==1420== 
==1420== For counts of detected and suppressed errors, rerun with: -v
==1420== Use --track-origins=yes to see where uninitialised values come from
==1420== ERROR SUMMARY: 56330 errors from 35 contexts (suppressed: 0 from 0)
```

## moneromooo-monero | 2017-01-27T20:47:03+00:00
Run again with --max-stackframe=2097824 as it helpfully suggests. If the cn_slow_hashes ones still happen, run with another, if it helpfully suggests one. If it still happens without a different stack size suggestion, then post again about it. This happens because cn_slow_hash allocates a huge buffer on the stack, and stacks usually aren't supposed to get that huge.

## ghost | 2017-01-27T21:06:19+00:00
Will do. Thanks. 

So the rest of the trace doesn't give any clear indication why MDEBUG and MTRACE are producing different behaviours? :(

## vtnerd | 2017-01-27T21:32:06+00:00
The errors during startup are the bigger concern. I did some code auditing through the relevant section, but nothing stood out to me. I have only vague theories on the source right now.

## moneromooo-monero | 2017-01-27T21:53:11+00:00
If you mean the "Syscall param epoll_ctl(event) points to uninitialised byte(s)", some syscal stuff (typically ioctl though) usually needs some description before valgrind knows what's supposed to be initialized, so I tend to mostly ignore these reports if they're not showing something obviously wrong.

## vtnerd | 2017-01-27T22:11:16+00:00
Really? This doesn't seem like typical behavior to me. Even with syscalls. And I can't reproduce the valgrind errors locally, although my environment is obviously very different.

This seems like undefined behavior somewhere early in the process. A memory overwrite or usage of an invalid pointer somewhere. Usually the culprits of these kinds of things ...

## moneromooo-monero | 2017-01-27T22:17:21+00:00
Can you try replacing std::mutex with std::recursive_mutex in easylogging++.h, lines 1106 and 1107 (for the hang).

## moneromooo-monero | 2017-01-27T22:17:39+00:00
vtnerd, I'm talking about ioctls here. This one might be different, admittedly.

## vtnerd | 2017-01-27T22:35:51+00:00
Oh right, sketchy drivers. Maybe @NanoAkron is using some of those?

## moneromooo-monero | 2017-01-27T22:47:37+00:00
OK, let me expand on what I said:

epoll_ctl is a syscall, and valgrind will not emulate the kernel to see what gets accessed in the data passed to it.

epoll_ctl takes a pointer to an event structure. This structure includes stuff that's not initialized. Since valgrind won't emulate the kernel, it uses a fallback warning that looks at what's not initialized there. There might be padding, or stuff that just won't actually get read/used by the kernel, based on the other parameters. So this is why I'm saying this is quite possibly a false positive. It might not, but false positives in those cases are frequent.

## vtnerd | 2017-01-28T01:27:38+00:00
Valgrind only complains if you touch the uninitialised data though. If you have an uninitialised struct then dump into a syscall, it should ignore IIRC.

## ghost | 2017-01-30T03:15:23+00:00
@moneromooo-monero's suggestion worked! Submitting a PR.

```
nodey@odroidc2:~$ valgrind --max-stackframe=2097824 ~/monero/build/release/bin/monerod --no-igd
==1298== Memcheck, a memory error detector
==1298== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==1298== Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info
==1298== Command: /home/nodey/monero/build/release/bin/monerod --no-igd
==1298== 
2017-01-30 03:13:01.597	         6e74830	INFO 	global	src/daemon/main.cpp:265	Monero 'Wolfram Warptangent' (v0.10.1.0-4629ead)
2017-01-30 03:13:01.747	         6e74830	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2017-01-30 03:13:01.752	         6e74830	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4E5EA3: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x508057: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5013EB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff464 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4E5EE7: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x508057: boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::socket_acceptor_service<boost::asio::ip::tcp> >(boost::asio::io_service&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x661107: boost::asio::detail::service_registry::do_use_service(boost::asio::io_service::service::key const&, boost::asio::io_service::service* (*)(boost::asio::io_service&)) [clone .constprop.2011] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5013EB: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff464 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::io_service::service* boost::asio::detail::service_registry::create<boost::asio::detail::epoll_reactor>(boost::asio::io_service&) (???:)
==1298== 
2017-01-30 03:13:01.841	         6e74830	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F5183: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x645A6B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5016D3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffeffe0c4 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CE7B3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F5457: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::init_server(unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x645A6B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::init(boost::program_options::variables_map const&) [clone .constprop.316] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5016D3: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffeffe064 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:05.699	         6e74830	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-01-30 03:13:05.709	         6e74830	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x55E03B: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50182F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff2b4 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CE7B3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x64BDFF: void boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::async_accept<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> > >(boost::asio::detail::reactive_socket_service<boost::asio::ip::tcp>::implementation_type&, boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >&, boost::asio::ip::basic_endpoint<boost::asio::ip::tcp>*, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >*>, boost::arg<1> (*)()> >&) [clone .constprop.885] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x55E317: cryptonote::core_rpc_server::init(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50182F: daemonize::t_daemon::t_daemon(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECDF: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xffefff1d4 is on thread 1's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:05.766	         6e74830	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-01-30 03:13:05.776	         6e74830	INFO 	global	src/daemon/core.h:74	Initializing core...
2017-01-30 03:13:06.072	         6e74830	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:318	Loading blockchain from folder /home/nodey/.bitmonero/lmdb ...
==1298== Warning: set address range perms: large range [0x3939c000, 0x43939c000) (defined)
==1298== Conditional jump or move depends on uninitialised value(s)
==1298==    at 0x6071E0: cryptonote::core::update_checkpoints() [clone .part.127] [clone .constprop.953] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x58E62F: cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4FDADF: daemonize::t_daemon::run(bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5EECEB: daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4B84C3: main (in /home/nodey/monero/build/release/bin/monerod)
==1298== 
2017-01-30 03:13:15.995	         6e74830	INFO 	global	src/daemon/core.h:79	Core initialized OK
2017-01-30 03:13:15.998	         6e74830	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
==1298== Thread 3:
==1298== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==1298==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==1298==    by 0x66DB47: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2067] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63BF7F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F0FFF: epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==1298== 
2017-01-30 03:13:16.081	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-01-30 03:13:16.195	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
==1298== Thread 8:
==1298== Syscall param epoll_pwait(sigmask) points to unaddressable byte(s)
==1298==    at 0x49512A4: epoll_pwait (epoll_pwait.c:42)
==1298==    by 0x66DB47: boost::asio::detail::epoll_reactor::run(bool, boost::asio::detail::op_queue<boost::asio::detail::task_io_service_operation>&) [clone .constprop.2067] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63BF7F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0x0 is not stack'd, malloc'd or (recently) free'd
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x515E57: boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CA0DF: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0xcf7c554 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::detail::reactive_socket_accept_op_base<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp>::do_perform(boost::asio::detail::reactor_op*) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CE7B3: boost::asio::detail::reactive_socket_service_base::start_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, int, boost::asio::detail::reactor_op*, bool, bool, bool) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F4B7F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_accept(boost::system::error_code const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50AF63: boost::asio::detail::reactive_socket_accept_op<boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >, boost::asio::ip::tcp, boost::_bi::bind_t<void, boost::_mfi::mf1<void, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&>, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::arg<1> (*)()> > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CA1E3: boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==    by 0x495110F: thread_start (clone.S:89)
==1298==  Address 0xcf7c344 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:16.490	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1029	
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
==1298== Thread 16:
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x523FBF: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_handshake(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request&, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x64C82F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x511BB7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F00EB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50CE0F: boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50DBEB: boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==    by 0x4865FC3: start_thread (pthread_create.c:335)
==1298==  Address 0xf77ad04 is on thread 16's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x660E4B: boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) [clone .constprop.2035] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x5243B3: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_handshake(int, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request&, nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x64C82F: int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.829] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x511BB7: epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F00EB: epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50CE0F: boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50DBEB: boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4CF7CF7: ??? (in /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.58.0)
==1298==  Address 0xf77aca4 is on thread 16's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:17.265	[P2P9]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1027	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

==1298== Thread 8:
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x4EA5B7: boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60B897: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60CE87: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1078] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60EDAF: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60F11B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4611] [clone .constprop.1073] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E76B7: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E4D37: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4EAAB3: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50B293: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4F168F: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xcf7ba84 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::basic_socket<boost::asio::ip::tcp, boost::asio::stream_socket_service<boost::asio::ip::tcp> >::open(boost::asio::ip::tcp const&) (???:)
==1298== 
==1298== Syscall param epoll_ctl(event) points to uninitialised byte(s)
==1298==    at 0x4951508: epoll_ctl (syscall-template.S:84)
==1298==    by 0x66DF4F: boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x660E4B: boost::asio::detail::reactive_socket_service_base::start_connect_op(boost::asio::detail::reactive_socket_service_base::base_implementation_type&, boost::asio::detail::reactor_op*, bool, sockaddr const*, unsigned long) [clone .constprop.2035] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60BAAB: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::connect(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned int, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) [clone .constprop.1082] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60CE87: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(nodetool::net_address const&, bool, unsigned long, bool) [clone .constprop.1078] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60EDAF: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist(bool) [clone .constprop.1074] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x60F11B: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count(bool, unsigned long) [clone .part.4611] [clone .constprop.1073] (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E76B7: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4E4D37: nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x4EAAB3: epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x50B293: boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) (in /home/nodey/monero/build/release/bin/monerod)
==1298==    by 0x63C13F: boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1343] (in /home/nodey/monero/build/release/bin/monerod)
==1298==  Address 0xcf7ba24 is on thread 8's stack
==1298==  in frame #1, created by boost::asio::detail::epoll_reactor::start_op(int, int, boost::asio::detail::epoll_reactor::descriptor_state*&, boost::asio::detail::reactor_op*, bool, bool) [clone .constprop.2061] (???:)
==1298== 
2017-01-30 03:13:41.864	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[212.20.7.188:52757 INC] Sync data returned a new top block candidate: 1234822 -> 1009962 [Your node is 224860 blocks (312 days) ahead] 
SYNCHRONIZATION started
2017-01-30 03:13:53.481	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:288	[91.107.12.146:64449 INC] Sync data returned a new top block candidate: 1234822 -> 1009962 [Your node is 224860 blocks (312 days) ahead] 
SYNCHRONISATION started
```

## ghost | 2017-01-30T10:52:23+00:00
@vtnerd is the 'conditional jump or move depends on uninitialised value(s)' a worry at all?

## vtnerd | 2017-02-01T19:17:17+00:00
@NanoAkron was this a 32-bit arm build?

If on a 32-bit build, I think the valgrind errors are likely a false-positive. ASIO is storing a pointer in the user portion of `epoll_event` structure which is 64-bits. That should explain the errors for the `epoll_ctl`, which was the bigger concern because the kernel is reading and not writing in that system call. The errors from `epoll_pwait` should be from ASIO providing an unitialized struct that the kernel fills (this is the case that @moneromooo-monero was talking about previously).

## vtnerd | 2017-02-01T19:19:08+00:00
Oh no wait, just realized there is another error in there that you were referencing. That error is rarely good, I've only seen a few cases where a programmer intended to use unitialized memory like that. I'll spam another response shortly.

## ghost | 2017-02-02T01:53:57+00:00
:)

I'm on 64-bit Ubuntu 16.04, ARMv8, GCC 5.4.0

## ghost | 2017-02-04T19:38:58+00:00
@vtnerd should I close this issue and open another one? What would I title it?

## vtnerd | 2017-02-06T05:37:26+00:00
I think it might be worth opening a new issue to investigate this issue. I would call it "possible undefined behavior on initialization". I'm also seeing an issue with `monerod` from the v0.10.1 release in a Gentoo VM. My issue is that it the first or second launch of `monerod` from a cold boot will segfault. 

Has there been a patch that possibly fixes this segmentation fault during initialization? I don't recall seeing any, but I will probably have to post more info before someone could answer.  Unfortunately reproducing is tricky because it generally only happens right after a cold boot ...

## ghost | 2017-02-06T07:54:28+00:00
Closing in favour of #1690 

## vtnerd | 2017-02-08T02:56:38+00:00
I think this should be re-visited, due to the race fixed by https://github.com/monero-project/monero/pull/1696 . Its possible that the mutex state was being corrupted as a result of the race.

# Action History
- Created by: ghost | 2017-01-19T23:25:59+00:00
- Closed at: 2017-02-06T07:54:28+00:00
