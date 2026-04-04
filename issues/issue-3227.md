---
title: 'request: add function monero-wallet-rpc::close_wallet() [+1]'
source_url: https://github.com/monero-project/monero/issues/3227
author: DavidBruchmann
assignees: []
labels: []
created_at: '2018-02-02T20:26:46+00:00'
updated_at: '2018-09-11T09:16:59+00:00'
type: issue
status: closed
closed_at: '2018-09-11T09:16:59+00:00'
---

# Original Description
The function close_wallet() would be appreciated as it enables the possibility still to work with the rpc-daemon without risking to manipulate any wallet without intention or getting wrong results.
Furthermore the function open_wallet() shouldn't work as long as there is still one wallet open IMHO, but that's a minor issue.

The function stop_wallet() is shutting the rpc-daemon completely down, that's not desired always, so close_wallet() still would add a small functional layer.

EDIT:
IMHO it's quite uncommon that authentication is done by an RPC-daemon.
Surely it has to offer a method but it seems the wallet-RPC-daemon was just concepted for a single wallet, daemons usually offer to serve several accounts and just offer the methods to connect to those. Also connection to the daemon could be done by several clients where surely not everyone is working with the same wallet. While adding the desired function closeWallet() it's also desired that the requirement to open directly a wallet is removed, like this the daemon can just do what daemons usually do: waiting for commands and serving on request.

# Discussion History
## nsbk | 2018-02-26T20:35:51+00:00
+1

## artyomsol | 2018-06-13T13:26:21+00:00
+1

## moneromooo-monero | 2018-09-11T09:15:01+00:00
+resolved

# Action History
- Created by: DavidBruchmann | 2018-02-02T20:26:46+00:00
- Closed at: 2018-09-11T09:16:59+00:00
