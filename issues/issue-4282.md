---
title: 'make_multisig error via monero-wallet-rpc: ''empty view keys'''
source_url: https://github.com/monero-project/monero/issues/4282
author: sneurlax
assignees: []
labels: []
created_at: '2018-08-19T23:34:38+00:00'
updated_at: '2018-08-20T05:11:35+00:00'
type: issue
status: closed
closed_at: '2018-08-20T05:06:58+00:00'
---

# Original Description
When using `make_multisig` via JSON-RPC (`monero-wallet-rpc`,) error code `-1` (`"empty view keys"`) is thrown.

To reproduce, create two wallets, `A` and `B`.  Open `A` and issue `prepare_multisig`.  Save the `multisig_info` that is produced.  Repeat for `B`.  Use `make_multisig` on `A` using the `multisig_info` from `B`.  Error `error: { code: -1, message: 'empty view keys' }` will be given.

Reproducible via `curl` as follows:

Open wallet `A`
```bash
curl -X POST http://localhost:28083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"open_wallet","params":{"filename":"testnet_multisig_wallet_2-2_a"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
}
```

Prepare multisig on wallet `A`
```bash
curl -X POST http://localhost:28083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"prepare_multisig","params":{}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "multisig_info": "MultisigV1PzEEyXkePUxKAKR7zmquxufstTxHf5UNyGyztd26dAtb2RWJH6NE7wRADpVaUCUxoq8hCTvTyT9ipZU25SXc8Php7j863hyDJ9VPuGz4dqRHx5J2sFKPfkXpijijwGbUnAJnDjgL3Fphskp3ZQioYt8pJShfobUBf7wkVJUvjuAM4wTx"
  }
}
```

Open wallet `B`
```bash
curl -X POST http:/localhost:28083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"open_wallet","params":{"filename":"testnet_multisig_wallet_2-2_b"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
}
```

Make multisig on wallet `B`
```bash
user@user:~/github/monerojs$  curl -X POST http:/localhost:28083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"make_multisig","params":{"multisig_info":"MultisigV1PzEEyXkePUxKAKR7zmquxufstTxHf5UNyGyztd26dAtb2RWJH6NE7wRADpVaUCUxoq8hCTvTyT9ipZU25SXc8Php7j863hyDJ9VPuGz4dqRHx5J2sFKPfkXpijijwGbUnAJnDjgL3Fphskp3ZQioYt8pJShfobUBf7wkVJUvjuAM4wTx"}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -1,
    "message": "empty view keys"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

Log level 4 of `monero-wallet-rpc` shown below:

```bash
Monero$ 0.12.3.0/monero-wallet-rpc --rpc-bind-port=28083 --testnet --disable-rpc-login --wallet-dir="/Monero/wallets" --log-level=4
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.
 
Monero 'Lithium Luna' (v0.12.3.0-release)
2018-08-19 16:10:49.420     7f1e928a5bc0        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:196  Setting log level = 4
2018-08-19 16:10:49.420     7f1e928a5bc0        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:199  Logging to: 0.12.3.0/monero-wallet-rpc.log
Logging to 0.12.3.0/monero-wallet-rpc.log
2018-08-19 16:10:49.420     7f1e928a5bc0        DEBUG   device.ledger   src/device/device_ledger.cpp:225        Device 0 Created
2018-08-19 16:10:49.421     7f1e928a5bc0        INFO    wallet.wallet2  src/wallet/wallet2.cpp:5552     ringdb path set to /home/user/.shared-ringdb/testnet
2018-08-19 16:10:49.443     7f1e928a5bc0        DEBUG   net.http        src/common/util.cpp:697 Address 'http://localhost:28081' is local
2018-08-19 16:10:49.443     7f1e928a5bc0        INFO    wallet.rpc      src/wallet/wallet_rpc_server.cpp:161    Daemon is local, assuming trusted
2018-08-19 16:10:49.443     7f1e928a5bc0        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:910   Set server type to: 1 from name: RPC, prefix_name = RPC
2018-08-19 16:10:49.443     7f1e928a5bc0        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:28083
2018-08-19 16:10:49.443     7f1e928a5bc0        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:839   start accept
2018-08-19 16:10:49.443     7f1e928a5bc0        DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
2018-08-19 16:10:49.444     7f1e928a5bc0        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:92    test, connection constructor set m_connection_type=1
2018-08-19 16:10:49.444     7f1e928a5bc0        DEBUG   net     contrib/epee/include/net/net_helper.h:512       Problems at cancel: Bad file descriptor
2018-08-19 16:10:49.444     7f1e928a5bc0        DEBUG   net     contrib/epee/include/net/net_helper.h:515       Problems at shutdown: Bad file descriptor
2018-08-19 16:10:49.444     7f1e928a5bc0        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3009   Starting wallet RPC server
2018-08-19 16:10:49.444     7f1e928a5bc0        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:89     Run net_service loop( 1 threads)...
2018-08-19 16:10:49.444 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:935   Run server thread name: RPC
2018-08-19 16:10:49.444 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:942   JOINING all threads
2018-08-19 16:10:52.452 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1032  handle_accept
2018-08-19 16:10:52.452 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1038  New server for RPC connections
2018-08-19 16:10:52.452 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:765   set m_connection_type = RPC
2018-08-19 16:10:52.452 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:163       Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2018-08-19 16:10:52.452 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:92    test, connection constructor set m_connection_type=1                   
2018-08-19 16:10:52.452 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:160   [sock 7] new connection from 127.0.0.1:56612 INC to 127.0.0.1:28083, total sockets objects 2                                                                                                                                                           
2018-08-19 16:10:52.452 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:616   New connection from host 127.0.0.1: 0                                   
2018-08-19 16:10:52.452 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:52.452 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:284    connection type RPC 127.0.0.1:28083 <--> 127.0.0.1:56612
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 258897 (last time 4.67977e-310)                                                                                                                                                                           
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~201b  (from 201 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [201 0 0 0 0 0 0 0 0 0 ]                                                                                                           
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 258897 (last time 0)     
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~201b  (from 201 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [201 0 0 0 0 0 0 0 0 0 ]                                                                                                               
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 49                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:52.454 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 109                                                                                                                                                             
Content-Type: text/plain                                                                                                                                                       
Last-Modified: Sun, 19 Aug 2018 16:10:52 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 0 < 258897 (last time 0)     
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~154b  (from 154 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [154 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:52.454 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=154 B
2018-08-19 16:10:52.454 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:52.454 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~109b  (from 109 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [263 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:52.454 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=109 B, is added to queue-size=2
2018-08-19 16:10:52.454 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 154
2018-08-19 16:10:52.454 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:52.454 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 154               
2018-08-19 16:10:52.454 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:52.454 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=109 B, from  queue size=1
2018-08-19 16:10:52.454 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 109
2018-08-19 16:10:52.461 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~201b  (from 201 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [402 0 0 0 0 0 0 0 0 0 ]                                                                                                           
2018-08-19 16:10:52.461 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~201b  (from 201 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [402 0 0 0 0 0 0 0 0 0 ]                                                                                                               
2018-08-19 16:10:52.461 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 49                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:52.461 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:52.462 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 109                                                                                                                                                             
Content-Type: text/plain                                                                                                                                                       
Last-Modified: Sun, 19 Aug 2018 16:10:52 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:52.462 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~154b  (from 154 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [417 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:52.462 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=154 B
2018-08-19 16:10:52.462 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:52.462 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~109b  (from 109 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [526 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:52.462 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=109 B, is added to queue-size=2
2018-08-19 16:10:52.462 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 154
2018-08-19 16:10:52.462 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:52.462 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 154               
2018-08-19 16:10:52.462 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:52.462 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=109 B, from  queue size=1
2018-08-19 16:10:52.462 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 109
2018-08-19 16:10:52.513 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~279b  (from 279 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [681 0 0 0 0 0 0 0 0 0 ]                                                                                                           
2018-08-19 16:10:52.513 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~279b  (from 279 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [681 0 0 0 0 0 0 0 0 0 ]                                                                                                               
2018-08-19 16:10:52.513 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 126                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:52.513 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'asa' is shorter than its prefix length, 4
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'ave' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'boa' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'cal' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'dar' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'don' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'dos' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'eco' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'eje' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'fax' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'feo' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'fin' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'gen' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'gol' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'haz' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'ira' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'luz' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'mar' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'mes' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.514 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'mil' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'oca' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'ojo' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'ola' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'oro' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'oso' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'pan' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'pez' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'pie' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'red' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'res' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.515 [RPC0]  WARN    default src/mnemonics/language_base.h:102       Español word 'rey' is shorter than its prefix length, 4                                 
2018-08-19 16:10:52.520 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5552     ringdb path set to /home/user/.shared-ringdb/testnet
2018-08-19 16:10:52.541 [RPC0]  DEBUG   net.http        contrib/epee/include/net/http_client.h:365      Reconnecting...
2018-08-19 16:10:52.542 [RPC0]  TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 226
2018-08-19 16:10:52.542 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)                             
2018-08-19 16:10:53.077 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:128      /json_rpc[create_wallet] processed with 0/565/0ms
2018-08-19 16:10:53.077 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 59                                                                                                                                                             
Content-Type: application/json                                                                                                                                                 
Last-Modified: Sun, 19 Aug 2018 16:10:53 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:53.077 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~159b  (from 159 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [685 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:53.077 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=159 B
2018-08-19 16:10:53.077 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:53.077 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~59b  (from 59 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [744 0 0 0 0 0 0 0 0 0 ]                                                                                                           
2018-08-19 16:10:53.077 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=59 B, is added to queue-size=2
2018-08-19 16:10:53.077 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 159
2018-08-19 16:10:53.078 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.078 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 159               
2018-08-19 16:10:53.078 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.078 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=59 B, from  queue size=1
2018-08-19 16:10:53.078 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 59
2018-08-19 16:10:53.121 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~256b  (from 256 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [937 0 0 0 0 0 0 0 0 0 ]                                                                                                           
2018-08-19 16:10:53.121 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~256b  (from 256 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [937 0 0 0 0 0 0 0 0 0 ]                                                                                                               
2018-08-19 16:10:53.121 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 103                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:53.121 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:53.122 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5552     ringdb path set to /home/user/.shared-ringdb/testnet
2018-08-19 16:10:53.158 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:3783     Loaded wallet keys file, with public address: 9t7MG3zDahZJefr7NdZpoQXtjmeeadahsZS2YijfJESP42w6sw7zGRE5jpAsQW5eGSizJ4JUyQz7uF2nT2L7SJXNJ5ZZd3H                                                                                                                           
2018-08-19 16:10:53.159 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:3802     Trying to decrypt cache data
2018-08-19 16:10:53.198 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:5660     Finding and saving rings...
2018-08-19 16:10:53.198 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:5672     Found 0 transactions                                                                   
2018-08-19 16:10:53.215 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5717     Found and saved rings for 0 transactions
2018-08-19 16:10:53.216 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:129      /json_rpc[open_wallet] processed with 0/95/0ms
2018-08-19 16:10:53.216 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 59                                                                                                                                                             
Content-Type: application/json                                                                                                                                                 
Last-Modified: Sun, 19 Aug 2018 16:10:53 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:53.216 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~159b  (from 159 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [903 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:53.216 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=159 B
2018-08-19 16:10:53.216 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:53.216 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~59b  (from 59 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [962 0 0 0 0 0 0 0 0 0 ]                                                                                                           
2018-08-19 16:10:53.216 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=59 B, is added to queue-size=2
2018-08-19 16:10:53.216 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 159
2018-08-19 16:10:53.216 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.216 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 159               
2018-08-19 16:10:53.216 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.216 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=59 B, from  queue size=1
2018-08-19 16:10:53.216 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 59
2018-08-19 16:10:53.261 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~206b  (from 206 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [1143 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:53.261 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~206b  (from 206 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [1143 0 0 0 0 0 0 0 0 0 ]                                                                                                             
2018-08-19 16:10:53.261 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 54                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:53.261 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:53.261 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:131      /json_rpc[prepare_multisig] processed with 0/0/0ms                             
2018-08-19 16:10:53.262 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 270                                                                                                                                                             
Content-Type: application/json                                                                                                                                                 
Last-Modified: Sun, 19 Aug 2018 16:10:53 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:53.262 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~160b  (from 160 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [1122 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:53.262 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=160 B
2018-08-19 16:10:53.262 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:53.262 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~270b  (from 270 b) Speed AVG=   1[w=1]    1[w=1] /  Limit=16 KiB/sec  [1392 0 0 0 0 0 0 0 0 0 ]                                                                                                         
2018-08-19 16:10:53.262 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=270 B, is added to queue-size=2
2018-08-19 16:10:53.262 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 160
2018-08-19 16:10:53.262 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.262 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 160               
2018-08-19 16:10:53.262 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.262 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=270 B, from  queue size=1
2018-08-19 16:10:53.262 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 270
2018-08-19 16:10:53.309 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 258897 < 258898 (last time 258898)                                                                                                                                                                           
2018-08-19 16:10:53.309 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~279b  (from 279 b) Speed AVG=   1[w=1]    1[w=1] /  Limit=16 KiB/sec  [279 1143 0 0 0 0 0 0 0 0 ]                                                                                                       
2018-08-19 16:10:53.309 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 258897 < 258898 (last time 258898)                                                                                                                                                                           
2018-08-19 16:10:53.309 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~279b  (from 279 b) Speed AVG=   1[w=1]    1[w=1] /  Limit=16 KiB/sec  [279 1143 0 0 0 0 0 0 0 0 ]                                                                                                           
2018-08-19 16:10:53.309 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 126                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:53.309 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:53.309 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5552     ringdb path set to /home/user/.shared-ringdb/testnet
2018-08-19 16:10:53.330 [RPC0]  DEBUG   net.http        contrib/epee/include/net/http_client.h:365      Reconnecting...
2018-08-19 16:10:53.330 [RPC0]  TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 226
2018-08-19 16:10:53.330 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_client.h:758      http_stream_filter::parse_cached_header(*)                             
2018-08-19 16:10:53.964 [RPC0]  DEBUG   net     contrib/epee/include/net/net_helper.h:512       Problems at cancel: Bad file descriptor
2018-08-19 16:10:53.964 [RPC0]  DEBUG   net     contrib/epee/include/net/net_helper.h:515       Problems at shutdown: Bad file descriptor                                       
2018-08-19 16:10:53.965 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:128      /json_rpc[create_wallet] processed with 0/655/0ms                               
2018-08-19 16:10:53.965 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 59                                                                                                                                                             
Content-Type: application/json                                                                                                                                                 
Last-Modified: Sun, 19 Aug 2018 16:10:53 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:53.965 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:183        Moving counter buffer by 1 second 258897 < 258898 (last time 258898)                                                                                                                                                                           
2018-08-19 16:10:53.965 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~159b  (from 159 b) Speed AVG=   0[w=1.51]    0[w=1.51] /  Limit=16 KiB/sec  [159 1392 0 0 0 0 0 0 0 0 ]                                                                                                 
2018-08-19 16:10:53.965 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=159 B
2018-08-19 16:10:53.965 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:53.965 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~59b  (from 59 b) Speed AVG=   1[w=1.511]    1[w=1.511] /  Limit=16 KiB/sec  [218 1392 0 0 0 0 0 0 0 0 ]                                                                                                 
2018-08-19 16:10:53.965 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=59 B, is added to queue-size=2
2018-08-19 16:10:53.965 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 159
2018-08-19 16:10:53.965 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.965 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 159               
2018-08-19 16:10:53.965 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:53.965 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=59 B, from  queue size=1
2018-08-19 16:10:53.965 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 59
2018-08-19 16:10:54.009 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~256b  (from 256 b) Speed AVG=   0[w=1.556]    0[w=1.556] /  Limit=16 KiB/sec  [535 1143 0 0 0 0 0 0 0 0 ]                                                                                               
2018-08-19 16:10:54.009 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~256b  (from 256 b) Speed AVG=   0[w=1.556]    0[w=1.556] /  Limit=16 KiB/sec  [535 1143 0 0 0 0 0 0 0 0 ]                                                                                                   
2018-08-19 16:10:54.009 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 103                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:54.009 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:54.009 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5552     ringdb path set to /home/user/.shared-ringdb/testnet
2018-08-19 16:10:54.051 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:3783     Loaded wallet keys file, with public address: 9yTmmdtnAaHgWxfRugaKKY9M1hqLxeMbAfNtkEWqf5bMGRFk5tVHuCbTHTXRWSr4hVajpVcoLf3ZwQWk1ZeeKk8QVe9H4rU                                                                                                                           
2018-08-19 16:10:54.051 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:3802     Trying to decrypt cache data
2018-08-19 16:10:54.098 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:5660     Finding and saving rings...
2018-08-19 16:10:54.098 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:5672     Found 0 transactions                                                                   
2018-08-19 16:10:54.118 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5717     Found and saved rings for 0 transactions
2018-08-19 16:10:54.119 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:129      /json_rpc[open_wallet] processed with 0/110/0ms
2018-08-19 16:10:54.119 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 59                                                                                                                                                             
Content-Type: application/json                                                                                                                                                 
Last-Modified: Sun, 19 Aug 2018 16:10:54 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:54.119 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~159b  (from 159 b) Speed AVG=   0[w=1.665]    0[w=1.665] /  Limit=16 KiB/sec  [377 1392 0 0 0 0 0 0 0 0 ]                                                                                               
2018-08-19 16:10:54.119 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=159 B
2018-08-19 16:10:54.119 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:54.119 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~59b  (from 59 b) Speed AVG=   1[w=1.665]    1[w=1.665] /  Limit=16 KiB/sec  [436 1392 0 0 0 0 0 0 0 0 ]                                                                                                 
2018-08-19 16:10:54.119 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=59 B, is added to queue-size=2
2018-08-19 16:10:54.119 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 159
2018-08-19 16:10:54.119 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:54.119 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 159               
2018-08-19 16:10:54.119 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:54.119 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=59 B, from  queue size=1
2018-08-19 16:10:54.120 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 59
2018-08-19 16:10:54.165 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~206b  (from 206 b) Speed AVG=   0[w=1.712]    0[w=1.712] /  Limit=16 KiB/sec  [741 1143 0 0 0 0 0 0 0 0 ]                                                                                               
2018-08-19 16:10:54.166 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~206b  (from 206 b) Speed AVG=   0[w=1.712]    0[w=1.712] /  Limit=16 KiB/sec  [741 1143 0 0 0 0 0 0 0 0 ]                                                                                                   
2018-08-19 16:10:54.166 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 54                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:54.166 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:54.166 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:131      /json_rpc[prepare_multisig] processed with 0/1/0ms                             
2018-08-19 16:10:54.166 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 270                                                                                                                                                             
Content-Type: application/json                                                                                                                                                 
Last-Modified: Sun, 19 Aug 2018 16:10:54 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:54.166 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~160b  (from 160 b) Speed AVG=   1[w=1.712]    1[w=1.712] /  Limit=16 KiB/sec  [596 1392 0 0 0 0 0 0 0 0 ]                                                                                               
2018-08-19 16:10:54.166 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=160 B
2018-08-19 16:10:54.166 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:54.166 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~270b  (from 270 b) Speed AVG=   1[w=1.712]    1[w=1.712] /  Limit=16 KiB/sec  [866 1392 0 0 0 0 0 0 0 0 ]                                                                                               
2018-08-19 16:10:54.166 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=270 B, is added to queue-size=2
2018-08-19 16:10:54.166 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 160
2018-08-19 16:10:54.166 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:54.166 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 160               
2018-08-19 16:10:54.166 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry                                                 
2018-08-19 16:10:54.166 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=270 B, from  queue size=1
2018-08-19 16:10:54.166 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 270
2018-08-19 16:10:54.209 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_in: packet of ~434b  (from 434 b) Speed AVG=   1[w=1.756]    1[w=1.756] /  Limit=16 KiB/sec  [1175 1143 0 0 0 0 0 0 0 0 ]                                                                                               
2018-08-19 16:10:54.209 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle <<< global-IN: packet of ~434b  (from 434 b) Speed AVG=   1[w=1.756]    1[w=1.756] /  Limit=16 KiB/sec  [1175 1143 0 0 0 0 0 0 0 0 ]                                                                                                   
2018-08-19 16:10:54.209 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:402  HTTP HEAD:                                                     
host: 127.0.0.1:28083                                                                                                                                                           
accept: application/json                                                                                                                                                       
content-type: application/json                                                                                                                                                 
content-length: 281                                                                                                                                                             
Connection: keep-alive                                                                                                                                                         
 
 
2018-08-19 16:10:54.209 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:66       HTTP [127.0.0.1] POST /json_rpc
2018-08-19 16:10:54.209 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:3295     empty view keys
2018-08-19 16:10:54.215 [RPC0]  TRACE   net.http        contrib/epee/include/net/http_protocol_handler.inl:580  HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok                                                                                                                                                                 
Server: Epee-based                                                                                                                                                             
Content-Length: 109                                                                                                                                                             
Content-Type: text/plain                                                                                                                                                       
Last-Modified: Sun, 19 Aug 2018 16:10:54 GMT                                                                                                                                   
Accept-Ranges: bytes                                                                                                                                                           
 
 
2018-08-19 16:10:54.215 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~154b  (from 154 b) Speed AVG=   1[w=1.761]    1[w=1.761] /  Limit=16 KiB/sec  [1020 1392 0 0 0 0 0 0 0 0 ]                                                                                             
2018-08-19 16:10:54.215 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:561   do_send_chunk() NOW SENSD: packet=154 B
2018-08-19 16:10:54.215 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:54.215 [RPC0]  TRACE   net.throttle    contrib/epee/src/network_throttle-detail.cpp:218        Throttle throttle_speed_out: packet of ~109b  (from 109 b) Speed AVG=   1[w=1.761]    1[w=1.761] /  Limit=16 KiB/sec  [1129 1392 0 0 0 0 0 0 0 0 ]
2018-08-19 16:10:54.215 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:546   do_send_chunk() NOW just queues: packet=109 B, is added to queue-size=2
2018-08-19 16:10:54.215 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:549   [127.0.0.1:56612 INC] [sock 7] Async send requested 154
2018-08-19 16:10:54.215 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:54.215 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 154
2018-08-19 16:10:54.215 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:630   Setting 00:30:00 expiry
2018-08-19 16:10:54.215 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:740   handle_write() NOW SENDS: packet=109 B, from  queue size=1
2018-08-19 16:10:54.215 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:705   [127.0.0.1:56612 INC] [sock 7] Async send calledback 109
2018-08-19 16:10:54.261 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:358   [sock 7] Some not success at read: End of file:2
2018-08-19 16:10:54.261 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:366   [sock 7] peer closed connection
2018-08-19 16:10:54.261 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:618   Closed connection from host 127.0.0.1: 1
2018-08-19 16:10:54.261 [RPC0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:105   [sock 7] Socket destroyed
2018-08-19 16:10:54.261 [RPC0]  DEBUG   net.p2p contrib/epee/src/connection_basic.cpp:171       Destructing connection p2p#0 to 0.0.0.0
```

# Discussion History
## stoffu | 2018-08-20T04:52:24+00:00
The `multisig_info` parameter is supposed to be an array, so you had to wrap the multisig info around with brackets. Also, you need to specify the `threshold` parameter which is 2 in this case:

    curl -X POST http:/localhost:28083/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"make_multisig","params":{"multisig_info":["MultisigV1PzEEyXkePUxKAKR7zmquxufstTxHf5UNyGyztd26dAtb2RWJH6NE7wRADpVaUCUxoq8hCTvTyT9ipZU25SXc8Php7j863hyDJ9VPuGz4dqRHx5J2sFKPfkXpijijwGbUnAJnDjgL3Fphskp3ZQioYt8pJShfobUBf7wkVJUvjuAM4wTx"],"threshold":2}}' -H 'Content-Type: application/json'


## sneurlax | 2018-08-20T05:03:25+00:00
re: threshold, fair enough, but I added the curl later and let that mistake slip in.  For reference, this is the actual method I'm using (from monerojs; updated to reflect new type):

```js
  /**
   * Make a multisig account
   *
   * @function make_multisig
   * @param {number} threshold - Threshold required to spend from multisig
   * @param {array} multisig_info - Array of multisignature information strings (from eg. prepare_multisig) 
   * @param {string} password - Passphrase to apply to multisig address
   *
   * @returns {object} - Example: {
   *   address: '9xXa4CtQsHqaTBoAvZLgZAXjKkzQnXR5tTVtp6P6NwAj2hokhkDd8NmSyLZN95wXqGcpo2wS92KeRBxDQaikNzPJ9nujoUB',
   *   multisig_info: ''
   * }
   */
  make_multisig(threshold, multisig_info, password = undefined) {
    let params = {
      threshold: threshold,
      multisig_info: multisig_info,
      password: password
    };

    return this._run('make_multisig', params);
  }
```

I didn't know that the multisig_info param was a string array, though, so I'll try that.  First attempts give `-1` `Bad multisig info: ...` but I'll bash away at it awhile

## sneurlax | 2018-08-20T05:06:58+00:00
The array type was absolutely the issue.  Thanks @stoffu!

# Action History
- Created by: sneurlax | 2018-08-19T23:34:38+00:00
- Closed at: 2018-08-20T05:06:58+00:00
