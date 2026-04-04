---
title: 'error creating wallet via RPC '
source_url: https://github.com/monero-project/monero/issues/8403
author: saravananp-001
assignees: []
labels: []
created_at: '2022-06-23T13:00:45+00:00'
updated_at: '2022-08-11T00:53:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
the wallet files are not created in the wallet-dir location when use the curl command of create_wallet in the terminal. but the response said
`{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
}`

# Discussion History
## plowsof | 2022-06-29T13:51:43+00:00
so you're starting your monero rpc with `--wallet-dir` (full path)  and you are passing the params to create_wallet of filename / language? https://github.com/plowsof/flipstarter-waas-wip/blob/fbb8c77dd9823d6606f5a48b0e25f8f9e361defb/app/setup_wallets.py#L286


## selsta | 2022-08-11T00:53:38+00:00
ping @saravananp-001, can you reply to the above comment?

# Action History
- Created by: saravananp-001 | 2022-06-23T13:00:45+00:00
