---
title: monerod refusing to start automatically on 0.14.1 GUI
source_url: https://github.com/monero-project/monero-gui/issues/2268
author: allegro101
assignees: []
labels: []
created_at: '2019-07-04T18:51:44+00:00'
updated_at: '2020-01-28T22:53:47+00:00'
type: issue
status: closed
closed_at: '2020-01-28T22:53:47+00:00'
---

# Original Description
Ever since 0.14.0 the daemon refuses to start when I click on monero-wallet-gui. I get an error screen telling me I must start monerod manually, which is what I do. Once monerod syncs I then open the GUI but this same glitch is reproduced in the new 0.14.1 GUI. Running Win 10 Pro. Any ideas why I have this minor glitch? 

# Discussion History
## xiphon | 2019-07-05T21:20:03+00:00
Could you provide a screenshot?

## allegro101 | 2019-07-06T01:32:56+00:00
The last time I got that error screen somehow starting the GUI corrupted my lmdb and I had to sync from scratch so I am not going to risk it. For some reason this time the database did not corrupt. The error message was just a black screen with white print stating the GUI was not able to connect to the daemon, check your logs for errors or you can try starting monerod manually. 

## dEBRUYNE-1 | 2019-07-06T11:36:47+00:00
Are there any errors in the log by the way? 

## allegro101 | 2019-07-06T16:53:44+00:00
Just checked the log no obvious errors. I would have expected to see an error stating could not connect to database but no. 

## dEBRUYNE-1 | 2019-07-06T21:16:59+00:00
Did you check both `monero-wallet-gui.log` and `bitmonero.log`? 

## allegro101 | 2019-07-06T22:09:49+00:00
For monero-wallet-gui.log does this help:
2019-07-04 17:09:18.935	1332	WARNING	frontend	src/wallet/api/wallet.cpp:410	Qt:5.9.7 GUI:v0.14.1.0 | screen: 1600x900 - dpi: 96 - ratio:0.833942
2019-07-04 17:09:31.493	1332	WARNING	util	src/common/util.cpp:891	Failed to determine whether address '' is local, assuming not
2019-07-04 17:09:31.494	1332	WARNING	util	src/common/util.cpp:891	Failed to determine whether address '' is local, assuming not
2019-07-04 17:09:33.971	1332	WARNING	frontend	src/wallet/api/wallet.cpp:410	libpng warning: iCCP: known incorrect sRGB profile
2019-07-04 17:09:35.373	1332	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2019-07-04 17:09:35.378	1332	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Keys.qml:123: TypeError: Cannot read property 'walletCreationHeight' of undefined
2019-07-04 17:09:35.378	1332	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///wizard/WizardCreateWallet1.qml:154: TypeError: Cannot read property 'walletCreationHeight' of undefined
2019-07-04 17:09:50.359	1332	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-07-04 17:47:29.670	5804	ERROR	wallet.mms	src/wallet/message_store.cpp:735	No message store file found: C:/Users/*redacted*/Documents/Monero/wallets/*redacted*/*redacted*.keys.mms

Note as long as I start monerod first and let it sync then open the GUI functions fine. 



## dEBRUYNE-1 | 2019-11-25T08:58:46+00:00
@allegro101 - Are you still seeing this issue with GUI v0.15.0.1? 

## allegro101 | 2019-11-27T04:30:31+00:00
@dEBRUYNE-1 I verified the binaries and installed GUI v0.15.0.1 but have not used yet, will switch over soon and post. I have made it a habit to back up my lmdb folder weekly in case of corruption. I still start monerod first, let it sync then start the GUI. 

## allegro101 | 2019-11-28T22:21:56+00:00
@dEBRUYNE-1sorry no joy problem persists. When I start GUI v.0.15.0.1 I get an error message that "Daemon failed to start. Please check your wallet and daemon log for errors. You can also try to start monerod automatically." Luckily my lmdb was not corrupted though. I had to start monerod first let it sync then start the GU! as before. Not a problem just minor inconvenience. 

## selsta | 2019-11-28T22:23:31+00:00
@allegro101 Can you try restarting your computer and then check if the GUI starts the daemon automatically?

## allegro101 | 2019-11-30T23:56:07+00:00
@selsta restarting made no difference. Since this is not a widely reported problem I am assuming it may be specific to my computer for some reason. 

## allegro101 | 2020-01-28T22:53:47+00:00
Problem was a corrupted OS I believe. Migrating to a new computer solved the problem and GUI v0.15.0.2 working fine now on Windows 10 Pro. Also very fast using a SSD. Thanks for all the suggestions. 

# Action History
- Created by: allegro101 | 2019-07-04T18:51:44+00:00
- Closed at: 2020-01-28T22:53:47+00:00
