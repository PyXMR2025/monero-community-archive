---
title: 'Trying connect from mobile wallet to monerod node: Signature mismatch, connection
  will be closed'
source_url: https://github.com/monero-project/monero/issues/4082
author: minzak
assignees: []
labels: []
created_at: '2018-06-29T14:54:36+00:00'
updated_at: '2018-06-29T16:06:14+00:00'
type: issue
status: closed
closed_at: '2018-06-29T16:06:14+00:00'
---

# Original Description
I run Monerod with systemd:
`ExecStart=/usr/local/bin/monerod --non-interactive --detach --no-igd --confirm-external-bind --restricted-rpc --fast-block-sync=0 --show-time-stats=1 --pidfile=/mnt/monero/monerod.pid --config-file=/mnt/monero/monerod.conf`

Where **monerod.conf** is:
```
data-dir=/mnt/monero
log-file=/mnt/monero/logs/monerod.log
log-level=4
p2p-bind-ip=178.128.XX.XX
p2p-bind-port=18080
zmq-rpc-bind-ip=127.0.0.1
zmq-rpc-bind-port=18082
rpc-bind-ip=127.0.0.1
rpc-bind-port=18081
```

In logs i see:
```
2018-06-29 14:41:06.470 [P2P5]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#26 to 0.0.0.0 currently we have sockets count:8
2018-06-29 14:41:06.470 [P2P5]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=2
2018-06-29 14:41:06.470 [P2P5]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 33] new connection from 176.36.83.XX:52364 INC to 178.128.20X.XX:18080, total sockets objects 8
2018-06-29 14:41:06.470 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:1761       [176.36.83.XX:52364 05e2f5a6-5c1d-9835-a57b-901da15d179c INC] NEW CONNECTION
2018-06-29 14:41:06.470 [P2P5]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type P2P 178.128.20X.XX:18080 <--> 176.36.83.XX:52364
2018-06-29 14:41:06.470 [P2P5]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 33] Some not success at read: End of file:2
2018-06-29 14:41:06.470 [P2P5]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:100   [sock 33] Socket destroyed without shutdown.
2018-06-29 14:41:06.470 [P2P5]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 33] Socket destroyed
2018-06-29 14:41:06.470 [P2P5]  INFO    net.p2p src/p2p/net_node.inl:1776       [176.36.83.XX:52364 05e2f5a6-5c1d-9835-a57b-901da15d179c INC] CLOSE CONNECTION
2018-06-29 14:41:06.470 [P2P5]  TRACE   net     contrib/epee/include/net/levin_protocol_handler_async.h:290     [176.36.83.XX:52364 INC] ~async_protocol_handler()
2018-06-29 14:41:06.470 [P2P5]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#22 to 176.36.83.XX
2018-06-29 14:41:08.480 [P2P8]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 342122 < 342135 (last time 342122)
2018-06-29 14:41:08.480 [P2P8]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 342123 < 342135 (last time 342123)
...
2018-06-29 14:41:08.657 [P2P9]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 342134 < 342135 (last time 342135)
2018-06-29 14:41:08.658 [P2P1]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 342134 < 342135 (last time 342134)
2018-06-29 14:41:08.658 [P2P1]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:316        dbg >>> global-OUT: speed is A=  27.203 vs Max=2.09715e+06  so sleep: D=-9.51857 sec E=     259 (Enow=   24487) M=2.09715e+06 W=   9.521 R=1.99667e+07 Wgood      11 History: [0 0 0 0 0 0 0 0 0 259 ] m_last_sample_time=  342136
...
2018-06-29 14:41:10.120 [P2P2]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 14:41:10.120 [P2P2]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#27 to 0.0.0.0 currently we have sockets count:7
2018-06-29 14:41:10.120 [P2P2]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=2
2018-06-29 14:41:10.120 [P2P2]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 32] new connection from 176.36.83.XX:52370 INC to 178.128.20X.XX:18080, total sockets objects 7
2018-06-29 14:41:10.120 [P2P2]  INFO    net.p2p src/p2p/net_node.inl:1761       [176.36.83.XX:52370 687b40be-57d6-a467-2695-39693961a2ae INC] NEW CONNECTION
2018-06-29 14:41:10.120 [P2P2]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type P2P 178.128.20X.XX:18080 <--> 176.36.83.XX:52370
2018-06-29 14:41:10.121 [P2P2]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second -9.1528e+126 < 342136 (last time -9.1528e+126)
2018-06-29 14:41:10.121 [P2P2]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 14:41:10.121 [P2P2]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 342135 < 342136 (last time 342136)
2018-06-29 14:41:10.121 [P2P2]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~122b  (from 122 b) Speed AVG=   0[w=9.985]    0[w=9.985] /  Limit=8192 KiB/sec  [122 168 0 0 0 0 0 0 0 0 ]
2018-06-29 14:41:10.121 [P2P2]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:316        dbg <<< global-IN: speed is A= 29.0436 vs Max=8.38861e+06  so sleep: D=-9.98496 sec E=     290 (Enow=     412) M=8.38861e+06 W=   9.985 R=8.376e+07 Wgood      11 History: [122 168 0 0 0 0 0 0 0 0 ] m_last_sample_time=  342137
2018-06-29 14:41:10.121 [P2P2]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:498     [176.36.83.XX:52370 INC] Signature mismatch, connection will be closed
2018-06-29 14:41:10.122 [P2P2]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 32] Socket destroyed
2018-06-29 14:41:10.122 [P2P2]  INFO    net.p2p src/p2p/net_node.inl:1776       [176.36.83.XX:52370 687b40be-57d6-a467-2695-39693961a2ae INC] CLOSE CONNECTION
2018-06-29 14:41:10.122 [P2P2]  TRACE   net     contrib/epee/include/net/levin_protocol_handler_async.h:290     [176.36.83.XX:52370 INC] ~async_protocol_handler()
2018-06-29 14:41:10.122 [P2P2]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#26 to 176.36.83.XX

```

In mobile wallet i got "node connection failed! .... "

What is wrong?


# Discussion History
## moneromooo-monero | 2018-06-29T15:50:35+00:00
Are you trying to connect the wallet to the P2P connection ?
Your RPC connection is on 18081. You should be using that one.


## minzak | 2018-06-29T16:06:14+00:00
Ow..... 
yes 18080 it is p2p (
(Нужно меньше работать)

My port is 18081 but on 0.0.0.0 IP. And now is all fine!
@moneromooo-monero  thanks!

# Action History
- Created by: minzak | 2018-06-29T14:54:36+00:00
- Closed at: 2018-06-29T16:06:14+00:00
