---
title: Add 'all_accounts' parameter to wallet rpc 'get_address' and 'incoming_transfers'
source_url: https://github.com/monero-project/monero/issues/5362
author: woodser
assignees: []
labels: []
created_at: '2019-03-28T19:11:43+00:00'
updated_at: '2019-04-02T23:31:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue requests the addition of the `all_accounts` parameter in wallet rpc `get_address` and `incoming_transfers` similar to `get_balance` and `get_transfers` (pr #5150).  Otherwise, a client must make one request per account to each of these endpoints in order to collect information across all accounts.  This becomes expensive as the number of accounts grows and especially if the requests are non-local.

Related to #5109.

# Discussion History
## jtgrassie | 2019-04-02T23:10:41+00:00
You mean like PR's #5154 and #5156 right? Also, is there a need for changing `incoming_transfers` given that `get_transfers` already get's incoming transfers too?

## woodser | 2019-04-02T23:31:08+00:00
Right.  As I understand it, `incoming_transfers` returns the key image, spent status, and index of incoming outputs.  These fields are not returned from `get_transfers`.

# Action History
- Created by: woodser | 2019-03-28T19:11:43+00:00
