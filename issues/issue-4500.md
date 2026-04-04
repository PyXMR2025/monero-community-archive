---
title: 'Bug: Receive page lags or hangs for large wallets'
source_url: https://github.com/monero-project/monero-gui/issues/4500
author: sneurlax
assignees: []
labels: []
created_at: '2025-09-04T18:54:34+00:00'
updated_at: '2025-09-04T18:54:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Opening a wallet with many subaddresses causes severe lag and impact usability.

To reproduce the issue, create a wallet with many addresses in monero-wallet-cli.  For example, using:
```
address mnew 1000
```
30+ times in monero-wallet-cli will create a wallet with 30,001 addresses (like a very active BTCPay wallet).  With this many addresses, the app will lag on a performant PC.

# Discussion History
# Action History
- Created by: sneurlax | 2025-09-04T18:54:34+00:00
