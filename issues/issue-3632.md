---
title: Crash of moned fixing pruned blockchain
source_url: https://github.com/monero-project/monero-gui/issues/3632
author: Liger0
assignees: []
labels: []
created_at: '2021-07-21T00:00:45+00:00'
updated_at: '2022-04-26T18:32:45+00:00'
type: issue
status: closed
closed_at: '2022-04-26T18:32:45+00:00'
---

# Original Description
Hi, at some point the download of my pruned blockchain got corrupted because the pc got restarted while synching.
I used the command  --prune-blockchain --db-salvage in the gui as flag and also tried to salvage by command prompt, but while starting the node monerod.exe reports a crash.

# Discussion History
## selsta | 2021-07-21T01:29:04+00:00
You most likely have to resync from scratch.

## Liger0 | 2021-07-21T12:50:07+00:00
It's the fourth time I try to resynch from 0, everytime it reaches 60% it freezes, the gui keeps saying "resynching", and the blockchain isn't updated anymore. I click "stop daemon" but it never does so. Even closing the wallet doesn't work at that point and I am forced to kill the process.

## Liger0 | 2021-07-24T21:59:55+00:00
I tried to resync yet again. After 3 days it was near its end with some hours remaining, the file was over 30GB.
I had to restart the PC, so I stopped the daemon by the gui correctly and closed the program. I noticed my system was still sluggish, after 10 minutes my hard disk still reported 100% of my hdd writing bandwidth was used, even though the gui was totally closed.

I restarted the PC, and the blockchain is corrupted again. It's ridiculous...

## selsta | 2021-07-24T22:47:04+00:00
There is something wrong with your system, hard drive, setup, or there is a bug. A corruption is rare, having it corrupt 5 times is not normal.

In general an SSD is recommended, but it also works on HDD.

Note that you can add `--db-sync-mode safe` it will avoid the blockchain from corrupting but it will result in slower sync. Alternatively you can simply use a remote node.

## Liger0 | 2021-07-25T00:03:29+00:00
It seems it keeps writing on the hdd after closing the daemon and the gui, I also found other claims that the blockchain gets corrupted when interrupting if it's synched with the pruning option.
The log's this:

`2021-07-24 21:05:47.766	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1680	Synced 2343532/2412008 (97%, 68476 left, 40% of total synced, estimated 22.1 hours left)

2021-07-24 21:06:13.720	[P2P6]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1680	Synced 2343552/2412008 (97%, 68456 left)

2021-07-24 21:06:20.278	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:80	p2p net loop stopped

2021-07-24 21:06:20.458	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:84	Stopping core RPC server...

2021-07-24 21:06:20.474	[SRV_MAIN]	INFO	global	src/daemon/daemon.cpp:227	Node stopped.

2021-07-24 21:06:20.487	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:96	Deinitializing core RPC server...

2021-07-24 21:06:20.515	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:90	Deinitializing p2p...

2021-07-24 21:06:32.904	[SRV_MAIN]	INFO	global	src/daemon/core.h:94	Deinitializing core...

2021-07-24 21:50:49.629	11804	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO

2021-07-24 21:50:49.658	11804	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.0-release)

2021-07-24 21:50:49.660	11804	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...

2021-07-24 21:50:49.661	11804	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK

2021-07-24 21:50:49.662	11804	INFO	global	src/daemon/core.h:63	Initializing core...

2021-07-24 21:50:49.708	11804	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder E:\Monero storage\bitmonero (pruned blockchain)\lmdb ...

2021-07-24 21:51:25.764	11804	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:1345	Failed to parse block from blob

2021-07-24 21:51:25.900	11804	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...

2021-07-24 21:51:25.918	11804	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully

2021-07-24 21:51:25.919	11804	ERROR	daemon	src/daemon/main.cpp:362	Exception in main! Failed to parse block from blob retrieved from the db

2021-07-24 21:57:19.452	10992	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO

2021-07-24 21:57:19.453	10992	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.2.0-release)

2021-07-24 21:57:19.454	10992	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...

2021-07-24 21:57:19.455	10992	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK

2021-07-24 21:57:19.457	10992	INFO	global	src/daemon/core.h:63	Initializing core...

2021-07-24 21:57:19.458	10992	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder E:\Monero storage\bitmonero (pruned blockchain)\lmdb ...

2021-07-24 21:57:19.513	10992	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:1345	Failed to parse block from blob

2021-07-24 21:57:19.932	10992	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...

2021-07-24 21:57:19.932	10992	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully

2021-07-24 21:57:19.933	10992	ERROR	daemon	src/daemon/main.cpp:362	Exception in main! Failed to parse block from blob retrieved from the db
`

## Liger0 | 2021-07-28T10:25:32+00:00
> 
> 
> There is something wrong with your system, hard drive, setup, or there is a bug. A corruption is rare, having it corrupt 5 times is not normal.
> 
> In general an SSD is recommended, but it also works on HDD.
> 
> Note that you can add `--db-sync-mode safe` it will avoid the blockchain from corrupting but it will result in slower sync. Alternatively you can simply use a remote node.

I downloaded the entire raw blockchain from getmonero.
When it ended the import, it gave the following error

![block failed](https://user-images.githubusercontent.com/20385116/127307262-a398dda7-2b5f-4c53-bf5a-1a7df1e9ac84.png)

I again tried to repair it, but monerod crashes.


## selsta | 2022-04-26T18:32:45+00:00
I'm closing this here as it seems to be a daemon bug and not a GUI bug. I would recommend to either try a different computer / hard drive or use a remote node.

# Action History
- Created by: Liger0 | 2021-07-21T00:00:45+00:00
- Closed at: 2022-04-26T18:32:45+00:00
