---
title: batch transaction mode already enabled
source_url: https://github.com/monero-project/monero/issues/3682
author: ghost
assignees: []
labels: []
created_at: '2018-04-23T00:06:51+00:00'
updated_at: '2018-08-16T19:24:54+00:00'
type: issue
status: closed
closed_at: '2018-08-16T19:24:54+00:00'
---

# Original Description
received a few batch transaction mode already enabled warnings when mining, the other threads were closed and seemed to all be suggesting an importing issues which is not the case here. MINT 18 latest compiled CLI

Only been here a short time, the Linux GUI failed/fails to load the daemon so switched to CLI but have been witnessing some warnings/errors so thought I would share before moving on a different project.

`2018-04-22 04:05:54.919	    7f8e0c2dc780	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-6f6521a)
2018-04-22 04:05:54.920	    7f8e0c2dc780	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-04-22 04:05:54.920	    7f8e0c2dc780	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-04-22 04:05:54.921	    7f8e0c2dc780	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-04-22 04:05:54.972	    7f8e0c2dc780	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-04-22 04:05:54.973	    7f8e0c2dc780	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-04-22 04:05:54.973	    7f8e0c2dc780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-04-22 04:05:54.973	    7f8e0c2dc780	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-04-22 04:05:54.974	    7f8e0c2dc780	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-04-22 04:05:54.975	    7f8e0c2dc780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder /home/brett/.bitmonero/lmdb ...
2018-04-22 04:05:55.306	    7f8e0c2dc780	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:525	Loading checkpoints
2018-04-22 04:05:56.619	    7f8e0c2dc780	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-04-22 04:05:56.619	    7f8e0c2dc780	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-04-22 04:05:56.619	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-04-22 04:05:56.622	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-04-22 04:05:57.624	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1386	
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization through "set_log <level|categories>" command,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).

Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************

2018-04-22 04:05:59.439	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[37.205.9.131:18080 OUT] Sync data returned a new top block candidate: 1556535 -> 1556537 [Your node is 2 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-04-22 04:06:07.640	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[37.205.9.131:18080 OUT]  Synced 1556537/1556537
2018-04-22 04:06:07.649	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	SYNCHRONIZED OK
2018-04-22 04:06:07.649	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1579	
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-04-22 04:06:11.061	[miner 0]	INFO 	global	src/cryptonote_basic/miner.cpp:434	Miner thread was started [0]
2018-04-22 04:06:11.062	[RPC1]	WARN 	miner	src/cryptonote_basic/miner.cpp:323	Mining has started with 4 threads, good luck!
2018-04-22 04:06:11.062	[miner 2]	INFO 	global	src/cryptonote_basic/miner.cpp:434	Miner thread was started [2]
2018-04-22 04:06:11.062	[miner 1]	INFO 	global	src/cryptonote_basic/miner.cpp:434	Miner thread was started [1]
2018-04-22 04:06:11.074	[miner 3]	INFO 	global	src/cryptonote_basic/miner.cpp:434	Miner thread was started [3]
2018-04-22 08:20:56.268	[P2P1]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556681
id:	<a6ebe9de95998c9eadf1abc70db7c241bae1d2f496623c33cfd213f626d33e6a>
PoW:	<a7e04a93d0df89e3a391aaa08b0f27221abd17c14ae25ccec3a12f0d00000000>
difficulty:	60813661243
2018-04-22 12:19:50.096	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[37.187.37.200:18080 OUT]  Synced 1556804/1556804
2018-04-22 12:19:50.098	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	SYNCHRONIZED OK
2018-04-22 12:22:53.752	[P2P7]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556803
id:	<e2930b963affaf596bb20e22f84789f8a5171c36629d91dd18abd441895b9312>
PoW:	<0da9d099b899872076e04a4504eff643de7bb5788271e8850e49910600000000>
difficulty:	62753916768
2018-04-22 12:23:20.491	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556804
id:	<a5b846923eb3f261650664da85009633a6bb346258fcbbe25349f046515b0314>
PoW:	<bc2291525b0feb7eec326c95805fdaea59d3cf6474b064fefcfba60700000000>
difficulty:	62640651889
2018-04-22 12:24:11.292	[P2P8]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556805
id:	<0387646785de7588e1322818177351602036ea7c983c712836538d125547b525>
PoW:	<343d1fdc325273315dfb0b8ce7c99fc41416e8f728ad1856df8a670d00000000>
difficulty:	62451300952
2018-04-22 12:24:25.922	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1464	###### REORGANIZE on height: 1556803 of 1556805 with cum_difficulty 13790955346848857
 alternative blockchain size: 4 with cum_difficulty 13791017805094086
2018-04-22 12:24:30.481	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556803
id:	<b12f2e549ef9ec8baa7609b533366f565b5a42e8da80806645853e57abd6d886>
PoW:	<4b4c6bf370605f8b3aab1c40805a5f199ee30ac64419205de8cda00c00000000>
difficulty:	62753916768
2018-04-22 12:24:30.575	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556804
id:	<7942f33dd4d303e0848080779ebe36c334635d0b1a3be828c647aadb4a89840b>
PoW:	<87404938b3c947d6c5bd233214d4cb85292878ac88429ba53578600300000000>
difficulty:	62640651889
2018-04-22 12:24:30.689	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556805
id:	<c7dae1ee1326e0e6036eb83155eceea5fc5a403a4c80c6c98ed2151c6acc8434>
PoW:	<87702c91bb03cb425249fb56b059dce66d7d5f2f4fa885595278f70300000000>
difficulty:	62451300952
2018-04-22 12:24:30.690	[P2P0]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2780	WARNING: batch transaction mode already enabled, but asked to enable batch mode
2018-04-22 12:24:31.316	[P2P0]	INFO 	global	src/cryptonote_core/blockchain.cpp:934	REORGANIZE SUCCESS! on height: 1556803, new blockchain size: 1556807
2018-04-22 13:06:53.395	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1167	[37.192.244.213:18080 OUT]  Synced 1556826/1556826
2018-04-22 13:06:53.395	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	SYNCHRONIZED OK
2018-04-22 14:00:17.279	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	SYNCHRONIZED OK
2018-04-22 14:05:29.575	[P2P8]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556854
id:	<fd5b08c2c2652de7d9c990075563020b80a17810e8bc99a9932e8ee25bfc96f5>
PoW:	<d8e4d041ad086ce02770f16cdd8397c01b93f5bac616a139f8b1450100000000>
difficulty:	62533633878
2018-04-22 14:06:49.800	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1464	###### REORGANIZE on height: 1556854 of 1556854 with cum_difficulty 13793995281986557
 alternative blockchain size: 2 with cum_difficulty 13794057825721827
2018-04-22 14:06:54.464	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:1475	----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1556854
id:	<ad4f84f4774d716f1cff9102b6271d450a7fe3a947f13a6e1f6427b01424ba32>
PoW:	<aab766a32f2b3bd26513cf27647f7a7d771be3244bf27f0188336e0700000000>
difficulty:	62533633878
2018-04-22 14:06:54.465	[P2P5]	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2780	WARNING: batch transaction mode already enabled, but asked to enable batch mode
2018-04-22 14:06:54.734	[P2P5]	INFO 	global	src/cryptonote_core/blockchain.cpp:934	REORGANIZE SUCCESS! on height: 1556854, new blockchain size: 1556856
2018-04-22 14:23:42.026	[P2P0]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:400	internal error: try to insert duplicate iterator in key_image set
2018-04-22 14:23:42.394	[P2P1]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:400	internal error: try to insert duplicate iterator in key_image set
2018-04-22 14:23:43.102	[P2P6]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:400	internal error: try to insert duplicate iterator in key_image set
2018-04-22 21:28:44.373	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	SYNCHRONIZED OK
2018-04-22 21:46:50.391	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[96.61.123.252:18080 OUT] Sync data returned a new top block candidate: 1557077 -> 1557478 [Your node is 401 blocks (0 days) behind] 
SYNCHRONIZATION started
2018-04-22 22:12:14.870	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1557	SYNCHRONIZED OK
` 

on a side note, here is a quick and dirty Shell script I was using to load the daemon, start mining and open a wallet https://pastebin.com/r5YexGvP


# Discussion History
## moneromooo-monero | 2018-04-23T08:50:02+00:00
The batch transaction warning is fine and can be ignored, it should be demoted to INFO I guess. The iterator messages are not fine, however, and will need fixing.


## moneromooo-monero | 2018-07-20T22:44:50+00:00
https://github.com/monero-project/monero/pull/4161 fixes the spurious warnings.
The iterator errors are already fixed in https://github.com/monero-project/monero/pull/3828


## moneromooo-monero | 2018-08-16T18:59:20+00:00
+resolved

# Action History
- Created by: ghost | 2018-04-23T00:06:51+00:00
- Closed at: 2018-08-16T19:24:54+00:00
