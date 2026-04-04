---
title: wallet2 get_payments() min_height is exclusive
source_url: https://github.com/monero-project/monero/issues/5751
author: woodser
assignees: []
labels: []
created_at: '2019-07-14T14:38:35+00:00'
updated_at: '2019-07-14T14:41:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
wallet2 get_payments() and get_payments_out() use a min and max height parameter to filter results by a block range.

The min_height parameter is treated as exclusive (i.e. payments at that height are omitted) in wallet2.cpp [here](https://github.com/monero-project/monero/blob/fd3ff741644152ed559fcf79550435d3df75b764/src/wallet/wallet2.cpp#L5680), [here](https://github.com/monero-project/monero/blob/fd3ff741644152ed559fcf79550435d3df75b764/src/wallet/wallet2.cpp#L5693), and [here](https://github.com/monero-project/monero/blob/fd3ff741644152ed559fcf79550435d3df75b764/src/wallet/wallet2.cpp#L5693).

This issue requests the min_height parameter be treated as inclusive so payments at that height are returned.  Otherwise the client must offset the intended minimum bound by -1 to be consistent with typical range filtering.

# Discussion History
# Action History
- Created by: woodser | 2019-07-14T14:38:35+00:00
