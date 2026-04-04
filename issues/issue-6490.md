---
title: transfer command return very large data？
source_url: https://github.com/monero-project/monero/issues/6490
author: GongSuiLi
assignees: []
labels: []
created_at: '2020-04-30T06:14:16+00:00'
updated_at: '2022-02-19T04:34:34+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:34:34+00:00'
---

# Original Description
When my program uses the command to call the Monero so file and transfer 0.0001 Monero, the unsigned transaction data returned is particularly large, even 16Mb. I tried to transfer xmr with different amounts, the size of the transaction data returned is still 16Mb, what is the reason?

# Discussion History
## moneromooo-monero | 2020-04-30T14:32:34+00:00
Since you say "unsigned", you're using the cold/hot wallet system, right ? If so, the transfer files also include new output data (from hot wallet to cold wallet) and key images (from cold wallet to hot wallet). If you make another payment, the file should be smaller as it's already transfered most output data.

# Action History
- Created by: GongSuiLi | 2020-04-30T06:14:16+00:00
- Closed at: 2022-02-19T04:34:34+00:00
