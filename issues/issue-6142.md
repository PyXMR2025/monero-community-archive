---
title: missing application/json header in daemon RPC on error
source_url: https://github.com/monero-project/monero/issues/6142
author: pocin
assignees: []
labels: []
created_at: '2019-11-15T18:55:37+00:00'
updated_at: '2020-07-08T23:02:42+00:00'
type: issue
status: closed
closed_at: '2020-07-08T23:02:42+00:00'
---

# Original Description
# problem
the daemon RPC call `get_block` doesn't return `content-type: application/json` but `text/plain` on error altough it returns the correct headers on succesfull call.

# example
```
$ curl -X POST \
    -H "Content-Type: application/json" \
    --data '{"jsonrpc": "2.0", "id": "0", "method": "get_block", "params": {"height": 99999999}}'\
    http://localhost:38081/json_rpc -D -

HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 172
Content-Type: text/plain
Last-Modified: Fri, 15 Nov 2019 18:48:30 GMT
Accept-Ranges: bytes

{
  "error": {
    "code": -2,
    "message": "Requested block height: 99999999 greater than current top block height: 454338"
  },
  "id": "0",
  "jsonrpc": "2.0"
}% 
```

try this with valid blockheight
```
$ curl -X POST \
    -H "Content-Type: application/json" \
    --data '{"jsonrpc": "2.0", "id": "0", "method": "get_block", "params": {"height": 400000}}'\
    http://localhost:38081/json_rpc -D -

HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 2623
Content-Type: application/json
Last-Modified: Fri, 15 Nov 2019 18:48:12 GMT
Accept-Ranges: bytes

{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "blob": "0b0b9190a9eb05299c7dce65e76e384582468b781ac72a680a9d1133a7e6d61bd180a461408de95b3132f502bcb51801ff80b51801dba6d0bebeec03028a534c24c68b3d041efcfe3
```

and it works ok.

Tested with `monerod --stagenet`
# expected outcome
return `content-type: application/json` on error.

# Discussion History
## moneromooo-monero | 2019-11-15T19:45:21+00:00
https://github.com/monero-project/monero/pull/6143

## moneromooo-monero | 2020-07-08T23:02:41+00:00
Merged

# Action History
- Created by: pocin | 2019-11-15T18:55:37+00:00
- Closed at: 2020-07-08T23:02:42+00:00
