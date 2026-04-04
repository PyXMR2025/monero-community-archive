---
title: '#3934(no connection to daemon) reproduced'
source_url: https://github.com/monero-project/monero/issues/4145
author: xinyijun
assignees: []
labels: []
created_at: '2018-07-17T09:07:26+00:00'
updated_at: '2018-07-18T08:29:07+00:00'
type: issue
status: closed
closed_at: '2018-07-18T08:29:07+00:00'
---

# Original Description
[](url)https://github.com/monero-project/monero/issues/3934 reproduced

We still have the issue([](url)https://github.com/monero-project/monero/issues/3934), below is the error log. In version v0.12.3.0, although DEFAULT_TIMEOUT_MS_REMOTE was increased to 5 minutes, the implementation of function get_timeout_from_bytes_read may still cause short timeout, it has such logic:
`
if (ms > get_default_timeout())
        ms = get_default_timeout();
`
Is it possible to change the logic as below or make it configurable?
` 
if (ms < get_default_timeout())
     ms = get_default_timeout();
`
> 2018-07-17 08:39:49.857	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1673:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getversion
2018-07-17 08:39:49.857	[RPC0]	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:109	Exception at while refreshing, what=no connection to daemon
2018-07-17 08:41:25.421	[RPC0]	WARN 	net	contrib/epee/include/net/net_helper.h:188	Some problems at connect, message: Operation timed out
2018-07-17 08:41:25.421	[RPC0]	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /json_rpc
2018-07-17 08:41:25.421	[RPC0]	ERROR	net.http	src/wallet/node_rpc_proxy.cpp:78	Failed to connect to daemon
2018-07-17 08:41:25.421	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1673	result->empty(). THROW EXCEPTION: tools::error::no_connection_to_daemon
2018-07-17 08:41:25.421	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1673:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getversion
2018-07-17 08:41:25.421	[RPC0]	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:109	Exception at while refreshing, what=no connection to daemon
2018-07-17 08:43:00.694	[RPC0]	WARN 	net	contrib/epee/include/net/net_helper.h:188	Some problems at connect, message: Operation timed out
2018-07-17 08:43:00.694	[RPC0]	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /json_rpc
2018-07-17 08:43:00.695	[RPC0]	ERROR	net.http	src/wallet/node_rpc_proxy.cpp:78	Failed to connect to daemon
2018-07-17 08:43:00.695	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1673	result->empty(). THROW EXCEPTION: tools::error::no_connection_to_daemon
2018-07-17 08:43:00.695	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1673:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getversion
2018-07-17 08:43:00.695	[RPC0]	ERROR	wallet.rpc	src/wallet/wallet_rpc_server.cpp:109	Exception at while refreshing, what=no connection to daemon
2018-07-17 08:44:36.004	[RPC0]	WARN 	net	contrib/epee/include/net/net_helper.h:188	Some problems at connect, message: Operation timed out
2018-07-17 08:44:36.005	[RPC0]	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:53	Failed to invoke http request to  /json_rpc
2018-07-17 08:44:36.005	[RPC0]	ERROR	net.http	src/wallet/node_rpc_proxy.cpp:78	Failed to connect to daemon
2018-07-17 08:44:36.005	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1673	result->empty(). THROW EXCEPTION: tools::error::no_connection_to_daemon
2018-07-17 08:44:36.005	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1673:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getversion

# Discussion History
## moneromooo-monero | 2018-07-17T12:25:59+00:00
No. If you do this, then it becomes very easy to DoS.
As for the timeout, it looks like you've got no connection to the node. getversion is a really, really fast RPC, it should not take 5 minutes.


## xinyijun | 2018-07-17T13:40:23+00:00
It did get connection to node, but it lost the connection frequently.
It didn't take 5 minutes, it took time calculated according to bytes(`boost::posix_time::milliseconds ms = (boost::posix_time::milliseconds)(unsigned)(bytes * TIMEOUT_EXTRA_MS_PER_BYTE);`)

## moneromooo-monero | 2018-07-17T14:14:12+00:00
OK, that could be tuned I suppose.


## xinyijun | 2018-07-18T02:08:27+00:00
Thanks, when will we have a release including the tune?

## xinyijun | 2018-07-18T08:29:07+00:00
Sorry, I made a mistake, it got no connection yesterday when I did test.

# Action History
- Created by: xinyijun | 2018-07-17T09:07:26+00:00
- Closed at: 2018-07-18T08:29:07+00:00
