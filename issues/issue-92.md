---
title: Add ability to create wallets through rpcwallet
source_url: https://github.com/monero-project/monero/issues/92
author: Jojatekok
assignees: []
labels: []
created_at: '2014-08-10T16:28:51+00:00'
updated_at: '2017-04-24T08:42:35+00:00'
type: issue
status: closed
closed_at: '2017-04-24T08:42:35+00:00'
---

# Original Description
No description

# Discussion History
## hyc | 2017-04-01T21:13:18+00:00
I may work on this. I suggest:
monero-wallet-rpc takes a commandline arg "--wallet-dir" to specify where newly created wallets will live.

createwallet RPC takes 3 params - simple filename, seed language, and password.

This probably also means we should have an RPC to return the list of supported seed languages.

This also would seem to require TLS if talking to a remote wallet.

# Action History
- Created by: Jojatekok | 2014-08-10T16:28:51+00:00
- Closed at: 2017-04-24T08:42:35+00:00
