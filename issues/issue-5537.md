---
title: exception when signing offline transactions
source_url: https://github.com/monero-project/monero/issues/5537
author: JustHereToHelp
assignees: []
labels: []
created_at: '2019-05-10T23:50:53+00:00'
updated_at: '2019-06-15T17:20:20+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:20:20+00:00'
---

# Original Description
I have no idea what's going on.

I'm on 14.0.0.2, and this worked the last time I did it back in November

ERROR	wallet.wallet2	src/wallet/wallet2.cpp:571	*status != CORE_RPC_STATUS_OK. THROW EXCEPTION: tools::error::wallet_generic_rpc_error



# Discussion History
## moneromooo-monero | 2019-05-11T00:04:49+00:00
This is because you're not running a daemon on that machine. You should not have to, but this is a bug in 0.14.0.2, which is fixed in master (there will be a release soon including the fix).

## moneromooo-monero | 2019-06-15T10:34:45+00:00
+resolved

# Action History
- Created by: JustHereToHelp | 2019-05-10T23:50:53+00:00
- Closed at: 2019-06-15T17:20:20+00:00
