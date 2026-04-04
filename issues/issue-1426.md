---
title: 'Testnet: Wallet fails to update balance after blockchain rollback'
source_url: https://github.com/monero-project/monero/issues/1426
author: iDunk5400
assignees: []
labels: []
created_at: '2016-12-10T16:46:08+00:00'
updated_at: '2017-04-10T22:08:13+00:00'
type: issue
status: closed
closed_at: '2017-04-10T22:08:13+00:00'
---

# Original Description
Following the testnet blockchain (deep) rollback after #1413 was merged, monero-wallet-cli failed to update the balance of my testnet wallet during more than 24 hours that it's been left running. Running rescan_bc in the wallet corrected the balance.

# Discussion History
## ghost | 2016-12-24T23:53:52+00:00
@iDunk5400 Does #1497 fix this for you?

# Action History
- Created by: iDunk5400 | 2016-12-10T16:46:08+00:00
- Closed at: 2017-04-10T22:08:13+00:00
