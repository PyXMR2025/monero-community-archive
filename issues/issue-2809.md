---
title: Daemon not stopping as expected on GUI v0.15.0.4
source_url: https://github.com/monero-project/monero-gui/issues/2809
author: allegro101
assignees: []
labels: []
created_at: '2020-03-15T22:43:25+00:00'
updated_at: '2020-05-29T22:13:58+00:00'
type: issue
status: closed
closed_at: '2020-05-29T22:13:58+00:00'
---

# Original Description
I wanted to report unexpected behaviour using the new x64 GUI v0.15.0.4 which was not present on the earlier GUI v0.15.0.2. Running a full local node on Win 10 Pro when the "stop daemon" button is clicked the daemon stops then in a few seconds starts again. The display cycles between connected and disconnected. Luckily when closing the GUI I get a message that the daemon is still running, would I like to shut it down or leave it running in the background. This fail safe keeps from corrupting the database but this behaviour was not present on earlier releases. Thanks for your attention to this matter.

# Discussion History
## xiphon | 2020-03-15T23:31:56+00:00
Could you please provide monerod logs?

## allegro101 | 2020-03-16T01:34:11+00:00
2020-03-15 22:24:19.809	5536	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-03-15 22:24:19.810	5536	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-03-15 22:24:19.810	5536	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-03-15 22:24:20.295	5536	INFO	msgwriter	src/common/scoped_message_writer.h:102	Stop signal sent
2020-03-15 22:24:23.575	15256	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-03-15 22:24:23.576	15256	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-03-15 22:24:23.576	15256	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-03-15 22:24:23.917	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 2055230, target: 2055230 (100%)
2020-03-15 22:24:23.917	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	Downloading at 6 kB/s
2020-03-15 22:24:23.917	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	7 peers
2020-03-15 22:24:23.917	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	82.15.100.93:18080        c89293533b9bc69f  normal            0         2055229  0 kB/s, 0 blocks / 0 MB queued
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	79.165.89.196:18089       802e93db841550a4  normal            0         2055229  2 kB/s, 0 blocks / 0 MB queued
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	62.210.220.22:18080       7edb8feb2b784bab  normal            0         2055229  0 kB/s, 0 blocks / 0 MB queued
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	78.46.244.111:18080       5ca1473ae56c1795  normal            0         2055229  2 kB/s, 0 blocks / 0 MB queued
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	139.162.46.14:51810       027acbf7aed6aecf  normal            0         2055229  2 kB/s, 0 blocks / 0 MB queued
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	67.243.131.94:18080       75d4e6da1ca9d350  normal            0         2055229  0 kB/s, 0 blocks / 0 MB queued
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	109.198.191.22:18080      d511ba3a9f838249  normal            0         2055229  0 kB/s, 0 blocks / 0 MB queued
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	0 spans, 0 MB
2020-03-15 22:24:23.918	15256	INFO	msgwriter	src/common/scoped_message_writer.h:102	[]
2020-03-15 22:24:24.511	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:80	p2p net loop stopped
2020-03-15 22:24:24.586	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:83	Stopping core RPC server...
2020-03-15 22:24:24.588	[SRV_MAIN]	INFO	global	src/daemon/daemon.cpp:216	Node stopped.
2020-03-15 22:24:24.660	[SRV_MAIN]	INFO	global	src/daemon/rpc.h:95	Deinitializing core RPC server...
2020-03-15 22:24:24.663	[SRV_MAIN]	INFO	global	src/daemon/p2p.h:90	Deinitializing p2p...
2020-03-15 22:24:24.677	[SRV_MAIN]	INFO	global	src/daemon/core.h:94	Deinitializing core...
2020-03-15 22:24:24.896	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2020-03-15 22:24:24.896	[SRV_MAIN]	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2020-03-15 22:24:27.201	9232	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-03-15 22:24:27.201	9232	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-03-15 22:24:27.202	9232	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-03-15 22:24:29.332	9232	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2020-03-15 22:25:29.891	13656	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-03-15 22:25:29.892	13656	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-03-15 22:25:29.892	13656	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-03-15 22:25:32.272	13656	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2020-03-15 22:25:35.552	14860	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-03-15 22:25:35.553	14860	INFO	global	src/daemon/main.cpp:271	Monero 'Carbon Chamaeleon' (v0.15.0.1-6def88ad4)
2020-03-15 22:25:35.553	14860	INFO	global	contrib/epee/src/net_ssl.cpp:127	Generating SSL certificate
2020-03-15 22:25:37.679	14860	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081


## xiphon | 2020-03-16T01:55:47+00:00
Looking at the logs, the daemon just stopped once and never started again.

## xiphon | 2020-03-16T02:02:24+00:00
Could you provide more details on what is going wrong and steps to reproduce the issue?

## allegro101 | 2020-03-16T02:32:34+00:00
I normally start the GUI and let it manage the daemon and explained the issue in my original post. There seems to be a bug shutting down the daemon automatically from within the GUI. Now when I start monerod manually, let the blockchain sync, then start the GUI when I click the stop daemon button the command window does show the daemon shutting down properly and I have no messages when I then close the GUI. To avoid chances of corrupting the database I will probably start monerod manually until a new point release comes out. 

## xiphon | 2020-03-16T02:38:17+00:00
> There seems to be a bug shutting down the daemon automatically from within the GUI

Why do you think so? According to the logs, monerod had been stopped successfully.

## allegro101 | 2020-03-16T03:22:04+00:00
Please refer to the OP. As I mentioned when letting the GUI manage the daemon when I try to stop monerod from within the GUI I get a message that it disconnects, than shortly after that it is connecting, then the cycle repeats. When I shut down the GUI I get a warning message that the daemon is still running and would I like to stop it, which I do. This was not a problem with the last point release. Sorry but the logs are not reflecting what I am seeing on the screen (the log was copy/pasted after monerod was stopped and the GUI closed.)

## allegro101 | 2020-03-26T13:52:18+00:00
I have now confirmed this bug by reproducing on a second Windows 10 Pro computer. 

## selsta | 2020-03-27T16:54:28+00:00
Can you post the exact steps to reproduce this? Clicking on Stop daemon on Windows 10 is exactly as expected on my system. Also make sure to only press the stop daemon button once.

## allegro101 | 2020-03-27T18:14:31+00:00
@selsta I thought I already did, just reference my previous posts in this thread. This behaviour was not present in the previous point release. I have duplicated it on two separate Win 10 Pro computers so it would seem to be legitimate. 

## selsta | 2020-03-27T19:26:31+00:00
I can not reproduce the issue with the info you provided. Can you make a screenshot of `Settings -> Node` page and a screenshot of `Settings -> Info` page?

## allegro101 | 2020-03-27T20:42:29+00:00
Sorry no screenshots. Using a local node with default settings in Settings > Node
Settings > Info:

GUI version: v0.15.0.4 (Qt 5.12.2)
Embedded Monero version: v0.15.0.1
Wallet path: C:/Users/(redacted)/Documents/Monero/wallets/xmr/xmr
Wallet creation height: 135000
Wallet log path: C:/Users/(redacted)/AppData/Roaming/monero-wallet-gui/monero-wallet-gui.log
Wallet mode: Advanced modeOpenGL

## allegro101 | 2020-05-29T22:13:58+00:00
This behaviour has been corrected in the new GUI v0.16.0.0. When I shut my local node down I still get the connecting/disconnecting notice cycling at lower left of the GUI screen. However when I exit the wallet the node seems to stop gracefully without a prompt asking me if I want to stop and there is no corruption of the blockchain. I consider this issue fixed, thanks to the developers!

# Action History
- Created by: allegro101 | 2020-03-15T22:43:25+00:00
- Closed at: 2020-05-29T22:13:58+00:00
