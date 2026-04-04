---
title: GUI daemon on OSx can't sync the last blocks
source_url: https://github.com/monero-project/monero/issues/2014
author: kamushki
assignees: []
labels:
- invalid
created_at: '2017-05-04T18:26:39+00:00'
updated_at: '2017-08-07T19:12:18+00:00'
type: issue
status: closed
closed_at: '2017-08-07T19:12:18+00:00'
---

# Original Description
after "friend" messed with it trying to speed up the synchronization, which was almost finished after 3 days of working(Indian inet), the network status went "Disconnected" (while the internet connection is fine)and in "send" it's failing to connect the wallet to daemon,and the sync process stuck on the same block,since yesterday it shows the same :
2017-05-04 23:36:33.157		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1223958/1223958 (100.0%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 1(out)+0(in) connections, uptime 0d 0h 0m 11s

2017-05-04 23:38:49.640		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1223958/1302929 (93.9%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 6(out)+0(in) connections, uptime 0d 0h 2m 27s

2017-05-04 23:50:38.437		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1223958/1302938 (93.9%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 8(out)+0(in) connections, uptime 0d 0h 14m 16s


Just after creating the wallet I've sent some xmr to it, the transaction appears on the blockchain ,but not in the wallet , will it appear when sync is done?
how to solve this daemon issue?

# Discussion History
## moneromooo-monero | 2017-05-06T11:49:36+00:00
Exit the daemon, and restart it with --log-level 1. It will then retry the sync and print more information about what is failing.

## kamushki | 2017-05-06T14:23:52+00:00
Thanx for help
Just did it:

2017-05-06 19:30:12.691		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-06 19:30:12.698		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-05-06 19:30:14.264		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-06 19:30:14.268		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-05-06 19:30:45.296		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-06 19:30:45.301		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-05-06 19:30:47.372		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-06 19:30:47.377		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-05-06 19:30:49.439		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-06 19:30:49.444		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-05-06 19:30:51.507		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-06 19:30:51.512		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-05-06 19:30:53.575		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-06 19:30:53.579		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-05-06 19:30:55.654		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1226558/1226558 (100.0%) on mainnet, not mining, net hash 49.71 MH/s, v4, up to date, 0(out)+0(in) connections, uptime 0d 0h 0m 13s

2017-05-06 19:31:23.034		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1226558/1226558 (100.0%) on mainnet, not mining, net hash 49.71 MH/s, v4, up to date, 2(out)+0(in) connections, uptime 0d 0h 0m 30s

2017-05-06 19:52:43.659		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1226558/1304227 (94.0%) on mainnet, not mining, net hash 49.71 MH/s, v4, up to date, 6(out)+0(in) connections, uptime 0d 0h 21m 50s


## kamushki | 2017-05-08T05:45:01+00:00
I still can't see my balance ... should I follow the suggestion to use remote node: node.moneroclub.com 8880 ?

## moneromooo-monero | 2017-05-08T20:37:32+00:00
You should post the log with level 1 as requested. You just posted irrelevant stuff AFAICT. The log is in ~/.bitmonero/bitmonero.log

## kamushki | 2017-05-09T02:09:14+00:00
I have set level 1 and that was the result...
I'm not a dev, jusr made a mistake cause unclear info on monero wallets, and have sent quite a lot XMR to the GUI just after openning it , and now can't access my funds... is there another(working) wallet that i can recover the Gui on with 25 w. mnemonic ???

## kamushki | 2017-05-09T02:43:33+00:00
I think that daemon address set wrong, cause network status disconnected

## moneromooo-monero | 2017-05-13T10:13:00+00:00
You're saying that what you posted in the contents of ~/.bitmonero/bitmonero.log ?
If so, then there's a problem somehwere, there should be a lot more than that.
Do you have another daemon running at the same time ?

## kamushki | 2017-05-13T12:22:24+00:00
Already synced with remote node as per advise i got on reddit...
Very poor support here(

## moneromooo-monero | 2017-05-13T18:05:47+00:00
That's because this is a bug tracker, not a support helpline...

## kamushki | 2017-05-14T03:09:49+00:00
Where is a monero support helpline?)

## moneromooo-monero | 2017-05-14T07:05:37+00:00
Try IRC on Freenode, #monero

## moneromooo-monero | 2017-08-07T18:01:25+00:00
No evidence of a bug, closing.

+invalid

## moneromooo-monero | 2017-08-07T19:06:56+00:00
+resolved

# Action History
- Created by: kamushki | 2017-05-04T18:26:39+00:00
- Closed at: 2017-08-07T19:12:18+00:00
