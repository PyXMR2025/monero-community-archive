---
title: 'Failed to commit a transaction to the db: File too large'
source_url: https://github.com/monero-project/monero/issues/8634
author: dawiepoolman
assignees: []
labels: []
created_at: '2022-11-13T09:48:37+00:00'
updated_at: '2022-11-13T10:40:30+00:00'
type: issue
status: closed
closed_at: '2022-11-13T10:40:30+00:00'
---

# Original Description
Hi guys

testing out a new NVMe on another RockPro64.  Formatted etx4 I get this error:

2022-11-13 09:43:53.972 I Synced 58924/2754766 (2%, 2695842 left)
2022-11-13 09:43:54.422 W Failed to commit a transaction to the db: File too large
2022-11-13 09:43:54.424 E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: File too large

any ideas?

# Discussion History
## dawiepoolman | 2022-11-13T10:40:30+00:00
..and what do you know, I have set the cpu governor = powersave as I did previously and it is running stable so far:
https://github.com/monero-project/monero/issues/8473

this makes it the second RockPro64 I got with the same vulnerability.

# Action History
- Created by: dawiepoolman | 2022-11-13T09:48:37+00:00
- Closed at: 2022-11-13T10:40:30+00:00
