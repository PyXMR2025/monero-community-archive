---
title: 'possible BUG: monero-wallet-rpc generates bad addresses? '
source_url: https://github.com/monero-project/monero/issues/9213
author: robertvo
assignees: []
labels:
- question
- low priority
created_at: '2024-03-04T19:24:28+00:00'
updated_at: '2024-03-05T01:43:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have generated view only wallet and ran monero-wallet-rpc on a Linux server.
That sever generated new addresses via create_address RPC call.
After payment to these addresses the server correctly notified the receipt and confirmations.
These payments were confirmed on the chain however never showed up in the original non-viewonly wallet.
I have verified that wallet is properly synchronized, and that monero-wallet-rpc was not compromised by checking sha256.

When I started monero-wallet-rpc on my windows machine with the exact same view only .keys wallet, and did 
get_address_index call, it said: "Address doesn't belong to the wallet". I triple checked I'm using the same wallet file on Linux and Windows. On linux the get_address_index returned index around 2712. I confirmed that get_address_index for the primary address was working fine returning index 0 on both Linux and Windows.

These payments went to a black hole because monero-wallet-rpc possibly generated wrong addresses.
Could that wallet be somehow corrupted?
I generated a brand new wallet and the problem is gone. 
I'm wondering why this happed and where did my money go and will this happen again in future? 



# Discussion History
## selsta | 2024-03-05T01:43:39+00:00
It's likely an issue with the lookahead, you can use the `--subaddress-lookahead 50:3000` parameter during the wallet creation in monero-wallet-cli to make sure it scans 3000 subaddresses in advance. By default the value is 250 if I remember correctly.

# Action History
- Created by: robertvo | 2024-03-04T19:24:28+00:00
