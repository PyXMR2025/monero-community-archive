---
title: monero-wallet-rpc  can not connect to monerod
source_url: https://github.com/monero-project/monero/issues/3445
author: kevingwang
assignees: []
labels: []
created_at: '2018-03-20T03:37:22+00:00'
updated_at: '2018-07-12T14:30:27+00:00'
type: issue
status: closed
closed_at: '2018-03-20T08:08:21+00:00'
---

# Original Description
ubuntu@ip-172-31-42-19:~/work/monero/monero-v0.11.1.0$ ./monero-wallet-rpc --rpc-bind-port 18082 --wallet-file wallet1  --disable-rpc-login
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to ./monero-wallet-rpc.log
2018-03-20 03:31:29.302	    7f002b060780	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1853	Loading wallet...
Wallet password: ******
2018-03-20 03:31:33.868	    7f002b060780	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 46w8ESHfJZ166pSnZTuPaAK9h7ZrK7kQTWU6FySBfeDL12DV8kF31eBQfo49SAT97SBobLsLmiJNDeae9yAqguRAT5pmrVS

2018-03-20 03:35:04.358	    7f002b060780	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2018-03-20 03:35:04.359	    7f002b060780	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1238	!r. THROW EXCEPTION: error::no_connection_to_daemon
2018-03-20 03:35:04.359	    7f002b060780	WARN 	net.http	src/wallet/wallet_errors.h:707	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1238:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gethashes.bin
2018-03-20 03:35:04.361	    7f002b060780	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1887	Wallet initialization failed: no connection to daemon


# Discussion History
## kevingwang | 2018-03-20T07:36:22+00:00
ubuntu@ip-172-31-42-19:~/work/monero/monero-v0.11.1.0$ ./monero-wallet-rpc --rpc-bind-port 18082 --wallet-file wallet1
Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to ./monero-wallet-rpc.log
2018-03-20 07:33:52.911	    7f0f51d0c780	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1853	Loading wallet...
Wallet password: ******
2018-03-20 07:33:56.577	    7f0f51d0c780	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:2505	Loaded wallet keys file, with public address: 46w8ESHfJZ166pSnZTuPaAK9h7ZrK7kQTWU6FySBfeDL12DV8kF31eBQfo49SAT97SBobLsLmiJNDeae9yAqguRAT5pmrVS
2018-03-20 07:35:04.896	    7f0f51d0c780	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:198	Failed to create file monero-wallet-rpc.18082.login. Check permissions or remove file
2018-03-20 07:35:04.897	    7f0f51d0c780	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1894	Failed to initialize wallet rpc server


## kevingwang | 2018-03-20T07:37:31+00:00
What is the reason of this issue ? 

Failed to create file monero-wallet-rpc.18082.login. Check permissions or remove file

## skinderis | 2018-07-12T14:26:56+00:00
Did you resolve this problem? Cause I have the issue...  I open wallet and in the beginning getting this log:
```
000000000, with tx: <538e1255828fc5240b0b4322a72456c5e9ffeaf36664782f01b8a580e1aa72c6>
monero-wallet_1  | 2018-07-12 14:28:35.215	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1312	Received money: 0.100000000000, with tx: <eddf291243c8fe8ea7f45dcff9f5b997481f4dbadcc5ffbcbf79db9aae57d565>
monero-wallet_1  | 2018-07-12 14:28:35.218	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1312	Received money: 21.661450692058, with tx: <eddf291243c8fe8ea7f45dcff9f5b997481f4dbadcc5ffbcbf79db9aae57d565>
monero-wallet_1  | 2018-07-12 14:28:35.220	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1418	Spent money: 21.762383872058, with tx: <eddf291243c8fe8ea7f45dcff9f5b997481f4dbadcc5ffbcbf79db9aae57d565>
monero-wallet_1  | 2018-07-12 14:28:35.295	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1312	Received money: 0.100000000000, with tx: <b4290727c1ffe029b60df0fedf779f5e7497dbb9acfd8bfcd8087c521ec91a25>
monero-wallet_1  | 2018-07-12 14:28:35.296	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1312	Received money: 9.899066820000, with tx: <b4290727c1ffe029b60df0fedf779f5e7497dbb9acfd8bfcd8087c521ec91a25>
monero-wallet_1  | 2018-07-12 14:28:35.297	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:1418	Spent money: 10.000000000000, with tx: <b4290727c1ffe029b60df0fedf779f5e7497dbb9acfd8bfcd8087c521ec91a25>

```
But suddenly something goes wrong and I get this:
```
monero-wallet_1  | 2018-07-12 14:25:39.552	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1699	!r. THROW EXCEPTION: error::no_connection_to_daemon
monero-wallet_1  | 2018-07-12 14:25:39.552	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1699:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
monero-wallet_1  | 2018-07-12 14:25:39.560	[RPC0]	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:109	Exception at while refreshing, what=no connection to daemon
monero-wallet_1  | 2018-07-12 14:26:21.355	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1699	!r. THROW EXCEPTION: error::no_connection_to_daemon
monero-wallet_1  | 2018-07-12 14:26:21.356	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1699:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
monero-wallet_1  | 2018-07-12 14:26:21.364	[RPC0]	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:109	Exception at while refreshing, what=no connection to daemon

```
This issue really annoys me for a long time 

# Action History
- Created by: kevingwang | 2018-03-20T03:37:22+00:00
- Closed at: 2018-03-20T08:08:21+00:00
