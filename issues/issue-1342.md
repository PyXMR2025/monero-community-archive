---
title: GUI Wallet not connecting to Daemon
source_url: https://github.com/monero-project/monero-gui/issues/1342
author: Orsontrius
assignees: []
labels: []
created_at: '2018-04-21T23:35:53+00:00'
updated_at: '2018-04-24T01:40:47+00:00'
type: issue
status: closed
closed_at: '2018-04-24T01:40:47+00:00'
---

# Original Description
Im using v.12 on Windows 10
When the wallet tries to sync the local node,  I get this error:

Please check your wallet and daemon log for errors. You can also try to start monerod.exe manually

So I went to check monero-wallet-gui.log and got this:

2018-04-21 23:18:13.582	8640	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-21 23:18:14.060	8640	WARN 	net.http	src/common/util.cpp:627	Failed to determine whether address '' is local, assuming not
2018-04-21 23:18:15.314	13968	WARN 	net.dns	src/common/dns_utils.cpp:508	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-04-21 23:18:24.347	8640	INFO 	logging	contrib/epee/src/mlog.cpp:185	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2018-04-21 23:18:25.450	13968	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:3718	Loaded wallet keys file, with public address: 45by4WVxrdV1fnAj5jRhg2Y4i2fvtJEyxg1vvzLDijA24J9ixHPpsqz1qAriuv7mLMin3Aod1ZQoeMybqNMvUgfwSb9b9AG

Ive been unsuccesful at fixing the problem myself and help would be greatly appreciated.

# Discussion History
## dEBRUYNE-1 | 2018-04-22T08:16:14+00:00
Have you tried this guide? 

https://monero.stackexchange.com/questions/6825/i-am-using-the-gui-and-my-daemon-doesnt-start-anymore

## Orsontrius | 2018-04-24T01:40:47+00:00
That guide worked, I resynced my blockchain and now it is back to normal, thanks.

# Action History
- Created by: Orsontrius | 2018-04-21T23:35:53+00:00
- Closed at: 2018-04-24T01:40:47+00:00
