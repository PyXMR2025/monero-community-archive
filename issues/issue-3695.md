---
title: The sweep_dust interface is executed successfully. How many dust transactions
  are required? What is the value of the dust transaction?
source_url: https://github.com/xmrig/xmrig/issues/3695
author: zelonH
assignees: []
labels: []
created_at: '2025-08-20T09:01:52+00:00'
updated_at: '2025-08-20T09:22:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
curl -s --digest -u ${user}:${password} -X POST http://127.0.0.1:10223/json_rpc \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc":"2.0",
    "id":"0",
    "method":"sweep_dust",
    "params": {
        "get_tx_keys": false,
        "do_not_relay": false,
        "get_tx_hex": true,
        "get_tx_metadata": false
    }
}'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "multisig_txset": "",
    "unsigned_txset": ""
  }
}

# Discussion History
## SChernykh | 2025-08-20T09:11:47+00:00
This is not an XMRig-related issue.

## zelonH | 2025-08-20T09:22:04+00:00
> This is not an XMRig-related issue.

hello ,So where should I ask?  @SChernykh 

# Action History
- Created by: zelonH | 2025-08-20T09:01:52+00:00
