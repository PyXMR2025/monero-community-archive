---
title: Missing `on_unconfirmed_money_received` notification when funds sent to same
  account
source_url: https://github.com/monero-project/monero/issues/8377
author: woodser
assignees: []
labels: []
created_at: '2022-06-04T19:35:53+00:00'
updated_at: '2022-06-08T10:44:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently the wallet does not provide a notification when funds are received from within the same account.

This issue requests calling `on_unconfirmed_money_received` when funds are transferred to the same account so listeners are reliably notified of any unconfirmed incoming funds.

Related to https://github.com/monero-project/monero/issues/7035

# Discussion History
# Action History
- Created by: woodser | 2022-06-04T19:35:53+00:00
