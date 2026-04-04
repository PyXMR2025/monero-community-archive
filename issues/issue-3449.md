---
title: Using curl to call monero-wallet-rpc api, the result is   401 Unauthorized
source_url: https://github.com/monero-project/monero/issues/3449
author: kevingwang
assignees: []
labels:
- invalid
created_at: '2018-03-20T08:14:05+00:00'
updated_at: '2018-06-18T14:57:11+00:00'
type: issue
status: closed
closed_at: '2018-06-18T14:57:11+00:00'
---

# Original Description
Start monero-wallet-rpc  successfully : 

./monero-wallet-rpc --rpc-bind-port 18082 --wallet-file wallet1
Monero 'Helium Hydra' (v0.11.1.0-release)
2018-03-20 07:58:33.069	    7fdfa8233780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18082
2018-03-20 07:58:33.110	    7fdfa8233780	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1898	Starting wallet rpc server


Then call the rpc api , the result is  <h1>401 Unauthorized</h1>

ubuntu@ip-172-31-42-19:~$ curl -u "wallet1":"123456" --digest -s -S -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance"}' -H 'Content-Type: application/json'
<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>ubuntu@ip-172-31-42-19:~$ 
ubuntu@ip-172-31-42-19:~$ 
ubuntu@ip-172-31-42-19:~$ 
ubuntu@ip-172-31-42-19:~$ curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance"}' -H 'Content-Type: application/json'
<html><head><title>Unauthorized Access</title></head><body><h1>401 Unauthorized</h1></body></html>ubuntu@ip-172-31-42-19:~$ 



# Discussion History
## kevingwang | 2018-03-20T09:09:34+00:00
If i use  --disable-rpc-login  option to start  monero-wallet-rpc, the result is correct: 

ubuntu@ip-172-31-42-19:~$ curl -X POST http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getbalance"}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "balance": 0,
    "unlocked_balance": 0
  }



so, how to use programming language( for example , php ) to call rpc api to transfer money? Always use 
--disable-rpc-login  to start  monero-wallet-rpc  ?


## moneromooo-monero | 2018-03-20T13:13:35+00:00
Works for me. Are you sure you copied the login/password correctly from the file it generates ?

## krtschmr | 2018-03-29T12:34:32+00:00
Hi @kevingwang 

this is how to do CURL correctly with the RPC client

https://github.com/krtschmr/monero/blob/master/lib/monero/client.rb#L8

## krtschmr | 2018-03-29T12:35:34+00:00
Hi @kevingwang 

this is how to do CURL correctly with the RPC client

https://github.com/krtschmr/monero/blob/master/lib/monero/client.rb#L8

Pls make sure to start correct

Start your daemon `./monerod --testnet`

Start your RPC Client `./monero-wallet-rpc --testnet --rpc-bind-port 18081 --rpc-bind-ip 127.0.0.1 --rpc-login username:password --log-level 4 --wallet-dir ./`





## moneromooo-monero | 2018-05-16T11:02:22+00:00
If no further comment soon, I'll assume this was user error and close.

## moneromooo-monero | 2018-06-18T14:45:16+00:00
+invalid

# Action History
- Created by: kevingwang | 2018-03-20T08:14:05+00:00
- Closed at: 2018-06-18T14:57:11+00:00
