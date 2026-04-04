---
title: OSX 10.9.5 - Daemon Failed to Start [+1]
source_url: https://github.com/monero-project/monero-gui/issues/644
author: srsandocan
assignees: []
labels:
- resolved
created_at: '2017-03-30T12:19:46+00:00'
updated_at: '2017-12-13T12:36:15+00:00'
type: issue
status: closed
closed_at: '2017-12-13T12:36:15+00:00'
---

# Original Description
Installed the new Monero GUI Beta 2
Worked all good on the instalation, added the password.
When trying to connect to the Daemon "waiting for daemon to start", it says

"Daemon failed to start" Please check your wallet and daemon log for errors. You can also try start monerod manually.

Tried to find the Logs but can't find it on the OSX (bitmonero.log or monero.log)

Rested and opened again, same message and when I click "ok" then i can go on "Settings" and "Start Daemon", now is synchronizing and looks like working, but not 100% Sure.

Will update after Sync

# Discussion History
## SamsungGalaxyPlayer | 2017-03-30T12:33:52+00:00
Similar to #642.

Can you try moving the files to a path that does not contain any spaces?

## srsandocan | 2017-03-30T12:39:56+00:00
Ok, done, look like same problem, doing some tests and let you know asap

## Jaqueeee | 2017-03-30T17:47:38+00:00
I didn't even know the GUI runs on 10.9.5. =)
Could you try this build from #646? https://build.getmonero.org/downloads/monero-wallet-gui-5d45967-osx-10.11.zip

If it doesnt make any difference. Here the logs on mac:
bitmonero.log 
[HOME_FOLDER]/.bitmonero/bitmonero.log
monero-wallet-gui.log
Right click monero-wallet-gui.app and select "show package contents"
Log file is located in Contents/Mac OS/monero-wallet-gui.log

Please also enable log level 3 on settings page. 



## srsandocan | 2017-03-30T18:57:58+00:00
:) Some times updating OS is really NOT the best option if you want your mac to run smooth.

Ok, so I rebooted some times and finally it started to sync.
After I saw your response, I changed the file to:
/volume/Users/myuser/Documents without changing name. It still synchronizing but it looks like same problems, some times some steps are not understood by the app and you need to toubleclick, or close and open.

Finally downloaded thw next Package you gave me #646 and looks like is working now with less problems but still synchronizing, I will write here again when is done.

Just one question, when I downloaded the new Package it still ask me for the password so I understand is reading from the same file, right? I can delete the older download without loosing my wallet?

P.S: Not a big deal as I'm just testing with a empty wallet but want to make sure of each step I'm doing.

I found the logs, thanks Jaqueeee, here is the output of the time it just failed again:

> 2017-03-30 19:10:19.807		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1286	refreshThreadFunc: m_refreshEnabled: 0
2017-03-30 19:10:19.807		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1287	refreshThreadFunc: m_status: 1
2017-03-30 19:10:19.807		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1275	refreshThreadFunc: waiting for refresh...
2017-03-30 19:10:24.983		DEBUG	WalletAPI	src/wallet/api/wallet.cpp:267	"2017-03-30 19:09:58.288\t\tINFO \tglobal\tcontrib/epee/src/mlog.cpp:145\tNew log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO\n2017-03-30 19:10:24.981\t\tERROR\tmsgwriter\tsrc/common/scoped_message_writer.h:94\tError: Couldn't connect to daemon\nError: Couldn't connect to daemon\n"

## srsandocan | 2017-03-30T20:05:47+00:00
Ok, here I come back, none of both working now:

When i check monero-wallet-gui.log here it is the output:

> wallet/api/wallet.cpp:267	>>> wallet updated
2017-03-30 22:02:16.904		DEBUG	WalletAPI	src/wallet/api/wallet.cpp:267	"2017-03-30 22:01:48.916\t\tINFO \tglobal\tcontrib/epee/src/mlog.cpp:145\tNew log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO\n2017-03-30 22:02:16.903\t\tERROR\tmsgwriter\tsrc/common/scoped_message_writer.h:94\tError: Couldn't connect to daemon\nError: Couldn't connect to daemon\n"
2017-03-30 22:02:16.904		DEBUG	WalletAPI	src/wallet/api/wallet.cpp:267	daemon not running. checking again in 2 seconds.
2017-03-30 22:02:16.906		DEBUG	WalletAPI	src/wallet/api/wallet.cpp:267	daemon start failed
2017-03-30 22:02:16.906		DEBUG	WalletAPI	src/wallet/api/wallet.cpp:267	Hiding processing splash
2017-03-30 22:02:16.907		DEBUG	WalletAPI	src/wallet/api/wallet.cpp:1330	startRefresh: refresh started/resumed...
2017-03-30 22:02:16.907		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1285	refreshThreadFunc: refresh lock acquired...
2017-03-30 22:02:16.907		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1286	refreshThreadFunc: m_refreshEnabled: 1
2017-03-30 22:02:16.907		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1287	refreshThreadFunc: m_status: 0
2017-03-30 22:02:16.907		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1289	refreshThreadFunc: refreshing...
2017-03-30 22:02:44.439		WARN 	net	contrib/epee/include/net/net_helper.h:177	Some problems at connect, message: Operation timed out
2017-03-30 22:03:12.439		WARN 	net	contrib/epee/include/net/net_helper.h:177	Some problems at connect, message: Operation timed out
2017-03-30 22:03:12.439		TRACE	WalletAPI	src/wallet/api/wallet.cpp:1315	doRefresh: skipping refresh - daemon is not synced
2017-03-30 22:03:12.439		DEBUG	WalletAPI	src/


When i go on " Show status" from GUI i have:

> 2017-03-30 21:19:42.181		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-03-30 21:23:12.235		ERROR	net.http	contrib/epee/include/net/http_client.h:441	Unexpected recv fail
2017-03-30 21:23:12.235		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-03-30 21:24:34.832		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-03-30 21:28:04.882		ERROR	net.http	contrib/epee/include/net/http_client.h:441	Unexpected recv fail
2017-03-30 21:28:04.890		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-03-30 21:30:38.637		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-03-30 21:34:08.691		ERROR	net.http	contrib/epee/include/net/http_client.h:441	Unexpected recv fail
2017-03-30 21:34:08.691		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-03-30 22:01:48.916		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-03-30 22:02:16.903		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

2017-03-30 22:03:38.900		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-03-30 22:04:06.758		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
Error: Couldn't connect to daemon

## srsandocan | 2017-03-30T22:41:19+00:00
Ok some update on it now that is synched.

When I open the wallet, is like if the GUI can't turn on the daemon, and I got the "Daemon failed to start" message again.
BUT, if I click on Connect, then it connect to the daemon.

It might be possible that the GUI is activating the daemon but not geting the answer correctly? So it's running but not connected if you don't click on connect?

Thanks


## rserranon | 2017-05-10T19:44:54+00:00
I have the same problem:

Using Mac OsX 10.11.6 El capitan

2017-05-10 14:42:18.056		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1306507/1307279 (99.9%) on mainnet, not mining, net hash 62.50 MH/s, v5, up to date, 3(out)+0(in) connections, uptime 0d 0h 0m 22s

## inbeacon | 2017-08-12T20:36:49+00:00
same here. Daemon does not start on macos 10.12.5

2017-08-12 22:36:06.964		ERROR	msgwriter	src/common/scoped_message_writer.h:94	Error: Couldn't connect to daemon
2017-08-12 22:36:08.980		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO


## justin8 | 2017-08-29T07:06:06+00:00
I also have the same problem here on 10.12.5

## mqklin | 2017-09-23T06:26:23+00:00
+1

## dEBRUYNE-1 | 2017-12-13T11:11:15+00:00
If the issue is strictly related to the daemon, please open an issue on monero-project/monero. 

+resolved

# Action History
- Created by: srsandocan | 2017-03-30T12:19:46+00:00
- Closed at: 2017-12-13T12:36:15+00:00
