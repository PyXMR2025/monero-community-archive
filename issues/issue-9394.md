---
title: 'Failed to sign unsigned tx: Hot wallets cannot import outputs'
source_url: https://github.com/monero-project/monero/issues/9394
author: jack-dot-wu
assignees: []
labels:
- question
created_at: '2024-07-08T03:39:01+00:00'
updated_at: '2024-07-10T19:21:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I use the only-view wallet to get the unsigned_txset with api transfer_split. And use the normal wallet to sign the unsigned_txset, but it show '{'code': -42, 'message': 'Failed to sign unsigned tx: Hot wallets cannot import outputs'}'.what is the cold wallet. How to create it?


# Discussion History
## selsta | 2024-07-10T19:21:17+00:00
It means that this wallet has been used together with an online node before. A cold wallet has to be created on an offline system.

# Action History
- Created by: jack-dot-wu | 2024-07-08T03:39:01+00:00
