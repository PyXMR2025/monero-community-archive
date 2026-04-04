---
title: Failed to initialize wallet RPC server
source_url: https://github.com/monero-project/monero-gui/issues/1295
author: MegaChange
assignees: []
labels:
- resolved
created_at: '2018-04-08T19:18:18+00:00'
updated_at: '2018-07-04T10:09:30+00:00'
type: issue
status: closed
closed_at: '2018-07-04T10:09:30+00:00'
---

# Original Description
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Users\Administrator>D:\monero-gui-v0.11.1.0\monero-wallet-rpc.exe --wallet-file d:\MoneroWallets\Main\Main --password ********* --rpc-bind-port 18082 --rpc-login user:user
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Lithium Luna' (v0.12.0.0-master-release)
Logging to D:\monero-gui-v0.11.1.0\monero-wallet-rpc.log
2018-04-08 15:13:38.658 8296    WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:2948   Loading wallet...
2018-04-08 15:13:39.010 8296    WARN    wallet.wallet2  src/wallet/wallet2.cpp:3718     Loaded wallet keys file, with public address: 4*********
2018-04-08 15:13:43.733 8296    INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:18082
2018-04-08 15:13:43.734 8296    FATAL   net     contrib/epee/include/net/abstract_tcp_server2.inl:741   Error starting server: bind: An attempt was made to access a socket in a way forbidden by its access permissions
2018-04-08 15:13:43.735 8296    ERROR   net.http        contrib/epee/include/net/http_server_impl_base.h:80     Failed to bind server
2018-04-08 15:13:43.735 8296    ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:2997 Failed to initialize wallet RPC server

looks like 18082 port is occupied by monerod.exe

what is the solution?

# Discussion History
## stoffu | 2018-04-09T06:26:28+00:00
Use any other port that's not used by monerod. There's no default port number defined for wallet RPC, and 18082 has been used a lot in usage examples purely by convention.

## dEBRUYNE-1 | 2018-07-04T08:38:41+00:00
+resolved

# Action History
- Created by: MegaChange | 2018-04-08T19:18:18+00:00
- Closed at: 2018-07-04T10:09:30+00:00
