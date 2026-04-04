---
title: Unable to synchronise, daemon fails to start
source_url: https://github.com/monero-project/monero/issues/4558
author: aminemarref
assignees: []
labels: []
created_at: '2018-10-11T14:18:04+00:00'
updated_at: '2018-10-23T11:55:58+00:00'
type: issue
status: closed
closed_at: '2018-10-23T11:55:57+00:00'
---

# Original Description
Hello,

I have been downloading the Monero blockchain via `monero-gui-v0.12.3.0` for some time now. Things were working fine until a couple of days ago when I can no longer synchronise with the blockchain.

In [1] below, is a log extract that shows the last time things worked alright.
In [2] below, is a log extract that I get whenever I use Monero GUI since the last time things worked fine.

I tried running monerod using the command `monerod --rpc-bind-port 18089` as this port number was suggested by few help topics online. What happens is that monerod finishes executing and returns to the prompt after outputing the lines in [3] below. These lines are also shown in the log file as in [4] below. The Monero GUI remains unimpressed by executing the previous command, and boldly shows "Network status: Disconnected" in the bottom left corner.

I am running this on Windows 10 Pro (x64).

Any ideas?

Thanks.

**[1] Log extract that shows that last time blocks were being synched successfully.**
`2018-10-09 13:22:36.344	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509072/1679107[0m
2018-10-09 13:23:14.194	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509092/1679107[0m
2018-10-09 13:23:41.322	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509112/1679107[0m
2018-10-09 13:23:55.951	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509132/1679107[0m
2018-10-09 13:24:11.174	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509152/1679107[0m
2018-10-09 13:24:16.931	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509172/1679107[0m
2018-10-09 13:24:20.485	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509192/1679107[0m
2018-10-09 13:24:23.008	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509212/1679107[0m
2018-10-09 13:26:21.844	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509232/1679107[0m
2018-10-09 13:26:25.542	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[72.53.100.165:18080 OUT] Sync data returned a new top block candidate: 1509232 -> 1679110 [Your node is 169878 blocks (235 days) behind] 
SYNCHRONIZATION started
2018-10-09 13:26:26.120	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509252/1679110[0m
2018-10-09 13:26:28.635	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509272/1679110[0m
2018-10-09 13:26:31.158	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509292/1679110[0m
2018-10-09 13:26:33.208	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509312/1679110[0m
2018-10-09 13:26:35.872	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509332/1679110[0m
2018-10-09 13:26:41.324	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509352/1679110[0m
2018-10-09 13:26:45.584	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509372/1679110[0m
2018-10-09 13:27:06.902	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509392/1679110[0m
2018-10-09 13:27:11.478	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509412/1679110[0m
2018-10-09 13:27:31.321	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509432/1679110[0m
2018-10-09 13:27:49.420	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509452/1679110[0m
2018-10-09 13:27:53.298	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509472/1679110[0m
2018-10-09 13:28:02.437	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509492/1679110[0m
2018-10-09 13:28:08.702	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509512/1679110[0m
2018-10-09 13:28:13.103	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509532/1679110[0m
2018-10-09 13:28:25.224	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509552/1679110[0m
2018-10-09 13:29:03.439	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509572/1679110[0m
2018-10-09 13:29:11.047	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509592/1679110[0m
2018-10-09 13:29:16.797	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509612/1679110[0m
2018-10-09 13:29:27.326	[P2P3]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-10-09 13:29:48.467	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509632/1679110[0m
2018-10-09 13:30:06.229	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509652/1679110[0m
2018-10-09 13:30:12.927	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509672/1679110[0m
2018-10-09 13:30:16.471	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509692/1679110[0m
2018-10-09 13:30:38.334	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509712/1679110[0m
2018-10-09 13:30:56.295	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509732/1679110[0m
2018-10-09 13:31:08.939	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509752/1679110[0m
2018-10-09 13:31:12.057	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509772/1679110[0m
2018-10-09 13:31:22.317	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[115.197.210.171:18080 OUT]  Synced 1509792/1679110[0m
2018-10-09 13:31:29.954	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[203.223.190.130:18080 OUT] Sync data returned a new top block candidate: 1509792 -> 1679111 [Your node is 169319 blocks (235 days) behind] 
SYNCHRONIZATION started`

**[2] Log extract that shows what is happening now each time I fire up Monero GUI.**
`2018-10-11 14:03:04.586	3376	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:03:05.989	3376	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-10-11 14:03:09.138	5464	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:03:10.597	5464	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-10-11 14:03:13.747	1452	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:03:15.193	1452	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-10-11 14:03:18.343	22364	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:03:19.797	22364	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-10-11 14:03:22.948	16836	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:03:24.352	16836	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-10-11 14:03:27.503	18024	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:03:28.937	18024	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-10-11 14:03:32.086	22516	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:03:33.500	22516	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081`

**[3] Output of running `monerod --rpc-bind-port 18089`.**
`2018-10-11 14:06:59.789 13988   INFO    global  src/daemon/main.cpp:282 Monero 'Lithium Luna' (v0.12.3.0-release)
2018-10-11 14:06:59.791 13988   INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-11 14:06:59.791 13988   INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-10-11 14:06:59.803 13988   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-10-11 14:07:04.547 13988   INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-10-11 14:07:05.416 13988   INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-11 14:07:05.425 13988   INFO    global  contrib/epee/include/net/http_server_impl_base.h:76  Binding on 127.0.0.1:18089
2018-10-11 14:07:05.427 13988   INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18089
2018-10-11 14:07:05.427 13988   INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-11 14:07:05.430 13988   INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...`

**[4] Log entries after running `monerod --rpc-bind-port 18089`.**
`2018-10-11 14:06:59.788	13988	INFO 	logging	contrib/epee/src/mlog.cpp:186	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-11 14:06:59.789	13988	INFO 	global	src/daemon/main.cpp:282	Monero 'Lithium Luna' (v0.12.3.0-release)
2018-10-11 14:06:59.791	13988	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-10-11 14:06:59.791	13988	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-10-11 14:06:59.803	13988	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-10-11 14:07:04.547	13988	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-10-11 14:07:05.416	13988	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-10-11 14:07:05.425	13988	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18089
2018-10-11 14:07:05.427	13988	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18089
2018-10-11 14:07:05.427	13988	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-10-11 14:07:05.430	13988	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...`

# Discussion History
## moneromooo-monero | 2018-10-11T15:02:41+00:00
Try running:

monerod --rpc-bind-port --log-level 1

That might give more info.

## aminemarref | 2018-10-11T15:55:31+00:00
Thanks for the prompt reply :-)
I run `monerod --rpc-bind-port 18089 --log-level 1` and got the log [5] below. I could not decipher what the problem is, could you please?

**[5] Log for running `monerod --rpc-bind-port 18089 --log-level 1`**
`C:\ProgramFiles\monero-gui-v0.12.3.0>monerod --rpc-bind-port 18089 --log-level 1
2018-10-11 15:46:50.952 19920   INFO    global  src/daemon/main.cpp:282 Monero 'Lithium Luna' (v0.12.3.0-release)
2018-10-11 15:46:50.953 19920   INFO    daemon  src/daemon/main.cpp:284 Moving from main() into the daemonize now.
2018-10-11 15:46:50.954 19920   INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-11 15:46:50.955 19920   INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-10-11 15:46:50.965 19920   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-10-11 15:46:50.966 19920   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2018-10-11 15:46:50.968 19920   INFO    net.p2p src/p2p/net_node.inl:1875       Set limit-up to 2048 kB/s
2018-10-11 15:46:50.968 19920   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-11 15:46:50.969 19920   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-11 15:46:50.973 19920   INFO    net.p2p src/p2p/net_node.inl:1888       Set limit-down to 8192 kB/s
2018-10-11 15:46:50.974 19920   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2018-10-11 15:46:50.975 19920   INFO    net.p2p src/p2p/net_node.inl:1910       Set limit-up to 2048 kB/s
2018-10-11 15:46:50.976 19920   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-11 15:46:50.977 19920   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-11 15:46:50.978 19920   INFO    net.p2p src/p2p/net_node.inl:1914       Set limit-down to 8192 kB/s
2018-10-11 15:46:51.474 11428   INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-10-11 15:46:51.475 7448    INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2018-10-11 15:46:51.477 1056    INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2018-10-11 15:46:51.613 9824    INFO    net.p2p src/p2p/net_node.inl:457        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2018-10-11 15:46:51.614 19920   INFO    net.p2p src/p2p/net_node.inl:495        DNS seed node lookup either timed out or failed, falling back to defaults
2018-10-11 15:46:51.615 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 107.152.130.98:18080
2018-10-11 15:46:51.616 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 161.67.132.39:18080
2018-10-11 15:46:51.617 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 163.172.182.165:18080
2018-10-11 15:46:51.620 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 195.154.123.123:18080
2018-10-11 15:46:51.621 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 198.74.231.92:18080
2018-10-11 15:46:51.622 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 212.83.172.165:18080
2018-10-11 15:46:51.624 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 212.83.175.67:18080
2018-10-11 15:46:51.626 19920   INFO    net.p2p src/p2p/net_node.inl:357        Added seed node: 5.9.100.248:18080
2018-10-11 15:46:51.646 19920   INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:910   Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-11 15:46:51.647 19920   INFO    net.p2p src/p2p/net_node.inl:546        Binding on 0.0.0.0:18080
2018-10-11 15:46:51.650 19920   INFO    net.p2p src/p2p/net_node.inl:551        [1;32mNet service bound to 0.0.0.0:18080[0m
2018-10-11 15:46:55.971 19920   WARN    net.p2p src/p2p/net_node.inl:2009       UPnP device was found but not recognized as IGD.
2018-10-11 15:46:55.972 19920   INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-10-11 15:46:56.835 19920   INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-11 15:46:56.835 19920   INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:910   Set server type to: 1 from name: RPC, prefix_name = RPC
2018-10-11 15:46:56.837 19920   INFO    global  contrib/epee/include/net/http_server_impl_base.h:76  Binding on 127.0.0.1:18089
2018-10-11 15:46:56.839 19920   INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18089
2018-10-11 15:46:56.840 19920   INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-11 15:46:56.842 19920   INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-10-11 15:47:14.041 19920   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:528  DB map size:     55255705600
2018-10-11 15:47:14.041 19920   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:529  Space used:      45000761344
2018-10-11 15:47:14.042 19920   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:530  Space remaining: 10254944256
2018-10-11 15:47:14.043 19920   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:531  Size threshold:  0
2018-10-11 15:47:14.044 19920   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:533  Percent used: 0.8144  Percent threshold: 0.8000`

## moneromooo-monero | 2018-10-11T15:57:33+00:00
It looks like it's starting, it might be timing out on a DNS query, or trying to find peers.

## moneromooo-monero | 2018-10-11T15:58:08+00:00
By the way, you'll want 0.13.0.2, 0.12.x.y will be unable to sync in about a week from now.

## aminemarref | 2018-10-12T09:36:16+00:00
I used the new release of monerod in the hope that the problem resolves itself, but I am still unable to sync. Could you please point me to where I can further investigate the DNS/peer connection issues you suspect?

## moneromooo-monero | 2018-10-12T10:01:11+00:00
Run with --log-level 1,net.p2p:DEBUG

Then wait a bit to see whether it tries to connect, and whether it succeeds.

## aminemarref | 2018-10-17T20:04:28+00:00
I got the following. Monerod as usual exits :-(

```
2018-10-17 20:01:17.412	10996	INFO 	logging	contrib/epee/src/mlog.cpp:242	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-10-17 20:01:17.413	10996	INFO 	logging	contrib/epee/src/mlog.cpp:242	New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,net.p2p:DEBUG
2018-10-17 20:01:17.414	10996	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-17 20:01:17.415	10996	INFO 	daemon	src/daemon/main.cpp:289	Moving from main() into the daemonize now.
2018-10-17 20:01:17.416	10996	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-10-17 20:01:17.416	10996	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-10-17 20:01:17.418	10996	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-10-17 20:01:17.419	10996	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-17 20:01:17.420	10996	INFO 	net.p2p	src/p2p/net_node.inl:1929	Set limit-up to 2048 kB/s
2018-10-17 20:01:17.421	10996	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-17 20:01:17.421	10996	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-17 20:01:17.421	10996	INFO 	net.p2p	src/p2p/net_node.inl:1942	Set limit-down to 8192 kB/s
2018-10-17 20:01:17.422	10996	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-17 20:01:17.422	10996	INFO 	net.p2p	src/p2p/net_node.inl:1964	Set limit-up to 2048 kB/s
2018-10-17 20:01:17.422	10996	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-17 20:01:17.423	10996	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-17 20:01:17.424	10996	INFO 	net.p2p	src/p2p/net_node.inl:1968	Set limit-down to 8192 kB/s
2018-10-17 20:01:17.426	17244	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[0] created for: seeds.moneroseeds.se
2018-10-17 20:01:17.427	23336	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[1] created for: seeds.moneroseeds.ae.org
2018-10-17 20:01:17.428	10996	DEBUG	net.p2p	src/p2p/net_node.inl:489	dns_threads created, now waiting for completion or timeout of 20000ms
2018-10-17 20:01:17.430	3936	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[2] created for: seeds.moneroseeds.ch
2018-10-17 20:01:17.430	15068	DEBUG	net.p2p	src/p2p/net_node.inl:461	dns_threads[3] created for: seeds.moneroseeds.li
2018-10-17 20:01:17.472	17244	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2018-10-17 20:01:17.473	17244	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2018-10-17 20:01:17.910	15068	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[3] DNS resolve done
2018-10-17 20:01:17.911	15068	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-10-17 20:01:17.911	3936	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[2] DNS resolve done
2018-10-17 20:01:17.912	3936	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2018-10-17 20:01:17.912	17244	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[0] DNS resolve done
2018-10-17 20:01:17.912	17244	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2018-10-17 20:01:17.952	23336	DEBUG	net.p2p	src/p2p/net_node.inl:469	dns_threads[1] DNS resolve done
2018-10-17 20:01:17.953	23336	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2018-10-17 20:01:17.953	10996	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.se: 0 results
2018-10-17 20:01:17.954	10996	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2018-10-17 20:01:17.955	10996	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.ch: 0 results
2018-10-17 20:01:17.956	10996	DEBUG	net.p2p	src/p2p/net_node.inl:505	DNS lookup for seeds.moneroseeds.li: 0 results
2018-10-17 20:01:17.957	10996	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2018-10-17 20:01:17.959	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 107.152.130.98:18080
2018-10-17 20:01:17.960	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=107.152.130.98, port=18080
2018-10-17 20:01:17.961	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 107.152.130.98:18080
2018-10-17 20:01:17.963	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 161.67.132.39:18080
2018-10-17 20:01:17.964	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=161.67.132.39, port=18080
2018-10-17 20:01:17.964	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 161.67.132.39:18080
2018-10-17 20:01:17.965	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 163.172.182.165:18080
2018-10-17 20:01:17.966	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=163.172.182.165, port=18080
2018-10-17 20:01:17.967	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 163.172.182.165:18080
2018-10-17 20:01:17.968	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 195.154.123.123:18080
2018-10-17 20:01:17.969	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=195.154.123.123, port=18080
2018-10-17 20:01:17.970	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 195.154.123.123:18080
2018-10-17 20:01:17.971	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 198.74.231.92:18080
2018-10-17 20:01:17.972	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=198.74.231.92, port=18080
2018-10-17 20:01:17.974	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 198.74.231.92:18080
2018-10-17 20:01:17.975	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 212.83.172.165:18080
2018-10-17 20:01:17.975	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.172.165, port=18080
2018-10-17 20:01:17.976	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.172.165:18080
2018-10-17 20:01:17.977	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 212.83.175.67:18080
2018-10-17 20:01:17.978	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.175.67, port=18080
2018-10-17 20:01:17.979	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.175.67:18080
2018-10-17 20:01:17.980	10996	DEBUG	net.p2p	src/p2p/net_node.inl:532	Seed node: 5.9.100.248:18080
2018-10-17 20:01:17.980	10996	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=5.9.100.248, port=18080
2018-10-17 20:01:17.981	10996	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 5.9.100.248:18080
2018-10-17 20:01:17.982	10996	DEBUG	net.p2p	src/p2p/net_node.inl:535	Number of seed nodes: 8
2018-10-17 20:01:18.003	10996	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-17 20:01:18.004	10996	INFO 	net.p2p	src/p2p/net_node.inl:571	Binding on 0.0.0.0:18080
2018-10-17 20:01:18.006	10996	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-10-17 20:01:18.008	10996	INFO 	net.p2p	src/p2p/net_node.inl:576	[1;32mNet service bound to 0.0.0.0:18080[0m
2018-10-17 20:01:18.008	10996	DEBUG	net.p2p	src/p2p/net_node.inl:2031	Attempting to add IGD port mapping.
2018-10-17 20:01:22.363	10996	WARN 	net.p2p	src/p2p/net_node.inl:2063	UPnP device was found but not recognized as IGD.
2018-10-17 20:01:22.365	10996	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-10-17 20:01:22.369	10996	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-10-17 20:01:22.369	10996	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 1 from name: RPC, prefix_name = RPC
2018-10-17 20:01:22.371	10996	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-10-17 20:01:22.371	10996	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-10-17 20:01:22.374	10996	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-10-17 20:01:22.374	10996	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-10-17 20:01:22.377	10996	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-10-17 20:01:41.166	10996	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:544	DB map size:     55255705600
2018-10-17 20:01:41.168	10996	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:545	Space used:      45000769536
2018-10-17 20:01:41.169	10996	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:546	Space remaining: 10254936064
2018-10-17 20:01:41.170	10996	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:547	Size threshold:  0
2018-10-17 20:01:41.172	10996	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:549	Percent used: 0.8144  Percent threshold: 0.9000
````


## moneromooo-monero | 2018-10-17T20:35:07+00:00
No logs at this point hint at a crash. You don't get any crash message ? If not try to run with gdb:
gdb /path/to/monerod
run INSERT PARAMETERS YOU USE FOR MONEROD HERE

## aminemarref | 2018-10-17T21:22:45+00:00
I get the following error message while debugging:
```
Thread 1 received signal SIGSEGV, Segmentation fault.
0x00007ffe7dd8440f in msvcrt!memmove () from C:\Windows\System32\msvcrt.dll
```

The following is the command prompt output.
```
GNU gdb (GDB) 8.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-w64-mingw32".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod.exe...done.
(gdb) run
Starting program: C:\ProgramFiles\monero-gui-v0.12.3.0\monerod.exe
[New Thread 1576.0x5d5c]
[New Thread 1576.0x3780]
[New Thread 1576.0x5da8]
[New Thread 1576.0x3564]
[New Thread 1576.0x5770]
2018-10-17 21:12:07.359 23900   INFO    global  src/daemon/main.cpp:287 Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-17 21:12:07.391 23900   INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-17 21:12:07.393 23900   INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-10-17 21:12:07.435 23900   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
[New Thread 1576.0x6c14]
[New Thread 1576.0x5da4]
[New Thread 1576.0x1a9c]
[New Thread 1576.0x63d0]
[New Thread 1576.0x6e24]
[Thread 1576.0x6c14 exited with code 0]
[Thread 1576.0x1a9c exited with code 0]
[Thread 1576.0x63d0 exited with code 0]
[Thread 1576.0x5da4 exited with code 0]
[New Thread 1576.0x6d4c]
2018-10-17 21:12:16.329 23900   INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
[New Thread 1576.0x6870]
2018-10-17 21:12:16.337 23900   INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-17 21:12:16.338 23900   INFO    global  contrib/epee/include/net/http_server_impl_base.h:76  Binding on 127.0.0.1:18081
[New Thread 1576.0x6bac]
2018-10-17 21:12:16.342 23900   INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-10-17 21:12:16.342 23900   INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-17 21:12:16.344 23900   INFO    global  src/cryptonote_core/cryptonote_core.cpp:447     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...

Thread 1 received signal SIGSEGV, Segmentation fault.
0x00007ffe7dd8440f in msvcrt!memmove () from C:\Windows\System32\msvcrt.dll
(gdb) run --log-level 1,net.p2p:DEBUG
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: C:\ProgramFiles\monero-gui-v0.12.3.0\monerod.exe --log-level 1,net.p2p:DEBUG
[New Thread 3644.0x43a0]
[New Thread 3644.0x4e3c]
[New Thread 3644.0x6744]
[New Thread 3644.0x3988]
[New Thread 3644.0x2174]
2018-10-17 21:14:53.382 17312   INFO    global  src/daemon/main.cpp:287 Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-17 21:14:53.407 17312   INFO    daemon  src/daemon/main.cpp:289 Moving from main() into the daemonize now.
2018-10-17 21:14:53.409 17312   INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-10-17 21:14:53.411 17312   INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-10-17 21:14:53.453 17312   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-10-17 21:14:53.478 17312   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2018-10-17 21:14:53.496 17312   INFO    net.p2p src/p2p/net_node.inl:1929       Set limit-up to 2048 kB/s
2018-10-17 21:14:53.498 17312   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-17 21:14:53.499 17312   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-17 21:14:53.500 17312   INFO    net.p2p src/p2p/net_node.inl:1942       Set limit-down to 8192 kB/s
2018-10-17 21:14:53.501 17312   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2018-10-17 21:14:53.503 17312   INFO    net.p2p src/p2p/net_node.inl:1964       Set limit-up to 2048 kB/s
2018-10-17 21:14:53.504 17312   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-17 21:14:53.505 17312   INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2018-10-17 21:14:53.506 17312   INFO    net.p2p src/p2p/net_node.inl:1968       Set limit-down to 8192 kB/s
[New Thread 3644.0x617c]
2018-10-17 21:14:53.512 24956   DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[0] created for: seeds.moneroseeds.se
[New Thread 3644.0x55fc]
2[New Thread 3644.0xcec]
018-10-17 21:14:53.515  22012   DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[1] created for: seeds.moneroseeds.ae.org
2[New Thread 3644.0x66e0]
018-10-17 21:14:53.519  3308    DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[2] created for: seeds.moneroseeds.ch
2018-10-17 21:14:53.521 17312   DEBUG   net.p2p src/p2p/net_node.inl:489        dns_threads created, now waiting for completion or timeout of 20000ms
2018-10-17 21:14:53.597 26336   DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[3] created for: seeds.moneroseeds.li
[New Thread 3644.0x6ba8]
2018-10-17 21:14:53.752 24956   INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2018-10-17 21:14:53.753 24956   INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2018-10-17 21:15:06.067 24956   DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[0] DNS resolve done
2018-10-17 21:15:06.067 24956   INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
[Thread 3644.0x617c exited with code 0]
2018-10-17 21:15:06.095 26336   DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[3] DNS resolve done
2018-10-17 21:15:06.096 26336   INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
[Thread 3644.0x66e0 exited with code 0]
2018-10-17 21:15:06.098 22012   DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[1] DNS resolve done
2018-10-17 21:15:06.102 22012   INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
[Thread 3644.0x55fc exited with code 0]
2018-10-17 21:15:06.114 3308    DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[2] DNS resolve done
2018-10-17 21:15:06.114 3308    INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
[Thread 3644.0xcec exited with code 0]
2018-10-17 21:15:06.120 17312   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.se: 0 results
2018-10-17 21:15:06.120 17312   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ae.org: 0 results
2018-10-17 21:15:06.121 17312   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ch: 0 results
2018-10-17 21:15:06.122 17312   DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.li: 0 results
2018-10-17 21:15:06.123 17312   INFO    net.p2p src/p2p/net_node.inl:519        DNS seed node lookup either timed out or failed, falling back to defaults
2018-10-17 21:15:06.124 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 107.152.130.98:18080
2018-10-17 21:15:06.127 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=107.152.130.98, port=18080
2018-10-17 21:15:06.128 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 107.152.130.98:18080
2018-10-17 21:15:06.129 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 161.67.132.39:18080
2018-10-17 21:15:06.129 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=161.67.132.39, port=18080
2018-10-17 21:15:06.130 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 161.67.132.39:18080
2018-10-17 21:15:06.131 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 163.172.182.165:18080
2018-10-17 21:15:06.132 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=163.172.182.165, port=18080
2018-10-17 21:15:06.133 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 163.172.182.165:18080
2018-10-17 21:15:06.134 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 195.154.123.123:18080
2018-10-17 21:15:06.134 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=195.154.123.123, port=18080
2018-10-17 21:15:06.137 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 195.154.123.123:18080
2018-10-17 21:15:06.137 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 198.74.231.92:18080
2018-10-17 21:15:06.138 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=198.74.231.92, port=18080
2018-10-17 21:15:06.139 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 198.74.231.92:18080
2018-10-17 21:15:06.140 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 212.83.172.165:18080
2018-10-17 21:15:06.141 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=212.83.172.165, port=18080
2018-10-17 21:15:06.142 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 212.83.172.165:18080
2018-10-17 21:15:06.143 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 212.83.175.67:18080
2018-10-17 21:15:06.144 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=212.83.175.67, port=18080
2018-10-17 21:15:06.146 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 212.83.175.67:18080
2018-10-17 21:15:06.147 17312   DEBUG   net.p2p src/p2p/net_node.inl:532        Seed node: 5.9.100.248:18080
2018-10-17 21:15:06.147 17312   INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=5.9.100.248, port=18080
2018-10-17 21:15:06.148 17312   INFO    net.p2p src/p2p/net_node.inl:377        Added node: 5.9.100.248:18080
2018-10-17 21:15:06.149 17312   DEBUG   net.p2p src/p2p/net_node.inl:535        Number of seed nodes: 8
2018-10-17 21:15:07.383 17312   INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:917   Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-17 21:15:07.387 17312   INFO    net.p2p src/p2p/net_node.inl:571        Binding on 0.0.0.0:18080
2018-10-17 21:15:07.394 17312   DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
[New Thread 3644.0x6b00]
2018-10-17 21:15:07.405 17312   INFO    net.p2p src/p2p/net_node.inl:576        [1;32mNet service bound to 0.0.0.0:18080[0m
2018-10-17 21:15:07.408 17312   DEBUG   net.p2p src/p2p/net_node.inl:2031       Attempting to add IGD port mapping.
2018-10-17 21:15:11.425 17312   INFO    net.p2p src/p2p/net_node.inl:2070       No IGD was found.
2018-10-17 21:15:11.427 17312   INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
[New Thread 3644.0x6c58]
2018-10-17 21:15:11.591 17312   INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-10-17 21:15:11.593 17312   INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:917   Set server type to: 1 from name: RPC, prefix_name = RPC
2018-10-17 21:15:11.596 17312   INFO    global  contrib/epee/include/net/http_server_impl_base.h:76  Binding on 127.0.0.1:18081
2018-10-17 21:15:11.602 17312   DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
[New Thread 3644.0x6258]
2018-10-17 21:15:11.610 17312   INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-10-17 21:15:11.613 17312   INFO    global  src/daemon/core.h:86    Initializing core...
2018-10-17 21:15:11.669 17312   INFO    global  src/cryptonote_core/cryptonote_core.cpp:447     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-10-17 21:15:40.706 17312   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:544  DB map size:     55255705600
2018-10-17 21:15:40.709 17312   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:545  Space used:      45000769536
2018-10-17 21:15:40.711 17312   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:546  Space remaining: 10254936064
2018-10-17 21:15:40.713 17312   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:547  Size threshold:  0
2018-10-17 21:15:40.716 17312   INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:549  Percent used: 0.8144  Percent threshold: 0.9000

Thread 1 received signal SIGSEGV, Segmentation fault.
0x00007ffe7dd8440f in msvcrt!memmove () from C:\Windows\System32\msvcrt.dll
```

Am I running out of memory or something?

## moneromooo-monero | 2018-10-17T21:36:23+00:00
Perfect!
You should have had a crash message, that's odd. Your OS seems to be dumb.
When it's stopped in gdb, type:
bt


## aminemarref | 2018-10-17T21:39:15+00:00
Lol. This is what I get now.

```
(gdb) bt
#0  0x00007ffe7dd8440f in msvcrt!memmove () from C:\Windows\System32\msvcrt.dll
#1  0x0000000000431ab5 in cryptonote::core_rpc_server::on_update(cryptonote::COMMAND_RPC_UPDATE::request const&, cryptonote::COMMAND_RPC_UPDATE::response&) ()
#2  0x0000000000000000 in ?? ()
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
```

## moneromooo-monero | 2018-10-17T21:43:48+00:00
Can you run a debug build for better info ?

## aminemarref | 2018-10-19T21:16:24+00:00
I will try doing that.
Meanwhile, I am running the process in Ubuntu 18 (in a virtual machine) and I am getting the following error:
```
Thread 1 "monerod" received signal SIGBUS, Bus error.
__memmove_sse2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:371
371	../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S: No such file or directory.
```

Which is similar to the one I get under Windows 10:
```
Thread 1 received signal SIGSEGV, Segmentation fault.
0x00007ffe7dd8440f in msvcrt!memmove () from C:\Windows\System32\msvcrt.dll
```

The following is the gdb trace:
```
amine@ubuntu:~/Workspace/monero-gui-v0.13.0.3$ gdb ./monerod
GNU gdb (Ubuntu 8.1-0ubuntu3) 8.1.0.20180409-git
Copyright (C) 2018 Free Software Foundation, Inc.
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
Reading symbols from ./monerod...done.
(gdb) run --rpc-bind-port 18089 --data-dir /home/amine/Workspace/monero-gui-v0.13.0.3/Blockchain/bitmonero/ --log-level 1
Starting program: /home/amine/Workspace/monero-gui-v0.13.0.3/monerod --rpc-bind-port 18089 --data-dir /home/amine/Workspace/monero-gui-v0.13.0.3/Blockchain/bitmonero/ --log-level 1
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
2018-10-19 21:03:37,176 INFO  [default] Page size: 4096
2018-10-19 21:03:38.183	    7ffff7fdd780	INFO 	global	src/daemon/main.cpp:287	Monero 'Beryllium Bullet' (v0.13.0.2-release)
2018-10-19 21:03:38.185	    7ffff7fdd780	INFO 	daemon	src/daemon/main.cpp:289	Moving from main() into the daemonize now.
2018-10-19 21:03:38.186	    7ffff7fdd780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-10-19 21:03:38.187	    7ffff7fdd780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-10-19 21:03:38.188	    7ffff7fdd780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-10-19 21:03:38.189	    7ffff7fdd780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-19 21:03:38.191	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:1929	Set limit-up to 2048 kB/s
2018-10-19 21:03:38.191	    7ffff7fdd780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-19 21:03:38.191	    7ffff7fdd780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-19 21:03:38.192	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:1942	Set limit-down to 8192 kB/s
2018-10-19 21:03:38.192	    7ffff7fdd780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 2048 kbps
2018-10-19 21:03:38.193	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:1964	Set limit-up to 2048 kB/s
2018-10-19 21:03:38.193	    7ffff7fdd780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-19 21:03:38.193	    7ffff7fdd780	INFO 	net.throttle	contrib/epee/src/network_throttle-detail.cpp:162	Setting LIMIT: 8192 kbps
2018-10-19 21:03:38.193	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:1968	Set limit-down to 8192 kB/s
[New Thread 0x7ffff6dfc700 (LWP 2791)]
2018-10-19 21:03:38.197	    7ffff6dfc700	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

[New Thread 0x7ffff65fb700 (LWP 2792)]
2018-10-19 21:03:38.208	    7ffff6dfc700	INFO 	net.dns	src/common/dns_utils.cpp:252	adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

[New Thread 0x7ffff5dfa700 (LWP 2793)]
[New Thread 0x7ffff55f9700 (LWP 2794)]
2018-10-19 21:03:38.340	    7ffff65fb700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
[Thread 0x7ffff65fb700 (LWP 2792) exited]
2018-10-19 21:03:38.341	    7ffff5dfa700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
[Thread 0x7ffff5dfa700 (LWP 2793) exited]
2018-10-19 21:03:38.343	    7ffff6dfc700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
[Thread 0x7ffff6dfc700 (LWP 2791) exited]
2018-10-19 21:03:40.159	    7ffff55f9700	INFO 	net.p2p	src/p2p/net_node.inl:481	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:519	DNS seed node lookup either timed out or failed, falling back to defaults
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=107.152.130.98, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 107.152.130.98:18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=161.67.132.39, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 161.67.132.39:18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=163.172.182.165, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 163.172.182.165:18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=195.154.123.123, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 195.154.123.123:18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=198.74.231.92, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 198.74.231.92:18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.172.165, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.172.165:18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=212.83.175.67, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 212.83.175.67:18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:360	Resolving node address: host=5.9.100.248, port=18080
2018-10-19 21:03:40.160	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:377	Added node: 5.9.100.248:18080
[Thread 0x7ffff55f9700 (LWP 2794) exited]
2018-10-19 21:03:40.167	    7ffff7fdd780	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-19 21:03:40.168	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:571	Binding on 0.0.0.0:18080
2018-10-19 21:03:40.169	    7ffff7fdd780	INFO 	net.p2p	src/p2p/net_node.inl:576	Net service bound to 0.0.0.0:18080
2018-10-19 21:03:44.486	    7ffff7fdd780	WARN 	net.p2p	src/p2p/net_node.inl:2063	UPnP device was found but not recognized as IGD.
2018-10-19 21:03:44.487	    7ffff7fdd780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-10-19 21:03:44.488	    7ffff7fdd780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-10-19 21:03:44.489	    7ffff7fdd780	INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:917	Set server type to: 1 from name: RPC, prefix_name = RPC
2018-10-19 21:03:44.489	    7ffff7fdd780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18089
2018-10-19 21:03:44.490	    7ffff7fdd780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18089
2018-10-19 21:03:44.490	    7ffff7fdd780	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-10-19 21:03:44.491	    7ffff7fdd780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:447	Loading blockchain from folder /home/amine/Workspace/monero-gui-v0.13.0.3/Blockchain/bitmonero/lmdb ...
2018-10-19 21:03:44.492	    7ffff7fdd780	WARN 	global	src/blockchain_db/lmdb/db_lmdb.cpp:1211	The blockchain is on a rotating drive: this will be very slow, use a SSD if possible
2018-10-19 21:03:44.493	    7ffff7fdd780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:544	DB map size:     55255705600
2018-10-19 21:03:44.493	    7ffff7fdd780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:545	Space used:      45000769536
2018-10-19 21:03:44.494	    7ffff7fdd780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:546	Space remaining: 10254936064
2018-10-19 21:03:44.494	    7ffff7fdd780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:547	Size threshold:  0
2018-10-19 21:03:44.494	    7ffff7fdd780	INFO 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:549	Percent used: 0.8144  Percent threshold: 0.9000

Thread 1 "monerod" received signal SIGBUS, Bus error.
__memmove_sse2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:371
371	../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S: No such file or directory.
```
On the plus side, In Ubuntu, I get a crash message for the program when run normally:
`Bus error (core dumped)`


## moneromooo-monero | 2018-10-19T21:31:47+00:00
You don't seem to have type "bt" in that paste.

## aminemarref | 2018-10-19T21:39:53+00:00
Here it is:
```
Thread 1 "monerod" received signal SIGBUS, Bus error.
__memmove_sse2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:371
371	../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S: No such file or directory.
(gdb) bt
#0  __memmove_sse2_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:371
#1  0x0000555555ca1643 in mdb_page_touch ()
#2  0x0000555555ca1c28 in mdb_page_search ()
#3  0x0000555555caa3dd in mdb_txn_commit ()
#4  0x0000555555a88472 in cryptonote::mdb_txn_safe::commit(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) ()
#5  0x0000555555ab7d6e in cryptonote::BlockchainLMDB::open(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int) ()
#6  0x0000555555b05031 in cryptonote::core::init(boost::program_options::variables_map const&, char const*, cryptonote::test_options const*) ()
#7  0x00005555558753e3 in daemonize::t_core::run() ()
#8  0x00005555558531c8 in daemonize::t_daemon::run(bool) ()
#9  0x000055555590c4fe in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#10 0x00005555559134fe in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#11 0x0000555555827035 in main ()
(gdb) 
```


## moneromooo-monero | 2018-10-19T21:42:11+00:00
Thanks. That looks like a corrupt DB. Did you have an OS crash recently ?

## aminemarref | 2018-10-19T21:43:36+00:00
No not at all.
There was a major Windows 10 update though.

## hyc | 2018-10-20T15:32:07+00:00
Windows updates have been pretty bad lately. https://github.com/nimiq-network/core/issues/387#issuecomment-401067760

## xiphon | 2018-10-20T15:40:08+00:00
@aminemarref 
are you running monerod on WSL?

## aminemarref | 2018-10-20T19:09:04+00:00
Initially, I was running monerod in Windows 10 until it could no longer synchronise. Then, I copied over the blockchain folder that I downloaded so far to an Ubuntu 18 running in VMware inside Windows 10 just for the sake of obtaining more useful debug information. Both crash.

## xiphon | 2018-10-21T21:08:16+00:00
If you are not running Monero on Windows using WSL, the issue is not related to Windows updates and broken WSL mmap.

## moneromooo-monero | 2018-10-23T11:16:18+00:00
It could be related, since "Then, I copied over the blockchain folder that I downloaded so far". So if windows corrupted the db, ubuntu got a corrupt db in the first place.

## aminemarref | 2018-10-23T11:55:57+00:00
Thanks @moneromooo-monero for your special help in this issue. Thanks everyone else.
I tried to salvage the database but it did not work.
I guess I will re-download the 40+ GBs of the chain again. Sigh.

# Action History
- Created by: aminemarref | 2018-10-11T14:18:04+00:00
- Closed at: 2018-10-23T11:55:57+00:00
