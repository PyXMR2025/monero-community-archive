---
title: 'User experience: 5 - 1 = 4 but wallet2 reports the incorrect balance until
  the first confirmation'
source_url: https://github.com/monero-project/monero/issues/5809
author: woodser
assignees: []
labels: []
created_at: '2019-08-14T21:30:18+00:00'
updated_at: '2020-11-05T15:30:57+00:00'
type: issue
status: closed
closed_at: '2020-11-05T15:30:56+00:00'
---

# Original Description
This issue documents the user's expected experience of having X balance in their wallet, sending Y amount to an external address, then expecting to see X - Y - the transaction fee balance remaining.

Currently wallet2 reports the incorrect balance until the first confirmation.

For example, the user has 5 XMR in their wallet.  They send 1 XMR.  Then they expect to see a balance of 4 XMR remaining, but instead they will see some number between 0 and 4 until the first confirmation.

The issue is that when wallet2 creates and relays a transaction, it immediately subtracts from its balance outputs spent by the transaction ("vins"), but it does not add to its balance any new outputs created by the transaction ("vouts") which will become spendable by the wallet.  This includes change outputs and any transfers the user sends to their own wallet.

To provide the expected experience, wallet2 needs to include unconfirmed vouts which will become spendable to the wallet in its balance.

# Discussion History
## woodser | 2020-11-05T15:30:56+00:00
The balance is correct after sending funds (but does not include unconfirmed deposits).

# Action History
- Created by: woodser | 2019-08-14T21:30:18+00:00
- Closed at: 2020-11-05T15:30:56+00:00
