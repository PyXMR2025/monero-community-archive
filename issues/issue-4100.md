---
title: '[Feature request] Add option to the wallet to set a higher number of rounds
  for the KDF'
source_url: https://github.com/monero-project/monero/issues/4100
author: garlicgambit
assignees: []
labels: []
created_at: '2018-07-05T22:10:48+00:00'
updated_at: '2018-09-04T23:08:52+00:00'
type: issue
status: closed
closed_at: '2018-09-04T23:08:52+00:00'
---

# Original Description
Please consider to add an option to the wallet to set a higher number of rounds for the KDF (key derivation function). Allow the user to only increase the number over the default value and configure it based in seconds.

Example:
```monero-wallet-cli --unlock-time 20```

This example would unlock the wallet after 20 seconds.

# Discussion History
## moneromooo-monero | 2018-07-05T23:02:07+00:00
Not based on time. It needs to be deterministic. But a custom multiplier can be done.

## stoffu | 2018-07-06T06:50:03+00:00
I've made a WIP #4103 which introduces a new flag `--kdf-rounds <N>`.

The practical problem with this code is that the heavy KDF computation gets triggered every time the user enters the wallet password (e.g. when making transfers and when changing wallet settings). This could be mitigated by caching the resulting encryption key, but I'm not sure if it's a good practice.


## MaxXor | 2018-07-06T16:41:44+00:00
Where is the current amount of rounds documented?

## moneromooo-monero | 2018-07-06T21:32:55+00:00
It is 1.


## moneromooo-monero | 2018-09-04T23:01:58+00:00
+resolved

# Action History
- Created by: garlicgambit | 2018-07-05T22:10:48+00:00
- Closed at: 2018-09-04T23:08:52+00:00
