---
title: 'monero-wallet-rpc feature request: support multiple "wallets"'
source_url: https://github.com/monero-project/monero/issues/5643
author: lessless
assignees: []
labels: []
created_at: '2019-06-14T22:14:15+00:00'
updated_at: '2019-06-15T06:48:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It will be cool if  monero-wallet-rpc  would be able to scan incoming blocks for  transactions for multiple wallets. 
Reason being is that very I/O heavy to run a `monero-wallet-rpc` instance per each wallet.

RPC API would allow to perform either bulk queries or select a specific wallet, kinda similar to what we have now.

TX notifications would be a bit more difficult to customize, since they are configured statically in config file. My take is that they can inform about all managed wallets. 

# Discussion History
## moneromooo-monero | 2019-06-14T22:17:02+00:00
If you mean account, it does. If you mean top level wallets, it does (not concurrently, but load/save).

## lessless | 2019-06-14T22:20:49+00:00
@moneromooo-monero my bad - I forgot that we have multiple accounts now. This is about top-level wallets. 

P.S.  I updated title to a more precise version. 

# Action History
- Created by: lessless | 2019-06-14T22:14:15+00:00
