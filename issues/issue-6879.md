---
title: The "failed to find tx meta" bug or feature
source_url: https://github.com/monero-project/monero/issues/6879
author: trurebel
assignees: []
labels: []
created_at: '2020-10-12T13:22:16+00:00'
updated_at: '2020-10-15T22:34:51+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:34:51+00:00'
---

# Original Description
Googling for this error message made me believe I might have corrupted my (newly synced) DB, so I did a couple of resyncs from scratch on Ubuntu and Windows, no improvements. Then I realized the meta message was connected to me starting solo mining. Then Google took me to this other issue where a comment suggested the "meta" is connected to pruned databases. I did not prune mine but maybe my peers are pruned? Anyway, the rate of this notification alone could crash the computer, that's what it feels like, and would jam up the log if it ends up in any log. I don't think the defaults here are sane, and that would be my second most requested feature, to somehow clean this up, after my first requested feature, a "monerod --pruned" that syncs from scratch in a pruned state.

# Discussion History
## moneromooo-monero | 2020-10-12T13:32:30+00:00
It's unrelated to pruning, it's a minor bug that is harmless in practice, you can ignore it. Your blockchain is most likely just fine.

## moneromooo-monero | 2020-10-12T13:43:26+00:00
https://github.com/monero-project/monero/pull/6880 silences it for now.

# Action History
- Created by: trurebel | 2020-10-12T13:22:16+00:00
- Closed at: 2020-10-15T22:34:51+00:00
