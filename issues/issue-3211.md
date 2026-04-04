---
title: Error writing wallet from hardware device
source_url: https://github.com/monero-project/monero-gui/issues/3211
author: IndustrialOne
assignees: []
labels: []
created_at: '2020-11-04T16:24:43+00:00'
updated_at: '2021-01-15T11:30:03+00:00'
type: issue
status: closed
closed_at: '2021-01-15T11:30:03+00:00'
---

# Original Description
I have set up my trezor wallet a while ago for BTC but now I want to create a monero account there as well but the first step is failing on monero GUI. The log shows the following errors:

2020-11-04 16:19:43.186	6400	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-11-04 16:19:49.922	6400	WARNING	frontend	src/wallet/api/wallet.cpp:412	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2020-11-04 16:19:49.923	8812	ERROR	device.trezor.transport	src/device_trezor/trezor/transport.cpp:1168	BridgeTransport enumeration failed:Bridge enumeration failed
2020-11-04 16:19:50.078	8812	ERROR	device.trezor	src/device_trezor/device_trezor.cpp:174	Get public address exception: Trezor returned failure: code=1, message=Unknown message
2020-11-04 16:19:50.078	8812	ERROR	account	src/cryptonote_basic/account.cpp:220	Cannot get a device address

What am I doing wrong?

Thanks.

# Discussion History
## dEBRUYNE-1 | 2020-11-04T19:10:55+00:00
Is your Trezor firmware updated to the latest version? Also, which specific GUI version are you using? 

## IndustrialOne | 2020-11-05T14:56:13+00:00
I updated my firmware, yes. My monero-gui is version 0.17.1.1-33afd0b (Qt 5.9.9) 64-bit.

________________________________
From: dEBRUYNE-1 <notifications@github.com>
Sent: Wednesday, November 4, 2020 12:11 PM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Error writing wallet from hardware device (#3211)


Is your Trezor firmware updated to the latest version? Also, which specific GUI version are you using?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3211#issuecomment-721920217>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4TE5533TOHOKEOII7TSOGRM3ANCNFSM4TKIHCMA>.


## dEBRUYNE-1 | 2020-11-08T11:29:48+00:00
Can you list the specific version # of the Trezor firmware? 

## IndustrialOne | 2020-11-08T12:36:11+00:00
Wtf, it says 1.9.3 on my wallet settings. I could've sworn I updated it just days ago. Is there a more direct way to find out what my firmware version is?

________________________________
From: dEBRUYNE-1 <notifications@github.com>
Sent: Sunday, November 8, 2020 4:29 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Error writing wallet from hardware device (#3211)


Can you list the specific version # of the Trezor firmware?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3211#issuecomment-723564312>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4WVHBFE73VKOMNYML3SOZ6LPANCNFSM4TKIHCMA>.


## IndustrialOne | 2020-11-08T12:49:09+00:00
Sorry, 1.9.3 is the latest for my model, I got it mixed up with the Trezor T.
Definitely 1.9.3.

________________________________
From: dEBRUYNE-1 <notifications@github.com>
Sent: Sunday, November 8, 2020 4:29 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Error writing wallet from hardware device (#3211)


Can you list the specific version # of the Trezor firmware?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3211#issuecomment-723564312>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4WVHBFE73VKOMNYML3SOZ6LPANCNFSM4TKIHCMA>.


## selsta | 2020-11-08T15:50:15+00:00
Trezor only has Monero support with Trezor Model T. Latest firmware for Model T is 2.3.4

## IndustrialOne | 2020-11-08T17:06:39+00:00
Well that sucks balls! But I can still run a full monero mode on my own PC, right?

________________________________
From: selsta <notifications@github.com>
Sent: Sunday, November 8, 2020 8:50 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Error writing wallet from hardware device (#3211)


Trezor only has Monero support with Trezor Model T. Latest firmware for Model T is 2.3.4

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3211#issuecomment-723596015>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4TQDXC5KJZAFPW4T53SO244FANCNFSM4TKIHCMA>.


## selsta | 2020-11-08T17:09:01+00:00
Correct.

# Action History
- Created by: IndustrialOne | 2020-11-04T16:24:43+00:00
- Closed at: 2021-01-15T11:30:03+00:00
