---
title: monerod crash on startup
source_url: https://github.com/seraphis-migration/monero/issues/386
author: bvcxza
assignees: []
labels: []
created_at: '2026-05-14T10:37:04+00:00'
updated_at: '2026-05-15T11:16:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Last blockchain update was using alpha version. Trying to update blockchain now using fcmp++-beta-stressnet (d1adfbba21cdde7cec4b732ae4682ac44ee79167):

```
2026-05-14 10:21:58.820     7fe7ddaaaac0  INFO  logging contrib/epee/src/mlog.cpp:274 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2026-05-14 10:21:58.820     7fe7ddaaaac0  INFO  logging contrib/epee/src/mlog.cpp:274 New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2026-05-14 10:21:58.820     7fe7ddaaaac0  INFO  global  src/daemon/main.cpp:298 Monero 'Fluorine Fermi' (v0.19.0.0-beta.1.1-d1adfbba2)
2026-05-14 10:21:58.820     7fe7ddaaaac0  INFO  global  src/daemon/protocol.h:57  Initializing cryptonote protocol...
2026-05-14 10:21:58.820     7fe7ddaaaac0  INFO  global  src/daemon/protocol.h:62  Cryptonote protocol initialized OK
2026-05-14 10:21:58.820     7fe7ddaaaac0  INFO  global  src/daemon/core.h:64  Initializing core...
2026-05-14 10:21:58.821     7fe7ddaaaac0  INFO  global  src/cryptonote_core/cryptonote_core.cpp:528 Loading blockchain from folder /home/xyz/.bitmonero/testnet/lmdb ...
2026-05-14 10:21:58.874     7fe7ddaaaac0  INFO  global  src/cryptonote_core/blockchain.cpp:438  Current top block <48843127c1596f7f4fffdfb26b8b4862febb24879d7daf5ad75b791a64497c2d> at height 2921180 has version 18 which disagrees with the ideal version 16
2026-05-14 10:21:58.874     7fe7ddaaaac0  INFO  global  src/cryptonote_core/blockchain.cpp:440  Popping blocks... 2921180
2026-05-14 10:21:58.881     7fe7ddaaaac0  ERROR cn  src/cryptonote_basic/cryptonote_format_utils.cpp:261  Failed to parse transaction from blob
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:126  Exception: cryptonote::DB_ERROR
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:127  Unwound call stack:
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [1]  0xa3) [0x564ab3165fa1]:__cxa_throw+0xa3) [0x564ab3165fa1]
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [2] /home/xyz/monero-fcmp/install/bin/monerod(+0xadd19) [0x564ab310dd19]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [3] /home/xyz/monero-fcmp/install/bin/monerod(+0x65b079) [0x564ab36bb079]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [4] /home/xyz/monero-fcmp/install/bin/monerod(+0x668e9b) [0x564ab36c8e9b]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [5] /home/xyz/monero-fcmp/install/bin/monerod(+0x74c861) [0x564ab37ac861]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [6] /home/xyz/monero-fcmp/install/bin/monerod(+0x770bcc) [0x564ab37d0bcc]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [7] /home/xyz/monero-fcmp/install/bin/monerod(+0x1e755e) [0x564ab324755e]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [8] /home/xyz/monero-fcmp/install/bin/monerod(+0x23f1dc) [0x564ab329f1dc]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [9] /home/xyz/monero-fcmp/install/bin/monerod(+0x1d0204) [0x564ab3230204]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [10] /home/xyz/monero-fcmp/install/bin/monerod(+0x24109a) [0x564ab32a109a]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [11] /home/xyz/monero-fcmp/install/bin/monerod(+0x1906a3) [0x564ab31f06a3]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [12] /lib/libc.so.6(+0x2b285) [0x7fe7dcc2b285]                                                         
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [13]  0x88) [0x7fe7dcc2b338]:__libc_start_main+0x88) [0x7fe7dcc2b338]
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165      [14] /home/xyz/monero-fcmp/install/bin/monerod(+0x199be5) [0x564ab31f9be5]  
2026-05-14 10:21:58.881     7fe7ddaaaac0  INFO  stacktrace  src/common/stack_trace.cpp:165
2026-05-14 10:21:58.881     7fe7ddaaaac0  ERROR blockchain  src/cryptonote_core/blockchain.cpp:452  Error popping block from blockchain: Failed to parse transaction from blob retrieved from the db
2026-05-14 10:21:58.918     7fe7ddaaaac0  INFO  global  src/daemon/protocol.h:79  Stopping cryptonote protocol...
2026-05-14 10:21:58.918     7fe7ddaaaac0  INFO  global  src/daemon/protocol.h:83  Cryptonote protocol stopped successfully
2026-05-14 10:21:58.918     7fe7ddaaaac0  ERROR daemon  src/daemon/main.cpp:366 Exception in main! Failed to parse transaction from blob retrieved from the db

```

# Discussion History
## j-berman | 2026-05-14T15:59:23+00:00
The alpha db is incompatible with the beta db. I'd recommend deleting your blockchain data dir and re-syncing from scratch using the latest beta version.

## bvcxza | 2026-05-15T10:49:08+00:00
Wallet balance lost too?

## nahuhh | 2026-05-15T11:16:01+00:00
Your alpha balance is lost, yes.

your pre-alpha testnet balance is not

# Action History
- Created by: bvcxza | 2026-05-14T10:37:04+00:00
