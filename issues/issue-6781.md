---
title: Wallet Internal Error monero-wallet-gui.AppImage
source_url: https://github.com/monero-project/monero/issues/6781
author: downystreet
assignees: []
labels: []
created_at: '2020-08-26T21:59:10+00:00'
updated_at: '2021-10-06T03:12:54+00:00'
type: issue
status: closed
closed_at: '2021-10-06T03:12:54+00:00'
---

# Original Description
Getting a strange error in the command terminal while the wallet daemon is syncing to the blockchain. Using the monero-wallet-gui.AppImage
Version: monero-gui-v0.16.0.3
OS: CentOS 8

Terminal readout:
2020-08-26 21:46:39.926	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-08-26 21:46:41.105	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2020-08-26 21:51:48.252	W Failed to generate key derivation from tx pubkey, skipping


# Discussion History
## moneromooo-monero | 2020-08-26T23:10:47+00:00
Did it not recover ? This happens if you sync to a daemon which has a lower height than your wallet is at, but the wallet is supposed to cleanup and resync.

## downystreet | 2020-08-27T00:37:09+00:00
Yes it recovered. I didn't know what it was or if it was important.

## moneromooo-monero | 2020-08-27T01:35:55+00:00
It's noisy I guess, but it's handled. I suppose it should be made less noisy then :)

# Action History
- Created by: downystreet | 2020-08-26T21:59:10+00:00
- Closed at: 2021-10-06T03:12:54+00:00
