---
title: Corrupted wallet when insufficient address lookahead on offline wallet
source_url: https://github.com/monero-project/monero/issues/8729
author: nxs-crypto
assignees: []
labels: []
created_at: '2023-02-03T13:34:48+00:00'
updated_at: '2023-02-03T13:34:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Running two monero instances with view-only wallet with offline signer setup on Monero on v0.18.1.1

The signing wallet first encountered the issue 
```
given output pubkey doesn't seem to belong to this address
```

Before contacting monero dev team, tried to do a full output sync, which failed with
```
Failed to generate key image
```

@moneromooo-monero suggested the signing wallets address lookahead wasn't sufficient, and this was verified by using `create_address` rpc to compare offset relative to view-only wallet.

After importing more addresses to signing wallet, signing still failed with 
```
now gettin m_tx.vout.size() <= m_internal_output_index. THROW EXCEPTION: error::wallet_internal_error
19:03 Failed to sign unsigned tx: Too few outputs, outputs may be corrupted
```

So the wallet cache was currupted.

We moved wallet cache and tried a fresh output sync, which failed with same error. 

The final the winning steps to fix issue 
1. Shutdown signing wallet
1. Move wallet cache file (/wallets/a -> /wallets/a_back)
1. Start signing wallet
1. Call `create_address` in a loop enough enough addresses generated to match view-only wallet
1. Do full output sync
1. Signing now works again

It seems this could raise a few issues

1. @moneromooo-monero suggested if an unknown pubkey/address is encountered it could try further address derivation for a match (moreso than 200 address lookahead)
1. When hitting this edge case, it seems trying to sync outputs corrupts the wallet cache db causing more issues
1. On create_address endpoint, it limits itself to `count` between 1-64. For our use cause we generated 100k addresses, so we had to run this command in a loop. The value could allow a larger count, as the 100k address derivations took < 10 minutes and other commands in the monero rpc (like output/key image sync can take longer)

# Discussion History
# Action History
- Created by: nxs-crypto | 2023-02-03T13:34:48+00:00
