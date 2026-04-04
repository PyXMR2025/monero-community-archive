---
title: Create wallet with JSON RPC FAILED
source_url: https://github.com/monero-project/monero/issues/1970
author: valuead
assignees: []
labels: []
created_at: '2017-04-13T18:35:12+00:00'
updated_at: '2017-08-09T10:18:13+00:00'
type: issue
status: closed
closed_at: '2017-08-09T10:18:13+00:00'
---

# Original Description
I'm trying to create wallet from JSON  and can't make it work nither with CLI or RPC
Without JSON I DO can make wallet with CLI
Please advice

**Environment:** 
WINDOWS 7 X64
Executing commands on the localhost
MoneroD fully synced status ok 100% completed and running





**The Command:** 

c:\dev>monero-wallet-rpc.exe --rpc-bind-ip 0.0.0.0 --rpc-bind-port 18081 --confirm-external-bind --disable-rpc-login --generate-from-json "C:\Xmr\1.txt"

**Responds** 
2017-04-13 21:21:15.193 8384    INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Monero 'Wolfram Warptangent' (v0.10.3.1-release)
Logging to c:\dev\monero-wallet-rpc.log
2017-04-13 21:21:15.202 8384    WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:1527   Loading wallet...
2017-04-13 21:21:15.260 8384    ERROR   net.http        src/wallet/node_rpc_proxy.cpp:78        Failed to connect to daemon
2017-04-13 21:21:15.261 8384    ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1180     result->empty(). THROW EXCEPTION: tools::error::no_connection_to_daemon
2017-04-13 21:21:15.262 8384    WARN    net.http        src/wallet/wallet_errors.h:697  C:/msys64/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1180:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getversion
2017-04-13 21:21:15.263 8384    ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:1561   Wallet initialization failed: no connection to daemon-----------------------------------------------------------------------------


**JSON FILE LOOKS LIKE THIS:**
{"address":"44YVn4FrxPWXgQxqMWshmE91KUDBrkLUf5GGGDnbR7gA91w7irvfoPKjNYNMDViXUW97jrqv9uosGh1KpMYVJNMcHthnHkz","viewkey":"2ca9f389719705b161c8c721d99a251b386a47f602fa0b86f77b71a6bb94600b","sendkey":"39ce1d8ff7124da5b460a9b9e5cf100c23812c542413c933c965078dbce19b06","version":1, "filename":"1.txt"}

# Discussion History
## moneromooo-monero | 2017-04-14T07:08:34+00:00
If this is a real key with monero on it, move it quick :)
Also, typo in spendkey (typoed as sendkey).


## DmRomantsov | 2017-04-14T09:58:12+00:00
These keys are generated using https://moneroaddress.org/ 
There are no coins on the wallet, we use it for the test
Also, we tried with fixed typo - result the same,

## valuead | 2017-04-14T13:44:34+00:00
Does anyone able to create wallet with JSON 
Contributors willing to help?
monero-wallet-rpc.exe  --generate-from-json 
Thank You

## moneromooo-monero | 2017-04-14T21:13:34+00:00
https://github.com/monero-project/monero/pull/1976

## moneromooo-monero | 2017-08-09T10:12:48+00:00
+resolved

# Action History
- Created by: valuead | 2017-04-13T18:35:12+00:00
- Closed at: 2017-08-09T10:18:13+00:00
