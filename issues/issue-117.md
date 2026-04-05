---
title: '[BUG] Can''t sync finish syncing testnet'
source_url: https://github.com/seraphis-migration/monero/issues/117
author: bobXMR
assignees: []
labels: []
created_at: '2025-09-29T19:05:39+00:00'
updated_at: '2025-10-03T16:20:37+00:00'
type: issue
status: closed
closed_at: '2025-10-03T16:20:37+00:00'
---

# Original Description
- Windows 11 Pro x64 24H2 OS Build 26100.6584
- Daemon Latest version: https://github.com/seraphis-migration/monero/releases/download/v0.19.0.0-alpha.1/windows_x64.zip
- Startup flags: --testnet --data-dir .bitmonero --log-file bitmonero.log --no-zmq --out-peers 32 --in-peers 32 --log-level 2 --rpc-max-connections-per-private-ip 100 --rpc-max-connections 100 --disable-dns-checkpoints --check-updates disabled --rpc-restricted-bind-ip=0.0.0.0 --rpc-restricted-bind-port=28089 --max-log-file-size=0 --no-igd --public-node --confirm-external-bind --max-connections-per-ip 10

-Issue: I've tried to sync the testnet blockchain twice, both times it wont sync past block height 802203:

Logging output images:
<img width="1165" height="536" alt="Image" src="https://github.com/user-attachments/assets/9739bdd9-e9a6-4852-8c26-72f17cb38b87" />
<img width="1602" height="654" alt="Image" src="https://github.com/user-attachments/assets/43bbc8a8-caa9-480d-9c59-48441597781a" />

Logging output level 2:

```2025-09-29 18:59:14.566 D Trying to connect to 88.198.199.23:28080, bind_ip = 0.0.0.0
2025-09-29 18:59:14.727 I [88.198.199.23:28080 504579b6-79b7-41ef-9d93-856bfea5dc9e OUT] NEW CONNECTION
2025-09-29 18:59:14.727 D  connection type 2 192.168.1.229:40775 <--> 88.198.199.23:28080 (via 88.198.199.23:28080)
2025-09-29 18:59:14.727 I [88.198.199.23:28080 OUT] 274 bytes sent for category command-1001 initiated by us
2025-09-29 18:59:14.728 D [88.198.199.23:28080 OUT] LEVIN_PACKET_SENT. [len=274, flags1, r?=?, cmd = 1001, ver=1
2025-09-29 18:59:14.728 D [88.198.199.23:28080 OUT] anvoke_handler, timeout: 5000
2025-09-29 18:59:15.036 D [88.198.199.23:28080 OUT] LEVIN_PACKET partial msg received. len=7300, current total 7267/13630 (53.3162%)
2025-09-29 18:59:15.037 D [88.198.199.23:28080 OUT] LEVIN_PACKET_RECEIVED. [len=13630, flags2, r?=?, cmd = 1001, v=1
2025-09-29 18:59:15.038 I [88.198.199.23:28080 OUT] 13630 bytes received for category command-1001 initiated by us
2025-09-29 18:59:15.039 D [88.198.199.23:28080 OUT] REMOTE PEERLIST: remote peerlist size=250
2025-09-29 18:59:15.039 I [88.198.199.23:28080 OUT] Sync data returned a new top block candidate: 802203 -> 2844478 [Your node is 2042275 blocks (7.8 years) behind]
2025-09-29 18:59:15.039 I SYNCHRONIZATION started
2025-09-29 18:59:15.039 I switching safe mode off
2025-09-29 18:59:15.040 I [88.198.199.23:28080 OUT] Remote blockchain height: 2844478, id: <a46416acdba312349e4e4ba8dcf704a26834fa3c4861601bbf270d7d826d1d12>
2025-09-29 18:59:15.040 D [88.198.199.23:28080 OUT] requesting callback
2025-09-29 18:59:15.040 I [88.198.199.23:28080 OUT] [0] state: requesting callback in state synchronizing
2025-09-29 18:59:15.040 I [88.198.199.23:28080 OUT] New connection handshaked, pruning seed 0
2025-09-29 18:59:15.040 D [88.198.199.23:28080 OUT]  COMMAND_HANDSHAKE INVOKED OK
2025-09-29 18:59:15.041 D [88.198.199.23:28080 OUT] CONNECTION HANDSHAKED OK.
2025-09-29 18:59:15.041 D [88.198.199.23:28080 OUT] callback fired
2025-09-29 18:59:15.041 D Making expected connection, type 1, 1/32 connections
2025-09-29 18:59:15.041 I [88.198.199.23:28080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=30
2025-09-29 18:59:15.041 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (1/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers 115?
2025-09-29 18:59:15.041 D [88.198.199.23:28080 OUT] post N10cryptonote20NOTIFY_REQUEST_CHAINE -->
2025-09-29 18:59:15.042 D Skipping 1 possible peers as they share a class B with existing peers
2025-09-29 18:59:15.042 I [88.198.199.23:28080 OUT] 983 bytes sent for category command-2006 initiated by us
2025-09-29 18:59:15.042 D Skipping 1 possible peers as they share a class B with existing peers
2025-09-29 18:59:15.042 D [88.198.199.23:28080 OUT] LEVIN_PACKET_SENT. [len=983, flags1, r?=?, cmd = 2006, ver=1
2025-09-29 18:59:15.043 I No available peer in white list filtered by 4
2025-09-29 18:59:15.043 I [88.198.199.23:28080 OUT] [0] state: requesting chain in state synchronizing
2025-09-29 18:59:15.043 D Making expected connection, type 2, 1/32 connections
2025-09-29 18:59:15.043 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (1/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers 115?
2025-09-29 18:59:15.045 D Considering connecting (out) to gray list peer: ad586b583df17779 38.6.155.106:18094, pruning seed 0 (stripe 4 needed)
2025-09-29 18:59:15.045 D Selected peer: ad586b583df17779 38.6.155.106:18094, pruning seed 0 [peer_list=2] last_seen: never
2025-09-29 18:59:15.045 D Connecting to 38.6.155.106:18094(peer_type=2, last_seen: never)...
2025-09-29 18:59:15.045 D Spawned connection #108 to 0.0.0.0 currently we have sockets count:3
2025-09-29 18:59:15.045 D connections_ size now 1
2025-09-29 18:59:15.045 D Trying to connect to 38.6.155.106:18094, bind_ip = 0.0.0.0
2025-09-29 18:59:15.895 D [88.198.199.23:28080 OUT] LEVIN_PACKET_RECEIVED. [len=400336, flags1, r?=?, cmd = 2007, v=1
2025-09-29 18:59:15.896 I [88.198.199.23:28080 OUT] 400336 bytes received for category command-2007 initiated by peer
2025-09-29 18:59:15.896 I [88.198.199.23:28080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=802202, m_total_height=2844478
2025-09-29 18:59:15.896 I [88.198.199.23:28080 OUT] [0] state: received chain in state synchronizing
2025-09-29 18:59:15.897 D [88.198.199.23:28080 OUT] first block hash <65377e0c43df2a38f99dc56751c673217d0a905ab892e7f5e6368ed92ecd9e89>, last <e16b88c7932df9b873563f9789223b2ff4674a98387184d42813aca44d652904>
2025-09-29 18:59:15.897 D block <65377e0c43df2a38f99dc56751c673217d0a905ab892e7f5e6368ed92ecd9e89> found in main chain
2025-09-29 18:59:15.897 D block <cf16e6f5c5b3d5a12f43b9e31ee03bb25e8847ddab6090006a4398cf5118aad1> found in m_invalid_blocks
2025-09-29 18:59:15.897 E [88.198.199.23:28080 OUT] Block is invalid or known without known type, dropping connection
2025-09-29 18:59:15.897 D [88.198.199.23:28080 OUT] dropping connection id 504579b6-79b7-41ef-9d93-856bfea5dc9e (pruning seed 0), score 1, flush_all_spans 0
2025-09-29 18:59:15.897 D Host 88.198.199.23 fail score=10
2025-09-29 18:59:15.898 I Target height decreasing from 2844478 to 0
2025-09-29 18:59:15.898 W monerod is now disconnected from the network
2025-09-29 18:59:15.898 I [88.198.199.23:28080 OUT] [0] state: closed in state synchronizing
2025-09-29 18:59:15.898 I [88.198.199.23:28080 504579b6-79b7-41ef-9d93-856bfea5dc9e OUT] CLOSE CONNECTION
2025-09-29 18:59:15.899 D Destructing connection #107 to 0.0.0.0
2025-09-29 18:59:17.728 D Destructing connection #108 to 0.0.0.0
2025-09-29 18:59:17.729 I 0Connect failed to 38.6.155.106:18094
2025-09-29 18:59:17.729 D Handshake failed
2025-09-29 18:59:17.729 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (0/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers
2025-09-29 18:59:17.731 D Considering connecting (out) to gray list peer: 518ba9af84c9abeb 154.199.217.173:18094, pruning seed 0 (stripe 4 needed)
2025-09-29 18:59:17.731 D Selected peer: 518ba9af84c9abeb 154.199.217.173:18094, pruning seed 0 [peer_list=2] last_seen: never
2025-09-29 18:59:17.731 D Connecting to 154.199.217.173:18094(peer_type=2, last_seen: never)...
2025-09-29 18:59:17.731 D Spawned connection #109 to 0.0.0.0 currently we have sockets count:2
2025-09-29 18:59:17.732 D connections_ size now 1
2025-09-29 18:59:17.732 D Trying to connect to 154.199.217.173:18094, bind_ip = 0.0.0.0
2025-09-29 18:59:20.184 D Destructing connection #109 to 0.0.0.0
2025-09-29 18:59:20.185 I 0Connect failed to 154.199.217.173:18094
2025-09-29 18:59:20.185 D Handshake failed
2025-09-29 18:59:20.185 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (0/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers
2025-09-29 18:59:20.187 D Considering connecting (out) to gray list peer: 65b93a754f445d1f 154.199.217.233:18082, pruning seed 0 (stripe 4 needed)
2025-09-29 18:59:20.187 D Selected peer: 65b93a754f445d1f 154.199.217.233:18082, pruning seed 0 [peer_list=2] last_seen: never
2025-09-29 18:59:20.187 D Connecting to 154.199.217.233:18082(peer_type=2, last_seen: never)...
2025-09-29 18:59:20.187 D Spawned connection #110 to 0.0.0.0 currently we have sockets count:2
2025-09-29 18:59:20.188 D connections_ size now 1
2025-09-29 18:59:20.188 D Trying to connect to 154.199.217.233:18082, bind_ip = 0.0.0.0
2025-09-29 18:59:22.959 D Destructing connection #110 to 0.0.0.0
2025-09-29 18:59:22.959 I 0Connect failed to 154.199.217.233:18082
2025-09-29 18:59:22.960 D Handshake failed
2025-09-29 18:59:23.961 I Failed to connect to any, trying seeds
2025-09-29 18:59:23.961 D Connecting to 208.123.187.228:28080(peer_type=1, last_seen: never)...
2025-09-29 18:59:23.962 D Spawned connection #111 to 0.0.0.0 currently we have sockets count:2
2025-09-29 18:59:23.962 D connections_ size now 1
2025-09-29 18:59:23.962 D Trying to connect to 208.123.187.228:28080, bind_ip = 0.0.0.0
2025-09-29 18:59:23.985 I [208.123.187.228:28080 32558444-1989-462e-81ee-790c8fabd146 OUT] NEW CONNECTION
2025-09-29 18:59:23.985 D  connection type 2 192.168.1.229:40788 <--> 208.123.187.228:28080 (via 208.123.187.228:28080)
2025-09-29 18:59:23.986 I [208.123.187.228:28080 OUT] 274 bytes sent for category command-1001 initiated by us
2025-09-29 18:59:23.986 D [208.123.187.228:28080 OUT] LEVIN_PACKET_SENT. [len=274, flags1, r?=?, cmd = 1001, ver=1
2025-09-29 18:59:23.986 D [208.123.187.228:28080 OUT] anvoke_handler, timeout: 5000
2025-09-29 18:59:24.017 D [208.123.187.228:28080 OUT] LEVIN_PACKET_RECEIVED. [len=2879, flags2, r?=?, cmd = 1001, v=1
2025-09-29 18:59:24.017 I [208.123.187.228:28080 OUT] 2879 bytes received for category command-1001 initiated by us
2025-09-29 18:59:24.017 D [208.123.187.228:28080 OUT] REMOTE PEERLIST: remote peerlist size=44
2025-09-29 18:59:24.017 D [208.123.187.228:28080 OUT]  COMMAND_HANDSHAKE(AND CLOSE) INVOKED OK
2025-09-29 18:59:24.018 D [208.123.187.228:28080 OUT] CONNECTION HANDSHAKED OK AND CLOSED.
2025-09-29 18:59:24.018 I [208.123.187.228:28080 OUT] [0] state: closed in state before_handshake
2025-09-29 18:59:24.018 I [208.123.187.228:28080 32558444-1989-462e-81ee-790c8fabd146 OUT] CLOSE CONNECTION
2025-09-29 18:59:24.018 D Destructing connection #111 to 0.0.0.0
2025-09-29 18:59:25.031 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (0/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers
2025-09-29 18:59:25.031 D Making expected connection, type 0, 0/2 connections
2025-09-29 18:59:25.032 D Making expected connection, type 1, 0/32 connections
2025-09-29 18:59:25.032 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (0/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers
2025-09-29 18:59:25.032 D Considering connecting (out) to white list peer: 25cbdfac6267dcf1 88.198.199.23:28080, pruning seed 0 (stripe 4 needed)
2025-09-29 18:59:25.032 D Selected peer: 25cbdfac6267dcf1 88.198.199.23:28080, pruning seed 0 [peer_list=1] last_seen: d0.h0.m0.s10
2025-09-29 18:59:25.032 D Connecting to 88.198.199.23:28080(peer_type=1, last_seen: d0.h0.m0.s10)...
2025-09-29 18:59:25.033 D Spawned connection #112 to 0.0.0.0 currently we have sockets count:2
2025-09-29 18:59:25.033 D connections_ size now 1
2025-09-29 18:59:25.033 D Trying to connect to 88.198.199.23:28080, bind_ip = 0.0.0.0
2025-09-29 18:59:25.193 I [88.198.199.23:28080 8a48ef3d-3ce4-4b4c-98d1-8035dd7f6027 OUT] NEW CONNECTION
2025-09-29 18:59:25.193 D  connection type 2 192.168.1.229:40790 <--> 88.198.199.23:28080 (via 88.198.199.23:28080)
2025-09-29 18:59:25.193 I [88.198.199.23:28080 OUT] 274 bytes sent for category command-1001 initiated by us
2025-09-29 18:59:25.194 D [88.198.199.23:28080 OUT] LEVIN_PACKET_SENT. [len=274, flags1, r?=?, cmd = 1001, ver=1
2025-09-29 18:59:25.194 D [88.198.199.23:28080 OUT] anvoke_handler, timeout: 5000
2025-09-29 18:59:25.356 D [88.198.199.23:28080 OUT] LEVIN_PACKET partial msg received. len=2920, current total 2887/13630 (21.1812%)
2025-09-29 18:59:25.357 D [88.198.199.23:28080 OUT] LEVIN_PACKET partial msg received. len=5840, current total 8727/13630 (64.0279%)
2025-09-29 18:59:25.357 D [88.198.199.23:28080 OUT] LEVIN_PACKET_RECEIVED. [len=13630, flags2, r?=?, cmd = 1001, v=1
2025-09-29 18:59:25.358 I [88.198.199.23:28080 OUT] 13630 bytes received for category command-1001 initiated by us
2025-09-29 18:59:25.359 D [88.198.199.23:28080 OUT] REMOTE PEERLIST: remote peerlist size=250
2025-09-29 18:59:25.359 I [88.198.199.23:28080 OUT] Sync data returned a new top block candidate: 802203 -> 2844478 [Your node is 2042275 blocks (7.8 years) behind]
2025-09-29 18:59:25.359 I SYNCHRONIZATION started
2025-09-29 18:59:25.360 I switching safe mode off
2025-09-29 18:59:25.360 I [88.198.199.23:28080 OUT] Remote blockchain height: 2844478, id: <a46416acdba312349e4e4ba8dcf704a26834fa3c4861601bbf270d7d826d1d12>
2025-09-29 18:59:25.360 D [88.198.199.23:28080 OUT] requesting callback
2025-09-29 18:59:25.360 I [88.198.199.23:28080 OUT] [0] state: requesting callback in state synchronizing
2025-09-29 18:59:25.360 I [88.198.199.23:28080 OUT] New connection handshaked, pruning seed 0
2025-09-29 18:59:25.360 D [88.198.199.23:28080 OUT]  COMMAND_HANDSHAKE INVOKED OK
2025-09-29 18:59:25.360 D [88.198.199.23:28080 OUT] CONNECTION HANDSHAKED OK.
2025-09-29 18:59:25.361 D [88.198.199.23:28080 OUT] callback fired
2025-09-29 18:59:25.361 D Making expected connection, type 1, 1/32 connections
2025-09-29 18:59:25.361 I [88.198.199.23:28080 OUT] -->>NOTIFY_REQUEST_CHAIN: m_block_ids.size()=30
2025-09-29 18:59:25.361 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (1/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers 115?
2025-09-29 18:59:25.361 D [88.198.199.23:28080 OUT] post N10cryptonote20NOTIFY_REQUEST_CHAINE -->
2025-09-29 18:59:25.361 D Skipping 1 possible peers as they share a class B with existing peers
2025-09-29 18:59:25.362 I [88.198.199.23:28080 OUT] 983 bytes sent for category command-2006 initiated by us
2025-09-29 18:59:25.362 D Skipping 1 possible peers as they share a class B with existing peers
2025-09-29 18:59:25.362 D [88.198.199.23:28080 OUT] LEVIN_PACKET_SENT. [len=983, flags1, r?=?, cmd = 2006, ver=1
2025-09-29 18:59:25.362 I No available peer in white list filtered by 4
2025-09-29 18:59:25.362 I [88.198.199.23:28080 OUT] [0] state: requesting chain in state synchronizing
2025-09-29 18:59:25.362 D Making expected connection, type 2, 1/32 connections
2025-09-29 18:59:25.363 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (1/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers 115?
2025-09-29 18:59:25.364 D Considering connecting (out) to gray list peer: c80253a65653ea0c 154.199.217.39:18082, pruning seed 0 (stripe 4 needed)
2025-09-29 18:59:25.364 D Selected peer: c80253a65653ea0c 154.199.217.39:18082, pruning seed 0 [peer_list=2] last_seen: never
2025-09-29 18:59:25.364 D Connecting to 154.199.217.39:18082(peer_type=2, last_seen: never)...
2025-09-29 18:59:25.365 D Spawned connection #113 to 0.0.0.0 currently we have sockets count:3
2025-09-29 18:59:25.365 D connections_ size now 1
2025-09-29 18:59:25.365 D Trying to connect to 154.199.217.39:18082, bind_ip = 0.0.0.0
2025-09-29 18:59:26.012 D [88.198.199.23:28080 OUT] LEVIN_PACKET_RECEIVED. [len=400336, flags1, r?=?, cmd = 2007, v=1
2025-09-29 18:59:26.013 I [88.198.199.23:28080 OUT] 400336 bytes received for category command-2007 initiated by peer
2025-09-29 18:59:26.013 I [88.198.199.23:28080 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10000, m_start_height=802202, m_total_height=2844478
2025-09-29 18:59:26.014 I [88.198.199.23:28080 OUT] [0] state: received chain in state synchronizing
2025-09-29 18:59:26.014 D [88.198.199.23:28080 OUT] first block hash <65377e0c43df2a38f99dc56751c673217d0a905ab892e7f5e6368ed92ecd9e89>, last <e16b88c7932df9b873563f9789223b2ff4674a98387184d42813aca44d652904>
2025-09-29 18:59:26.014 D block <65377e0c43df2a38f99dc56751c673217d0a905ab892e7f5e6368ed92ecd9e89> found in main chain
2025-09-29 18:59:26.014 D block <cf16e6f5c5b3d5a12f43b9e31ee03bb25e8847ddab6090006a4398cf5118aad1> found in m_invalid_blocks
2025-09-29 18:59:26.015 E [88.198.199.23:28080 OUT] Block is invalid or known without known type, dropping connection
2025-09-29 18:59:26.015 D [88.198.199.23:28080 OUT] dropping connection id 8a48ef3d-3ce4-4b4c-98d1-8035dd7f6027 (pruning seed 0), score 1, flush_all_spans 0
2025-09-29 18:59:26.015 D Host 88.198.199.23 fail score=11
2025-09-29 18:59:26.015 I Host 88.198.199.23 blocked.
2025-09-29 18:59:26.016 I Target height decreasing from 2844478 to 0
2025-09-29 18:59:26.016 W monerod is now disconnected from the network
2025-09-29 18:59:26.016 I [88.198.199.23:28080 OUT] [0] state: closed in state synchronizing
2025-09-29 18:59:26.016 I [88.198.199.23:28080 8a48ef3d-3ce4-4b4c-98d1-8035dd7f6027 OUT] CLOSE CONNECTION
2025-09-29 18:59:26.016 D Destructing connection #112 to 0.0.0.0
2025-09-29 18:59:27.680 D Destructing connection #113 to 0.0.0.0
2025-09-29 18:59:27.681 I 0Connect failed to 154.199.217.39:18082
2025-09-29 18:59:27.681 D Handshake failed
2025-09-29 18:59:27.681 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (0/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers
2025-09-29 18:59:27.683 D Considering connecting (out) to gray list peer: c606abbff52f6646 38.6.155.219:18082, pruning seed 0 (stripe 4 needed)
2025-09-29 18:59:27.683 D Selected peer: c606abbff52f6646 38.6.155.219:18082, pruning seed 0 [peer_list=2] last_seen: never
2025-09-29 18:59:27.683 D Connecting to 38.6.155.219:18082(peer_type=2, last_seen: never)...
2025-09-29 18:59:27.684 D Spawned connection #114 to 0.0.0.0 currently we have sockets count:2
2025-09-29 18:59:27.684 D connections_ size now 1
2025-09-29 18:59:27.684 D Trying to connect to 38.6.155.219:18082, bind_ip = 0.0.0.0
2025-09-29 18:59:29.952 D Destructing connection #114 to 0.0.0.0
2025-09-29 18:59:29.952 I 0Connect failed to 38.6.155.219:18082
2025-09-29 18:59:29.952 D Handshake failed
2025-09-29 18:59:29.953 D get_next_needed_pruning_stripe: want height 802203 (802203 from blockchain, 802203 from block queue), stripe 4 (0/32 on it and 0 on 5, 0 others) -> 4 (+0), current peers
2025-09-29 18:59:29.954 D Considering connecting (out) to gray list peer: 13f36b65afcf88f8 38.6.156.48:18094, pruning seed 0 (stripe 4 needed)
2025-09-29 18:59:29.955 D Selected peer: 13f36b65afcf88f8 38.6.156.48:18094, pruning seed 0 [peer_list=2] last_seen: never
2025-09-29 18:59:29.955 D Connecting to 38.6.156.48:18094(peer_type=2, last_seen: never)...
2025-09-29 18:59:29.955 D Spawned connection #115 to 0.0.0.0 currently we have sockets count:2
2025-09-29 18:59:29.955 D connections_ size now 1
2025-09-29 18:59:29.955 D Trying to connect to 38.6.156.48:18094, bind_ip = 0.0.0.0
2025-09-29 18:59:34.971 D Destructing connection #115 to 0.0.0.0
2025-09-29 18:59:34.971 I 0Connect failed to 38.6.156.48:18094
2025-09-29 18:59:34.971 D Handshake failed
2025-09-29 18:59:35.979 I Failed to connect to any, trying seeds
2025-09-29 18:59:35.979 D Connecting to 185.141.216.147:28080(peer_type=1, last_seen: never)...
2025-09-29 18:59:35.980 D Spawned connection #116 to 0.0.0.0 currently we have sockets count:2
2025-09-29 18:59:35.980 D connections_ size now 1
2025-09-29 18:59:35.980 D Trying to connect to 185.141.216.147:28080, bind_ip = 0.0.0.0
2025-09-29 18:59:36.064 I [185.141.216.147:28080 200c445f-862d-4ccd-beb5-34ad5155f05e OUT] NEW CONNECTION
2025-09-29 18:59:36.065 D  connection type 2 192.168.1.229:40809 <--> 185.141.216.147:28080 (via 185.141.216.147:28080)
2025-09-29 18:59:36.065 I [185.141.216.147:28080 OUT] 274 bytes sent for category command-1001 initiated by us
2025-09-29 18:59:36.065 D [185.141.216.147:28080 OUT] LEVIN_PACKET_SENT. [len=274, flags1, r?=?, cmd = 1001, ver=1
2025-09-29 18:59:36.065 D [185.141.216.147:28080 OUT] anvoke_handler, timeout: 5000
2025-09-29 18:59:36.156 D [185.141.216.147:28080 OUT] LEVIN_PACKET_RECEIVED. [len=3050, flags2, r?=?, cmd = 1001, v=1
2025-09-29 18:59:36.156 I [185.141.216.147:28080 OUT] 3050 bytes received for category command-1001 initiated by us
2025-09-29 18:59:36.156 D [185.141.216.147:28080 OUT] REMOTE PEERLIST: remote peerlist size=47
2025-09-29 18:59:36.157 D [185.141.216.147:28080 OUT]  COMMAND_HANDSHAKE(AND CLOSE) INVOKED OK
2025-09-29 18:59:36.157 I [185.141.216.147:28080 OUT] [0] state: closed in state before_handshake
2025-09-29 18:59:36.157 I [185.141.216.147:28080 200c445f-862d-4ccd-beb5-34ad5155f05e OUT] CLOSE CONNECTION
2025-09-29 18:59:36.157 D Destructing connection #116 to 0.0.0.0
2025-09-29 18:59:36.157 D [185.141.216.147:28080 OUT] CONNECTION HANDSHAKED OK AND CLOSED.
2025-09-29 18:59:37.173 D STARTED PEERLIST IDLE HANDSHAKE
2025-09-29 18:59:37.173 D FINISHED PEERLIST IDLE HANDSHAKE
2025-09-29 18:59:37.173 D Connecting to 208.123.187.228:28080(peer_type=1, last_seen: never)...```

# Discussion History
## nahuhh | 2025-09-29T19:37:00+00:00
What is the output of `sync_info`

the 88.198 node looks like its sending bad blocks

```
2025-09-29 18:59:15.897 D block <65377e0c43df2a38f99dc56751c673217d0a905ab892e7f5e6368ed92ecd9e89> found in main chain
2025-09-29 18:59:15.897 D block <cf16e6f5c5b3d5a12f43b9e31ee03bb25e8847ddab6090006a4398cf5118aad1> found in m_invalid_blocks 
```

## bobXMR | 2025-09-30T03:56:01+00:00
j-berman has identified and fixed the issue. Issue was caused by an issue with zeroCommitVartime.

## j-berman | 2025-09-30T14:41:38+00:00
We can keep this issue open until the fix is deployed, in case others run into the same problem

## j-berman | 2025-10-03T16:20:37+00:00
Fix deployed in the [latest release](https://github.com/seraphis-migration/monero/releases) (alpha stressnet v1.1 at time of writing)

# Action History
- Created by: bobXMR | 2025-09-29T19:05:39+00:00
- Closed at: 2025-10-03T16:20:37+00:00
