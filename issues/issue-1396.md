---
title: 'Daemon Synchronized Block height is not synching '
source_url: https://github.com/monero-project/monero-gui/issues/1396
author: andranikmirzoyan
assignees: []
labels: []
created_at: '2018-05-10T02:47:38+00:00'
updated_at: '2018-05-10T06:24:55+00:00'
type: issue
status: closed
closed_at: '2018-05-10T06:24:55+00:00'
---

# Original Description
OSX HighSierra 10.13.4
GUI version: v0.12.0.0
Embedded Monero version: v0.12.0.0
Status Shows: Height: 1562939/1562939 (100.0%) on mainnet, not mining, net hash 492.54 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 10d 9h 12m 57s


Hi.. After installing and synching the monero-gui-wallet,  the block height got stuck at 1562939 and  didn't continue to synch even though it's connected to the network and the message "Daemon is synchronized (1562939) , Wallet is synchronized is displayed.  The instructions on the following page "https://monero.stackexchange.com/questions/6649/transaction-stuck-as-pending-in-the-gui"  did not help resolve my issue, and the block height on my status window in the wallet is behind by a very large number. Here are some lines from the bitmonero.log file. Also I have downloaded the entire blockchain to a external USB HDD, not sure if this matters in my case. 

2018-05-10 01:45:54.100   0x7fff9c186380        INFO    logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-10 01:45:54.108   0x7fff9c186380        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 1562939/1562939 (100.0%) on mainnet, not mining, net hash 492.54 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 10d 5h 54m 22s
2018-05-10 01:46:42.727   0x7fff9c186380        INFO    logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-10 01:46:42.736   0x7fff9c186380        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 1562939/1562939 (100.0%) on mainnet, not mining, net hash 492.54 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 10d 5h 55m 10s
2018-05-10 01:46:49.689   0x7fff9c186380        INFO    logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-10 01:46:49.696   0x7fff9c186380        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 1562939/1562939 (100.0%) on mainnet, not mining, net hash 492.54 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 10d 5h 55m 17s
2018-05-10 01:48:03.768   0x7fff9c186380        INFO    logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-10 01:48:03.775   0x7fff9c186380        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 1562939/1562939 (100.0%) on mainnet, not mining, net hash 492.54 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 10d 5h 56m 31s
2018-05-10 02:36:44.547   0x7fff9c186380        INFO    logging contrib/epee/src/mlog.cpp:185   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-05-10 02:36:44.556   0x7fff9c186380        INFO    msgwriter       src/common/scoped_message_writer.h:102  Height: 1562939/1562939 (100.0%) on mainnet, not mining, net hash 492.54 MH/s, v7, up to date, 8(out)+0(in) connections, uptime 10d 6h 45m 12s

Thank you in advance.

# Discussion History
## andranikmirzoyan | 2018-05-10T06:24:55+00:00
I connected to a remote node and the wallet synced up... Walla...

# Action History
- Created by: andranikmirzoyan | 2018-05-10T02:47:38+00:00
- Closed at: 2018-05-10T06:24:55+00:00
