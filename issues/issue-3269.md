---
title: error in ./monero
source_url: https://github.com/monero-project/monero/issues/3269
author: isaack0815
assignees: []
labels:
- invalid
created_at: '2018-02-15T06:40:49+00:00'
updated_at: '2018-06-20T09:41:06+00:00'
type: issue
status: closed
closed_at: '2018-06-20T09:41:06+00:00'
---

# Original Description
hay,

i run the ./monerd and have this error:

> 2018-02-15 06:38:35.184	    7f7f4c230740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-02-15 06:38:35.184	    7f7f4c230740	INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2018-02-15 06:38:35.184	    7f7f4c230740	INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2018-02-15 06:38:35.185	    7f7f4c230740	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-02-15 06:38:35.675	    7f7f4c230740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2018-02-15 06:38:35.679	    7f7f4c230740	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2018-02-15 06:38:35.679	    7f7f4c230740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2018-02-15 06:38:35.679	    7f7f4c230740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
2018-02-15 06:38:35.679	    7f7f4c230740	ERROR	daemon	src/daemon/main.cpp:287	Exception in main! Failed to initialize p2p server.


# Discussion History
## leonklingele | 2018-02-15T06:43:45+00:00
Try to start with `--log-level 1`.

## moneromooo-monero | 2018-02-15T08:12:14+00:00
Looks like you're running another monerod already. If you really intend to run another one, bind to other ports (--p2p-bind-port, --rpc-bind-port, and possibly --zmq-rpc-bind-port).

## moneromooo-monero | 2018-05-16T11:09:50+00:00
If no further comment, I'll assume this is the "port is in use" thing again, which should now be visible by default, and close this.

## moneromooo-monero | 2018-06-20T09:05:41+00:00
No further response, no way to know whether it's a bug or not.
+invalid


# Action History
- Created by: isaack0815 | 2018-02-15T06:40:49+00:00
- Closed at: 2018-06-20T09:41:06+00:00
