---
title: When using transfer_split and a payment id, the get_bulk_payments will not
  find it
source_url: https://github.com/monero-project/monero/issues/126
author: ianchildress
assignees: []
labels: []
created_at: '2014-09-10T22:33:41+00:00'
updated_at: '2014-09-10T22:40:09+00:00'
type: issue
status: closed
closed_at: '2014-09-10T22:40:09+00:00'
---

# Original Description
I have tested this sending to my own account and it may only be an issue when sending to your own account.

When you send payments using transfer_split and reference a payment id, the get_bulk_payments will not find the payment using that payment id. 

However, using the same command syntax and variables if I change from transfer_split to just transfer it works fine and I can use get_bulk_payments to find the payment id payment.


# Discussion History
# Action History
- Created by: ianchildress | 2014-09-10T22:33:41+00:00
- Closed at: 2014-09-10T22:40:09+00:00
