---
title: Transaction filter not updating results
source_url: https://github.com/monero-project/monero-gui/issues/2266
author: kwukduck
assignees: []
labels: []
created_at: '2019-07-04T15:16:02+00:00'
updated_at: '2019-07-04T15:35:16+00:00'
type: issue
status: closed
closed_at: '2019-07-04T15:34:41+00:00'
---

# Original Description
When searching it will keep showing the last result(s) matching the filter that had a match, even if the current entry has no matches. (eg, i have a transaction of 1, 2, 3, 4 and 5 xmr. Then search for 2, it will show only 2 (as it should), now continue typing, add a 1 to the filter, so '21', it will still show the 2 xmr as a match, while there are no actual matches.
The results list should be empty.

# Discussion History
## kwukduck | 2019-07-04T15:35:15+00:00
Not an issue.

# Action History
- Created by: kwukduck | 2019-07-04T15:16:02+00:00
- Closed at: 2019-07-04T15:34:41+00:00
