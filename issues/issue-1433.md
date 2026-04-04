---
title: History page becomes unresponsive when too much txs
source_url: https://github.com/monero-project/monero-gui/issues/1433
author: Lafudoci
assignees: []
labels:
- enhancement
- resolved
created_at: '2018-05-28T11:05:07+00:00'
updated_at: '2019-04-24T12:45:42+00:00'
type: issue
status: closed
closed_at: '2019-04-24T12:45:42+00:00'
---

# Original Description
I have a stagenet wallet with countless received txs. Clicking on history page freezes the whole GUI program.  I believe it's caused by displaying too much txs. The default behavior is that the history list shows all txs at opening. Maybe we could just show the last few txs and have "load more" or "next page"?

# Discussion History
## sanderfoobar | 2018-05-28T11:56:42+00:00
You are correct, that page should be paginated. Could you estimate how many txs that wallet has?

+enhancement 
+bug

## Lafudoci | 2018-05-28T12:03:46+00:00
There might be about 7000 txs.

## selsta | 2019-04-24T12:21:41+00:00
#2025 

+resolved

# Action History
- Created by: Lafudoci | 2018-05-28T11:05:07+00:00
- Closed at: 2019-04-24T12:45:42+00:00
