---
title: wallet2::balance -> m_light_wallet_unlocked_balance, wallet2::unlocked_balance
  -> m_light_wallet_balance O_o
source_url: https://github.com/monero-project/monero/issues/7627
author: mahnunchik
assignees: []
labels: []
created_at: '2021-03-24T13:39:38+00:00'
updated_at: '2021-04-06T18:23:57+00:00'
type: issue
status: closed
closed_at: '2021-04-06T18:23:57+00:00'
---

# Original Description
`wallet2::balance` method returns `m_light_wallet_unlocked_balance` and `wallet2::unlocked_balance` returns `m_light_wallet_balance` when `m_light_wallet` is true.

It seems values should be swapped.

https://github.com/monero-project/monero/blob/v0.17.1.9/src/wallet/wallet2.cpp#L5967-L5995

# Discussion History
## moneromooo-monero | 2021-03-25T09:34:25+00:00
Indeed, thanks. Fixed in https://github.com/monero-project/monero/pull/7635

# Action History
- Created by: mahnunchik | 2021-03-24T13:39:38+00:00
- Closed at: 2021-04-06T18:23:57+00:00
