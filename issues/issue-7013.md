---
title: 'Wallet started with --offline option showing "Error: wallet failed to connect
  to daemon"'
source_url: https://github.com/monero-project/monero/issues/7013
author: jonathancross
assignees: []
labels: []
created_at: '2020-11-11T16:16:55+00:00'
updated_at: '2022-02-19T01:05:09+00:00'
type: issue
status: closed
closed_at: '2022-02-19T01:05:09+00:00'
---

# Original Description
When starting the v0.17.1.1 wallet on an offline system, I am seeing this confusing error message despite using the `--offline` option:
```
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Background refresh thread started
```

# Discussion History
## moneromooo-monero | 2020-12-10T17:57:45+00:00
https://github.com/monero-project/monero/pull/7113

# Action History
- Created by: jonathancross | 2020-11-11T16:16:55+00:00
- Closed at: 2022-02-19T01:05:09+00:00
