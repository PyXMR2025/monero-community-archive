---
title: 'devguides: stop_wallet description needs clarification'
source_url: https://github.com/monero-project/monero-site/issues/2093
author: dimalinux
assignees: []
labels:
- '📚 docs: dev guides'
created_at: '2022-10-30T23:01:25+00:00'
updated_at: '2022-12-01T07:14:25+00:00'
type: issue
status: closed
closed_at: '2022-12-01T07:14:25+00:00'
---

# Original Description
In the monero [wallet RPC documentation](https://github.com/monero-project/monero-site/blame/0d05edf78e2e1b41d36c905f967168b2d98d6561/resources/developer-guides/wallet-rpc.md#L1336-L1338):

The description of `close_wallet` is:
> Close the currently opened wallet, after trying to save it.

The description of  `stop_wallet` is:
> Stops the wallet, storing the current state.

Since the user can open and close different wallets on a single `monero-wallet-rpc` instance (and may not even have an open wallet on a running instance), they don't understand the difference between these two methods. I would change the wording of `stop_wallet` to:
> Store the current state of any open wallet and exit the `monero-wallet-rpc` process. 

# Discussion History
## plowsof | 2022-11-01T11:24:04+00:00
Thank you ( i've ctrl+f'd for exit many times .. i end up using the pid file to stop it )

# Action History
- Created by: dimalinux | 2022-10-30T23:01:25+00:00
- Closed at: 2022-12-01T07:14:25+00:00
