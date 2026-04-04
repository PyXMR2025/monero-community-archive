---
title: monero-wallet-rcp should check on startup if it can bind to the specified --rpc-bind-port
source_url: https://github.com/monero-project/monero/issues/6855
author: thestick613
assignees: []
labels: []
created_at: '2020-10-01T20:45:19+00:00'
updated_at: '2020-10-02T19:20:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monero-wallet-rpc will start up, check for old transaction, and after all of that finally tries to bind to the --rpc-bind-port. If it can't do so, it crashes.

```
2020-10-01 20:39:23.930 E Failed to bind IPv4: bind: Permission denied
2020-10-01 20:39:23.931 F Error starting server: Failed to bind IPv4 (set to required)
2020-10-01 20:39:23.931 E Failed to bind server
2020-10-01 20:39:23.932 E Failed to initialize wallet RPC server
```

I think it should do that earlier on. What do you think?


# Discussion History
## moneromooo-monero | 2020-10-02T13:52:10+00:00
Can you include a stack trace for the crash ?
See "Debugging" in README.md for how to get one and set up cores.

## thestick613 | 2020-10-02T19:20:13+00:00
I used a wrong term. It doesn't crash, it just exits, but it's very frustrating, because the wallet loads all the previous transactions, which may take a few minutes, only to print an error and exit. I suggested testing the port before doing all that hard work.

# Action History
- Created by: thestick613 | 2020-10-01T20:45:19+00:00
