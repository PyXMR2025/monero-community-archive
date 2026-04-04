---
title: Enhancement request - add freeze/thaw/frozen and set_ring functionality to
  RPC wallet
source_url: https://github.com/monero-project/monero/issues/6669
author: Adreik
assignees: []
labels: []
created_at: '2020-06-20T11:27:30+00:00'
updated_at: '2020-06-20T11:27:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently there exists in the Monero CLI wallet the capability to exclude specific outputs from transactions (freeze/thaw/frozen) and to set specific ring members for outputs.

However, neither functionality exists for the [RPC wallet](https://web.getmonero.org/resources/developer-guides/wallet-rpc.html) according to the documentation. 

Proposal: 

-Add an RPC method that takes a key image/one-time pubkey of an output along with a list of indices of outputs to use as ring members.

-Add frozen/thaw/freeze RPC methods that take the key image/one-time pubkey of an output and return a boolean if it is currently marked as unspendable within the wallet/mark the output as spendable/mark the output as unspendable by the wallet.

# Discussion History
# Action History
- Created by: Adreik | 2020-06-20T11:27:30+00:00
