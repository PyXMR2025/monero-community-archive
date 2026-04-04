---
title: Input/Output error - Core Dumped in VBox
source_url: https://github.com/monero-project/monero/issues/3330
author: jodobear
assignees: []
labels: []
created_at: '2018-02-28T23:31:03+00:00'
updated_at: '2022-03-16T15:31:22+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:31:22+00:00'
---

# Original Description
Hi All!

I've been trying to sync monero for more than 3 weeks now and i have been having a consistent issue with that. I am new to this so maybe missing some info, sorry about that but, if this reporting helps and somebody can help me that would be appreciated:

**System info:**
Host: Windows 10
Guest running on VBox 5.2.6 r120293: Mint Sylvia 18.3 with 4 cores of i7 8th gen U processor & 4GB RAM

**Issue Description**
I run `./monerod`, monero starts syncing and after a while it stops giving me the error 
`ERROR	blockchain	src/cryptonote_core/blockchain.cpp:420	Error syncing blockchain db: Failed to sync database: Input/output error-- shutting down now to prevent issues!
terminate called after throwing an instance of 'cryptonote::DB_ERROR'
  what():  Failed to sync database: Input/output error
Aborted (core dumped)`
I run `./monerod` again and it starts syncing and after a while it stops again without any damage to the blockchain. This has been happening several times.
At first it gave me `Bus Error : core dumped`. After searching for the issue i ran `./monerod --db-salvage` and it started, synced for a while and then the `Input/Output error` started. Don't know what's happening here. Following is the log from the terminal:

**Monero Log**

`Use the "help" command to see the list of available commands.
**********************************************************************

2018-02-28 14:32:18.766	[P2P1]	WARN 	global	src/cryptonote_core/cryptonote_core.cpp:1282	**********************************************************************
2018-02-28 14:32:18.766	[P2P1]	WARN 	global	src/cryptonote_core/cryptonote_core.cpp:1283	Last scheduled hard fork time shows a daemon update is needed now.
2018-02-28 14:32:18.766	[P2P1]	WARN 	global	src/cryptonote_core/cryptonote_core.cpp:1284	**********************************************************************
2018-02-28 14:32:19.215	[P2P1]	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-02-28 14:32:19.547	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[83.128.251.73:18080 OUT] Sync data returned a new top block candidate: 471179 -> 1519487 [Your node is 1048308 blocks (1081 days) behind] 
SYNCHRONIZATION started
2018-02-28 14:32:53.413	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[83.128.251.73:18080 OUT]  Synced 471279/1519487
2018-02-28 14:33:07.479	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[83.128.251.73:18080 OUT]  Synced 471379/1519487
2018-02-28 14:33:21.353	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[83.128.251.73:18080 OUT]  Synced 471479/1519487
                                ***clipped***

2018-02-28 15:46:58.305	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[83.128.251.73:18080 OUT]  Synced 482078/1519552
2018-02-28 15:50:01.354	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[47.185.200.233:18080 OUT] Sync data returned a new top block candidate: 482178 -> 1519553 [Your node is 1037375 blocks (1073 days) behind] 
SYNCHRONIZATION started
2018-02-28 15:50:01.357	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[83.128.251.73:18080 OUT]  Synced 482178/1519552
2018-02-28 15:50:32.066	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[83.128.251.73:18080 OUT]  Synced 482278/1519553
2018-02-28 15:51:28.405	    7f2acd8f2700	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:72	Failed to sync database: Input/output error
2018-02-28 15:51:29.830	    7f2acd8f2700	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:420	Error syncing blockchain db: Failed to sync database: Input/output error-- shutting down now to prevent issues!
terminate called after throwing an instance of 'cryptonote::DB_ERROR'
  what():  Failed to sync database: Input/output error
Aborted (core dumped)
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $ ./monerod
2018-02-28 18:11:12.785	    7f67161f2740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-02-28 18:11:12.785	    7f67161f2740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2018-02-28 18:11:12.785	    7f67161f2740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2018-02-28 18:11:12.786	    7f67161f2740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-02-28 18:11:17.012	    7f67161f2740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2018-02-28 18:11:17.012	    7f67161f2740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2018-02-28 18:11:17.012	    7f67161f2740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2018-02-28 18:11:17.012	    7f67161f2740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2018-02-28 18:11:17.012	    7f67161f2740	INFO 	global	src/daemon/core.h:73	Initializing core...
2018-02-28 18:11:17.012	    7f67161f2740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/jim/.bitmonero/lmdb ...
2018-02-28 18:11:17.200	    7f67161f2740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:421	Loading checkpoints
2018-02-28 18:11:17.670	    7f67161f2740	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-02-28 18:11:17.670	    7f67161f2740	INFO 	global	src/daemon/core.h:78	Core initialized OK
2018-02-28 18:11:17.670	    7f67161f2740	INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2018-02-28 18:11:17.671	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2018-02-28 18:11:17.671	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-02-28 18:11:18.673	[P2P1]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1258	
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2018-02-28 18:11:18.673	[P2P1]	WARN 	global	src/cryptonote_core/cryptonote_core.cpp:1282	**********************************************************************
2018-02-28 18:11:18.673	[P2P1]	WARN 	global	src/cryptonote_core/cryptonote_core.cpp:1283	Last scheduled hard fork time shows a daemon update is needed now.
2018-02-28 18:11:18.674	[P2P1]	WARN 	global	src/cryptonote_core/cryptonote_core.cpp:1284	**********************************************************************
2018-02-28 18:11:19.075	[P2P1]	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-02-28 18:11:20.102	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[83.128.251.73:18080 OUT] Sync data returned a new top block candidate: 482278 -> 1519627 [Your node is 1037349 blocks (1074 days) behind] 
SYNCHRONIZATION started
2018-02-28 18:11:24.887	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:305	[176.9.1.92:18080 OUT] Sync data returned a new top block candidate: 482278 -> 1519628 [Your node is 1037350 blocks (1074 days) behind] 
SYNCHRONIZATION started
2018-02-28 18:11:33.172	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1154	[89.38.97.122:18080 OUT]  Synced 482378/1519628`

# Discussion History
## moneromooo-monero | 2018-03-01T11:21:19+00:00
I/O error sounds like a hardware error. However, IIRC we did fix a bug that would cause that error to be thrown by the LMDB layer. Are you using master, or 0.11.1.0 ?

## jodobear | 2018-03-01T14:37:51+00:00
Hey moneromooo!

I am using Helium Hydra v0.11.1.0.

I ran diagnostics after getting the I/O error on my partition and it's clean, in fact it only contains the Mint VBox nothing else. The laptop is new and everything is clean AFASIK. The Mint VBox is also clean and only used for bitcoin and monero nodes. The bitcoin node has synced and now syncing monero node which is giving me this issue.

## moneromooo-monero | 2018-03-01T14:43:45+00:00
OK, try master then. It might stop syncing, but will resume upon restart (fixed in git, but not yet merged).

## jodobear | 2018-03-02T12:11:47+00:00
Well, since this morning i'm getting `Bus Error`! Below is the log:

tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $ ./monerod
2018-03-02 10:02:59.515	    7fd09a63d740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-03-02 10:02:59.515	    7fd09a63d740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2018-03-02 10:02:59.515	    7fd09a63d740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2018-03-02 10:02:59.518	    7fd09a63d740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-03-02 10:03:03.908	    7fd09a63d740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2018-03-02 10:03:03.909	    7fd09a63d740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2018-03-02 10:03:03.909	    7fd09a63d740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2018-03-02 10:03:03.909	    7fd09a63d740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2018-03-02 10:03:03.909	    7fd09a63d740	INFO 	global	src/daemon/core.h:73	Initializing core...
2018-03-02 10:03:03.910	    7fd09a63d740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/jim/.bitmonero/lmdb ...
Bus error (core dumped)
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $ ./monerod
2018-03-02 11:20:13.023	    7f58f62a8740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-03-02 11:20:13.023	    7f58f62a8740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2018-03-02 11:20:13.023	    7f58f62a8740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2018-03-02 11:20:13.023	    7f58f62a8740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-03-02 11:20:17.243	    7f58f62a8740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2018-03-02 11:20:17.243	    7f58f62a8740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2018-03-02 11:20:17.243	    7f58f62a8740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2018-03-02 11:20:17.243	    7f58f62a8740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2018-03-02 11:20:17.243	    7f58f62a8740	INFO 	global	src/daemon/core.h:73	Initializing core...
2018-03-02 11:20:17.243	    7f58f62a8740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/jim/.bitmonero/lmdb ...
Bus error (core dumped)
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $
tin@tin-mint-vb ~/monero/monero-gui-v0.11.1.0 $ ./monerod --db-salvage
2018-03-02 11:20:28.287	    7f314ec0c740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-03-02 11:20:28.287	    7f314ec0c740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2018-03-02 11:20:28.287	    7f314ec0c740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2018-03-02 11:20:28.287	    7f314ec0c740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-03-02 11:20:32.445	    7f314ec0c740	INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2018-03-02 11:20:32.446	    7f314ec0c740	INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2018-03-02 11:20:32.446	    7f314ec0c740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2018-03-02 11:20:32.446	    7f314ec0c740	INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2018-03-02 11:20:32.446	    7f314ec0c740	INFO 	global	src/daemon/core.h:73	Initializing core...
2018-03-02 11:20:32.446	    7f314ec0c740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:323	Loading blockchain from folder /home/jim/.bitmonero/lmdb ...
2018-03-02 11:20:32.447	    7f314ec0c740	WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:1155	LMDB memory map needs to be resized, doing that now.
2018-03-02 11:20:32.450	    7f314ec0c740	INFO 	global	src/blockchain_db/lmdb/db_lmdb.cpp:494	LMDB Mapsize increased.  Old: 7168MiB, New: 8192MiB
Bus error (core dumped)

## jodobear | 2018-03-02T12:44:18+00:00
i'm not sure how to install master? should i delete the current installation and install monero using snap?

## moneromooo-monero | 2018-08-15T11:38:30+00:00
A bit late, but better to use 0.12.3.0 (or, in a few days, 0.12.4.0 when it's out), as this has fixes for DB corruption after sync's done.

# Action History
- Created by: jodobear | 2018-02-28T23:31:03+00:00
- Closed at: 2022-03-16T15:31:22+00:00
