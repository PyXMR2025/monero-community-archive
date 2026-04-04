---
title: query_key option to return TRUE or FALSE on checks for stored key of certain
  type
source_url: https://github.com/monero-project/monero/issues/8373
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2022-06-02T21:04:30+00:00'
updated_at: '2022-06-19T01:10:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There are many cases where servers may be used with a view key only to receive payments. Thus, it is useful to have functionality to be able to safely check through an RPC call if a wallet is view-only or not.

Related: https://monero.stackexchange.com/questions/10160/querying-wallet-rpc-about-whether-a-wallet-is-view-only

The RPC should allow an option to "check" for a given key_type if the particular key exists. The response should be `TRUE` or `FALSE`.

The RPC call should accept as an input a new optional parameter `command` with can be set to `return` (existing functionality) or `check` (true/false response).

This specific implementation is just an illustration of a possible method to meet the requirements of safely checking if a view-only wallet exists or not. The Monero devs (you) have a better idea of how it's best to implement.

# Discussion History
## plowsof | 2022-06-10T03:20:43+00:00
An error message will be returned if you query the spend key of a view-only wallet, so in a 'round about way' you can detect it by checking the response (which will be `The wallet is watch-only. Cannot retrieve spend key.`) but i guess a specific check wouldn't be too hard to implement , *checks notes* ah yes, i have zero c++ knowledge :D
```
curl -X POST http://192.168.1.68:18084/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"query_key","params":{"key_type":"view_key"}}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "key": "f359631075708155cc3d92a32b75a7d02a5dcf27756707b47a2b31b21c389501"
  }
}
```
```
curl -X POST http://192.168.1.68:18084/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"query_key","params":{"key_type":"spend_key"}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -29,
    "message": "The wallet is watch-only. Cannot retrieve spend key."
  },
  "id": "0",
  "jsonrpc": "2.0"
```



# Action History
- Created by: SamsungGalaxyPlayer | 2022-06-02T21:04:30+00:00
