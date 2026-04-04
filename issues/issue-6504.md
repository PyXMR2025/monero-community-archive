---
title: Entering invalid password prints std::exception
source_url: https://github.com/monero-project/monero/issues/6504
author: selsta
assignees: []
labels: []
created_at: '2020-05-04T17:48:23+00:00'
updated_at: '2020-05-07T15:43:48+00:00'
type: issue
status: closed
closed_at: '2020-05-07T15:43:48+00:00'
---

# Original Description
Original bug report that got closed: #6496

When entering a wrong password it prints `std::exception` instead of `invalid password`.

```
selsta@mbpR ~/d/m/b/D/m/r/bin (master)> ./monero-wallet-cli --wallet-file ~/selsta.keys
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Carbon Chamaeleon' (v0.15.0.0-8185054db)
Logging to ./monero-wallet-cli.log
Wallet password: 
Error: failed to load wallet: std::exception
```

# Discussion History
# Action History
- Created by: selsta | 2020-05-04T17:48:23+00:00
- Closed at: 2020-05-07T15:43:48+00:00
