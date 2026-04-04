---
title: daemon rpc get_peer_list returns uninitialized values for every peer
source_url: https://github.com/monero-project/monero/issues/5093
author: woodser
assignees: []
labels: []
created_at: '2019-01-24T19:52:05+00:00'
updated_at: '2019-01-30T15:17:35+00:00'
type: issue
status: closed
closed_at: '2019-01-30T15:17:35+00:00'
---

# Original Description
Daemon RPC's `get_peer_list` returns the following for every peer under `gray_list` and `white_list`:

`{ host: '<none>', id: 0, ip: 0, last_seen: 0, port: 0 }`

Method: POST
URI: http://localhost:38081/get_peer_list

The daemon being tested was updated from master yesterday and it works as expected on a previous build from 12/18.

# Discussion History
## moneromooo-monero | 2019-01-24T20:37:23+00:00
https://github.com/monero-project/monero/pull/5094

## moneromooo-monero | 2019-01-30T15:12:50+00:00
The code got rewritten in the meantime.

+resolved


# Action History
- Created by: woodser | 2019-01-24T19:52:05+00:00
- Closed at: 2019-01-30T15:17:35+00:00
