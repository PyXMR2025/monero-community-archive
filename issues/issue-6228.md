---
title: E Transaction spends at least one output which is too young
source_url: https://github.com/monero-project/monero/issues/6228
author: ghost
assignees: []
labels: []
created_at: '2019-12-12T17:52:18+00:00'
updated_at: '2020-05-17T14:39:11+00:00'
type: issue
status: closed
closed_at: '2020-05-17T14:39:10+00:00'
---

# Original Description
since the fork monerod kicks out this error from time to time - FYI

2019-12-12 17:47:33.038	E Transaction spends at least one output which is too young


# Discussion History
## moneromooo-monero | 2019-12-12T17:58:38+00:00
Is it one of your transactions (ie, when you send one) ?

## ghost | 2019-12-12T18:06:07+00:00
I don't think it is - I have no transactions roughly 3 days or so but the daemon kicks out that message every few hours.

## moneromooo-monero | 2019-12-12T18:14:46+00:00
Then it's someone sending a bad tx, and if your node is still syncing fine, you can ignore it.

## moneromooo-monero | 2020-05-17T14:39:10+00:00
No bug here. Reopen if you think there is, with more info.


# Action History
- Created by: ghost | 2019-12-12T17:52:18+00:00
- Closed at: 2020-05-17T14:39:10+00:00
