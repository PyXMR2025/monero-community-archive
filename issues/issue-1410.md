---
title: show_transfers via JSON-RPC
source_url: https://github.com/monero-project/monero/issues/1410
author: gituser
assignees: []
labels: []
created_at: '2016-12-06T08:44:00+00:00'
updated_at: '2016-12-15T20:39:53+00:00'
type: issue
status: closed
closed_at: '2016-12-15T20:39:53+00:00'
---

# Original Description
Hello.

There is already show_transfers command in cli to show all possible transfers.

But for JSON-RPC there is only incoming_transfers functionality which show incoming transfers only.

Is it possible to add show_transfers or outgoing_transfers for JSON-RPC as well (show_transfers would be better as it displays payment_id as well as txid).

Thank you.

# Discussion History
## moneromooo-monero | 2016-12-06T19:31:42+00:00
Use get_transfers. Set misc booleans to true for what you're interested in (in, out, pending, etc)

## moneromooo-monero | 2016-12-06T19:33:55+00:00
And the payment id is incldued.

## gituser | 2016-12-15T20:39:53+00:00
thanks, closing this.

# Action History
- Created by: gituser | 2016-12-06T08:44:00+00:00
- Closed at: 2016-12-15T20:39:53+00:00
