---
title: 'fast_exit followed by exit resulted in "segmentation fault: 11"'
source_url: https://github.com/monero-project/monero/issues/592
author: sammy007
assignees: []
labels: []
created_at: '2016-01-02T08:38:45+00:00'
updated_at: '2016-12-15T18:10:40+00:00'
type: issue
status: closed
closed_at: '2016-12-15T18:10:40+00:00'
---

# Original Description
```
fast_exit
Daemon stopped
exit
2016-Jan-02... [node] Stop signal sent
...
Deinitializing rpc server...
```

Segmentation fault: 11

On El Capitan.


# Discussion History
## moneromooo-monero | 2016-02-06T12:29:01+00:00
I think we could just remove fast_exit now, since (1) there is no lengthy save op on exit anymore and (2) the wait-forever-on-network bug is fixed.

On Linux, fast_exit doesn't stop anyway, it seems to fail, and exit after that works fine.


# Action History
- Created by: sammy007 | 2016-01-02T08:38:45+00:00
- Closed at: 2016-12-15T18:10:40+00:00
