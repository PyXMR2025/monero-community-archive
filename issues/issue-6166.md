---
title: monerod v0.15.0.0 testnet sync block fail！
source_url: https://github.com/monero-project/monero/issues/6166
author: apufvqsp
assignees: []
labels: []
created_at: '2019-11-21T07:34:13+00:00'
updated_at: '2019-11-21T08:20:55+00:00'
type: issue
status: closed
closed_at: '2019-11-21T08:20:55+00:00'
---

# Original Description
monerod log as follows

```
2019-11-21 07:30:45.006 [P2P0]  INFO    net.p2p src/p2p/net_node.inl:1262       0Connect failed to 5.9.100.248:28080
2019-11-21 07:30:45.006 [P2P0]  DEBUG   net.p2p src/p2p/net_node.inl:1255       Connecting to 163.172.182.165:28080(peer_type=1, last_seen: never)...
2019-11-21 07:30:45.006 [P2P0]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:153       Spawned connection #614 to 0.0.0.0 currently we have sockets count:2
2019-11-21 07:30:45.006 [P2P0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:111   test, connection constructor set m_connection_type=2
2019-11-21 07:30:45.006 [P2P0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1452  connections_ size now 1
2019-11-21 07:30:45.006 [P2P0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1529  Trying to connect to 163.172.182.165:28080, bind_ip = 0.0.0.0
2019-11-21 07:30:49.475 [P2P1]  DEBUG   cn      src/cryptonote_core/cryptonote_core.cpp:1881    Not checking block rate, offline or syncing
2019-11-21 07:30:50.007 [P2P0]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:184       Destructing connection #614 to 0.0.0.0
2019-11-21 07:30:50.007 [P2P0]  INFO    net.p2p src/p2p/net_node.inl:1262       0Connect failed to 163.172.182.165:28080
2019-11-21 07:30:50.007 [P2P0]  DEBUG   net.p2p src/p2p/net_node.inl:1255       Connecting to 192.110.160.146:28080(peer_type=1, last_seen: never)...
2019-11-21 07:30:50.007 [P2P0]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:153       Spawned connection #615 to 0.0.0.0 currently we have sockets count:2
2019-11-21 07:30:50.007 [P2P0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:111   test, connection constructor set m_connection_type=2
2019-11-21 07:30:50.007 [P2P0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1452  connections_ size now 1
2019-11-21 07:30:50.007 [P2P0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1529  Trying to connect to 192.110.160.146:28080, bind_ip = 0.0.0.0
2019-11-21 07:30:55.007 [P2P0]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:184       Destructing connection #615 to 0.0.0.0
```
is there anyone else encountered this problem?
How to solve it?

# Discussion History
# Action History
- Created by: apufvqsp | 2019-11-21T07:34:13+00:00
- Closed at: 2019-11-21T08:20:55+00:00
