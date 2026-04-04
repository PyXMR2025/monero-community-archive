---
title: Monero transferred funds haven't arrived
source_url: https://github.com/monero-project/monero/issues/8399
author: davidbroomhead
assignees: []
labels: []
created_at: '2022-06-22T16:07:27+00:00'
updated_at: '2022-06-22T17:08:26+00:00'
type: issue
status: closed
closed_at: '2022-06-22T17:08:01+00:00'
---

# Original Description
Hi there - I transferred funds from one GUI wallet to another, but the funds haven't arrived. The outgoing transaction from the first wallet is showing as there & present, but the incoming wallet is still showing as 'no transactions yet'. When I checked both the outgoing & incoming wallet IDs at wallet.mymonero.com, they are both showing as empty & 'no transactions yet'.

I rebuilt both wallets following the instructions in this post:

https://monero.stackexchange.com/questions/6649/transaction-stuck-as-pending-in-the-gui

But this did not fix the situation. 

The outgoing transaction is definitely showing the correct address, but that receiving address is showing as 'no transactions yet'.

Is there anything else I can try, or are the funds lost? 

# Discussion History
## selsta | 2022-06-22T17:02:30+00:00
Which software did you use for the sending and the receiving wallet? Monero GUI or MyMonero?

## davidbroomhead | 2022-06-22T17:05:02+00:00
It was Monero GUI wallet

## selsta | 2022-06-22T17:08:01+00:00
Please open an issue here: https://github.com/monero-project/monero-gui/issues

Also add the version you are using, add the transaction id from the missing transaction, and the wallet restore height (you can find it on Settings -> Info page).

## davidbroomhead | 2022-06-22T17:08:26+00:00
Thanks - will do


# Action History
- Created by: davidbroomhead | 2022-06-22T16:07:27+00:00
- Closed at: 2022-06-22T17:08:01+00:00
