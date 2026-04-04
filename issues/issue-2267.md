---
title: Transaction history date filter incorrect.
source_url: https://github.com/monero-project/monero-gui/issues/2267
author: kwukduck
assignees: []
labels: []
created_at: '2019-07-04T15:17:06+00:00'
updated_at: '2019-08-14T20:52:28+00:00'
type: issue
status: closed
closed_at: '2019-08-14T20:52:28+00:00'
---

# Original Description
The date filter on the transaction history does not filter on date correctly. I just made a transaction 2019/07/04 but it does not show up when the date range is set to 2019/07/04 ~ 2019/07/05. However, when i set it to 2019/07/03 ~ 2019/07/05 it shows up just fine, and the date on the transaction is also correctly shown as 2019/07/04. Very strange.

# Discussion History
## kwukduck | 2019-07-04T16:04:22+00:00
This could possibly be a time-zone thing.
I did another transaction and it does show up. So now i have 2 transactions on 2019/07/04 of which only one (the most recent) shows up when the filter is set to 2019/07/04 ~ 2019/07/05, for the other one to show as well i need to set it one day earlier.

# Action History
- Created by: kwukduck | 2019-07-04T15:17:06+00:00
- Closed at: 2019-08-14T20:52:28+00:00
