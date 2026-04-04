---
title: transfer_split RPC call does not return info about amount in each transaction
source_url: https://github.com/monero-project/monero/issues/2120
author: binaryFate
assignees: []
labels: []
created_at: '2017-06-25T18:14:10+00:00'
updated_at: '2017-07-03T10:29:28+00:00'
type: issue
status: closed
closed_at: '2017-07-03T10:29:28+00:00'
---

# Original Description
When using `transfer_split` RPC, we know that all transactions together sent the amount requested. But we do not know from the RPC response how this whole amount is actually split per-transaction.
(Only the fees per transaction are returned). Knowing the per-transaction amount would be useful in several situations, it currently requires subsequent RPC calls which makes it cumbersome.

Example where this functionality would be useful: When you track your transactions with a local DB (common for any service) and send a bunch of txs sent via `transfer_split` to a counterparty such as an exchange, and you want to check the amount declared as "arrived" by this counterparty is actually correct with respect to what you have recorded locally in your DB. You cannot without knowing the actual amount to be received in each tx by the counterparty. A practical consequence of this: you send to an exchange such as poloniex, which suddenly stops confirming deposits for a day or two, and only a part of your transactions are confirmed: you have no way to know how many XMR are actually "missing" on your account since you do not know how many XMR are transferred in each tx.

It is not so much an issue for individual users that use the wallet (GUI or CLI) as this info can be trivially checked, but it is more complex when you run a service that relies purely on RPC and handles dozens or more of transactions a day. 

Note the `transfer` command does not suffer this as it only sends a single transaction that necessarily sends the exact amount requested.

# Discussion History
# Action History
- Created by: binaryFate | 2017-06-25T18:14:10+00:00
- Closed at: 2017-07-03T10:29:28+00:00
