---
title: 'ux p2pool: enable ''start mining'' if user inputs remote host flags'
source_url: https://github.com/monero-project/monero-gui/issues/4093
author: plowsof
assignees: []
labels: []
created_at: '2023-01-01T03:50:20+00:00'
updated_at: '2023-01-01T03:50:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
we don't need to be connected to a local/remote node to start mining. if user enters these p2pool flags: `--host node.monerodevs.org --rpc-port 18089 --zmq-port 18084`, "start mining" should be possible.

clicking on "start mining" should grab the values currently inside the startup flags box (currently you have to stop/start for the new values to be used)

There is also no 'error: p2pool failed to start' screen (if user supplies bad arguments or the host ^ is offline / something else goes wrong.

# Discussion History
# Action History
- Created by: plowsof | 2023-01-01T03:50:20+00:00
