---
title: Monerod Doesn't Connect to Peers.
source_url: https://github.com/monero-project/monero/issues/2160
author: fkdis
assignees: []
labels:
- invalid
created_at: '2017-07-08T20:12:42+00:00'
updated_at: '2017-08-08T10:54:14+00:00'
type: issue
status: closed
closed_at: '2017-08-08T10:54:14+00:00'
---

# Original Description
I have installed the Monero GUI and it was giving some errors so I went back to the cli. When I run ./monerod everything seems to work fine but when I do status it gives me -
"Height: 1346603/1346603 (100.0%) on mainnet, not mining, net hash 99.90 MH/s, v5, up to date, 0(out)+0(in) connections, uptime 0d 0h 11m 57s"
Why is it not connecting to peers? I did a few things before asking on monero.stackexchange.com, here are all of the details https://monero.stackexchange.com/questions/4533/monerod-doesnt-connect-to-peers/4537?noredirect=1 and I did have the daemon running for longer than that afterwards but the issue was still relevant.  If you read it he tells me do give the output with options and I didn't really know what he meant by "log" so here is two minutes of output from monerod. 

2017-07-08 14:04:39.821	    7f39cb2dfec0	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-07-08 14:04:39.823	    7f39cb2dfec0	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,global:INFO,stacktrace:INFO,net.cn:DEBUG,net.p2p:DEBUG
2017-07-08 14:04:39.823	    7f39cb2dfec0	INFO 	global	src/daemon/main.cpp:282	Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-07-08 14:04:39.823	    7f39cb2dfec0	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-07-08 14:04:39.823	    7f39cb2dfec0	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-07-08 14:04:39.823	    7f39cb2dfec0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-07-08 14:04:39.824	    7f39ca5f1700	DEBUG	net.p2p	src/p2p/net_node.inl:455	dns_threads[0] created for: seeds.moneroseeds.se
2017-07-08 14:04:39.824	    7f39c9df0700	DEBUG	net.p2p	src/p2p/net_node.inl:455	dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-07-08 14:04:39.824	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:483	dns_threads created, now waiting for completion or timeout of 20000ms
2017-07-08 14:04:39.824	    7f39c95ef700	DEBUG	net.p2p	src/p2p/net_node.inl:455	dns_threads[2] created for: seeds.moneroseeds.ch
2017-07-08 14:04:39.824	    7f39c8dee700	DEBUG	net.p2p	src/p2p/net_node.inl:455	dns_threads[3] created for: seeds.moneroseeds.li
2017-07-08 14:04:39.842	    7f39c95ef700	DEBUG	net.p2p	src/p2p/net_node.inl:463	dns_threads[2] DNS resolve done
2017-07-08 14:04:39.842	    7f39c95ef700	INFO 	net.p2p	src/p2p/net_node.inl:475	dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-07-08 14:04:39.842	    7f39c8dee700	DEBUG	net.p2p	src/p2p/net_node.inl:463	dns_threads[3] DNS resolve done
2017-07-08 14:04:39.842	    7f39c8dee700	INFO 	net.p2p	src/p2p/net_node.inl:475	dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-07-08 14:04:39.842	    7f39c9df0700	DEBUG	net.p2p	src/p2p/net_node.inl:463	dns_threads[1] DNS resolve done
2017-07-08 14:04:39.842	    7f39c9df0700	INFO 	net.p2p	src/p2p/net_node.inl:475	dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-07-08 14:04:40.789	    7f39ca5f1700	DEBUG	net.p2p	src/p2p/net_node.inl:463	dns_threads[0] DNS resolve done
2017-07-08 14:04:40.789	    7f39ca5f1700	INFO 	net.p2p	src/p2p/net_node.inl:475	dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-07-08 14:04:40.789	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:499	DNS lookup for seeds.moneroseeds.se: 0 results
2017-07-08 14:04:40.789	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:499	DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-07-08 14:04:40.789	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:499	DNS lookup for seeds.moneroseeds.ch: 0 results
2017-07-08 14:04:40.789	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:499	DNS lookup for seeds.moneroseeds.li: 0 results
2017-07-08 14:04:40.789	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:513	DNS seed node lookup either timed out or failed, falling back to defaults
2017-07-08 14:04:40.789	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 107.152.130.98:18080
2017-07-08 14:04:40.789	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 107.152.130.98:18080
2017-07-08 14:04:40.789	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 161.67.132.39:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 161.67.132.39:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 163.172.182.165:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 163.172.182.165:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 195.154.123.123:28080
2017-07-08 14:04:40.790	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 195.154.123.123:28080
2017-07-08 14:04:40.790	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 198.74.231.92:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 198.74.231.92:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 212.83.172.165:28080
2017-07-08 14:04:40.790	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 212.83.172.165:28080
2017-07-08 14:04:40.790	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 212.83.175.67:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 212.83.175.67:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:524	Seed node: 5.9.100.248:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:390	Added seed node: 5.9.100.248:18080
2017-07-08 14:04:40.790	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:527	Number of seed nodes: 8
2017-07-08 14:04:40.791	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:1747	Set limit-up to 2048 kB/s
2017-07-08 14:04:40.791	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:1761	Set limit-down to 8192 kB/s
2017-07-08 14:04:40.791	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:1783	Set limit-up to 2048 kB/s
2017-07-08 14:04:40.791	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:1787	Set limit-down to 8192 kB/s
2017-07-08 14:04:40.791	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:566	Binding on 0.0.0.0:18080
2017-07-08 14:04:40.792	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-07-08 14:04:40.792	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:571	Net service bound to 0.0.0.0:18080
2017-07-08 14:04:40.792	    7f39cb2dfec0	DEBUG	net.p2p	src/p2p/net_node.inl:577	Attempting to add IGD port mapping.
2017-07-08 14:04:41.856	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/net_node.inl:604	Added IGD port mapping.
2017-07-08 14:04:41.856	    7f39cb2dfec0	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-07-08 14:04:41.856	    7f39cb2dfec0	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-07-08 14:04:41.857	    7f39cb2dfec0	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-07-08 14:04:41.857	    7f39cb2dfec0	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-07-08 14:04:41.857	    7f39cb2dfec0	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-07-08 14:04:41.857	    7f39cb2dfec0	INFO 	global	src/daemon/core.h:73	Initializing core...
2017-07-08 14:04:41.858	    7f39cb2dfec0	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:326	Loading blockchain from folder /home/peyto/.bitmonero/lmdb ...
2017-07-08 14:05:30.432	    7f39cb2dfec0	WARN 	net.dns	src/common/dns_utils.cpp:531	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-07-08 14:05:30.790	    7f39cb2dfec0	INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-07-08 14:05:30.790	    7f39cb2dfec0	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-07-08 14:05:30.791	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-07-08 14:05:30.791	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-07-08 14:05:30.791	[SRV_MAIN]	INFO 	net.p2p	src/p2p/net_node.inl:662	Run net_service loop( 10 threads)...
2017-07-08 14:05:30.791	    7f39bb7fe700	INFO 	net.p2p	src/p2p/net_node.inl:634	Thread monitor number of peers - start
2017-07-08 14:05:31.791	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:1215	STARTED PEERLIST IDLE HANDSHAKE
2017-07-08 14:05:31.791	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:1227	FINISHED PEERLIST IDLE HANDSHAKE
2017-07-08 14:05:31.791	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:31.791	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:05:31.791	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:05:31.791	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:05:31.791	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2017-07-08 14:05:31.791	[P2P3]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1098	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-07-08 14:05:31.792	[P2P3]	WARN 	net.dns	src/common/dns_utils.cpp:531	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-07-08 14:05:36.792	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 5.9.100.248:18080
2017-07-08 14:05:36.792	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:05:36.792	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:36.792	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:05:36.792	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:05:36.792	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:05:36.792	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:05:36.792	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#2 to 0.0.0.0 currently we have sockets count:3
2017-07-08 14:05:41.793	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:05:41.793	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:05:41.793	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:41.793	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:41.793	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:05:41.793	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:05:41.793	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:41.793	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:43.793	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:05:43.794	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:05:43.794	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:05:43.794	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:05:43.794	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#3 to 0.0.0.0 currently we have sockets count:4
2017-07-08 14:05:48.794	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 5.9.100.248:18080
2017-07-08 14:05:48.794	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:05:48.795	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:05:48.795	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:05:48.795	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:05:48.795	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:05:48.795	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:05:48.795	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:05:48.795	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#4 to 0.0.0.0 currently we have sockets count:5
2017-07-08 14:05:53.795	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:05:53.795	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:05:53.796	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:05:53.796	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:53.796	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:53.796	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:53.796	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:05:55.796	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:05:55.796	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:05:55.796	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:05:55.796	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:05:55.796	[P2P5]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#5 to 0.0.0.0 currently we have sockets count:6
2017-07-08 14:06:00.797	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 5.9.100.248:18080
2017-07-08 14:06:00.797	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:00.797	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:00.797	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:06:00.797	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:06:00.797	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:06:00.797	[P2P5]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#6 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:05.792	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#1 to 0.0.0.0
2017-07-08 14:06:05.797	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:06:05.797	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:05.798	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:05.798	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:05.798	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:05.798	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:05.798	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:05.798	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:05.798	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:07.798	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:07.798	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:06:07.798	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:06:07.798	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:06:07.798	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#7 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:10.792	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#2 to 0.0.0.0
2017-07-08 14:06:12.799	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 5.9.100.248:18080
2017-07-08 14:06:12.799	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:12.799	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:12.799	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:12.799	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:06:12.799	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:06:12.799	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:06:12.799	[P2P1]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#8 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:15.792	[P2P4]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#3 to 0.0.0.0
2017-07-08 14:06:17.800	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:06:17.800	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:17.800	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:17.800	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:17.800	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:17.800	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:17.800	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:17.800	[P2P1]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:19.801	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:19.801	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:06:19.801	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:06:19.801	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:06:19.801	[P2P4]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#9 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:20.792	[P2P8]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#4 to 0.0.0.0
2017-07-08 14:06:24.801	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 5.9.100.248:18080
2017-07-08 14:06:24.801	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:24.801	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:24.801	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:06:24.801	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:06:24.801	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:06:24.801	[P2P4]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#10 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:29.802	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:06:29.802	[P2P4]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:29.802	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:29.802	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:29.802	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:29.802	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:29.802	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:29.802	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:29.802	[P2P4]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:30.793	[P2P5]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#5 to 0.0.0.0
2017-07-08 14:06:31.803	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:31.803	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:06:31.803	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:06:31.803	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:06:31.803	[P2P5]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#11 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:35.793	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#6 to 0.0.0.0
2017-07-08 14:06:36.803	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 5.9.100.248:18080
2017-07-08 14:06:36.803	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:36.803	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:36.803	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:36.804	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:36.804	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:06:36.804	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:06:36.804	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:06:36.804	[P2P5]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#12 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:40.793	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#7 to 0.0.0.0
2017-07-08 14:06:41.804	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:06:41.804	[P2P5]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:41.804	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:41.805	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:41.805	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:41.805	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:41.805	[P2P5]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:42.805	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1215	STARTED PEERLIST IDLE HANDSHAKE
2017-07-08 14:06:42.805	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1227	FINISHED PEERLIST IDLE HANDSHAKE
2017-07-08 14:06:43.805	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:43.805	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:06:43.805	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:06:43.805	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:06:43.805	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#13 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:45.794	[P2P3]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#8 to 0.0.0.0
2017-07-08 14:06:48.806	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 5.9.100.248:18080
2017-07-08 14:06:48.806	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:48.806	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:48.806	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:48.806	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:06:48.806	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:06:48.806	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:06:48.806	[P2P0]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#14 to 0.0.0.0 currently we have sockets count:7
2017-07-08 14:06:50.794	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#9 to 0.0.0.0
2017-07-08 14:06:53.807	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:06:53.807	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:06:53.807	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:53.807	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:53.807	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:53.807	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:53.807	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=0, max_index=2)
2017-07-08 14:06:53.807	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:06:55.794	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:172	Destructing connection p2p#10 to 0.0.0.0
2017-07-08 14:06:55.807	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:06:55.807	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 3438092305516468477 107.152.130.98:18080
2017-07-08 14:06:55.807	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 3438092305516468477 107.152.130.98:18080[white=1] last_seen: never
2017-07-08 14:06:55.808	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 107.152.130.98:18080(white=1, last_seen: never)...
2017-07-08 14:06:55.808	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#15 to 0.0.0.0 currently we have sockets count:6
2017-07-08 14:07:00.808	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:932	[0.0.0.0:0 OUT] Connect failed to 107.152.130.98:18080
2017-07-08 14:07:00.808	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1086	Handshake failed
2017-07-08 14:07:00.808	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:07:00.808	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:07:00.808	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=2(x=2, max_index=2)
2017-07-08 14:07:00.808	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:851	Random connection index=0(x=1, max_index=2)
2017-07-08 14:07:00.808	[P2P2]	INFO 	net.p2p	src/p2p/net_node.inl:1067	Considering connecting (out) to peer: 18098763612394748909 5.9.100.248:18080
2017-07-08 14:07:00.808	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:1083	Selected peer: 18098763612394748909 5.9.100.248:18080[white=1] last_seen: never
2017-07-08 14:07:00.809	[P2P2]	DEBUG	net.p2p	src/p2p/net_node.inl:918	Connecting to 5.9.100.248:18080(white=1, last_seen: never)...
2017-07-08 14:07:00.809	[P2P2]	INFO 	net.p2p	src/p2p/connection_basic.cpp:164	Spawned connection p2p#16 to 0.0.0.0 currently we have sockets count:7
status
Height: 1346603/1346603 (100.0%) on mainnet, not mining, net hash 99.90 MH/s, v5, up to date, 0(out)+0(in) connections, uptime 0d 0h 2m 21s

I left it running for longer(again) and it still did not connect to anyone.

# Discussion History
## moneromooo-monero | 2017-07-08T21:58:41+00:00
Try: telnet 5.9.100.248 18080
Does this connect ?

## fkdis | 2017-07-09T00:17:00+00:00
Trying 5.9.100.248...
telnet: Unable to connect to remote host: Connection timed out
However I got curios and a ping worked fine. 

## moneromooo-monero | 2017-07-09T10:35:24+00:00
Then a firewall of some sort is blocking connections. Find it, and fix it. monerod won't work till telnet works.

## moneromooo-monero | 2017-08-08T10:51:38+00:00
No response, and it wasn't a monerod thing since telnet also failed.

+invalid
+resolved

# Action History
- Created by: fkdis | 2017-07-08T20:12:42+00:00
- Closed at: 2017-08-08T10:54:14+00:00
