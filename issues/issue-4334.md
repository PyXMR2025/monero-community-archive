---
title: 'wallet RPC - open_wallet: "Failed to open wallet"/error::invalid_password'
source_url: https://github.com/monero-project/monero/issues/4334
author: el00ruobuob
assignees: []
labels: []
created_at: '2018-09-03T15:04:15+00:00'
updated_at: '2018-09-14T11:32:59+00:00'
type: issue
status: closed
closed_at: '2018-09-14T11:32:59+00:00'
---

# Original Description
Trying to open a newly created wallet through RPC always end with this error.

I tried with and without a password, and both wallets are opening correctly if directly opened either with wallet-cli or wallet-rpc.

curl log when opening the wallet:
```
$ curl -X POST http://localhost:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"open_wallet","params":{"filename":"stage4"}}' -H 'Content-Type: application/json'
{
  "error": {
    "code": -1,
    "message": "Failed to open wallet"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

wallet-rpc log (level 4) at the same time:
```
2018-09-03 15:00:30.349	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1039	handle_accept
2018-09-03 15:00:30.349	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:1045	New server for RPC connections
2018-09-03 15:00:30.349	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:772	set m_connection_type = RPC 
2018-09-03 15:00:30.350	[RPC0]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2018-09-03 15:00:30.350	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:92	test, connection constructor set m_connection_type=1
2018-09-03 15:00:30.350	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:160	[sock 468] new connection from 127.0.0.1:55248 INC to 127.0.0.1:18082, total sockets objects 2
2018-09-03 15:00:30.364	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:616	New connection from host 127.0.0.1: 0
2018-09-03 15:00:30.366	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:630	Setting 00:30:00 expiry
2018-09-03 15:00:30.366	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:284	 connection type RPC 127.0.0.1:18082 <--> 127.0.0.1:55248
2018-09-03 15:00:30.368	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:183	Moving counter buffer by 1 second 0 < 236742 (last time 0)
2018-09-03 15:00:30.368	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:218	Throttle throttle_speed_in: packet of ~220b  (from 220 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [220 0 0 0 0 0 0 0 0 0 ]
2018-09-03 15:00:30.368	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:183	Moving counter buffer by 1 second 0 < 236742 (last time 0)
2018-09-03 15:00:30.368	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:218	Throttle <<< global-IN: packet of ~220b  (from 220 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [220 0 0 0 0 0 0 0 0 0 ]
2018-09-03 15:00:30.369	[RPC0]	TRACE	net.http	contrib/epee/include/net/http_protocol_handler.inl:410	HTTP HEAD:

Host: localhost:18082

User-Agent: curl/7.59.0

Accept: */*

Content-Type: application/json

Content-Length: 80




2018-09-03 15:00:30.369	[RPC0]	DEBUG	wallet.rpc	src/wallet/wallet_rpc_server.h:66	HTTP [127.0.0.1] POST /json_rpc
2018-09-03 15:00:30.378	[RPC0]	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:5832	ringdb path set to C:\ProgramData\.shared-ringdb\stagenet
2018-09-03 15:00:30.450	[RPC0]	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2018-09-03 15:00:30.450	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:3079	!r. THROW EXCEPTION: error::invalid_password
2018-09-03 15:00:30.450	[RPC0]	WARN 	net.http	src/wallet/wallet_errors.h:805	C:/msys64/home/idunk/monero/src/wallet/wallet2.cpp:3079:N5tools5error16invalid_passwordE: invalid password
2018-09-03 15:00:30.455	[RPC0]	DEBUG	net	contrib/epee/include/net/net_helper.h:512	Problems at cancel: Le descripteur de fichier fourni nӥst pas valide
2018-09-03 15:00:30.458	[RPC0]	DEBUG	net	contrib/epee/include/net/net_helper.h:515	Problems at shutdown: Le descripteur de fichier fourni nӥst pas valide
2018-09-03 15:00:30.464	[RPC0]	TRACE	net.http	contrib/epee/include/net/http_protocol_handler.inl:589	HTTP_RESPONSE_HEAD: << 

HTTP/1.1 200 Ok

Server: Epee-based

Content-Length: 115

Content-Type: text/plain

Last-Modified: Mon, 03 Sep 2018 15:00:30 GMT

Accept-Ranges: bytes




2018-09-03 15:00:30.467	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:183	Moving counter buffer by 1 second 0 < 236742 (last time 0)
2018-09-03 15:00:30.471	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:218	Throttle throttle_speed_out: packet of ~154b  (from 154 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [154 0 0 0 0 0 0 0 0 0 ]
2018-09-03 15:00:30.474	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:561	do_send_chunk() NOW SENSD: packet=154 B
2018-09-03 15:00:30.482	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:630	Setting 00:30:00 expiry
2018-09-03 15:00:30.487	[RPC0]	TRACE	net.throttle	contrib/epee/src/network_throttle-detail.cpp:218	Throttle throttle_speed_out: packet of ~115b  (from 115 b) Speed AVG=   0[w=1]    0[w=1] /  Limit=16 KiB/sec  [269 0 0 0 0 0 0 0 0 0 ]
2018-09-03 15:00:30.490	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:546	do_send_chunk() NOW just queues: packet=115 B, is added to queue-size=2
2018-09-03 15:00:30.494	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:549	[127.0.0.1:55248 INC] [sock 468] Async send requested 154
2018-09-03 15:00:30.498	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:630	Setting 00:30:00 expiry
2018-09-03 15:00:30.503	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:712	[127.0.0.1:55248 INC] [sock 468] Async send calledback 154
2018-09-03 15:00:30.508	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:630	Setting 00:30:00 expiry
2018-09-03 15:00:30.512	[RPC0]	DEBUG	net	contrib/epee/include/net/abstract_tcp_server2.inl:747	handle_write() NOW SENDS: packet=115 B, from  queue size=1
2018-09-03 15:00:30.516	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:712	[127.0.0.1:55248 INC] [sock 468] Async send calledback 115
2018-09-03 15:00:30.519	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:358	[sock 468] Some not success at read: End of file:2
2018-09-03 15:00:30.524	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:366	[sock 468] peer closed connection
2018-09-03 15:00:30.530	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:618	Closed connection from host 127.0.0.1: 1
2018-09-03 15:00:30.532	[RPC0]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:105	[sock 468] Socket destroyed
2018-09-03 15:00:30.536	[RPC0]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:171	Destructing connection p2p#0 to 127.0.0.1
```

# Discussion History
## moneromooo-monero | 2018-09-03T17:49:35+00:00
Worked for me. With password "foo".


## el00ruobuob | 2018-09-03T18:38:37+00:00
Will try again tomorrow.

## el00ruobuob | 2018-09-04T07:30:30+00:00
I seems to be a problem of both `--wallet-dir` and `--wallet-file` used in the same time.
While i was using `wallet-file` with an argument of `wallets\<name>\<name>` and `wallet-dir` with an argument of `wallets\`
After copying the wallet file in the `wallets\` directory (without subfolder) it is working fine.

Perhaps would it be good to forbid to use a full path for `--wallet-file` when `--wallet-dir` is in use and only allow filename?

## moneromooo-monero | 2018-09-04T09:20:54+00:00
https://github.com/monero-project/monero/pull/4337

## el00ruobuob | 2018-09-05T12:56:42+00:00
After more tests, it seems the problem is more related to the `--password` flag.
I cannot reproduce the problem by having both `--wallet-dir` and `--wallet-file` if i do not pass a password.
However, it seems that passing both the `--wallet-dir` and `--wallet-file` prevent the wallet from being opened (with or without a password).

## moneromooo-monero | 2018-09-14T11:26:29+00:00
+resolved

# Action History
- Created by: el00ruobuob | 2018-09-03T15:04:15+00:00
- Closed at: 2018-09-14T11:32:59+00:00
