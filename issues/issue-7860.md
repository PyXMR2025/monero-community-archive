---
title: --offline option not respected when creating wallet from json
source_url: https://github.com/monero-project/monero/issues/7860
author: NikEyX
assignees: []
labels: []
created_at: '2021-08-13T16:24:30+00:00'
updated_at: '2021-08-13T16:24:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`monero-wallet-cli --generate-from-json test.json --offline`
will create the wallet, but break with this error:
```
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
```

`--offline` should respect the fact that I don't want to refresh the wallet at that point and exit or at the minimum not raise an error.

# Discussion History
# Action History
- Created by: NikEyX | 2021-08-13T16:24:30+00:00
