---
title: archiving log files
source_url: https://github.com/monero-project/monero/issues/8219
author: BebeSparkelSparkel
assignees: []
labels: []
created_at: '2022-03-15T02:52:08+00:00'
updated_at: '2022-03-15T15:57:38+00:00'
type: issue
status: closed
closed_at: '2022-03-15T09:23:08+00:00'
---

# Original Description
I have noticed that some daemons are sent a signal when their log files are being swapped out and archived.

Does monerod require a signal or something else when log archiver is running to keep it from crashing?

# Discussion History
## trasherdk | 2022-03-15T06:15:51+00:00
I have in `/etc/logrotate.d/monero`
```
/var/lib/monero/data/mainnet/logs/*.log {
        notifempty
        weekly
        rotate 4
        missingok
        copytruncate
}
```

## BebeSparkelSparkel | 2022-03-15T15:57:38+00:00
Thanks. I'll have to see if my OpenBSD has an equivalent to `copytruncate`

# Action History
- Created by: BebeSparkelSparkel | 2022-03-15T02:52:08+00:00
- Closed at: 2022-03-15T09:23:08+00:00
