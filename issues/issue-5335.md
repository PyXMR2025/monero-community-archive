---
title: Core dumped while starting xmr daemon...
source_url: https://github.com/monero-project/monero/issues/5335
author: jq8778
assignees: []
labels: []
created_at: '2019-03-22T19:57:06+00:00'
updated_at: '2019-03-22T20:09:24+00:00'
type: issue
status: closed
closed_at: '2019-03-22T20:02:17+00:00'
---

# Original Description
logs are here:
2019-03-22 19:55:17.387     7f2142da8780        INFO    global  src/daemon/main.cpp:287 Monero 'Boron Butterfly' (v0.14.0.2-release)
2019-03-22 19:55:17.388     7f2142da8780        INFO    daemon  src/daemon/main.cpp:289 Moving from main() into the daemonize now.
2019-03-22 19:55:17.388     7f2142da8780        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2019-03-22 19:55:17.388     7f2142da8780        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2019-03-22 19:55:17.389     7f2142da8780        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...
2019-03-22 19:55:17.390     7f2142da8780        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2019-03-22 19:55:17.391     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:1929       Set limit-up to 2048 kB/s
2019-03-22 19:55:17.391     7f2142da8780        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2019-03-22 19:55:17.391     7f2142da8780        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2019-03-22 19:55:17.391     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:1942       Set limit-down to 8192 kB/s
2019-03-22 19:55:17.391     7f2142da8780        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 2048 kbps
2019-03-22 19:55:17.391     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:1964       Set limit-up to 2048 kB/s
2019-03-22 19:55:17.391     7f2142da8780        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2019-03-22 19:55:17.392     7f2142da8780        INFO    net.throttle    contrib/epee/src/network_throttle-detail.cpp:162        Setting LIMIT: 8192 kbps
2019-03-22 19:55:17.392     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:1968       Set limit-down to 8192 kB/s
2019-03-22 19:55:17.394     7f214209e700        INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-03-22 19:55:17.394     7f214209e700        INFO    net.dns src/common/dns_utils.cpp:252    adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-03-22 19:55:25.061     7f214189d700        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[1] addr_str: seeds.moneroseeds.ae.org  number of results: 0
2019-03-22 19:55:29.884     7f213909c700        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[2] addr_str: seeds.moneroseeds.ch  number of results: 0
2019-03-22 19:55:32.509     7f214109c700        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[3] addr_str: seeds.moneroseeds.li  number of results: 0
2019-03-22 19:55:36.466     7f214209e700        INFO    net.p2p src/p2p/net_node.inl:481        dns_threads[0] addr_str: seeds.moneroseeds.se  number of results: 0
2019-03-22 19:55:36.466     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:519        DNS seed node lookup either timed out or failed, falling back to defaults
2019-03-22 19:55:36.466     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=107.152.130.98, port=18080
2019-03-22 19:55:36.466     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 107.152.130.98:18080
2019-03-22 19:55:36.466     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=161.67.132.39, port=18080
2019-03-22 19:55:36.466     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 161.67.132.39:18080
2019-03-22 19:55:36.466     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=163.172.182.165, port=18080
2019-03-22 19:55:36.466     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 163.172.182.165:18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=195.154.123.123, port=18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 195.154.123.123:18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=198.74.231.92, port=18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 198.74.231.92:18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=212.83.172.165, port=18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 212.83.172.165:18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=212.83.175.67, port=18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 212.83.175.67:18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:360        Resolving node address: host=5.9.100.248, port=18080
2019-03-22 19:55:36.467     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:377        Added node: 5.9.100.248:18080
2019-03-22 19:55:36.472     7f2142da8780        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:917   Set server type to: 2 from name: P2P, prefix_name = P2P
2019-03-22 19:55:36.472     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:571        Binding on 0.0.0.0:18080
2019-03-22 19:55:36.472     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:576        Net service bound to 0.0.0.0:18080
2019-03-22 19:55:40.477     7f2142da8780        INFO    net.p2p src/p2p/net_node.inl:2070       No IGD was found.
2019-03-22 19:55:40.477     7f2142da8780        INFO    global  src/daemon/p2p.h:68     p2p server initialized OK
2019-03-22 19:55:40.477     7f2142da8780        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2019-03-22 19:55:40.477     7f2142da8780        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:917   Set server type to: 1 from name: RPC, prefix_name = RPC
2019-03-22 19:55:40.477     7f2142da8780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:18081
2019-03-22 19:55:40.477     7f2142da8780        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2019-03-22 19:55:40.478     7f2142da8780        INFO    global  src/daemon/core.h:86    Initializing core...
2019-03-22 19:55:40.478     7f2142da8780        INFO    global  src/cryptonote_core/cryptonote_core.cpp:469     Loading blockchain from folder /root/.bitmonero/lmdb ...
2019-03-22 19:55:40.479     7f2142da8780        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:559  DB map size:     83725833216
2019-03-22 19:55:40.479     7f2142da8780        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:560  Space used:      72186191872
2019-03-22 19:55:40.479     7f2142da8780        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:561  Space remaining: 11539641344
2019-03-22 19:55:40.479     7f2142da8780        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:562  Size threshold:  0
2019-03-22 19:55:40.479     7f2142da8780        INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:564  Percent used: 0.8622  Percent threshold: 0.9000
Segmentation fault (core dumped)


# Discussion History
## jq8778 | 2019-03-22T20:02:17+00:00
solved by adding --db-salvage

# Action History
- Created by: jq8778 | 2019-03-22T19:57:06+00:00
- Closed at: 2019-03-22T20:02:17+00:00
