---
title: 0.12 failed to run as service under Windows
source_url: https://github.com/monero-project/monero/issues/3508
author: Keksov
assignees: []
labels: []
created_at: '2018-03-28T09:02:44+00:00'
updated_at: '2018-08-15T13:09:00+00:00'
type: issue
status: closed
closed_at: '2018-08-15T13:09:00+00:00'
---

# Original Description
Just upgrading monerod to the new version. Removed old version and install new one with command monerod --install-service. Got strange errors in log after start and monerod removes itself from services list automatically. System: Windows Server 2008 R2. Previous version was running without any problems and if I start monerod from command line widow it works without errors. The only noticeable difference in log file is that while starting as service it tries to bind to ZMQ socket, in normal mode (from cmd line) it didn't

2018-03-28 08:53:59.722	2576	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-03-28 08:53:59.722	2576	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-03-28 08:53:59.737	2576	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Service installed
2018-03-28 08:55:05.850	1224	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-03-28 08:55:05.850	1224	INFO 	global	src/daemon/main.cpp:280	Monero 'Lithium Luna' (v0.12.0.0-master-release)
2018-03-28 08:55:05.850	1224	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.0.0-master-release) Daemonised
2018-03-28 08:55:05.850	1224	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-03-28 08:55:05.850	1224	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-03-28 08:55:05.850	1224	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-03-28 08:55:10.140	1224	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-03-28 08:55:10.624	1224	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-03-28 08:55:10.624	1224	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 127.0.0.1:18081
2018-03-28 08:55:10.624	1224	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-03-28 08:55:10.624	2144	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-03-28 08:55:10.624	2144	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-03-28 08:55:10.702	2144	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:525	Loading checkpoints
2018-03-28 08:55:10.811	2144	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-03-28 08:55:10.811	2144	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-03-28 08:55:10.811	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-03-28 08:55:10.842	[SRV_MAIN]	ERROR	default	src/rpc/zmq_server.cpp:112	Error creating ZMQ Socket: Invalid argument
2018-03-28 08:55:10.842	[SRV_MAIN]	ERROR	daemon	src/daemon/daemon.cpp:162	Failed to add TCP Socket (:) to ZMQ RPC Server
2018-03-28 08:55:10.842	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-03-28 08:55:10.842	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-03-28 08:55:10.842	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-03-28 08:55:10.842	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-03-28 08:55:14.898	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-03-28 08:55:15.008	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-03-28 08:55:15.008	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-03-28 08:55:15.008	[SRV_MAIN]	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Service uninstalled

# Discussion History
## laurencee | 2018-03-30T11:14:13+00:00
Yep same issue on Win 10 x64

## kadzsol | 2018-03-30T19:49:11+00:00
Same issue Win 10 pro x64

## tinola | 2018-04-03T20:53:41+00:00
Yep, same for me, Win 10 ent x64

...
[SRV_MAIN] ERROR default src/rpc/zmq_server.cpp:112 Error creating ZMQ Socket: Invalid argument
[SRV_MAIN] ERROR daemon src/daemon/daemon.cpp:162 Failed to add TCP Socket (:) to ZMQ RPC Server
...

## leerees | 2018-04-04T11:33:24+00:00
Same here, I'm thinking maybe we was supposed to export our old wallets before upgrading. 

## moneromooo-monero | 2018-04-04T12:20:10+00:00
If someone who gets that problem can compile with a patch, try this and post the new log (default settings):

```
diff --git a/src/rpc/zmq_server.cpp b/src/rpc/zmq_server.cpp
index 3aee8c4..2dea932 100644
--- a/src/rpc/zmq_server.cpp
+++ b/src/rpc/zmq_server.cpp
@@ -98,14 +98,20 @@ bool ZmqServer::addTCPSocket(std::string address, std::string port)
 {
   try
   {
+MGINFO("trace");
     std::string addr_prefix("tcp://");
 
+MGINFO("trace");
     rep_socket.reset(new zmq::socket_t(context, ZMQ_REP));
 
+MGINFO("trace");
     rep_socket->setsockopt(ZMQ_RCVTIMEO, &DEFAULT_RPC_RECV_TIMEOUT_MS, sizeof(DEFAULT_RPC_RECV_TIMEOUT_MS));
 
+MGINFO("trace");
     std::string bind_address = addr_prefix + address + std::string(":") + port;
+MGINFO("trace, address: [" << bind_address << "]");
     rep_socket->bind(bind_address.c_str());
+MGINFO("trace");
   }
   catch (const std::exception& e)
   {

```

## Keksov | 2018-04-04T13:33:01+00:00
How to build monerod for Windows?

## moneromooo-monero | 2018-04-04T14:35:52+00:00
Instructions are in the README.md file.

## Keksov | 2018-04-04T16:34:36+00:00
Looks like libreadline compiled without lib(n)curse. How can I tell cmake to add -lncurses?
Got build error:
```
/C/msys64/mingw64/bin/cmake.exe -E remove -f CMakeFiles/cmTC_d0d72.dir/objects.a
ar cr CMakeFiles/cmTC_d0d72.dir/objects.a "CMakeFiles/cmTC_d0d72.dir/CheckFunctionExists.c.obj" 
/C/msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe  -fno-strict-aliasing -maes -std=c11 -D_GNU_SOURCE -m64 -DWIN32_LEAN_AND_MEAN  -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-unused-variable -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-error=unused-value -Wno-error=unused-but-set-variable -Waggregate-return -Wnested-externs -Wold-style-definition -Wstrict-prototypes -march=x86-64  -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fno-strict-aliasing -DCHECK_FUNCTION_EXISTS=rl_filename_completion_function    -Wl,--whole-archive CMakeFiles/cmTC_d0d72.dir/objects.a -Wl,--no-whole-archive  -o cmTC_d0d72.exe -Wl,--major-image-version,0,--minor-image-version,0 /C/msys64/mingw64/lib/libreadline.a -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 
C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0xa3f): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0xb6d): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0xbcf): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0x1895): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0x2a27): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(display.o):(.text+0x2d21): more undefined references to `tputs' follow

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x20c): undefined reference to `tgetnum'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x2e9): undefined reference to `tgetnum'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x714): undefined reference to `tgetent'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x752): undefined reference to `tgetstr'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x7b3): undefined reference to `tgetflag'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x802): undefined reference to `tgetflag'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0x877): undefined reference to `tgetflag'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xaf7): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xba9): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xc17): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xc6d): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xc9d): undefined reference to `tputs'

C:/msys64/mingw64/lib/libreadline.a(terminal.o):(.text+0xce0): more undefined references to `tputs' follow

collect2.exe: error: ld returned 1 exit status
```


## moneromooo-monero | 2018-04-04T17:48:03+00:00
In build/debug/CMakeCache.txt, look for Readline_LIBRARY, and add the path to libncurses.so at the end, with a space delimiter.

## kadzsol | 2018-04-07T11:12:50+00:00
anyone managed to get it fixed?

## Sylvyrfysh | 2018-04-30T22:01:43+00:00
Try libncurses.a

## kadzsol | 2018-05-01T15:39:33+00:00
Would it be possible for you to compile with this and share the extra log or send me the binary so I can create the log?

-----

If someone who gets that problem can compile with a patch, try this and post the new log (default settings):

diff --git a/src/rpc/zmq_server.cpp b/src/rpc/zmq_server.cpp
index 3aee8c4..2dea932 100644
--- a/src/rpc/zmq_server.cpp
+++ b/src/rpc/zmq_server.cpp
@@ -98,14 +98,20 @@ bool ZmqServer::addTCPSocket(std::string address, std::string port)
 {
   try
   {
+MGINFO("trace");
     std::string addr_prefix("tcp://");
 
+MGINFO("trace");
     rep_socket.reset(new zmq::socket_t(context, ZMQ_REP));
 
+MGINFO("trace");
     rep_socket->setsockopt(ZMQ_RCVTIMEO, &DEFAULT_RPC_RECV_TIMEOUT_MS, sizeof(DEFAULT_RPC_RECV_TIMEOUT_MS));
 
+MGINFO("trace");
     std::string bind_address = addr_prefix + address + std::string(":") + port;
+MGINFO("trace, address: [" << bind_address << "]");
     rep_socket->bind(bind_address.c_str());
+MGINFO("trace");
   }
   catch (const std::exception& e)
   {



## kadzsol | 2018-06-14T20:43:43+00:00
anyone still busy with this?

## moneromooo-monero | 2018-06-17T12:50:39+00:00
I've added the patch to a dummy PR in https://github.com/monero-project/monero/pull/4009 so the build bot will build a windows binary with it.

## moneromooo-monero | 2018-06-17T14:24:46+00:00
It's built, there are downloadable binaries from https://build.getmonero.org/builders/monero-static-win64/builds/4682. This is based off the release-v0.12 branch.


## kadzsol | 2018-06-17T14:31:28+00:00
Testing it now...

## kadzsol | 2018-06-17T14:49:14+00:00
I have manually overwrote the binaries in my previous installation (that is why version still seems 0.11). it installs OK as a service.
 
C:\monero\monero-gui-0.11.0.0>monerod --install-service
2018-06-17 14:41:49.733 6632    INFO    global  src/daemon/main.cpp:279 Monero 'Lithium Luna' (v0.12.2.0-4b004ef3)
Service installed

I can also start it:

C:\monero\monero-gui-0.11.0.0>monerod --start-service
2018-06-17 14:42:02.592 2300    INFO    global  src/daemon/main.cpp:279 Monero 'Lithium Luna' (v0.12.2.0-4b004ef3)
Starting service
Service started

Unfortunately, it deinstalls itself like the older 0.12 version did.

C:\monero\monero-gui-0.11.0.0>monerod --stop-service
2018-06-17 14:46:06.874 5224    INFO    global  src/daemon/main.cpp:279 Monero 'Lithium Luna' (v0.12.2.0-4b004ef3)
Stopping service
Error: Couldn't find service: The specified service does not exist as an installed service.

C:\monero\monero-gui-0.11.0.0>monerod --start-service
2018-06-17 14:43:33.014 6316    INFO    global  src/daemon/main.cpp:279 Monero 'Lithium Luna' (v0.12.2.0-4b004ef3)
Starting service
Error: Couldn't find service: The specified service does not exist as an installed service.



## kadzsol | 2018-06-17T14:53:36+00:00
Here is the log of installing and starting.

2018-06-17 14:52:19.218	984	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-17 14:52:19.218	984	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-4b004ef3)
2018-06-17 14:52:19.233	984	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Service installed
2018-06-17 14:52:25.577	5828	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-17 14:52:25.577	5828	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-4b004ef3)
2018-06-17 14:52:25.593	5828	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting service
2018-06-17 14:52:28.562	7128	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-17 14:52:28.562	7128	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-4b004ef3)
2018-06-17 14:52:28.562	7128	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.2.0-4b004ef3) Daemonised
2018-06-17 14:52:28.562	7128	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-06-17 14:52:28.562	7128	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-06-17 14:52:28.562	7128	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-06-17 14:52:33.374	7128	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-06-17 14:52:34.468	7128	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-06-17 14:52:34.468	7128	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 192.168.0.200:18081
2018-06-17 14:52:34.468	7128	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-06-17 14:52:34.468	5828	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Service started
2018-06-17 14:52:34.468	6320	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-06-17 14:52:34.483	6320	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-06-17 14:52:35.218	6320	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:526	Loading checkpoints
2018-06-17 14:52:35.530	6320	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-06-17 14:52:35.530	6320	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-06-17 14:52:35.530	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-06-17 14:52:35.546	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:101	trace
2018-06-17 14:52:35.546	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:104	trace
2018-06-17 14:52:35.608	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:107	trace
2018-06-17 14:52:35.608	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:110	trace
2018-06-17 14:52:35.608	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:112	trace, address: [tcp://:]
2018-06-17 14:52:35.608	[SRV_MAIN]	ERROR	default	src/rpc/zmq_server.cpp:118	Error creating ZMQ Socket: Invalid argument
2018-06-17 14:52:35.608	[SRV_MAIN]	ERROR	daemon	src/daemon/daemon.cpp:162	Failed to add TCP Socket (:) to ZMQ RPC Server
2018-06-17 14:52:35.608	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-06-17 14:52:35.624	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:84	Stopping core RPC server...
2018-06-17 14:52:35.624	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:96	Deinitializing core RPC server...
2018-06-17 14:52:35.624	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:90	Deinitializing p2p...
2018-06-17 14:52:39.921	[SRV_MAIN]	INFO 	global	src/daemon/core.h:103	Deinitializing core...
2018-06-17 14:52:40.312	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2018-06-17 14:52:40.312	[SRV_MAIN]	INFO 	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2018-06-17 14:52:40.312	[SRV_MAIN]	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Service uninstalled


## moneromooo-monero | 2018-06-17T19:17:46+00:00
https://build.getmonero.org/builders/monero-static-win64/builds/4685 might fix. If not, post the logs please,

## kadzsol | 2018-06-17T19:42:05+00:00
**This one works!!!**

2018-06-17 19:33:11.068	7024	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-17 19:33:11.068	7024	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-21d35746)
2018-06-17 19:33:11.084	7024	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Service installed
2018-06-17 19:33:18.209	5412	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-17 19:33:18.209	5412	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-21d35746)
2018-06-17 19:33:18.256	5412	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Starting service
2018-06-17 19:33:21.521	7140	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-06-17 19:33:21.521	7140	INFO 	global	src/daemon/main.cpp:279	Monero 'Lithium Luna' (v0.12.2.0-21d35746)
2018-06-17 19:33:21.537	7140	WARN 	daemon	src/daemon/executor.cpp:61	Monero 'Lithium Luna' (v0.12.2.0-21d35746) Daemonised
2018-06-17 19:33:21.537	7140	INFO 	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2018-06-17 19:33:21.537	7140	INFO 	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2018-06-17 19:33:21.537	7140	INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2018-06-17 19:33:26.615	7140	INFO 	global	src/daemon/p2p.h:68	p2p server initialized OK
2018-06-17 19:33:27.740	7140	INFO 	global	src/daemon/rpc.h:63	Initializing core RPC server...
2018-06-17 19:33:27.740	7140	INFO 	global	contrib/epee/include/net/http_server_impl_base.h:76	Binding on 192.168.0.200:18081
2018-06-17 19:33:27.740	7140	INFO 	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2018-06-17 19:33:27.740	5412	INFO 	msgwriter	src/common/scoped_message_writer.h:102	Service started
2018-06-17 19:33:27.740	1684	INFO 	global	src/daemon/core.h:86	Initializing core...
2018-06-17 19:33:27.740	1684	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:427	Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-06-17 19:33:28.537	1684	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:526	Loading checkpoints
2018-06-17 19:33:28.974	1684	INFO 	global	src/daemon/core.h:92	Core initialized OK
2018-06-17 19:33:28.974	1684	INFO 	global	src/daemon/rpc.h:74	Starting core RPC server...
2018-06-17 19:33:28.974	[SRV_MAIN]	INFO 	global	src/daemon/rpc.h:79	core RPC server started ok
2018-06-17 19:33:29.006	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:101	trace
2018-06-17 19:33:29.006	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:104	trace
2018-06-17 19:33:29.053	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:107	trace
2018-06-17 19:33:29.053	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:110	trace
2018-06-17 19:33:29.053	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:116	trace, address: [tcp://*:*]
2018-06-17 19:33:29.053	[SRV_MAIN]	INFO 	global	src/rpc/zmq_server.cpp:118	trace
2018-06-17 19:33:29.053	[SRV_MAIN]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2018-06-17 19:33:30.068	[P2P7]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1354	[1;33m
**********************************************************************
The daemon will start synchronizing with the network. This may take a long time to complete.


## moneromooo-monero | 2018-06-17T20:21:09+00:00
Great, thanks for testing, I'll PR it now.

## moneromooo-monero | 2018-08-15T13:06:43+00:00
Fixed in #4012

+resolved

# Action History
- Created by: Keksov | 2018-03-28T09:02:44+00:00
- Closed at: 2018-08-15T13:09:00+00:00
