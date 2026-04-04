---
title: Monero transferred funds haven't arrived
source_url: https://github.com/monero-project/monero-gui/issues/3950
author: davidbroomhead
assignees: []
labels: []
created_at: '2022-06-22T17:15:38+00:00'
updated_at: '2022-06-22T22:05:57+00:00'
type: issue
status: closed
closed_at: '2022-06-22T22:05:57+00:00'
---

# Original Description
Hi there - I transferred funds from one GUI wallet to another, but the funds haven't arrived. The outgoing transaction from the first wallet is showing as there & present, but the incoming wallet is still showing as 'no transactions yet'. When I checked both the outgoing & incoming wallet IDs at wallet.mymonero.com, they are both showing as empty & 'no transactions yet'.

I rebuilt both wallets following the instructions in this post:

https://monero.stackexchange.com/questions/6649/transaction-stuck-as-pending-in-the-gui

But this did not fix the situation.

The outgoing transaction is definitely showing the correct address, but that receiving address is showing as 'no transactions yet'.

Is there anything else I can try, or are the funds lost?

Monero GUI Wallet version: 0.17.3.2

Transaction ID: 223e1b3ef7f1dbf27afe77920430b9e86d5141a671c58032f34c42afcf0f4ba2

Wallet restore height: 2506948

# Discussion History
## selsta | 2022-06-22T17:25:42+00:00
Sorry, please also add which wallet mode you are using. It's also visible on Settings -> Info.

Your funds are not lost, we will just have to rescan them.

## davidbroomhead | 2022-06-22T17:43:39+00:00
Great thanks. Wallet mode is

Advanced mode (Remote node)

Remote node in use is 

node.moneroworld.com
18089

## selsta | 2022-06-22T17:53:56+00:00
Can you try to use this remote node instead?

address: `88.198.199.23`
port: `18081`

Other remote node in case the above has issues:

address: `node.supportxmr.com`
port: `18081`

address: `78.47.80.55`
port: `18081`

address: `node.community.rino.io`
port: `18081`

Afterwards please go to Settings -> Info, click on "(Change)" next to wallet restore height and press okay twice. It should do a rescan, this might take a while and your funds should show up.

## davidbroomhead | 2022-06-22T17:54:51+00:00
Ok I will do this - is this on both wallets, or just the receiving one


## selsta | 2022-06-22T17:58:43+00:00
just the receiving one

## davidbroomhead | 2022-06-22T17:59:54+00:00
Ok thanks, its just rebuilding now


## davidbroomhead | 2022-06-22T20:26:48+00:00
Hey there - the rebuild worked, I can see the funds! Thanks so much for your help!

# Action History
- Created by: davidbroomhead | 2022-06-22T17:15:38+00:00
- Closed at: 2022-06-22T22:05:57+00:00
