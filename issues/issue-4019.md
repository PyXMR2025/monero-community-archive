---
title: xmr purchase not showing in wallet
source_url: https://github.com/monero-project/monero-gui/issues/4019
author: danx42
assignees: []
labels: []
created_at: '2022-08-31T14:19:20+00:00'
updated_at: '2022-09-01T05:52:34+00:00'
type: issue
status: closed
closed_at: '2022-09-01T05:48:38+00:00'
---

# Original Description
I made a purchase on Monero Local. The transaction was sent successfully but is not showing in my monero wallet (GUI). I have verified the transaction on xmrchain.net. Have triggered wallet refresh but still nothing. Any help would be really appreciated!

# Discussion History
## cnxnhcv | 2022-08-31T17:50:21+00:00
I have the same problem although I'm 100% I sent the xmr, however, downloaded the latest version, now the new version keeps saying couldn't open the wallet file,  
Edit: I changed the file path and the wallet opened fine, however, I can't see the xmr I added to the wallet.

## selsta | 2022-08-31T21:12:13+00:00
@danx42 @cnxnhcv Can both of you go to Settings -> Info and post

- Version
- Wallet mode
- Wallet restore height

then I can give further instructions.

## cnxnhcv | 2022-09-01T01:12:56+00:00
> @danx42 @cnxnhcv Can both of you go to Settings -> Info and post
> 
> * Version
> * Wallet mode
> * Wallet restore height
> 
> then I can give further instructions.

Thanks for the fast replay,

Im atm using the latest version (0.18.1.0)
wallet mode: I normally use simple mode, however, Im trying Advanced mode (Local node) at the moment 
Wallet restore height (228705)

Noteworthy, I was using a really old version something around 0.13, it was going fine with me so I didnt want to upgrade - which is dumb from my side-,, Also the old version opens my wallet file with no issue but the new version keeps saying it can not do that until I change the file path, but unfortunately it shows the balance without the added xmr.

thanks for your time 

## selsta | 2022-09-01T01:15:15+00:00
> Also the old version opens my wallet file with no issue but the new version keeps saying it can not do that until I change the file path

This seems to be related to special characters in the file path and will be resolved in an upcoming update.

> but unfortunately it shows the balance without the added xmr.

Is your local node synced? Can you go to Settings -> Log, type `status` into the textbox and post the output here?

## cnxnhcv | 2022-09-01T01:21:36+00:00
>>> status
[01/09/2022 05:21] 2022-09-01 01:21:07.619 I Monero 'Fluorine Fermi' (v0.18.1.0-release) 
Height: 1351204/2702027 (50.0%) on mainnet, not mining, net hash 115.86 MH/s, v5, 10(out)+0(in) connections, uptime 0d 4h 18m 33s

## selsta | 2022-09-01T01:23:25+00:00
Your node is only 50% synchronised. You can either wait for it to go to 100% (which can take between 12h and multiple days depending on your hardware) or you can set a remote node.

You can set a remote node in Settings -> Node -> Remote node. https://nodes.monero.com has a list of remote nodes.

## cnxnhcv | 2022-09-01T02:20:42+00:00
wow!
It actually worked, my issue was I was connected to a dead old node probably, updated my node and the xmr showed up.

I am really really grateful, for you to have the time to answer noobs like me, the Brightside I found this website where I can learn more about xmr.

wish you all the best,

## danx42 | 2022-09-01T05:48:38+00:00
> Your node is only 50% synchronised. You can either wait for it to go to 100% (which can take between 12h and multiple days depending on your hardware) or you can set a remote node.

Yeah, I think this was my problem. Downloaded another client on a mobile device and recovered my wallet on it and xmr showed. Now showing in the GUI also.
Thanks!


# Action History
- Created by: danx42 | 2022-08-31T14:19:20+00:00
- Closed at: 2022-09-01T05:48:38+00:00
