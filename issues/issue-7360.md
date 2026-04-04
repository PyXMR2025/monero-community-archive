---
title: sweep_all command does not store recipient's address and payment id
source_url: https://github.com/monero-project/monero/issues/7360
author: AJIekceu4
assignees: []
labels: []
created_at: '2021-02-01T08:52:06+00:00'
updated_at: '2021-02-08T18:46:34+00:00'
type: issue
status: closed
closed_at: '2021-02-08T18:46:34+00:00'
---

# Original Description
Hello. I am using CLI version Monero 'Oxygen Orion' (v0.17.1.7-release) wallet. And found out that after using sweep_all command and transfer balance to integrated address (Kraken), command show_transfers did not show recepient's address or payment id. It is just show "0000000000000000" and "-" instead of payment id and address. Before this i was use "transfer" command to the same integrated address multiple times and everything is ok.
If i use show_transfer txid, then i see same problem:

> Payment ID: 0000000000000000
> Change: 0.000000000000
> Fee: 0.000011410000
> Destinations: 

# Discussion History
## moneromooo-monero | 2021-02-08T00:08:44+00:00
Addresses do get stored here. It might due to particular non default conditions on your side ?
Encrypted payment IDs are only decodable by the recipient, so they won't show for the sender. 

## AJIekceu4 | 2021-02-08T07:09:58+00:00
> Addresses do get stored here. It might due to particular non default conditions on your side ?
> Encrypted payment IDs are only decodable by the recipient, so they won't show for the sender.

Hello. I was do as always (as i remember it): opened a wallet, entered a passphrase, typed "refresh", wait until refresh is finish, after this typed "sweep_all address_from_kraken", entered password and transaction confirmation (i use my remote node in all cases). After i get transaction ID, closed wallet (did not wait until transaction get 10 confirmation or wallet became blocked) by closing terminal in which wallet was started (did not use exit command, just closed terminal window with mouse click). All previous transactions from this wallet i was doing the same way (maybe close wallet after it blocked with passphrase, can't remember now) and all recipients information was stored.

## moneromooo-monero | 2021-02-08T16:05:10+00:00
"closed terminal window with mouse click" means killing the window with the usual x button ? If so, you're killing monero-wallet-cli before it has a chance to save the wallet cache.

## AJIekceu4 | 2021-02-08T18:46:34+00:00
> "closed terminal window with mouse click" means killing the window with the usual x button ? If so, you're killing monero-wallet-cli before it has a chance to save the wallet cache.

Ok, thanks. I will close this issue then.


# Action History
- Created by: AJIekceu4 | 2021-02-01T08:52:06+00:00
- Closed at: 2021-02-08T18:46:34+00:00
