---
title: Is there a simple algorithm to convert Height <-> Date?
source_url: https://github.com/monero-project/monero/issues/9094
author: developergames2d
assignees: []
labels:
- question
- low priority
created_at: '2023-12-21T07:27:30+00:00'
updated_at: '2023-12-21T13:29:23+00:00'
type: issue
status: closed
closed_at: '2023-12-21T13:29:23+00:00'
---

# Original Description
Is there a simple algorithm to convert BlockHeight <-> BlockDate?

# Discussion History
## hyc | 2023-12-21T13:27:40+00:00
Converting height to date is trivial, just read the timestamp in the block.

Converting date to height takes more work, you can use wallet/wallet2.cpp:get_blockchain_height_by_date().

## selsta | 2023-12-21T13:29:23+00:00
https://github.com/monero-project/monero-gui/blob/master/js/Wizard.js#L134

Here is an algorithm for date to height.

# Action History
- Created by: developergames2d | 2023-12-21T07:27:30+00:00
- Closed at: 2023-12-21T13:29:23+00:00
