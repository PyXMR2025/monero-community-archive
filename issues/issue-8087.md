---
title: 'Privacy improvement: warn if one transaction sent by another includes >1 output
  to the wallet'
source_url: https://github.com/monero-project/monero/issues/8087
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-11-26T20:36:46+00:00'
updated_at: '2021-11-26T20:36:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Related to https://git.featherwallet.org/feather/feather/issues/385

Conditions for the warning (all must be true):

* The transaction is not initiated by the user (eg: churn, change)
* The transaction has >1 output destined for the wallet

Background:

There are some legitimate reasons to receive multiple outputs in the same transaction, but this should be only expected in situations where the recipient expects this. Receiving multiple outputs in individual transactions results in a heightened risk of poisoned outputs tracing.

Clarifications:

* The warning should be provided regardless of receiving address(es), so long as >1 output is received by the same mnemonic seed

Warning:

> You received 2+ outputs in the same transaction. If this is unexpected, proceed with extreme caution as the sender may be trying to track you. It's strongly recommended to churn each of these outputs individually, and for you to research poisoned outputs if you have a strict threat model.

Bonus points:

* Have a one-click button to churn each output individually, but timing remains an unsolved issue

# Discussion History
# Action History
- Created by: SamsungGalaxyPlayer | 2021-11-26T20:36:46+00:00
