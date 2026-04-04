---
title: GUI wallet synced with daemon; funds not appearing
source_url: https://github.com/monero-project/monero-gui/issues/3912
author: anon74652393854769423587
assignees: []
labels: []
created_at: '2022-05-06T13:21:38+00:00'
updated_at: '2022-05-06T14:21:38+00:00'
type: issue
status: closed
closed_at: '2022-05-06T14:21:24+00:00'
---

# Original Description
I tried to exchange some btc (Around 250 USD) to XMR using Changelly. On that side, the transaction out to the XMR address was successful. Double checked addresses; all as it should be.

However in my desktop wallet (Monero GUI) it has not shown up. The daemon is synced and it has been a day and I honestly have no idea what to do.

I'm a noob at this, not gonna lie. I'm literally just trying to buy some herbal medicine for myself, in a safe manner to improve my quality of life, in a country whose government is very much against this particular medicine. I'm not moving a shit ton around so I can afford (at least $250) to be a noob.

Is there something I have missed? Or is it a blockchain issue?

TX ID is vjbghubfj3zg84bs

# Discussion History
## selsta | 2022-05-06T13:24:52+00:00
Do you have a monero transaction id? The tx id you posted seems to be the Changelly ID. It should look something like:

```
e36e78deffc8af4d832249e83356ac5f38c14758465a1052617cdfa79b8ee5a3
```

Can you go to Settings -> Info and post the following:

- GUI version
- Wallet restore height
- Wallet mode

## anon74652393854769423587 | 2022-05-06T13:34:42+00:00
I think this is the right one: 23e2fd441fd2e52d18f779c259b14719af9c62f578a14c983c02e18bb683c855

GUI version 0.17.3.2-unknown (Qt 5.15.3)
restore height 2596098
simple mode

## selsta | 2022-05-06T13:36:48+00:00
Try to use advanced mode and set a custom remote node. You can go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `88.198.199.23`
port: `18081`

Then wait for everything to sync and report back if your issue is resolved.

----------

Other remote node in case the above has issues:

address: `node.supportxmr.com`
port: `18081`

address: `78.47.80.55`
port: `18081`

address: `node.community.rino.io`
port: `18081`

## anon74652393854769423587 | 2022-05-06T13:51:07+00:00
Unfortunately no change, tried all listed remote nodes and restarted the GUI and daemon, nothing

## selsta | 2022-05-06T13:54:31+00:00
Please enter the first IP (88.198...) and then wait a couple minutes. Then check if the bottom left corner displays the following:

- Wallet is synchronized
- Daemon is synchronized (2617***)
- Network status: Remote node

If all this is the case I'll give you further instructions.

## anon74652393854769423587 | 2022-05-06T13:59:02+00:00
Done, can confirm all 3 conditions on bottom left corner but balance is not showing new funds still

## selsta | 2022-05-06T14:09:29+00:00
Ok, go to Settings -> Info, click on "(Change)" next to Wallet restore height and then click on okay twice, without changing anything. That will result in a full rescan and hopefully your funds show up.

Also can you please confirm that it says "Account #0" in the top left corner? Different accounts have different balances and transaction history so I want to make sure that you didn't select a different one accidentally.

## anon74652393854769423587 | 2022-05-06T14:19:31+00:00
Success! Thank you so much for your prompt and noob-friendly help :)

## selsta | 2022-05-06T14:21:24+00:00
Great. Make sure to stay connected to the remote node in advanced mode then everything should work fine in the future.

# Action History
- Created by: anon74652393854769423587 | 2022-05-06T13:21:38+00:00
- Closed at: 2022-05-06T14:21:24+00:00
