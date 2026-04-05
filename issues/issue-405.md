---
title: 'Proposal: the log level for adding new blocks should be `INFO` instead of
  `DEBUG`'
source_url: https://github.com/Cuprate/cuprate/issues/405
author: Har01d
assignees: []
labels:
- C-proposal
created_at: '2025-03-13T18:26:42+00:00'
updated_at: '2025-05-03T15:57:35+00:00'
type: issue
status: closed
closed_at: '2025-05-03T15:57:35+00:00'
---

# Original Description
Right now when the node is launched, it's not really clear whether it's functioning. Changing `stdout = { level = "info" }` to `debug` yields too much output to `STDOUT`.

```
cuprate@xmr-cuprate:~$ ./cuprated
Using config at: /home/cuprate/Cuprated.toml
2025-03-13T18:11:03.091200Z  INFO init_hardfork_state{chain_height=3367024}: Initializing hard-fork state this may take a while.
2025-03-13T18:11:03.091208Z  INFO init_weight_cache{chain_height=3367024 chain=Main}: Initializing weight cache this may take a while.
2025-03-13T18:11:03.091358Z  INFO init_weight_cache{chain_height=3367024 chain=Main}:get_long_term_weights{range=3267024..3367024 chain=Main}: getting block long term weights.
2025-03-13T18:11:03.091216Z  INFO init_difficulty_cache{chain_height=3367024 chain=Main}: Initializing difficulty cache this may take a while.
2025-03-13T18:11:03.095474Z  INFO init_difficulty_cache{chain_height=3367024 chain=Main}:get_blocks_timestamps{block_heights=3366289..3367024 chain=Main}: Getting blocks timestamps
2025-03-13T18:11:03.157383Z  INFO init_difficulty_cache{chain_height=3367024 chain=Main}: Current chain height: 3367024, accounting for 735 blocks timestamps
2025-03-13T18:11:03.157461Z  INFO init_hardfork_state{chain_height=3367024}: Initialized Hfs, current fork: V16, HFVotes { total: 10080, V1: 10080, V2: 10080, V3: 10080, V4: 10080, V5: 10080, V6: 10080, V7: 10080, V8: 10080, V9: 10080, V10: 10080, V11: 10080, V12: 10080, V13: 10080, V14: 10080, V15: 10080, V16: 10080 }
2025-03-13T18:11:03.157745Z  INFO init_weight_cache{chain_height=3367024 chain=Main}:get_block_weights{range=3366924..3367024 chain=Main}: getting block weights.
2025-03-13T18:11:03.163558Z  INFO init_weight_cache{chain_height=3367024 chain=Main}: Initialized block weight cache, chain-height: 3367024, long term weights length: 100000, short term weights length: 100
2025-03-13T18:11:03.525224Z  INFO Loading peers from file: /home/cuprate/.cache/cuprate/addressbook/ClearNet
2025-03-13T18:11:03.527389Z  INFO Starting outbound connection maintainer, target outbound connections: 64
2025-03-13T18:11:03.527429Z  INFO inbound_server: Starting inbound connection server
2025-03-13T18:11:03.528336Z  INFO Starting blockchain syncer
(end)
```

While we can see the new blocks in the log `grep`ped by `block`:

```
...
2025-03-13T18:23:36.925610Z DEBUG got blockchain context: BlockchainContext { cumulative_difficulty: 432913247583951277, context_to_verify_block: ContextToVerifyBlock { median_wei>
2025-03-13T18:23:36.925663Z DEBUG Preparing block for verification, expected height: 3367031
2025-03-13T18:23:36.943678Z DEBUG verifying block: a5febb73a4f5adf47c0b741f23d3abf4717704b09cc574725fcde26c0a524725
2025-03-13T18:23:36.944219Z DEBUG Verifying block header.
2025-03-13T18:23:36.944271Z DEBUG Updating blockchain cache with new block, height: 3367031
2025-03-13T18:23:36.944292Z DEBUG Accounting for new blocks timestamp (1741890214) and cumulative_difficulty (432913761077076268)
2025-03-13T18:23:36.944311Z DEBUG Adding new block's 3367031 weights to block cache, weight: 130317, long term weight: 176470
2025-03-13T18:23:36.944408Z DEBUG Accounting for new blocks vote, height: 3367031, vote: V16
2025-03-13T18:23:36.950959Z DEBUG queuing block at chain height 3367032 for broadcast
...
```

# Discussion History
# Action History
- Created by: Har01d | 2025-03-13T18:26:42+00:00
- Closed at: 2025-05-03T15:57:35+00:00
