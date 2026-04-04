---
title: Unable to restore view-only wallet on Linux cli wallet
source_url: https://github.com/monero-project/monero/issues/4644
author: scmlxmr
assignees: []
labels: []
created_at: '2018-10-18T06:38:46+00:00'
updated_at: '2018-10-18T08:41:02+00:00'
type: issue
status: closed
closed_at: '2018-10-18T08:41:02+00:00'
---

# Original Description
I have tried restoring view only wallet with --generate-from-view-key argument with the wallet accepting the address but omits following error after entering secret view key : 
**Error: failed to parse view key secret key.** 
To discount possibility of my view key is corrupted, i have retried by generating a dummy wallet and try to restore from the new view key. Failed with the same error. 

```
Enter the number corresponding to the language of your choice: 1
Generated new wallet: 475ysQU1NDJRwTk7yXKpaS4tti6NmtiKajDXK4hcLcERCie4pnPhwUuPaNzdcP3AuyHGhsJjyNqaf2TEUYjx7yP25pqgnSX
View key: 5ddfa729fe909076713c41d786d173b25cc090f603ad99ef7deb336c3e97eb04
**********************************************************************
```

Followed by 

```
root@scml-node:~# monero-wallet-cli --daemon-address 127.0.0.1:18089 --generate-from-view-key test2
2018-10-18 06:22:44,526 INFO  [default] Page size: 4096
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Beryllium Bullet' (v0.13.0.2-release)
Logging to monero-wallet-cli.log
Standard address: 475ysQU1NDJRwTk7yXKpaS4tti6NmtiKajDXK4hcLcERCie4pnPhwUuPaNzdcP3AuyHGhsJjyNqaf2TEUYjx7yP25pqgnSX
Secret view key: : 5ddfa729fe909076713c41d786d173b25cc090f603ad99ef7deb336c3e97eb04

Error: failed to parse view key secret key
```

Connected to node through SSH (Putty) & used copy paste as input if this information matters.


# Discussion History
## scmlxmr | 2018-10-18T06:42:19+00:00
monero-wallet-cli.log
```
2018-10-18 06:16:21.638     7f7775d18780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,ne$
2018-10-18 06:17:09.844     7f44991c4780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,ne$
2018-10-18 06:19:06.017     7fddb90e7780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,ne$
2018-10-18 06:19:42.500     7f65ac722780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,ne$
2018-10-18 06:21:29.505     7f74a2f85780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,ne$
2018-10-18 06:22:45.532     7faae74f5780        INFO    logging contrib/epee/src/mlog.cpp:242   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.p2p:FATAL,ne$
```



## moneromooo-monero | 2018-10-18T08:38:20+00:00
Fixed in https://github.com/monero-project/monero/pull/4568, which is merged already.

+resolved

# Action History
- Created by: scmlxmr | 2018-10-18T06:38:46+00:00
- Closed at: 2018-10-18T08:41:02+00:00
