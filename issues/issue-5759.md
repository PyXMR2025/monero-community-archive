---
title: Where is the doc files about how to use the executable file.
source_url: https://github.com/monero-project/monero/issues/5759
author: ScottGold
assignees: []
labels: []
created_at: '2019-07-17T13:32:47+00:00'
updated_at: '2019-07-18T12:44:54+00:00'
type: issue
status: closed
closed_at: '2019-07-18T12:44:54+00:00'
---

# Original Description
The monero-wallet-rpc need a wallet file, how to generate a wallet file?


# Discussion History
## moneromooo-monero | 2019-07-17T13:55:15+00:00
Either use monero-wallet-cli to create one (--help for the list of command line parameters, "help" while in monero-wallet-cli), or use monero-wallet-rpc (see the list of RPC in https://web.getmonero.org/resources/developer-guides/wallet-rpc.html).

## ScottGold | 2019-07-18T02:59:47+00:00
Thanks for reply.
I'm confusing why monerod and monero-wallet-rpc both listening on the port 18082, and which application will the RPC connect to?

## moneromooo-monero | 2019-07-18T11:05:27+00:00
They should not listen on the same port. They indeed cannot. You connect to the daemon RPC if you want to call a daemon RPC, and to the wallet if you want to call a wallet RPC. Daemon RPC deal with the blockchain, wallet RPC deal with your keys.

## ScottGold | 2019-07-18T12:44:54+00:00
Thanks.

# Action History
- Created by: ScottGold | 2019-07-17T13:32:47+00:00
- Closed at: 2019-07-18T12:44:54+00:00
