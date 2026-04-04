---
title: Amount includes the fee as well, when transaction is in mempool
source_url: https://github.com/monero-project/monero-gui/issues/651
author: peanutsformonkeys
assignees: []
labels:
- resolved
created_at: '2017-03-30T20:56:01+00:00'
updated_at: '2018-11-18T13:27:28+00:00'
type: issue
status: closed
closed_at: '2018-11-18T13:27:28+00:00'
---

# Original Description
I noticed that when I sent 1 XMR, and wanted to check on the History page, that the Amount also includes the fee, thus:

* Amount: `1.020432720000`
* Fee: `0.020432720000`

For a moment, I thought I had made a mistake … But then, after the transaction was confirmed, the Amount reverted to `1.000000000000`. This seems like counter-intuitive to me, at least I can't think of a reason why we would do that? I suppose most people will be confused. In this case, it was relatively easy to understand because I had sent a round number. If that were not the case, I guess some people will briefly panic.

I reproduced it today with Beta 2 on testnet, by sending 5 XMR, to illustrate what I described above. Before confirmation ("Pending"):

<img width="691" alt="testnet-pending-red" src="https://cloud.githubusercontent.com/assets/21346321/24525752/d1cf8fda-159b-11e7-9794-392b9781d50c.png">

After confirmation:

<img width="691" alt="testnet-confirmed" src="https://cloud.githubusercontent.com/assets/21346321/24525764/dffac052-159b-11e7-82a8-6a2636329497.png">

I suppose this is a bug, and unintentional?

# Discussion History
## ghost | 2017-03-31T00:40:06+00:00
Same as #580

## erciccione | 2018-11-18T13:25:51+00:00
+resolved

# Action History
- Created by: peanutsformonkeys | 2017-03-30T20:56:01+00:00
- Closed at: 2018-11-18T13:27:28+00:00
