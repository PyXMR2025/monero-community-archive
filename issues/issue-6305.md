---
title: Connection failure errors
source_url: https://github.com/monero-project/monero/issues/6305
author: charminULTRA
assignees: []
labels: []
created_at: '2020-01-25T18:34:17+00:00'
updated_at: '2020-01-27T02:38:37+00:00'
type: issue
status: closed
closed_at: '2020-01-27T02:38:37+00:00'
---

# Original Description
Hi all - I'm pretty new to Monerod, and I'm attempting to use the solo mining feature. I'm getting lots of errors in the level 1 logs and when I attempt to solo mine, it works for a few mins then crashes. Here's my level 1 log, can anyone tell me what may be wrong?

> 2020-01-25 18:32:15.372	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[51.79.58.89:53103 42f4e9e3-0b04-4cdb-bcf4-facc09d45d72 INC] NEW CONNECTION
2020-01-25 18:32:15.394	[P2P7]	INFO	net.p2p	src/p2p/net_node.inl:2469	[51.79.58.89:18080 bbfd877c-7b65-4da1-ac0c-6341e99d1485 OUT] NEW CONNECTION
2020-01-25 18:32:15.421	[P2P7]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:759	Setting timer on a shut down object
2020-01-25 18:32:15.422	[P2P9]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[51.79.58.89:18080 OUT] [0] state: closed in state before_handshake
2020-01-25 18:32:15.422	[P2P9]	INFO	net.p2p	src/p2p/net_node.inl:2485	[51.79.58.89:18080 bbfd877c-7b65-4da1-ac0c-6341e99d1485 OUT] CLOSE CONNECTION
2020-01-25 18:32:19.959	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[35.180.86.57:60120 13ee1290-6c74-4528-85f3-7d110aee2bae INC] NEW CONNECTION
2020-01-25 18:32:21.192	[P2P7]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1576	[103.94.48.176:18080 OUT] dropping synced peer, 0 syncing, 8 synced
2020-01-25 18:32:21.482	[P2P7]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[103.94.48.176:18080 OUT] [0] state: closed in state normal
2020-01-25 18:32:21.483	[P2P7]	INFO	net.p2p	src/p2p/net_node.inl:2485	[103.94.48.176:18080 4c837bfe-25e0-4d42-8df3-ec9a1eb015c4 OUT] CLOSE CONNECTION
2020-01-25 18:32:21.960	[P2P7]	WARNING	net.p2p	src/p2p/net_node.inl:2195	[<none> OUT] back ping connect failed to 35.180.86.57:18080
2020-01-25 18:32:26.951	[P2P9]	INFO	net.p2p	src/p2p/net_node.inl:1262	0Connect failed to 114.24.192.122:18080
2020-01-25 18:32:31.953	[P2P9]	INFO	net.p2p	src/p2p/net_node.inl:1262	0Connect failed to 81.159.184.94:18080
2020-01-25 18:32:32.794	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[50.231.13.42:52853 33723598-8e0a-4d71-9307-15c1485331fe INC] NEW CONNECTION
2020-01-25 18:32:32.904	[P2P7]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[50.231.13.42:52853 INC] [0] state: closed in state normal
2020-01-25 18:32:32.904	[P2P7]	INFO	net.p2p	src/p2p/net_node.inl:2485	[50.231.13.42:52853 33723598-8e0a-4d71-9307-15c1485331fe INC] CLOSE CONNECTION
2020-01-25 18:32:34.794	[P2P6]	WARNING	net.p2p	src/p2p/net_node.inl:2195	[<none> OUT] back ping connect failed to 50.231.13.42:18080
2020-01-25 18:32:36.954	[P2P9]	INFO	net.p2p	src/p2p/net_node.inl:1262	0Connect failed to 209.93.12.32:18080
2020-01-25 18:32:37.063	[P2P9]	INFO	net.p2p	src/p2p/net_node.inl:2469	[73.140.212.184:18080 8f5ee237-18e2-4ab6-9953-eae2167c00a7 OUT] NEW CONNECTION
2020-01-25 18:32:37.270	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[73.140.212.184:61867 5edf50ee-70f6-4f6b-b352-ac26bc7f4699 INC] NEW CONNECTION
2020-01-25 18:32:37.281	[P2P5]	INFO	net.p2p	src/p2p/net_node.inl:1073	[73.140.212.184:18080 OUT] New connection handshaked, pruning seed 0
2020-01-25 18:32:37.282	[P2P9]	INFO	net.p2p	src/p2p/net_node.inl:1321	Connecting to 147.228.137.167:18080(last_seen: never)...
2020-01-25 18:32:37.380	[P2P3]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[73.140.212.184:61867 INC] [0] state: closed in state before_handshake
2020-01-25 18:32:37.380	[P2P3]	INFO	net.p2p	src/p2p/net_node.inl:2485	[73.140.212.184:61867 5edf50ee-70f6-4f6b-b352-ac26bc7f4699 INC] CLOSE CONNECTION
2020-01-25 18:32:38.578	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[78.94.76.98:51366 9d3a9b77-dda7-4d7a-8a70-f9aa301674fe INC] NEW CONNECTION
2020-01-25 18:32:40.435	[P2P6]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[78.94.76.98:51366 INC] [0] state: closed in state normal
2020-01-25 18:32:40.436	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2485	[78.94.76.98:51366 9d3a9b77-dda7-4d7a-8a70-f9aa301674fe INC] CLOSE CONNECTION
2020-01-25 18:32:42.137	[P2P3]	WARNING	net.p2p	src/p2p/net_node.inl:2195	[<none> OUT] back ping connect failed to 78.94.76.98:18080
2020-01-25 18:32:42.284	[P2P9]	INFO	net.p2p	src/p2p/net_node.inl:1327	[<none> OUT] Connect failed to 147.228.137.167:18080
2020-01-25 18:32:48.757	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[95.216.173.99:54874 7f90c985-8413-45c5-a4fa-489233e6b9b5 INC] NEW CONNECTION
2020-01-25 18:32:49.042	[P2P3]	INFO	net.p2p	src/p2p/net_node.inl:2469	[95.216.173.99:18080 9fc57df0-8d00-4a3f-9719-69694cd3689a OUT] NEW CONNECTION
2020-01-25 18:32:49.201	[P2P3]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[95.216.173.99:54874 INC] [0] state: closed in state normal
2020-01-25 18:32:49.201	[P2P3]	INFO	net.p2p	src/p2p/net_node.inl:2485	[95.216.173.99:54874 7f90c985-8413-45c5-a4fa-489233e6b9b5 INC] CLOSE CONNECTION
2020-01-25 18:32:49.328	[P2P3]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:759	Setting timer on a shut down object
2020-01-25 18:32:49.328	[P2P5]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[95.216.173.99:18080 OUT] [0] state: closed in state before_handshake
2020-01-25 18:32:49.328	[P2P5]	INFO	net.p2p	src/p2p/net_node.inl:2485	[95.216.173.99:18080 9fc57df0-8d00-4a3f-9719-69694cd3689a OUT] CLOSE CONNECTION
2020-01-25 18:32:56.337	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[51.79.58.90:33393 4244e426-0ab5-4577-8864-b9db5fa2d47c INC] NEW CONNECTION
2020-01-25 18:32:56.360	[P2P3]	INFO	net.p2p	src/p2p/net_node.inl:2469	[51.79.58.90:18080 eeca3ec8-937a-4016-bd14-b9524f8c2ceb OUT] NEW CONNECTION
2020-01-25 18:32:56.388	[P2P6]	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:759	Setting timer on a shut down object
2020-01-25 18:32:56.388	[P2P3]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2471	[51.79.58.90:18080 OUT] [0] state: closed in state before_handshake
2020-01-25 18:32:56.389	[P2P3]	INFO	net.p2p	src/p2p/net_node.inl:2485	[51.79.58.90:18080 eeca3ec8-937a-4016-bd14-b9524f8c2ceb OUT] CLOSE CONNECTION
2020-01-25 18:32:56.798	[P2P6]	INFO	net.p2p	src/p2p/net_node.inl:2469	[47.74.243.212:40380 4e798654-fdd1-4a61-acb2-5bc4f736826a INC] NEW CONNECTION

> 

# Discussion History
## ndorf | 2020-01-25T19:40:07+00:00
Sorry to hear that your daemon is crashing, but none of these messages is relevant to that. These are simply connections closing and opening to other peers (the `net.p2p` log category is what tells you that). You can't do anything about a peer that chooses to disconnect unexpectedly, for instance.

Are there no other errors in your log that might be more relevant? What happens exactly when the process crashes?




## moneromooo-monero | 2020-01-25T22:29:39+00:00
Does it crash only when mining ?

## charminULTRA | 2020-01-26T18:08:14+00:00
> Sorry to hear that your daemon is crashing, but none of these messages is relevant to that. These are simply connections closing and opening to other peers (the `net.p2p` log category is what tells you that). You can't do anything about a peer that chooses to disconnect unexpectedly, for instance.
> 
> Are there no other errors in your log that might be more relevant? What happens exactly when the process crashes?

I didn't see anything that seemed relevant to me. I've attached my log (at set_log 1) below starting with when I begin mining in the monerod CLI. The monerod.exe program just disappears.

[Log.txt](https://github.com/monero-project/monero/files/4113965/Log.txt)

> Does it crash only when mining ?

Yes, mines for only about 10-15 minutes before the program just disappears.

## moneromooo-monero | 2020-01-26T19:10:55+00:00
Please post a stack trace.
Run in gdb, then after it crashes, run "bt" and paste the ouput (there will likely be several pages to go through).

## charminULTRA | 2020-01-26T20:12:38+00:00
> Please post a stack trace.
> Run in gdb, then after it crashes, run "bt" and paste the ouput (there will likely be several pages to go through).

Never used gdb before but I'll give this a shot. Will post back.

## charminULTRA | 2020-01-27T02:38:37+00:00
Figure it out, I'm running a Ryzen 1600X, that was the problem (opcache).

# Action History
- Created by: charminULTRA | 2020-01-25T18:34:17+00:00
- Closed at: 2020-01-27T02:38:37+00:00
