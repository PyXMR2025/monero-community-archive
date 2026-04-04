---
title: txpool Error & Unable to send transaction(s) to tor Warning
source_url: https://github.com/monero-project/monero/issues/7981
author: d3vm4rc-d07-d3
assignees: []
labels: []
created_at: '2021-09-29T13:24:20+00:00'
updated_at: '2021-09-29T13:44:01+00:00'
type: issue
status: closed
closed_at: '2021-09-29T13:43:22+00:00'
---

# Original Description
> 2021-09-29 09:53:56.670 [P2P1]  ERROR   txpool  src/cryptonote_core/tx_pool.cpp:1427      failed to find tx meta: <d8f6bdd86f8cd963151debc6f7ed7767c5313a85957d7b2660ace1d3277d0a3f> (will only print once)

> 
> 2021-09-29 09:58:21.870 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459909
> 2021-09-29 10:25:25.573 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459919
> 2021-09-29 10:33:50.536 [P2P5]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459925
> 2021-09-29 10:40:45.523 [P2P7]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459931
> 2021-09-29 10:59:22.685 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459942
> 2021-09-29 11:06:15.193 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459948
> 2021-09-29 11:34:54.969 [P2P4]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459966
> 2021-09-29 11:55:07.700 [P2P1]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459979
> 2021-09-29 12:08:48.813 [P2P2]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459982
> 2021-09-29 12:20:36.490 [P2P6]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2459991
> 2021-09-29 12:46:04.519 [P2P0]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2460010
> 2021-09-29 13:16:23.118 [P2P8]  WARNING net.p2p.tx      src/cryptonote_protocol/levin_notify.cpp:681    Unable to send transaction(s) to tor - no suitable outbound connections at height 2460023

I get lots of warnings even though the Node is fully synced and reachable via Tor as well.


# Discussion History
## hyc | 2021-09-29T13:43:22+00:00
It's just a warning, safe to ignore.

Notice the difference in block heights at each occurrence of the message. This shows that at several minute intervals you've lost all outbound Tor connections. The fact that the heights are not continuous means that connectivity was re-established in those intervals. 

# Action History
- Created by: d3vm4rc-d07-d3 | 2021-09-29T13:24:20+00:00
- Closed at: 2021-09-29T13:43:22+00:00
