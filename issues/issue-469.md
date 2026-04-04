---
title: Mining with 0 h/s should be prevented
source_url: https://github.com/monero-project/monero-gui/issues/469
author: medusadigital
assignees: []
labels: []
created_at: '2017-02-11T21:23:59+00:00'
updated_at: '2017-03-03T14:27:11+00:00'
type: issue
status: closed
closed_at: '2017-03-03T14:27:11+00:00'
---

# Original Description
In the mining Tab, there is the Field <threads>, which is optional. But if its left empty the miner will start mining with 0 h/s.

To prevent this, monero-wallet.-gui should behave like monero-wallet-cli and start mining with 1 thread, if there is no value in field <threads>

# Discussion History
# Action History
- Created by: medusadigital | 2017-02-11T21:23:59+00:00
- Closed at: 2017-03-03T14:27:11+00:00
