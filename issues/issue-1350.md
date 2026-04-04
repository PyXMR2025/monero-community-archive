---
title: Monero GUI transaction was sent, but not received?
source_url: https://github.com/monero-project/monero-gui/issues/1350
author: bigpun87
assignees: []
labels:
- resolved
created_at: '2018-04-23T01:56:29+00:00'
updated_at: '2018-09-04T00:07:10+00:00'
type: issue
status: closed
closed_at: '2018-07-04T09:18:32+00:00'
---

# Original Description
Hi - I sent 1 monero to my Binance account, and it is showing as "sent" on my GUI if I "prove/check" the transaction, but on moneroblocks.info I cannot find the transaction at all. Binance is claiming they never received it either and it's been almost 2 days. My Monero GUI account was also reduced for 1 Monero, which implies it was sent? 

If it helps, I sent the transaction on an older version of the Monero GUI (version 11) and then upgraded to version 12 after to hope it would help, but it has not.

Tx ID: | 9f81ecaa5034180f601a469c0b7ef70ad270b1a7b57b6364aee01ce3d25434ef


Thanks




# Discussion History
## dEBRUYNE-1 | 2018-04-23T11:26:51+00:00
See my post below:

>If your transaction does not show up on a blockexplorer like, for instance, [XMRchain](https://xmrchain.net) or [MoneroBlocks](https://moneroblocks.info), you, most likely, performed it on the wrong (alternative) chain. Therefore, you should be able to resolve your issue with this guide:

>https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-created-pe

>Please note (from the [linked guide](https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-as-a-result)):

>>As a general rule of thumb, for each day you synced after the fork height (1546000 or April 6) you have to pop 800 blocks. Thus, let's say you synced 10 days on the wrong (alternative) chain, you should use --pop-blocks 8000

>Since we're 17 days after the scheduled network upgrade, you ought to use `--pop-blocks 13600`

>P.S. I reckon aforementioned guide might be a bit convoluted. Therefore, if you need any assistance, feel free to shoot me a PM. 

>P.P.S. Your Monero should be back in your wallet after applying aforementioned guides. 

## bigpun87 | 2018-04-25T03:44:46+00:00
unfortunately none of the above work - I re-synced the blockchain with the instructions provided to no avail and also upgrade to v0.12. I then ran the went "flush_txpool" but the transaction did not show as "failed". I then changed the wallet directory but that did not help.. Anyway to just wipe this clean and start from scratch? Feel exhausted from this

## bigpun87 | 2018-04-25T04:14:37+00:00
also, I would PM you, but no idea how to!

## dEBRUYNE-1 | 2018-04-25T11:29:09+00:00
@bigpun87 - You can PM me on reddit -> https://www.reddit.com/user/dEBRUYNE_1/

## victorgp | 2018-04-27T23:58:03+00:00
Same happened to me, PM sent in reddit

## victorgp | 2018-04-28T04:07:36+00:00
@bigpun87 @dEBRUYNE-1 i've managed to fix the problem by using a remote node, something that i wanted to avoid but it was my last resort, by using a local node i didn't manage to fix the problem, and i followed all the steps in that link.

You can get remote nodes from here https://moneroworld.com/

At least i have my coins again...

## dEBRUYNE-1 | 2018-07-04T08:42:47+00:00
This particular issue is resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

## dEBRUYNE-1 | 2018-07-04T08:42:52+00:00
+resolved

## jetflyer888 | 2018-08-03T20:05:07+00:00
@dEBRUYNE-1 thanks for all of the information, I tried https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/ but in my GUI transaction history I see the transaction (Monero GUI to Binance transaction) but haven't received funds in Binance. After upgrading to v01220 I still see transaction in history with funds not reinstated.

If you can offer any help that would be greatly appreciated as I'm stuck as to what to try next. Thanks

## jetflyer888 | 2018-08-04T04:27:18+00:00
@dEBRUYNE-1 all resolved now by installing v012.3.0 - thanks all for previous posts.

## techjeffe | 2018-09-04T00:07:10+00:00
Thank you for this note @dEBRUYNE-1 - helped me recover 2 XMR! Appreciate you!

# Action History
- Created by: bigpun87 | 2018-04-23T01:56:29+00:00
- Closed at: 2018-07-04T09:18:32+00:00
