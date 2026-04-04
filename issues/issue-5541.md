---
title: 'Wallet RPC: open_wallet throws non-descriptive error when wallet already open'
source_url: https://github.com/monero-project/monero/issues/5541
author: aaronovz1
assignees: []
labels: []
created_at: '2019-05-12T20:11:53+00:00'
updated_at: '2019-08-27T15:13:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
open_wallet fails if the wallet is already open but the error and error code is non-descriptive. You can't tell if it is a real error or if the wallet is simply already open. I think it would be better to return "Wallet already open" as a warning instead of "Failed to open wallet". That way the error can be safely ignored and further wallet operations can be done.

# Discussion History
## moneromooo-monero | 2019-08-27T15:13:12+00:00
It's a real error. open_wallet does not error out if there is a wallet open.

# Action History
- Created by: aaronovz1 | 2019-05-12T20:11:53+00:00
