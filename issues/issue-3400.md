---
title: 'Documentation: add daemon-job-timeout'
source_url: https://github.com/xmrig/xmrig/issues/3400
author: koitsu
assignees: []
labels:
- bug
created_at: '2024-01-14T23:15:42+00:00'
updated_at: '2024-01-25T02:49:44+00:00'
type: issue
status: closed
closed_at: '2024-01-25T02:49:44+00:00'
---

# Original Description
Two simple things to fix:

* The `--daemon-job-timeout` flag is missing from https://xmrig.com/docs/miner/command-line-options  (but it is visible via `--help`)
* The `daemon-job-timeout` parameter is missing from https://xmrig.com/docs/miner/config/pool (please be sure to note that the value is in milliseconds and defaults to 15000)

Thanks SChernykh!

# Discussion History
## xmrig | 2024-01-16T17:35:02+00:00
Done. Other missing options also added: `--daemon-zmq-port=N`, `"spend-secret-key"`, `"sni"`, `"daemon-zmq-port"`.
Thank you.





## koitsu | 2024-01-25T02:49:44+00:00
Looks great. Thanks SChernykh!

# Action History
- Created by: koitsu | 2024-01-14T23:15:42+00:00
- Closed at: 2024-01-25T02:49:44+00:00
