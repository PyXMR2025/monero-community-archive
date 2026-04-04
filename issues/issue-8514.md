---
title: set-daemon command not referenced in initialization message
source_url: https://github.com/monero-project/monero/issues/8514
author: dscotese
assignees: []
labels: []
created_at: '2022-08-17T17:50:30+00:00'
updated_at: '2022-10-05T15:46:34+00:00'
type: issue
status: closed
closed_at: '2022-10-05T15:46:34+00:00'
---

# Original Description
"This is the command line monero wallet. It needs to connect to a monero daemon to work correctly."
This is a frustrating error because it doesn't provide any advice.  It should be revised to:
"This is the command line monero wallet. Use set-daemon to connect to a monero
daemon to work correctly."

# Discussion History
## moneromooo-monero | 2022-08-19T17:06:43+00:00
It is not an error. It always prints that. For most people, they will not have to use set_daemon, the wallet will use the local daemon.

There is a reference to set_daemon in the actual error message:

> Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.


## dscotese | 2022-10-05T15:46:34+00:00
RTFL, in addition to RTFM.  Understood. Closing for that reason.

# Action History
- Created by: dscotese | 2022-08-17T17:50:30+00:00
- Closed at: 2022-10-05T15:46:34+00:00
