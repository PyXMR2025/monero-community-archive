---
title: linux(Command-Line Tools Only),run monero-wallet-rpc , use curl request , return
  'Unauthorized Access'
source_url: https://github.com/monero-project/monero/issues/2553
author: holdgan
assignees: []
labels:
- invalid
created_at: '2017-09-30T02:57:42+00:00'
updated_at: '2019-01-17T08:31:55+00:00'
type: issue
status: closed
closed_at: '2017-09-30T08:12:21+00:00'
---

# Original Description
./monero-wallet-rpc --rpc-bind-port 18082 --wallet-file sun --password ****** &

curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance"}' -H 'Content-Type: application/json'

<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>

------------------------------------
I don't know why,
help me.

# Discussion History
## moneromooo-monero | 2017-09-30T08:10:10+00:00
See --disable-rpc-login or the other login related options.
If you need help using monero, this is not the place. Try #monero on freenode, or Reddit.

+invalid


## fourseaLee | 2019-01-17T08:31:55+00:00
curl  -u username:password --digest  -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance"}' -H 'Content-Type: application/json'  maybe can use. @jiushigan 

# Action History
- Created by: holdgan | 2017-09-30T02:57:42+00:00
- Closed at: 2017-09-30T08:12:21+00:00
