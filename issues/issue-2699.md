---
title: Problem running monerod on OpenBSD
source_url: https://github.com/monero-project/monero/issues/2699
author: ston1th
assignees: []
labels: []
created_at: '2017-10-22T09:59:39+00:00'
updated_at: '2017-11-01T13:47:54+00:00'
type: issue
status: closed
closed_at: '2017-11-01T13:47:54+00:00'
---

# Original Description
Hello guys,

im trying to run the latest release version v0.11.0.0-release on OpenBSD 6.2 -stable.

It seems like the initial sync is failing:

```
2017-10-22 09:47:10.080   0x1ef064b2b280        INFO    logging contrib/epee/src/mlog.cpp:148   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-10-22 09:47:10.081   0x1ef064b2b280        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-22 09:47:10.081   0x1ef064b2b280        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-22 09:47:10.081   0x1ef064b2b280        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-10-22 09:47:10.088   0x1ef064b2b280        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-10-22 09:47:14.208   0x1ef064b2b280        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-22 09:47:14.208   0x1ef064b2b280        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-22 09:47:14.208   0x1ef064b2b280        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-22 09:47:14.213   0x1ef064b2b280        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-22 09:47:14.214   0x1ef064b2b280        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-22 09:47:14.216   0x1ef064b2b280        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-10-22 09:47:14.229   0x1ef064b2b280        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-10-22 09:47:14.229   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: cryptonote::DB_ERROR
2017-10-22 09:47:14.229   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-10-22 09:47:14.229   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:159  
2017-10-22 09:47:14.392   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: cryptonote::DB_ERROR
2017-10-22 09:47:14.392   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-10-22 09:47:14.392   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:159  
2017-10-22 09:47:14.392   0x1ef064b2b280        ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3403 Error adding block with hash: <418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3> to blockchain, what = Error adding hard fork version to db transaction: MDB_NOTFOUND: No matching key/data pair found
2017-10-22 09:47:14.392   0x1ef064b2b280        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Attempt to get hash from height 0 failed -- hash not in db
2017-10-22 09:47:14.392   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: cryptonote::BLOCK_DNE
2017-10-22 09:47:14.392   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2017-10-22 09:47:14.392   0x1ef064b2b280        INFO    stacktrace      src/common/stack_trace.cpp:159  
2017-10-22 09:47:14.392   0x1ef064b2b280        FATAL   daemon  src/daemon/daemon.cpp:150       Uncaught exception! Attempt to get hash from height 0 failed -- hash not in db
2017-10-22 09:47:14.392   0x1ef064b2b280        INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-10-22 09:47:14.393   0x1ef064b2b280        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-10-22 09:47:14.394   0x1ef064b2b280        INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-10-22 09:47:14.403   0x1ef064b2b280        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-10-22 09:47:14.404   0x1ef064b2b280        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
```

Running it again causes a segfault:
```
gdb monerod monerod.core  
GNU gdb 6.3
Copyright 2004 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "amd64-unknown-openbsd6.2"...
Core was generated by `monerod'.
Program terminated with signal 11, Segmentation fault.
Reading symbols from /usr/lib/libpthread.so.24.0...done.
Loaded symbols for /usr/lib/libpthread.so.24.0
Loaded symbols for /var/monero/monerod
Reading symbols from /usr/lib/libssl.so.44.1...done.
Loaded symbols for /usr/lib/libssl.so.44.1
Reading symbols from /usr/lib/libcrypto.so.42.0...done.
Loaded symbols for /usr/lib/libcrypto.so.42.0
Reading symbols from /usr/local/lib/libestdc++.so.17.1...done.
Loaded symbols for /usr/local/lib/libestdc++.so.17.1
Reading symbols from /usr/lib/libm.so.10.0...done.
Loaded symbols for /usr/lib/libm.so.10.0
Symbols already loaded for /usr/lib/libpthread.so.24.0
Reading symbols from /usr/lib/libc.so.90.0...done.
Loaded symbols for /usr/lib/libc.so.90.0
Reading symbols from /usr/libexec/ld.so...done.
Loaded symbols for /usr/libexec/ld.so
#0  0x00000f72a3ef3ec5 in mdb_cursor_put.part.18 () from monerod
(gdb)
```

# Discussion History
## moneromooo-monero | 2017-10-22T10:03:01+00:00
Can you type "bt" here and paste the output ?

## ston1th | 2017-10-22T10:03:53+00:00
```
(gdb) bt
#0  0x00000f72a3ef3ec5 in mdb_cursor_put.part.18 () from monerod
#1  0x83a58e86b80c9dfa in ?? ()
#2  0x00020000b80c9dfa in ?? ()
#3  0x00000f7400000000 in ?? ()
#4  0x00007f7f00000000 in ?? ()
#5  0x0000000000000000 in ?? ()
```

## moneromooo-monero | 2017-10-22T10:05:56+00:00
Can you build a debug version ? And if possible with libunwind so we get stack traces for the exceptions.

## ston1th | 2017-10-22T10:43:32+00:00
First run:
```
./monerod-debug --log-level 4 
2017-10-22 10:40:44.631         0x82c8546280        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-22 10:40:44.633      0x82c8546280        INFO    daemon  src/daemon/main.cpp:281 Moving from main() into the daemonize now.
2017-10-22 10:40:44.634      0x82c8546280        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-22 10:40:44.634      0x82c8546280        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-10-22 10:40:44.637      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:136  Blockchain::Blockchain
2017-10-22 10:40:44.644      0x82c8546280        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-10-22 10:40:44.646      0x82eb1f7a38        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[0] created for: seeds.moneroseeds.se
2017-10-22 10:40:44.646      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:489        dns_threads created, now waiting for completion or timeout of 20000ms
2017-10-22 10:40:44.647      0x82eb1f8838        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[2] created for: seeds.moneroseeds.ch
2017-10-22 10:40:44.647      0x82eb1f8038        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-10-22 10:40:44.647      0x82eb1f8a38        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[3] created for: seeds.moneroseeds.li
2017-10-22 10:40:44.749      0x82eb1f7a38        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[0] DNS resolve done
2017-10-22 10:40:44.767      0x82eb1f8038        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[1] DNS resolve done
2017-10-22 10:40:44.768      0x82eb1f8038        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-10-22 10:40:44.768      0x82eb1f7a38        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-10-22 10:40:44.786      0x82eb1f8a38        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[3] DNS resolve done
2017-10-22 10:40:44.786      0x82eb1f8a38        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-10-22 10:40:44.786      0x82eb1f8838        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[2] DNS resolve done
2017-10-22 10:40:44.786      0x82eb1f8838        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-10-22 10:40:44.787      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.se: 0 results
2017-10-22 10:40:44.787      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-10-22 10:40:44.787      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ch: 0 results
2017-10-22 10:40:44.788      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.li: 0 results
2017-10-22 10:40:44.788      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:519        DNS seed node lookup either timed out or failed, falling back to defaults
2017-10-22 10:40:44.788      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 107.152.130.98:18080
2017-10-22 10:40:44.788      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 107.152.130.98:18080
2017-10-22 10:40:44.788      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 161.67.132.39:18080
2017-10-22 10:40:44.789      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 161.67.132.39:18080
2017-10-22 10:40:44.789      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 163.172.182.165:18080
2017-10-22 10:40:44.789      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 163.172.182.165:18080
2017-10-22 10:40:44.789      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 195.154.123.123:28080
2017-10-22 10:40:44.789      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 195.154.123.123:28080
2017-10-22 10:40:44.789      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 198.74.231.92:18080
2017-10-22 10:40:44.789      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 198.74.231.92:18080
2017-10-22 10:40:44.790      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 212.83.172.165:28080
2017-10-22 10:40:44.790      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 212.83.172.165:28080
2017-10-22 10:40:44.790      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 212.83.175.67:18080
2017-10-22 10:40:44.790      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 212.83.175.67:18080
2017-10-22 10:40:44.790      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 5.9.100.248:18080
2017-10-22 10:40:44.790      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 5.9.100.248:18080
2017-10-22 10:40:44.790      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:533        Number of seed nodes: 8
2017-10-22 10:40:44.799      0x82c8546280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+06 kbps
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:1883       Set limit-up to 2048 kB/s
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:1897       Set limit-down to 8192 kB/s
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+06 kbps
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:1919       Set limit-up to 2048 kB/s
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:40:44.800      0x82c8546280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:40:44.801      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:1923       Set limit-down to 8192 kB/s
2017-10-22 10:40:44.802      0x82c8546280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:795   Set server type to: 2 from name: P2P, prefix_name = P2P
2017-10-22 10:40:44.802      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:572        Binding on 0.0.0.0:18080
2017-10-22 10:40:44.802      0x82c8546280        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:734   start accept
2017-10-22 10:40:44.804      0x82c8546280        INFO    net.p2p src/p2p/connection_basic.cpp:164        Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-10-22 10:40:44.804      0x82c8546280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85    test, connection constructor set m_connection_type=2
2017-10-22 10:40:44.804      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:577        Net service bound to 0.0.0.0:18080
2017-10-22 10:40:44.804      0x82c8546280        DEBUG   net.p2p src/p2p/net_node.inl:583        Attempting to add IGD port mapping.
2017-10-22 10:40:48.847      0x82c8546280        INFO    net.p2p src/p2p/net_node.inl:622        No IGD was found.
2017-10-22 10:40:48.847      0x82c8546280        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-22 10:40:48.847      0x82c8546280        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-22 10:40:48.852      0x82c8546280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:795   Set server type to: 1 from name: RPC, prefix_name = RPC
2017-10-22 10:40:48.852      0x82c8546280        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-22 10:40:48.853      0x82c8546280        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:734   start accept
2017-10-22 10:40:48.853      0x82c8546280        INFO    net.p2p src/p2p/connection_basic.cpp:164        Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-10-22 10:40:48.853      0x82c8546280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85    test, connection constructor set m_connection_type=1
2017-10-22 10:40:48.853      0x82c8546280        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-22 10:40:48.853      0x82c8546280        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-22 10:40:48.856      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1070 BlockchainLMDB::BlockchainLMDB
2017-10-22 10:40:48.856      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1388 BlockchainLMDB::get_db_name
2017-10-22 10:40:48.856      0x82c8546280        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-10-22 10:40:48.858      0x82c8546280        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:339     option: fast
2017-10-22 10:40:48.858      0x82c8546280        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:339     option: async
2017-10-22 10:40:48.858      0x82c8546280        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:339     option: 1000
2017-10-22 10:40:48.858      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1091 BlockchainLMDB::open
2017-10-22 10:40:48.883      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1150 LMDB memory map size: 1073741824
2017-10-22 10:40:48.883      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:502  BlockchainLMDB::need_resize
2017-10-22 10:40:48.883      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:518  DB map size:     1073741824
2017-10-22 10:40:48.884      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:519  Space used:      4096
2017-10-22 10:40:48.884      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:520  Space remaining: 1073737728
2017-10-22 10:40:48.884      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:521  Size threshold:  0
2017-10-22 10:40:48.884      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:523  Percent used: 0.0000  Percent threshold: 0.8000
2017-10-22 10:40:48.886      0x82c8546280        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1219 Setting m_height to: 0
2017-10-22 10:40:48.927      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:48.932      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:288  Blockchain::init
2017-10-22 10:40:48.939      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:48.939      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:40:48.939      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:48.940      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3119 BlockchainLMDB::get_hard_fork_version
2017-10-22 10:40:48.940      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:40:48.940      0x82c8546280        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-10-22 10:40:48.944      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:48.945      0x82c8546280        INFO    hardfork        src/cryptonote_basic/hardfork.cpp:194   The DB has no hard fork info, reparsing from start
2017-10-22 10:40:48.945      0x82c8546280        DEBUG   hardfork        src/cryptonote_basic/hardfork.cpp:197   reorganizing from 1
2017-10-22 10:40:48.945      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:48.945      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:40:48.945      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:48.945      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3100 BlockchainLMDB::set_hard_fork_version
2017-10-22 10:40:48.951      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:48.951      0x82c8546280        DEBUG   hardfork        src/cryptonote_basic/hardfork.cpp:206   reorganization done
2017-10-22 10:40:48.951      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:48.951      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:40:48.951      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:48.951      0x82c8546280        INFO    blockchain      src/cryptonote_core/blockchain.cpp:342  Blockchain not loaded, generating genesis block.
2017-10-22 10:40:49.078      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:3455 Blockchain::add_new_block
2017-10-22 10:40:49.079      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2744 BlockchainLMDB::block_txn_start RO
2017-10-22 10:40:49.079      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:2118 Blockchain::have_block
2017-10-22 10:40:49.079      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1675 BlockchainLMDB::block_exists
2017-10-22 10:40:49.079      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1686 Block with hash 418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3 not found in db
2017-10-22 10:40:49.079      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:563  Blockchain::get_tail_id
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1945 BlockchainLMDB::top_block_hash
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2776 BlockchainLMDB::block_txn_stop
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:3100 Blockchain::handle_block_to_main_chain
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2744 BlockchainLMDB::block_txn_start RO
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:563  Blockchain::get_tail_id
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1945 BlockchainLMDB::top_block_hash
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:3030 Blockchain::check_block_timestamp
2017-10-22 10:40:49.080      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:3001 Blockchain::get_adjusted_time
2017-10-22 10:40:49.081      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.081      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:711  Blockchain::get_difficulty_for_next_block
2017-10-22 10:40:49.081      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.081      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.081      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.167      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:279  Blockchain::get_current_blockchain_height
2017-10-22 10:40:49.167      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.167      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:279  Blockchain::get_current_blockchain_height
2017-10-22 10:40:49.167      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.167      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.167      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:968  Blockchain::prevalidate_miner_transaction
2017-10-22 10:40:49.167      0x82c8546280        DEBUG   blockchain      src/cryptonote_core/blockchain.cpp:976  Miner tx hash: <c88ce9783b4f11190d7b9c17a69c1c52200f9faaee8e98dd07e6811175177139>
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:995  Blockchain::validate_miner_transaction
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:1048 Blockchain::get_last_n_blocks_sizes
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2776 BlockchainLMDB::block_txn_stop
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2828 BlockchainLMDB::add_block
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:49.168      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:502  BlockchainLMDB::need_resize
2017-10-22 10:40:49.169      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:518  DB map size:     1073741824
2017-10-22 10:40:49.169      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:519  Space used:      4096
2017-10-22 10:40:49.169      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:520  Space remaining: 1073737728
2017-10-22 10:40:49.169      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:521  Size threshold:  0
2017-10-22 10:40:49.169      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:523  Percent used: 0.0000  Percent threshold: 0.8000
2017-10-22 10:40:49.169      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2749 BlockchainLMDB::block_txn_start
2017-10-22 10:40:49.169      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.170      0x82c8546280        TRACE   blockchain.db   src/blockchain_db/blockchain_db.cpp:107 null tx_hash_ptr - needed to compute: <c88ce9783b4f11190d7b9c17a69c1c52200f9faaee8e98dd07e6811175177139>
2017-10-22 10:40:49.170      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:753  BlockchainLMDB::add_transaction_data
2017-10-22 10:40:49.170      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.170      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2126 BlockchainLMDB::get_tx_count
2017-10-22 10:40:49.170      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:847  BlockchainLMDB::add_output
2017-10-22 10:40:49.170      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.175      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1987 BlockchainLMDB::num_outputs
2017-10-22 10:40:49.176      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:910  BlockchainLMDB::add_tx_amount_output_indices
2017-10-22 10:40:49.176      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:652  BlockchainLMDB::add_block
2017-10-22 10:40:49.176      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:40:49.176      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3100 BlockchainLMDB::set_hard_fork_version
2017-10-22 10:40:49.176      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:79   Error adding hard fork version to db transaction: MDB_NOTFOUND: No matching key/data pair found
2017-10-22 10:40:49.176      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:49.177      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2800 BlockchainLMDB::block_txn_abort
2017-10-22 10:40:49.177      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:49.177      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:331  mdb_txn_safe: m_txn not NULL in destructor - calling mdb_txn_abort()
2017-10-22 10:40:49.177      0x82c8546280        ERROR   blockchain      src/cryptonote_core/blockchain.cpp:3403 Error adding block with hash: <418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3> to blockchain, what = Error adding hard fork version to db transaction: MDB_NOTFOUND: No matching key/data pair found
2017-10-22 10:40:49.178      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3151 BlockchainLMDB::fixup
2017-10-22 10:40:49.180      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2671 BlockchainLMDB::set_batch_transactions
2017-10-22 10:40:49.180      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2677 batch transactions enabled
2017-10-22 10:40:49.180      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2545 BlockchainLMDB::batch_start
2017-10-22 10:40:49.180      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:553  BlockchainLMDB::check_and_resize_for_batch
2017-10-22 10:40:49.180      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:554  [check_and_resize_for_batch] checking DB size
2017-10-22 10:40:49.180      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:502  BlockchainLMDB::need_resize
2017-10-22 10:40:49.180      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:518  DB map size:     1073741824
2017-10-22 10:40:49.180      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:519  Space used:      4096
2017-10-22 10:40:49.181      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:520  Space remaining: 1073737728
2017-10-22 10:40:49.181      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:521  Size threshold:  0
2017-10-22 10:40:49.181      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:523  Percent used: 0.0000  Percent threshold: 0.8000
2017-10-22 10:40:49.181      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2576 batch transaction: begin
2017-10-22 10:40:49.181      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1894 BlockchainLMDB::get_block_hash_from_height
2017-10-22 10:40:49.181      0x82c8546280        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Attempt to get hash from height 0 failed -- hash not in db
2017-10-22 10:40:49.182      0x82c8546280        FATAL   daemon  src/daemon/daemon.cpp:150       Uncaught exception! Attempt to get hash from height 0 failed -- hash not in db
2017-10-22 10:40:49.182      0x82c8546280        INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-10-22 10:40:49.182      0x82c8546280        TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:94    [sock -1] Socket destroyed without shutdown.
2017-10-22 10:40:49.182      0x82c8546280        TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:98    [sock -1] Socket destroyed
2017-10-22 10:40:49.182      0x82c8546280        INFO    net.p2p src/p2p/connection_basic.cpp:172        Destructing connection p2p#0 to 0.0.0.0
2017-10-22 10:40:49.182      0x82c8546280        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-10-22 10:40:49.182      0x82c8546280        INFO    net     src/p2p/net_node.h:250  Killing the net_node
2017-10-22 10:40:49.182      0x82c8546280        INFO    net     src/p2p/net_node.h:254  Joined extra background net_node threads
2017-10-22 10:40:49.183      0x82c8546280        TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:94    [sock -1] Socket destroyed without shutdown.
2017-10-22 10:40:49.184      0x82c8546280        TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:98    [sock -1] Socket destroyed
2017-10-22 10:40:49.184      0x82c8546280        TRACE   net     contrib/epee/include/net/levin_protocol_handler_async.h:281     [0.0.0.0:0 OUT] ~async_protocol_handler()
2017-10-22 10:40:49.184      0x82c8546280        INFO    net.p2p src/p2p/connection_basic.cpp:172        Destructing connection p2p#0 to 0.0.0.0
2017-10-22 10:40:49.184      0x82c8546280        INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-10-22 10:40:49.185      0x82c8546280        TRACE   miner   src/cryptonote_basic/miner.cpp:333      Miner has received stop signal
2017-10-22 10:40:49.185      0x82c8546280        DEBUG   miner   src/cryptonote_basic/miner.cpp:337      Not mining - nothing to stop
2017-10-22 10:40:49.185      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:437  Blockchain::deinit
2017-10-22 10:40:49.185      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:439  Stopping blockchain read/write activity
2017-10-22 10:40:49.185      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1294 BlockchainLMDB::close
2017-10-22 10:40:49.185      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1297 close() first calling batch_abort() due to active batch transaction
2017-10-22 10:40:49.185      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2648 BlockchainLMDB::batch_abort
2017-10-22 10:40:49.186      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:355  mdb_txn_safe: abort()
2017-10-22 10:40:49.186      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:40:49.186      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2666 batch transaction: aborted
2017-10-22 10:40:49.186      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1310 BlockchainLMDB::sync
2017-10-22 10:40:49.190      0x82c8546280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:457  Local blockchain read/write activity stopped successfully
2017-10-22 10:40:49.190      0x82c8546280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1059 BlockchainLMDB::~BlockchainLMDB
2017-10-22 10:40:49.191      0x82c8546280        TRACE   miner   src/cryptonote_basic/miner.cpp:333      Miner has received stop signal
2017-10-22 10:40:49.191      0x82c8546280        DEBUG   miner   src/cryptonote_basic/miner.cpp:337      Not mining - nothing to stop
2017-10-22 10:40:49.191      0x82c8546280        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-10-22 10:40:49.191      0x82c8546280        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
```

Second run:
```
2017-10-22 10:41:44.518       0x15f5f9fe8280        INFO    global  src/daemon/main.cpp:279 Monero 'Helium Hydra' (v0.11.0.0-release)
2017-10-22 10:41:44.519    0x15f5f9fe8280        INFO    daemon  src/daemon/main.cpp:281 Moving from main() into the daemonize now.
2017-10-22 10:41:44.519    0x15f5f9fe8280        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-10-22 10:41:44.519    0x15f5f9fe8280        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-10-22 10:41:44.520    0x15f5f9fe8280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:136  Blockchain::Blockchain
2017-10-22 10:41:44.530    0x15f5f9fe8280        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-10-22 10:41:44.532    0x15f6353d3838        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[0] created for: seeds.moneroseeds.se
2017-10-22 10:41:44.532    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:489        dns_threads created, now waiting for completion or timeout of 20000ms
2017-10-22 10:41:44.533    0x15f6353d2238        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-10-22 10:41:44.533    0x15f65c6b2e38        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[3] created for: seeds.moneroseeds.li
2017-10-22 10:41:44.534    0x15f65c6b2038        DEBUG   net.p2p src/p2p/net_node.inl:461        dns_threads[2] created for: seeds.moneroseeds.ch
2017-10-22 10:41:44.680    0x15f6353d2238        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[1] DNS resolve done
2017-10-22 10:41:44.680    0x15f6353d2238        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-10-22 10:41:44.681    0x15f6353d3838        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[0] DNS resolve done
2017-10-22 10:41:44.687    0x15f6353d3838        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-10-22 10:41:44.719    0x15f65c6b2038        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[2] DNS resolve done
2017-10-22 10:41:44.719    0x15f65c6b2038        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-10-22 10:41:44.722    0x15f65c6b2e38        DEBUG   net.p2p src/p2p/net_node.inl:469        dns_threads[3] DNS resolve done
2017-10-22 10:41:44.722    0x15f65c6b2e38        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-10-22 10:41:44.723    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.se: 0 results
2017-10-22 10:41:44.723    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-10-22 10:41:44.723    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.ch: 0 results
2017-10-22 10:41:44.723    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:505        DNS lookup for seeds.moneroseeds.li: 0 results
2017-10-22 10:41:44.723    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:519        DNS seed node lookup either timed out or failed, falling back to defaults
2017-10-22 10:41:44.724    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 107.152.130.98:18080
2017-10-22 10:41:44.733    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 107.152.130.98:18080
2017-10-22 10:41:44.733    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 161.67.132.39:18080
2017-10-22 10:41:44.733    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 161.67.132.39:18080
2017-10-22 10:41:44.733    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 163.172.182.165:18080
2017-10-22 10:41:44.733    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 163.172.182.165:18080
2017-10-22 10:41:44.733    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 195.154.123.123:28080
2017-10-22 10:41:44.734    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 195.154.123.123:28080
2017-10-22 10:41:44.734    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 198.74.231.92:18080
2017-10-22 10:41:44.734    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 198.74.231.92:18080
2017-10-22 10:41:44.734    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 212.83.172.165:28080
2017-10-22 10:41:44.734    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 212.83.172.165:28080
2017-10-22 10:41:44.734    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 212.83.175.67:18080
2017-10-22 10:41:44.734    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 212.83.175.67:18080
2017-10-22 10:41:44.734    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:530        Seed node: 5.9.100.248:18080
2017-10-22 10:41:44.735    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:395        Added seed node: 5.9.100.248:18080
2017-10-22 10:41:44.735    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:533        Number of seed nodes: 8
2017-10-22 10:41:44.736    0x15f5f9fe8280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+06 kbps
2017-10-22 10:41:44.736    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:1883       Set limit-up to 2048 kB/s
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:1897       Set limit-down to 8192 kB/s
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+06 kbps
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:1919       Set limit-up to 2048 kB/s
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+06 kbps
2017-10-22 10:41:44.737    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:1923       Set limit-down to 8192 kB/s
2017-10-22 10:41:44.741    0x15f5f9fe8280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:795   Set server type to: 2 from name: P2P, prefix_name = P2P
2017-10-22 10:41:44.741    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:572        Binding on 0.0.0.0:18080
2017-10-22 10:41:44.742    0x15f5f9fe8280        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:734   start accept
2017-10-22 10:41:44.746    0x15f5f9fe8280        INFO    net.p2p src/p2p/connection_basic.cpp:164        Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-10-22 10:41:44.747    0x15f5f9fe8280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85    test, connection constructor set m_connection_type=2
2017-10-22 10:41:44.747    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:577        Net service bound to 0.0.0.0:18080
2017-10-22 10:41:44.747    0x15f5f9fe8280        DEBUG   net.p2p src/p2p/net_node.inl:583        Attempting to add IGD port mapping.
2017-10-22 10:41:48.795    0x15f5f9fe8280        INFO    net.p2p src/p2p/net_node.inl:622        No IGD was found.
2017-10-22 10:41:48.795    0x15f5f9fe8280        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-10-22 10:41:48.797    0x15f5f9fe8280        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-10-22 10:41:48.797    0x15f5f9fe8280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:795   Set server type to: 1 from name: RPC, prefix_name = RPC
2017-10-22 10:41:48.798    0x15f5f9fe8280        INFO    global  contrib/epee/include/net/http_server_impl_base.h:70     Binding on 127.0.0.1:18081
2017-10-22 10:41:48.798    0x15f5f9fe8280        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:734   start accept
2017-10-22 10:41:48.798    0x15f5f9fe8280        INFO    net.p2p src/p2p/connection_basic.cpp:164        Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-10-22 10:41:48.798    0x15f5f9fe8280        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85    test, connection constructor set m_connection_type=1
2017-10-22 10:41:48.798    0x15f5f9fe8280        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-10-22 10:41:48.798    0x15f5f9fe8280        INFO    global  src/daemon/core.h:73    Initializing core...
2017-10-22 10:41:48.805    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1070 BlockchainLMDB::BlockchainLMDB
2017-10-22 10:41:48.805    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1388 BlockchainLMDB::get_db_name
2017-10-22 10:41:48.805    0x15f5f9fe8280        INFO    global  src/cryptonote_core/cryptonote_core.cpp:323     Loading blockchain from folder /root/.bitmonero/lmdb ...
2017-10-22 10:41:48.807    0x15f5f9fe8280        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:339     option: fast
2017-10-22 10:41:48.807    0x15f5f9fe8280        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:339     option: async
2017-10-22 10:41:48.807    0x15f5f9fe8280        DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:339     option: 1000
2017-10-22 10:41:48.807    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1091 BlockchainLMDB::open
2017-10-22 10:41:48.809    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:502  BlockchainLMDB::need_resize
2017-10-22 10:41:48.809    0x15f5f9fe8280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:518  DB map size:     1073741824
2017-10-22 10:41:48.809    0x15f5f9fe8280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:519  Space used:      12288
2017-10-22 10:41:48.809    0x15f5f9fe8280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:520  Space remaining: 1073729536
2017-10-22 10:41:48.809    0x15f5f9fe8280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:521  Size threshold:  0
2017-10-22 10:41:48.809    0x15f5f9fe8280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:523  Percent used: 0.0000  Percent threshold: 0.8000
2017-10-22 10:41:48.810    0x15f5f9fe8280        DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1219 Setting m_height to: 0
2017-10-22 10:41:48.816    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:41:48.816    0x15f5f9fe8280        TRACE   blockchain      src/cryptonote_core/blockchain.cpp:288  Blockchain::init
2017-10-22 10:41:48.817    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:41:48.817    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:41:48.818    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:41:48.818    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3119 BlockchainLMDB::get_hard_fork_version
2017-10-22 10:41:48.818    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:41:48.818    0x15f5f9fe8280        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:72   Error attempting to retrieve a hard fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2017-10-22 10:41:48.820    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:41:48.821    0x15f5f9fe8280        INFO    hardfork        src/cryptonote_basic/hardfork.cpp:194   The DB has no hard fork info, reparsing from start
2017-10-22 10:41:48.821    0x15f5f9fe8280        DEBUG   hardfork        src/cryptonote_basic/hardfork.cpp:197   reorganizing from 1
2017-10-22 10:41:48.822    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1973 BlockchainLMDB::height
2017-10-22 10:41:48.822    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2709 BlockchainLMDB::block_rtxn_start
2017-10-22 10:41:48.822    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:312  mdb_txn_safe: destructor
2017-10-22 10:41:48.822    0x15f5f9fe8280        TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3100 BlockchainLMDB::set_hard_fork_version
Segmentation fault (core dumped)
```

GDB:
```
...
#0  0x000015f6a1034f54 in mdb_cursor_put (mc=0x7f7ffffd3df0, key=0x7f7ffffd4200, data=0x7f7ffffd4220, flags=131072)
    at /tmp/monero-0.11.0.0/external/db_drivers/liblmdb/mdb.c:7542
7542            nsize = IS_LEAF2(mc->mc_pg[mc->mc_top]) ? key->mv_size : mdb_leaf_size(env, key, rdata);
(gdb) bt    
#0  0x000015f6a1034f54 in mdb_cursor_put (mc=0x7f7ffffd3df0, key=0x7f7ffffd4200, data=0x7f7ffffd4220, flags=131072)
    at /tmp/monero-0.11.0.0/external/db_drivers/liblmdb/mdb.c:7542
#1  0x000015f6a103cf4d in mdb_put (txn=0x15f5c0038800, dbi=14, key=0x7f7ffffd4200, data=0x7f7ffffd4220, flags=131072)
    at /tmp/monero-0.11.0.0/external/db_drivers/liblmdb/mdb.c:9639
Die: DW_TAG_unspecified_type (abbrev = 174, offset = 962757)
        has children: FALSE
        attributes:
                DW_AT_name (DW_FORM_strp) string: "decltype(nullptr)"
Dwarf Error: Cannot find type of die [in module /tmp/monero-0.11.0.0/build/debug/src/blockchain_db/libblockchain_db.so]
```

## moneromooo-monero | 2017-10-22T11:01:43+00:00
That's the error:

2017-10-22 10:40:49.176      0x82c8546280        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:79   Error adding hard fork version to db transaction: MDB_NOTFOUND: No matching key/data pair found

Can you log height and version, by adding this as the first line of void BlockchainLMDB::set_hard_fork_version(uint64_t height, uint8_t version)

MGINFO("height: " << height << ", version: " << (unsigned)version);


## hyc | 2017-10-22T11:02:05+00:00
This is a known issue with OpenBSD, it has no unified buffer cache. LMDB will only work on this platform when WRITEMAP is used. In this case, with --db-sync-mode=fastest.

## hyc | 2017-10-22T11:07:24+00:00
could add something like
````
#ifdef OPENBSD
 mdb_flags |= MDB_WRITEMAP;
#endif
````
in blockchain_db/lmdb/db_lmdb.cpp near the `mdb_env_create() ... mdb_flags` stuff is. Using whatever appropriate definition to detect OpenBSD in the preprocessor.

## ston1th | 2017-10-22T11:17:40+00:00
Thank you all for the help!
This seems to fix it: `--db-sync-mode=fastest`.

Edit:

This seems to work fine with the default commandline flags and with `--db-sync-mode=fastest`:
```
--- db_lmdb.cpp.orig    Sun Oct 22 13:28:59 2017
+++ db_lmdb.cpp Sun Oct 22 13:24:11 2017
@@ -1117,6 +1117,9 @@
 
   m_folder = filename;
 
+#ifdef __OpenBSD__
+  mdb_flags |= MDB_WRITEMAP;
+#endif
   // set up lmdb environment
   if ((result = mdb_env_create(&m_env)))
     throw0(DB_ERROR(lmdb_error("Failed to create lmdb environment: ", result).c_str()));
```

# Action History
- Created by: ston1th | 2017-10-22T09:59:39+00:00
- Closed at: 2017-11-01T13:47:54+00:00
