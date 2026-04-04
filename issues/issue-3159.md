---
title: Monerod does not exit with a 0 exit code on successful shutdown
source_url: https://github.com/monero-project/monero/issues/3159
author: muff1nman
assignees: []
labels: []
created_at: '2018-01-20T03:25:33+00:00'
updated_at: '2018-02-18T19:29:48+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:29:48+00:00'
---

# Original Description
After successful shutdown:

```
2018-01-20 03:24:10.523	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:80	p2p net loop stopped
2018-01-20 03:24:10.536	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:78	Stopping core rpc server...
2018-01-20 03:24:10.536	[SRV_MAIN]	INFO 	global	src/daemon/daemon.cpp:145	Node stopped.
2018-01-20 03:24:10.536	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:90	Deinitializing rpc server...
2018-01-20 03:24:10.536	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-01-20 03:24:10.537	[SRV_MAIN]	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2018-01-20 03:24:10.558	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2018-01-20 03:24:10.558	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
```

The exit code should be 0, but it is 1:

```
$ echo $?
1
```

# Discussion History
## moneromooo-monero | 2018-01-20T10:42:54+00:00
https://github.com/monero-project/monero/pull/3161

## moneromooo-monero | 2018-02-18T19:22:22+00:00
+resolved

# Action History
- Created by: muff1nman | 2018-01-20T03:25:33+00:00
- Closed at: 2018-02-18T19:29:48+00:00
