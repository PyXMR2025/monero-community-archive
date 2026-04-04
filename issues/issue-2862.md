---
title: 'Blockchain error src/cryptonote_core/blockchain.cpp:3412 Error adding block
  with hash: <4bf55b58c16e7efedd11f61c9bfbed3d7eac65a782fa56e1737f31d4c4c54311> to
  blockchain, what = Attempting to add transaction that''s already in the db (tx id
  804609)'
source_url: https://github.com/monero-project/monero/issues/2862
author: herrlogi
assignees: []
labels: []
created_at: '2017-11-26T01:42:50+00:00'
updated_at: '2017-11-26T20:33:54+00:00'
type: issue
status: closed
closed_at: '2017-11-26T20:33:49+00:00'
---

# Original Description
I think after a crash something got corrupted ive tried downloading the blockchain https://downloads.getmonero.org/blockchain.raw
But I just cant get my deamon to be uptodate and work in any way. 
Im sorry but I need help, mining I can do pretty well but this whole deamon stuff is above me :(

PROBLEM SOLVED by finding out the refered blockchain file and deleting for a full rescan.


2017-11-26 01:39:34.106 11084   INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.1.0-release)
2017-11-26 01:39:34.106 11084   INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-11-26 01:39:34.106 11084   INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-11-26 01:39:34.107 11084   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-11-26 01:39:35.338 11084   INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-11-26 01:39:35.338 11084   INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-11-26 01:39:35.339 11084   INFO    global  contrib/epee/include/net/http_server_impl_base.h:70  Binding on 127.0.0.1:18081
2017-11-26 01:39:35.339 11084   INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-11-26 01:39:35.339 11084   INFO    global  src/daemon/core.h:73    Initializing core...
2017-11-26 01:39:35.340 11084   INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-11-26 01:39:35.527 11084   INFO    global  src/cryptonote_core/cryptonote_core.cpp:421     Loading checkpoints
2017-11-26 01:39:35.608 11084   WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-26 01:39:35.608 11084   INFO    global  src/daemon/core.h:78    Core initialized OK
2017-11-26 01:39:35.609 11084   INFO    global  src/daemon/rpc.h:68     Starting core rpc server...
2017-11-26 01:39:35.609 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok
2017-11-26 01:39:35.609 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2017-11-26 01:39:36.611 [P2P7]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1258    [1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************
[0m
2017-11-26 01:39:36.681 [P2P7]  WARN    net.dns src/common/dns_utils.cpp:487    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-11-26 01:39:37.417 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [206.72.193.82:18080 OUT] Sync data returned a new top block candidate: 453570 -> 1451073 [Your node is 997503 blocks (998 days) behind]
SYNCHRONIZATION started
2017-11-26 01:39:38.552 [P2P5]  INFO    global  src/cryptonote_core/blockchain.cpp:1427 [1;34m----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 453569
id:     <1ca62a20a842b387fc8d8507957dcc18f080e0e71dd9b61c99fa5e53b4559da8>
PoW:    <5efd1cf0b78602925fa0dd6aeb9d7996ac059a416a24ee95ec94595d00000000>
difficulty:     907127735[0m
2017-11-26 01:39:38.554 [P2P5]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3412 Error adding block with hash: <4bf55b58c16e7efedd11f61c9bfbed3d7eac65a782fa56e1737f31d4c4c54311> to blockchain, what = Attempting to add transaction that's already in the db (tx id 804609)
2017-11-26 01:39:39.567 [P2P9]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3412 Error adding block with hash: <4bf55b58c16e7efedd11f61c9bfbed3d7eac65a782fa56e1737f31d4c4c54311> to blockchain, what = Attempting to add transaction that's already in the db (tx id 804609)
2017-11-26 01:39:39.954 [P2P5]  ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3412 Error adding block with hash: <4bf55b58c16e7efedd11f61c9bfbed3d7eac65a782fa56e1737f31d4c4c54311> to blockchain, what = Attempting to add transaction that's already in the db (tx id 804609)


# Discussion History
## moneromooo-monero | 2017-11-26T08:37:23+00:00
Please post the output of:

mdb_stat -a ~/.bitmonero/lmdb


## herrlogi | 2017-11-26T09:05:38+00:00
thank you moneromooo-monero.
how can I get this output? I tried give"mdb_stat -a ~/.bitmonero/lmdb" as command inside monerod but that doesnt seem to work.
and i made a shortcut with adding K:\Miner\monero-gui-win-x64-v0.11.1.0\monero-gui-v0.11.1.0\monerod.exe mdb_stat -a ~/.bitmonero/lmdb
then it just launches shortly and closes itself

## moneromooo-monero | 2017-11-26T09:51:25+00:00
It's not a monerod command, it's a separate program. If you're on Windows, you  might have to compile it separately, unless you have a mdb-tools or similar package.
And if you're using the GUI, you probably didn't build it yourself, so that makes things a bit more complicated...
I'll ask around what's the best way for Windows.

## herrlogi | 2017-11-26T10:22:20+00:00
Ive tried gui but also the command line program. 
Compiling i have never done before though.

I just ran a  search for all bitmonero things and deleted c:\programdata\bitmonero
It seems to have started a fresh blockchain download.  

it seems to be running alright now will update soon


## moneromooo-monero | 2017-11-26T13:26:24+00:00
For reference, a Windows mdb_stat binary is here: https://mega.nz/#!iFFHHKIZ!FuAmblXe5hxGGqh6hp0heL1ohK3NqP5-LBaCN7Kl6xU

It was built by someone trustworthy, but always exercise caution when running stuff from the internet.

# Action History
- Created by: herrlogi | 2017-11-26T01:42:50+00:00
- Closed at: 2017-11-26T20:33:49+00:00
