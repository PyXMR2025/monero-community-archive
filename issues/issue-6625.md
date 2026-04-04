---
title: 'Error:  Setting timer on a shut down object'
source_url: https://github.com/monero-project/monero/issues/6625
author: ronohara
assignees: []
labels: []
created_at: '2020-06-03T11:08:37+00:00'
updated_at: '2020-06-03T13:16:32+00:00'
type: issue
status: closed
closed_at: '2020-06-03T13:16:32+00:00'
---

# Original Description
2020-06-03 10:57:48.959	I Monero 'Nitrogen Nebula' (v0.16.0.0-release)
2020-06-03 10:35:10.353 [P2P2]  ERROR   net     contrib/epee/include/net/abstrac
t_tcp_server2.inl:766   Setting timer on a shut down object
2020-06-03 10:35:10.353 [P2P2]  INFO    net.cn  src/cryptonote_protocol/cryptono
te_protocol_handler.inl:2666    [167.99.114.88:18080 OUT] [0] state: closed in s
tate before_handshake

Very rare but recurring error - is this something to worry about ... if not perhaps this should be a warning.

# Discussion History
## moneromooo-monero | 2020-06-03T11:43:27+00:00
It's something that should not happen but is handled properly, unless you find evidence to the contrary.

## ronohara | 2020-06-03T13:16:28+00:00
It seems to be handled properly. It jumped out at me because it was highlighted in red... so I became mildly concerned.  

# Action History
- Created by: ronohara | 2020-06-03T11:08:37+00:00
- Closed at: 2020-06-03T13:16:32+00:00
