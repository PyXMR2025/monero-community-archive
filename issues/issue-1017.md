---
title: Error message on first connection to a peer during initial sync (testnet)
source_url: https://github.com/monero-project/monero/issues/1017
author: iDunk5400
assignees: []
labels: []
created_at: '2016-08-30T12:58:32+00:00'
updated_at: '2016-10-04T22:32:49+00:00'
type: issue
status: closed
closed_at: '2016-10-04T22:32:49+00:00'
---

# Original Description
Starting bitmonerod.exe (c3ba844) on testnet for the first time, on Windows 10 Pro x64, produced the following error message each time it connected to a new peer:
`ERROR C:/msys64/home/re/bitmonero/src/cryptonote_core/blockchain.cpp:1832 Ours and foreign blockchain have only genesis block in common... o.O`
The blockchain continued synchronizing normally.

Relevant parts of bitmonero.log:

```
2016-Aug-30 11:43:36.533384 Initializing cryptonote protocol...
2016-Aug-30 11:43:36.533384 Cryptonote protocol initialized OK
2016-Aug-30 11:43:36.535884 Initializing p2p server...
2016-Aug-30 11:43:36.538384 Set limit-up to 256 kB/s
2016-Aug-30 11:43:36.538384 Set limit-down to 8192 kB/s
2016-Aug-30 11:43:36.538885 Set limit-down to 8192 kB/s
2016-Aug-30 11:43:36.538885 Binding on 0.0.0.0:28080
2016-Aug-30 11:43:36.539384 Net service bound to 0.0.0.0:28080
2016-Aug-30 11:43:36.539384 P2p server initialized OK
2016-Aug-30 11:43:36.539884 Initializing core rpc server...
2016-Aug-30 11:43:36.539884 Binding on 127.0.0.1:28081
2016-Aug-30 11:43:36.540385 Core rpc server initialized OK on port: 28081
2016-Aug-30 11:43:36.540385 Initializing core...
2016-Aug-30 11:43:36.541385 Loading blockchain from folder C:\ProgramData\bitmonero\testnet\lmdb ...
2016-Aug-30 11:43:36.541385 option: fast
2016-Aug-30 11:43:36.541385 option: async
2016-Aug-30 11:43:36.541385 option: 1000
2016-Aug-30 11:43:36.559887 Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2016-Aug-30 11:43:36.560387 The DB has no hard fork info, reparsing from start
2016-Aug-30 11:43:36.560387 Blockchain not loaded, generating genesis block.
2016-Aug-30 11:43:36.675902 Blockchain initialized. last block: 0, d1518.h4.m43.s36 time ago, current difficulty: 1
2016-Aug-30 11:43:36.676402 Core initialized OK
2016-Aug-30 11:43:36.676402 Starting core rpc server...
2016-Aug-30 11:43:36.676402 Run net_service loop( 2 threads)...
2016-Aug-30 11:43:36.677402 [SRV_MAIN]Core rpc server started ok
2016-Aug-30 11:43:36.678402 [SRV_MAIN]Starting p2p net loop...
2016-Aug-30 11:43:36.678902 [SRV_MAIN]Run net_service loop( 10 threads)...
2016-Aug-30 11:43:37.679528 [P2P7]
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level>" command*, where <level> is between 0 (no details) and 4 (very verbose).

Use "help" command to see the list of available commands.

Note: in case you need to interrupt the process, use "exit" command. Otherwise, the current progress won't be saved.
**********************************************************************
2016-Aug-30 11:44:05.947100 [P2P9][62.210.104.109:28080 OUT]Sync data returned unknown top block: 1 -> 801782 [801781 blocks (556 days) behind] 
SYNCHRONIZATION started
2016-Aug-30 11:44:05.984605 [P2P9]ERROR C:/msys64/home/re/bitmonero/src/cryptonote_core/blockchain.cpp:1832 Ours and foreign blockchain have only genesis block in common... o.O
2016-Aug-30 11:44:09.738075 [P2P7][62.210.104.109:28080 OUT]Synced 201/801782
2016-Aug-30 11:44:13.011486 [P2P6][62.210.104.109:28080 OUT]Synced 401/801782
2016-Aug-30 11:44:16.281896 [P2P7][62.210.104.109:28080 OUT]Synced 601/801782
2016-Aug-30 11:44:19.405789 [P2P9][107.152.130.98:28080 OUT]Sync data returned unknown top block: 601 -> 801782 [801181 blocks (556 days) behind] 
SYNCHRONIZATION started
2016-Aug-30 11:44:19.407789 [P2P9]ERROR C:/msys64/home/re/bitmonero/src/cryptonote_core/blockchain.cpp:1832 Ours and foreign blockchain have only genesis block in common... o.O
2016-Aug-30 11:44:19.510801 [P2P7][62.210.104.109:28080 OUT]Synced 801/801782
2016-Aug-30 11:44:22.791222 [P2P9][62.210.104.109:28080 OUT]Synced 1001/801782
2016-Aug-30 11:44:26.003126 [P2P9][62.210.104.109:28080 OUT]Synced 1201/801782
2016-Aug-30 11:44:29.369548 [P2P5][62.210.104.109:28080 OUT]Synced 1401/801782
2016-Aug-30 11:44:32.662461 [P2P9][62.210.104.109:28080 OUT]Synced 1601/801782
2016-Aug-30 11:44:36.025883 [P2P9][62.210.104.109:28080 OUT]Synced 1801/801782
2016-Aug-30 11:44:41.281042 [P2P9][62.210.104.109:28080 OUT]Synced 2001/801782
2016-Aug-30 11:44:44.812986 [P2P9][62.210.104.109:28080 OUT]Synced 2201/801782
2016-Aug-30 11:44:48.152905 [P2P5][62.210.104.109:28080 OUT]Synced 2401/801782
2016-Aug-30 11:44:51.528828 [P2P9][62.210.104.109:28080 OUT]Synced 2601/801782
2016-Aug-30 11:44:54.920254 [P2P9][62.210.104.109:28080 OUT]Synced 2801/801782
2016-Aug-30 11:44:58.118655 [P2P6][107.13.138.161:28080 OUT]Sync data returned unknown top block: 2801 -> 801783 [798982 blocks (554 days) behind] 
SYNCHRONIZATION started
2016-Aug-30 11:44:58.120656 [P2P6]ERROR C:/msys64/home/re/bitmonero/src/cryptonote_core/blockchain.cpp:1832 Ours and foreign blockchain have only genesis block in common... o.O
2016-Aug-30 11:44:58.235169 [P2P9][62.210.104.109:28080 OUT]Synced 3001/801783
2016-Aug-30 11:45:01.648098 [P2P9][62.210.104.109:28080 OUT]Synced 3201/801783
2016-Aug-30 11:45:05.051525 [P2P9][62.210.104.109:28080 OUT]Synced 3401/801783

...............

2016-Aug-30 12:44:58.949895 [P2P8][62.210.104.109:28080 OUT]Synced 202181/801823
2016-Aug-30 12:45:02.798379 [P2P8][62.210.104.109:28080 OUT]Synced 202381/801823
2016-Aug-30 12:45:06.742874 [P2P8][62.210.104.109:28080 OUT]Synced 202581/801823
2016-Aug-30 12:45:17.941779 [P2P3][62.210.104.109:28080 OUT]Sync data returned unknown top block: 202612 -> 801823 [599211 blocks (416 days) behind] 
SYNCHRONIZATION started
2016-Aug-30 12:45:17.976783 [P2P3]ERROR C:/msys64/home/re/bitmonero/src/cryptonote_core/blockchain.cpp:1832 Ours and foreign blockchain have only genesis block in common... o.O
2016-Aug-30 12:45:24.176561 [P2P8][62.210.104.109:28080 OUT]Synced 202812/801823
2016-Aug-30 12:45:24.176561 [P2P3][107.152.130.98:28080 OUT]Synced 202812/801823
2016-Aug-30 12:45:27.671999 [P2P8][107.152.130.98:28080 OUT]Synced 203012/801823

...............

2016-Aug-30 12:57:27.284463 [P2P7][62.210.104.109:28080 OUT]Synced 241409/801831
2016-Aug-30 12:57:30.886415 [P2P2][62.210.104.109:28080 OUT]Synced 241609/801831
2016-Aug-30 12:57:34.342849 [P2P8][107.13.138.161:28080 OUT]Sync data returned unknown top block: 241609 -> 801831 [560222 blocks (389 days) behind] 
SYNCHRONIZATION started
2016-Aug-30 12:57:34.369352 [P2P8]ERROR C:/msys64/home/re/bitmonero/src/cryptonote_core/blockchain.cpp:1832 Ours and foreign blockchain have only genesis block in common... o.O
2016-Aug-30 12:57:34.511369 [P2P2][62.210.104.109:28080 OUT]Synced 241809/801831
2016-Aug-30 12:57:38.138325 [P2P8][62.210.104.109:28080 OUT]Synced 242009/801831
2016-Aug-30 12:57:41.936801 [P2P7][62.210.104.109:28080 OUT]Synced 242209/801831
2016-Aug-30 12:57:45.704774 [P2P7][62.210.104.109:28080 OUT]Synced 242409/801831
2016-Aug-30 12:57:49.099700 [P2P7][62.210.104.109:28080 OUT]Synced 242608/801831
2016-Aug-30 12:57:55.256473 [P2P8][107.13.138.161:28080 OUT]Synced 242808/801831
2016-Aug-30 12:57:55.256473 [P2P7][62.210.104.109:28080 OUT]Synced 242808/801831
2016-Aug-30 12:57:58.621895 [P2P8][62.210.104.109:28080 OUT]Synced 243008/801831
2016-Aug-30 12:57:58.621895 [P2P7][107.13.138.161:28080 OUT]Synced 243008/801831
2016-Aug-30 12:58:02.234435 [P2P7][62.210.104.109:28080 OUT]Synced 243208/801831
2016-Aug-30 12:58:02.234935 [P2P8][107.13.138.161:28080 OUT]Synced 243208/801831
2016-Aug-30 12:58:05.963909 [P2P7][62.210.104.109:28080 OUT]Synced 243408/801831
2016-Aug-30 12:58:05.963909 [P2P8][107.13.138.161:28080 OUT]Synced 243408/801831
2016-Aug-30 12:58:09.512354 [P2P2][107.13.138.161:28080 OUT]Synced 243608/801831
2016-Aug-30 12:58:09.512354 [P2P6][62.210.104.109:28080 OUT]Synced 243608/801831
2016-Aug-30 12:58:13.269332 [P2P7][107.13.138.161:28080 OUT]Synced 243808/801832
2016-Aug-30 12:58:13.269332 [P2P6][62.210.104.109:28080 OUT]Synced 243808/801832
2016-Aug-30 12:58:16.820811 [P2P9][51.175.75.137:28080 OUT]Sync data returned unknown top block: 243815 -> 801832 [558018 blocks (387 days) behind] 
SYNCHRONIZATION started
2016-Aug-30 12:58:16.874818 [P2P9]ERROR C:/msys64/home/re/bitmonero/src/cryptonote_core/blockchain.cpp:1832 Ours and foreign blockchain have only genesis block in common... o.O
2016-Aug-30 12:58:16.977330 [P2P7][107.13.138.161:28080 OUT]Synced 244008/801832
2016-Aug-30 12:58:16.977330 [P2P6][62.210.104.109:28080 OUT]Synced 244008/801832
```


# Discussion History
## moneromooo-monero | 2016-08-30T15:12:14+00:00
I get this also on Linux.
This is a third node that is trying to sync with yours. It's sending a set of block hashes that it has. Your node has pretty much nothing yet, so the only thing that's in common is the genesis block. This is normal, and I'm not sure why this would not have been seen before.


## skaht | 2016-09-24T04:17:35+00:00
After compiling, I also get this same error on a Mac after performing a blockchain export under v.0.9.4 and importing under v.0.10.0 and firing up ./monerod for some of the very early blocks.


## iDunk5400 | 2016-10-04T22:32:49+00:00
Ok, normal behaviour.


# Action History
- Created by: iDunk5400 | 2016-08-30T12:58:32+00:00
- Closed at: 2016-10-04T22:32:49+00:00
