---
title: Sometimes new transaction is stuck on local node, doesn't propagate to network
source_url: https://github.com/monero-project/monero/issues/2183
author: urza
assignees: []
labels: []
created_at: '2017-07-20T19:08:08+00:00'
updated_at: '2017-08-15T20:18:13+00:00'
type: issue
status: closed
closed_at: '2017-08-15T20:18:13+00:00'
---

# Original Description
Hello,
we found small issue, that occurs only very occasionally.
I saw this twice, first it happened to me few weeks ago, today it happened to a friend:

Using latest release of cli-wallet and monerod on linux (ubuntu).
Create new transaction (without payment id, but that is probably not relevant) via standard command "transfer" in CLI wallet with monerod running locally. Everything seems ok, but the transaction is not propagated to network, even after hours.

Show transfer in wallet shows this transaction as "failed".

Attached screenshots from today (excuse the censorship:) - you can see the tx id
56d812fd2ff819238ecc119fb63b9f91b6cf1c4032ec5a9a129b68e7693e2794
and search blockchain explorers, it is not in blockchain.

![xmr1](https://user-images.githubusercontent.com/189804/28434198-c5e6bfea-6d8e-11e7-91f9-30493ccba6ef.jpg)
![xmr2](https://user-images.githubusercontent.com/189804/28434200-c6054776-6d8e-11e7-85f9-bff156d4fa03.jpg)

What helps is this (thanks to dEBRUYNE  for help)

1.  on daemon "flush_txpool"
2.  on wallet "rescan_spend"
3.  balance will be returned to sender's wallet and he can sent money again

I can only speculate what is the reason for this behaviour. The result is that the new transaction does not propagate to network.

It would be great if the daemon could detect this and try to re-upload the transaction again. Or at least warn the user.

Thank you for your good work.

# Discussion History
## moneromooo-monero | 2017-07-22T12:42:07+00:00
The user was warned, since you say: Show transfer in wallet shows this transaction as "failed".
Tranactions are re-relayed after two hours (and every two hours for half a day IIRC).
You'd need to run a second daemon with log level 1 to see why it rejects that tx.

## urza | 2017-07-22T14:18:28+00:00
After discussion on IRC, easy solution to implement and solve the issue is probably to change the message "Money sent successfully" to something that indicates that the transaction was created and submitted to daemon, but wasn't necessarily propagated to network.

I propose this message: 

> "Transaction submitted to daemon successfully. You can check transaction status by 'show_transfers' command."

## moneromooo-monero | 2017-08-15T20:12:31+00:00
+resolved

# Action History
- Created by: urza | 2017-07-20T19:08:08+00:00
- Closed at: 2017-08-15T20:18:13+00:00
