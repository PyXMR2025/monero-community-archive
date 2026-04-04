---
title: Mainnet wallet cannot be oppend as testnet wallet
source_url: https://github.com/monero-project/monero/issues/3715
author: zeshanvirk
assignees: []
labels:
- invalid
created_at: '2018-04-27T06:53:36+00:00'
updated_at: '2018-04-28T17:55:46+00:00'
type: issue
status: closed
closed_at: '2018-04-28T17:55:46+00:00'
---

# Original Description
I ran monerod by typing command in cmd **"./monerod --testnet"**, it syncs the whole blockchain and i started monero-wallet-cli using command **"./monero-wallet-cli set_daemon 28081"** and i created a wallet, then i tried to run the rpc wallet but got error mainnet wallet cannot be oppend as testnet wallet. My command is 
**"./monero-wallet-rpc --testnet --wallet-file file-name --password ***** --rpc-bind-port 28090**

# Discussion History
## moneromooo-monero | 2018-04-27T07:15:29+00:00
You clearly ran monero-wallet-cli without --testnet above. Or is that a typo and you did use --testnet ?
Moreover, "set_daemon 28081" should not be a valid command. Commands passed as parameter also run it and exit (or should).

## zeshanvirk | 2018-04-27T07:37:44+00:00
Fixed, i forgot to run cli too with --testnet, i didn't read it anywhere to run the cli too on testnet. running cli too on testnet works for me. Thanks

## moneromooo-monero | 2018-04-27T17:31:05+00:00
+invalid

# Action History
- Created by: zeshanvirk | 2018-04-27T06:53:36+00:00
- Closed at: 2018-04-28T17:55:46+00:00
