---
title: 'Error: Couldn''t connect to daemon'
source_url: https://github.com/monero-project/monero/issues/2083
author: fresheneesz
assignees: []
labels:
- invalid
created_at: '2017-06-12T03:37:26+00:00'
updated_at: '2017-09-25T19:32:55+00:00'
type: issue
status: closed
closed_at: '2017-09-25T18:48:24+00:00'
---

# Original Description
I'm getting a bunch of errors in my daemon status log and while the gui client *says* "Network status: Synchronizing", its clearly not. Here are the errors:

```
2017-06-11 20:27:03.695	12008	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:04.703	12008	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:12.654	11380	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:13.663	11380	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:15.682	7560	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:16.685	7560	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:18.703	11740	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:19.705	11740	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:21.723	7568	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:22.725	7568	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:24.743	11336	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:25.745	11336	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:27.768	11804	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:28.768	11804	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:30.787	8904	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-06-11 20:27:31.787	8904	ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-06-11 20:27:33.807	10028	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1324846/1324846 (100.0%) on mainnet, not mining, net hash 76.90 MH/s, v5, up to date, 0(out)+1(in) connections, uptime 0d 0h 0m 3s

2017-06-11 20:28:59.213	3776	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1324846/1330608 (99.6%) on mainnet, not mining, net hash 76.90 MH/s, v5, up to date, 8(out)+4(in) connections, uptime 0d 0h 1m 27s

2017-06-11 20:29:00.425	10524	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1324846/1330608 (99.6%) on mainnet, not mining, net hash 76.90 MH/s, v5, up to date, 8(out)+4(in) connections, uptime 0d 0h 1m 28s
```

The gui says "GUI version: release", "Embedded Monero version: release". Is it supposed to just say "release" and not a specific version? Also, I'm currently  5167 blocks behind and counting. It seems to be registering that new blocks have happened and the gui client updates that number of blocks remaining updates every once in a while to go up a block or two, but its not downloading or processing new blocks.


# Discussion History
## fresheneesz | 2017-06-12T03:50:09+00:00
Hmm, it started working now . Not sure what was going on, but something seems wrong if the GUI says "Synchronizing" when it can't connect to the daemon.

## Jaqueeee | 2017-06-12T05:35:27+00:00
Nothing wrong there. Log says "couldn't connect to daemon" for a little while before the daemon is fully started and accept connection from gui. On last row you see that the daemon is running and it's syncing. 

The version tags on settings will be corrected in next release. For now the "release" is the latest version. 

## fresheneesz | 2017-06-13T00:18:41+00:00
> On last row you see that the daemon is running and it's syncing.

Why does it have a ton of things that say "warning" and "fatal" on it then? 

```
New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL
```

Something is either wrong with logging or something is wrong with monero. Either way, something should be fixed.


## moneromooo-monero | 2017-06-13T22:45:41+00:00
It tells you which logging parameters are active. This is mormal.

## fresheneesz | 2017-06-14T03:15:59+00:00
Ok.. That's a pretty strange way to present every single log with very redundant info like that. Why not just print out logging categories when they actually change so you don't have to print them out every log?

But fine, regardless, the GUI shouldn't say "Syncing" if its not actually connected, right?

## Jaqueeee | 2017-06-14T21:22:53+00:00
@fresheneesz 
Agree the log output isn't optimal. 
Wrt status. We could change it to "Connecting" or similar until sync starts. 
However, the GUI repo is https://github.com/monero-project/monero-core
Please submit an issue there if you'd like. 


## fresheneesz | 2017-06-15T07:18:23+00:00
Ok, will do. Thanks!

## moneromooo-monero | 2017-07-31T19:26:49+00:00
Yes, it should print this only when the settings change. So I guess they're changing. Or it's a new process started each time.

## moneromooo-monero | 2017-09-25T18:42:45+00:00
Looks like it was just waiting for the daemon to be ready before connecting.

+invalid

## fresheneesz | 2017-09-25T19:32:43+00:00
@moneromooo-monero Has the GUI been improved to report more correctly what's going on? My understanding is that this ticket should be closed when the GUI reports "Connecting" while its trying to connect to the daemon, rather than "Syncing". Has this happened? If not, please reopen.

# Action History
- Created by: fresheneesz | 2017-06-12T03:37:26+00:00
- Closed at: 2017-09-25T18:48:24+00:00
