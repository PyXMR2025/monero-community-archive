---
title: Sending to a standard address without specifying a payment ID still gives prompt
  about using subaddress instead of encrypted payment ID
source_url: https://github.com/monero-project/monero/issues/6523
author: sethforprivacy
assignees: []
labels: []
created_at: '2020-05-12T20:40:01+00:00'
updated_at: '2020-07-19T18:18:41+00:00'
type: issue
status: closed
closed_at: '2020-07-19T18:18:41+00:00'
---

# Original Description
When sending from monero-wallet-cli to any non-subaddress, and not specifying a payment ID of any kind, once the transaction is confirmed monero-wallet-cli warns the user with the following text:

`NOTE: this transaction uses an encrypted payment ID: consider using subaddresses instead`

This text shouldn't appear when not specifying a payment ID, AFAICT.

# Discussion History
## sethforprivacy | 2020-05-12T20:49:27+00:00
I also tested this with another external 4-address and got the same response upon confirmation of the Tx.

## erciccione | 2020-05-13T09:59:05+00:00
AFAIK all transactions have a dummy encrypted payment ID now. Could that be the reason for the warning?

## selsta | 2020-05-13T10:00:06+00:00
It should not trigger on a dummy PID.

## sethforprivacy | 2020-05-13T12:16:27+00:00
Yeah, I figured it's being *caused* by the dummy PID, but doesn't seem like that's intended behavior.
@moneromooo-monero made a patch that I'll try to test out today: https://github.com/moneromooo-monero/bitmonero/commit/a90e9bf4cfed3e126751e0c6ec65deacda065d41

## moneromooo-monero | 2020-05-13T13:59:47+00:00
https://github.com/monero-project/monero/pull/6527

It was triggering on change, since you can't decrypt it as it's encrypted to the recipient so it could not tell it was a dummy one.

## moneromooo-monero | 2020-06-01T11:51:47+00:00
Should be fixed now. Hopefully no special cases left.

# Action History
- Created by: sethforprivacy | 2020-05-12T20:40:01+00:00
- Closed at: 2020-07-19T18:18:41+00:00
