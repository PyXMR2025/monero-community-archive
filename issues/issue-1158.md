---
title: Enable always-confirm-transfers by default in monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/1158
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2016-10-01T08:18:32+00:00'
updated_at: '2016-12-15T17:09:26+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:09:26+00:00'
---

# Original Description
I think there's a strong case to made for having `always-confirm-transfers` enabled by default in monero-wallet-cli. Currently, any newly created wallet has it disabled:

```
[wallet 4*****]: set
...
always-confirm-transfers = 0
```

There are a few of **scenarios with financial loss** that could be prevented by having this `always-confirm-transfers` setting enabled by default:
- Copy & paste mistakes: Preparing a transfer command in a text editor, sending the transaction (paste), and then later, pasting the clipboard contents another time by accident in the terminal with the opened wallet.
- Constructing a transfer command in the opened wallet, but inadvertedly omitting the payment ID at the end, e.g. because there was a newline included when pasting the amount value. The transaction gets sent without payment ID, and normally the money is unrecoverable. There was a recent [discussion on reddit](https://www.reddit.com/r/Monero/comments/555wjy/xmrto_problems/) about this type of accident. A number of people seemed to favor having the confirmation enabled by default.

In addition, it is also helpful to know the transaction fee upfront. I can sometimes vary wildly.


# Discussion History
## ghost | 2016-10-23T18:24:26+00:00
#1225


# Action History
- Created by: peanutsformonkeys | 2016-10-01T08:18:32+00:00
- Closed at: 2016-12-15T17:09:26+00:00
