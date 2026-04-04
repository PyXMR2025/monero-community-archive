---
title: 'monero-wallet-cli: transfer sent to myself shows as one outgoing tx with the
  amount sent'
source_url: https://github.com/monero-project/monero/issues/1401
author: JollyMort
assignees: []
labels: []
created_at: '2016-12-04T17:47:17+00:00'
updated_at: '2017-08-25T21:19:34+00:00'
type: issue
status: closed
closed_at: '2017-08-25T21:19:29+00:00'
---

# Original Description
Built from this: https://github.com/monero-project/monero/commit/c36cb5434059ed53daf947b189343ac0bd8f31d8 on Lubuntu 16.04 x64.

When sending `<amount>` back to the same wallet which made the tx and when running `show_transfers` command afterwards, the `show_transfer` command shows as if the `<amount>` had been sent away and out of the wallet. It shows just one `out` with the `<amount>`.

However, when loading the same wallet into v0.10.0, instead of an `out` with the `<amount>`, it shows an `out` of 0.00000 which is more reasonable as the net change was 0 (- the fee).

Both show the same balance, though.

# Discussion History
## JollyMort | 2017-08-25T21:19:29+00:00
i think this was fixed in the meantime, somewhere somehow

# Action History
- Created by: JollyMort | 2016-12-04T17:47:17+00:00
- Closed at: 2017-08-25T21:19:29+00:00
