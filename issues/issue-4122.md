---
title: monero-wallet-rpc hang when use transfer method
source_url: https://github.com/monero-project/monero/issues/4122
author: DogLi
assignees: []
labels: []
created_at: '2018-07-09T23:01:49+00:00'
updated_at: '2018-07-10T06:39:59+00:00'
type: issue
status: closed
closed_at: '2018-07-10T06:39:30+00:00'
---

# Original Description
version: 0.12.2.0/0.12.3.0
start monerod and monero-wallet-rpc without  `--testnet`

log of 0.12.3.0:

```
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:8115     Using v4 rules
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:8115     Using v5 rules
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7412     transfer: adding 0.100000000000, for a total of 0.100000000000
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7445     Candidate subaddress index for spending: 0
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7500     Starting with 1 non-dust outputs and 0 dust outputs
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7525     checking preferred
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:565      estimated rct tx size for 2 with ring size 7 and 2: 13762 (1024 saved)
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:6751     pick_preferred_rct_inputs: needed_money 0.102389100000
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:6759     We can use 3 alone: 17.474681369999
2018-07-09 23:07:24.644 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:7539     Found preferred rct inputs for rct tx: 3 (17.474681369999)
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7561     done checking preferred
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7575     Start of loop with 1 0
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7576     unused_transfers_indices: 3
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7577     unused_dust_indices:
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7578     dsts size 1, first 0.100000000000
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7579     adding_fee 0, use_rct 1
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7621     Picking output 3, amount 17.474681369999, ki <375009f26720f4f0f38995b6dd631ddce826e6976e4a9ee9ed7cae49ab2ce6ca>
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:565      estimated rct tx size for 1 with ring size 7 and 1: 6887 (512 saved)
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7642     We can fully pay 49vp5crQBoG9xz6Ejj257DMZY6pf9o6R67R7JX5TbdfBLMk41dcpdsqKkSQuPvyqiyFUUrQwKJrMxNw26xfZUy8M7qVYxND for 0.100000000000
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7662     Considering whether to create a tx now, 1 inputs, tx limit 299400
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:565      estimated rct tx size for 1 with ring size 7 and 2: 13197 (544 saved)
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:565      estimated rct tx size for 1 with ring size 7 and 2: 13197 (544 saved)
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7698     Trying to create a tx now, with 1 outputs and 1 inputs
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:8115     Using v5 rules
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:6501     transfer_selected_rct: starting with fee 0.002218450000
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:6502     selected transfers: 3
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:6510     transfer: adding 0.100000000000, for a total of 0.102218450000
2018-07-09 23:07:24.644 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:6550     wanted 0.102218450000, found 17.474681369999, fee 0.002218450000
2018-07-09 23:07:24.645 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:5884     fake_outputs_count: 6
```
Then all rpc requests such as `get_height`, `get_balance` will hang.

# Discussion History
## DogLi | 2018-07-10T06:39:59+00:00
caused by the dns problem

# Action History
- Created by: DogLi | 2018-07-09T23:01:49+00:00
- Closed at: 2018-07-10T06:39:30+00:00
