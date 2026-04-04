---
title: Exception in Ubuntu 24.04.1 LTS using v0.18.3.4
source_url: https://github.com/monero-project/monero/issues/9757
author: juazki
assignees: []
labels:
- question
created_at: '2025-01-31T09:17:10+00:00'
updated_at: '2025-01-31T17:33:47+00:00'
type: issue
status: closed
closed_at: '2025-01-31T17:33:47+00:00'
---

# Original Description
Running in Ubuntu 24.04.1 LTS, built v0.18.3.4 using Docker.

When running the daemon from the GUI it fails to start up with the following log output:

> 2025-01-31 09:11:23.850	    7a36a8b847c0	INFO	logging	contrib/epee/src/mlog.cpp:274	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2025-01-31 09:11:23.850	    7a36a8b847c0	INFO	global	src/daemon/main.cpp:309	Monero 'Fluorine Fermi' (v0.18.3.4-release)
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::system::system_error>
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1] /home/william/monero-gui/build/release/bin/monerod(+0x5053da) [0x6380393053da] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /home/william/monero-gui/build/release/bin/monerod(+0x164c17) [0x638038f64c17] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /home/william/monero-gui/build/release/bin/monerod(+0x245d7f) [0x638039045d7f] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /home/william/monero-gui/build/release/bin/monerod(+0x248650) [0x638039048650] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /home/william/monero-gui/build/release/bin/monerod(+0x1bd11b) [0x638038fbd11b] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /home/william/monero-gui/build/release/bin/monerod(+0x1bd80e) [0x638038fbd80e] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /home/william/monero-gui/build/release/bin/monerod(+0x1bdcbf) [0x638038fbdcbf] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /home/william/monero-gui/build/release/bin/monerod(+0x211532) [0x638039011532] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /home/william/monero-gui/build/release/bin/monerod(+0x1b0663) [0x638038fb0663] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /home/william/monero-gui/build/release/bin/monerod(+0xfc241) [0x638038efc241] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /home/william/monero-gui/build/release/bin/monerod(+0xf6ed4) [0x638038ef6ed4] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /home/william/monero-gui/build/release/bin/monerod(+0xd57fd) [0x638038ed57fd] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13]  0x2a1ca) [0x7a36a882a1ca]:_64-linux-gnu/libc.so.6(+0x2a1ca) [0x7a36a882a1ca]
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14]  0x8b) [0x7a36a882a28b]:_64-linux-gnu/libc.so.6(__libc_start_main+0x8b) [0x7a36a882a28b]
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] /home/william/monero-gui/build/release/bin/monerod(+0xe7e49) [0x638038ee7e49] 
2025-01-31 09:11:35.907	    7a36a8b847c0	INFO	stacktrace	src/common/stack_trace.cpp:172	
2025-01-31 09:11:35.908	    7a36a8b847c0	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081


I have tried to build the master branch and I am getting the same issue.

Any ideas?

# Discussion History
## selsta | 2025-01-31T13:13:44+00:00
Do you mean https://github.com/monero-project/monero-gui/blob/master/Dockerfile.linux? This is only for building the GUI binary, not monerod. Can you try to use monerod from getmonero.org CLI downloads and see if it works?

## juazki | 2025-01-31T16:50:46+00:00
I have always used the build instructions of the Monero GUI build everything and run it from there. Those commands build the gui, the cli and the daemon. This setup has worked without issues for some time now. First, I used to build all from source and then they moved to the Docker setup which has worked fine in the past.

I would prefer to build everything from source instead of downloading.

## juazki | 2025-01-31T16:52:15+00:00
I opened the issue here since it looks like something related to the daemon and not the GUI, but I could open it in the repository of the GUI if you think it makes more sense.

## juazki | 2025-01-31T17:24:50+00:00
I have built the daemon from this repository and it works now. The binaries are definitely not the same. 

I have checked and the GUI build does static build while I did not do static when I built the repository from here. Maybe that is the problem.

## selsta | 2025-01-31T17:29:12+00:00
To get a static `monerod`, you can use the gitian build system: https://github.com/monero-project/monero/tree/release-v0.18/contrib/gitian

The docker build in monero-gui repo is only for building the GUI binary. I guess that can be better documented to avoid confusion.

# Action History
- Created by: juazki | 2025-01-31T09:17:10+00:00
- Closed at: 2025-01-31T17:33:47+00:00
