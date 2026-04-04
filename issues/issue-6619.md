---
title: Update unbound dependency
source_url: https://github.com/monero-project/monero/issues/6619
author: MaxXor
assignees: []
labels: []
created_at: '2020-06-02T11:38:53+00:00'
updated_at: '2021-09-09T19:13:06+00:00'
type: issue
status: closed
closed_at: '2021-09-09T19:13:06+00:00'
---

# Original Description
The [in-tree unbound dependency](https://github.com/monero-project/unbound) is several releases behind the [upstream unbound repository](https://github.com/NLnetLabs/unbound). I've tried to submit a PR myself but git rebase and merge commits are failing because of the diverged commit history of the monero unbound and the original unbound branch.

# Discussion History
## moneromooo-monero | 2020-06-02T11:50:36+00:00
I made one (#6230) a while back. It needs someone with write access to push -f though.

## sanderfoobar | 2020-09-07T14:39:23+00:00
Better yet; perhaps we can get rid of the in-tree unbound and follow upstream. AFAIK. @anonimal ported it in because there was the idea that unbound were too slow with their updates ... and now we are too slow following them.

# Action History
- Created by: MaxXor | 2020-06-02T11:38:53+00:00
- Closed at: 2021-09-09T19:13:06+00:00
