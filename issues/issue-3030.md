---
title: Transaction verification failed in cryptonote_core.cpp (still running a pool)
source_url: https://github.com/monero-project/monero/issues/3030
author: sleever
assignees: []
labels:
- invalid
created_at: '2017-12-29T19:09:54+00:00'
updated_at: '2017-12-30T01:08:25+00:00'
type: issue
status: closed
closed_at: '2017-12-30T01:08:25+00:00'
---

# Original Description
Hello everybody,

Yesterday I already posted the issue regarding https://github.com/monero-project/monero/issues/3023 where I suddenly got the error "transaction in pool not found". Because of this issue I have increased the logging of the daemon to level 1 so that I could receive more information.

The issue still concerns the Electroneum wallet and I will also post this question over there.

Upon doing so I stumbled on a very large number of errors regarding "transaction verification failed" and LEVIN_ERROR_CONNECTION_TIMEDOUT.

Again I would like to ask whether this is considered normal and/or could have anything to do with not finding any blocks.

Next to that I would like to know how to fix these kind of issues.

The wallet is up to date and synced up with the chain as the status determines:

Height: 89111/89111 (100.0%) on mainnet, not mining, net hash 196.37 MH/s, v1, up to date, 51(out)+19(in) connections, uptime 0d 2h 39m 40s

The error log:

`2017-12-29 18:55:15.069 [P2P4]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:289     [93.80.176.132:26967 OUT] [levin_protocol] -->> start_outer_call failed
2017-12-29 18:55:15.366 [P2P5]  ERROR   verify  src/cryptonote_core/blockchain.cpp:2557 Key image already spent in blockchain: 64414688cf5b4da9092a1738ab988a1c35edb1b539127b6b59718f470a10fb4b
2017-12-29 18:55:15.380 [P2P5]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <6aedb8f8af159734bf1845fbefde09b6a063183072e13676a5f7415b5c124d5e>
2017-12-29 18:55:19.758 [P2P5]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:289     [93.80.176.132:26967 OUT] [levin_protocol] -->> start_outer_call failed
2017-12-29 18:55:34.549 [P2P4]  WARN    net.p2p src/p2p/net_node.inl:756        [46.240.204.217:26967 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-12-29 18:55:34.549 [P2P7]  WARN    net.p2p src/p2p/net_node.inl:805        [46.240.204.217:26967 OUT] COMMAND_HANDSHAKE Failed
2017-12-29 18:55:54.259 [P2P8]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <3036cecf6f9ae5d7bf12198460607550445815e6fde869adc6933220c99f4c1e>
2017-12-29 18:55:55.309 [P2P6]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <20668e0faaa65a2f6a265a311299b1d3599682d7a5ac83919a9dc221ea7f9d64>
2017-12-29 18:56:03.541 [P2P9]  WARN    net.p2p src/p2p/net_node.inl:1564       [0.0.0.0:0 OUT] back ping connect failed to 108.180.35.235:26967
2017-12-29 18:56:54.474 [P2P4]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <c1c1b4c22e18eeecef6632bb63376b270f81ee6bc003c8eac13bd0e2086feef2>
2017-12-29 18:56:56.528 [P2P3]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <d4311f5dd1662b0eeb88e7fa8dc4218d42fc5f613737e40e040238ba5f457d0c>
2017-12-29 18:56:56.528 [P2P7]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <d4311f5dd1662b0eeb88e7fa8dc4218d42fc5f613737e40e040238ba5f457d0c>
2017-12-29 18:57:02.719 [P2P6]  WARN    net.p2p src/p2p/net_node.inl:1564       [0.0.0.0:0 OUT] back ping connect failed to 116.102.2.65:26967
2017-12-29 18:57:03.175 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:1564       [0.0.0.0:0 OUT] back ping connect failed to 84.22.48.109:26967
2017-12-29 18:57:04.905 [P2P1]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <7e5c437e5fb486c26cd4021fc36e502931f2529d84ce8872ea3a55007fddc351>
2017-12-29 18:57:04.906 [P2P8]  ERROR   net     contrib/epee/include/net/levin_protocol_handler_async.h:289     [94.181.116.182:54047 INC] [levin_protocol] -->> start_outer_call failed
2017-12-29 18:57:14.959 [P2P2]  WARN    net.p2p src/p2p/net_node.inl:756        [185.228.232.221:26967 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-12-29 18:57:14.959 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:805        [185.228.232.221:26967 OUT] COMMAND_HANDSHAKE Failed
2017-12-29 18:57:24.974 [P2P7]  WARN    net.p2p src/p2p/net_node.inl:1564       [0.0.0.0:0 OUT] back ping connect failed to 34.204.167.160:26967
2017-12-29 18:57:44.182 [P2P0]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <1964054836de9be90c097c605c31a3697cf648a8355ffd64e76138e06c253049>
2017-12-29 18:57:45.864 [P2P3]  WARN    net.p2p src/p2p/net_node.inl:1564       [0.0.0.0:0 OUT] back ping connect failed to 82.202.160.196:26967
2017-12-29 18:58:04.128 [P2P1]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <7195690e725791dd13331fa540b03abe63a53d76abef89ff9f5ee291d357a0f7>
2017-12-29 18:58:06.909 [P2P0]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <866148d4e8911376ea123febd845a7a0e3718cc8048690e951a5cce29530c462>
2017-12-29 18:58:08.540 [P2P7]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <3e35cae6f2729d84ff036a5edd750779d741505a398ad457834f0776489b5a09>
2017-12-29 18:58:18.467 [P2P5]  WARN    net.p2p src/p2p/net_node.inl:1564       [0.0.0.0:0 OUT] back ping connect failed to 88.200.214.46:26967
2017-12-29 18:58:21.157 [P2P0]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <7a1d338c1a4564a65fb7387815747536982a14869b4deee74c05ee1e3d3e3f74>
2017-12-29 18:58:26.694 [P2P4]  ERROR   verify  src/cryptonote_core/cryptonote_core.cpp:653     Transaction verification failed: <556ff1d4c83d1460aedb99ed54c538b317fa9351f59d229927dd42f7b00eebd2>`

Again, thanks a lot for your time to look into this.

Best regards,

# Discussion History
## moneromooo-monero | 2017-12-29T19:57:02+00:00
Txes can fail for many reasons. Maybe your blockchain is corrupt and gives bad info. Or maybe the txes are indeed invalid. set_log 1 will tell you more about why a tx is invalid. The timeouts are usually fine.

## hyc | 2017-12-29T23:47:23+00:00
His log clearly says "Key image already spent" so that txn is obviously invalid.

## moneromooo-monero | 2017-12-30T00:32:04+00:00
Ah indeed it does for the first one. Though not the other ones.

## moneromooo-monero | 2017-12-30T01:07:51+00:00
Anyway, regardless, this is a bug tracker, not a helpdesk.

+invalid


# Action History
- Created by: sleever | 2017-12-29T19:09:54+00:00
- Closed at: 2017-12-30T01:08:25+00:00
