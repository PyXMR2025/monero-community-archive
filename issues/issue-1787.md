---
title: Error net.p2p
source_url: https://github.com/monero-project/monero/issues/1787
author: keatond
assignees: []
labels: []
created_at: '2017-02-24T01:01:00+00:00'
updated_at: '2017-02-26T17:27:40+00:00'
type: issue
status: closed
closed_at: '2017-02-26T17:27:40+00:00'
---

# Original Description
Good Evening Monero Developers!

Running monerod.exe as admin and am getting the below errors. Hope this helps with development!

2017-02-23 19:23:37.735 [P2P3]  ERROR   net.p2p src/p2p/net_node.inl:1461       [86.135.71.248:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:24:39.895 [P2P7]  ERROR   net.p2p src/p2p/net_node.inl:1461       [61.91.122.189:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:28:59.455 [P2P1]  ERROR   net.p2p src/p2p/net_node.inl:1461       [65.110.26.18:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:28:59.471 [P2P4]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:257     [65.110.26.18:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-02-23 19:29:34.051 [P2P1]  ERROR   ringct  src/ringct/rctOps.cpp:264       ge_frombytes_vartime failed at 264
2017-02-23 19:29:34.066 [P2P1]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:666     rct signature semantics check failed
2017-02-23 19:31:07.024 [P2P5]  ERROR   net.p2p src/p2p/net_node.inl:1461       [199.244.51.97:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:31:07.040 [P2P3]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:257     [199.244.51.97:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-02-23 19:32:13.168 [P2P3]  ERROR   net.p2p src/p2p/net_node.inl:724        [93.228.10.48:18080 OUT] COMMAND_HANDSHAKE invoke failed. (fffffffc, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-02-23 19:32:13.168 [P2P1]  ERROR   net.p2p src/p2p/net_node.inl:773        [93.228.10.48:18080 OUT] COMMAND_HANDSHAKE Failed
2017-02-23 19:33:14.453 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:1461       [69.43.206.102:18084 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:34:16.847 [P2P3]  ERROR   net.p2p src/p2p/net_node.inl:1461       [176.9.147.178:8180 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:35:18.303 [P2P3]  ERROR   net.p2p src/p2p/net_node.inl:1461       [5.135.120.51:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:35:18.319 [P2P1]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:257     [5.135.120.51:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-02-23 19:38:32.297 [P2P6]  ERROR   net.p2p src/p2p/net_node.inl:1461       [76.66.169.216:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (fffffffd, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-02-23 19:38:32.297 [P2P5]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:257     [76.66.169.216:18080 OUT] [levin_protocol] -->> start_outer_call failed
2017-02-23 19:45:08.615 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:724        [76.9.81.205:18080 OUT] COMMAND_HANDSHAKE invoke failed. (fffffffc, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-02-23 19:45:08.615 [P2P5]  ERROR   net.p2p src/p2p/net_node.inl:773        [76.9.81.205:18080 OUT] COMMAND_HANDSHAKE Failed

# Discussion History
## moneromooo-monero | 2017-02-24T01:38:40+00:00
Thanks for reporting. These are normal and ignorable.

# Action History
- Created by: keatond | 2017-02-24T01:01:00+00:00
- Closed at: 2017-02-26T17:27:40+00:00
