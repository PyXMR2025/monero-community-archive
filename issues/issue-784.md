---
title: Windows "Program not Responding" after having been running for a while
source_url: https://github.com/monero-project/monero-gui/issues/784
author: aaronjolson
assignees: []
labels: []
created_at: '2017-06-30T04:03:47+00:00'
updated_at: '2017-12-13T14:33:29+00:00'
type: issue
status: closed
closed_at: '2017-12-13T14:33:29+00:00'
---

# Original Description
I have been having an issue running the Monero GUI on my Windows 10 desktop machine. The wallet takes a super long time to get going, but it does eventually start. Once it starts and the GUI has rendered, it works. I have been trying to get the network to sync. It syncs for a while, my computer stays on, (it is set to never go to sleep and never rest the screen) but after running for a while the wallet locks up. I start seeing the loading cursor when hovering over the wallet window.
In my Resource Monitor I see the CPU of that process drop from 50% - 80% to 0 and the status becomes Not responding.
I see a second instance of monero-wallet-gui.exe appear that has a status of suspended.

I've set the log level to 3. Not sure where those logs go, if they are on my system I'd link them here.

 I have been running the same version of the wallet GUI software on a second Windows laptop without seeing this issue. 

It does appear to resolve itself eventually (5 -20minutes) if I select the window (bring it into view) and select the wait for program to respond option.

If I select to show status of the daemon from the GUI I see this in the logs
```
2017-06-29 18:19:49.771	1472	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1257105/1257105 (100.0%) on mainnet, not mining, net hash 54.02 MH/s, v4, up to date, 0(out)+0(in) connections, uptime 0d 0h 3m 1s

2017-06-29 18:34:09.293	1624	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1260105/1343520 (93.8%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 10(out)+0(in) connections, uptime 0d 0h 14m 21s

2017-06-29 18:34:28.742	12144	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1260105/1343520 (93.8%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 10(out)+0(in) connections, uptime 0d 0h 14m 40s

2017-06-29 20:02:15.768	4420	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1277105/1343520 (95.1%) on mainnet, not mining, net hash 63.13 MH/s, v4 (next fork in 16.0 days), up to date, 10(out)+0(in) connections, uptime 0d 1h 42m 27s

2017-06-29 21:52:10.664	7828	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1294816/1343613 (96.4%) on mainnet, not mining, net hash 61.82 MH/s, v5, up to date, 7(out)+0(in) connections, uptime 0d 3h 34m 15s

2017-06-29 23:07:56.558	4640	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1306016/1343647 (97.2%) on mainnet, not mining, net hash 67.08 MH/s, v5, up to date, 8(out)+0(in) connections, uptime 0d 4h 48m 38s
```

# Discussion History
## dEBRUYNE-1 | 2017-12-13T11:15:10+00:00
Are you still incurring this issue?

## aaronjolson | 2017-12-13T14:33:29+00:00
Not for a while, but I haven't had to download the whole chain history in a while either (as I haven't been starting from scratch). This can probably be closed.

# Action History
- Created by: aaronjolson | 2017-06-30T04:03:47+00:00
- Closed at: 2017-12-13T14:33:29+00:00
