---
title: Add `relayed` parameter to daemon RPC get_transactions and wallet RPC get_transfers
source_url: https://github.com/monero-project/monero/issues/5137
author: woodser
assignees: []
labels: []
created_at: '2019-02-11T14:13:23+00:00'
updated_at: '2019-03-13T12:06:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently `relayed` is not returned for daemon RPC's get_transactions or wallet RPC's get_transfers, so the client must make an additional call (e.g. to daemon RPC get_transactions_pool) in order to to know if unconfirmed transactions are relayed.  This issue requests the relayed field be added to these two RPC calls.

# Discussion History
## moneromooo-monero | 2019-03-13T11:47:30+00:00
It's a daemon thing, so it makes no sense for the wallet.
For the daemon... I'm not sure. It's a pool specific thing, so it you start asking for that you'll probably also ask for all pool related things like relayed time, whether it was asked to be relayed or not, whether it was popped from a block, etc. While I'm not 100% sure about this yet, I tend to think no.

## moneromooo-monero | 2019-03-13T11:49:26+00:00
Do you have a good use for this ? Note that "relayed" is not necessarily correct. There is no check whether a peer has actually received it, just whether it was sent, errors or not.

## moneromooo-monero | 2019-03-13T12:06:49+00:00
https://github.com/moneromooo-monero/bitmonero/tree/rpcre, not sure whether to PR it.


# Action History
- Created by: woodser | 2019-02-11T14:13:23+00:00
