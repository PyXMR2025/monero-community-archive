---
title: 'monerod: crash while synchronizing with the network'
source_url: https://github.com/monero-project/monero/issues/2521
author: ghost
assignees: []
labels:
- duplicate
created_at: '2017-09-24T10:41:10+00:00'
updated_at: '2017-09-26T10:16:07+00:00'
type: issue
status: closed
closed_at: '2017-09-24T13:48:19+00:00'
---

# Original Description
Console output before crash:

> 2017-09-23 22:57:18.274 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [164.132.166.19:18080 OUT] Sync data returned a new top block candidate: 1358593 -> 1405674 [Your node is 47081 blocks (65 days) behind]
> SYNCHRONIZATION started
> 
> Thread 13 "monerod" received signal SIGSEGV, Segmentation fault.

This happens both with official build (https://getmonero.org/downloads/#linux) and native debug build of  "release-v0.11.0.0" branch (make debug).
I tested official build on Tails (3.1) and Ubuntu (16.04.3 LTS) and native build on Ubuntu (gcc version 5.4.0).
Everytime I start monerod I supply the same env (data.mdb, etc) and crash is always reproducible on first block received.
I tried to specify "--block-sync-size" manually in range 1..20 but it doesn't have any impact.

Trace:
```
(gdb) bt
#0  __memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:1525
#1  0x00007ffff7592533 in cryptonote::Blockchain::handle_block_to_main_chain
      (this=this@entry=0x3460600, bl=..., id=..., bvc=...) 
      at src/cryptonote_core/blockchain.cpp:3334
#2  0x00007ffff7598340 in cryptonote::Blockchain::add_new_block 
      (this=this@entry=0x3460600, bl_=..., bvc=...) 
      at src/cryptonote_core/blockchain.cpp:3481
```
(see below full trace)
```
(gdb) frame 1
#1  0x00007ffff7592533 in cryptonote::Blockchain::handle_block_to_main_chain
      (this=this@entry=0x3460600, bl=...,  id=..., bvc=...) 
      at src/cryptonote_core/blockchain.cpp:3334
3334          if (memcmp(&m_blocks_txs_check[tx_index++], &tx_id, sizeof(tx_id)) != 0)

(gdb) p tx_index 
$1 = 1

(gdb) p m_blocks_txs_check
$8 = std::vector of length 0, capacity 0
```
So it **seems** like uninitialized std::vector `m_blocks_txs_check`

Full trace: 
[crash.log](https://github.com/monero-project/monero/files/1327211/crash.log)

Feel free to ask for missing details.

# Discussion History
## moneromooo-monero | 2017-09-24T13:42:18+00:00
Fixed in https://github.com/monero-project/monero/pull/2492

+duplicate

## ghost | 2017-09-26T10:16:07+00:00
I have built master branch.

Now monerod doesn't crash but sync process stuck on the same point.
I start monerod with "--block-sync-size 1"

Logs are full of stuff like this:

2017-09-26 10:09:24.755 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:722        [212.83.172.165:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-09-26 10:09:24.755 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [212.83.172.165:28080 OUT] COMMAND_HANDSHAKE Failed
2017-09-26 10:09:25.257 [P2P9]  WARN    net.p2p src/p2p/net_node.inl:1594       [212.83.175.67:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-09-26 10:09:26.071 [P2P8]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:305     [207.244.103.152:18080 OUT] Sync data returned a new top block candidate: 1358593 -> 1407453 [Your node is 48860 blocks (67 days) behind] 
SYNCHRONIZATION started
2017-09-26 10:09:30.631 [P2P4]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3401 Block with id: <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42> has at least one transaction (id: <4e9f0f57c64b6caa7fcb2faaee7aabb6fd00ea31a9fb9d7b77d9f34ef56d3c2d>) with wrong inputs.
2017-09-26 10:09:30.632 [P2P4]  ERROR   verify  src/cryptonote_core/blockchain.cpp:3404 Block with id <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42> added as invalid because of wrong inputs in transactions
2017-09-26 10:09:33.878 [P2P9]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = <a2fb4f1f3be520e889d5d92d67b649be5516bf76bf48c4d1370bfdd36cfa3ca1>, height 1358594, parent in alt 0, parent in main 0 (parent <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42>, current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)
2017-09-26 10:09:38.998 [P2P4]  WARN    net.p2p src/p2p/net_node.inl:743        [50.53.99.93:18080 OUT] COMMAND_HANDSHAKE invoked, but process_payload_sync_data returned false, dropping connection.
2017-09-26 10:09:38.999 [P2P0]  WARN    net.p2p src/p2p/net_node.inl:771        [50.53.99.93:18080 OUT] COMMAND_HANDSHAKE Failed
2017-09-26 10:09:42.488 [P2P8]  ERROR   verify  src/cryptonote_core/blockchain.cpp:1437 Block recognized as orphaned and rejected, id = <a2fb4f1f3be520e889d5d92d67b649be5516bf76bf48c4d1370bfdd36cfa3ca1>, height 1358594, parent in alt 0, parent in main 0 (parent <bda3c7ca528bf0bfe263da52e35590e213b713267d1e12f1df623baa50e54e42>, current top <28c9c916402d888d5ee8fb019b8f25386dca5f8ba8c1f5775e6e80fc0b474c61>, chain height 1358593)
2017-09-26 10:09:44.788 [P2P6]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [176.9.2.145:8180 OUT] Got block with unknown parent which was not requested - querying block hashes
2017-09-26 10:09:47.245 [P2P4]  ERROR   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1021    [91.213.203.48:18080 OUT] Got block with unknown parent which was not requested - querying block hashes

# Action History
- Created by: ghost | 2017-09-24T10:41:10+00:00
- Closed at: 2017-09-24T13:48:19+00:00
