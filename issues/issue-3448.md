---
title: monero-wallet-rpc creating double spend tx that are rejected by monerod
source_url: https://github.com/monero-project/monero/issues/3448
author: sneurlax
assignees: []
labels:
- invalid
created_at: '2018-03-20T06:29:16+00:00'
updated_at: '2018-03-20T16:16:55+00:00'
type: issue
status: closed
closed_at: '2018-03-20T16:16:55+00:00'
---

# Original Description
I'm working on [monero-integrations/monerophp](https://github.com/monero-integrations/monerophp) in [sneurlax/monerophp#feature/rpc](https://github.com/sneurlax/monerophp/tree/feature/rpc) and trying to get it ready for the upcoming network upgrade.  I am on testnet and monero-wallet-rpc is apparently creating invalid tx (invalid due to double spends.)

here is a pastebin of my monero-wallet-rpc output: https://pastebin.mozilla.org/9080413

I've tried adding more (and less) parameters to the transfer method, I've tried using flush_txpool on the node in question, and I've tried sending tx via monero-wallet-cli (which works just fine.)  I have plenty of spendable balance.  I had one or two tx out of 50 or so go through inexplicably, and unfortunately not reproducibly (I was fuzzing around a bit trying to add and remove parameters, thinking that 0.12 has added some mandatory fields)

# Discussion History
## moneromooo-monero | 2018-03-20T13:04:03+00:00
Are you running two wallets on the same wallet file at the same time ? If so, don't. Then run rescan_spent once.

## sneurlax | 2018-03-20T14:15:34+00:00
no, I am not, but you are correct that running rescan_spent is a fix: this morning I refreshed the monerophp page and it transferred successfully on the first try, but the second transfer failed.  I opened the wallet with monero-wallet-cli, used rescan_spent, and monerophp was able to spend again ... what's the cause of this?  am I going to have to add a hook to rescan_spent after every transfer?  that certainly works, but ... feels like I'm doing something wrong.

this can be closed but I am updating the node.js wrapper to be ready for 1546000, too, and feel like I should have a more elegant fix than tagging rescan_spent to the tail of every transfer

## moneromooo-monero | 2018-03-20T14:27:11+00:00
Post a level 2 wallet log to github or fpaste.org or pastebin.mozilla.org (from the start, including the working initial tx).

## sneurlax | 2018-03-20T14:51:58+00:00
[monerod.txt](https://github.com/monero-project/monero/files/1829829/monerod.txt)

[monero-wallet-rpc.txt](https://github.com/monero-project/monero/files/1829830/monero-wallet-rpc.txt)

## moneromooo-monero | 2018-03-20T15:09:03+00:00
Your wallet log shows that after sending the first tx, you reload the wallet without having saved it, so it doesn't remember it's spent that output in the first place.

Edit: well, I *assume* you didn't save it, there are no logs showing such, and I think there should be though I'm not 100% sure. Did you save it or not ?

## sneurlax | 2018-03-20T15:40:21+00:00
not as far as I can see, no.  but this is new behavior as of 0.12, the wrapper didn't change and I wasn't encountering this issue before (built from master on the 12th... should rebuild to make sure it's current behavior.)

I'll add a call to save after transfers are made instead of rescan_spent before (either will work.)  as far as I'm concerned this is closed, thank you so much for holding my hand through this, ha

## moneromooo-monero | 2018-03-20T16:15:55+00:00
The wallet would see the outputs are spent when the tx is mined fwiw. Maybe you waited enough time before.

+invalid


# Action History
- Created by: sneurlax | 2018-03-20T06:29:16+00:00
- Closed at: 2018-03-20T16:16:55+00:00
