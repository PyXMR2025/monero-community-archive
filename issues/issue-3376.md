---
title: 'Windows 10: memory mapped db file eats 11GB of physical RAM'
source_url: https://github.com/monero-project/monero-gui/issues/3376
author: tidux
assignees: []
labels: []
created_at: '2021-04-04T23:09:26+00:00'
updated_at: '2021-05-12T18:21:18+00:00'
type: issue
status: closed
closed_at: '2021-05-12T18:21:18+00:00'
---

# Original Description
Is there any way I can change this behavior of the local node?  My system is swapping for nearly everything else and it makes my PC borderline unusable.

# Discussion History
## selsta | 2021-05-08T15:05:59+00:00
Is this during sync or also afterwards?

## tidux | 2021-05-12T18:19:18+00:00
This was during sync.

## selsta | 2021-05-12T18:21:18+00:00
It should not be an issue afterwards. Sync is resource intensive. Closing as there isn't much we can do here on the GUI side (we already have reduced the concurrency for GUI users).

# Action History
- Created by: tidux | 2021-04-04T23:09:26+00:00
- Closed at: 2021-05-12T18:21:18+00:00
