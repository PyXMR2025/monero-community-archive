---
title: monero-wallet-rpc does not like to connect to Tor hidden services
source_url: https://github.com/monero-project/monero/issues/4039
author: moneromooo-monero
assignees: []
labels: []
created_at: '2018-06-22T22:33:45+00:00'
updated_at: '2022-03-16T15:46:28+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:46:28+00:00'
---

# Original Description
From codah on IRC:

i tried version 12.0 and 12.2 but both wont work


user@computer$ torsocks ./monero-wallet-rpc --rpc-bind-port 29088 --rpc-bind-ip 127.0.0.1 --password='test' --wallet-file=test2 --daemon-address=zdhkwneu7lfaum2p.onion:18099  --log-level 4  --disable-rpc-login


```
date [RPC0]  TRACE   net     contrib/epee/include/net/net_helper.h:403       READ ENDS: Success. bytes_tr: 2968
date [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:2042     Got 1 and OK
date [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:2101     update_pool_state end
date [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:2333     Refresh done, blocks received: 3, balance (all accounts): 0.000000000000, unlocked: 0.000000000000
date[RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:984   handle_accept
date [RPC0]  ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:1005  Some problems at accept: Bad address, connections_count = 1
date [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:1670     Daemon is recent enough, asking for pruned blocks
date [RPC0]  TRACE   net     contrib/epee/include/net/net_helper.h:264       Problems at write: Broken pipe
date [RPC0]  ERROR   net.http        contrib/epee/include/net/http_client.h:397      HTTP_CLIENT: Failed to SEND
date [RPC0]  INFO    net.http        contrib/epee/include/storages/http_abstract_invoke.h:84 Failed to invoke http request to  /getblocks.bin
date [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1684     !r. THROW EXCEPTION: error::no_connection_to_daemon
date [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:794  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1684:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
date [RPC0]  ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:109    Exception at while refreshing, what=no connection to daemon
```



note: torsocks works with monero-wallet-cli and monerod without problem, maybe it timeouts to quick? i have no idea of why this is happening

# Discussion History
## moneromooo-monero | 2018-06-23T08:43:35+00:00
Works for me, with both monero-wallet-rpc and monero-wallet-cli.
Any particular unusual network config ?

## moneromooo-monero | 2018-06-23T18:11:39+00:00
From IRC, the problem is not that monero-wallet-rpc can't connect to the onion hidden service, it's that a client cannot connect to monero-wallet-rpc while moenro-wallet-rpc is connected to the onion hidden service.

Still works for me.


## keffnet | 2018-06-25T14:31:28+00:00
It shouldnt work. I think you need to specify AllowOutboundLocalhost 1 

## moneromooo-monero | 2018-06-25T15:40:20+00:00
Reminds me, I used TORSOCKS_ALLOW_INBOUND=1. Didn't help codah.

## normoes | 2018-07-06T09:28:51+00:00
If this is timeout-related, it could be related to [#3934](https://github.com/monero-project/monero/issues/3934) and [#3962](https://github.com/monero-project/monero/pull/3962).

Both seem to be included in [0.12.3.0](https://github.com/monero-project/monero/compare/v0.12.3.0...master).

## jonathancross | 2019-11-12T15:25:15+00:00
Is this still an issue in `v0.15.0.0`?

## normoes | 2019-11-12T15:54:55+00:00
I never had problems with this issue.

## selsta | 2022-03-16T15:46:28+00:00
No other reports, closing due to inactivity.

# Action History
- Created by: moneromooo-monero | 2018-06-22T22:33:45+00:00
- Closed at: 2022-03-16T15:46:28+00:00
