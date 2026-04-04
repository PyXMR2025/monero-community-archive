---
title: wallet-dir option occurs rpc server error on windows
source_url: https://github.com/monero-project/monero/issues/3548
author: pandakiki11111
assignees: []
labels: []
created_at: '2018-04-04T08:40:56+00:00'
updated_at: '2018-09-14T11:16:55+00:00'
type: issue
status: closed
closed_at: '2018-09-14T11:16:55+00:00'
---

# Original Description
I need to use <create wallet api> on rpc server. so I add --wallet-dir option when I start wallet rpc server like this ↓

monero-wallet-rpc --rpc-bind-ip 0.0.0.0 --rpc-bind-port 18082 --log-level 4 --disable-rpc-login --confirm-external-bind --daemon-port 18081 --trusted-daemon --password password --shared-ringdb-dir ringdb --testnet --wallet-file testWallet --wallet-dir walletDir

but it occurs error like this ↓

INFO 	net	contrib/epee/include/net/abstract_tcp_server2.inl:802	Set server type to: 1 from name: RPC, prefix_name = RPC
INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 0.0.0.0:18082
DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:731	start accept
DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#0 to 0.0.0.0 currently we have sockets count:1
DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:83	test, connection constructor set m_connection_type=1
DEBUG	net	contrib/epee/include/net/net_helper.h:512	Problems at cancel: wrong file handle
DEBUG	net	contrib/epee/include/net/net_helper.h:515	Problems at shutdown: wrong file handle
WARN 	wallet.rpc	src/wallet/wallet_rpc_server.cpp:3001	Starting wallet RPC server
INFO 	net.http	contrib/epee/include/net/http_server_impl_base.h:89	Run net_service loop( 1 threads)...
DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:827	Run server thread name: RPC
DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:834	JOINING all threads

this error occurs only when I add wallet-dir option on command
it works fine when I add <wallet-file> option instead of <wallet-dir> option

# Discussion History
## moneromooo-monero | 2018-04-04T10:01:25+00:00
Do you have a stack trace in the log showing where the wrong file handle exception comes from ?

## pandakiki11111 | 2018-04-05T01:16:39+00:00
@moneromooo-monero I think it is "invalid file handle" error from windows. That message comes out with Korean. that log is all I got. it copied from < monero-wallet-rpc.log >

## pandakiki11111 | 2018-04-05T02:43:57+00:00
@moneromooo-monero If wallet-dir option added, some file copies to wallet directory??

## moneromooo-monero | 2018-04-05T13:30:20+00:00
New wallets will be put in that directory. I think that's all, but I've not used this before so I'm not sure.

## hyc | 2018-04-05T17:25:55+00:00
The `--wallet-dir` option is mutually exclusive with the `--wallet-file` option, as the `--help` indicates. I suppose we should add an error message for this case, currently there is none and any passed in wallet-file is ignored when wallet-dir is used.

When `--wallet-dir` is used the client must send open_wallet or create_wallet RPC before doing anything else.

## moneromooo-monero | 2018-09-04T23:08:08+00:00
https://github.com/monero-project/monero/pull/4337

## moneromooo-monero | 2018-09-14T11:07:03+00:00
+resolved

# Action History
- Created by: pandakiki11111 | 2018-04-04T08:40:56+00:00
- Closed at: 2018-09-14T11:16:55+00:00
