---
title: monerod “exit” command raising an exception in log
source_url: https://github.com/monero-project/monero/issues/7134
author: ghost
assignees: []
labels: []
created_at: '2020-12-11T19:35:52+00:00'
updated_at: '2022-02-19T00:49:21+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:49:21+00:00'
---

# Original Description
monerod “exit” command , raising an exception in log:

```
020-12-11 19:27:29.782	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:80	p2p net loop stopped
2020-12-11 19:27:29.883	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::system_error
2020-12-11 19:27:29.883	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2020-12-11 19:27:29.885	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x111) [0x558b59422341]:__wrap___cxa_throw+0x111) [0x558b59422341]
2020-12-11 19:27:29.885	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monero/build/Linux/master/release/bin/monerod(+0x42736e) [0x558b58f5b36e] 
2020-12-11 19:27:29.885	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x90b) [0x558b59468f5b]:_ZN10cryptonote3rpc9ZmqServer5serveEv+0x90b) [0x558b59468f5b]
2020-12-11 19:27:29.885	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monero/build/Linux/master/release/bin/monerod(+0xea64f5) [0x558b599da4f5] 
2020-12-11 19:27:29.885	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x7fa3) [0x7fd2894eefa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7fd2894eefa3]
2020-12-11 19:27:29.885	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x3f) [0x7fd28941f4cf]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7fd28941f4cf]
2020-12-11 19:27:29.885	    7fb81f7fe700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2020-12-11 19:27:29.886	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:84	Stopping core RPC server...
2020-12-11 19:27:29.886	[SRV_MAIN]	INFO	global	src/daemon/daemon.cpp:227	Node stopped.
2020-12-11 19:27:29.897	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2020-12-11 19:27:29.898	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:90	Deinitializing p2p...
2020-12-11 19:27:30.097	[SRV_MAIN]	INFO	global	src/daemon/core.h:94	Deinitializing core...
2020-12-11 19:27:30.106	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2020-12-11 19:27:30.106	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
```

# Discussion History
## dungdang95 | 2020-12-25T06:18:55+00:00
Me too, my monerod was killed. I start again and it exit again. Here my log:

`2020-12-25 05:34:06.227	[P2P7]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[147.135.178.157:18080 OUT] 10 bytes received for category command-1003 initiated by peer
2020-12-25 05:34:06.227	[P2P7]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[147.135.178.157:18080 OUT] 38 bytes sent for category command-1003 initiated by peer
2020-12-25 05:34:06.229	[P2P9]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[185.220.101.130:16754 INC] 2931 bytes sent for category command-2903018099 initiated by us
2020-12-25 05:34:06.255	[P2P0]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[209.250.243.248:34694 INC] 1478 bytes received for category command-2002 initiated by peer
2020-12-25 05:34:06.255	[P2P0]	INFO	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:922	[209.250.243.248:34694 INC] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-12-25 05:34:06.256	[P2P0]	INFO	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:924	Including transaction <fd10a49fcb6b76e881d0a02353c4577121cf659b2d5c1d38047df54b022fb965>
2020-12-25 05:34:06.265	[P2P2]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[144.217.241.118:12371 OUT] 1478 bytes sent for category command-3238300275 initiated by us
2020-12-25 05:34:06.333	[P2P4]	INFO	net.p2p.traffic	contrib/epee/include/storages/levin_abstract_invoke2.h:44	[51.79.117.99:16789 OUT] 519 bytes received for category command-2007 initiated by peer
2020-12-25 05:34:06.333	[P2P4]	INFO	net.p2p.msg	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2411	[51.79.117.99:16789 OUT] Received NOTIFY_RESPONSE_CHAIN_ENTRY: m_block_ids.size()=10, m_start_height=2259691, m_total_height=2259701
2020-12-25 05:34:06.333	[P2P4]	INFO	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2412	[51.79.117.99:16789 OUT] [0] state: received chain in state synchronizing`



![image](https://user-images.githubusercontent.com/60590661/103124597-d79a3100-46ba-11eb-8a0b-c36bcd7a4124.png)


## selsta | 2022-02-19T00:49:21+00:00
@dungdang95 I think that was due to a network attack. It shouldn't happen anymore with modern monerod versions.

# Action History
- Created by: ghost | 2020-12-11T19:35:52+00:00
- Closed at: 2022-02-19T00:49:21+00:00
