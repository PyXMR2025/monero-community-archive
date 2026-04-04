---
title: monero-wallet-cli show_transfer command does not show the actual number of
  confirmations
source_url: https://github.com/monero-project/monero/issues/8667
author: imfiesh
assignees: []
labels: []
created_at: '2022-12-05T00:05:32+00:00'
updated_at: '2022-12-05T00:05:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```show_transfer``` subtracts 10 (the spendable age) from (current block height - tx height) and then claims that is the number of confirmations, which it's obviously not. Compare with the reference documentation for monero-wallet-rpc which defines _confirmations_ as _Number of block mined since the block containing this transaction_, which I think is in line with how most people use the word, especially if they come from other cryptocurrencies. It's confusing.

Version: 0.18.1.0

# Discussion History
# Action History
- Created by: imfiesh | 2022-12-05T00:05:32+00:00
