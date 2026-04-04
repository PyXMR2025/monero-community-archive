---
title: 'NOTE: this transaction uses an encrypted payment ID: consider using subaddresses
  instead'
source_url: https://github.com/monero-project/monero/issues/6343
author: anonproject
assignees: []
labels:
- invalid
created_at: '2020-02-18T00:16:11+00:00'
updated_at: '2020-02-18T01:41:42+00:00'
type: issue
status: closed
closed_at: '2020-02-18T01:41:42+00:00'
---

# Original Description
I am using create_address RPC method to create an address and sweep_all RPC method to send a trasaction.

The problem is that in CLI upon receiving such a transaction I see the following:
```text
NOTE: this transaction uses an encrypted payment ID: consider using subaddresses instead
```
But how come?  I never used any payment id:

```bash
# generate a new address
#
json=$(cat <<-EOF
{"jsonrpc":"2.0","id":"0","method":"create_address","params":{"account_index":$destpick,"label":"$sourcepick:$source1:$source2:$source3"}}
EOF
)
o=$(timeout 60s curl --connect-timeout 10 --max-time 60 -X POST http://127.0.0.1:18082/json_rpc -d "$json" -H 'Content-Type: application/json')
echo "$o" | jq .
destaddress=$(echo "$o" | jq -r .result.address)
echo "new address has been created: $destaddress"

# make a transaction
#
  json=$(cat <<-EOF
  {
    "jsonrpc":"2.0",
    "id":"0",
    "method":"sweep_all",
    "params":{
      "address":"$destaddress",
      "account_index":$source,
      "subaddr_indices":[$source1,$source2,$source3],
      "priority":0,
      "do_not_relay":false,
      "unlock_time":0,
      "get_tx_keys":true,
      "get_tx_hex":false
    }
  }
EOF
)

echo "$json" | jq .
o=$(curl -X POST http://localhost:18082/json_rpc -d "$json" -H 'Content-Type: application/json')
```

# Discussion History
## moneromooo-monero | 2020-02-18T01:36:16+00:00
It triggers on the default ones. It got fixed since (#6197).

+invalid

# Action History
- Created by: anonproject | 2020-02-18T00:16:11+00:00
- Closed at: 2020-02-18T01:41:42+00:00
