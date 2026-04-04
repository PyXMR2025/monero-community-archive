---
title: 'monero gui wallet crashing '
source_url: https://github.com/monero-project/monero-gui/issues/3651
author: sjatkins
assignees: []
labels: []
created_at: '2021-07-31T20:55:58+00:00'
updated_at: '2021-07-31T21:09:07+00:00'
type: issue
status: closed
closed_at: '2021-07-31T21:09:07+00:00'
---

# Original Description
I am on ubuntu 20.10.  Wallet has worked on this system before. monero-gui-wallet version 0.17.2.2.  

./monero-wallet-gui
2021-07-31 20:50:33.683	W Qt:5.15.2 GUI:0.17.2.2-937cb98 | screen: 3440x1440 - available: QSize(3440, 1440) - dpi: 109.393 - ratio:0.854202
2021-07-31 20:50:33.950	W QGLXContext: Failed to create dummy context
2021-07-31 20:50:36.270	W Logging to "/home/samantha/.bitmonero/monero-wallet-gui.log"
2021-07-31 20:50:36.303	W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2021-07-31 20:50:36.318	E Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile) 

I have seen this failure on other versions in the past.  How do I get around this? 

# Discussion History
## selsta | 2021-07-31T20:58:00+00:00
How did you install the GUI?

Can you try to update graphics drivers and restart your system?

## sjatkins | 2021-07-31T20:59:47+00:00
no I cannot update graphics drives as this is my main linux system and I don't want to fool with those and haven't fool with the for some time.  I installed from the standard getmonero.org download.  
from the log mentioned above:

2021-07-31 20:50:36.270	    7f98cf9f7800	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2021-07-31 20:50:36.270	    7f98cf9f7800	WARNING	frontend	src/wallet/api/wallet.cpp:412	Logging to "/home/samantha/.bitmonero/monero-wallet-gui.log"
2021-07-31 20:50:36.303	    7f98cf9f7800	WARNING	frontend	src/wallet/api/wallet.cpp:412	qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:259:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2021-07-31 20:50:36.318	    7f98cf9f7800	ERROR	frontend	src/wallet/api/wallet.cpp:416	Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags<QSurfaceFormat::FormatOption>(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior QSurfaceFormat::DoubleBuffer, swapInterval 1, colorSpace QSurfaceFormat::DefaultColorSpace, profile  QSurfaceFormat::NoProfile) 


## sjatkins | 2021-07-31T21:00:37+00:00
will try a apt update & apt upgrade and a reboot though. 

## sjatkins | 2021-07-31T21:09:06+00:00
OK, nevermind.  System upgrades and reboot fixed it.  

# Action History
- Created by: sjatkins | 2021-07-31T20:55:58+00:00
- Closed at: 2021-07-31T21:09:07+00:00
