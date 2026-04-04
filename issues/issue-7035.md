---
title: Support on_unconfirmed_money_spent notifications in wallet2's callback listener
source_url: https://github.com/monero-project/monero/issues/7035
author: woodser
assignees: []
labels: []
created_at: '2020-11-21T16:37:15+00:00'
updated_at: '2020-11-21T16:37:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
wallet2's callback listener currently supports [on_unconfirmed_money_received](https://github.com/monero-project/monero/blob/83f1d863bd80e5e04c64dfa4d43edd132d1d21d2/src/wallet/wallet2.h#L141) which notifies when money is received and unconfirmed.

This issue requests adding support for a corresponding `on_unconfirmed_money_spent` which notifies when money is spent and unconfirmed.

# Discussion History
# Action History
- Created by: woodser | 2020-11-21T16:37:15+00:00
