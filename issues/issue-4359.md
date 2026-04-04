---
title: '`wallet2::import_multisig` doesn''t signal about error if refresh failed'
source_url: https://github.com/monero-project/monero/issues/4359
author: naughtyfox
assignees: []
labels: []
created_at: '2018-09-10T15:54:11+00:00'
updated_at: '2018-09-21T19:16:58+00:00'
type: issue
status: closed
closed_at: '2018-09-21T19:16:58+00:00'
---

# Original Description
We encountered the following bug - if refresh error happens like wallet disconnected from daemon when  multisig wallets exchange with multisig key images `wallet2::import_multisig` function does not indicate that operation is failed. Client code cannot determine if operation has been successful. This happens because sync exception just captured and wasn't propogated to the calling code (https://github.com/monero-project/monero/blob/fad88e18a9795b377676ad6f63c1772868e0d761/src/wallet/wallet2.cpp#L10881).

This kind of error occurs especially often on mobile devices where connectivity may be not stable.

# Discussion History
## moneromooo-monero | 2018-09-21T19:11:42+00:00
+resolved

# Action History
- Created by: naughtyfox | 2018-09-10T15:54:11+00:00
- Closed at: 2018-09-21T19:16:58+00:00
