---
title: Improper closing of Levin streams on failure
source_url: https://github.com/monero-project/monero/issues/4813
author: svegaxmr
assignees: []
labels: []
created_at: '2018-11-06T21:26:05+00:00'
updated_at: '2019-08-27T15:54:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Triggered by sending an incorrect genesis block on initial full chain sync (minor = 1 instead of 0). Connection exits without any warning on requesting side. Provider side appears to try to send LEVIN_ERROR_CONNECTION_DESTROYED (-3), but closes the connection before sending that. Trace is
```
2018-11-06 15:02:38.399 [P2P0]  ERROR   net.p2p src/cryptonote_core/blockchain.cpp:1858 Client sent wrong NOTIFY_REQUEST_CHAIN: genesis block mismatch:
id: <48ca7cd3c8de5b6a4d53d2861fbdaedca141553559f9be9520068053cda8430b>,
expected: <418015bb9ae982a1975da7d79277c2705727a56894ba0fb246adaabb1f4632e3>,
 dropping connection
2018-11-06 15:02:38.399 [P2P0]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:3076 BlockchainLMDB::block_txn_abort
2018-11-06 15:02:38.399 [P2P0]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1252    [127.0.0.1:57602 INC] Failed to handle NOTIFY_REQUEST_CHAIN.
2018-11-06 15:02:38.399 [P2P0]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1736    [127.0.0.1:57602 INC] dropping connection id dfc7ad47-8e2b-7781-c508-2eaa50bd3409, add_fail 0, flush_all_spans 0
2018-11-06 15:02:38.400 [P2P0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:618   Closed connection from host 127.0.0.1: 1
2018-11-06 15:02:38.400 [P2P0]  INFO    net     contrib/epee/include/storages/levin_abstract_invoke2.h:122      Failed to invoke command 1007 return code -3
2018-11-06 15:02:38.400 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:1642       [127.0.0.1:57602 INC] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2018-11-06 15:02:38.401 [P2P0]  TRACE   net     contrib/epee/include/net/levin_protocol_handler_async.h:312     [127.0.0.1:57602 INC] [levin_protocol] <<-- finish_outer_call
2018-11-06 15:02:38.401 [P2P0]  TRACE   net     contrib/epee/include/net/abstract_tcp_server2.inl:245   [127.0.0.1:57602 INC] [sock 1608] release
2018-11-06 15:02:38.402 [P2P4]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:260   [127.0.0.1:57602 INC] fired_callback
2018-11-06 15:02:38.402 [P2P4]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:99      [127.0.0.1:57602 INC] callback fired
```
This happens in other places as well, which I am unable to trigger connecting to my local testing node. I will set up a remote node of my own in a few days and be able to provide more information on unexpected disconnects after connection when that happens.

# Discussion History
## moneromooo-monero | 2019-08-27T15:54:57+00:00
Could be fixed by https://github.com/monero-project/monero/pull/5824

# Action History
- Created by: svegaxmr | 2018-11-06T21:26:05+00:00
