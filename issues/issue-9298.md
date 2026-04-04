---
title: Support getting unconfirmed transfers from monero-wallet-rpc without fetching
  from pool
source_url: https://github.com/monero-project/monero/issues/9298
author: woodser
assignees: []
labels:
- feature
- proposal
- discussion
created_at: '2024-04-21T10:43:46+00:00'
updated_at: '2024-04-25T05:53:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently monero-wallet-rpc supports [getting transfers](https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#get_transfers) with the `pool` option to return unconfirmed transfers in the pool.

However, this option will always [update the pool state from the daemon](https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/wallet/wallet_rpc_server.cpp#L2681) to get the latest pool transfers.

There is no way to get unconfirmed transfers already known to be in the pool without fetching the latest pool state, which is unnecessary if the wallet is already regularly syncing from the pool, and the extra request can be problematic with mainnet nodes rejecting too many requests from too many client wallets.

This issue requests being able to get transfers already known to be in the pool without fetching the latest pool state from monerod.

# Discussion History
# Action History
- Created by: woodser | 2024-04-21T10:43:46+00:00
