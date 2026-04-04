---
title: monero-wallet-rpc height is less than monerod height
source_url: https://github.com/monero-project/monero/issues/4132
author: skinderis
assignees: []
labels:
- invalid
created_at: '2018-07-13T11:17:29+00:00'
updated_at: '2018-07-19T15:17:03+00:00'
type: issue
status: closed
closed_at: '2018-07-19T15:17:03+00:00'
---

# Original Description
Hi,
I am running _monero-wallet-rpc_ and _monerod_ on separate docker containers. Wallet container is connecting to _monerod_ container. But the weird thing happens that when i run `getheight` command on _monero-wallet-rpc_ it shows less height than height showed in by `monerod` (`get_height` method). Sometimes I stop wallet and open it again and it suddenly synchnorizes, but usually not and `getheight` < `get_info`

For example, wallet height is **1143125** and daemon height is **1143155**, so **30** blocks are not synced on monero wallet. (I am running testnet now)

Is there any way for the wallet to be all the time updated and synced with blockchain? 
And, if my wallet is stopped, is it syncing or when I `open_wallet` it, then it starts to sync (that means if long time not opened wallet might take time to sync when it opened again)?

Thanks!

# Discussion History
## moneromooo-monero | 2018-07-13T13:26:39+00:00
Run monero-wallet-rpc with --log-level 1 and see whether you get any errors.

If you've not loaded a wallet in a long time, then yes, it'll obviously take longer to refresh than if it had been opened recently.

If your wallet is loaded, then it should sync with the node every 20 seconds. If it doesn't, then it might be a bug.


## skinderis | 2018-07-19T13:46:15+00:00
I solved the problem by using RPC method `store` on wallet. But one more issue that I am facing is that wallet sometimes shows message `{'code': -38, 'message': 'no connection to daemon'}`. This error makes a lot of problems for me as I can't automate `transfer` method. My code is trying to send some monero and when it shows this error I have to fix it by hand.

The error `{'code': -38, 'message': 'no connection to daemon'}` is not showing all the time it's 50% of succedding. What can I do?

Maybe someone has working `monerod` and `monero-wallet-rpc` docker images (where wallet is connected to daemon and works without this error) here? it would be very helpful!
@moneromooo-monero @dEBRUYNE-1 


## moneromooo-monero | 2018-07-19T15:11:09+00:00
Use 0.12.2.3.0, it's easier on timeouts.

User error (exiting without saving), so closing.

+invalid


# Action History
- Created by: skinderis | 2018-07-13T11:17:29+00:00
- Closed at: 2018-07-19T15:17:03+00:00
