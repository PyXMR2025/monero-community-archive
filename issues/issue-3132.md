---
title: The 'do_not_relay' flag in /sendrawtransaction daemon RPC method is both undocumented
  AND defaults to 'true'
source_url: https://github.com/monero-project/monero/issues/3132
author: emesik
assignees: []
labels: []
created_at: '2018-01-16T00:53:16+00:00'
updated_at: '2018-01-30T09:48:34+00:00'
type: issue
status: closed
closed_at: '2018-01-30T09:48:34+00:00'
---

# Original Description
This looks weird. When submitting a raw transaction to the daemon, it stays in mempool and isn't relayed further by default. What's worse, the behavior and the flag [aren't documented](https://getmonero.org/resources/developer-guides/daemon-rpc.html#sendrawtransaction).

For starters, I [updated the docs](https://github.com/monero-project/monero-site/pull/556) but I'm still wondering:

1. Why the default value is `true`?
2. What is the purpose of not relaying transactions at all? Do we need it?

# Discussion History
## moneromooo-monero | 2018-01-16T10:27:35+00:00
There is no default value. If you don't give it, it's uninitialized. We can give default values since fairly recently though, I'll do that. Not relaying txes is needed if you want to mine the tx.

## moneromooo-monero | 2018-01-16T11:16:14+00:00
https://github.com/monero-project/monero/pull/3136 should fix it.

## moneromooo-monero | 2018-01-30T09:45:38+00:00
+resolved

# Action History
- Created by: emesik | 2018-01-16T00:53:16+00:00
- Closed at: 2018-01-30T09:48:34+00:00
