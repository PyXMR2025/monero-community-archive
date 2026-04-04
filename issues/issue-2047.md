---
title: '[Feature proposal] Warn user when a tx with low fee is being submitted while
  the mempool is busy'
source_url: https://github.com/monero-project/monero/issues/2047
author: kenshi84
assignees: []
labels: []
created_at: '2017-05-25T09:42:27+00:00'
updated_at: '2017-09-20T19:30:27+00:00'
type: issue
status: closed
closed_at: '2017-09-20T19:30:27+00:00'
---

# Original Description
I enjoy the low priority fee setting as it allows me to transact privately at an incredibly low cost. However, it sometimes screws me up when I use XMR.TO to pay in BTC for an order that expires relatively quickly (like in an hour) while the mempool is very busy; my BTC payment order expired before my XMR transfer was confirmed and XMR.TO finished the exchange. What I should've done instead is to check the current status of the mempool and increase the fee accordingly, which I think is quite cumbersome to do especially for causal users.

So, here's my feature proposal: the wallet would show a warning message when the user is about to submit a transaction with the low fee setting while the mempool is busy.

I'm not sure yet how it should be implemented (e.g., how to define the notion of the 'busyness' of the mempool), though.
Any thoughts?

# Discussion History
## kenshi84 | 2017-05-26T01:48:50+00:00
An alternative idea: the wallet would automatically choose the best fee setting for every transfer depending on the current state of the mempool (i.e. use high fee when the mempool is busy, otherwise use low fee).

## binaryFate | 2017-06-25T19:03:35+00:00
Just looking at the mempool to judge likelihood of a tx with given fee to go through would probably work OK right now. But it is not very sound long term, as miners can mine transactions that are not broadcast publicly (for instance they have special deals with pools or exchanges). 

The only reliable metric is to look at the fees of transactions mined in the N recent blocks: this is what Bitcoin core is doing by the way, where based on the recent blocks you can specify a number of block "I want my transaction mined within 3 blocks" and the software tells you what fees to use for this.

I am not advocating to follow that road necessarily, just that mempool by itself is non-reliable data. (But for non-critical stuff like just issuing a warning that might be perfectly ok for some years...).

## hyc | 2017-09-20T19:28:49+00:00
This was added in PR #2362 
+resolved

# Action History
- Created by: kenshi84 | 2017-05-25T09:42:27+00:00
- Closed at: 2017-09-20T19:30:27+00:00
