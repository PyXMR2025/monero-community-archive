---
title: Monero Gui not showing funds
source_url: https://github.com/monero-project/monero-gui/issues/3892
author: DarkAngel85
assignees: []
labels: []
created_at: '2022-04-24T17:58:34+00:00'
updated_at: '2022-04-27T05:40:39+00:00'
type: issue
status: closed
closed_at: '2022-04-27T05:22:48+00:00'
---

# Original Description
I had funds in my Monero Gui wallet which I had set up with the Ledger Nano S. 

I transferred more funds, but the wallet never updated the amount of XMR in the wallet. I deleted the monero wallet and the Monero files and downloaded the Monero Gui from scratch with the Ledger. The receiving wallet address is exactly the same as before. So it's the same wallet. However it is saying I have zero balance. It is not even showing the funds that were showing up before. 

# Discussion History
## selsta | 2022-04-24T18:00:03+00:00
What did you set as your restore height?

## DarkAngel85 | 2022-04-24T18:01:54+00:00
2396387

## marlonpnz | 2022-04-24T19:42:50+00:00
Same problem here. I notice the "secret view key" is all zeros, like "000000...". I do not know if ledger also protect the private view key, like it does with the spend key. However I suspect it may be related with the fact that the balance is not shown anymore. I have a balance I did transfer some months ago, which was ok at that time. But now is not showing, it is, the balance always show as zero, even after complete synchronization. Any suggestion?
OBS: I tried to restore in all ways, including that one where we put the date before the transaction. No method worked.

## selsta | 2022-04-24T19:46:17+00:00
@marlonpnz As long as you export the view key everything is fine. The keys don't get displayed by the GUI.

------

Can both of you go to Settings -> Info and post the "wallet mode" and "wallet restore height"?

@DarkAngel85 I know you posted it already but I just want that you confirm what it says on that page.

## marlonpnz | 2022-04-24T22:32:59+00:00
thanks @selsta,
update: it finally worked some minutes ago. I set it up today once more, creating a new hardware wallet in simple mode. After some hours the balance show up. This is weird, once I did this process many times and let it syncing for many hours before. Luckily I was not in a hurry to sell. Don't know what could be the reason.
I will try again in some days, than will check the info page as stated.

## selsta | 2022-04-24T22:34:16+00:00
@marlonpnz I would recommend to setup advanced mode with a remote node.

Simple mode can be a bit spotty because it uses a random remote node :/ Do you need instructions for that?

## DarkAngel85 | 2022-04-25T05:23:20+00:00
the wallet mode in my case is: Simple mode and the Wallet restore height: 2396387. Today my original amount is showing up, but still no sign of the rest of the funds I transferred a week ago. 

Yes please, if you suggest Advance mode I would appreciate instructions. 

## selsta | 2022-04-26T01:27:02+00:00
You can go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `88.198.199.23`
port: `18081`

This should resolve your issue for now. No extra hard disk space required.

----------

Other remote node in case the above has issues:

address: `node.supportxmr.com`
port: `18081`

address: `78.47.80.55`
port: `18081`

address: `node.community.rino.io`
port: `18081`

## DarkAngel85 | 2022-04-26T18:37:21+00:00
Thanks. Am still trying to wait for the wallet to fully load. Will keep you updated once it's sorted out. 

## selsta | 2022-04-26T18:38:21+00:00
Do you have the transaction id of the funds that are missing?

## DarkAngel85 | 2022-04-27T05:20:52+00:00
I can finally see the funds in my wallet. Thanks for your help! Hope you have a good rest of the week :)

## DarkAngel85 | 2022-04-27T05:27:22+00:00
I just tried making a donation to the Monero core team, but the wallet has come up with error 64

## selsta | 2022-04-27T05:28:12+00:00
Can you make a screenshot of this error? I'm not aware of error 64.

Edit: Seems to be Ledger related, don't need a screenshot.

## selsta | 2022-04-27T05:33:46+00:00
@DarkAngel85 did you make sure that you export the Ledger view key on wallet opening? Also did you make sure that your Ledger is unlocked the whole time during transaction creation?

## DarkAngel85 | 2022-04-27T05:39:27+00:00
Hi I tried it twice. Once when the Ledger was not connected and another time when it was. The error came up both times. I have closed and reopened the wallet and it has now worked. I sent a small donation to thank you for your help. 

The best thing to do in that situation is for the wallet to give the user feedback to connect the Ledger beforehand so the error does not come up. I'm a UX designer so if the Monero team needs any advice you can ask :)

## selsta | 2022-04-27T05:40:38+00:00
Yes, that definitely has to be improved! Thank you for the donation :)

# Action History
- Created by: DarkAngel85 | 2022-04-24T17:58:34+00:00
- Closed at: 2022-04-27T05:22:48+00:00
