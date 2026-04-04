---
title: monerod can't sync, stop on height 1548539
source_url: https://github.com/monero-project/monero/issues/3613
author: fanmaomao
assignees: []
labels: []
created_at: '2018-04-12T06:12:38+00:00'
updated_at: '2018-04-12T07:05:08+00:00'
type: issue
status: closed
closed_at: '2018-04-12T07:05:08+00:00'
---

# Original Description
this is the daemon log : 

```
2018-04-12 02:21:17.485	    7f53047d0740	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-12 02:21:17.485	    7f53047d0740	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-04-12 02:21:17.486	    7f53047d0740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Forking to background...
2018-04-12 02:21:17.487	    7f53047d0740	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.0.0-master-release) Daemonised
2018-04-12 02:21:17.495	    7f53047d0740	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-04-12 02:21:17.496	    7f53047d0740	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-04-12 02:21:17.497	    7f53047d0740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-04-12 02:21:18.916	    7f53047d0740	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-04-12 02:21:18.916	    7f53047d0740	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-04-12 02:21:18.917	    7f53047d0740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-04-12 02:21:18.917	    7f53047d0740	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-04-12 02:21:18.917	    7f53047d0740	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-04-12 02:21:18.919	    7f53047d0740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /home/monerodaemon/.bitmonero/lmdb ...
2018-04-12 02:25:35.947	    7f53047d0740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:525	Loading checkpoints
2018-04-12 02:25:36.238	    7f53047d0740	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-04-12 02:25:36.631	    7f53047d0740	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-04-12 02:25:36.631	    7f53047d0740	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-04-12 02:25:36.631	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-04-12 02:25:36.641	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-04-12 02:25:37.642	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1386	
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2018-04-12 02:25:38.256	[P2P1]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-04-12 02:25:39.849	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[80.6.160.104:18080 OUT] Sync data returned a new top block candidate: 1548539 -> 1548540 [Your node is 1 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-04-12 02:25:41.568	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[94.130.75.17:18080 OUT] Sync data returned a new top block candidate: 1548539 -> 1549299 [Your node is 760 blocks (1 days) behind] 
SYNCHRONIZATION started
2018-04-12 02:26:23.570	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1546000
id:	<b408bf4cfcd7de13e7e370c84b8314c85b24f0ba4093ca1d6eeb30b35e34e91a>
PoW:	<2a7cfab56266ea8ec7902b94b59abd7f38a13c3d84d704ebf4fa1a0100000000>
difficulty:	134716086238
2018-04-12 02:26:23.652	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1546001
id:	<6bf1de4ef6333d7b36265e1aef6c5eb771218b4a4936a667d5c839505f08b427>
PoW:	<4922b86c0134e519c157c799b2e9563e715033c006092473381d880400000000>
difficulty:	134683006645
2018-04-12 02:26:23.728	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1546002
id:	<ec59a5a72f04f56dd326e9ed5a271fae126287cad85d6b167561fba180228a64>
PoW:	<065e5e70f63e929ea50a3a46ef1f92bd8a48cb0d7d72f18d4b41ec0500000000>
difficulty:	134898041182
2018-04-12 02:26:23.818	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1546003
id:	<7a7f83110d0dc0d0589b1a5fc48bfd8b817e7151cf3cdb35dfc1adf4615019a0>
PoW:	<c1d13c8cc35016bdb367bf39b6aef64646fe727d873f5bfa63b3570600000000>
difficulty:	134673716587
2018-04-12 02:26:23.910	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1546004
id:	<2254825fdea624f240b829a20c809a521500962fd4c936cc24e0f1ed1d9f635c>
PoW:	<ea8b2f3ca13248037e799b3fd4d04c4f30c93d2b9b4bd3e2de4d050800000000>
difficulty:	134664906146
2018-04-12 02:26:24.004	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1546005
id:	<c7704ed04367ad29120ef5f3f7f7e54d4b352ea751b391248c709c51c5dc402a>
PoW:	<0614422c792f9937fe33e5b30b190b6a508e3f83291a2737511a4c0100000000>
difficulty:	134662100105

...
...
...

2018-04-12 03:37:54.835	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1548556
id:	<b1d60b63c018e2ca06104eea69d3fd51c5992b17985cc60fd68d1bba1763f59e>
PoW:	<4364cf8a00847bb89d450a7f71d6444e9f20dcdacc6f073bf6ccc20300000000>
difficulty:	56899019563
2018-04-12 03:37:54.900	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1548557
id:	<f416bb5a7ecca289a45492c9670e0762dfcf3aeccf370d94552b00b19d067a45>
PoW:	<6d57ea0daeafed046d15e82bfff4ead41fb03ff184190c8be3ba2a0c00000000>
difficulty:	56907737796
2018-04-12 03:37:54.964	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1548558
id:	<cc354fc1a680bc7bdb56c637fd8d672286a56a0785ae2d0b35b295c31b2e5ebe>
PoW:	<ee751070511aa5f034ffd1265766f1ee8f8668c40f3a9a499236d20600000000>
difficulty:	56952022867
2018-04-12 03:37:55.029	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1548559
id:	<3c6ae65eb9cd654f99818cfd32f82d19e23e621bb5ede04d14cc48df728c6d8b>
PoW:	<bdc10fcb06af0e39e8b3d5fb60df4acc5a39d8c232c1e9e37fc68f0800000000>
difficulty:	57153652658
2018-04-12 03:38:58.113	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[145.239.74.203:18080 OUT] Sync data returned a new top block candidate: 1548539 -> 1549330 [Your node is 791 blocks (1 days) behind] 
SYNCHRONIZATION started
2018-04-12 03:46:26.627	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[107.161.31.12:18080 OUT] Sync data returned a new top block candidate: 1548539 -> 1549333 [Your node is 794 blocks (1 days) behind] 
SYNCHRONIZATION started
2018-04-12 03:47:48.109	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[107.161.31.12:18080 OUT] Sync data returned a new top block candidate: 1548539 -> 1549334 [Your node is 795 blocks (1 days) behind] 
SYNCHRONIZATION started
2018-04-12 03:49:55.665	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[37.10.71.87:18080 OUT] Sync data returned a new top block candidate: 1548539 -> 1549335 [Your node is 796 blocks (1 days) behind] 
SYNCHRONIZATION started
```

i restart the daemon many times, but still does not work

# Discussion History
# Action History
- Created by: fanmaomao | 2018-04-12T06:12:38+00:00
- Closed at: 2018-04-12T07:05:08+00:00
