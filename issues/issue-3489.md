---
title: Stuck pending transaction in gui wallet v. 0.17.2.0
source_url: https://github.com/monero-project/monero-gui/issues/3489
author: ghost
assignees: []
labels: []
created_at: '2021-05-19T15:56:39+00:00'
updated_at: '2022-08-16T16:24:00+00:00'
type: issue
status: closed
closed_at: '2021-05-25T03:30:01+00:00'
---

# Original Description
I sent a transaction to a valid Monero subaddress using my GUI wallet. Here is some basic device information:

OS: Ubuntu 20.04.2 Focoal Fossa, 5.8.0-53-generic
Monero GUI wallet version: 0.17.2.0

I have a transaction that hasn't been picked up by a miner after one hour. Is there a manner in which I can cancel this transaction in the GUI wallet? The transaction ID is not present in blockchair or exploremonero. Please let me know. Thanks.

# Discussion History
## ghost | 2021-05-19T16:16:01+00:00
I've rechecked the wallet and my local node. THe local node is fully synced. Transaction is still stuck in a "pending" state.

## selsta | 2021-05-19T16:17:15+00:00
You can go to Settings -> Log and type `relay_tx txid` to relay the transaction again.

To abort the transaction enter `flush_txpool txid`

## ghost | 2021-05-19T16:30:31+00:00
Flushing the txid worked. Thanks.

Sent from ProtonMail mobile

-------- Original Message --------
On May 19, 2021, 12:17 PM, selsta wrote:

> You can go to Settings -> Log and type relay_tx txid to relay the transaction again.
>
> To abort the transaction enter flush_txpool txid
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/3489#issuecomment-844258177), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/APMCUJAO34U3BYLHND2AUPTTOPQB7ANCNFSM45E7KAQQ).

# Action History
- Created by: ghost | 2021-05-19T15:56:39+00:00
- Closed at: 2021-05-25T03:30:01+00:00
