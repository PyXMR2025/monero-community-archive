---
title: Child monerod process keeps open fds from the wallet process
source_url: https://github.com/monero-project/monero-gui/issues/1676
author: moneromooo-monero
assignees: []
labels: []
created_at: '2018-10-17T10:28:30+00:00'
updated_at: '2018-10-17T10:36:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When running the daemon from the GUI, it keeps open fds, so it's currently keeping an fd to, eg, the wallet keys file (fixed in github).
It's hard to fix "generically" since this uses QProcess, which doesn't seem to have a way to close fds on execve.
And we don't have access to the child process before exec.
After the wallet keys file patch is merged, monerod will still have an open fd to the wallet log file, for instance.


# Discussion History
# Action History
- Created by: moneromooo-monero | 2018-10-17T10:28:30+00:00
