---
title: Monero Wallet
source_url: https://github.com/monero-project/monero-gui/issues/4379
author: tacobella1
assignees: []
labels:
- question
created_at: '2024-12-03T22:00:00+00:00'
updated_at: '2024-12-05T00:50:21+00:00'
type: issue
status: closed
closed_at: '2024-12-05T00:50:20+00:00'
---

# Original Description
I really hope someone can help me, I've been trying to get my wallet to sync and I just can't seem to do it. I thought perhaps my laptop was not sufficient to run the wallet so I just bought a new laptop. I spent loads of money on the new laptop and it still won't load, I'm really pulling my hair out. I tried deleting everything and then to restore my wallet from a ledger nano x. I tried running it in simple mode, then tried the next level up and then full bootstrap. The wallet blocks get stuck and don't load.  The bar at the bottom loads and then the bar above it gets stuck usually at 999025 but sometimes other blocks and won't go beyond. Any ideas gratefully received.

# Discussion History
## selsta | 2024-12-03T22:29:51+00:00
@tacobella1 ignore the comment above, that's a scam. will try to get it removed

## tacobella1 | 2024-12-03T23:03:03+00:00
Oh yes, haha. They tried to get me to put in my mnemnomic (or however you spell it) phrase. I went there before I saw your message. lol

## selsta | 2024-12-03T23:04:20+00:00
Regarding your issue, did you export your view key when opening the wallet?

## tacobella1 | 2024-12-03T23:06:41+00:00
Yes, I did that and it all starts to load but then gets stuck and won't go any further


## selsta | 2024-12-03T23:08:03+00:00
When restoring the wallet, which restore height or restore date did you set?

## tacobella1 | 2024-12-03T23:08:39+00:00
I set the date as 2021-01-01 as I don't know the restore height


## selsta | 2024-12-03T23:10:08+00:00
Is the before you first received monero? Setting a date closer to when you first received monero means it will sync faster / skip more blocks.

Also I would recommend you to select advanced mode with a dedicated remote node. Do you know how to do that or do you need instructions?

## tacobella1 | 2024-12-03T23:10:59+00:00
Yes please may you give me instructions, that would be fantastic, thank you

## selsta | 2024-12-03T23:18:49+00:00
Try to use advanced mode and set a custom remote node. You can go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `node.monerodevs.org `
port: `18089`

Please report back if syncing with this one works or if it also gets stuck.

----------

Other remote node in case the above has issues: https://monero.fail

## tacobella1 | 2024-12-03T23:28:25+00:00
Thanks so much I will let you know


## tacobella1 | 2024-12-04T06:09:07+00:00
Hey, I left the wallet running all night. This morning the daemon has synchronized completely but the daemon has not synced at all yet. It did not work.

![image](https://github.com/user-attachments/assets/ff76feea-23c6-43f6-9003-6ceeeb3b8856)


## selsta | 2024-12-04T14:26:22+00:00
I have never seen this behaviour before but let's try a couple more steps to debug this issue.

Try this node, I just tested it locally and it works as expected.

address: `node3.monerodevs.org `
port: `18089`

If you still get the "waiting for daemon to sync" message then close your wallet, and create a new non-Ledger wallet and report back if it's able to sync up, or not.

These two steps should narrow down the issue.


## tacobella1 | 2024-12-04T19:44:22+00:00
I got it working, I changed to a different node and it worked. Thanks so much for helping!

## selsta | 2024-12-05T00:50:20+00:00
Good to hear, closing this as resolved.

# Action History
- Created by: tacobella1 | 2024-12-03T22:00:00+00:00
- Closed at: 2024-12-05T00:50:20+00:00
