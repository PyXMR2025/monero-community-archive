---
title: Monero-wallet-rpc keeps crashing
source_url: https://github.com/monero-project/monero/issues/2068
author: analogic
assignees: []
labels: []
created_at: '2017-06-02T18:51:22+00:00'
updated_at: '2017-06-04T18:40:32+00:00'
type: issue
status: closed
closed_at: '2017-06-04T18:40:32+00:00'
---

# Original Description
I've installed new version after old version just stop working (due hard fork I guess). 

Monero-wallet-rpc loads pruned blocks after couple hours, then it works for some time and fails. Next start is same - load from block 1267523, works for some time and then fall.

Log:
```
...
2017-06-02 17:26:29.223 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:527   [66.66.66.66:43392 INC] [sock 15] Async send requested 395
2017-06-02 17:26:29.223 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:601   [66.66.66.66:43392 INC] [sock 15] Async send calledback 395
2017-06-02 17:26:29.224 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:634   handle_write() NOW SENDS: packet=98 B, from  queue size=1
2017-06-02 17:26:29.224 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:601   [66.66.66.66:43392 INC] [sock 15] Async send calledback 98
2017-06-02 17:26:29.225 [RPC0]  TRACE   net.throttle    src/p2p/network_throttle-detail.cpp:224 Throttle throttle_speed_in: packet of ~437b  (from 437 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [558 0 0 0 0 0 0 0 0 0 ]
2017-06-02 17:26:29.225 [RPC0]  TRACE   net.throttle    src/p2p/network_throttle-detail.cpp:224 Throttle <<< global-IN: packet of ~447488b  (from 447488 b) Speed AVG= 876[w=9.875]  876[w=9.875] /  Limit=16 KiB/sec  [571392 0 0 0 0 7633920 1105920 0 0 0 ]
2017-06-02 17:26:29.225 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:62       HTTP [66.66.66.66] POST /json_rpc
2017-06-02 17:26:29.225 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:68       /json_rpc[getheight] processed with 0/0/0ms
2017-06-02 17:26:29.225 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:547  HTTP_RESPONSE_HEAD: <<

HTTP/1.1 200 Ok

Server: Epee-based

Content-Length: 80

Content-Type: application/json

Last-Modified: Fri, 02 Jun 2017 17:26:29 GMT

Accept-Ranges: bytes




2017-06-02 17:26:29.225 [RPC0]  TRACE   net.throttle    src/p2p/network_throttle-detail.cpp:224 Throttle throttle_speed_out: packet of ~159b  (from 159 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [652 0 0 0 0 0 0 0 0 0 ]
2017-06-02 17:26:29.225 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:539   do_send() NOW SENSD: packet=159 B
2017-06-02 17:26:29.225 [RPC0]  TRACE   net.throttle    src/p2p/network_throttle-detail.cpp:224 Throttle throttle_speed_out: packet of ~80b  (from 80 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [732 0 0 0 0 0 0 0 0 0 ]
2017-06-02 17:26:29.225 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:524   do_send() NOW just queues: packet=80 B, is added to queue-size=2
./run: line 6:  1784 Segmentation fault      (core dumped) /usr/bin/monero-wallet-rpc --rpc-bind-port 18082 --wallet-file /data/wallet.bin --rpc-bind-ip 0.0.0.0 --confirm-external-bind --rpc-login 'monerorpc:***' --log-level 4 --trusted-daemon
```

I don't have core dump yet due wrong kernel setting, will have to wait to next dump.

It is last release version, ubuntu, running in docker.

# Discussion History
## analogic | 2017-06-04T18:40:32+00:00
It somewhat solved itself. Closing for now

# Action History
- Created by: analogic | 2017-06-02T18:51:22+00:00
- Closed at: 2017-06-04T18:40:32+00:00
