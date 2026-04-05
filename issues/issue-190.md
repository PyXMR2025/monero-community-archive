---
title: Received levin response but have no invoke handlers
source_url: https://github.com/seraphis-migration/monero/issues/190
author: bobXMR
assignees: []
labels: []
created_at: '2025-10-22T14:11:16+00:00'
updated_at: '2025-10-22T16:14:11+00:00'
type: issue
status: closed
closed_at: '2025-10-22T16:14:11+00:00'
---

# Original Description
I'm seeing this "no invoke handlers" error on the v1.3 release of the FCMP++ and Carrot alpha stressnet software:

<details>
<summary>level 2 logs of error</summary>

```
2025-10-22 04:49:23.456 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:911     Including transaction <0a8702ef134032e3feddc6d8e1ad019f71915f7485edad437069ce35830d7ea3>
2025-10-22 04:49:23.466 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:911     Including transaction <2f8f67f1ba733b21613ae5ab4e5f6b166d130cc90456e6213610731ec8d19ebb>
2025-10-22 04:49:23.475 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:911     Including transaction <28961c5f0e2d809cd543fb0b565fd52d484c1493ff3abfb6b1d46204e3e28be3>
2025-10-22 04:49:23.479 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:911     Including transaction <dce4c836b65eac3a97cdfdfea1c73b59bfbda9ba6663ec34f1f2161af4f2eeee>
2025-10-22 04:49:23.486 [P2P7]  DEBUG   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:560    bulletproof+ clawback: 460
2025-10-22 04:49:23.492 [P2P7]  INFO    perf.txpool     src/common/perf_timer.cpp:120   PERF             ----------
2025-10-22 04:49:23.492 [P2P7]  DEBUG   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:560    bulletproof+ clawback: 460
2025-10-22 04:49:23.506 [P2P7]  INFO    perf.ringct     src/common/perf_timer.cpp:156   PERF     9178      verRctSemanticsSimple
2025-10-22 04:49:23.506 [P2P7]  DEBUG   blockchain      src/cryptonote_core/blockchain.cpp:4042 Using 0.000000019000/byte fee
2025-10-22 04:49:23.507 [P2P7]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3762 Key image already spent in blockchain: f41604b4da66ba43d25be14cf6ac49e29003fd29655808882bf5c0b1222aeb3c
2025-10-22 04:49:23.507 [P2P7]  INFO    perf.blockchain src/common/perf_timer.cpp:156   PERF      379      check_tx_inputs
2025-10-22 04:49:23.507 [P2P7]  INFO    txpool  src/cryptonote_core/tx_pool.cpp:270     tx used wrong inputs, rejected
2025-10-22 04:49:23.507 [P2P7]  INFO    perf.txpool     src/common/perf_timer.cpp:156   PERF    15329    add_tx
2025-10-22 04:49:23.507 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:961     [202.169.99.195:4473 INC] Tx verification failed, dropping connection
2025-10-22 04:49:23.508 [P2P7]  DEBUG   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2822    [202.169.99.195:4473 INC] dropping connection id 6e84d3fd-1353-4f39-8ace-c9cf5259217d (pruning seed 0), score 0, flush_all_spans 0
2025-10-22 04:49:23.511 [P2P7]  INFO    net     contrib/epee/include/storages/levin_abstract_invoke2.h:74       Failed to invoke command 1002 return code -3
2025-10-22 04:49:23.515 [P2P7]  WARNING net.p2p src/p2p/net_node.inl:1281       [202.169.99.195:4473 INC] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2025-10-22 04:49:23.516 [P2P7]  DEBUG   net     contrib/epee/include/net/levin_protocol_handler_async.h:489     [202.169.99.195:4473 INC] LEVIN_PACKET_RECEIVED. [len=1047, flags1, r?=, cmd = 2006, v=1
2025-10-22 04:49:23.516 [P2P7]  INFO    net.p2p.traffic contrib/epee/include/net/levin_protocol_handler_async.h:56      [202.169.99.195:4473 INC] 1047 bytes received for category command-2006 initiated by peer
2025-10-22 04:49:23.517 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1807    [202.169.99.195:4473 INC] Received NOTIFY_REQUEST_CHAIN (32 blocks
2025-10-22 04:49:23.517 [P2P7]  INFO    net.p2p.msg     src/cryptonote_protocol/cryptonote_protocol_handler.inl:1830    [202.169.99.195:4473 INC] -->>NOTIFY_RESPONSE_CHAIN_ENTRY: m_start_height=2859853, m_total_height=2859855, m_block_ids.size()=2
2025-10-22 04:49:23.517 [P2P7]  DEBUG   cn.block_queue  src/cryptonote_protocol/cryptonote_protocol_handler.h:227       [202.169.99.195:4473 INC] post N10cryptonote27NOTIFY_RESPONSE_CHAIN_ENTRYE -->
2025-10-22 04:49:23.518 [P2P7]  DEBUG   net     contrib/epee/include/net/levin_protocol_handler_async.h:489     [202.169.99.195:4473 INC] LEVIN_PACKET_RECEIVED. [len=172, flags2, r?=, cmd = 1002, v=1
2025-10-22 04:49:23.518 [P2P7]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:513     Received levin response but have no invoke handlers
2025-10-22 04:49:23.521 [P2P7]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:2896    [202.169.99.195:4473 INC] [0] state: closed in state normal
2025-10-22 04:49:23.525 [P2P7]  INFO    net.p2p src/p2p/net_node.inl:2717       [202.169.99.195:4473 6e84d3fd-1353-4f39-8ace-c9cf5259217d INC] CLOSE CONNECTION
2025-10-22 04:49:23.529 [P2P7]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:177       Destructing connection #5552 to 0.0.0.0
```
</details>

# Discussion History
## j-berman | 2025-10-22T16:14:11+00:00
Looks like because the connection was destroyed from the "Key image already spent in blockchain" error (expected from #141), while asynchronously handling COMMAND_TIMED_SYNC, it doesn't add an invoke handler (connection is already destroyed [here](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/contrib/epee/include/net/levin_protocol_handler_async.h#L758-L759), and so it doesn't get added [here](https://github.com/seraphis-migration/monero/blob/dbf9ff3110aa3aaec160442620fcb18edb99cf3f/contrib/epee/include/net/levin_protocol_handler_async.h#L607-L630)). Thus, it sees the "have no invoke handlers" error handling that last packet.

So all looks "expected" to me.

# Action History
- Created by: bobXMR | 2025-10-22T14:11:16+00:00
- Closed at: 2025-10-22T16:14:11+00:00
