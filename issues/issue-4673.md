---
title: 'wallet-rpc: Write subaddresses to wallet file instantly when created'
source_url: https://github.com/monero-project/monero/issues/4673
author: ghost
assignees: []
labels:
- invalid
created_at: '2018-10-20T11:28:32+00:00'
updated_at: '2018-11-07T14:41:16+00:00'
type: issue
status: closed
closed_at: '2018-11-07T14:41:16+00:00'
---

# Original Description
Wallet-rpc does not write sub-addresses to file instantly. instead, it saves them when it 'cleanly' exits.

In a production environment which we keep the rpc daemon for months there is a possibility of it failing. When it fails the unsaved sub-addresses will be lost and has to be created manually by restoring the wallet through wallet-cli. Creating 6000 sub-addresses takes hours and we can't check the payment. It's a nightmare.

#3994 Monero locks the wallet file as of v0.13 and I think it can save sub-addresses every time at creation.

# Discussion History
## moneromooo-monero | 2018-10-20T17:24:48+00:00
You can save the wallet yourself with the "store" RPC. Saving can take quite a while for large wallets, so I don't think auto saving every time is a good idea.

At some point, we might end up with a LMDB based wallet cache, which would "autosave" everything instantly. However, this is a large amount of work so no indication of when this will be done yet.


## moneromooo-monero | 2018-11-07T14:21:03+00:00
Since this would take quite a long time saving all the time, I'll close this.

+invalid

# Action History
- Created by: ghost | 2018-10-20T11:28:32+00:00
- Closed at: 2018-11-07T14:41:16+00:00
