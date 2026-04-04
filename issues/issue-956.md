---
title: Сan not send coins
source_url: https://github.com/monero-project/monero-gui/issues/956
author: kvachkov
assignees: []
labels:
- duplicate
created_at: '2017-11-14T19:24:28+00:00'
updated_at: '2018-01-11T13:54:15+00:00'
type: issue
status: closed
closed_at: '2018-01-11T13:54:15+00:00'
---

# Original Description
In the wallet monero-gui-win-x64-v0.11.1.0 is not the active send button. There are coins, the wallet is synchronized. Wallet logs:
![image](https://user-images.githubusercontent.com/26360204/32800098-84b32ac4-c98a-11e7-885d-caf3cb3083f9.png)
![image](https://user-images.githubusercontent.com/26360204/32800212-c797009a-c98a-11e7-8842-f04868f7b78f.png)



# Discussion History
## dEBRUYNE-1 | 2017-11-15T17:34:03+00:00
Did you try to restart the GUI + daemon?

## medusadigital | 2017-11-16T11:03:07+00:00
the send butto can also be disabled if Address validation fails.

make sure u copy it correctly or the entry in your addressboook is correct

## kvachkov | 2017-11-19T16:30:05+00:00
The address was checked, everything is in order. I tried to send via monero-wallet-cli.exe. Written that the transaction was successful, but the balance has not changed and nothing has come to another purse ...
![image](https://user-images.githubusercontent.com/26360204/32992784-0313681a-cd60-11e7-9104-73d81932cb18.png)

Daemon address: node.moneroworld.com
Log daemon:

Height: 1446458/1446458 (100.0%) on mainnet, not mining, net hash 238.84 MH/s, v6, up to date, 8(out)+0(in) connections, uptime 0d 0h 4m 23s
Height: 1446458/1446458 (100.0%) on mainnet, not mining, net hash 238.84 MH/s, v6, up to date, 8(out)+0(in) connections, uptime 0d 0h 5m 2s

## stoffu | 2017-11-19T22:55:15+00:00
Look carefully at the message which says:

> Unsigned transaction(s) successfully written to file: unsigned_monero_tx

which means you're sending from a watch-only wallet.
It's a correct behavior that the balance doesn't change. It changes only when it receives new funds (increase), or when it imports key images from the full wallet (decrease).

## kvachkov | 2017-11-20T04:52:21+00:00
Thank you, yesterday I realized that I sent it with a watch-only wallet. I had to create a watch-only wallet, because the main one was not saved after creation in the specified folder. Tell me where is the temporary file with the purse after it was created, because when you close the wallet gui it only needs to be restored.
Also, if you select a directory for the purse when you create it, if the folder has Russian characters, an error occurs ...

## stoffu | 2017-11-20T05:50:02+00:00
I think the GUI stores the wallet files under `<home_folder>/monero/wallets/` (but I could be wrong). Not sure about how to deal with Russian characters. Maybe copy the file to a path without Russian characters and try opening it again?

## sanderfoobar | 2018-01-11T13:14:28+00:00
Related to #199 #758 #820 and eventually https://github.com/monero-project/monero/issues/1390

## medusadigital | 2018-01-11T13:36:54+00:00
closing here with dublicate label, since fix will be directly in libwallet API.

https://github.com/monero-project/monero/issues/1390

## medusadigital | 2018-01-11T13:37:22+00:00
+duplicate

# Action History
- Created by: kvachkov | 2017-11-14T19:24:28+00:00
- Closed at: 2018-01-11T13:54:15+00:00
