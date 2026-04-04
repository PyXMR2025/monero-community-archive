---
title: Can't connect to na.node.moneroworld.com as remote node when using Ledger
source_url: https://github.com/monero-project/monero-gui/issues/1533
author: aaronjolson
assignees: []
labels:
- resolved
created_at: '2018-07-30T03:13:48+00:00'
updated_at: '2018-12-17T08:54:32+00:00'
type: issue
status: closed
closed_at: '2018-12-17T08:54:32+00:00'
---

# Original Description
I just downloaded the new 12.3 lithium luna version of the Monero Wallet GUI. I went through the wizard, selecting set up hardware wallet, everything appeared to be working. However I don't have room on my machine to download the entire chain. I usually just use a remote node. In this case, trying to use the default  na.node.moneroworld.com

 1. I go to settings 
 2. I select remote node
 3. click connect

Then the key scrolling across the screen of the Ledger freezes. The ledger device becomes completely unresponsive. The bottom section of the GUI says that the daemon is synchronized, the "wallet blocks remaining" says all 15******* remaining, all grey bar, it also doesn't move.

If I click around in the GUI, say from the settings tab, up to the send or receive tab, the network status changes to disconnected.

Any ideas on how to fix this? Is this a known issue? 
Any other info I could provide that would be helpful?

I am running on Windows 10.
If I close the Monero GUI the Ledger goes back to scrolling and behaving normally immediately. 

Someone suggested I try a different node.
I tried node.xmrbackb.one at port 18081,
When I try to connect to that one I get a bit different behavior

The wallet blocks remaining says waiting for daemon to sync. The daemon blocks remaining is stuck at 23411. The ledger screen does not freeze though, which is encouraging? 

# Discussion History
## dEBRUYNE-1 | 2018-07-31T10:50:20+00:00
What did you use as `Restore height` upon generating the Ledger Monero wallet? 

## aaronjolson | 2018-08-17T15:59:53+00:00
1580000, also I set the subaddress-lookahead to 3:200

## dEBRUYNE-1 | 2018-08-19T11:03:52+00:00
@aaronjolson - Could you try to redo the Ledger wallet creation process with the parameters of [this guide](https://monero.stackexchange.com/questions/9901/how-do-i-generate-a-ledger-monero-wallet-with-the-gui-monero-wallet-gui) and the `node.moneroworld.com` (port 18089) remote node? 

## dEBRUYNE-1 | 2018-12-17T08:12:17+00:00
Author has not responded to my suggestion. I therefore am going to close this issue.



## dEBRUYNE-1 | 2018-12-17T08:12:24+00:00
+resolved

# Action History
- Created by: aaronjolson | 2018-07-30T03:13:48+00:00
- Closed at: 2018-12-17T08:54:32+00:00
