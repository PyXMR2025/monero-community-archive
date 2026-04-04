---
title: Cannot connect to any peers in a testnet
source_url: https://github.com/monero-project/monero/issues/2819
author: Revinand
assignees: []
labels: []
created_at: '2017-11-15T12:29:15+00:00'
updated_at: '2017-11-15T14:40:39+00:00'
type: issue
status: closed
closed_at: '2017-11-15T14:40:39+00:00'
---

# Original Description
I upgraded my node to the latest version (0.11.1.0) and everything is working good in mainnet, but there is a problem with connection in the testnet (stacked on 1039873 block). Logs cluttered with:


```
2017-11-15 12:19:03.742	[P2P1]	WARN 	net.p2p	src/p2p/net_node.inl:808	[*.*.*.*:28080 OUT] COMMAND_HANDSHAKE Failed
2017-11-15 12:19:03.743	[P2P1]	INFO 	net.p2p	src/p2p/net_node.inl:985	[*.*.*.*:28080 OUT] Failed to HANDSHAKE with peer *.*.*.*:28080
```
For all peers node tries to connect.

Tried to set priority node to testnet.xmrchain.com with no luck.
Tried to sync from the scratch. The same effect.

Also there is a strange message appears all the time:

```
2017-11-15 12:23:06.616	[P2P3]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:342	[sock 21] Some not success at read: End of file:2
2017-11-15 12:23:07.754	[P2P3]	TRACE	net	contrib/epee/include/net/abstract_tcp_server2.inl:98	[sock 22] Socket destroyed
```

Node is running from the docker container like this:

```
$ monerod --testnet --rpc-bind-ip 0.0.0.0 --p2p-bind-ip 0.0.0.0 --add-priority-node 192.110.160.146:28080 --block-sync-size 10 --confirm-external-bind --non-interactive
```

What should I do to sync?

# Discussion History
## moneromooo-monero | 2017-11-15T14:14:48+00:00
The first logs are normal. Not sure about the second. I'd make sure your p2pstate.bin is removed, in case it has lots of obsolete peers which would take time to go through, but even then you should stil get the priority node (assuming it's up). Try 162.213.38.63:28080, which I know is up, just in case. Also please post the output of "status".


## Revinand | 2017-11-15T14:40:39+00:00
@moneromooo-monero thanks a lot! p2pstate.bin file removal and setting the node you've provided as priority node did help!

# Action History
- Created by: Revinand | 2017-11-15T12:29:15+00:00
- Closed at: 2017-11-15T14:40:39+00:00
