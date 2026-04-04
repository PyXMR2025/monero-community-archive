---
title: 'monero-wallet-cli: Empty Destinations'
source_url: https://github.com/monero-project/monero/issues/2861
author: m9ra
assignees: []
labels: []
created_at: '2017-11-24T19:21:48+00:00'
updated_at: '2017-11-24T21:06:59+00:00'
type: issue
status: closed
closed_at: '2017-11-24T21:06:59+00:00'
---

# Original Description
Dear Monero developers, 
I'm confused by monero-wallet-cli behavior.
 
Some of the transactions made (via monero-wallet-rpc) does have empty Destinations info.
 
Monero 'Helium Hydra' (v0.11.0.0-8d511f3)
 
```
show_transfer TXID_PLACEHOLDER
Outgoing transaction found
txid: <TXID_PLACEHOLDER>
Height: 1449822
Timestamp: 07:06:30 AM
Amount: 0.516871446050
Payment ID: 0000000000000000
Change: 5.740382929930
Fee: 0.003262420000
Destinations:
Note:
```

The target address was an Integrated Monero Address (so I'm also confused, why the Payment ID is zeros)
What does it mean? I checked the transaction on http://blox.minexmr.com via Prove Transaction feature and it has shown that the expected amount was transferred to the desired integrated monero address.


# Discussion History
## moneromooo-monero | 2017-11-24T19:38:12+00:00
Did you rescan the blockchain after making that tx ?

## m9ra | 2017-11-24T19:59:13+00:00
I ran rescan_spent and rescan_bt in the monero-wallet-cli and the show_transfer output looks still the same.

## moneromooo-monero | 2017-11-24T20:10:35+00:00
Running rescan_bc (or deleting the cache, or restoring from seed) will do this. You can't pull the destinations addresses from the blockchain, and payment ids from integrated addresses are only decryptable by the recipient. They're only remembered while you have your wallet cache. If it is recreated, those informations are gone.

## m9ra | 2017-11-24T20:19:42+00:00
I see, destinations for all transactions are gone now. However, before I run rescan_bc I could see Destinations for older transactions but not for the most recent one - so cache could get corrupted somehow? 

Anyway, thank you for the explanation. I was worried that my wallet is corrupted somehow.



## moneromooo-monero | 2017-11-24T20:24:56+00:00
If you could see older ones but not more recent ones, it sounds like a bug, unless you're using that same wallet from two different places, in which case only the sending wallet knows about the destination and therefore can remember them.

## m9ra | 2017-11-24T20:30:15+00:00
I made all the transactions via monero-wallet-rpc on a single machine. So it seems that cache information stopped to be saved at some point.

## moneromooo-monero | 2017-11-24T20:45:27+00:00
The info in the first post seem to be obtained via monero-wallet-cli. Is this correct ? If so, have you ever sent a tx via monero-wallet-rpc while monero-wallet-cli was running ? If you run two wallets on the same wallet cache, the last one to exit will save and overwrite what the other wrote. Similarly, if you kill the wallet or it crashes, it won't have the opportunity to save that kind of info.

## m9ra | 2017-11-24T21:06:59+00:00
Yes, its obtained from monero-wallet-cli. I'm occasionally using it to observe what was done via RPC. I can also rembember that I stopped the RPC before the first empty Destinations transaction. (So it had the chance to save cache info) Now I stopped the RPC again and the info appeared for the most recent transaction. So, the issue was my misunderstanding of the caching mechanism.

Thank you for the explanation!

# Action History
- Created by: m9ra | 2017-11-24T19:21:48+00:00
- Closed at: 2017-11-24T21:06:59+00:00
