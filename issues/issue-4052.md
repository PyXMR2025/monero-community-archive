---
title: 'Exception: boost::thread_interrupted (Unwound call stack:)'
source_url: https://github.com/monero-project/monero/issues/4052
author: minzak
assignees: []
labels: []
created_at: '2018-06-25T15:43:01+00:00'
updated_at: '2018-06-26T10:45:22+00:00'
type: issue
status: closed
closed_at: '2018-06-26T10:45:22+00:00'
---

# Original Description
I use monero binaries on Debian 8 x64
Also i installed it:
**apt install pcscd libbz2-dev build-essential cmake pkg-config libboost-all-dev libssl-dev libzmq3-dev libunbound-dev libsodium-dev libminiupnpc-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev libgtest-dev doxygen graphviz**

And compiled boost v1.66

And i got this:

```
2018-06-25 15:46:28.908	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 18601/1602897[0m
2018-06-25 15:46:31.998	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 18701/1602897[0m
2018-06-25 15:46:38.022	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 18801/1602897[0m
2018-06-25 15:46:42.124	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 18901/1602897[0m
2018-06-25 15:46:45.531	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19001/1602897[0m
2018-06-25 15:46:48.518	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19101/1602897[0m
2018-06-25 15:46:51.947	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19201/1602897[0m
2018-06-25 15:46:52.789	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-06-25 15:46:52.940	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-06-25 15:46:52.940	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-06-25 15:46:52.943	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /usr/local/bin/monerod:__wrap___cxa_throw+0x10a [0x5560a756e0ea]
2018-06-25 15:46:52.943	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /usr/local/bin/monerod:boost::this_thread::interruption_point()+0x76 [0x5560a7911436]
2018-06-25 15:46:52.943	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /usr/local/bin/monerod:cryptonote::rpc::ZmqServer::serve()+0x895 [0x5560a7581635]
2018-06-25 15:46:52.943	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /usr/local/bin/monerod+0x99e5dd [0x5560a79115dd]
2018-06-25 15:46:52.943	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7ffaf9b72064]
2018-06-25 15:46:52.943	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7ffaf98a762d]
2018-06-25 15:46:52.943	    7ffaf61ae700	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-06-25 15:46:52.943	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-06-25 15:46:52.943	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-06-25 15:46:52.944	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-06-25 15:46:52.944	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-06-25 15:46:56.953	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-06-25 15:46:57.002	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-06-25 15:46:57.002	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-06-25 15:46:58.230	    7fda188e0780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:46:58.231	    7fda188e0780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:46:58.231	    7fda188e0780	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-25 15:46:58.231	    7fda188e0780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2018-06-25 15:46:58.234	    7fda188e0780	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.2.0-release) Daemonised
2018-06-25 15:46:58.234	    7fda188e0780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-06-25 15:46:58.234	    7fda188e0780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-06-25 15:46:58.235	    7fda188e0780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-06-25 15:47:02.258	    7fda188e0780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-06-25 15:47:02.260	    7fda188e0780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-06-25 15:47:02.260	    7fda188e0780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-06-25 15:47:02.260	    7fda188e0780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-06-25 15:47:02.261	    7fda188e0780	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-06-25 15:47:02.261	    7fda188e0780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /mnt/monero/lmdb ...
2018-06-25 15:47:02.343	    7fda188e0780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:526	Loading checkpoints
2018-06-25 15:47:02.370	    7fda188e0780	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-06-25 15:47:02.370	    7fda188e0780	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-06-25 15:47:02.370	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-06-25 15:47:02.370	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-06-25 15:47:03.371	[P2P2]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1354	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
[0m
2018-06-25 15:47:03.398	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[134.60.77.10:18080 OUT] Sync data returned a new top block candidate: 19201 -> 1602054 [Your node is 1582853 blocks (1509 days) behind] 
SYNCHRONIZATION started
2018-06-25 15:47:06.704	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[5.9.157.150:18080 OUT] Sync data returned a new top block candidate: 19201 -> 1602897 [Your node is 1583696 blocks (1510 days) behind] 
SYNCHRONIZATION started
2018-06-25 15:47:07.526	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19301/1602897[0m
2018-06-25 15:47:10.077	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19401/1602897[0m
2018-06-25 15:47:12.616	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19501/1602897[0m
2018-06-25 15:47:15.209	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19601/1602897[0m
2018-06-25 15:47:17.873	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19701/1602897[0m
2018-06-25 15:47:20.433	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19801/1602897[0m
2018-06-25 15:47:23.054	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 19901/1602897[0m
2018-06-25 15:47:25.694	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20001/1602897[0m
2018-06-25 15:47:28.391	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20101/1602897[0m
2018-06-25 15:47:31.602	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20201/1602897[0m
2018-06-25 15:47:37.451	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20301/1602897[0m
2018-06-25 15:47:41.236	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20401/1602897[0m
2018-06-25 15:47:44.054	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20501/1602897[0m
2018-06-25 15:47:50.164	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20601/1602897[0m
2018-06-25 15:47:56.015	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20701/1602897[0m
2018-06-25 15:47:59.306	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20801/1602897[0m
2018-06-25 15:48:03.165	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 20901/1602897[0m
2018-06-25 15:48:06.448	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 21001/1602897[0m
2018-06-25 15:48:10.945	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 21101/1602898[0m
2018-06-25 15:48:15.873	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 21201/1602898[0m
2018-06-25 15:48:19.340	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 21301/1602898[0m
2018-06-25 15:48:22.782	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 21401/1602898[0m
2018-06-25 15:48:26.427	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[134.60.77.10:18080 OUT]  Synced 21501/1602898[0m
2018-06-25 15:48:28.516	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-06-25 15:48:29.456	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-06-25 15:48:29.456	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-06-25 15:48:29.458	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /usr/local/bin/monerod:__wrap___cxa_throw+0x10a [0x55662787e0ea]
2018-06-25 15:48:29.458	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /usr/local/bin/monerod:boost::this_thread::interruption_point()+0x76 [0x556627c21436]
2018-06-25 15:48:29.458	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /usr/local/bin/monerod:cryptonote::rpc::ZmqServer::serve()+0x895 [0x556627891635]
2018-06-25 15:48:29.458	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /usr/local/bin/monerod+0x99e5dd [0x556627c215dd]
2018-06-25 15:48:29.458	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7fda17dac064]
2018-06-25 15:48:29.458	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fda17ae162d]
2018-06-25 15:48:29.458	    7fd9c3fff700	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-06-25 15:48:29.458	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-06-25 15:48:29.459	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-06-25 15:48:29.459	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-06-25 15:48:29.459	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-06-25 15:48:33.468	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-06-25 15:48:33.497	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-06-25 15:48:33.497	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-06-25 15:48:34.731	    7fd0a4f98780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:48:34.731	    7fd0a4f98780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:48:34.731	    7fd0a4f98780	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-25 15:48:34.731	    7fd0a4f98780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2018-06-25 15:48:34.734	    7fd0a4f98780	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.2.0-release) Daemonised
2018-06-25 15:48:34.734	    7fd0a4f98780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-06-25 15:48:34.734	    7fd0a4f98780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-06-25 15:48:34.735	    7fd0a4f98780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-06-25 15:48:38.755	    7fd0a4f98780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-06-25 15:48:38.756	    7fd0a4f98780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-06-25 15:48:38.756	    7fd0a4f98780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-06-25 15:48:38.756	    7fd0a4f98780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-06-25 15:48:38.756	    7fd0a4f98780	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-06-25 15:48:38.757	    7fd0a4f98780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /mnt/monero/lmdb ...
2018-06-25 15:48:38.836	    7fd0a4f98780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:526	Loading checkpoints
2018-06-25 15:48:38.855	    7fd0a4f98780	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-06-25 15:48:38.855	    7fd0a4f98780	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-06-25 15:48:38.855	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-06-25 15:48:38.856	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-06-25 15:48:39.856	[P2P3]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1354	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
[0m
2018-06-25 15:48:44.890	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[5.9.157.150:18080 OUT] Sync data returned a new top block candidate: 21501 -> 1602898 [Your node is 1581397 blocks (1509 days) behind] 
SYNCHRONIZATION started
2018-06-25 15:48:48.163	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 21601/1602898[0m
2018-06-25 15:48:56.851	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 21701/1602898[0m
2018-06-25 15:48:59.489	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 21801/1602898[0m
2018-06-25 15:49:02.483	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 21901/1602898[0m
2018-06-25 15:49:05.029	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22001/1602898[0m
2018-06-25 15:49:07.808	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22101/1602898[0m
2018-06-25 15:49:10.509	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22201/1602898[0m
2018-06-25 15:49:13.054	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22301/1602898[0m
2018-06-25 15:49:18.209	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22401/1602898[0m
2018-06-25 15:49:21.648	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22501/1602898[0m
2018-06-25 15:49:27.067	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22601/1602898[0m
2018-06-25 15:49:30.584	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22701/1602898[0m
2018-06-25 15:49:33.775	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22801/1602898[0m
2018-06-25 15:49:37.786	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 22901/1602898[0m
2018-06-25 15:49:40.635	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 23001/1602898[0m
2018-06-25 15:49:44.404	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 23101/1602898[0m
2018-06-25 15:49:49.932	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 23201/1602898[0m
2018-06-25 15:49:53.232	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 23301/1602898[0m
2018-06-25 15:49:56.562	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 23401/1602898[0m
2018-06-25 15:50:03.728	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 23501/1602898[0m
2018-06-25 15:50:05.224	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-06-25 15:50:05.925	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-06-25 15:50:05.925	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-06-25 15:50:05.927	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /usr/local/bin/monerod:__wrap___cxa_throw+0x10a [0x55b5adc5e0ea]
2018-06-25 15:50:05.927	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /usr/local/bin/monerod:boost::this_thread::interruption_point()+0x76 [0x55b5ae001436]
2018-06-25 15:50:05.927	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /usr/local/bin/monerod:cryptonote::rpc::ZmqServer::serve()+0x895 [0x55b5adc71635]
2018-06-25 15:50:05.927	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /usr/local/bin/monerod+0x99e5dd [0x55b5ae0015dd]
2018-06-25 15:50:05.927	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7fd0a4464064]
2018-06-25 15:50:05.927	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fd0a419962d]
2018-06-25 15:50:05.927	    7fd0a0aa0700	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-06-25 15:50:05.928	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-06-25 15:50:05.928	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-06-25 15:50:05.928	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-06-25 15:50:05.928	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-06-25 15:50:09.938	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-06-25 15:50:09.941	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-06-25 15:50:09.941	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-06-25 15:50:11.231	    7fa3994ed780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:50:11.231	    7fa3994ed780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:50:11.231	    7fa3994ed780	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-25 15:50:11.232	    7fa3994ed780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2018-06-25 15:50:11.234	    7fa3994ed780	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.2.0-release) Daemonised
2018-06-25 15:50:11.234	    7fa3994ed780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-06-25 15:50:11.234	    7fa3994ed780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-06-25 15:50:11.235	    7fa3994ed780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-06-25 15:50:15.262	    7fa3994ed780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-06-25 15:50:15.262	    7fa3994ed780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-06-25 15:50:15.262	    7fa3994ed780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-06-25 15:50:15.262	    7fa3994ed780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-06-25 15:50:15.262	    7fa3994ed780	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-06-25 15:50:15.263	    7fa3994ed780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /mnt/monero/lmdb ...
2018-06-25 15:50:15.349	    7fa3994ed780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:526	Loading checkpoints
2018-06-25 15:50:15.373	    7fa3994ed780	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-06-25 15:50:15.373	    7fa3994ed780	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-06-25 15:50:15.373	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-06-25 15:50:15.374	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-06-25 15:50:16.374	[P2P2]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1354	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
[0m
2018-06-25 15:50:16.401	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[5.9.157.150:18080 OUT] Sync data returned a new top block candidate: 23501 -> 1602898 [Your node is 1579397 blocks (1507 days) behind] 
SYNCHRONIZATION started
2018-06-25 15:50:18.977	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 23601/1602898[0m
2018-06-25 15:50:28.843	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 23701/1602898[0m
2018-06-25 15:50:53.015	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 23801/1602900[0m
2018-06-25 15:51:00.116	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 23901/1602900[0m
2018-06-25 15:51:03.762	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24001/1602900[0m
2018-06-25 15:51:07.978	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24101/1602900[0m
2018-06-25 15:51:12.457	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24201/1602900[0m
2018-06-25 15:51:16.680	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24301/1602900[0m
2018-06-25 15:51:22.428	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24401/1602900[0m
2018-06-25 15:51:28.808	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24501/1602900[0m
2018-06-25 15:51:32.661	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24601/1602900[0m
2018-06-25 15:51:41.560	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[37.59.44.25:18080 OUT]  Synced 24701/1602900[0m
2018-06-25 15:51:41.814	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-06-25 15:51:42.469	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: boost::thread_interrupted
2018-06-25 15:51:42.469	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-06-25 15:51:42.471	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /usr/local/bin/monerod:__wrap___cxa_throw+0x10a [0x55de356400ea]
2018-06-25 15:51:42.471	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /usr/local/bin/monerod:boost::this_thread::interruption_point()+0x76 [0x55de359e3436]
2018-06-25 15:51:42.471	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /usr/local/bin/monerod:cryptonote::rpc::ZmqServer::serve()+0x895 [0x55de35653635]
2018-06-25 15:51:42.471	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /usr/local/bin/monerod+0x99e5dd [0x55de359e35dd]
2018-06-25 15:51:42.471	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7fa3989b9064]
2018-06-25 15:51:42.471	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fa3986ee62d]
2018-06-25 15:51:42.471	    7fa394ff5700	INFO 	stacktrace	src/common/stack_trace.cpp:163	
2018-06-25 15:51:42.472	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-06-25 15:51:42.472	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-06-25 15:51:42.472	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-06-25 15:51:42.472	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-06-25 15:51:46.480	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-06-25 15:51:46.508	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-06-25 15:51:46.508	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-06-25 15:51:47.731	    7fac84e63780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:51:47.731	    7fac84e63780	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-25 15:51:47.731	    7fac84e63780	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-25 15:51:47.732	    7fac84e63780	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2018-06-25 15:51:47.735	    7fac84e63780	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.2.0-release) Daemonised
2018-06-25 15:51:47.736	    7fac84e63780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-06-25 15:51:47.736	    7fac84e63780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-06-25 15:51:47.736	    7fac84e63780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-06-25 15:51:51.759	    7fac84e63780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-06-25 15:51:51.760	    7fac84e63780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-06-25 15:51:51.760	    7fac84e63780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-06-25 15:51:51.760	    7fac84e63780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-06-25 15:51:51.760	    7fac84e63780	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-06-25 15:51:51.760	    7fac84e63780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /mnt/monero/lmdb ...
2018-06-25 15:51:51.840	    7fac84e63780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:526	Loading checkpoints
2018-06-25 15:51:51.862	    7fac84e63780	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-06-25 15:51:51.862	    7fac84e63780	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-06-25 15:51:51.862	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-06-25 15:51:51.862	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-06-25 15:51:52.863	[P2P2]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1354	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
[0m
2018-06-25 15:51:52.903	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[5.9.157.150:18080 OUT] Sync data returned a new top block candidate: 24701 -> 1602900 [Your node is 1578199 blocks (1507 days) behind] 
SYNCHRONIZATION started
2018-06-25 15:52:02.596	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 24801/1602900[0m
2018-06-25 15:52:06.305	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 24901/1602900[0m
2018-06-25 15:52:16.852	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 25001/1602900[0m
2018-06-25 15:52:21.054	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 25101/1602900[0m
2018-06-25 15:52:30.138	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 25201/1602900[0m
2018-06-25 15:52:33.626	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 25301/1602900[0m
2018-06-25 15:52:36.966	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171	[1;33m[5.9.157.150:18080 OUT]  Synced 25401/1602900[0m

```

What wrong?
It crashes many times and systemd restart it

# Discussion History
## moneromooo-monero | 2018-06-25T17:18:18+00:00
systemd is shit by default. Use --non-interactive, or the systemd config file from the monero tree.


## minzak | 2018-06-25T17:22:44+00:00
) I know, but not matter how to run node, main question why it always crashed!? Need Increase verbosity? it can helps?
P.S. I add --non-interactive to exec string.

## minzak | 2018-06-26T10:45:22+00:00
answer here - https://github.com/monero-project/monero/issues/4051

# Action History
- Created by: minzak | 2018-06-25T15:43:01+00:00
- Closed at: 2018-06-26T10:45:22+00:00
