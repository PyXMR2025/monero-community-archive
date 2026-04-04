---
title: 'Error: Couldn''t connect to daemon (after importing blockchain.raw)'
source_url: https://github.com/monero-project/monero/issues/3742
author: WPFilmmaker
assignees: []
labels: []
created_at: '2018-05-01T16:02:50+00:00'
updated_at: '2022-04-08T14:43:44+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:43:44+00:00'
---

# Original Description
 Hi all, first of all I am sorry if this is a duplicate, I couldn't find anything about it. I am a new user. I imported blockchain.raw in the latest monero v0.12.0.0 (the latest string is "block 1266430 / 1546605"  therefore I am assuming everything went good). However after importing it and starting the wallet I can't  start the daemon anymore. Before mporting the blockchain everything was fine. I get the following error:

`"starting monerod /home/marco/Downloads/monero-gui-v0.12.0.0/monerod"
With command line arguments  ("--detach", "--data-dir", "/home/marco/Downloads", "--check-updates", "disabled")
2018-05-01 15:49:42.609	    7fb0623cd740	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
Forking to background...
sending external cmd:  ("status")
"Error: Couldn't connect to daemon: 127.0.0.1:18081\n"
daemon not running. checking again in 2 seconds.
sending external cmd:  ("status")
`

I saw that this is the same error as #2480 however that ticket was closed as a fix was released (and relates to an older version).

Has anyone have an idea about how I can fix this?

Edit: the terminal update to block "1271550 / 1546605" so it hasn't finished! I will let you updated once it finishes for real.


# Discussion History
## moneromooo-monero | 2018-05-01T16:41:41+00:00
The import file may be incomplete. The remainder would be synced off the network. Even if the import stopped partway through, monerod should work (and sync from that point).

Anyway, what software is printing the log you print ? It seems to be running monerod, but I see no monerod error. Check in ~/.bitmonero/bitmonero.log for the actual monerod messages.


## WPFilmmaker | 2018-05-03T15:47:19+00:00
I mported the blockchain corretly but it didn't matter as I can't still connect. @moneromooo-monero that output was from the terminal so I am assuming it was moneror.
This is the log:
`**********************************************************************
[0m
2018-04-30 20:43:00.039	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[103.60.164.111:18080 OUT] Sync data returned a new top block candidate: 1255094 -> 1562794 [Your node is 307700 blocks (427 days) behind] 
SYNCHRONIZATION started
2018-04-30 20:43:06.773	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255114/1562794[0m
2018-04-30 20:43:12.209	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255134/1562794[0m
2018-04-30 20:43:15.617	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255154/1562794[0m
2018-04-30 20:43:20.127	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255174/1562794[0m
2018-04-30 20:43:25.085	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255194/1562794[0m
2018-04-30 20:43:28.195	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255214/1562794[0m
2018-04-30 20:43:33.859	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255234/1562794[0m
2018-04-30 20:43:38.025	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255254/1562794[0m
2018-04-30 20:43:53.903	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255274/1562794[0m
2018-04-30 20:43:56.180	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255294/1562794[0m
2018-04-30 20:44:00.048	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255314/1562794[0m
2018-04-30 20:44:04.381	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255334/1562794[0m
2018-04-30 20:44:07.031	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255354/1562794[0m
2018-04-30 20:44:09.946	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255374/1562794[0m
2018-04-30 20:44:15.130	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255394/1562794[0m
2018-04-30 20:44:20.410	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255414/1562794[0m
2018-04-30 20:44:23.885	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255434/1562794[0m
2018-04-30 20:44:26.367	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255454/1562794[0m
2018-04-30 20:44:42.863	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255474/1562794[0m
2018-04-30 20:44:46.079	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255494/1562794[0m
2018-04-30 20:44:49.156	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255514/1562794[0m
2018-04-30 20:44:51.732	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255534/1562794[0m
2018-04-30 20:44:54.867	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255554/1562794[0m
2018-04-30 20:44:57.995	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255574/1562794[0m
2018-04-30 20:45:01.264	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255594/1562794[0m
2018-04-30 20:45:05.722	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255614/1562794[0m
2018-04-30 20:45:09.209	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255634/1562794[0m
2018-04-30 20:45:12.887	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255654/1562794[0m
2018-04-30 20:45:34.724	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255674/1562794[0m
2018-04-30 20:45:38.895	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255694/1562794[0m
2018-04-30 20:45:42.840	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255714/1562794[0m
2018-04-30 20:45:44.506	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255734/1562794[0m
2018-04-30 20:45:47.887	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255754/1562794[0m
2018-04-30 20:45:50.832	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255774/1562794[0m
2018-04-30 20:45:53.166	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255794/1562794[0m
2018-04-30 20:45:55.936	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255814/1562794[0m
2018-04-30 20:45:59.773	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255834/1562794[0m
2018-04-30 20:46:03.630	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255854/1562794[0m
2018-04-30 20:46:13.787	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255874/1562794[0m
2018-04-30 20:46:24.963	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255894/1562794[0m
2018-04-30 20:46:30.878	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255914/1562794[0m
2018-04-30 20:46:36.329	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255934/1562794[0m
2018-04-30 20:46:37.962	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255954/1562794[0m
2018-04-30 20:46:40.340	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255974/1562794[0m
2018-04-30 20:46:42.563	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1255994/1562794[0m
2018-04-30 20:46:44.907	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1256014/1562794[0m
2018-04-30 20:46:47.407	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1256034/1562794[0m
2018-04-30 20:46:49.686	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1256054/1562794[0m
2018-04-30 20:47:08.290	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1256074/1562794[0m
2018-04-30 20:47:10.658	    7f04e492d740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-30 20:47:10.859	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[1;33m[172.104.224.250:51810 OUT]  Synced 1256094/1562794[0m
2018-04-30 20:47:10.862	    7f04e492d740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 1256074/1562794 (80.4%) on mainnet, not mining, net hash 61.36 MH/s, v4, up to date, 8(out)+0(in) connections, uptime 0d 0h 4m 44s
2018-04-30 20:47:13.464	    7efd4131f740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-30 20:47:13.465	    7efd4131f740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Stop signal sent
2018-04-30 20:47:16.482	    7f85c6649740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-30 20:47:16.778	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-04-30 20:47:16.780	    7f85c6649740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 1256095/1562794 (80.4%) on mainnet, not mining, net hash 61.60 MH/s, v4, up to date, 8(out)+0(in) connections, uptime 0d 0h 4m 50s
2018-04-30 20:47:16.863	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-04-30 20:47:16.863	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-04-30 20:47:16.865	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /home/marco/Downloads/monero-gui-v0.12.0.0/monerod:__wrap___cxa_throw+0x10a [0x5600bef461ba]
2018-04-30 20:47:16.865	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /home/marco/Downloads/monero-gui-v0.12.0.0/monerod:boost::this_thread::interruption_point()+0x76 [0x5600bf2dcff6]
2018-04-30 20:47:16.865	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /home/marco/Downloads/monero-gui-v0.12.0.0/monerod:cryptonote::rpc::ZmqServer::serve()+0x895 [0x5600bef59705]
2018-04-30 20:47:16.865	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /home/marco/Downloads/monero-gui-v0.12.0.0/monerod+0x9870c5 [0x5600bf2dd0c5]
2018-04-30 20:47:16.865	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x76ba [0x7f9d6dd596ba]
2018-04-30 20:47:16.865	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7f9d6da8f41d]
2018-04-30 20:47:16.865	    7f9d6a37e700	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-04-30 20:47:16.865	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-04-30 20:47:16.865	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-04-30 20:47:16.866	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-04-30 20:47:16.866	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-04-30 20:47:20.889	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-04-30 20:47:21.540	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-04-30 20:47:21.540	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-05-01 14:53:52.895	    7fe0e0d1a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 14:53:52.946	    7fe0e0d1a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 14:53:57.094	    7f1fd7beb740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 14:53:57.094	    7f1fd7beb740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 14:54:41.677	    7f4b5e34a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 14:54:41.678	    7f4b5e34a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 14:54:44.687	    7fce935df740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 14:54:44.707	    7fce935df740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 1/1 (100.0%) on mainnet, not mining, net hash 0 H/s, v1, up to date, 0(out)+0(in) connections, uptime 0d 0h 0m 1s
2018-05-01 14:56:58.815	    7f3869dc7740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 14:56:58.898	    7f3869dc7740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 61028/1563318 (3.9%) on mainnet, not mining, net hash 3.80 MH/s, v1, up to date, 8(out)+0(in) connections, uptime 0d 0h 2m 15s
2018-05-01 14:57:01.611	    7fad65914740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 14:57:02.112	    7fad65914740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Stop signal sent
2018-05-01 14:57:05.125	    7f09c14e4740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 14:57:05.126	    7f09c14e4740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:12:07.979	    7f86072e3740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:12:07.979	    7f86072e3740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:12:22.010	    7f14a5b82740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:12:22.011	    7f14a5b82740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:12:25.031	    7f844e32d740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:12:25.033	    7f844e32d740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:12:28.049	    7ffa50a09740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:12:28.054	    7ffa50a09740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Height: 61428/61428 (100.0%) on mainnet, not mining, net hash 4.22 MH/s, v1, up to date, 0(out)+0(in) connections, uptime 0d 0h 0m 3s
2018-05-01 15:48:33.395	    7ff39ef22740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:48:33.631	    7ff39ef22740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:48:47.690	    7fcad563e740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:48:47.690	    7fcad563e740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:48:50.701	    7f6fcf53a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:48:50.702	    7f6fcf53a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:48:53.715	    7fa22b2ca740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:48:53.716	    7fa22b2ca740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:48:56.728	    7faa85118740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:48:56.729	    7faa85118740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:48:59.740	    7f17b5b04740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:48:59.741	    7f17b5b04740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:02.752	    7f87c1f66740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:02.753	    7f87c1f66740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:05.769	    7f3a4b31a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:05.769	    7f3a4b31a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:08.781	    7f6a46fd1740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:08.782	    7f6a46fd1740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:11.795	    7fddad368740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:11.796	    7fddad368740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:14.809	    7f2e057bf740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:14.810	    7f2e057bf740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:44.610	    7fe89f53a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:44.611	    7fe89f53a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:47.621	    7f28306d2740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:47.621	    7f28306d2740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:50.631	    7f7f12717740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:50.632	    7f7f12717740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:53.643	    7f3710db3740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:53.644	    7f3710db3740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:56.654	    7f3f32f39740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:56.655	    7f3f32f39740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:49:59.664	    7fac3f744740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:49:59.665	    7fac3f744740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:50:02.677	    7fd0412b8740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:50:02.678	    7fd0412b8740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:50:05.687	    7f18646e6740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:50:05.688	    7f18646e6740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:50:08.698	    7facf4f67740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:50:08.699	    7facf4f67740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 15:50:11.712	    7f597d41d740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 15:50:11.713	    7f597d41d740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-01 16:02:58.470	    7f853273e740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-01 16:02:58.471	    7f853273e740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:23.812	    7fe722b15740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:23.938	    7fe722b15740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:37.975	    7f2c13f0a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:37.975	    7f2c13f0a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:40.988	    7f5f57a0a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:41.437	    7f5f57a0a740	ERROR	net.http	contrib/epee/include/net/http_client.h:456	Unexpected recv fail
2018-05-02 02:24:41.438	    7f5f57a0a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Problem fetching info-- rpc_request: 
2018-05-02 02:24:44.451	    7fc36f8bd740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:44.452	    7fc36f8bd740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:47.466	    7fe39c0b8740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:47.467	    7fe39c0b8740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:50.479	    7f7be245e740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:50.481	    7f7be245e740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:53.506	    7ff82dcdb740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:53.507	    7ff82dcdb740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:56.543	    7f1b61890740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:56.545	    7f1b61890740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:24:59.559	    7f4a75389740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:24:59.560	    7f4a75389740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:25:02.581	    7f59c5d57740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:25:02.582	    7f59c5d57740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:25:05.598	    7f8594f7e740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:25:05.599	    7f8594f7e740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-02 02:25:30.429	    7f0c62627740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-02 02:25:30.430	    7f0c62627740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:42:54.411	    7f7508b81740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:42:54.539	    7f7508b81740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:08.599	    7f8d5a1da740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:08.600	    7f8d5a1da740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:11.612	    7f8e44356740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:11.613	    7f8e44356740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:14.626	    7f7ec317c740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:14.627	    7f7ec317c740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:17.641	    7ff8cb325740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:17.642	    7ff8cb325740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:20.655	    7fe229db0740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:20.655	    7fe229db0740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:23.670	    7f9730686740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:23.671	    7f9730686740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:26.683	    7f6aa765a740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:26.684	    7f6aa765a740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:29.702	    7fd44e319740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:29.703	    7fd44e319740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:32.715	    7f425c340740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:32.716	    7f425c340740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2018-05-03 15:43:35.731	    7fd38fbc1740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-03 15:43:35.732	    7fd38fbc1740	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
`

Apologies for the lenght but I don't know how to format in github :/

## moneromooo-monero | 2018-05-04T10:49:15+00:00
To format, you add a line with \`\`\` before the log, then a line with \`\`\` after it. There seems nothing wrong at first glance. The daemon seems to stop normally at some point. Try running monerod this way (stop the GUI first):

monerod --log-level 1

Add the path to the binary to match your system of course.

## WPFilmmaker | 2018-05-12T15:02:57+00:00
@moneromooo-monero Sorry for the late reply, I ran ./monerod --log-level 1 in the monero folder, but from the terminal it seems to be checking the blockchain not opening the wallet , am I doing something wrong?

## moneromooo-monero | 2018-05-12T16:19:50+00:00
monerod syncs the blockchain, monero-wallet-cli sync the wallet (using monerod). Syncing the daemon does not need a wallet.

## moneromooo-monero | 2018-09-09T12:15:22+00:00
I'm not sure what the problem is supposed to be here.
Is this still happening with 0.12.3.0 ?


## selsta | 2022-04-08T14:43:44+00:00
Closing, no reply.

# Action History
- Created by: WPFilmmaker | 2018-05-01T16:02:50+00:00
- Closed at: 2022-04-08T14:43:44+00:00
