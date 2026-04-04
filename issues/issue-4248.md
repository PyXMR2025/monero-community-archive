---
title: Failed to connect to any peers or seeds
source_url: https://github.com/monero-project/monero/issues/4248
author: jwm1969
assignees: []
labels: []
created_at: '2018-08-11T17:45:53+00:00'
updated_at: '2018-08-11T21:38:41+00:00'
type: issue
status: closed
closed_at: '2018-08-11T21:38:00+00:00'
---

# Original Description
Everything was working well until a couple of days ago.

started with:

./monerod --log-level 1,net.p2p:DEBUG

What does handshake failed mean?

Output:

2018-08-11 17:43:10.680	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:815	Random connection index=4(x=12, max_index=20)
2018-08-11 17:43:10.680	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1102	Considering connecting (out) to peer: 5985d76b2c8ee7c5 58.220.30.108:18080
2018-08-11 17:43:10.680	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1117	Selected peer: 5985d76b2c8ee7c5 58.220.30.108:18080[peer_list=1] last_seen: d1.h23.m45.s36
2018-08-11 17:43:10.681	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:905	Connecting to 58.220.30.108:18080(peer_type=1, last_seen: d1.h23.m45.s36)...
2018-08-11 17:43:10.681	[P2P0]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#1 to 0.0.0.0 currently we have sockets count:2
2018-08-11 17:43:10.790	[P2P1]	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-08-11 17:43:15.685	[P2P0]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:171	Destructing connection p2p#1 to 0.0.0.0
2018-08-11 17:43:15.685	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:921	[0.0.0.0:0 OUT] Connect failed to 58.220.30.108:18080
2018-08-11 17:43:15.685	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1120	Handshake failed
2018-08-11 17:43:15.685	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:815	Random connection index=5(x=13, max_index=20)
2018-08-11 17:43:15.685	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1102	Considering connecting (out) to peer: 3de2d94d7b7a7be3 184.72.107.81:18080
2018-08-11 17:43:15.685	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1117	Selected peer: 3de2d94d7b7a7be3 184.72.107.81:18080[peer_list=1] last_seen: d1.h23.m45.s42
2018-08-11 17:43:15.685	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:905	Connecting to 184.72.107.81:18080(peer_type=1, last_seen: d1.h23.m45.s42)...
2018-08-11 17:43:15.685	[P2P0]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#2 to 0.0.0.0 currently we have sockets count:2
2018-08-11 17:43:20.272	[P2P0]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:171	Destructing connection p2p#2 to 0.0.0.0
2018-08-11 17:43:20.272	[P2P0]	INFO 	net.p2p	src/p2p/net_node.inl:921	[0.0.0.0:0 OUT] Connect failed to 184.72.107.81:18080
2018-08-11 17:43:20.272	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1120	Handshake failed
2018-08-11 17:43:20.273	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:815	Random connection index=0(x=6, max_index=20)
2018-08-11 17:43:20.273	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1102	Considering connecting (out) to peer: 6fed5918ca9b6415 128.199.252.162:18080
2018-08-11 17:43:20.273	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:1117	Selected peer: 6fed5918ca9b6415 128.199.252.162:18080[peer_list=1] last_seen: d1.h23.m45.s8
2018-08-11 17:43:20.273	[P2P0]	DEBUG	net.p2p	src/p2p/net_node.inl:905	Connecting to 128.199.252.162:18080(peer_type=1, last_seen: d1.h23.m45.s8)...
2018-08-11 17:43:20.273	[P2P0]	DEBUG	net.p2p	contrib/epee/src/connection_basic.cpp:163	Spawned connection p2p#3 to 0.0.0.0 currently we have sockets count:2

# Discussion History
## jwm1969 | 2018-08-11T21:38:00+00:00
Closing issue, exported and then imported lmdb and rolled back to 12.3.0 release binary instead of my own compile and its working again; something i did wrong i am sure.

# Action History
- Created by: jwm1969 | 2018-08-11T17:45:53+00:00
- Closed at: 2018-08-11T21:38:00+00:00
