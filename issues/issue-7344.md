---
title: describe_transfer has incorrect output when multiple transactions are present
source_url: https://github.com/monero-project/monero/issues/7344
author: lxop
assignees: []
labels: []
created_at: '2021-01-22T03:06:29+00:00'
updated_at: '2021-08-02T22:47:36+00:00'
type: issue
status: closed
closed_at: '2021-08-02T22:47:36+00:00'
---

# Original Description
When `transfer_split` is used on a view-only wallet, it produces an unsigned transaction set. As implied by the term "set", this can comprise multiple transactions; this can occur when the required inputs mean that a single transaction would be too large. (Once #7322 is merged, it will also occur if more than 15 outputs are specified).

If this transaction set is inspected with `describe_transfer`, the response will contain multiple lists of recipients (one list per transaction) but the lists are incorrect. Specifically, the first list will correctly show the recipients from the first transaction, but the second list will contain the recipients from both the first and the second transactions, the third list contains recipients from the first, second, and third transactions, and so forth: each list contains the aggregated outputs from all transactions so far instead of just its own.

# Discussion History
# Action History
- Created by: lxop | 2021-01-22T03:06:29+00:00
- Closed at: 2021-08-02T22:47:36+00:00
