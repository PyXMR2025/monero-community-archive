---
title: ERROR daemon src/daemon/main.cpp:288 Exception in main! Failed to initialize
  p2p server.
source_url: https://github.com/monero-project/monero/issues/3755
author: xnulliver
assignees: []
labels:
- invalid
created_at: '2018-05-05T14:58:49+00:00'
updated_at: '2018-08-15T12:17:04+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:17:04+00:00'
---

# Original Description
`
2018-05-05 14:53:32.699	    7f782350bec0	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-05-05 14:53:32.699	    7f782350bec0	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-05-05 14:53:32.700	    7f782350bec0	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-05-05 14:53:32.700	    7f782350bec0	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-05-05 14:53:45.017	    7f782350bec0	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-05-05 14:53:45.021	    7f782350bec0	ERROR	daemon	src/daemon/core.h:108	Failed to deinitialize core...
2018-05-05 14:53:45.021	    7f782350bec0	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-05-05 14:53:45.022	    7f782350bec0	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-05-05 14:53:45.022	    7f782350bec0	ERROR	daemon	src/daemon/main.cpp:288	Exception in main! Failed to initialize p2p server.

`

As described in #2361 i tried to fix it with:
`./monerod exit`
but no deamon is running:
`Error: Couldn't connect to daemon: 127.0.0.1:18081`

# Discussion History
## moneromooo-monero | 2018-05-05T15:28:45+00:00
Start with --log-level 1
Also check whether it's already running.

## dEBRUYNE-1 | 2018-05-06T11:40:34+00:00
This typically indicates you already have a `monerod` running. Could you check your process list? 

## moneromooo-monero | 2018-06-20T21:54:50+00:00
ping

Also, are you running it from some kind of watchdog like upstart, systemd, or the like, and did not tell us ?

## moneromooo-monero | 2018-07-19T21:45:20+00:00
I'm going to close this unless there's a reply soon.

## moneromooo-monero | 2018-08-15T11:29:13+00:00
+invalid

# Action History
- Created by: xnulliver | 2018-05-05T14:58:49+00:00
- Closed at: 2018-08-15T12:17:04+00:00
