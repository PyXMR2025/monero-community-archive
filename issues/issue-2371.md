---
title: wallet-rpc returns false indices on add_address_book
source_url: https://github.com/monero-project/monero/issues/2371
author: fkr-0
assignees: []
labels: []
created_at: '2017-08-29T11:30:43+00:00'
updated_at: '2017-09-25T20:36:26+00:00'
type: issue
status: closed
closed_at: '2017-09-25T20:36:26+00:00'
---

# Original Description
If you add an entry to the address book, the returned index is counting from 1. But its actually stored with indices counting from 0. Example:

`curl -X POST http://localhost:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"add_address_book","params":{"address":"A135xq3GVMdU5qtAm4hN7zjPgz8bRaiSUQmtuDdjZ6CgXayvQruJy3WPe95qj873JhK4YdTQjoR39Leg6esznQk8PckhjRN"}}' -H 'Content-Type: application/json'`
```json
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "index": 1
  }
}
```
`curl -X POST http://localhost:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":get_address_book","params":{"entries":[1]}}' -H 'Content-Type: application/json'`
```json
{
  "error": {
    "code": -12,
    "message": "Index out of range: 1"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```
`curl -X POST http://localhost:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_address_book","params":{"entries":[0]}}' -H 'Content-Type: application/json'`
```json
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "entries": [{
      "address": "A135xq3GVMdU5qtAm4hN7zjPgz8bRaiSUQmtuDdjZ6CgXayvQruJy3WPe95qj873JhK4YdTQjoR39Leg6esznQk8PckhjRN",
      "description": "",
      "index": 0,
      "payment_id": "0000000000000000000000000000000000000000000000000000000000000000"
    }]
  }
}
```


# Discussion History
## moneromooo-monero | 2017-08-29T19:26:54+00:00
I'm not sure that index is useful anyway. It might as well return the number of entries. If you delete another, the index becomes invalid, so it's a bit pointless. I think it might be better to just omit this...

## moneromooo-monero | 2017-09-13T10:10:04+00:00
I guess it might as well return the right index till we decide whether to remove it or not.

https://github.com/monero-project/monero/pull/2443

## moneromooo-monero | 2017-09-25T20:31:16+00:00
+resolved

# Action History
- Created by: fkr-0 | 2017-08-29T11:30:43+00:00
- Closed at: 2017-09-25T20:36:26+00:00
