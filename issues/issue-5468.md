---
title: Add a monero-wallet-rpc method for getting users' latest transaction info
source_url: https://github.com/monero-project/monero/issues/5468
author: WooKeyWallet
assignees: []
labels: []
created_at: '2019-04-20T02:57:39+00:00'
updated_at: '2019-06-15T17:22:05+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:22:04+00:00'
---

# Original Description
Hi, we are WooKey team, a dev team of Monero wallet. 
By now, to reduce the synchronization time of restoring a wallet, almost all wallets require their users to fill block height or date. However, the user experience in this way is not good.

Could you please provide a PRC method, which is possible to get the date or block height of the lastest transation at a given address. Even if it's not accurate to day, just accurate to month would be enough.

# Discussion History
## moneromooo-monero | 2019-04-20T08:33:28+00:00
Do you mean a wallet RPC, or a daemon RPC ?
If the former, call incoming_transfers, and check the block height field of the last entry you get.
If the latter, then no. The daemon has no access to your secret keys. You want mymonero instead.

## moneromooo-monero | 2019-04-20T08:43:24+00:00
Actually the block height is in prevent in that RPC. https://github.com/monero-project/monero/pull/5470 adds it.

## WooKeyWallet | 2019-04-21T09:20:09+00:00
> Actually the block height is in prevent in that RPC. #5470 adds it.

Thank you for that . We will continue to work on the wallet for monero.

## moneromooo-monero | 2019-06-15T10:40:02+00:00
I'm not sure whether this is invalid or resolved :) I'll choose resolved.

+resolved


# Action History
- Created by: WooKeyWallet | 2019-04-20T02:57:39+00:00
- Closed at: 2019-06-15T17:22:04+00:00
