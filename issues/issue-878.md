---
title: Black Screen on Startup
source_url: https://github.com/monero-project/monero-gui/issues/878
author: medusadigital
assignees: []
labels:
- bug
- resolved
created_at: '2017-09-17T14:32:14+00:00'
updated_at: '2018-07-17T13:54:30+00:00'
type: issue
status: closed
closed_at: '2018-07-17T13:54:30+00:00'
---

# Original Description
Users are Reporting a new Bug, which looks like a previous one, causing a black screen at Application Startup on Windows.

https://www.reddit.com/r/Monero/comments/6zpves/the_gui_binaries_have_been_finalized/dmxb0ot/

`2017-09-12 22:58:07.972	7996	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-09-12 22:58:09.608	7996	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-09-12 22:58:10.067	7996	INFO 	logging	contrib/epee/src/mlog.cpp:156	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2017-09-12 22:58:10.160	13772	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-09-12 22:58:10.160	13772	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-09-12 22:58:10.160	13772	WARN 	net.http	src/wallet/wallet_errors.h:707	C:/msys64/home/vagrant/slave/monero-core-win64/build/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-09-12 22:58:10.161	13772	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
2017-09-12 22:58:11.680	5244	WARN 	net.dns	src/common/dns_utils.cpp:487	WARNING: no two valid MoneroPulse DNS checkpoint records were received`



Those users have sucessfully been running GUI Beta 2, so the issue has to come from a new Change (maybe related to the DNS fix, which fixed previous black screens in Beta 2)


Issue seems very exotic, only 2 reports on Windows





# Discussion History
## medusadigital | 2017-09-17T14:33:13+00:00
+Bug

## danielponte | 2017-09-22T11:53:56+00:00
I never tried the beta, but on final Im getting a black screen. Anything I can do to help?

## elkhornJAZZ | 2017-10-27T04:31:50+00:00
windows 7 home premium 64bit*
I have issues running the new GUI wallet - monero-gui-0.11.0.0

*********************************************************************************
2017-10-27 04:02:41.512	4704	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
********************************************************************************
I have no problem running - monero-gui-win-x64-v0.10.3.1
low graphics mode doesnt help



## sanderfoobar | 2018-07-17T13:50:25+00:00
Should be fixed in the newer versions. Re-open if problems persists.

+resolved

# Action History
- Created by: medusadigital | 2017-09-17T14:32:14+00:00
- Closed at: 2018-07-17T13:54:30+00:00
