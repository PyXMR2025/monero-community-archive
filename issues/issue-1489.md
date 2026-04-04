---
title: 'monero-wallet-rpc Wallet initialization failed: std::bad_alloc'
source_url: https://github.com/monero-project/monero/issues/1489
author: got3nks
assignees: []
labels: []
created_at: '2016-12-22T17:39:40+00:00'
updated_at: '2018-01-08T14:00:35+00:00'
type: issue
status: closed
closed_at: '2018-01-08T14:00:35+00:00'
---

# Original Description
After upgrading to v0.10.1 I can no longer load a wallet created with simplewallet (v0.9):
```

monero@server:~$ /home/monero/monero-wallet-rpc --rpc-bind-ip=0.0.0.0 --rpc-bind-port 8082 --password xxx --wallet-file /home/monero/wallet.bin --daemon-address=127.0.0.1:18081
Creating the logger system
Monero 'Wolfram Warptangent' (v0.10.1.0-release)
Logging at log level 0 to /home/monero/monero-wallet-rpc.log
2016-Dec-22 17:37:01.660812 Loading wallet...
2016-Dec-22 17:37:01.703471 Unknown refresh-type value (32767), using default
2016-Dec-22 17:37:01.703733 Loaded wallet keys file, with public address: xxxxxx
2016-Dec-22 17:37:03.603663 ERROR /DISTRIBUTION-BUILD/src/walle /wallet_rpc_server.cpp:1205 Wallet initialization failed: std::bad_alloc
```

# Discussion History
## gituser | 2016-12-22T21:29:38+00:00
Just restore your wallet using seed or private key into new wallet file via monero-wallet-cli.

## dEBRUYNE-1 | 2016-12-29T20:01:44+00:00
This is caused by an incompatible wallet cache. If you delete the cache (`<wallet>`) you should be able to open the wallet created with simplewallet. If that doesn't work, use the method described by @gituser. 

## vtnerd | 2016-12-30T07:21:58+00:00
So this is most likely caused by a crazy allocation request when trying to parse in the new invalid format. Does the existing cache format have a header that can be used to identity between types? So that the code doesn't try to blindly attempt to parse the wrong format?

## dEBRUYNE-1 | 2018-01-08T13:17:45+00:00
+resolved

# Action History
- Created by: got3nks | 2016-12-22T17:39:40+00:00
- Closed at: 2018-01-08T14:00:35+00:00
