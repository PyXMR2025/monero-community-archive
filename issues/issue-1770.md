---
title: 'Peering issues, can we fix with some kind of version # in the initial peering
  handshake?'
source_url: https://github.com/monero-project/monero/issues/1770
author: Gingeropolous
assignees: []
labels: []
created_at: '2017-02-22T02:25:13+00:00'
updated_at: '2017-09-02T12:42:19+00:00'
type: issue
status: closed
closed_at: '2017-09-02T12:42:19+00:00'
---

# Original Description
A lot of people running the new software end up connected to bad nodes - nodes that haven't updated in forever. I hypothesize that noobs aren't even able to sync with the network because they end up in a bad-peer blackhole, where they only connect to bad peers, and then they end up getting banned by good nodes. Total conjecture here, but there have definitely been people that have a real hard time synchronizing their daemons. 

This is likely to continue as we keep forking. 

Can't we just add a thing wherein the node asks the peer-node which version of Monerod its running? 

The only downside is that a malicious entity could intentionally run bad nodes with "new" version info. But I don't think thats a problem, because the version check would just be a first-line of evaluation. After a peer passes this line, it then continues with its standard operations.

This would just drop all the crap nodes off the network.  

# Discussion History
## moneroexamples | 2017-02-22T21:38:44+00:00
The handshake error occur not only with old nodes. I run private monero testnet network for tests, with all nodes being of exactly same version v0.10.1.0-3f171b93. 

```
Height: 322/322 (100.0%) on testnet, mining at 61 H/s, net hash 55 H/s, v4, up to date, 2(out)+1(in) connections, uptime 0d 0h 2m 29s
```

The handshake error also appears despite same version being used, but network seems working.
```
2017-02-23 05:31:36.659	[P2P2]	ERROR	net.p2p	src/p2p/net_node.inl:718	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-02-23 05:31:36.659	[P2P0]	ERROR	net.p2p	src/p2p/net_node.inl:767	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE Failed
2017-02-23 05:32:11.661	[P2P6]	ERROR	net.p2p	src/p2p/net_node.inl:718	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-02-23 05:32:11.661	[P2P3]	ERROR	net.p2p	src/p2p/net_node.inl:767	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE Failed
2017-02-23 05:32:46.662	[P2P9]	ERROR	net.p2p	src/p2p/net_node.inl:718	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-02-23 05:32:46.662	[P2P4]	ERROR	net.p2p	src/p2p/net_node.inl:767	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE Failed
2017-02-23 05:33:21.663	[P2P3]	ERROR	net.p2p	src/p2p/net_node.inl:718	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-02-23 05:33:21.663	[P2P2]	ERROR	net.p2p	src/p2p/net_node.inl:767	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE Failed
2017-02-23 05:33:56.664	[P2P9]	ERROR	net.p2p	src/p2p/net_node.inl:718	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-02-23 05:33:56.664	[P2P8]	ERROR	net.p2p	src/p2p/net_node.inl:767	[127.0.0.1:48080 OUT] COMMAND_HANDSHAKE Failed
```

The errors dont show with `set_log 0` though. 

## iamsmooth | 2017-03-05T17:30:44+00:00
> I hypothesize that noobs aren't even able to sync with the network because they end up in a bad-peer blackwhole, where they only connect to bad peers, and then they end up getting banned by good nodes. 

This should never happen. If it does happen it is evidence of a bug.

If you ever connect to even one good peer that should be enough.


## moneromooo-monero | 2017-09-02T12:36:43+00:00
Nodes now send the ideal version for their top height, which serves as a "fork version number", and connections are dropped if this doesn't match what the other side thinks it should be.

+resolved


# Action History
- Created by: Gingeropolous | 2017-02-22T02:25:13+00:00
- Closed at: 2017-09-02T12:42:19+00:00
