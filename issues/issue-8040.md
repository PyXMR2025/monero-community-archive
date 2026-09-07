---
title: flow that allows assigning unique ids to payments
source_url: https://github.com/monero-project/monero/issues/8040
author: anycolo
assignees: []
labels: []
created_at: '2021-11-03T13:55:46+00:00'
updated_at: '2026-09-05T18:57:23+00:00'
type: issue
status: closed
closed_at: '2026-09-05T18:57:23+00:00'
---

# Original Description
Let's assume the following:
I have a monero rpc wallet. I select an address and an amount and i try to make the payment via a http call. The network fails at that point, and i'm not sure if the payment succeeded.
There should be a way to specify a transaction description, and if the monero wallets sees that transaction description twice, it will refuse the second payment.
I can't be the only one who lost money doing this.

# Discussion History
## selsta | 2022-02-18T23:35:05+00:00
Can you explain what you mean with the network fails? At what point does it fail?

## anycolo | 2022-02-19T05:42:38+00:00
The http call fails. You send the request, the monero rpc processes it, but the response doesn't get back to you, because of a packet loss, or because your internet connection fails at that exact moment.

## selsta | 2026-09-05T18:57:23+00:00
This can be handled by creating the transaction with `do_not_relay: true` and `get_tx_metadata: true`, persisting the returned transaction metadata, and then using `relay_tx`.

If the `relay_tx` HTTP response is lost, the same transaction metadata can simply be submitted again, which does not create a second payment.

# Action History
- Created by: anycolo | 2021-11-03T13:55:46+00:00
- Closed at: 2026-09-05T18:57:23+00:00
