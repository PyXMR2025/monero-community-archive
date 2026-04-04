---
title: Docker container exits immediately..
source_url: https://github.com/monero-project/monero/issues/4034
author: j4ys0n
assignees: []
labels: []
created_at: '2018-06-20T19:22:41+00:00'
updated_at: '2018-06-21T21:19:46+00:00'
type: issue
status: closed
closed_at: '2018-06-21T21:19:46+00:00'
---

# Original Description
Are there instructions for running the docker container built from the Dockerfile in this repo? I can't find them anywhere.

here's my start command: `sudo docker run -d -v ~/xmr-data:/root/.bitmonero -v ~/xmr-wallet:/wallet -p 18080:18080 -p 18081:18081 --name xmr xmr`

here's the output from the logs. it starts up and exits right away.. what am I missing?
```
2018-06-20 19:18:34.155	    7f23157b4740	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-master-896512b)
2018-06-20 19:18:34.155	    7f23157b4740	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-06-20 19:18:34.155	    7f23157b4740	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-06-20 19:18:34.156	    7f23157b4740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-06-20 19:18:38.393	    7f23157b4740	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-06-20 19:18:38.394	    7f23157b4740	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-06-20 19:18:38.394	    7f23157b4740	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 0.0.0.0:18081
2018-06-20 19:18:38.394	    7f23157b4740	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-06-20 19:18:38.394	    7f23157b4740	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-06-20 19:18:38.394	    7f23157b4740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:426	Loading blockchain from folder /root/.bitmonero/lmdb ...
2018-06-20 19:18:38.408	    7f23157b4740	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:525	Loading checkpoints
2018-06-20 19:18:38.444	    7f23157b4740	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-06-20 19:18:38.444	    7f23157b4740	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-06-20 19:18:38.444	    7f23157b4740	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-06-20 19:18:38.444	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-06-20 19:18:38.444	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-06-20 19:18:38.444	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-06-20 19:18:39.448	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-06-20 19:18:39.448	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:189	Node stopped.
2018-06-20 19:18:39.448	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-06-20 19:18:39.448	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-06-20 19:18:43.453	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-06-20 19:18:43.455	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-06-20 19:18:43.456	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
```

# Discussion History
## moneromooo-monero | 2018-06-20T21:45:59+00:00
Try with --non-interactive

## j4ys0n | 2018-06-20T22:53:10+00:00
does that make it so that i can't interact with the node? the docs just say "turn on non-interactive mode" but that's not very descriptive. will i be able to import wallets?

## moneromooo-monero | 2018-06-21T08:45:56+00:00
You can interact with the node, just not via its command line console. It has RPC, which can be used via, eg: monerod status, which calls the running daemon. You can't import  wallets in monerod, whether it is in interactive mode or not.

# Action History
- Created by: j4ys0n | 2018-06-20T19:22:41+00:00
- Closed at: 2018-06-21T21:19:46+00:00
