---
title: Transaction not appearing in GUI Wallet.
source_url: https://github.com/monero-project/monero/issues/3641
author: tobyaj
assignees: []
labels: []
created_at: '2018-04-15T10:24:00+00:00'
updated_at: '2018-04-15T15:32:24+00:00'
type: issue
status: closed
closed_at: '2018-04-15T15:32:24+00:00'
---

# Original Description
Hi I'm wondering if anyone can help. Last week on the day of the monero update i sent a payment to changelly of litecoin to recieve monero at first the transaction failed because of the update( I think) and then a couple days later after being in contact with changelly customer service they said the payment had now been completed. However the payment hasn't appeared in my monero gui wallet, i'm using a remote node and I followed a guide changing the name of the file. to do full restart and resync but still nothing.I've followed another guide and confirmed i can see both the failed and completed transactions on the block chain but they're not in my wallet. I've signed into mymonero with the same key but the balance reads 0 on there too. I can pay 0.1XMR to import my transactions but i'm hesitant to pay as I'm unsure that will help. Any advice would be great, Changelly customer services can see the transaction so nothing else they can do. My block creation height is 0.

# Discussion History
## moneromooo-monero | 2018-04-15T10:42:01+00:00
What version of monero tools are you using ? If < 0.12.0.0, then you're forked off and need to fix this (https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-as-a-result).

## tobyaj | 2018-04-15T13:33:49+00:00
I've been advised that this wont help if i  using a remote-node? I am on version 12 though, 

## moneromooo-monero | 2018-04-15T14:00:12+00:00
If you mean a third party's node, then you can't do that of course. You'd need *them* to do it. But you want to run your own node if you can. More security (both directly and indirectly), privacy (also directly and indirectly).

## tobyaj | 2018-04-15T15:32:24+00:00
Through another forum I was advised to do the below and it worked! Problem solved. 

Change the remote node to node.moneroworld.com with port 18089

Click in another empty box (on the Settings page) to ensure your settings are properly saved.

Change the Wallet creation height to 1548000

The GUI wallet will now perform a new refresh.


# Action History
- Created by: tobyaj | 2018-04-15T10:24:00+00:00
- Closed at: 2018-04-15T15:32:24+00:00
