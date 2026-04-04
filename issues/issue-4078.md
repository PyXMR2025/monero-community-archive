---
title: How to configure monero-wallet to use with mobile app (pair node with mobile
  wallet)?
source_url: https://github.com/monero-project/monero/issues/4078
author: minzak
assignees: []
labels: []
created_at: '2018-06-29T13:50:10+00:00'
updated_at: '2018-06-29T16:37:48+00:00'
type: issue
status: closed
closed_at: '2018-06-29T16:37:48+00:00'
---

# Original Description
I have worked monero node, here is some from logs:

```
root@monero:/mnt/monero/logs# tail -f monero.log
2018-06-29 13:00:51.299 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1171    [176.9.38.XXX:18080 OUT]  Synced 1605641/1605641
2018-06-29 13:00:51.299 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1561    SYNCHRONIZED OK
2018-06-29 13:00:51.299 [P2P4]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1583
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2018-06-29 13:00:51.381 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1561    SYNCHRONIZED OK
2018-06-29 13:00:51.632 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1561    SYNCHRONIZED OK
2018-06-29 13:16:23.826 [P2P7]  INFO    global  src/cryptonote_core/blockchain.cpp:1534 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1602053
id:     <984296ff64bd07f43f01c5896470ed0436ed7b16a7a6d6ffa731f94e5cd010f8>
PoW:    <bd558c8a44f24e75edc5e14095d87bf407fdfcd995f9823985b7e70a00000000>
difficulty:     48520939092
2018-06-29 13:23:32.248 [P2P4]  INFO    global  src/cryptonote_core/blockchain.cpp:1534 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 1604268
id:     <26e4e2ce11b6da2591bcedf19c743c803603b906b4c049c14000fbdfaa6ee3c6>
PoW:    <4a7a65f937a1ac58a774af677260e54711b7d52d88ed6af33b56141400000000>
difficulty:     `54378018794`
```

Now i try run  monero-wallet-rpc:
**monero-wallet-rpc --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18088 --log-level=4 --confirm-external-bind --daemon-port=18088 --trusted-daemon --shared-ringdb-dir=/mnt/monero/shared-ringdb --wallet-dir=/mnt/monero/wallets**

```
root@monero:/mnt/monero# monero-wallet-rpc --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18088 --log-level=4 --confirm-external-bind --daemon-port=18088 --trusted-daemon --shared-ringdb-dir=/mnt/monero/shared-ringdb --wallet-dir=/mnt/monero/wallets
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-29 13:15:33.170     7f31e834c780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:192  Setting log level = 4
2018-06-29 13:15:33.170     7f31e834c780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:195  Logging to: monero-wallet-rpc.log
Logging to monero-wallet-rpc.log
2018-06-29 13:15:33.170     7f31e834c780        DEBUG   device.ledger   src/device/device_ledger.cpp:223        Device 0 Created
2018-06-29 13:15:33.171     7f31e834c780        INFO    wallet.wallet2  src/wallet/wallet2.cpp:5531     ringdb path set to /mnt/monero/shared-ringdb
2018-06-29 13:15:33.218     7f31e834c780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:221    RPC username/password is stored in file monero-wallet-rpc.18088.login
2018-06-29 13:15:33.219     7f31e834c780        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:862   Set server type to: 1 from name: RPC, prefix_name = RPC
2018-06-29 13:15:33.219     7f31e834c780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 0.0.0.0:18088
2018-06-29 13:15:33.219     7f31e834c780        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:791   start accept
2018-06-29 13:15:33.219     7f31e834c780        DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-06-29 13:15:33.219     7f31e834c780        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:15:33.219     7f31e834c780        DEBUG   net     contrib/epee/include/net/net_helper.h:512       Problems at cancel: Bad file descriptor
2018-06-29 13:15:33.219     7f31e834c780        DEBUG   net     contrib/epee/include/net/net_helper.h:515       Problems at shutdown: Bad file descriptor
2018-06-29 13:15:33.219     7f31e834c780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3001   Starting wallet RPC server
2018-06-29 13:15:33.219     7f31e834c780        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:89     Run net_service loop( 1 threads)...
2018-06-29 13:15:33.219 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:887   Run server thread name: RPC
2018-06-29 13:15:33.219 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:894   JOINING all threads
2018-06-29 13:16:33.107 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:16:33.107 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:16:33.107 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:16:33.107 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2018-06-29 13:16:33.107 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:16:33.107 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 8] new connection from 176.36.83.XX:55574 INC to 178.128.20X.XX:18088, total sockets objects 2
2018-06-29 13:16:33.107 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:33.107 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:55574
2018-06-29 13:16:33.108 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 8] Some not success at read: End of file:2
2018-06-29 13:16:40.628 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:16:40.628 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:16:40.628 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:16:40.628 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#2 to 0.0.0.0 currently we have sockets count:3
2018-06-29 13:16:40.628 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:16:40.628 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 9] new connection from 176.36.83.XX:55584 INC to 178.128.20X.XX:18088, total sockets objects 3
2018-06-29 13:16:40.628 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:40.629 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:55584
2018-06-29 13:16:40.630 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337067 (last time 0)
2018-06-29 13:16:40.630 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:40.630 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337067 (last time 0)
2018-06-29 13:16:40.630 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:40.631 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:40.664 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:40.664 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:40.664 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 401 Unauthorized
Server: Epee-based
Content-Length: 98
Content-Type: text/html
Last-Modified: Fri, 29 Jun 2018 13:16:40 GMT
Accept-Ranges: bytes
WWW-authenticate:Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="90R6NuaxoL3Izp1EpQ9Y/Q==",stale=false
WWW-authenticate:Digest qop="auth",algorithm=MD5-sess,realm="monero-rpc",nonce="90R6NuaxoL3Izp1EpQ9Y/Q==",stale=false


2018-06-29 13:16:40.664 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337067 (last time 0)
2018-06-29 13:16:40.664 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~395b  (from 395 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [395 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:40.664 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   do_send() NOW SENSD: packet=395 B
2018-06-29 13:16:40.664 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:40.664 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~98b  (from 98 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [493 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:40.664 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:534   do_send() NOW just queues: packet=98 B, is added to queue-size=2
2018-06-29 13:16:40.664 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:537   [176.36.83.XX:55584 INC] [sock 9] Async send requested 395
2018-06-29 13:16:40.664 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:40.664 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:55584 INC] [sock 9] Async send calledback 395
2018-06-29 13:16:40.664 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:40.664 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:692   handle_write() NOW SENDS: packet=98 B, from  queue size=1
2018-06-29 13:16:40.664 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:55584 INC] [sock 9] Async send calledback 98
2018-06-29 13:16:40.749 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 9] Some not success at read: End of file:2
2018-06-29 13:16:43.107 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:55574 INC] connection timeout, closing
2018-06-29 13:16:43.108 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 8] Socket destroyed
2018-06-29 13:16:43.108 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#0 to 176.36.83.XX
2018-06-29 13:16:45.108 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:16:45.108 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:16:45.109 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:16:45.109 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#3 to 0.0.0.0 currently we have sockets count:3
2018-06-29 13:16:45.109 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:16:45.109 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 8] new connection from 176.36.83.XX:55590 INC to 178.128.20X.XX:18088, total sockets objects 3
2018-06-29 13:16:45.109 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:45.109 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:55590
2018-06-29 13:16:45.111 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 8] Some not success at read: End of file:2
2018-06-29 13:16:48.443 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:16:48.443 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:16:48.443 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:16:48.443 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#4 to 0.0.0.0 currently we have sockets count:4
2018-06-29 13:16:48.443 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:16:48.443 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 10] new connection from 176.36.83.XX:55596 INC to 178.128.20X.XX:18088, total sockets objects 4
2018-06-29 13:16:48.443 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:48.443 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:55596
2018-06-29 13:16:48.443 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 10] Some not success at read: End of file:2
2018-06-29 13:16:50.664 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:55584 INC] connection timeout, closing
2018-06-29 13:16:50.664 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 9] Socket destroyed
2018-06-29 13:16:50.664 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#1 to 176.36.83.XX
2018-06-29 13:16:53.975 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:16:53.975 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:16:53.975 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:16:53.975 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#5 to 0.0.0.0 currently we have sockets count:4
2018-06-29 13:16:53.975 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:16:53.975 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 9] new connection from 176.36.83.XX:55604 INC to 178.128.20X.XX:18088, total sockets objects 4
2018-06-29 13:16:53.975 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:53.976 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:55604
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337080 (last time 0)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337067 < 337080 (last time 337068)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337068 < 337080 (last time 337069)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337069 < 337080 (last time 337070)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337070 < 337080 (last time 337071)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337071 < 337080 (last time 337072)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337072 < 337080 (last time 337073)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337073 < 337080 (last time 337074)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337074 < 337080 (last time 337075)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337075 < 337080 (last time 337076)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337076 < 337080 (last time 337077)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337077 < 337080 (last time 337078)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337078 < 337080 (last time 337079)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 337079 < 337080 (last time 337080)
2018-06-29 13:16:53.976 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~122b  (from 122 b) Speed AVG=   0[w=9.839]    0[w=9.839] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:53.976 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:54.009 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:54.009 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~87b  (from 87 b) Speed AVG=   0[w=9.873]    0[w=9.873] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:54.010 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 401 Unauthorized
Server: Epee-based
Content-Length: 98
Content-Type: text/html
Last-Modified: Fri, 29 Jun 2018 13:16:54 GMT
Accept-Ranges: bytes
WWW-authenticate:Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="ERG9u3XD6U8KO7oBQVEUyg==",stale=false
WWW-authenticate:Digest qop="auth",algorithm=MD5-sess,realm="monero-rpc",nonce="ERG9u3XD6U8KO7oBQVEUyg==",stale=false


2018-06-29 13:16:54.010 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337080 (last time 0)
2018-06-29 13:16:54.010 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~395b  (from 395 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [395 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:54.010 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   do_send() NOW SENSD: packet=395 B
2018-06-29 13:16:54.011 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:54.011 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~98b  (from 98 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [493 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:16:54.011 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:534   do_send() NOW just queues: packet=98 B, is added to queue-size=2
2018-06-29 13:16:54.011 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:537   [176.36.83.XX:55604 INC] [sock 9] Async send requested 395
2018-06-29 13:16:54.012 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:54.012 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:55604 INC] [sock 9] Async send calledback 395
2018-06-29 13:16:54.012 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:16:54.012 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:692   handle_write() NOW SENDS: packet=98 B, from  queue size=1
2018-06-29 13:16:54.012 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:55604 INC] [sock 9] Async send calledback 98
2018-06-29 13:16:54.086 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 9] Some not success at read: End of file:2
2018-06-29 13:16:55.109 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:55590 INC] connection timeout, closing
2018-06-29 13:16:55.109 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 8] Socket destroyed
2018-06-29 13:16:55.109 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#2 to 176.36.83.XX
2018-06-29 13:16:58.443 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:55596 INC] connection timeout, closing
2018-06-29 13:16:58.443 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 10] Socket destroyed
2018-06-29 13:16:58.443 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#3 to 176.36.83.XX
2018-06-29 13:17:04.012 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:55604 INC] connection timeout, closing
2018-06-29 13:17:04.012 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 9] Socket destroyed
2018-06-29 13:17:04.013 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#4 to 176.36.83.XX
^C2018-06-29 13:17:05.731       [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:898   JOINING all threads - almost
2018-06-29 13:17:05.731 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:900   JOINING all threads - DONE
2018-06-29 13:17:05.731 [SRV_MAIN]      INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:96     net_service loop stopped.
2018-06-29 13:17:05.731 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3011   Stopped wallet RPC server
2018-06-29 13:17:05.731 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3014   Saving wallet...
2018-06-29 13:17:05.731 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3016   Successfully saved
2018-06-29 13:17:05.731 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:100   [sock -1] Socket destroyed without shutdown.
2018-06-29 13:17:05.731 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock -1] Socket destroyed
2018-06-29 13:17:05.731 [SRV_MAIN]      DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#5 to 0.0.0.0
2018-06-29 13:17:05.731 [SRV_MAIN]      DEBUG   device.ledger   src/device/device_ledger.cpp:228        Device 0 Destroyed
root@monero:/mnt/monero#

```

In wallet i got error, node connection failed ( it is not depends from exist wallet or create new.

Also i try use **--disable-rpc-login** still can't connect via wallet, but in logs i see code 200 OK

**monero-wallet-rpc --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18088 --log-level=4 --confirm-external-bind --daemon-port=18088 --trusted-daemon --shared-ringdb-dir=/mnt/monero/shared-ringdb --wallet-dir=/mnt/monero/wallets --disable-rpc-login**
```
root@monero:/mnt/monero# monero-wallet-rpc --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18088 --log-level=4 --confirm-external-bind --daemon-port=18088 --trusted-daemon --shared-ringdb-dir=/mnt/monero/shared-ringdb --wallet-dir=/mnt/monero/wallets --disable-rpc-login
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-29 13:30:11.318     7f78ee3ef780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:192  Setting log level = 4
2018-06-29 13:30:11.318     7f78ee3ef780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:195  Logging to: monero-wallet-rpc.log
Logging to monero-wallet-rpc.log
2018-06-29 13:30:11.318     7f78ee3ef780        DEBUG   device.ledger   src/device/device_ledger.cpp:223        Device 0 Created
2018-06-29 13:30:11.319     7f78ee3ef780        INFO    wallet.wallet2  src/wallet/wallet2.cpp:5531     ringdb path set to /mnt/monero/shared-ringdb
2018-06-29 13:30:11.358     7f78ee3ef780        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:862   Set server type to: 1 from name: RPC, prefix_name = RPC
2018-06-29 13:30:11.359     7f78ee3ef780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 0.0.0.0:18088
2018-06-29 13:30:11.359     7f78ee3ef780        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:791   start accept
2018-06-29 13:30:11.359     7f78ee3ef780        DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-06-29 13:30:11.359     7f78ee3ef780        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:30:11.359     7f78ee3ef780        DEBUG   net     contrib/epee/include/net/net_helper.h:512       Problems at cancel: Bad file descriptor
2018-06-29 13:30:11.359     7f78ee3ef780        DEBUG   net     contrib/epee/include/net/net_helper.h:515       Problems at shutdown: Bad file descriptor
2018-06-29 13:30:11.360     7f78ee3ef780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3001   Starting wallet RPC server
2018-06-29 13:30:11.360     7f78ee3ef780        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:89     Run net_service loop( 1 threads)...
2018-06-29 13:30:11.360 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:887   Run server thread name: RPC
2018-06-29 13:30:11.360 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:894   JOINING all threads
2018-06-29 13:30:55.860 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:30:55.860 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:30:55.860 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:30:55.860 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2018-06-29 13:30:55.860 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:30:55.860 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 8] new connection from 176.36.83.XX:56200 INC to 178.128.20X.XX:18088, total sockets objects 2
2018-06-29 13:30:55.861 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:30:55.861 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:56200
2018-06-29 13:30:55.861 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 8] Some not success at read: End of file:2
2018-06-29 13:31:01.275 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:31:01.276 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:31:01.276 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:31:01.276 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#2 to 0.0.0.0 currently we have sockets count:3
2018-06-29 13:31:01.276 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:31:01.276 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 9] new connection from 176.36.83.XX:56208 INC to 178.128.20X.XX:18088, total sockets objects 3
2018-06-29 13:31:01.276 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:31:01.276 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:56208
2018-06-29 13:31:01.277 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337928 (last time 0)
2018-06-29 13:31:01.278 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:31:01.278 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337928 (last time 0)
2018-06-29 13:31:01.278 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:31:01.278 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:31:01.311 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:31:01.311 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:31:01.311 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [176.36.83.XX] GET /json_rpc
2018-06-29 13:31:01.311 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 114
Content-Type: text/plain
Last-Modified: Fri, 29 Jun 2018 13:31:01 GMT
Accept-Ranges: bytes

2018-06-29 13:31:01.311 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 337928 (last time 0)
2018-06-29 13:31:01.311 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~154b  (from 154 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [154 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:31:01.311 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   do_send() NOW SENSD: packet=154 B
2018-06-29 13:31:01.311 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:31:01.311 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~114b  (from 114 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [268 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:31:01.311 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:534   do_send() NOW just queues: packet=114 B, is added to queue-size=2
2018-06-29 13:31:01.311 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:537   [176.36.83.XX:56208 INC] [sock 9] Async send requested 154
2018-06-29 13:31:01.311 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:31:01.311 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:56208 INC] [sock 9] Async send calledback 154
2018-06-29 13:31:01.311 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:31:01.311 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:692   handle_write() NOW SENDS: packet=114 B, from  queue size=1
2018-06-29 13:31:01.311 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:56208 INC] [sock 9] Async send calledback 114
2018-06-29 13:31:01.394 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 9] Some not success at read: End of file:2
2018-06-29 13:31:05.861 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:56200 INC] connection timeout, closing
2018-06-29 13:31:05.861 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 8] Socket destroyed
2018-06-29 13:31:05.862 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#0 to 176.36.83.XX
2018-06-29 13:31:11.311 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:56208 INC] connection timeout, closing
2018-06-29 13:31:11.312 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 9] Socket destroyed
2018-06-29 13:31:11.312 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#1 to 176.36.83.XX
^C2018-06-29 13:31:13.835       [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:898   JOINING all threads - almost
2018-06-29 13:31:13.835 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:900   JOINING all threads - DONE
2018-06-29 13:31:13.835 [SRV_MAIN]      INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:96     net_service loop stopped.
2018-06-29 13:31:13.835 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3011   Stopped wallet RPC server
2018-06-29 13:31:13.835 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3014   Saving wallet...
2018-06-29 13:31:13.835 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3016   Successfully saved
2018-06-29 13:31:13.835 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:100   [sock -1] Socket destroyed without shutdown.
2018-06-29 13:31:13.835 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock -1] Socket destroyed
2018-06-29 13:31:13.835 [SRV_MAIN]      DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#2 to 0.0.0.0
2018-06-29 13:31:13.836 [SRV_MAIN]      DEBUG   device.ledger   src/device/device_ledger.cpp:228        Device 0 Destroyed
root@monero:/mnt/monero#
```

Even if i use login and pass (also use in mobile wallet user:pass@node:port) i got the same:

```
root@monero:/mnt/monero# monero-wallet-rpc --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18088 --log-level=4 --confirm-external-bind --daemon-port=18088 --trusted-daemon --shared-ringdb-dir=/mnt/monero/shared-ringdb --wallet-dir=/mnt/monero/wallets --rpc-login user:pass
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.2.0-release)
2018-06-29 13:53:21.282     7f53dca93780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:192  Setting log level = 4
2018-06-29 13:53:21.282     7f53dca93780        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:195  Logging to: monero-wallet-rpc.log
Logging to monero-wallet-rpc.log
2018-06-29 13:53:21.283     7f53dca93780        DEBUG   device.ledger   src/device/device_ledger.cpp:223        Device 0 Created
2018-06-29 13:53:21.283     7f53dca93780        INFO    wallet.wallet2  src/wallet/wallet2.cpp:5531     ringdb path set to /mnt/monero/shared-ringdb
2018-06-29 13:53:21.317     7f53dca93780        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:862   Set server type to: 1 from name: RPC, prefix_name = RPC
2018-06-29 13:53:21.318     7f53dca93780        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 0.0.0.0:18088
2018-06-29 13:53:21.318     7f53dca93780        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:791   start accept
2018-06-29 13:53:21.318     7f53dca93780        DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-06-29 13:53:21.318     7f53dca93780        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:53:21.318     7f53dca93780        DEBUG   net     contrib/epee/include/net/net_helper.h:512       Problems at cancel: Bad file descriptor
2018-06-29 13:53:21.318     7f53dca93780        DEBUG   net     contrib/epee/include/net/net_helper.h:515       Problems at shutdown: Bad file descriptor
2018-06-29 13:53:21.318     7f53dca93780        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3001   Starting wallet RPC server
2018-06-29 13:53:21.319     7f53dca93780        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:89     Run net_service loop( 1 threads)...
2018-06-29 13:53:21.319 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:887   Run server thread name: RPC
2018-06-29 13:53:21.319 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:894   JOINING all threads
2018-06-29 13:54:19.355 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:54:19.355 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:54:19.355 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:54:19.355 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2018-06-29 13:54:19.355 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:54:19.355 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 8] new connection from 176.36.83.XX:56578 INC to 178.128.20X.XX:18088, total sockets objects 2
2018-06-29 13:54:19.355 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:19.355 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:56578
2018-06-29 13:54:19.357 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 8] Some not success at read: End of file:2
2018-06-29 13:54:23.972 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
2018-06-29 13:54:23.973 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:989   New server for RPC connections
2018-06-29 13:54:23.973 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:717   set m_connection_type = RPC
2018-06-29 13:54:23.973 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#2 to 0.0.0.0 currently we have sockets count:3
2018-06-29 13:54:23.973 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:91    test, connection constructor set m_connection_type=1
2018-06-29 13:54:23.973 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:159   [sock 9] new connection from 176.36.83.XX:56584 INC to 178.128.20X.XX:18088, total sockets objects 3
2018-06-29 13:54:23.973 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:23.973 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:280    connection type RPC 178.128.20X.XX:18088 <--> 176.36.83.XX:56584
2018-06-29 13:54:23.973 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 339330 (last time 0)
2018-06-29 13:54:23.973 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:23.973 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 339330 (last time 0)
2018-06-29 13:54:23.973 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~122b  (from 122 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [122 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:23.973 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:24.006 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.006 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [209 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.006 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 401 Unauthorized
Server: Epee-based
Content-Length: 98
Content-Type: text/html
Last-Modified: Fri, 29 Jun 2018 13:54:24 GMT
Accept-Ranges: bytes
WWW-authenticate:Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="tTwsXCgd4OlwV96KFMmHnA==",stale=false
WWW-authenticate:Digest qop="auth",algorithm=MD5-sess,realm="monero-rpc",nonce="tTwsXCgd4OlwV96KFMmHnA==",stale=false


2018-06-29 13:54:24.006 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 339330 (last time 0)
2018-06-29 13:54:24.006 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~395b  (from 395 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [395 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.006 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   do_send() NOW SENSD: packet=395 B
2018-06-29 13:54:24.006 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:24.006 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~98b  (from 98 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [493 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.006 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:534   do_send() NOW just queues: packet=98 B, is added to queue-size=2
2018-06-29 13:54:24.006 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:537   [176.36.83.XX:56584 INC] [sock 9] Async send requested 395
2018-06-29 13:54:24.006 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:24.006 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:56584 INC] [sock 9] Async send calledback 395
2018-06-29 13:54:24.006 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:24.006 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:692   handle_write() NOW SENDS: packet=98 B, from  queue size=1
2018-06-29 13:54:24.006 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:56584 INC] [sock 9] Async send calledback 98
2018-06-29 13:54:24.073 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~308b  (from 308 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [517 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.073 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~308b  (from 308 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [517 0 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.073 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:09.994531 expiry
2018-06-29 13:54:24.145 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 339330 < 339331 (last time 339331)
2018-06-29 13:54:24.145 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [87 517 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.145 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 339330 < 339331 (last time 339331)
2018-06-29 13:54:24.145 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~87b  (from 87 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [87 517 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.145 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [176.36.83.XX] GET /json_rpc
2018-06-29 13:54:24.146 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 114
Content-Type: text/plain
Last-Modified: Fri, 29 Jun 2018 13:54:24 GMT
Accept-Ranges: bytes


2018-06-29 13:54:24.146 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 339330 < 339331 (last time 339331)
2018-06-29 13:54:24.146 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~154b  (from 154 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [154 493 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.146 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   do_send() NOW SENSD: packet=154 B
2018-06-29 13:54:24.146 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:24.146 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~114b  (from 114 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [268 493 0 0 0 0 0 0 0 0 ]
2018-06-29 13:54:24.146 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:534   do_send() NOW just queues: packet=114 B, is added to queue-size=2
2018-06-29 13:54:24.146 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:537   [176.36.83.XX:56584 INC] [sock 9] Async send requested 154
2018-06-29 13:54:24.146 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:24.146 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:56584 INC] [sock 9] Async send calledback 154
2018-06-29 13:54:24.146 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:596   Setting 00:00:10 expiry
2018-06-29 13:54:24.146 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:692   handle_write() NOW SENDS: packet=114 B, from  queue size=1
2018-06-29 13:54:24.146 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:657   [176.36.83.XX:56584 INC] [sock 9] Async send calledback 114
2018-06-29 13:54:24.265 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:353   [sock 9] Some not success at read: End of file:2
2018-06-29 13:54:29.356 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:610   [176.36.83.XX:56578 INC] connection timeout, closing
2018-06-29 13:54:29.356 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 8] Socket destroyed
2018-06-29 13:54:29.356 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#0 to 176.36.83.XX
^C2018-06-29 13:54:33.768       [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:898   JOINING all threads - almost
2018-06-29 13:54:33.768 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:900   JOINING all threads - DONE
2018-06-29 13:54:33.768 [SRV_MAIN]      INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:96     net_service loop stopped.
2018-06-29 13:54:33.768 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3011   Stopped wallet RPC server
2018-06-29 13:54:33.768 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3014   Saving wallet...
2018-06-29 13:54:33.768 [SRV_MAIN]      WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3016   Successfully saved
2018-06-29 13:54:33.768 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:100   [sock -1] Socket destroyed without shutdown.
2018-06-29 13:54:33.768 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock -1] Socket destroyed
2018-06-29 13:54:33.768 [SRV_MAIN]      DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#2 to 0.0.0.0
2018-06-29 13:54:33.768 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:100   [sock 9] Socket destroyed without shutdown.
2018-06-29 13:54:33.768 [SRV_MAIN]      TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:104   [sock 9] Socket destroyed
2018-06-29 13:54:33.768 [SRV_MAIN]      DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#1 to 176.36.83.XX
2018-06-29 13:54:33.768 [SRV_MAIN]      DEBUG   device.ledger   src/device/device_ledger.cpp:228        Device 0 Destroyed
root@monero:/mnt/monero#

```

What is wrong?
How to pair mobile wallet with monero node?


# Discussion History
## minzak | 2018-06-29T16:37:48+00:00
решение тут -> https://github.com/monero-project/monero/issues/4082

# Action History
- Created by: minzak | 2018-06-29T13:50:10+00:00
- Closed at: 2018-06-29T16:37:48+00:00
