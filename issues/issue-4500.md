---
title: monero-wallet-rpc returns incorrect balances and omits transactions when sending
  to/from the same account
source_url: https://github.com/monero-project/monero/issues/4500
author: woodser
assignees: []
labels: []
created_at: '2018-10-04T19:42:38+00:00'
updated_at: '2019-01-09T08:55:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue may be reproduced by sending a transaction from account 0 to account 0 of the same wallet.

Before the transaction has confirmed:

- `get_transfers` does not return the transaction which should be type "pool".
- `get_accounts` and `get_balance` return incorrect balances.

After the transaction has confirmed:

- `get_accounts` and `get_balance` return the correct balances.
- `get_transfers` does not return the transaction which should be type "incoming".

Similar results are seen if sending e.g. from account 1 to account 0.

# Discussion History
## woodser | 2018-10-04T19:46:10+00:00
This issue entails #4428.

## moneromooo-monero | 2018-10-05T12:47:26+00:00
The transfer is of type pending (on the sending wallet). I confirm it does not show up in get_transfers while in the pool. 

getbalance returns the balance with the sent money subtracted, it'll be added when the tx is received.
After mining, I do see the tx (type out), and the balance is correct.

So the only problem here seems to be get_transfer not seeing pool/pending txes.

## woodser | 2018-10-05T13:08:20+00:00
Outgoing transactions are immediately deducted from the balance before being confirmed.  Is it not possible to have mempool transactions immediately added to the balance before being confirmed?  That would go a long way for the user experience to have mempool funds immediately added to the wallet balance.  In conjunction with the get_transfers fix, it will also ensure the balance == total incoming payments including what's in the mempool.

## woodser | 2018-10-05T13:12:11+00:00
Also I believe that confirmed incoming transactions do not return from get_transfers, in addition to unconfirmed incoming transactions, when sent to/from the same account, especially account 0.

## moneromooo-monero | 2018-10-05T13:34:46+00:00
It is possible, but not really wanted. There is no guarantee the tx will confirm.

About your last comment, are you *really really sure* the tx is missing, and not seen as out as before ?

## moneromooo-monero | 2018-10-05T13:37:00+00:00
It looks like the subaddresses patch broke the pool txes being seen by the wallet. Weird we didn't see that before.

## moneromooo-monero | 2018-10-05T13:41:14+00:00
Only for wallet to same wallet. Not sure we care much then.

Maybe that whole thing needs an overhaul. A lot of it is arbitrary anyway.


## woodser | 2018-10-05T14:17:38+00:00
I confirmed that "in" and "pool" transactions are missing from get_transfers when a payment is sent from account 0 to account 0.  They return as expected when sending from account 1 to account 0.  Unfortunately it is impossible to collect some fields from the affected transactions such as fee, timestamp, unlock_time, is_double_spend, height, and confirmations because these fields are only returned from get_transfers.

Edit:
>"and not see as out as before"

The "out" does appear in get_transfers, just not the "pool" or "in" counterpart when sent to/from account 0.

## woodser | 2018-10-05T14:17:45+00:00
Regarding mempool transactions being reflected in the balance, I think the same logic should apply to both pending and mempool transactions since neither are guaranteed to confirm.  Otherwise, it creates a lopsided balance where only outgoing pending transactions are deducted.  Crediting the balance with unconfirmed transactions is more inline with user expectation/intuition that the balance increases when an incoming transaction is detected even if the funds are not immediately spendable, which the unlocked balance represents.  It is also consistent with almost every other wallet.

## thestick613 | 2019-01-09T08:55:11+00:00
Sending a transaction from a monero wallet to the same monero wallet using a payment_id, with `make_integrated_address`, as described in this issue, will not show that transaction in `get_transfers in`. The same transaction appears in `get_transfers out`, but with an `payment_id` of `0000000000000000`. The transaction is not found when searching for it with 'get_payments' using the original payment_id.

How am i supposed to find that transaction?

# Action History
- Created by: woodser | 2018-10-04T19:42:38+00:00
