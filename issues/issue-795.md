---
title: Add "outgoing_transfers" as simplewallet json_rpc method.
source_url: https://github.com/monero-project/monero/issues/795
author: bigreddmachine
assignees: []
labels: []
created_at: '2016-04-05T17:25:59+00:00'
updated_at: '2016-05-10T12:31:42+00:00'
type: issue
status: closed
closed_at: '2016-05-10T12:31:41+00:00'
---

# Original Description
Right now, simplewallet's json_rpc allows a user to request incoming transfers, but to see outgoing transfers you have to be using simplewallet from the command line, inputing "show_transfers out".

Could a new json_rpc method be introduced similar to "incoming_transfers" but for outgoing?


# Discussion History
## moneromooo-monero | 2016-04-27T07:41:36+00:00
get_transfers, with 4 booleans (in, out, pending, failed)


## antanst | 2016-04-27T10:05:30+00:00
Thanks for that! I'm trying it right now in a wallet with both incoming and outgoing transfers in the past, with various combinations:

`curl -X POST http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"in":true}}' -H 'Content-Type: application/json'`

`curl -X POST http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_transfers","params":{"out":true,"in":true,"pending":false,"failed":false}}' -H 'Content-Type: application/json'`

in all cases I get no results:

`
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
}
`


## fluffypony | 2016-05-10T12:31:41+00:00
Added - if there are any bugs with the feature please open separate issues


# Action History
- Created by: bigreddmachine | 2016-04-05T17:25:59+00:00
- Closed at: 2016-05-10T12:31:41+00:00
