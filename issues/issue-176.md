---
title: Handle inbound connection pings.
source_url: https://github.com/Cuprate/cuprate/issues/176
author: Boog900
assignees: []
labels:
- A-p2p
- C-bug
- E-easy
created_at: '2024-06-19T18:42:01+00:00'
updated_at: '2024-09-09T22:12:07+00:00'
type: issue
status: closed
closed_at: '2024-09-09T22:12:07+00:00'
---

# Original Description
Currently if we don't have an available permits for inbound connections we drop the connection completely, we should wait to see if the connection just wanted to send us a ping to see if we are reachable.

Here is where this should happen:

https://github.com/Cuprate/cuprate/blob/4653ac58849c81b6ab993a1d23f061a97962524b/p2p/p2p/src/inbound_server.rs#L106

We spawn a separate task to wait for the first message to see if it is a ping, then respond if it is and close the connection.

We should also limit the number of concurrent pings to 2 and we should also have a reasonable timeout so we are not waiting for too long.

# Discussion History
# Action History
- Created by: Boog900 | 2024-06-19T18:42:01+00:00
- Closed at: 2024-09-09T22:12:07+00:00
