---
title: '"Exception: boost::thread_interrupted" on v0.13.0.2-77ef8c18 and MASTER'
source_url: https://github.com/monero-project/monero/issues/4665
author: Ulmo
assignees: []
labels:
- invalid
created_at: '2018-10-19T18:42:34+00:00'
updated_at: '2019-07-13T03:17:44+00:00'
type: issue
status: closed
closed_at: '2019-03-13T17:34:05+00:00'
---

# Original Description
I keep getting this error:

[bitmonero-crash.log](https://github.com/monero-project/monero/files/2496971/bitmonero-crash.log)

Excerpt:

2018-10-19 18:39:19.383     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::thread_interrupted
2018-10-19 18:39:19.383     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:
2018-10-19 18:39:19.385     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:172      [1] ./monerod:__cxa_throw+0x10d [0x55d4e5b6cb2d]
2018-10-19 18:39:19.385     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1:boost::this_thread::interruption_point()+0x76 [0x7f61a914fae6]
2018-10-19 18:39:19.385     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] ./monerod:cryptonote::rpc::ZmqServer::serve()+0x97d [0x55d4e5b7d83d]
2018-10-19 18:39:19.385     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:172      [4] /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.65.1+0x11bcd [0x7f61a914fbcd]
2018-10-19 18:39:19.385     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] /lib/x86_64-linux-gnu/libpthread.so.0+0x76db [0x7f61a89856db]
2018-10-19 18:39:19.385     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] /lib/x86_64-linux-gnu/libc.so.6:clone+0x3f [0x7f61a86ae88f]


# Discussion History
## moneromooo-monero | 2018-10-19T19:17:30+00:00
You can ignore that, it's fine.
Your log is named bitmonero-crash.log, do you have a crash somewhere ?

## Ulmo | 2018-10-20T05:29:13+00:00
In the log file attached to my first message, it shows what I am having trouble with:  as soon as the program starts up, it shuts down.  Here's the excerpt where it switches from starting up to shutting down.

2018-10-19 18:39:18.382 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...
2018-10-19 18:39:18.382 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:80     p2p net loop stopped
2018-10-19 18:39:19.383     7f61a1614700        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: boost::thread_interrupted

To me, it looked like a caught crash.

## moneromooo-monero | 2018-10-20T08:47:55+00:00
Ah, are you using somthing like systemd, upstart, or some other thing like this ?
If so, those things close the standard input, which looks exactly like ^D, which is the "please exit" signal.
If this is the case, you want either:
- use --non-interactive
- use --detach
- don't use systemd or upstart etc

## moneromooo-monero | 2018-10-20T09:20:39+00:00
Apply https://github.com/monero-project/monero/pull/4670 and see if you see the new log.

## moneromooo-monero | 2018-11-02T12:14:39+00:00
That is now merged. If there's no reply in like a week or so, I'll assume you were using such a system and close.

## Ulmo | 2018-11-06T23:08:11+00:00
I appologize that I haven't had time to look into this.

I'm back.  Ok, my Monero Dragon has been behaving ever since I updated it on 2018-10-30T13:47:37.654258251-07 at head 29073f65e8816d4c32b6ffef514943a5650b8d3b.  I don't know what fixed it.  I don't think I changed the way I was running it.  I did notice that I was not able to suspend it and put it into background, but I think I tried foreground when it failed, too.  Something fixed it.  I was able to use my old wallet with the new dragon and slay the coins.  Well, transmit them.  I was able to use them with a trading partner, too.  Everything is working the last time I awoke the dragon, but I have since put it back to sleep since I don't need its chained blocks right now.

## moneromooo-monero | 2019-03-13T17:28:24+00:00
Alright, reopen if it breaks again then (with recent master).

+invalid

## bladeFury | 2019-07-13T03:17:44+00:00
I'm getting this stack trace when build from source using v0.14.1.0, but no error with pre builded binary,  Is it related to boost version?

2019-07-13 03:00:58.474	    7f0196d1dbc0	WARNING	global	src/blockchain_db/lmdb/db_lmdb.cpp:1314	The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2019-07-13 03:01:01.616	    7f0196d1dbc0	INFO	global	src/cryptonote_core/cryptonote_core.cpp:651	Loading checkpoints
2019-07-13 03:01:06.474	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::thread_interrupted
2019-07-13 03:01:06.474	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2019-07-13 03:01:06.475	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x10d) [0x55fdfc37295d]:__cxa_throw+0x10d) [0x55fdfc37295d]
2019-07-13 03:01:06.475	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x76) [0x7f01945d3ae6]:_64-linux-gnu/libboost_thread.so.1.65.1(_ZN5boost11this_thread18interruption_pointEv+0x76) [0x7f01945d3ae6]
2019-07-13 03:01:06.475	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x31c) [0x55fdfc1c7d2c]:_ZZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE4initERKN5boost15program_options13variables_mapEENKUlvE_clEv+0x31c) [0x55fdfc1c7d2c]
2019-07-13 03:01:06.475	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x11bcd) [0x7f01945d3bcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7f01945d3bcd]
2019-07-13 03:01:06.475	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x76db) [0x7f0193a6b6db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f0193a6b6db]
2019-07-13 03:01:06.475	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x3f) [0x7f019379488f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f019379488f]
2019-07-13 03:01:06.475	    7f018e98c700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2019-07-13 03:01:07.110	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::thread_interrupted
2019-07-13 03:01:07.110	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2019-07-13 03:01:07.111	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x10d) [0x55fdfc37295d]:__cxa_throw+0x10d) [0x55fdfc37295d]
2019-07-13 03:01:07.111	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x76) [0x7f01945d3ae6]:_64-linux-gnu/libboost_thread.so.1.65.1(_ZN5boost11this_thread18interruption_pointEv+0x76) [0x7f01945d3ae6]
2019-07-13 03:01:07.111	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x31c) [0x55fdfc1c7d2c]:_ZZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE4initERKN5boost15program_options13variables_mapEENKUlvE_clEv+0x31c) [0x55fdfc1c7d2c]
2019-07-13 03:01:07.111	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x11bcd) [0x7f01945d3bcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7f01945d3bcd]
2019-07-13 03:01:07.111	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x76db) [0x7f0193a6b6db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f0193a6b6db]
2019-07-13 03:01:07.111	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x3f) [0x7f019379488f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f019379488f]
2019-07-13 03:01:07.111	    7f018f18d700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2019-07-13 03:01:16.030	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::thread_interrupted
2019-07-13 03:01:16.031	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2019-07-13 03:01:16.031	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x10d) [0x55fdfc37295d]:__cxa_throw+0x10d) [0x55fdfc37295d]
2019-07-13 03:01:16.031	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2]  0x76) [0x7f01945d3ae6]:_64-linux-gnu/libboost_thread.so.1.65.1(_ZN5boost11this_thread18interruption_pointEv+0x76) [0x7f01945d3ae6]
2019-07-13 03:01:16.031	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3]  0x31c) [0x55fdfc1c7d2c]:_ZZN8nodetool11node_serverIN10cryptonote29t_cryptonote_protocol_handlerINS1_4coreEEEE4initERKN5boost15program_options13variables_mapEENKUlvE_clEv+0x31c) [0x55fdfc1c7d2c]
2019-07-13 03:01:16.031	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4]  0x11bcd) [0x7f01945d3bcd]:_64-linux-gnu/libboost_thread.so.1.65.1(+0x11bcd) [0x7f01945d3bcd]
2019-07-13 03:01:16.031	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5]  0x76db) [0x7f0193a6b6db]:_64-linux-gnu/libpthread.so.0(+0x76db) [0x7f0193a6b6db]
2019-07-13 03:01:16.032	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6]  0x3f) [0x7f019379488f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7f019379488f]
2019-07-13 03:01:16.032	    7f019018f700	INFO	stacktrace	src/common/stack_trace.cpp:172	
2019-07-13 03:01:33.494	    7f0196d1dbc0	INFO	global	src/daemon/core.h:83	Core initialized OK
2019-07-13 03:01:33.495	    7f0196d1dbc0	INFO	global	src/daemon/rpc.h:73	Starting core RPC server...
2019-07-13 03:01:33.495	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:78	core RPC server started ok
2019-07-13 03:01:33.497	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:78	Starting p2p net loop...

# Action History
- Created by: Ulmo | 2018-10-19T18:42:34+00:00
- Closed at: 2019-03-13T17:34:05+00:00
