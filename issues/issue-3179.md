---
title: Waiting Confirmation
source_url: https://github.com/monero-project/monero-gui/issues/3179
author: userlip
assignees: []
labels: []
created_at: '2020-10-18T12:43:00+00:00'
updated_at: '2020-10-20T07:31:22+00:00'
type: issue
status: closed
closed_at: '2020-10-20T07:31:22+00:00'
---

# Original Description
I am using the latest Wallet version and this morning I tried to make a transaction that is now stuck at "Waiting Confirmation"
I was using my local node, but also tried it using the XMR.to Node, no changes still.

Also the Transaction appears in the "Transaction" Tab but disappears from there after 30 to 40 seconds.

GUI Version: 0.17.1.0-cb1f3ad

Also: I do not want this transaction to go through anymore as I already made the payment, do I need to do something? (I am scared that the transaction will go through if the bug is fixed)

# Discussion History
## selsta | 2020-10-18T12:47:55+00:00
What is the output of "status" if you enter it on Settings -> Log?

## userlip | 2020-10-18T12:54:12+00:00
`>>> status
[18.10.2020 14:53] 2020-10-18 12:53:37.017 I Monero 'Oxygen Orion' (v0.17.1.0-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081`

## selsta | 2020-10-18T12:56:00+00:00
Is this with local node running or connected to remote node?

## userlip | 2020-10-18T12:57:22+00:00
I now have it connected to the remote node of XMR.to as mentioned in this comment https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706480292

But at the time of the creation of the transaction I was running everything locally

## userlip | 2020-10-20T07:31:22+00:00
Version 0.17.1.1 of the Wallet now shows the Transaction as failed

# Action History
- Created by: userlip | 2020-10-18T12:43:00+00:00
- Closed at: 2020-10-20T07:31:22+00:00
