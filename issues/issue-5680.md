---
title: Clarification on if  --prune-blockchain is required permanently
source_url: https://github.com/monero-project/monero/issues/5680
author: BKdilse
assignees: []
labels:
- invalid
created_at: '2019-06-20T18:23:08+00:00'
updated_at: '2019-06-20T18:33:40+00:00'
type: issue
status: closed
closed_at: '2019-06-20T18:33:40+00:00'
---

# Original Description
Please clarify if the switch  `--prune-blockchain` is required on Daemon start up each time, after the database has already been pruned?

I've read that you must use the switch each time the monerd is restarted, else future blocks will not be pruned. I've also read else where, that it is a one time requirement.

Which is it please?

# Discussion History
## moneromooo-monero | 2019-06-20T18:31:51+00:00
It's a one time thing. Once pruned, it stays pruned as it syncs.

+invalid


# Action History
- Created by: BKdilse | 2019-06-20T18:23:08+00:00
- Closed at: 2019-06-20T18:33:40+00:00
