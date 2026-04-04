---
title: '[Debian Buster]: (v0.17.2.1) Successful build yet ''QtQml.Models is not installed''
  error'
source_url: https://github.com/monero-project/monero-gui/issues/3440
author: possientis
assignees: []
labels: []
created_at: '2021-04-25T12:12:11+00:00'
updated_at: '2021-04-26T14:54:50+00:00'
type: issue
status: closed
closed_at: '2021-04-26T14:54:50+00:00'
---

# Original Description
I am attempting to build `monero-wallet-gui` on Debian Buster. I believe I have successfully installed all required dependencies as per the `README` and the build appears to be successful. Yet when I launch the wallet I am getting the error

```
2021-04-25 11:52:22.015	W Qt:5.11.3 GUI:0.17.2.1-8444a956 | screen: 1600x900 - dpi: 96 - ratio:0.842986
2021-04-25 11:52:22.289	W QQmlApplicationEngine failed to load component
2021-04-25 11:52:22.289	W qrc:/main.qml:29 module "QtQml.Models" version 2.12 is not installed
2021-04-25 11:52:22.289	E Error: no root objects
```
I thought maybe I had failed to install the package `qml-module-qtqml-models2` but this isn't the case.

It is possible this is my fault and I have done something wrong somewhere, but reporting the issue just in case someone else sees it. I am surprised the build should succeed if a dependency has not been properly installed. 



 

# Discussion History
## selsta | 2021-04-25T21:08:20+00:00
@possientis try to build latest master

## possientis | 2021-04-26T05:45:59+00:00
@selsta ack, will revert asap
**Edit:**
This is an incremental build of latest `master`. Will try a clean build and revert if any different.
```
john@front:~/Libs/monero-gui/build/bin$ ./monero-wallet-gui 
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
2021-04-26 05:59:26.482	W Qt:5.11.3 GUI:0.17.2.1-8444a956 | screen: 1600x900 - dpi: 96 - ratio:0.842986
2021-04-26 05:59:26.762	W QQmlApplicationEngine failed to load component
2021-04-26 05:59:26.762	W qrc:/main.qml:29 module "QtQml.Models" version 2.12 is not installed
2021-04-26 05:59:26.762	E Error: no root objects
```

**Edit:**
Sorry I was running the wrong executable before (as the path indicates). After a clean build of `Master` i get:
```
john@front:~/Libs/monero-gui/build/release/bin$ ./monero-wallet-gui 
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
2021-04-26 09:06:33.235	W Qt:5.11.3 GUI:0.17.2.1-40-gd2fc4e60 | screen: 1600x900 - available: QSize(1600, 873) - dpi: 96 - ratio:0.842986
2021-04-26 09:06:35.750	W QQmlApplicationEngine failed to load component
2021-04-26 09:06:35.750	W qrc:/main.qml:2369 Type MoneroComponents.MenuBar unavailable
2021-04-26 09:06:35.750	W qrc:/components/MenuBar.qml:29 module "Qt.labs.platform" is not installed
2021-04-26 09:06:35.750	E Error: no root objects
```
Interestingly, this is complaining about something else now : )

## xiphon | 2021-04-26T10:01:39+00:00
https://github.com/monero-project/monero-gui#on-linux

## possientis | 2021-04-26T10:33:35+00:00
@xiphon Thank you, are you suggesting that I probably failed to follow these guidelines and should read the document again and retry?

## xiphon | 2021-04-26T11:31:04+00:00
Yeah, did you install `qml-module-qt-labs-platform` dependency?

## possientis | 2021-04-26T11:59:33+00:00
@xiphon I am very sorry, you are right, for some reason I had failed to install that dependency. All good now. My sincere apologies and thank you ! I leave it to you guys to close ticket. 

## possientis | 2021-04-26T13:33:22+00:00
For the avoidance of doubt, the master branch is fine after installing missing dependency `qml-module-qt-labs-platform`, but `v0.17.2.1` still has the same failure as initially reported.

## xiphon | 2021-04-26T14:54:50+00:00
Already fixed via https://github.com/monero-project/monero-gui/pull/3392, the fix will get included in the next release.

# Action History
- Created by: possientis | 2021-04-25T12:12:11+00:00
- Closed at: 2021-04-26T14:54:50+00:00
