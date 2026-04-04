---
title: sweep_dust Transaction cannot pay for itself
source_url: https://github.com/monero-project/monero/issues/1525
author: got3nks
assignees: []
labels:
- invalid
created_at: '2017-01-04T13:11:27+00:00'
updated_at: '2017-10-15T18:48:21+00:00'
type: issue
status: closed
closed_at: '2017-10-15T18:48:21+00:00'
---

# Original Description
```
# curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sweep_dust"}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -4,
    "message": "Transaction cannot pay for itself"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

How do we fix this?

# Discussion History
## moneromooo-monero | 2017-01-04T14:51:11+00:00
Wait and hope Monero becomes valuable enough.

## ghost | 2017-01-04T23:32:59+00:00
How small is your dust?

## moneromooo-monero | 2017-10-15T18:33:38+00:00
No reply, and no indication that the sum of the dust is enough to pay for the fee, so I'm going to conclude it's working. Reopen if this is not the case.

+invalid

# Action History
- Created by: got3nks | 2017-01-04T13:11:27+00:00
- Closed at: 2017-10-15T18:48:21+00:00
