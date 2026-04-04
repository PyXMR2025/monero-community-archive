---
title: Get change amount from 0 conf transactions
source_url: https://github.com/monero-project/monero/issues/9636
author: woodser
assignees: []
labels:
- wallet
created_at: '2024-12-21T13:10:46+00:00'
updated_at: '2025-01-05T11:37:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue requests getting the change amount from transactions with 0 confirmations, if possible, even if funds were sent back to self.

Knowing the change amount will allow clients to accurately know their balance + expected incoming funds.

# Discussion History
## jeffro256 | 2024-12-27T19:58:24+00:00
On which API(s)? JSON-RPC? `wallet2` function? `wallet2` listeners?

## woodser | 2024-12-27T19:59:55+00:00
Yeah monero-wallet-rpc.

## jeffro256 | 2025-01-05T08:33:40+00:00
Which method?

## woodser | 2025-01-05T11:37:35+00:00
`get_transfers` and `get_transfer_by_txid`

# Action History
- Created by: woodser | 2024-12-21T13:10:46+00:00
