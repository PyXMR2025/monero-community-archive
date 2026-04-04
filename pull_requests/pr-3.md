---
title: Wizard path 1 according specifications
source_url: https://github.com/monero-project/monero-gui/pull/3
author: mbg033
assignees: []
labels: []
created_at: '2016-01-26T07:40:16+00:00'
updated_at: '2016-01-27T13:56:42+00:00'
type: pull_request
status: merged
closed_at: '2016-01-27T13:56:42+00:00'
merged_at: '2016-01-27T13:56:42+00:00'
---

# Original Description
Implemented "wizard path 1" with following exceptions:
- settings is not saved to any file actually, only in runtime object
- "password strength" indicator is statically initialized and doesn't depend on actual password
- there's no "disabled" state for "next" button, currently button just hidden if something preventing to go to next page.


# Discussion History
# Action History
- Created by: mbg033 | 2016-01-26T07:40:16+00:00
- Merged at: 2016-01-27T13:56:42+00:00
