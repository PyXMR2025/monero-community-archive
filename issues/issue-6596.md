---
title: daemon rpc `relay_tx` returning code 0, blank message
source_url: https://github.com/monero-project/monero/issues/6596
author: woodser
assignees: []
labels: []
created_at: '2020-05-27T16:05:23+00:00'
updated_at: '2020-07-08T22:58:15+00:00'
type: issue
status: closed
closed_at: '2020-07-08T22:58:15+00:00'
---

# Original Description
Since updating to v0.16.0.0, this response is returned from daemon rpc `relay_tx`: `{error={code=0, message=}, id=0, jsonrpc=2.0}`

It works when the daemon is switched back to v0.15.0.5.

# Discussion History
## moneromooo-monero | 2020-05-28T11:34:15+00:00
https://github.com/monero-project/monero/pull/6599

## moneromooo-monero | 2020-07-08T22:58:15+00:00
Merged

# Action History
- Created by: woodser | 2020-05-27T16:05:23+00:00
- Closed at: 2020-07-08T22:58:15+00:00
