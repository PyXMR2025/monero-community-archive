---
title: Weird display when sending money to sub address in same wallet
source_url: https://github.com/monero-project/monero-gui/issues/2699
author: ar-
assignees: []
labels: []
created_at: '2020-01-06T11:53:40+00:00'
updated_at: '2020-01-07T17:05:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Sending money to myself doens't seem to be handled correctly or is at least displayed wrongly. Wrongly in different ways.

To reproduce:

1. Put some money into a wallet
2. Create a sub address
3. send funds to the sub address, for example 0.001
4. wait for 10 confirmations

Error 1:
The transaction list shows only one outgoing transaction of 0.001.

Expected behavior:
There should be 2 transactions visible. One outgoing of 0.001 and one incoming on the same block height, of the same amount, or maybe slightly reduces due to fees. So maybe 0.00995 incoming.

Error 2:
Create a view-only wallet of the wallet. Now there is an incoming (!!) transaction of 0.001 visible. And no outgoing transaction at all. Also there is another incoming transaction on the same block visible, but of a totally unrelated amount. In my case that is 0.003. Possibly mixed up with a previous transaction.

Expected behavior: 
Most importantly the display should be the same as in the non-view-only wallet. There are not 2 transactions on the same block, but they should correlate to the spending. So 1 incoming and 1 outgoing transactions on the same block while the incoming might be slightly lower. Also the display should not be mixed up with other transactions, like showing an unrelated much higher amount incoming on the same block.


# Discussion History
## rating89us | 2020-01-07T16:58:53+00:00
Error 1 is duplicate of issue #2185. 

While this behavior (displaying a single outgoing transaction) is the default in CLI wallet, I agree with @ar-, and I still believe that the GUI wallet should detect that this is a "churn" transaction and display 2 transactions in Transactions tab, one outgoing and one incoming, both on the same block height.

# Action History
- Created by: ar- | 2020-01-06T11:53:40+00:00
