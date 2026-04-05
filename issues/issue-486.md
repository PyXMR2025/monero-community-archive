---
title: Log when there are no incoming connections
source_url: https://github.com/Cuprate/cuprate/issues/486
author: hinto-janai
assignees: []
labels:
- C-request
- E-easy
- E-help-wanted
created_at: '2025-05-23T13:08:27+00:00'
updated_at: '2025-08-07T13:28:34+00:00'
type: issue
status: closed
closed_at: '2025-08-07T13:28:34+00:00'
---

# Original Description
## Feature
Occasionally log (with `WARN` level) when there are no incoming connections similar to `monerod`:
```
No incoming connections - check firewalls/routers allow port 18080
```

## How
The port formatted should use this variable:
https://github.com/Cuprate/cuprate/blob/ce7a04f2d964875a95530b4cb2cb9522f6fce2f4/binaries/cuprated/src/config/p2p.rs#L221

- `monerod` logs this every 1 hour
- The log could be skipped if `max_inbound_connections == 0` in the config

# Discussion History
# Action History
- Created by: hinto-janai | 2025-05-23T13:08:27+00:00
- Closed at: 2025-08-07T13:28:34+00:00
