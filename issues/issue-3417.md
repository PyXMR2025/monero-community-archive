---
title: Using curl to call monero-wallet-rpc api , the result is  401 Unauthorized
source_url: https://github.com/monero-project/monero/issues/3417
author: kevingwang
assignees: []
labels:
- invalid
created_at: '2018-03-16T08:53:25+00:00'
updated_at: '2018-03-16T09:56:50+00:00'
type: issue
status: closed
closed_at: '2018-03-16T09:56:50+00:00'
---

# Original Description
ubuntu@ip-172-31-42-19:~$ curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance"}' -H 'Content-Type: application/json'
<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>ubuntu@ip-172-31-42-19:~$ 


# Discussion History
## moneromooo-monero | 2018-03-16T08:56:16+00:00
Either disable authentication (--disable-rpc-login), or authenticate (digest method).

+invalid


## kevingwang | 2018-03-16T09:53:40+00:00
And how to transfer by programming  (for example , by php programming ) ?
There is no username and password parameters  for the JSON-RPC function of transfer() .

## kevingwang | 2018-03-16T09:55:51+00:00
ubuntu@ip-172-31-42-19:~$ curl  -u "wallet1":"123456" --digest -s -S  -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance"}' -H 'Content-Type: application/json'
<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>ubuntu@ip-172-31-42-19:~$ 


# Action History
- Created by: kevingwang | 2018-03-16T08:53:25+00:00
- Closed at: 2018-03-16T09:56:50+00:00
