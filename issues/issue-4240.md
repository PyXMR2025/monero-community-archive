---
title: GUI hangs if `monerod` cannot bind
source_url: https://github.com/monero-project/monero-gui/issues/4240
author: hinto-janai
assignees: []
labels: []
created_at: '2023-11-07T15:55:25+00:00'
updated_at: '2023-11-13T20:13:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When starting `monero-wallet-gui` and starting a local node, it will hang with no indication/error/log if `monerod` itself cannot bind, e.g:
```
2023-11-07 17:44:20.109	E ZMQ bind failed: Address already in use
2023-11-07 17:44:20.121	E Exception in main! Failed to add TCP socket(127.0.0.1:18082) to ZMQ RPC Server
```

## Reproduce
1. Start something on ZMQ/RPC port
2. Start `monero-wallet-gui` and launch local node
3. `monero-wallet-gui` hangs forever attempting to launch `monerod` which cannot bind

![image](https://github.com/monero-project/monero-gui/assets/101352116/e6b1b5f4-4028-4477-bfc5-80e3ba6b3f04)

Something could be logged if `monerod` exits with non-zero.

# Discussion History
## plowsof | 2023-11-12T23:22:20+00:00
after 120 seconds i get a notification that the daemon failed to start. does this scenario fool the checks? (i bound an rpc wallet to 18083 and launched monerod in from the gui with `--zmq-pub tcp://127.0.0.1:18083` )

## hinto-janai | 2023-11-13T20:13:58+00:00
Interesting - if that flag (or any flag I'm assuming) is passed, it will properly error:

![image](https://github.com/monero-project/monero-gui/assets/101352116/68270e53-ff7b-480b-83d3-a200ff65dbc2)

This doesn't happen without a flag though, port blocked with no flag will hang forever - maybe this error should be copy+pasted here. I'll try fixing this later.

# Action History
- Created by: hinto-janai | 2023-11-07T15:55:25+00:00
