---
title: '[bug] - Set daemon allows any address'
source_url: https://github.com/monero-project/monero/issues/8316
author: reemuru
assignees: []
labels: []
created_at: '2022-05-06T13:28:53+00:00'
updated_at: '2022-05-29T15:29:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Related to #8314 

Current behavior:
The `set_daemon` wallet rpc command allows setting the daemon to an invalid address without any notification from the rpc response. This in turn results in the wallet rpc staying alive but continuously throwing the "Exception while refreshing, what=no connection to daemon" error message. 

Expected behavior:
Return an error message / code in the http response when there is no daemon running at the address passed.

Steps to replicate
1. Start monerod
2. Connect monero-wallet-rpc and open a wallet
3. Call `set_daemon` with an invalid daemon address

Reference:
https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#set_daemon


# Discussion History
# Action History
- Created by: reemuru | 2022-05-06T13:28:53+00:00
