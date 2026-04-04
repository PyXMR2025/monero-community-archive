---
title: Monero wallet RPC error
source_url: https://github.com/monero-project/monero/issues/8761
author: ghost
assignees: []
labels: []
created_at: '2023-03-04T12:45:55+00:00'
updated_at: '2023-03-05T05:39:56+00:00'
type: issue
status: closed
closed_at: '2023-03-05T05:39:25+00:00'
---

# Original Description
2023-03-04 12:33:56.856 E Blocks start before blockchain offset: 0 2720000
2023-03-04 12:34:05.043 E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-03-04 12:35:54.256 E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error

# Discussion History
## selsta | 2023-03-05T03:13:34+00:00
Are you using testnet, stagenet or mainnet? Was your node fully synced before you created / opened this wallet? Did you try a full wallet rescan?

## ghost | 2023-03-05T05:29:30+00:00
I am using mainnet. Node was not fully synchronised. I created the wallet and started monero-wallet-rpc when it was 45% synced. 

> Are you using testnet, stagenet or mainnet? Was your node fully synced before you created / opened this wallet? Did you try a full wallet rescan?



## selsta | 2023-03-05T05:31:59+00:00
How did you create this wallet? If your node isn't synced then you can ignore this message.

## ghost | 2023-03-05T05:37:19+00:00
> How did you create this wallet? If your node isn't synced then you can ignore this message.

I created it using monero-wallet-cli repositories, it did not ask for full synchronisation. After wallet creation, I started monero-wallet-rpc but getting the error, which I previously mentioned.

## selsta | 2023-03-05T05:39:25+00:00
The error means that your wallet height is significantly higher than your daemon height. Sync your daemon and then it will go away. If you continue to have issues after your daemon is fully synced comment here and I will reopen the issue.

# Action History
- Created by: ghost | 2023-03-04T12:45:55+00:00
- Closed at: 2023-03-05T05:39:25+00:00
