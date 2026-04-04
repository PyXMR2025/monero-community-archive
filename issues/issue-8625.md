---
title: Validation of `export_outputs` pagination parameters
source_url: https://github.com/monero-project/monero/issues/8625
author: evercraze
assignees: []
labels: []
created_at: '2022-10-25T08:33:33+00:00'
updated_at: '2022-11-02T07:24:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[Undocumented](https://github.com/monero-project/monero/blob/master/src/wallet/wallet_rpc_server.cpp#L2795) pagination params (`start`, `count`) in `export_outputs` are not verified and may produce a runtime error with edge values.

In particular, when the `start` value is higher than the total output count.
```
curl http://xxx/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"export_outputs", "params": {"all": true, "start": 50, "count": 5}}' -H 'Content-Type: application/json'
```

The response from the monero is following:
```json
{
  "error": {
    "code": -1,
    "message": "vector::reserve"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

The error occurs during output vector preparation on [wallet2.cpp#L13271](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L13271).

# Discussion History
## plowsof | 2022-10-30T13:48:08+00:00
are we meant to verify that ourselves? or should it be caught and return an error message for this case?  the test is checking for == here (which would miss this edge case, but surely the logic in our loops wouldn't pass it these wrong params anyway)  https://github.com/monero-project/monero/commit/0cbf5571d3ccd07c81d33b05dd23b2ac9c777c3b#diff-94a7c03c6f20df0978f9f76505f75d4115fccfc83875ad2b88f4d5280226fbebR108 @moneromooo-monero 

## evercraze | 2022-11-02T07:24:57+00:00
I believe it's a good practice to verify and sanitise input parameters rather than throwing runtime error that could *potentially* affect the wallet state.

# Action History
- Created by: evercraze | 2022-10-25T08:33:33+00:00
