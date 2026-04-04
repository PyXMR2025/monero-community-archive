---
title: bg-mining-miner-target does not seem to get applied.
source_url: https://github.com/monero-project/monero/issues/6604
author: ronohara
assignees: []
labels: []
created_at: '2020-05-31T11:21:20+00:00'
updated_at: '2020-10-15T22:43:05+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:43:05+00:00'
---

# Original Description
2020-05-31 11:21:52.016	I Monero 'Nitrogen Nebula' (v0.16.0.0-release)


With this in the .conf file:

bg-mining-enable=1
bg-mining-ignore-battery=1
bg-mining-miner-target=65
mining-threads=8

mining_status shows..

Smart mining enabled:
  Target: 40% CPU
  Idle threshold: 90% CPU
  Min idle time: 10 seconds
  Ignore battery: yes

The miner Target is the default value, not the parameter setting.



# Discussion History
## moneromooo-monero | 2020-05-31T12:37:44+00:00
https://github.com/monero-project/monero/pull/6607

# Action History
- Created by: ronohara | 2020-05-31T11:21:20+00:00
- Closed at: 2020-10-15T22:43:05+00:00
