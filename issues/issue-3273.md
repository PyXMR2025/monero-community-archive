---
title: Stuck at Creating Transaction
source_url: https://github.com/monero-project/monero-gui/issues/3273
author: vitormilagres1992
assignees: []
labels: []
created_at: '2020-12-16T12:59:07+00:00'
updated_at: '2021-01-15T11:00:36+00:00'
type: issue
status: closed
closed_at: '2021-01-15T11:00:36+00:00'
---

# Original Description
Hi, I am trying to send my funds to another wallet and I get stuck at the CREATING TRANSACTION step. It keeps loading, but never creates the transaction. I am having the same issue with my software wallet on my laptop and also with my hardware ledger wallet. Both of them using the Monero-GUI interface

I am running the latest version of the software, that is monero-gui-v0.17.1.7. I have just upgraded the firmware on my ledger and updated the apps. Still the same issue

# Discussion History
## selsta | 2020-12-16T12:59:51+00:00
Did you accept it on your Ledger?

## vitormilagres1992 | 2020-12-16T13:01:22+00:00
> Did you accept it on your Ledger?

It never asked for anything on my ledger. I even have this issue with the software wallet saved on my computer

## selsta | 2020-12-16T13:02:53+00:00
Which node are you using?

## vitormilagres1992 | 2020-12-16T13:34:02+00:00
I tried to use my own node, but apparently it did not work. Then i moved to a public node and it worked just fine. I have no clue as to why my node is not running properly, I do not have anything different to run my node, like startup flags or something that could make me mess up easily. I just click on LOCAL NODE and then START DAEMON. My wallet syncs up perfectly, but I cannot send transactions.

## selsta | 2020-12-16T13:35:20+00:00
This might help for local node: https://www.reddit.com/r/Monero/comments/kdqj5i/running_01717_worked_at_first_without_ban_list/gfy1x01/?context=3

## xiphon | 2021-01-15T11:00:36+00:00
Resolved in v0.17.1.9.

# Action History
- Created by: vitormilagres1992 | 2020-12-16T12:59:07+00:00
- Closed at: 2021-01-15T11:00:36+00:00
