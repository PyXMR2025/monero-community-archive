---
title: 'Broadcasting Raw Transaction fails with Error: Ringct type 3 is not allowed
  from v11'
source_url: https://github.com/monero-project/monero/issues/5385
author: yawto
assignees: []
labels:
- duplicate
created_at: '2019-04-01T19:45:57+00:00'
updated_at: '2019-04-01T22:09:32+00:00'
type: issue
status: closed
closed_at: '2019-04-01T22:09:32+00:00'
---

# Original Description
I am currently using the v0.14.0.2 releases of Monerod and Monero-Wallet-RPC for offline signing. After upgrading to v0.14.0.2 I started getting transactions rejected by the daemon. The initial error was that the fee was too low. After raising the priority of the transaction to 2 I stopped receiving an error regarding the fee, but the transaction was still rejected by the daemon with the error `Ringct type 3 is not allowed from v11`. Looking at `rct_signatures` in the raw transaction, the type is indeed listed as 3, but I'm not sure where or how that is set, and more importantly, how to change it to the correct type.

Monero-Wallet-RPC is returning the following error:

```{"code":-41,"message":"Failed to submit signed tx: transaction was rejected by daemon"}```

Below are the logs from Monerod:

```2019-04-01 19:02:58.701 [RPC1]  DEBUG   net.http        src/rpc/core_rpc_server.h:78    HTTP [127.0.0.1] GET /sendrawtransaction
2019-04-01 19:02:58.702 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:111   PERF             ----------
2019-04-01 19:02:58.702 [RPC1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2279 transaction with hash 7ed4ac707f14c4c57a48cac6a05b2417c3b87be669a641855609e83033ba9e52 not found in db
2019-04-01 19:02:58.703 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF       11          VERIFY_start
2019-04-01 19:02:58.704 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF       67          VERIFY_line_61
2019-04-01 19:02:58.705 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF     1041          VERIFY_line_61rl_new
2019-04-01 19:02:58.705 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF      503          VERIFY_line_62
2019-04-01 19:02:58.705 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF       33          VERIFY_line_21_22
2019-04-01 19:02:58.706 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF      303            VERIFY_line_24_25_invert
2019-04-01 19:02:58.706 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF      990          VERIFY_line_24_25
2019-04-01 19:02:58.708 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF     1216          VERIFY_line_26_new
2019-04-01 19:02:58.716 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF     8486          VERIFY_step2_check
2019-04-01 19:02:58.716 [RPC1]  INFO    perf    src/common/perf_timer.cpp:140   PERF    13226        VERIFY
2019-04-01 19:02:58.716 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF       13      verRctSemanticsSimple
2019-04-01 19:02:58.716 [RPC1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2279 transaction with hash 7ed4ac707f14c4c57a48cac6a05b2417c3b87be669a641855609e83033ba9e52 not found in db
2019-04-01 19:02:58.716 [RPC1]  DEBUG   blockchain      src/cryptonote_core/blockchain.cpp:3011 Using 0.000000019777/byte fee
2019-04-01 19:02:58.716 [RPC1]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2437 Ringct type 3 is not allowed from v11
2019-04-01 19:02:58.716 [RPC1]  INFO    txpool  src/cryptonote_core/tx_pool.cpp:213     Transaction with id= <7ed4ac707f14c4c57a48cac6a05b2417c3b87be669a641855609e83033ba9e52> has at least one invalid output
2019-04-01 19:02:58.716 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF        0      add_tx
2019-04-01 19:02:58.716 [RPC1]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:960     Transaction verification failed: <7ed4ac707f14c4c57a48cac6a05b2417c3b87be669a641855609e83033ba9e52>
2019-04-01 19:02:58.716 [RPC1]  WARN    daemon.rpc      src/rpc/core_rpc_server.cpp:721 [on_send_raw_tx]: tx verification failed: invalid output
2019-04-01 19:02:58.716 [RPC1]  DEBUG   perf    src/common/perf_timer.cpp:140   PERF       14    on_send_raw_tx
2019-04-01 19:02:58.716 [RPC1]  DEBUG   net.http        src/rpc/core_rpc_server.h:96    /sendrawtransaction processed with 0/15/0ms

Let me know if I can provide any additional information and thanks for your help.

# Discussion History
## moneromooo-monero | 2019-04-01T20:06:42+00:00
Fixed in https://github.com/monero-project/monero/pull/5277


## moneromooo-monero | 2019-04-01T22:04:58+00:00
+duplicate

# Action History
- Created by: yawto | 2019-04-01T19:45:57+00:00
- Closed at: 2019-04-01T22:09:32+00:00
