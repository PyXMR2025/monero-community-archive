---
title: monero-wallet-rpc not connecting to monerod
source_url: https://github.com/monero-project/monero/issues/3622
author: skinderis
assignees: []
labels: []
created_at: '2018-04-12T15:46:16+00:00'
updated_at: '2018-04-13T11:08:50+00:00'
type: issue
status: closed
closed_at: '2018-04-13T11:08:50+00:00'
---

# Original Description
Hi, I am trying to connect monero-wallet-rpc to monerod, both binaries are running on the same docker container. When I run method **getheight** on my wallet it returns **height: 1** (not synced with daemon).
monero.conf:
```
data-dir=/root/monero/data
rpc-bind-ip=0.0.0.0
rpc-bind-port=18556
p2p-bind-port=18555
p2p-bind-ip=0.0.0.0
rpc-login=user:password
```
monero-wallet.conf:
```
daemon-address=127.0.0.1:18556
rpc-bind-ip=0.0.0.0
rpc-bind-port=18557
rpc-login=user:password
wallet-dir=/root/monero/data/monero-wallets
```                                         
start.sh
```
#!/bin/bash 
./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach && \
./monero-wallet-rpc --config-file /root/monero/data/monero-wallet.conf --confirm-external-bind
```
Error log:
```
monero_1  | Monero 'Lithium Luna' (v0.12.0.0-master-8361d60)
monero_1  | Logging to ./monero-wallet-rpc.log
monero_1  | 2018-04-12 15:43:20.782	    7f73ac5c0780	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 0.0.0.0:18557
monero_1  | 2018-04-12 15:43:20.782	    7f73ac5c0780	WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:3001	Starting wallet RPC server
monero_1  | 2018-04-12 15:44:35.751	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3709	Loaded wallet keys file, with public address: 41pLNkSGSJK8pWAG9dd57YcWB82gH5ucHNEPnGt1FBN59PrdYqKUGB1SfZxGQPcYcDEbctmpN2kpVbtupm6yCRf16oXkjuY
monero_1  | 2018-04-12 15:44:35.928	[RPC0]	ERROR	net.http	contrib/epee/include/net/http_client.h:424	Client has incorrect username/password for server requiring authentication
monero_1  | 2018-04-12 15:44:35.928	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5583	!r. THROW EXCEPTION: error::no_connection_to_daemon
monero_1  | 2018-04-12 15:44:35.928	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/home/igoris/Desktop/monero/src/wallet/wallet2.cpp:5583:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gettransactions
monero_1  | 2018-04-12 15:44:35.967	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:3818	Failed to save rings, will try again next time
monero_1  | 2018-04-12 15:44:40.830	[RPC0]	ERROR	net.http	contrib/epee/include/net/http_client.h:424	Client has incorrect username/password for server requiring authentication
monero_1  | 2018-04-12 15:44:40.830	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1681	!r. THROW EXCEPTION: error::no_connection_to_daemon
monero_1  | 2018-04-12 15:44:40.830	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/home/igoris/Desktop/monero/src/wallet/wallet2.cpp:1681:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gethashes.bin
monero_1  | 2018-04-12 15:44:40.834	[RPC0]	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:109	Exception at while refreshing, what=no connection to daemon
```
Anyone knows how I can connect monero-wallet-rpc to daemon which is running in the same docker container?

# Discussion History
## stoffu | 2018-04-13T04:12:12+00:00
As the log says, the wallet RPC is failing the authentication required by the daemon:

```
monero_1  | 2018-04-12 15:44:35.928	[RPC0]	ERROR	net.http	contrib/epee/include/net/http_client.h:424	Client has incorrect username/password for server requiring authentication
```

which needs to be set via the `daemon-login` setting. The `rpc-login` setting of the wallet RPC is another authentication that the wallet RPC requires from the users accessing the wallet RPC.


## skinderis | 2018-04-13T10:38:51+00:00
@stoffu, Yep that was exactly my issue! I just removed rpc login and pass from daemon conf file and wallet syncs with the daemon :+1: 

## dEBRUYNE-1 | 2018-04-13T11:00:41+00:00
+resolved

# Action History
- Created by: skinderis | 2018-04-12T15:46:16+00:00
- Closed at: 2018-04-13T11:08:50+00:00
