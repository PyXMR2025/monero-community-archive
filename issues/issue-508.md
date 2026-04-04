---
title: Daemon crashed after error "BDB4531 transaction has active cursors"
source_url: https://github.com/monero-project/monero/issues/508
author: osensei
assignees: []
labels: []
created_at: '2015-11-28T20:39:11+00:00'
updated_at: '2017-08-08T11:24:15+00:00'
type: issue
status: closed
closed_at: '2017-08-08T11:24:15+00:00'
---

# Original Description
The daemon had been running for almost 3 days on my RPi2 with current master's HEAD (4061a32082554f3b18429b85b35398469b061faa) when it crashed with the following output:

```
BDB4531 transaction has active cursors 
BDB0061 PANIC: Invalid argument 
Segmentation fault (core dumped)
```


# Discussion History
## moneromooo-monero | 2017-08-08T11:13:29+00:00
Berkeley DB support is now removed as LMDB supports all our targets.

+resolved

# Action History
- Created by: osensei | 2015-11-28T20:39:11+00:00
- Closed at: 2017-08-08T11:24:15+00:00
