---
title: Node stops syncing at 2210720
source_url: https://github.com/monero-project/monero/issues/6926
author: bitcodernull
assignees: []
labels: []
created_at: '2020-10-21T05:42:38+00:00'
updated_at: '2020-10-21T06:28:05+00:00'
type: issue
status: closed
closed_at: '2020-10-21T06:28:05+00:00'
---

# Original Description
 the log is as follows:

2020-10-21 05:41:36.619	[P2P6]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.238:18080 OUT] 10 bytes sent for category command-1003 initiated by us
2020-10-21 05:41:37.189	[P2P2]	INFO	net.p2p	src/p2p/net_node.inl:2420	[162.218.65.239:62424 f49238d4-dc3a-4b03-a8a8-e43e22c5cfa9 INC] NEW CONNECTION
2020-10-21 05:41:37.732	[P2P7]	WARNING	net.p2p	src/p2p/net_node.inl:2164	[162.218.65.238:18080 OUT] back ping invoke wrong response "OK" from162.218.65.238:18080, hsh_peer_id=5566169844332725069, rsp.peer_id=a0fa01ab3c3af277
2020-10-21 05:41:37.732	[P2P2]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.239:62424 INC] 227 bytes received for category command-1001 initiated by peer
2020-10-21 05:41:37.732	[P2P7]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:765	Setting timer on a shut down object
2020-10-21 05:41:37.732	[P2P7]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2676	[162.218.65.238:18080 OUT] [0] state: closed in state before_handshake
2020-10-21 05:41:37.732	[P2P7]	INFO	net.p2p	src/p2p/net_node.inl:2436	[162.218.65.238:18080 2258493b-8e06-4fa1-a5bd-83d8f27d7fef OUT] CLOSE CONNECTION
2020-10-21 05:41:37.732	[P2P2]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.239:62424 INC] 10 bytes sent for category command-1007 initiated by us
2020-10-21 05:41:37.734	[P2P2]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.239:62424 INC] 14211 bytes sent for category command-1001 initiated by peer
2020-10-21 05:41:37.899	[P2P4]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.89.181.95:3448 OUT] 10 bytes received for category command-1003 initiated by peer
2020-10-21 05:41:37.899	[P2P4]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.89.181.95:3448 OUT] 38 bytes sent for category command-1003 initiated by peer
2020-10-21 05:41:38.138	[P2P8]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.75.102.208:5769 OUT] 10 bytes received for category command-1003 initiated by peer
2020-10-21 05:41:38.138	[P2P8]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.75.102.208:5769 OUT] 38 bytes sent for category command-1003 initiated by peer
2020-10-21 05:41:38.222	[P2P9]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.239:62424 INC] 29 bytes received for category command-1007 initiated by us
2020-10-21 05:41:38.501	[P2P0]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2676	[162.218.65.239:62424 INC] [0] state: closed in state normal
2020-10-21 05:41:38.501	[P2P0]	INFO	net.p2p	src/p2p/net_node.inl:2436	[162.218.65.239:62424 f49238d4-dc3a-4b03-a8a8-e43e22c5cfa9 INC] CLOSE CONNECTION
2020-10-21 05:41:38.726	[P2P4]	INFO	net.p2p	src/p2p/net_node.inl:2420	[162.218.65.240:33991 e7f24411-014d-4424-949e-09e87ddb309f INC] NEW CONNECTION
2020-10-21 05:41:38.940	[P2P3]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.255.233.156:8502 OUT] 10 bytes received for category command-1003 initiated by peer
2020-10-21 05:41:38.940	[P2P3]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.255.233.156:8502 OUT] 38 bytes sent for category command-1003 initiated by peer
2020-10-21 05:41:39.044	[P2P8]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.240:33991 INC] 227 bytes received for category command-1001 initiated by peer
2020-10-21 05:41:39.044	[P2P8]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.240:33991 INC] 10 bytes sent for category command-1007 initiated by us
2020-10-21 05:41:39.046	[P2P8]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.240:33991 INC] 14154 bytes sent for category command-1001 initiated by peer
2020-10-21 05:41:39.575	[P2P0]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.240:33991 INC] 29 bytes received for category command-1007 initiated by us
2020-10-21 05:41:39.732	[P2P6]	WARNING	net.p2p	src/p2p/net_node.inl:2136	[<none> OUT] back ping connect failed to 162.218.65.239:18081
2020-10-21 05:41:39.812	[P2P7]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2676	[162.218.65.240:33991 INC] [0] state: closed in state normal
2020-10-21 05:41:39.812	[P2P7]	INFO	net.p2p	src/p2p/net_node.inl:2436	[162.218.65.240:33991 e7f24411-014d-4424-949e-09e87ddb309f INC] CLOSE CONNECTION
2020-10-21 05:41:40.726	[P2P8]	INFO	net.p2p	src/p2p/net_node.inl:2420	[162.218.65.241:56663 dc5867a7-ce1c-4892-baec-2ddf0af8cf22 INC] NEW CONNECTION
2020-10-21 05:41:40.947	[P2P4]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.241:56663 INC] 227 bytes received for category command-1001 initiated by peer
2020-10-21 05:41:40.948	[P2P4]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.241:56663 INC] 10 bytes sent for category command-1007 initiated by us
2020-10-21 05:41:40.949	[P2P4]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.241:56663 INC] 14026 bytes sent for category command-1001 initiated by peer
2020-10-21 05:41:41.044	[P2P6]	WARNING	net.p2p	src/p2p/net_node.inl:2136	[<none> OUT] back ping connect failed to 162.218.65.240:18080
2020-10-21 05:41:41.486	[P2P0]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[162.218.65.241:56663 INC] 29 bytes received for category command-1007 initiated by us
2020-10-21 05:41:41.492	[P2P3]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[54.39.75.71:12674 OUT] 10 bytes received for category command-1003 initiated by peer
2020-10-21 05:41:41.492	[P2P3]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[54.39.75.71:12674 OUT] 38 bytes sent for category command-1003 initiated by peer
2020-10-21 05:41:41.727	[P2P7]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2676	[162.218.65.241:56663 INC] [0] state: closed in state normal
2020-10-21 05:41:41.727	[P2P7]	INFO	net.p2p	src/p2p/net_node.inl:2436	[162.218.65.241:56663 dc5867a7-ce1c-4892-baec-2ddf0af8cf22 INC] CLOSE CONNECTION
2020-10-21 05:41:42.312	[P2P6]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.79.11.199:6771 OUT] 10 bytes received for category command-1003 initiated by peer
2020-10-21 05:41:42.312	[P2P6]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.79.11.199:6771 OUT] 38 bytes sent for category command-1003 initiated by peer
^C

# Discussion History
## ghost | 2020-10-21T06:03:21+00:00
https://www.reddit.com/r/Monero/comments/jdp770/cli_v01711_oxygen_orion_released_fixes_block/

## bitcodernull | 2020-10-21T06:28:01+00:00
thanks
it works now

# Action History
- Created by: bitcodernull | 2020-10-21T05:42:38+00:00
- Closed at: 2020-10-21T06:28:05+00:00
