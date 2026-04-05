---
title: '[BUG] node failed to verify FCMP++ proof'
source_url: https://github.com/seraphis-migration/monero/issues/46
author: j-berman
assignees: []
labels: []
created_at: '2025-05-16T01:14:59+00:00'
updated_at: '2025-10-03T16:29:47+00:00'
type: issue
status: closed
closed_at: '2025-10-03T16:29:47+00:00'
---

# Original Description
Reported by @ComputeryPony ([link](https://github.com/seraphis-migration/monero/pull/32#issuecomment-2878515641)):

> Ah, and another, I had previously tested sending FCMP++ transactions from the GUI using this patch and it worked but now I get an error when attempting to send from the GUI.

```
Couldn't send the money: transaction <ae980cc1f8f6ea40976a458cd84b8725ae0bcbe0754e889d679d1dbdb6aa3d36> was rejected by daemon with status: Failed. Reason: invalid input
```

and in the console of the GUI:

```
E daemon_send_resp.status != CORE_RPC_STATUS_OK. THROW EXCEPTION: error::tx_rejected
```

and in the node it was connected to:

```
E Failed to verify FCMP++ proof
```
_____

Haven't repro'd this on the latest. Keeping this open as a tracking issue.

# Discussion History
## j-berman | 2025-10-03T16:29:47+00:00
https://github.com/seraphis-migration/monero/issues/45#issuecomment-3358729383

# Action History
- Created by: j-berman | 2025-05-16T01:14:59+00:00
- Closed at: 2025-10-03T16:29:47+00:00
