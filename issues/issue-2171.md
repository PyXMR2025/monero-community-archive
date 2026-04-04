---
title: Daemon stacks at memory map resizing
source_url: https://github.com/monero-project/monero/issues/2171
author: SJMartins
assignees: []
labels:
- invalid
created_at: '2017-07-14T02:08:27+00:00'
updated_at: '2017-09-20T19:24:23+00:00'
type: issue
status: closed
closed_at: '2017-09-20T19:24:23+00:00'
---

# Original Description
Hi, I'm using GUI for Win64 (Win10, RAM 8Gb) and Minerod crashes at LMDB loading.

Any clue on how to deal with it?


2017-07-13 23:01:18.876 8840    INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-07-13 23:01:18.884 8840    INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-07-13 23:01:18.890 8840    INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-07-13 23:01:18.895 8840    INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-07-13 23:01:18.901 8840    INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-07-13 23:01:21.369 8840    INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-07-13 23:01:21.370 8840    INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-07-13 23:01:21.377 8840    INFO    global  contrib/epee/include/net/http_server_impl_base.h:70  Binding on 127.0.0.1:18081
2017-07-13 23:01:21.379 8840    INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-07-13 23:01:21.380 8840    INFO    global  src/daemon/core.h:73    Initializing core...
2017-07-13 23:01:21.389 8840    INFO    global  src/cryptonote_core/cryptonote_core.cpp:326     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-07-13 23:01:21.406 8840    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1138 LMDB memory map needs to be resized, doing that now.
2017-07-13 23:01:21.409 8840    INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:487  LMDB Mapsize increased.  Old: 7168MiB, New: 8192MiB


# Discussion History
## perl5577 | 2017-07-14T07:52:48+00:00
Your are space on disk ?

## moneromooo-monero | 2017-07-14T09:12:57+00:00
If it crashes, give a stack trace if you can (not sure how to do that on Windows).
If it just gets stuck (as the title implies), wait a bit, as it might be timing out on some network call.
You can also run with "--log-level 2", which should give more information about where exactly it's crashing or getting stuck.

## SJMartins | 2017-07-16T01:05:38+00:00
The log level 2:

2017-07-15 22:04:17.727 6032    INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-07-15 22:04:17.729 6032    INFO    global  contrib/epee/src/mlog.cpp:153   New log categories: *:DEBUG
2017-07-15 22:04:17.729 6032    INFO    global  src/daemon/main.cpp:282 Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-07-15 22:04:17.731 6032    INFO    daemon  src/daemon/main.cpp:284 Moving from main() into the daemonize now.
2017-07-15 22:04:17.731 6032    INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...
2017-07-15 22:04:17.732 6032    INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK
2017-07-15 22:04:17.733 6032    INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2017-07-15 22:04:17.735 8696    DEBUG   net.p2p src/p2p/net_node.inl:455        dns_threads[0] created for: seeds.moneroseeds.se
2017-07-15 22:04:17.735 5888    DEBUG   net.p2p src/p2p/net_node.inl:455        dns_threads[1] created for: seeds.moneroseeds.ae.org
2017-07-15 22:04:17.735 18000   DEBUG   net.p2p src/p2p/net_node.inl:455        dns_threads[2] created for: seeds.moneroseeds.ch
2017-07-15 22:04:17.736 6032    DEBUG   net.p2p src/p2p/net_node.inl:483        dns_threads created, now waiting for completion or timeout of 20000ms
2017-07-15 22:04:17.736 4716    DEBUG   net.p2p src/p2p/net_node.inl:455        dns_threads[3] created for: seeds.moneroseeds.li
2017-07-15 22:04:18.466 8696    DEBUG   net.p2p src/p2p/net_node.inl:463        dns_threads[0] DNS resolve done
2017-07-15 22:04:18.466 8696    INFO    net.p2p src/p2p/net_node.inl:475        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2017-07-15 22:04:18.495 18000   DEBUG   net.p2p src/p2p/net_node.inl:463        dns_threads[2] DNS resolve done
2017-07-15 22:04:18.496 18000   INFO    net.p2p src/p2p/net_node.inl:475        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2017-07-15 22:04:18.498 4716    DEBUG   net.p2p src/p2p/net_node.inl:463        dns_threads[3] DNS resolve done
2017-07-15 22:04:18.498 4716    INFO    net.p2p src/p2p/net_node.inl:475        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2017-07-15 22:04:18.775 5888    DEBUG   net.p2p src/p2p/net_node.inl:463        dns_threads[1] DNS resolve done
2017-07-15 22:04:18.776 5888    INFO    net.p2p src/p2p/net_node.inl:475        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2017-07-15 22:04:18.777 6032    DEBUG   net.p2p src/p2p/net_node.inl:499        DNS lookup for seeds.moneroseeds.se: 0 results
2017-07-15 22:04:18.778 6032    DEBUG   net.p2p src/p2p/net_node.inl:499        DNS lookup for seeds.moneroseeds.ae.org: 0 results
2017-07-15 22:04:18.778 6032    DEBUG   net.p2p src/p2p/net_node.inl:499        DNS lookup for seeds.moneroseeds.ch: 0 results
2017-07-15 22:04:18.779 6032    DEBUG   net.p2p src/p2p/net_node.inl:499        DNS lookup for seeds.moneroseeds.li: 0 results
2017-07-15 22:04:18.779 6032    INFO    net.p2p src/p2p/net_node.inl:513        DNS seed node lookup either timed out or failed, falling back to defaults
2017-07-15 22:04:18.780 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 107.152.130.98:18080
2017-07-15 22:04:18.781 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 107.152.130.98:18080
2017-07-15 22:04:18.781 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 161.67.132.39:18080
2017-07-15 22:04:18.782 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 161.67.132.39:18080
2017-07-15 22:04:18.782 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 163.172.182.165:18080
2017-07-15 22:04:18.783 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 163.172.182.165:18080
2017-07-15 22:04:18.784 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 195.154.123.123:28080
2017-07-15 22:04:18.784 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 195.154.123.123:28080
2017-07-15 22:04:18.786 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 198.74.231.92:18080
2017-07-15 22:04:18.787 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 198.74.231.92:18080
2017-07-15 22:04:18.787 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 212.83.172.165:28080
2017-07-15 22:04:18.788 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 212.83.172.165:28080
2017-07-15 22:04:18.789 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 212.83.175.67:18080
2017-07-15 22:04:18.789 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 212.83.175.67:18080
2017-07-15 22:04:18.790 6032    DEBUG   net.p2p src/p2p/net_node.inl:524        Seed node: 5.9.100.248:18080
2017-07-15 22:04:18.790 6032    INFO    net.p2p src/p2p/net_node.inl:390        Added seed node: 5.9.100.248:18080
2017-07-15 22:04:18.791 6032    DEBUG   net.p2p src/p2p/net_node.inl:527        Number of seed nodes: 8
2017-07-15 22:04:18.793 6032    INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+006 kbps
2017-07-15 22:04:18.793 6032    INFO    net.p2p src/p2p/net_node.inl:1747       Set limit-up to 2048 kB/s
2017-07-15 22:04:18.794 6032    INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-07-15 22:04:18.794 6032    INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-07-15 22:04:18.796 6032    INFO    net.p2p src/p2p/net_node.inl:1761       Set limit-down to 8192 kB/s
2017-07-15 22:04:18.797 6032    INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 4.40402e+006 kbps
2017-07-15 22:04:18.797 6032    INFO    net.p2p src/p2p/net_node.inl:1783       Set limit-up to 2048 kB/s
2017-07-15 22:04:18.798 6032    INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-07-15 22:04:18.798 6032    INFO    net.throttle    src/p2p/network_throttle-detail.cpp:162 Setting LIMIT: 8.38861e+006 kbps
2017-07-15 22:04:18.799 6032    INFO    net.p2p src/p2p/net_node.inl:1787       Set limit-down to 8192 kB/s
2017-07-15 22:04:18.805 6032    INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:794   Set server type to: 2 from name: P2P, prefix_name = P2P
2017-07-15 22:04:18.807 6032    INFO    net.p2p src/p2p/net_node.inl:566        Binding on 0.0.0.0:18080
2017-07-15 22:04:18.808 6032    DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:733   start accept
2017-07-15 22:04:18.808 6032    INFO    net.p2p src/p2p/connection_basic.cpp:164        Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-07-15 22:04:18.809 6032    INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85 test, connection constructor set m_connection_type=2
2017-07-15 22:04:18.810 6032    INFO    net.p2p src/p2p/net_node.inl:571        [1;32mNet service bound to 0.0.0.0:18080[0m
2017-07-15 22:04:18.810 6032    DEBUG   net.p2p src/p2p/net_node.inl:577        Attempting to add IGD port mapping.
2017-07-15 22:04:20.021 6032    WARN    net.p2p src/p2p/net_node.inl:607        IGD was found but reported as not connected.
2017-07-15 22:04:20.021 6032    INFO    global  src/daemon/p2p.h:68     P2p server initialized OK
2017-07-15 22:04:20.022 6032    INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...
2017-07-15 22:04:20.023 6032    INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:794   Set server type to: 1 from name: RPC, prefix_name = RPC
2017-07-15 22:04:20.207 6032    INFO    global  contrib/epee/include/net/http_server_impl_base.h:70  Binding on 127.0.0.1:18081
2017-07-15 22:04:20.208 6032    DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:733   start accept
2017-07-15 22:04:20.209 6032    INFO    net.p2p src/p2p/connection_basic.cpp:164        Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2017-07-15 22:04:20.209 6032    INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:85 test, connection constructor set m_connection_type=1
2017-07-15 22:04:20.210 6032    INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081
2017-07-15 22:04:20.211 6032    INFO    global  src/daemon/core.h:73    Initializing core...
2017-07-15 22:04:20.213 6032    INFO    global  src/cryptonote_core/cryptonote_core.cpp:326     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-07-15 22:04:20.215 6032    DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:342     option: fast
2017-07-15 22:04:20.215 6032    DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:342     option: async
2017-07-15 22:04:20.216 6032    DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:342     option: 1000
2017-07-15 22:04:20.219 6032    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:71   Failed to open lmdb environment: Input/output error
2017-07-15 22:04:20.219 6032    ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:395     Error opening database: Failed to open lmdb environment: Input/output error
2017-07-15 22:04:20.220 6032    INFO    global  src/daemon/rpc.h:90     Deinitializing rpc server...
2017-07-15 22:04:20.220 6032    INFO    net.p2p src/p2p/connection_basic.cpp:172        Destructing connection p2p#0 to 0.0.0.0
2017-07-15 22:04:20.221 6032    INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...
2017-07-15 22:04:20.222 6032    INFO    net     src/p2p/net_node.h:241  Killing the net_node
2017-07-15 22:04:20.223 6032    INFO    net     src/p2p/net_node.h:245  Joined extra background net_node threads
2017-07-15 22:04:20.225 6032    WARN    net.p2p src/p2p/net_node.inl:704        Failed to save config to file C:\ProgramData\bitmonero/p2pstate.bin
2017-07-15 22:04:20.226 6032    INFO    net.p2p src/p2p/connection_basic.cpp:172        Destructing connection p2p#0 to 0.0.0.0
2017-07-15 22:04:20.228 6032    INFO    global  src/daemon/core.h:89    Deinitializing core...
2017-07-15 22:04:20.230 6032    DEBUG   miner   src/cryptonote_basic/miner.cpp:325      Not mining - nothing to stop
2017-07-15 22:04:20.231 6032    INFO    txpool  src/cryptonote_core/tx_pool.cpp:788     Received signal to deactivate memory pool store
2017-07-15 22:04:20.232 6032    ERROR   txpool  src/cryptonote_core/tx_pool.cpp:806     Failed to serialize memory pool to file C:\ProgramData\bitmonero/poolstate.bin
2017-07-15 22:04:20.233 6032    ERROR   daemon  src/daemon/core.h:94    Failed to deinitialize core...
2017-07-15 22:04:20.233 6032    DEBUG   miner   src/cryptonote_basic/miner.cpp:325      Not mining - nothing to stop
2017-07-15 22:04:20.234 6032    INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...
2017-07-15 22:04:20.234 6032    INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully


## moneromooo-monero | 2017-07-16T07:53:12+00:00
>  Input/output error

That means your hard disk has hardware issues and is starting to fail.

hyc: can LMDB cause EIO for other reasons (ie, some weird case of page faults) ?


## hyc | 2017-09-20T19:21:35+00:00
Nope, EIO is only returned for hardware failures. Note that this log also shows failures writing p2pstate.bin and poolstate.bin - the disk is definitely trashed. Not our bug.
+invalid


# Action History
- Created by: SJMartins | 2017-07-14T02:08:27+00:00
- Closed at: 2017-09-20T19:24:23+00:00
