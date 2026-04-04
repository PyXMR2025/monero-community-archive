---
title: Set max log size for daemon
source_url: https://github.com/monero-project/monero/issues/2321
author: smccloud
assignees: []
labels:
- easy
created_at: '2017-08-21T18:20:30+00:00'
updated_at: '2017-09-25T21:06:21+00:00'
type: issue
status: closed
closed_at: '2017-09-25T21:06:21+00:00'
---

# Original Description
I would love the ability to set a max log size for the daemon on my machine.  I have it installed as a Windows service, but I do not want to have to stop it and restart it every so often just to clear out the log file.

# Discussion History
## moneromooo-monero | 2017-08-21T18:31:10+00:00
Log files are rotated every 100 MB. You can then auto remove the log files with the same name with an extra -* suffix (ie, instead ~/.bitmonero/bitmonero.log-* or wherever it is on windows).


## moneromooo-monero | 2017-08-26T19:56:17+00:00
+easy

## moneromooo-monero | 2017-09-25T21:02:17+00:00
+resolved

# Action History
- Created by: smccloud | 2017-08-21T18:20:30+00:00
- Closed at: 2017-09-25T21:06:21+00:00
