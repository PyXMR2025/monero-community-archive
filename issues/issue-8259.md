---
title: log rotation managed by system
source_url: https://github.com/monero-project/monero/issues/8259
author: BebeSparkelSparkel
assignees: []
labels: []
created_at: '2022-04-13T21:54:50+00:00'
updated_at: '2022-05-29T15:32:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, I am using the system to manage log rotation. It switches the log but monero does not use the new file handle. Is there a a way to signal monerod that the log file has changed and needs to update the file handle?

Many daemons use -HUP or -USR1 signals. Is this supported? If not, can it be added?

# Discussion History
## trasherdk | 2022-04-19T07:12:18+00:00
Use [logrotate](https://linux.die.net/man/8/logrotate) with `copytruncate`
```
Truncate the original log file in place after creating a copy, instead of moving the old log file and optionally creating a new one.
It can be used when some program cannot be told to close its logfile and thus might continue writing (appending) to the previous log file forever.
Note that there is a very small time slice between copying the file and truncating it, so some logging data might be lost.
When this option is used, the create option will have no effect, as the old log file stays in place. 
```

## BebeSparkelSparkel | 2022-04-19T12:02:45+00:00
@trasherdk OpenBSD does not have the `copytruncate` function. I was talking with some devs and they said that `copytruncate` was a legacy method and thus not included.

## trasherdk | 2022-04-22T09:00:24+00:00
@BebeSparkelSparkel I have no idea how BSD's work.
I'm on Slackware, and it doesn't get more legacy than that :laughing: 

# Action History
- Created by: BebeSparkelSparkel | 2022-04-13T21:54:50+00:00
