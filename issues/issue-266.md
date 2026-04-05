---
title: Daemon gets killed by OOM killer while syncing FCMP blocks
source_url: https://github.com/seraphis-migration/monero/issues/266
author: stianov
assignees: []
labels: []
created_at: '2025-12-13T15:40:00+00:00'
updated_at: '2025-12-13T18:11:59+00:00'
type: issue
status: closed
closed_at: '2025-12-13T18:11:59+00:00'
---

# Original Description
This might be related to this: https://github.com/seraphis-migration/monero/issues/202

However, I have some more details. I started synchronizing a FCMP stressnet node yesterday from scratch and when I came back it had been killed by the OOM killer (This is Linux, Fedora 43 x64). This happened right after it started syncing blocks from the FCMP fork. It had not had any memory issues before this. It takes about 10 minutes of syncing FCMP blocks until the memory has grown to 10 GB. If I start the node over again, it picks up from where it left off and the memory balloons again and it gets killed after 15 minutes.

I can reproduce this issue on my machine, so please tell me if I can contribute anything or provide more details.

(Just because it's correlated to syncing FCMP blocks doesn't necessarily mean that that is the catalyst, although it is likely)

# Discussion History
## stianov | 2025-12-13T15:43:28+00:00
It seems that this is identical to this: https://github.com/seraphis-migration/monero/issues/147

So it should probably be closed as duplicate

## nahuhh | 2025-12-13T16:22:11+00:00
You can build this branch https://github.com/j-berman/monero/tree/test-fcmp%2B%2B-alpha-stressnet

which should prevent OOMs

## stianov | 2025-12-13T18:11:59+00:00
That worked, thank you!

# Action History
- Created by: stianov | 2025-12-13T15:40:00+00:00
- Closed at: 2025-12-13T18:11:59+00:00
