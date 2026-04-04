---
title: '`make` top-level does not resume a failed compilation'
source_url: https://github.com/monero-project/monero/issues/6464
author: R030t1
assignees: []
labels: []
created_at: '2020-04-19T00:32:18+00:00'
updated_at: '2020-04-19T00:33:00+00:00'
type: issue
status: closed
closed_at: '2020-04-19T00:33:00+00:00'
---

# Original Description
Per title. Had a build fail due to OOM. Re-running the command seems to purge everything and restart. This should be left to a `dist-clean` or similar command.

# Discussion History
## R030t1 | 2020-04-19T00:33:00+00:00
Hmm, apologies, something weird went on with my previous build. The most recent attempt did not have this issue.

# Action History
- Created by: R030t1 | 2020-04-19T00:32:18+00:00
- Closed at: 2020-04-19T00:33:00+00:00
