---
title: Monero GUI v0.14.1 fails to launch
source_url: https://github.com/monero-project/monero-gui/issues/2259
author: Hub-O-Gits
assignees: []
labels:
- resolved
created_at: '2019-07-03T20:23:59+00:00'
updated_at: '2019-07-04T21:09:38+00:00'
type: issue
status: closed
closed_at: '2019-07-04T21:09:38+00:00'
---

# Original Description
Notes:
- Windows 7 SP1 x64.
- This is from the zip file, not the installer.
- When the GUI's launched, a process is created momentarily then closes. No GUI appears, and there are no errors.
- I tried the batch script to start it in low graphics mode but that didn't work either.
- (Btw, the download only contains the executables. Is the user supposed to have all of the other files from v0.14.0?)

The following is from the log for the last launch attempt:

> 2019-07-03 20:01:31.001	8376	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-07-03 20:01:31.002	8376	WARNING	frontend	src/wallet/api/wallet.cpp:410	app startd (log: C:/Users/username/AppData/Roaming/monero-wallet-gui/monero-wallet-gui.log)
2019-07-03 20:01:31.003	8376	WARNING	frontend	src/wallet/api/wallet.cpp:410	Qt:5.9.7 GUI:v0.14.1.0 | screen: 1366x768 - dpi: 96 - ratio:0.562369
2019-07-03 20:01:31.710	5336	WARNING	frontend	src/wallet/api/wallet.cpp:410	qmlRegisterType requires absolute URLs.
< several lines of the same entry above >
2019-07-03 20:01:31.801	8376	WARNING	frontend	src/wallet/api/wallet.cpp:410	QQmlApplicationEngine failed to load component
2019-07-03 20:01:31.801	8376	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///main.qml:1398 Type StandardDialog unavailable
qrc:///components/StandardDialog.qml:30 module "QtQuick.Controls" version 2.0 is not installed
2019-07-03 20:01:31.801	8376	ERROR	frontend	src/wallet/api/wallet.cpp:414	Error: no root objects

# Discussion History
## dEBRUYNE-1 | 2019-07-03T20:59:36+00:00
Do you run active AV (AntiVirus) software? If so, certain necessary files may have been quarantined. I'd advise to apply this guide (which implies re-extracting the `.zip` file) and try again thereafter:

https://monero.stackexchange.com/questions/10798/my-antivirus-av-software-blocks-quarantines-the-monero-gui-wallet-is-there

## Hub-O-Gits | 2019-07-03T21:43:36+00:00
There's no AV software installed. And the built-in Windows Defender app is disabled.

In case it's relevant, I should clarify that I'm using the stand-alone/portable install. And that I updated my v0.14.0 installation by copying the contents of the v0.14.1 zip to the existing client directory, which retains all of the libraries/etc from v0.14.0. (And as I asked above: why are there no libraries/etc in the v0.14.1 zip?)

Also, what about these excerpts from the log in my initial post:

"qmlRegisterType requires absolute URLs."
"QQmlApplicationEngine failed to load component"
"qrc:///main.qml:1398 Type StandardDialog unavailable"
"qrc:///components/StandardDialog.qml:30 module "QtQuick.Controls" version 2.0 is not installed"
"Error: no root objects"

## dEBRUYNE-1 | 2019-07-03T22:44:50+00:00
>And that I updated my v0.14.0 installation by copying the contents of the v0.14.1 zip to the existing client directory, which retains all of the libraries/etc from v0.14.0.

This may be an issue. Can you perhaps re-extract the v0.14.1.0 `.zip` file to a fresh directory. 

## xiphon | 2019-07-04T09:22:58+00:00
> the download only contains the executables

That's okay. v0.14.1 is the first release coming with statically linked Monero GUI binary.

> Is the user supposed to have all of the other files from v0.14.0

No

## Hub-O-Gits | 2019-07-04T19:08:23+00:00
Statically linked. Ugh. I totally spaced on that, should have known better.
So yeah that worked: removing all of the old v0.14.0 files. For some reason I assumed I was supposed to update the existing installation with the new exe's.
I also assumed the v0.14.1 exe would just ignore the old libraries if it didn't need them.

## dEBRUYNE-1 | 2019-07-04T21:00:44+00:00
Good to hear! Going to mark this as resolved then. 

## dEBRUYNE-1 | 2019-07-04T21:00:49+00:00
+resolved

# Action History
- Created by: Hub-O-Gits | 2019-07-03T20:23:59+00:00
- Closed at: 2019-07-04T21:09:38+00:00
