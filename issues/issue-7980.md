---
title: transfer and transfer_split lack the option to subtract the fee from the transfer
  amount
source_url: https://github.com/monero-project/monero/issues/7980
author: LocalMonero
assignees: []
labels: []
created_at: '2021-09-28T22:15:00+00:00'
updated_at: '2024-02-24T18:03:05+00:00'
type: issue
status: closed
closed_at: '2024-02-24T18:03:05+00:00'
---

# Original Description
It is relatively common practice for the payment processing industry specifically and business in general for the recipient of a transfer to cover the fees. Recipients are often businesses, and customers hate whenever the final price that they need to pay is more than the price shown (because the payment would be price + transfer fee).

In cryptocurrency, this would mean the customer sending the transfer with the "subtract fee from transfer amount" option enabled. Bitcoin, after all, has the "subtractfeefrom" option when sending a transfer, precisely for this purpose.

Currently, the only way one can send a transfer with the fee deducted from the transfer amount is through using the sweep commands.

The normal transfer command should include an option that allows you to deduct the fee from the transferred amount automatically.

# Discussion History
# Action History
- Created by: LocalMonero | 2021-09-28T22:15:00+00:00
- Closed at: 2024-02-24T18:03:05+00:00
