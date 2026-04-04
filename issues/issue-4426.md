---
title: 'Daemon issue with monero 0.12.3 '
source_url: https://github.com/monero-project/monero/issues/4426
author: php-wizard
assignees: []
labels: []
created_at: '2018-09-24T00:21:09+00:00'
updated_at: '2018-09-24T15:17:01+00:00'
type: issue
status: closed
closed_at: '2018-09-24T15:17:01+00:00'
---

# Original Description
When i run the latest monero gui 0.12.3 , it gets stuck at waiting for the daemon to start, and the daemon prints this at some point:

global  src/cryptonote_core/blockchain.cpp:460  Current top block <00e78ec7c92806fbb9b08e83efd7201383efb9947ce1f735e7f013f54b810b03> at height 1637510 has version 6 which disagrees with the ideal version 7

Is that normal?

This is the full output from the daemon

----

2018-09-24 00:16:26.025 17232   INFO    global  src/daemon/main.cpp:282 Monero 'Lithium Luna' (v0.12.3.0-release)
2018-09-24 00:16:26.026 17232   INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2018-09-24 00:16:26.026 17232   INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2018-09-24 00:16:26.027 17232   INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2018-09-24 00:16:27.293 17232   INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2018-09-24 00:16:28.439 17232   INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2018-09-24 00:16:28.439 17232   INFO    global  contrib/epee/include/net/http_server_impl_base.h:76  Binding on 127.0.0.1:18081
2018-09-24 00:16:28.439 17232   INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2018-09-24 00:16:28.439 17232   INFO    global  src/daemon/core.h:86    Initializing core...
2018-09-24 00:16:28.439 17232   INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-09-24 00:16:29.806 17232   INFO    global  src/cryptonote_core/blockchain.cpp:460  Current top block <e594cf2fbe48b13b75583d4c9c69bac55aa12c4bd255dbc33a767b5cb6366117> at height 1633181 has version 6 which disagrees with the ideal version 7
2018-09-24 00:16:29.806 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1633181
2018-09-24 00:16:31.107 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1633081
2018-09-24 00:16:31.978 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632981
2018-09-24 00:16:32.729 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632881
2018-09-24 00:16:33.612 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632781
2018-09-24 00:16:34.474 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632681
2018-09-24 00:16:36.563 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632581
2018-09-24 00:16:38.292 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632481
2018-09-24 00:16:46.080 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632381
2018-09-24 00:16:47.697 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632281
2018-09-24 00:16:49.531 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632181
2018-09-24 00:16:51.643 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1632081
2018-09-24 00:16:53.444 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631981
2018-09-24 00:16:55.302 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631881
2018-09-24 00:16:57.095 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631781
2018-09-24 00:17:00.399 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631681
2018-09-24 00:17:06.765 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631581
2018-09-24 00:17:08.479 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631481
2018-09-24 00:17:09.946 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631381
2018-09-24 00:17:11.546 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631281
2018-09-24 00:17:13.147 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631181
2018-09-24 00:17:15.718 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1631081
2018-09-24 00:17:22.181 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630981
2018-09-24 00:17:23.636 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630881
2018-09-24 00:17:25.307 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630781
2018-09-24 00:17:27.004 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630681
2018-09-24 00:17:28.582 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630581
2018-09-24 00:17:30.149 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630481
2018-09-24 00:17:32.070 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630381
2018-09-24 00:17:34.297 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630281
2018-09-24 00:17:40.206 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630181
2018-09-24 00:17:41.925 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1630081
2018-09-24 00:17:43.566 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1629981
2018-09-24 00:17:45.952 17232   INFO    global  src/cryptonote_core/blockchain.cpp:462  Popping blocks... 1629881
-----

...and it keeps printing Popping blocks while the GUI says "Daemon failed to start"


# Discussion History
## plavirudar | 2018-09-24T01:07:50+00:00
You didn't update your client at 1539500 to Lithium Luna and were syncing the "Monero Classic" blockchain. Thanks to upgrades in the daemon, you should just leave the daemon running and it will automatically delete that fork (which is what "popping blocks" is doing) and sync you onto the right chain. 

Any transactions you made from April to now will likely be lost, due to them being broadcast on the wrong chain. 

## dEBRUYNE-1 | 2018-09-24T15:14:42+00:00
+resolved

# Action History
- Created by: php-wizard | 2018-09-24T00:21:09+00:00
- Closed at: 2018-09-24T15:17:01+00:00
