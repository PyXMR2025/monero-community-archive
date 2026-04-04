---
title: synchronisation monerod
source_url: https://github.com/monero-project/monero/issues/2049
author: masonsam
assignees: []
labels:
- invalid
created_at: '2017-05-25T23:54:54+00:00'
updated_at: '2017-10-12T18:06:09+00:00'
type: issue
status: closed
closed_at: '2017-09-21T09:30:26+00:00'
---

# Original Description
I had a problem whit the synchronisation of monerod because when start give me this error:
--log-level 2
`2017-05-26 01:45:42.857	    7f49065b6740	INFO 	net.p2p	src/p2p/net_node.inl:545	Binding on 0.0.0.0:18080
2017-05-26 01:45:42.859	    7f49065b6740	ERROR	net	contrib/epee/include/net/abstract_tcp_server2.inl:740	Exception at [boosted_tcp_server<t_protocol_handler>::init_server], what=bind: Address already in use
2017-05-26 01:45:42.859	    7f49065b6740	ERROR	net.p2p	src/p2p/net_node.inl:547	Failed to bind server
2017-05-26 01:45:42.860	    7f49065b6740	INFO 	global	src/daemon/core.h:89	Deinitializing core...
2017-05-26 01:45:42.860	    7f49065b6740	DEBUG	miner	src/cryptonote_basic/miner.cpp:325	Not mining - nothing to stop
2017-05-26 01:45:42.861	    7f49065b6740	INFO 	txpool	src/cryptonote_core/tx_pool.cpp:763	Received signal to deactivate memory pool store
2017-05-26 01:45:42.861	    7f49065b6740	INFO 	txpool	src/cryptonote_core/tx_pool.cpp:767	Memory pool store already empty
2017-05-26 01:45:42.862	    7f49065b6740	ERROR	daemon	src/daemon/core.h:94	Failed to deinitialize core...
2017-05-26 01:45:42.862	    7f49065b6740	DEBUG	miner	src/cryptonote_basic/miner.cpp:325	Not mining - nothing to stop
2017-05-26 01:45:42.862	    7f49065b6740	INFO 	global	src/daemon/protocol.h:77	Stopping cryptonote protocol...
2017-05-26 01:45:42.862	    7f49065b6740	INFO 	global	src/daemon/protocol.h:81	Cryptonote protocol stopped successfully
2017-05-26 01:45:42.862	    7f49065b6740	INFO 	msgwriter	src/common/scoped_message_writer.h:94	Daemon stopped successfully
Daemon stopped successfully
2017-05-26 01:45:42.862	    7f49065b6740	ERROR	daemon	src/daemon/main.cpp:288	Exception in main! Failed to initialize p2p server.

`
Thank you

# Discussion History
## moneroexamples | 2017-05-26T01:44:37+00:00
Maybe this is the problem:

```
Address already in use [...] Failed to bind server
```
Check if you dont have any other monero deamon running, or one in a zombie state keeping the ports blocked.


## masonsam | 2017-05-26T02:17:17+00:00
And how can i check this?

## moneroexamples | 2017-05-26T02:40:48+00:00
In linux you can just run `netstat -lntu | grep 1808` and check if monero port 1808x are in use. Or just restart you computer, to kill all zompie monero process than can be bind to these ports.

## masonsam | 2017-05-26T10:46:12+00:00
Perfect i kill monero process now there is this:

`2017-05-26 12:43:31.697	    7fcda043b740	WARN 	checkpoints	src/cryptonote_basic/checkpoints.cpp:85	CHECKPOINT FAILED FOR HEIGHT 1288616. EXPECTED HASH: <87ac1bc7aa6c5eedc510abb9c694034f9e7f9dce4c60698af37009b6365>, FETCHED HASH: <1e6b1019968d4a3b281ab70d83947bc051ac952f26d2693c427b04d82151f>

2017-05-26 12:43:31.697	    7fcda043b740	ERROR	blockchain	src/cryptonote_core/blockchain.cpp:3469	WARNING: local blockchain failed to pass a MoneroPulse checkpoint, and you could be on a fork. You should either sync up from scratch, OR download a fresh blockchain bootstrap, OR enable checkpoint enforcing with the --enforce-dns-checkpointing command-line option
`

## masonsam | 2017-05-26T12:10:55+00:00
Does not sync, it continue to give me this error:
`2017-05-26 14:03:35.038	[P2P7]	ERROR	net.p2p	src/p2p/net_node.inl:798	[91.152.122.132:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-05-26 14:03:35.038	[P2P7]	ERROR	net.p2p	src/p2p/net_node.inl:798	[91.152.122.132:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2017-05-26 14:03:35.039	[P2P7]	ERROR	net.p2p	src/p2p/net_node.inl:798	[92.255.232.119:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
2017-05-26 14:04:36.049	[P2P0]	ERROR	net.p2p	src/p2p/net_node.inl:798	[92.255.232.119:18080 OUT] COMMAND_TIMED_SYNC invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
`


## moneromooo-monero | 2017-07-03T17:41:49+00:00
Have you tried the --enforce-dns-checkpointing the message was telling you to ? If so, did it work ? If not, what errors ?

## moneromooo-monero | 2017-09-21T09:25:22+00:00
The first error was another process already running, the second one should be handled by --enforce-dns-checkpointing but we can't be sure as there's no further messages.

+invalid

# Action History
- Created by: masonsam | 2017-05-25T23:54:54+00:00
- Closed at: 2017-09-21T09:30:26+00:00
