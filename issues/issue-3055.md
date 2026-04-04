---
title: are you interested in stracktrace entries from  "bitmonero.log" file ?
source_url: https://github.com/monero-project/monero/issues/3055
author: aotto1968
assignees: []
labels:
- invalid
created_at: '2018-01-03T17:23:47+00:00'
updated_at: '2018-01-03T18:56:26+00:00'
type: issue
status: closed
closed_at: '2018-01-03T18:56:26+00:00'
---

# Original Description
hi,

  I have a couple of …

```
2018-01-03 16:56:08.972 [P2P9]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:494  LMDB Mapsize increased.  Old: 47572MiB, New: 48596MiB
2018-01-03 16:56:09.394 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:120  Exception: cryptonote::OUTPUT_DNE
2018-01-03 16:56:09.394 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:121  Unwound call stack:
2018-01-03 16:56:09.398 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [1] /home/dev1usr/monero-gui-v0.11.1.0/monerod:__wrap___cxa_throw+0x102 [0x8914e
2018-01-03 16:56:09.398 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [2] /home/dev1usr/monero-gui-v0.11.1.0/monerod() [0x7c8044]
2018-01-03 16:56:09.398 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [3] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::BlockchainLMDB::get_o
2018-01-03 16:56:09.398 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [4] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::Blockchain::check_tx_
2018-01-03 16:56:09.398 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [5] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::Blockchain::check_tx_
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [6] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::Blockchain::check_tx_
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [7] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::tx_memory_pool::add_t
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [8] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::core::add_new_tx(cryp
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [9] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::core::handle_incoming
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [10] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::core::handle_incomin
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [11] /home/dev1usr/monero-gui-v0.11.1.0/monerod:cryptonote::t_cryptonote_protoco
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [12] /home/dev1usr/monero-gui-v0.11.1.0/monerod:int epee::net_utils::buff_to_t_a
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [13] /home/dev1usr/monero-gui-v0.11.1.0/monerod:int cryptonote::t_cryptonote_pro
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [14] /home/dev1usr/monero-gui-v0.11.1.0/monerod:int nodetool::node_server<crypto
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [15] /home/dev1usr/monero-gui-v0.11.1.0/monerod:nodetool::node_server<cryptonote
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [16] /home/dev1usr/monero-gui-v0.11.1.0/monerod:epee::levin::async_protocol_hand
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [17] /home/dev1usr/monero-gui-v0.11.1.0/monerod:epee::net_utils::connection<epee
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [18] /home/dev1usr/monero-gui-v0.11.1.0/monerod:void boost::asio::detail::strand
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [19] /home/dev1usr/monero-gui-v0.11.1.0/monerod:boost::asio::detail::completion_
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [20] /home/dev1usr/monero-gui-v0.11.1.0/monerod:void boost::asio::detail::strand
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [21] /home/dev1usr/monero-gui-v0.11.1.0/monerod:boost::asio::detail::reactive_so
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [22] /home/dev1usr/monero-gui-v0.11.1.0/monerod:boost::asio::detail::epoll_react
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [23] /home/dev1usr/monero-gui-v0.11.1.0/monerod:epee::net_utils::boosted_tcp_ser
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [24] /home/dev1usr/monero-gui-v0.11.1.0/monerod() [0x988fa5]
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [25] /lib64/libpthread.so.0+0x8744 [0x7efebc233744]
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159      [26] /lib64/libc.so.6:clone+0x6d [0x7efebbf71aad]
2018-01-03 16:56:09.399 [P2P3]  INFO    stacktrace      src/common/stack_trace.cpp:159
2018-01-03 16:56:09.399 [P2P9]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:578  [batch] DB resize needed
2018-01-03 16:56:09.401 [P2P9]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:494  LMDB Mapsize increased.  Old: 48596MiB, New: 49620MiB

```

# Discussion History
## moneromooo-monero | 2018-01-03T18:52:52+00:00
It's not clear whether this one's expected. It's from the txpool, so it may be that the tx was invalid in the first place (referencing an output which does not exist). There are cases where it's expected. So not enough information to tell whether OK or not, but it's probably OK if it went on its way after that. Closing, but thanks for letting us know.

+invalid


# Action History
- Created by: aotto1968 | 2018-01-03T17:23:47+00:00
- Closed at: 2018-01-03T18:56:26+00:00
