---
title: 'Daemon: net.p2p errors in testnet daemon''s log'
source_url: https://github.com/monero-project/monero/issues/2018
author: iDunk5400
assignees: []
labels: []
created_at: '2017-05-08T20:26:15+00:00'
updated_at: '2017-08-15T23:12:12+00:00'
type: issue
status: closed
closed_at: '2017-08-15T23:12:12+00:00'
---

# Original Description
Running 81b370d on both testnet and mainnet with same uptime, I started seeing net.p2p errors "random_starter_index < peers_local.size() failed!!" today. Log level for both daemons is 1,net.p2p:FATAL and I only see these errors on testnet.
```
2017-05-08 13:34:25.141 [P2P5]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 13:34:38.961 [P2P2]  ERROR   net.p2p src/p2p/net_node.inl:745        [107.167.87.242:28080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-05-08 13:34:38.961 [P2P5]  ERROR   net.p2p src/p2p/net_node.inl:794        [107.167.87.242:28080 OUT] COMMAND_HANDSHAKE Failed
2017-05-08 13:37:21.939 [P2P6]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 13:50:07.610 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 14:17:14.445 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 14:20:49.004 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 14:38:02.444 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 14:45:04.758 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 15:03:30.545 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 15:04:46.271 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 15:29:28.821 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 15:46:16.930 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 16:00:32.414 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 16:08:33.530 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 16:11:03.392 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 16:42:10.536 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 17:13:52.430 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 17:46:11.949 [P2P1]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 17:57:16.509 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 18:00:04.629 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 18:58:03.553 [P2P2]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 19:34:42.151 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:819        [213.152.162.99:30996 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-05-08 20:02:35.323 [P2P9]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 20:07:42.972 [P2P8]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 20:36:05.496 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
status
Height: 906807/906807 (100.0%) on testnet, not mining, net hash 240 H/s, v5, up to date, 7(out)+0(in) connections, uptime 3d 8h 38m 12s
2017-05-08 21:00:34.813 [P2P8]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
2017-05-08 21:11:10.388 [P2P8]  ERROR   net.p2p src/p2p/net_node.inl:1121       random_starter_index < peers_local.size() failed!!
status
Height: 906836/906836 (100.0%) on testnet, not mining, net hash 239 H/s, v5, up to date, 7(out)+0(in) connections, uptime 3d 9h 35m 16s
```
I asked @moneromooo-monero about it, and he thinks the errors might be related to PR #1701 since that PR touches code in that general area.
The errors started appearing around the time of my daily internet reconnection, after about 3 days uptime.

# Discussion History
## moneromooo-monero | 2017-05-08T20:31:25+00:00
After looking at the code, I'm not sure it's to do with that PR anymore.

The code in make_new_connection_from_peerlist sets a max_random_index local, then proceeds to a loop which calls, among other things, try_to_connect_and_handshake_with_new_peer. This function can call append_with_peer_white and append_with_peer_anchor. These functions will modify the size of the white/anchor (and possibly gray) lists. This will then change the notional value of max_random_index, but not the cached value.


## moneromooo-monero | 2017-08-15T23:11:08+00:00
+resolved

# Action History
- Created by: iDunk5400 | 2017-05-08T20:26:15+00:00
- Closed at: 2017-08-15T23:12:12+00:00
