---
title: When rebuilding wallet cache from seed, Fee shows up as Max Amount.
source_url: https://github.com/monero-project/monero/issues/1289
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-02T15:59:20+00:00'
updated_at: '2016-11-05T09:24:00+00:00'
type: issue
status: closed
closed_at: '2016-11-05T09:24:00+00:00'
---

# Original Description
When rebuilding wallet cache from seed, Fees can shows up as Max Amount. This affects nearly all Outgoing transactions, Old and New. Affects GUI and CLI, tested with version v0.10.0.0-b06c1ab and below.

How to reproduce: 

- restore any wallet from seed that contains outgoing transactions

# Discussion History
## medusadigital | 2016-11-03T18:15:06+00:00
issue is resolved here: https://github.com/moneromooo-monero/bitmonero/tree/amount_out


## medusadigital | 2016-11-05T09:24:00+00:00
https://github.com/monero-project/monero/pull/1295 is merged.

works ---> closed


# Action History
- Created by: medusadigital | 2016-11-02T15:59:20+00:00
- Closed at: 2016-11-05T09:24:00+00:00
