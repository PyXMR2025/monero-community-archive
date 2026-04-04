---
title: Monero Spendable Outputs
source_url: https://github.com/monero-project/monero/issues/6254
author: YasserNoureldin
assignees: []
labels: []
created_at: '2019-12-19T10:50:47+00:00'
updated_at: '2020-05-16T16:03:00+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:02:59+00:00'
---

# Original Description
As far as i understood about the spendable outputs is that if I receive 5 XMR in a transaction then i have one spendable output and i can make one transaction with this 5 XMRs that will be locked untill the transaction is confirmed, And if i receive the 5 XMR in 5 different transactions where each is 1 XMR then i will 5 spendable outputs and i can make 5 transactions where 1 XMR will be locked per transaction, am I right?

The case now for me is That I have two wallets (A and B) .. wallet (A) has 9 XMR and wallet (B) is empty, I sent from A to B 14 transactions where each is 0.1 XMR, now as i understand and explained above .. In wallet (B) I have a balance of 1.4 XMR and 14 spendable outputs and I can make 14 transactions where each will be locking 0.1 XMR per transaction.

This is not what happens, now when I am trying to send back from Wallet (B) to wallet (A) transactions where each is 0.01 XMR, I can only send 7 transactions where each transaction os locking 0.2 XMR of the balance not 0.1 XMR.
Can you please help me unerstand the concept of spendable outputs if there is something I don't clearly understand?

# Discussion History
## moneromooo-monero | 2019-12-19T11:47:15+00:00
You are more or less correct, but the wallet will usually try to include two inputs in a transaction, explaining your 0.2 case above. You can tweak the min-output-count and min-output-value settings in the wallet, which control when this behaviour happens. The wallet will try to keep at least min-output-count outputs of value at least min-output-value. So if you set count/value to, say, 100, 0.01, the wallet will do what you were expecting (using one output per tx).

## moneromooo-monero | 2020-05-16T16:02:59+00:00
No bug here.

# Action History
- Created by: YasserNoureldin | 2019-12-19T10:50:47+00:00
- Closed at: 2020-05-16T16:02:59+00:00
