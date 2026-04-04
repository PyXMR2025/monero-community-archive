---
title: Monero wallet freezes ledger
source_url: https://github.com/monero-project/monero-gui/issues/1937
author: tippierchip
assignees: []
labels:
- resolved
created_at: '2019-02-12T22:55:49+00:00'
updated_at: '2019-02-20T07:45:34+00:00'
type: issue
status: closed
closed_at: '2019-02-20T07:45:34+00:00'
---

# Original Description
I've downloaded the the windows monero wallet yesterday and opened a new account with my nano ledger s.
Then i let it the wallet sync and while syncing i made a transaction to my ledger/ monero wallet.
The sync took a while so i discconected the ledger and let it keep syncing.
Today i wanted to check my balance but couldnt access my acount.
Tge ledger it kept on freezing when asking for the view key.
So i deleted the monero wallet and reinstalled it.. 
Than Tried to open a new wallet with the ledger but still it freezes when asking for the view key.
Any sulutions


# Discussion History
## dEBRUYNE-1 | 2019-02-13T08:47:37+00:00
You're, alas, probably affected by this issue:

https://github.com/LedgerHQ/ledger-app-monero/issues/29



## cslashm | 2019-02-13T14:50:48+00:00
@tippierchip please report to the above issue, giving full detailed of tou OS, client version, app version (check it in "settings" menue of the app)

Moreover you said 'The sync took a while so i discconected the ledger and let it keep syncing.' Not You SHALL not disconnect your device while using your wallet.


## tippierchip | 2019-02-13T21:08:44+00:00
@cslashm the opwerating system is windows 64 bit
the monero wallet is 0.13.0.4 Beryllium Bullet (gui)
the nano ledger s is updated to 1.5.5 
everything is the most recent brand new updates.
regarding your comment i really did not have much of a choice unless i was gonna leave my ledger connected to the computer all night long. also the wallet seemed to do just fine after i dissconected the ledger device so i let it sync.
the problem was the morning after when trying to reconnect. the wallet wouldn't connect and kept asking for a password which i didnt have cause it was never made also whaen trying to open from the file it wouldn't read the wallets file.
after erasinf the wallet from my computer and reinstalling it i tried to open a new wallet with the ledger but it freezes when asking for the view keys. exactly like what @dEBRUYNE-1  refered to it seems like theres a fault with the app and the ledger connection atm.
the ledger works just fine on ledger live and on other wallets but my monero is gone for now till the next update i guess :(   

## mmbyday | 2019-02-16T00:15:49+00:00
@tippierchip I can confirm 0.13.0.4 gui with 1.5.5 nano s firmware, with 1.1.2 xmr ledger app is working. Is ledger live closed, or any other apps that might use the nano s, when you try using the gui? 

## cslashm | 2019-02-18T08:07:56+00:00
@mmbyday Thanks for reporting. Can you provide me your OS configuration?

## mmbyday | 2019-02-20T00:37:43+00:00
@cslashm windows10

## dEBRUYNE-1 | 2019-02-20T07:38:03+00:00
This has been fixed with the recently released v1.1.3 of the Ledger Monero blue app. 

## dEBRUYNE-1 | 2019-02-20T07:38:07+00:00
+resolved

# Action History
- Created by: tippierchip | 2019-02-12T22:55:49+00:00
- Closed at: 2019-02-20T07:45:34+00:00
