---
title: Failed to send funds to another address via RPC
source_url: https://github.com/monero-project/monero/issues/3869
author: i3bitcoin
assignees: []
labels: []
created_at: '2018-05-27T08:11:53+00:00'
updated_at: '2018-06-05T18:24:57+00:00'
type: issue
status: closed
closed_at: '2018-06-05T18:24:57+00:00'
---

# Original Description
I'm getting this error while trying to send funds to another address.
Any suggesions how can it be fixed?

[RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:6233     !real_out_found. THROW EXCEPTION: error::wallet_internal_error

[RPC0]  WARN    net.http        src/wallet/wallet_errors.h:794  /root/monero/src/wallet/wallet2.cpp:6233:N5tools5error21wallet_internal_errorE: Daemon response did not include the requested real output

# Discussion History
## moneromooo-monero | 2018-05-27T08:28:09+00:00
Run both daemon and wallet with --log-level 2, and post the logs to fpaste.org or pastebin.mozilla.org or paste.debian.net. The wallet log will contain some private info (but not your secret keys), so you may want to set a password on fpaste.org and PM it to me on Freenode (moneromooo).
Also post the commit hash of the code you are running and the RPC command and parameters you are using.

## moneromooo-monero | 2018-05-30T14:06:04+00:00
Fixed in https://github.com/monero-project/monero/pull/3882

## dEBRUYNE-1 | 2018-06-05T18:17:01+00:00
+resolved

# Action History
- Created by: i3bitcoin | 2018-05-27T08:11:53+00:00
- Closed at: 2018-06-05T18:24:57+00:00
