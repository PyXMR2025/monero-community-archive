---
title: 'monero-wallet-rpc: Add account_index parameter to query_key API'
source_url: https://github.com/monero-project/monero/issues/3864
author: mmorrell
assignees: []
labels: []
created_at: '2018-05-26T03:01:57+00:00'
updated_at: '2018-05-28T03:57:46+00:00'
type: issue
status: closed
closed_at: '2018-05-28T03:57:46+00:00'
---

# Original Description
Currently the "query_key" API only returns the mnemonic/viewkey/spendkey of the main account (account index 0).

I think there would be value in adding a parameter for "account_index" so that you can query the keys of subaccounts, if this is possible.


# Discussion History
## stoffu | 2018-05-26T05:43:26+00:00
That does not any make sense. All subaddresses are derived solely from the original view/spend keys and the index. Finding money transfers to subaddresses is handled by the wallet internal code. There is absolutely no need to present secret keys corresponding to subaddresses to the user.

# Action History
- Created by: mmorrell | 2018-05-26T03:01:57+00:00
- Closed at: 2018-05-28T03:57:46+00:00
