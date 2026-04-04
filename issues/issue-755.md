---
title: Mac binary v0-9-3-0 fails
source_url: https://github.com/monero-project/monero/issues/755
author: songproducer
assignees: []
labels: []
created_at: '2016-03-24T07:24:45+00:00'
updated_at: '2016-03-24T07:25:43+00:00'
type: issue
status: closed
closed_at: '2016-03-24T07:25:43+00:00'
---

# Original Description
Creating the logger system
2016-Mar-24 15:22:44.141786 Initializing cryptonote protocol...
2016-Mar-24 15:22:44.141850 Cryptonote protocol initialized OK
2016-Mar-24 15:22:44.142064 Initializing p2p server...
2016-Mar-24 15:22:45.112023 Set limit-up to 2048 kB/s
2016-Mar-24 15:22:45.112117 Set limit-down to 8192 kB/s
2016-Mar-24 15:22:45.112168 Set limit-up to 2048 kB/s
2016-Mar-24 15:22:45.112226 Set limit-down to 8192 kB/s
2016-Mar-24 15:22:45.126731 Binding on 0.0.0.0:18080
2016-Mar-24 15:22:45.126867 ERROR /DISTRIBUTION-BUILD/contrib/epee/include/net/abstract_tcp_server2.inl:728 Exception at [boosted_tcp_server<t_protocol_handler>::init_server], what=bind: Address already in use
2016-Mar-24 15:22:45.126923 ERROR /DISTRIBUTION-BUILD/src/p2p/net_node.inl:506 Failed to bind server
2016-Mar-24 15:22:45.127665 Deinitializing core...
2016-Mar-24 15:22:45.127705 Closing IO Service.
2016-Mar-24 15:22:45.127757 Failed to deinitialize core...
2016-Mar-24 15:22:45.127804 Deinitializing cryptonote_protocol...
2016-Mar-24 15:22:45.127893 ERROR /DISTRIBUTION-BUILD/src/daemon/main.cpp:269 Exception in main! Failed to initialize p2p server.


# Discussion History
## songproducer | 2016-03-24T07:25:43+00:00
Just realised I had the previous version running at the same time!


# Action History
- Created by: songproducer | 2016-03-24T07:24:45+00:00
- Closed at: 2016-03-24T07:25:43+00:00
