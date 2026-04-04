---
title: Prevent --block-notify while syncing
source_url: https://github.com/monero-project/monero/issues/6317
author: 00-matt
assignees: []
labels: []
created_at: '2020-02-06T09:50:22+00:00'
updated_at: '2020-02-06T12:29:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, is there a way to prevent the `--block-notify` command from firing while the daemon is still syncing? It currently overwhelms my poor message queue.

# Discussion History
## Gingeropolous | 2020-02-06T12:29:43+00:00
i mean, obviously this would be a good feature / modification to include. But in the meantime, just don't use the flag during the initial sync. 

# Action History
- Created by: 00-matt | 2020-02-06T09:50:22+00:00
