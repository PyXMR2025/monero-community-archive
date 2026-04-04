---
title: Error attempting to sync testnet in v0.13.0.2
source_url: https://github.com/monero-project/monero/issues/4554
author: oliverw
assignees: []
labels: []
created_at: '2018-10-10T19:12:59+00:00'
updated_at: '2018-10-16T10:37:46+00:00'
type: issue
status: closed
closed_at: '2018-10-10T20:56:08+00:00'
---

# Original Description
I've just built v0.13.0.2 from source in Ubuntu 16.04 (WSL). Upon starting monerod with an empty data directory the following happens:

> oliver@DESKTOP-2GKAJGE: $ rm -rf .bitmonero/
> oliver@DESKTOP-2GKAJGE: $ monero/build/Linux/_HEAD_detached_at_v0.13.0.2_/release/bin/monerod --testnet
> 2018-10-10 19:04:23,918 INFO  [default] Page size: 4096
> 2018-10-10 19:04:24.923     7fcd21ae0780        INFO    global  src/daemon/main.cpp:287 Monero 'Beryllium Bullet' (v0.13.0.2-release)
> 2018-10-10 19:04:24.923     7fcd21ae0780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
> 2018-10-10 19:04:24.927     7fcd21ae0780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
> 2018-10-10 19:04:24.927     7fcd21ae0780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
> 2018-10-10 19:04:27.597     7fcd21ae0780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
> 2018-10-10 19:04:27.597     7fcd21ae0780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
> 2018-10-10 19:04:27.597     7fcd21ae0780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76       Binding on 127.0.0.1:28081
> 2018-10-10 19:04:27.597     7fcd21ae0780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 28081
> 2018-10-10 19:04:27.597     7fcd21ae0780        INFO    global  src/daemon/core.h:86    Initializing core...
> 2018-10-10 19:04:27.598     7fcd21ae0780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:447       Loading blockchain from folder /home/oliver/.bitmonero/testnet/lmdb ...
> 2018-10-10 19:04:27.601     7fcd21ae0780        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:75     Error attempting to retrieve a hard fork version at height 0 from the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
> 2018-10-10 19:04:27.605     7fcd21ae0780        FATAL   daemon  src/daemon/daemon.cpp:195       Uncaught exception! Error adding hard fork version to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
> 2018-10-10 19:04:27.605     7fcd21ae0780        INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
> 2018-10-10 19:04:27.605     7fcd21ae0780        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
> 2018-10-10 19:04:28.685     7fcd21ae0780        INFO    global  src/daemon/core.h:103   Deinitializing core...
> 2018-10-10 19:04:28.688     7fcd21ae0780        INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
> 2018-10-10 19:04:28.688     7fcd21ae0780        INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully

# Discussion History
## moneromooo-monero | 2018-10-10T19:29:06+00:00
32 bit machine ?

## oliverw | 2018-10-10T19:39:32+00:00
It's Ubuntu in Windows Subsystem for Linux (WSL): 

> $ uname -a
> Linux DESKTOP-2GKAJGE 4.4.0-17134-Microsoft #285-Microsoft Thu Aug 30 17:31:00 PST 2018 x86_64 x86_64 x86_64 GNU/Linux

I never had compatibility problems with it but you never know.

## moneromooo-monero | 2018-10-10T20:29:46+00:00
o_O

Does this filesystem support (non buggy) mmap ?

## iDunk5400 | 2018-10-10T20:45:09+00:00
https://github.com/Microsoft/WSL/issues/658


## oliverw | 2018-10-10T20:56:08+00:00
@iDunk5400 @moneromooo-monero  Allright that explains it. Closing.

## hyc | 2018-10-10T22:37:58+00:00
@iDunk5400 LMDB doesn't attempt to mmap zero length files (we already ran into that bug years ago and worked around it). This is more likely a more recent bug https://github.com/nimiq-network/core/issues/387#issuecomment-401835135

I worked with the NIMIQ guys to diagnose the problem.
https://twitter.com/hyc_symas/status/1013800256088215552

## DinoStray | 2018-10-16T08:22:49+00:00
I got error like you,
First , I delete all data from testnet folder.
Then, start monerod with --testnet.

2018-10-16T10:36:06.878033334Z 2018-10-16 10:36:06.877      7fea613f4780        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:917   Set server type to: 2 from name: P2P, prefix_name = P2P
2018-10-16T10:36:10.902571431Z 2018-10-16 10:36:10.902      7fea613f4780        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:549  Percent used: 0.0104  Percent threshold: 0.9000
2018-10-16T10:36:10.903754650Z 2018-10-16 10:36:10.903      7fea613f4780        INFO    global  src/daemon/core.h:92    Core initialized OK
2018-10-16T10:36:10.903758513Z 2018-10-16 10:36:10.903      7fea613f4780        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2018-10-16T10:36:10.903763095Z 2018-10-16 10:36:10.903      7fea613f4780        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:89     Run net_service loop( 2 threads)...
2018-10-16T10:36:10.903901838Z 2018-10-16 10:36:10.903  [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2018-10-16T10:36:10.904956407Z 2018-10-16 10:36:10.904  [SRV_MAIN]      INFO    daemon  src/daemon/daemon.cpp:174       Starting ZMQ server...
2018-10-16T10:36:10.904997884Z 2018-10-16 10:36:10.904  [SRV_MAIN]      INFO    daemon  src/daemon/daemon.cpp:178       ZMQ server started at 127.0.0.1:28082.
2018-10-16T10:36:10.905014085Z 2018-10-16 10:36:10.904  [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-10-16T10:36:10.905100783Z 2018-10-16 10:36:10.905  [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:636        Run net_service loop( 10 threads)...
2018-10-16T10:36:10.905107312Z 2018-10-16 10:36:10.905  [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:642        net_service loop stopped.
2018-10-16T10:36:10.905110189Z 2018-10-16 10:36:10.905  [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2018-10-16T10:36:11.907352507Z 2018-10-16 10:36:11.907  [SRV_MAIN]      INFO    global  src/daemon/rpc.h:84     Stopping core RPC server...
2018-10-16T10:36:11.907537743Z 2018-10-16 10:36:11.907  [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:190       Node stopped.
2018-10-16T10:36:11.907886310Z 2018-10-16 10:36:11.907  [SRV_MAIN]      INFO    global  src/daemon/rpc.h:96     Deinitializing core RPC server...
2018-10-16T10:36:11.908057229Z 2018-10-16 10:36:11.907  [SRV_MAIN]      INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2018-10-16T10:36:11.908069098Z 2018-10-16 10:36:11.907  [SRV_MAIN]      INFO    net     src/p2p/net_node.h:250  Killing the net_node
2018-10-16T10:36:11.908074304Z 2018-10-16 10:36:11.908  [SRV_MAIN]      INFO    net     src/p2p/net_node.h:254  Joined extra background net_node threads
2018-10-16T10:36:15.912567110Z 2018-10-16 10:36:15.912  [SRV_MAIN]      INFO    net.p2p src/p2p/net_node.inl:2113       No IGD was found.
2018-10-16T10:36:15.912698437Z 2018-10-16 10:36:15.912  [SRV_MAIN]      INFO    global  src/daemon/core.h:103   Deinitializing core...
2018-10-16T10:36:15.914132704Z 2018-10-16 10:36:15.914  [SRV_MAIN]      INFO    global  src/daemon/protocol.h:75        Stopping cryptonote protocol...
2018-10-16T10:36:15.914155442Z 2018-10-16 10:36:15.914  [SRV_MAIN]      INFO    global  src/daemon/protocol.h:79        Cryptonote protocol stopped successfully

# Action History
- Created by: oliverw | 2018-10-10T19:12:59+00:00
- Closed at: 2018-10-10T20:56:08+00:00
