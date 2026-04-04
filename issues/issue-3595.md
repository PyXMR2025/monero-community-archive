---
title: Error when running monero-wallet-rpc with docker-compose up
source_url: https://github.com/monero-project/monero/issues/3595
author: skinderis
assignees: []
labels: []
created_at: '2018-04-10T11:14:26+00:00'
updated_at: '2018-04-10T15:25:17+00:00'
type: issue
status: closed
closed_at: '2018-04-10T15:25:17+00:00'
---

# Original Description
monero-wallet-rpc creates .login file even if i provide user and pass in config file:
```
Starting monerodocker_monero_1 ... 
Starting monerodocker_monero_1 ... done
Attaching to monerodocker_monero_1
monero_1  | 2018-04-10 11:18:35.660	    7fafb52e0740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
monero_1  | Forking to background...
monero_1  | Monero 'Helium Hydra' (v0.11.1.0-release)
monero_1  | Logging to ./monero-wallet-rpc.log
monero_1  | 2018-04-10 11:18:35.674	    7f4811fef740	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:198	Failed to create file monero-wallet-rpc.18557.login. Check permissions or remove file
monero_1  | 2018-04-10 11:18:35.674	    7f4811fef740	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:1894	Failed to initialize wallet rpc server

```


# Discussion History
# Action History
- Created by: skinderis | 2018-04-10T11:14:26+00:00
- Closed at: 2018-04-10T15:25:17+00:00
