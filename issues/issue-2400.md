---
title: Monero GUI unable to connect remote node
source_url: https://github.com/monero-project/monero/issues/2400
author: AniketBhadane
assignees: []
labels: []
created_at: '2017-09-05T03:47:18+00:00'
updated_at: '2017-09-05T17:00:31+00:00'
type: issue
status: closed
closed_at: '2017-09-05T17:00:31+00:00'
---

# Original Description
I'm getting Network Status Disconnected in Monero GUI. I'm giving remote node daemon address as node.moneroworld.com:18089. I'm attaching bitmonero.log

> 2017-09-05 09:03:42.972	6512	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
> 2017-09-05 09:03:43.979	6512	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
> 2017-09-05 09:05:28.493	2120	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
> 2017-09-05 09:05:29.500	2120	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
> 2017-09-05 09:05:29.769	7912	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
> 2017-09-05 09:05:30.776	7912	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
> 2017-09-05 09:05:36.790	1468	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
> 2017-09-05 09:05:36.792	1468	INFO 	global	src/daemon/main.cpp:282	Monero 'Wolfram Warptangent' (v0.10.3.1-release)
> 2017-09-05 09:05:36.793	1468	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
> 2017-09-05 09:05:36.794	1468	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
> 2017-09-05 09:05:36.796	1468	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
> 2017-09-05 09:05:38.779	8368	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
> 2017-09-05 09:05:39.670	1468	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
> 2017-09-05 09:05:39.671	1468	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
> 2017-09-05 09:05:39.673	1468	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
> 2017-09-05 09:05:39.674	1468	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
> 2017-09-05 09:05:39.675	1468	INFO 	global	src/daemon/core.h:73	Initializing core...
> 2017-09-05 09:05:39.677	1468	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:326	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
> 2017-09-05 09:06:47.593	1468	INFO 	global	src/daemon/core.h:78	Core initialized OK
> 2017-09-05 09:06:47.594	1468	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
> 2017-09-05 09:06:47.596	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
> 2017-09-05 09:06:47.597	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
> 2017-09-05 09:06:48.599	[P2P7]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1098	[1;33m
> **********************************************************************
> The daemon will start synchronizing with the network. It may take up to several hours.
> 
> You can set the level of process detailization* through "set_log <level|categories>" command*,
> where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)
> 
> Use the "help" command to see the list of available commands.
> **********************************************************************
> [0m
> 2017-09-05 09:06:49.502	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[37.153.1.247:18080 OUT] Sync data returned a new top block candidate: 40601 -> 1392108 [Your node is 1351507 blocks (1203 days) behind] 
> SYNCHRONIZATION started
> 2017-09-05 09:07:01.140	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004	[1;33m[37.153.1.247:18080 OUT]  Synced 40801/1392108[0m
> 2017-09-05 09:07:03.957	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004	[1;33m[37.153.1.247:18080 OUT]  Synced 41001/1392108[0m
> 2017-09-05 09:07:07.450	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[188.216.222.80:18090 OUT] Sync data returned a new top block candidate: 41001 -> 1392109 [Your node is 1351108 blocks (1202 days) behind] 
> SYNCHRONIZATION started
> 2017-09-05 09:07:09.069	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004	[1;33m[37.153.1.247:18080 OUT]  Synced 41201/1392109[0m
> 

![monero](https://user-images.githubusercontent.com/15356930/30044472-dd8f8234-921a-11e7-914a-43e23f651c3a.JPG)


# Discussion History
## moneromooo-monero | 2017-09-05T07:56:11+00:00
That log looks like it's connected and syncing fine.


## AniketBhadane | 2017-09-05T07:59:44+00:00
In the initial few lines, there's:

2017-09-05 09:03:43.979	6512	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon

Also my data.mdb size is now more than 250MB. Is this expected in case of remote node? Also why is Network Status shown as Disconnected? Is it downloading the entire blockchain instead of connecting to remote node?

## dEBRUYNE-1 | 2017-09-05T16:51:44+00:00
Apparently node.moneroworld.com:18089 is down currently. See:

https://www.reddit.com/r/Monero/comments/6y5h5u/monero_gui_unable_to_connect_remote_node/dmlawae/

+resolved

# Action History
- Created by: AniketBhadane | 2017-09-05T03:47:18+00:00
- Closed at: 2017-09-05T17:00:31+00:00
