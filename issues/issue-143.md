---
title: Wallet stuck with `reorg_depth_error`
source_url: https://github.com/seraphis-migration/monero/issues/143
author: j-berman
assignees: []
labels: []
created_at: '2025-10-07T15:53:25+00:00'
updated_at: '2025-10-15T02:33:19+00:00'
type: issue
status: closed
closed_at: '2025-10-15T02:33:19+00:00'
---

# Original Description
@Rucknium reported in stressnet matrix:

> This error in monero-wallet-rpc appeared a few minutes after wallet creation, while the local node had 0-2 p2p connections. It keeps printing each time a block is found I think:

```
2025-10-07 00:43:49.320 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:3177     !blockchain.is_in_bounds(parsed_blocks_start_idx-1). THROW EXCEPTION: error::reorg_depth_error
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Exception: tools::error::reorg_depth_error
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:135  Unwound call stack:
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [1]  0x113) [0x565305cb7507]:__cxa_throw+0x113) [0x565305cb7507]
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [2] ./monero-wallet-rpc(+0x49818d) [0x565305fce18d] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [3] ./monero-wallet-rpc(+0x3b128e) [0x565305ee728e] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [4] ./monero-wallet-rpc(+0x45ba9b) [0x565305f91a9b] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [5] ./monero-wallet-rpc(+0x21e4ad) [0x565305d544ad] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [6] ./monero-wallet-rpc(+0x225254) [0x565305d5b254] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [7] ./monero-wallet-rpc(+0x20f1be) [0x565305d451be] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [8] ./monero-wallet-rpc(+0x2317fd) [0x565305d677fd] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [9] ./monero-wallet-rpc(+0x251a46) [0x565305d87a46] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [10] ./monero-wallet-rpc(+0x26d14e) [0x565305da314e] 
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [11]  0x1143b) [0x7f706e5c143b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7f706e5c143b]
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [12]  0x8609) [0x7f706d8e0609]:_64-linux-gnu/libpthread.so.0(+0x8609) [0x7f706d8e0609]
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [13]  0x43) [0x7f706d805353]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f706d805353]
2025-10-07 00:43:49.320 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173
2025-10-07 00:43:49.322 [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:239    Exception at while refreshing, what=Daemon's response did not include a block in the local hashchain, we must have exceeded the max reorg depth. The wallet needs to be rescanned manually
```

> Maybe something to do with new reorg code? Is that in this stressnet? There were no deep reorgs around the time that this appeared.
> I created 10 wallets at the same time. seems like it happened to all of them.
> I sent these wallets some XMR from another wallet. I think the tx would have arrived before the messages appeared. I think the funding tx did not arrive in other nodes' txpools until later, due to p2p connectivity issues.
> just in case that's relevant
> ofrnxmr@ofrnxmr:monero.social : Did you create them offline? Or connected to an old daemon?
> Rucknium: No. MWR instances were booted and connected to the local node. Then restore_deterministic_wallet. I set restore height to exactly current height. That could have cut it close, especially if there were short reorgs.



# Discussion History
## j-berman | 2025-10-07T17:24:18+00:00
According to @Rucknium's logs, it looks like this is what happened:

- Created block when chain tip was block n.
- Block n-1 was reorged out.
- Wallet got stuck trying to refresh starting on top of the block hash n-1 that was reorged out.
- Since the wallet has no block hashes saved before that one (except the genesis block), the daemon just kept serving the genesis block.
- The wallet can't handle a reorg from below its restore height, and so got stuck unable to proceed without a rescan.

Potential solution: first time wallet creation should start the refresh from max reorg depth blocks below the restore height.

Relevant wallet RPC logs showing loop on top of block hash `8634417042ccc9948a4312b06a66524cf066d47b7e478bc311dd36b2aa6f367f`:

```
2025-10-07 16:52:05.917 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3338     Refresh will ignore low start_height 0 and proceed to scan contiguously on top of already synced blocks
2025-10-07 16:52:05.917 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:3312     Refresh starting from block 2849698
2025-10-07 16:52:05.917 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3015     Requesting blocks starting on top of block hash <8634417042ccc9948a4312b06a66524cf066d47b7e478bc311dd36b2aa6f367f>, n blocks synced: 2849698, init_tree_sync: 0
2025-10-07 16:52:06.351 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3044     Pulled blocks: blocks_start_height 1, count 1000, height 1001, node height 2849932, top hash <b5fd70e1d3e7e9ab529e87085b66f90e4630038db7ce053c9a1f7e5eedf63242>, pool info 1
...<pool txs>...
2025-10-07 16:52:06.362 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:3177     !blockchain.is_in_bounds(parsed_blocks_start_idx-1). THROW EXCEPTION: error::reorg_depth_error
2025-10-07 16:52:06.362 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:1014 /home/user/Rucknium/git/fcmp++-stressnet/monero-gui-repo/monero/src/wallet/wallet2.cpp:3177:N5tools5error17reorg_depth_errorE: Daemon's response did not include a block in the local hashchain, we must have exceeded the max reorg depth. The wallet needs to be rescanned manually
2025-10-07 16:52:06.362 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Exception: tools::error::reorg_depth_error
2025-10-07 16:52:06.362 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:135  Unwound call stack:
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [1]  0x113) [0x55fa08501507]:__cxa_throw+0x113) [0x55fa08501507]
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [2] ./monero-wallet-rpc(+0x49818d) [0x55fa0881818d] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [3] ./monero-wallet-rpc(+0x3b128e) [0x55fa0873128e] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [4] ./monero-wallet-rpc(+0x45ba9b) [0x55fa087dba9b] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [5] ./monero-wallet-rpc(+0x21e4ad) [0x55fa0859e4ad] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [6] ./monero-wallet-rpc(+0x225254) [0x55fa085a5254] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [7] ./monero-wallet-rpc(+0x20f1be) [0x55fa0858f1be] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [8] ./monero-wallet-rpc(+0x2317fd) [0x55fa085b17fd] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [9] ./monero-wallet-rpc(+0x251a46) [0x55fa085d1a46] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [10] ./monero-wallet-rpc(+0x26d14e) [0x55fa085ed14e] 
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [11]  0x1143b) [0x7f569f82343b]:_64-linux-gnu/libboost_thread.so.1.71.0(+0x1143b) [0x7f569f82343b]
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [12]  0x8609) [0x7f569eb42609]:_64-linux-gnu/libpthread.so.0(+0x8609) [0x7f569eb42609]
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173      [13]  0x43) [0x7f569ea67353]:_64-linux-gnu/libc.so.6(clone+0x43) [0x7f569ea67353]
2025-10-07 16:52:06.363 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:173
2025-10-07 16:52:06.365 [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:239    Exception at while refreshing, what=Daemon's response did not include a block in the local hashchain, we must have exceeded the max reorg depth. The wallet needs to be rescanned manually
```

Relevant daemon output from `alt_chain_info` showing that block hash `8634417042ccc9948a4312b06a66524cf066d47b7e478bc311dd36b2aa6f367f` was reorged out:

```
2 blocks long, from height 2849696 (237 deep), diff 1132889113525: 8634417042ccc9948a4312b06a66524cf066d47b7e478bc311dd36b2aa6f367f
```

EDIT: corrected to explain the actual cause.

## j-berman | 2025-10-08T03:10:58+00:00
Correction: looks like this bug was only possible when the reorg was 2 blocks or more, and reorged out the restore height's **prev** block as well, which is consistent with @Rucknium's observed event.

## j-berman | 2025-10-15T02:33:19+00:00
Fixed in #144 

# Action History
- Created by: j-berman | 2025-10-07T15:53:25+00:00
- Closed at: 2025-10-15T02:33:19+00:00
