---
title: Pending stuck
source_url: https://github.com/monero-project/monero-gui/issues/3140
author: Simao12W
assignees: []
labels:
- bug
created_at: '2020-10-08T11:45:14+00:00'
updated_at: '2022-01-15T22:02:30+00:00'
type: issue
status: closed
closed_at: '2020-10-14T14:14:25+00:00'
---

# Original Description
So i made everything from this topic https://monero.stackexchange.com/questions/6649/transaction-stuck-as-pending-in-the-gui
I send for the 2nd time and I still have a transaction pending, 18 minutes 0/10 confirmations. A transfer to me was in 2 minutes. 
I tried to sent 3 transactions, 1 was ok. 

>>> relay_tx e315d781a29f04a4589de35d2570f4c8029cfdc0b08423ebf8202b8d8cf47b31
[08.10.2020 13:53] 2020-10-08 11:53:57.193 I Monero 'Oxygen Orion' (v0.17.0.1-release) 
Error: Unsuccessful -- json_rpc_request:

# Discussion History
## xiphon | 2020-10-08T13:14:41+00:00
What wallet mode are you using? What steps did you do and what results did you get?

## Simao12W | 2020-10-08T15:12:32+00:00
Simply mode, flushed tx, renamed wallet name to old, restarted and then sent for the 2nd time. 
Now I did it again and i have a clean history. What to do know?

## xiphon | 2020-10-08T17:05:40+00:00
Did you try switching to another remote node (the "shuffle" icon near the connection status bars)?

## Sorb78 | 2020-10-09T23:09:39+00:00
Me and four other users have the same problem here:

https://www.reddit.com/r/Monero/comments/j871b8/transaction_not_being_confirmed/
https://www.reddit.com/r/Monero/comments/j86o7l/stuck_in_waiting_for_confirmation/
https://www.reddit.com/r/Monero/comments/j7umwx/tx_not_getting_confirmed_what_to_do/
https://www.reddit.com/r/monerosupport/comments/j7lnfa/help_me_please_monero_confirmation_010/

Either this version of monero-gui or the Ledger app is borked.


## selsta | 2020-10-09T23:12:20+00:00
@Sorb78 Are you also using simple mode?

We will release v0.17.0.2 soon and revert a change we did with the last release.

## selsta | 2020-10-09T23:13:57+00:00
In the meantime you can select Advanced mode and manually connect to a remote node, this should resolve the sending issue for now.

## Sorb78 | 2020-10-09T23:16:39+00:00
Yes I am using simple mode as I only have 18 GB available on my SSD.
Ok hope the new release will fix it. Thanks!

## selsta | 2020-10-09T23:17:53+00:00
@Sorb78 You can go to the main menu by clicking on the exit symbol in the top left corner.

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

address: `node.melo.tools`
port: `18081`

## Sorb78 | 2020-10-09T23:28:27+00:00
Thanks for the instructions. I tried it but it did not help. I tried to send the stuck transaction with relay_tx but I got the same error again as in the first post from Simao12W above. I then created a new transaction and it said "Transaction successfully sent!" but once again it was not sent to the mempool.

I can try the new version when it's released and delete the wallet file again.

## selsta | 2020-10-09T23:32:59+00:00
Please try again with new wallet file. The workaround I posted should definitely work with a fresh wallet, as it does not use the code we changed at all. Sending a transaction might take min 5 seconds up to 3 minutes to show up in the mempool, depending on how successful Dandelion++ is.

## Sorb78 | 2020-10-09T23:34:47+00:00
Wait, something's happening! 😄 I refreshed xmrchain.net and now it's there with two confirmations!! 🎉 

Edit: Thanks a lot! I will note it on Reddit.

## dccasciato | 2020-10-10T03:38:28+00:00
@selsta : Is there a way to generate a new wallet file to use your workaround:

_Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: node.xmr.to
port: 18081_

but **also** transfer funds from the old wallet file to be used there? I ask because using the remote node with the existing wallet does indicate that everything is connected and synchronized... tho the status command gives me this 

Error: Couldn't connect to daemon: 127.0.0.1:18081

Is this because I am using the existing wallet file? If so, my funds are held up and are not transferable to the new wallet file when I generate it...



## selsta | 2020-10-10T03:44:03+00:00
Did you try if transferring worked with the workaround? If not, please try to create a new wallet file by restoring from seed. Then try again.

> Error: Couldn't connect to daemon: 127.0.0.1:18081

You can ignore this as long as it says synchronized in the bottom left corner.

## dccasciato | 2020-10-10T03:56:23+00:00
ok, all good now. thanks for the quick response!


## molecular | 2020-10-10T20:26:56+00:00
thanks for all the infos, guys. I was getting frustrated...

## selsta | 2020-10-13T20:24:54+00:00
v0.17.1.0 has been tagged and will be released tomorrow.

## selsta | 2020-10-14T14:14:25+00:00
https://www.getmonero.org/2020/10/14/monero-GUI-0.17.1.0-released.html

## molecular | 2020-10-15T14:21:16+00:00
confirming it 0.17.1.0 fixes the issue for me. Thanks everyone.

## userlip | 2020-10-18T08:38:37+00:00
Just wanted to say that I currently am experiencing this bug with the newest version (0.17.1.0).
I don't know much about troubleshooting but just let me know how I can be of help (should I open a new Issue?)

Edit: Also sometimes I noticed that the transaction that is waiting to be confirmed, disappears from the transaction list after a few seconds. So I go to the Transactions in the GUI Wallet and the transaction is there then I wait for like 20 to 40 seconds and it just disappears.

Yes I did all the steps from https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706480292

## alan-camilo | 2020-11-03T23:30:08+00:00
I am running 0.17.1.1 GUI on Debian and I am facing the exact same issue when trying to send xmr in simple mode. The workaround given by @selsta [comment](https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354) using a remote node works but even with the last version the issue  is **not** solved when using the simple mode.

## xiphon | 2020-11-04T00:29:48+00:00
We are actively working on it. There will be new release in a few days.

## peterbelau1 | 2020-12-03T21:18:57+00:00
FYI, I'm still seeing this issue as of v0.17.1.5-release

## selsta | 2020-12-03T21:50:57+00:00
@peterbelau1 Simple mode? Are you sure that it really is failing or do they still confirm after a couple minutes even if they initially display failed?

## peterbelau1 | 2020-12-04T19:26:20+00:00
My apologies -- this seems to be the wrong bug thread although related to the same issue(?) What I'm experiencing seems to be documented here:

https://www.reddit.com/r/Monero/comments/k5vvsf/update_01715_slow_current_blocks/

# Action History
- Created by: Simao12W | 2020-10-08T11:45:14+00:00
- Closed at: 2020-10-14T14:14:25+00:00
