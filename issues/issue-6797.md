---
title: '[SUGGESTION] Use a minimum value for the restore height of Ledger and Trezor
  wallets. '
source_url: https://github.com/monero-project/monero/issues/6797
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2020-09-03T18:02:50+00:00'
updated_at: '2021-01-04T01:11:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Both Ledger and Trezor support has only been available in recent years (basically since mid 2018 (Ledger) and mid 2019 (Trezor)). As such, it is unlikely that any Ledger or Trezor Monero wallet will have transactions from before that date (barring an edge case where a user having converted a generic Monero seed into a Ledger or Trezor mnemonic seed). To improve user experience, we should consider setting a minimum value for the restore height of Ledger and Trezor wallets, especially given that the proposal of embedding a restore height in the mnemonic seed cannot be applied to Trezor and Ledger Monero wallets (since both use a different derivation scheme for the mnemonic seed). 

# Discussion History
## sethforprivacy | 2020-09-05T19:18:11+00:00
That's a great idea! Since it would be so rare to see users who have imported an older seed into their Ledger/Trezor, this would mitigate a lot of the potential painpoints experienced, especially as HW wallets are slower to sync.

## rating89us | 2020-09-06T13:46:24+00:00
We could further improve this by defining in Monero software the launch dates of each hardware wallet model.

Initially this would be useful for Ledger, which has two models that support Monero: Nano S and Nano X. Nano X is the newer  one and was released in May 2019. 

Trezor only supports Monero in Model T, and model One probably won't support Monero. But anyway defining the launch date in Monero software would still be useful to decrease scanning time of future Trezor models, not yet released.

## skorokithakis | 2021-01-04T01:10:38+00:00
I can see this being a major source of confusion for people who got a Nano X to replace their Nano S and used the same seed. If they don't pay attention, they'll miss a bunch of transactions, and I would rather err on the side of not missing transactions.

# Action History
- Created by: dEBRUYNE-1 | 2020-09-03T18:02:50+00:00
