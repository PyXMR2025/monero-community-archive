---
title: bitmonero.log is full of "Failed to read line."
source_url: https://github.com/monero-project/monero/issues/7539
author: M0ns1gn0r
assignees: []
labels: []
created_at: '2021-03-12T19:52:11+00:00'
updated_at: '2021-04-06T18:24:19+00:00'
type: issue
status: closed
closed_at: '2021-04-06T18:24:18+00:00'
---

# Original Description
I have 90 log files with only this message:

```
2021-03-12 19:48:12.919	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.919	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.919	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.919	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.919	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.919	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.919	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.920	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.920	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-12 19:48:12.920	12540	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
```

A new 100 MB file is produced every minute.

Monero GUI 0.17.1.9-release on Win 7 x64


# Discussion History
## moneromooo-monero | 2021-03-12T20:28:03+00:00
Are you piping anything into whatever program generates this ? Or executing it from a non shell program, that kind of thing ?

## M0ns1gn0r | 2021-03-13T09:41:10+00:00
@moneromooo-monero 

I open `monero-wallet-gui.exe` from `Total Commander`, then the GUI automatically starts the `monerod.exe` (I use the simple mode). 

But the problem persists even if I start `monero-wallet-gui.exe` directly from the explorer.

## M0ns1gn0r | 2021-03-13T21:16:13+00:00
The problem doesn't reproduce if I open the GUI client via `start-low-graphics-mode.bat`. 

## mj-xmr | 2021-03-15T13:15:54+00:00
> I have 90 log files with only this message:

Please give a few examples of file names of the log files. I'll look into it.


## M0ns1gn0r | 2021-03-15T13:26:26+00:00
@mj-xmr 
```
bitmonero.log
bitmonero.log-part-1
bitmonero.log-part-2
bitmonero.log-part-3
```

And so on. Then it looks like that a rolling log mechanism overrides them.

## mj-xmr | 2021-03-15T19:28:18+00:00
From IRC:

_(selsta) usual solution is attempt to update drivers and check if issue reappears_

## selsta | 2021-03-15T19:40:22+00:00
Talking about graphics drivers

## M0ns1gn0r | 2021-03-15T19:41:19+00:00
As I said, the issue disappears when I start the GUI from the command line. It's hard to believe that the graphics drivers can have something to do with that. But I'll give it a try.

## M0ns1gn0r | 2021-03-15T19:45:00+00:00
Sorry, I forgot to mention, that the issue disappears not because of the "low graphics" mode, but because the GUI is started from the command line. I checked that by changing the script to: 
```
@echo off

start /b monero-wallet-gui.exe
```

## selsta | 2021-03-15T19:52:32+00:00
Ok, sorry then I misunderstood this. Usually if things work with low graphics mode it means it is graphics drivers related but in your case it seems command line (or something else) related.

## M0ns1gn0r | 2021-03-15T20:02:15+00:00
No problem. Maybe the problem lays in Win7 x64.

This is how the log looks like after starting the GUI:
```
2021-03-15 19:58:20.844	6960	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-03-15 19:58:20.844	6960	INFO	global	src/daemon/main.cpp:294	Monero 'Oxygen Orion' (v0.17.1.9-release)
2021-03-15 19:58:20.844	6960	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2021-03-15 19:58:20.844	6960	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2021-03-15 19:58:20.845	6960	INFO	global	src/daemon/core.h:63	Initializing core...
2021-03-15 19:58:20.845	6960	INFO	global	src/cryptonote_core/cryptonote_core.cpp:515	Loading blockchain from folder <redacted> ...
2021-03-15 19:58:21.070	6960	INFO	global	src/cryptonote_core/cryptonote_core.cpp:690	Loading checkpoints
2021-03-15 19:58:21.070	6960	INFO	global	src/daemon/core.h:73	Core initialized OK
2021-03-15 19:58:21.070	6960	INFO	global	src/daemon/p2p.h:63	Initializing p2p server...
2021-03-15 19:58:21.110	6960	INFO	global	src/daemon/p2p.h:68	p2p server initialized OK
2021-03-15 19:58:21.110	6960	INFO	global	src/daemon/rpc.h:63	Initializing core RPC server...
2021-03-15 19:58:21.111	6960	INFO	global	contrib/epee/include/net/http_server_impl_base.h:79	Binding on 127.0.0.1 (IPv4):18081
2021-03-15 19:58:22.042	6960	INFO	global	src/daemon/rpc.h:69	core RPC server initialized OK on port: 18081
2021-03-15 19:58:22.078	6960	INFO	global	src/daemon/rpc.h:74	Starting core RPC server...
2021-03-15 19:58:22.079	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:79	core RPC server started ok
2021-03-15 19:58:22.079	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:78	Starting p2p net loop...
2021-03-15 19:58:22.079	8852	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-15 19:58:22.080	8852	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
2021-03-15 19:58:22.080	8852	ERROR	console_handler	contrib/epee/include/console_handler.h:397	Failed to read line.
...and so on...
```

## moneromooo-monero | 2021-03-18T22:26:09+00:00
My guess is that Total Commander changes the new process' stdin, which causes monerod to be unable to read from it. Maybe the GUI does not start monerod with --non-interactive ?

## xiphon | 2021-03-19T10:33:39+00:00
> Maybe the GUI does not start monerod with --non-interactive ?

Yep. https://github.com/monero-project/monero-gui/pull/3360

# Action History
- Created by: M0ns1gn0r | 2021-03-12T19:52:11+00:00
- Closed at: 2021-04-06T18:24:18+00:00
