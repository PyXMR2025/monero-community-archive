---
title: Fee is not carved out of partial output with split transactions
source_url: https://github.com/monero-project/monero/issues/7337
author: lxop
assignees: []
labels: []
created_at: '2021-01-21T03:36:03+00:00'
updated_at: '2021-09-09T19:07:09+00:00'
type: issue
status: closed
closed_at: '2021-09-09T19:07:09+00:00'
---

# Original Description
When a transfer is split into multiple transactions and one of the addresses is only partially paid in the first transaction, the fee for the first transaction should be carved out of that partial payment (according to the comments on `wallet2::create_transactions_2`). The logic for this behaviour exists, but it is never hit because of the test
```c++
if (inputs < outputs)
{
  LOG_PRINT_L2("We don't have enough for the basic fee, switching to adding_fee");
  adding_fee = true;
  goto skip_tx;
}
```
which is before that logic gets a chance to run and will always be hit if that carving logic would have been used.

The consequence of this bug is that a whole extra input is added to the transaction to pay the fee and the rest of that input value is locked up as change.

NB: I have also observed this behaviour in reality while experimenting with Monero transactions, it is not just my theory about the code :-)

The code that is causing this problem was added in #2989.

Perhaps the solution to this is to perform the "carve it out of the partial payment" logic *before* calling `transfer_selected[_rct]` (and possibly also afterwards, where it currently is)?

# Discussion History
# Action History
- Created by: lxop | 2021-01-21T03:36:03+00:00
- Closed at: 2021-09-09T19:07:09+00:00
