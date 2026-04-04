---
title: gui don't start
source_url: https://github.com/monero-project/monero-gui/issues/835
author: Simon0Harms
assignees: []
labels:
- resolved
created_at: '2017-08-24T11:57:25+00:00'
updated_at: '2018-11-18T13:54:29+00:00'
type: issue
status: closed
closed_at: '2018-11-18T13:54:29+00:00'
---

# Original Description
version:
monero-gui-0.10.3.1-beta2 (.deb)

Ubuntu Mate 16.04 64 Bit.

./monero-wallet-gui
High DPI auto scaling - enabled
2017-08-24 13:53:42.086	    7fbd97b20780	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-08-24 13:53:43.053	    7fbd97b20780	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
XIO:  fatal IO error 16 (Das Gerät oder die Ressource ist belegt) on X server ":0.0"
      after 537 requests (537 known processed) with 0 events remaining.
Speicherzugriffsfehler (Speicherabzug geschrieben)


# Discussion History
## Jaqueeee | 2017-08-24T12:49:30+00:00
Ubuntu Mate? What kind of system do you have?
You could try the low graphics mode:
https://monero.stackexchange.com/questions/2928/how-to-change-the-monero-wallet-gui-rendering-mode-for-older-computers

## Simon0Harms | 2017-08-24T13:04:05+00:00
Ryzen5-1600X
ATI Radeon X1600 

Same problem with low graphics mode:
MLSCENE_DEVICE=softwarecontext ./monero-wallet-gui
High DPI auto scaling - enabled
2017-08-24 15:01:40.337	    7fc7e9ab1780	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-08-24 15:01:41.354	    7fc7e9ab1780	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
XIO:  fatal IO error 16 (Das Gerät oder die Ressource ist belegt) on X server ":0.0"
      after 537 requests (537 known processed) with 0 events remaining.
Speicherzugriffsfehler (Speicherabzug geschrieben)



## Jaqueeee | 2017-08-24T14:46:50+00:00
You're missing a Q in QMLSCENE_DEVICE in the paste above. 

## Simon0Harms | 2017-08-24T17:53:00+00:00
Thanks that was a Mistake, but it is very buggy.
If change the window to for example look up my key and change then back i get this view
![bugging](https://user-images.githubusercontent.com/10880193/29680700-ad32ccd6-8905-11e7-9ba2-b18efcf90010.png)
 
I can get the buttons back if i hover over every button with the mouse, but i can not get the whole window refreshed :(

## medusadigital | 2017-09-14T15:05:46+00:00
how is the new version doing for you @Simon0Harms , still same issue ? 

## dEBRUYNE-1 | 2017-10-27T13:49:58+00:00
Can you try v0.11.1.0?

## dkarma | 2017-12-16T20:19:06+00:00
i got the same issue with v.0.11.1.0

2017-12-16 20:17:28.915	    7f13f1e90740	INFO 	logging	contrib/epee/src/mlog.cpp:148	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO

qml: qrScannerEnabled disabled
qrc:///pages/Settings.qml:503: TypeError: Cannot read property 'walletCreationHeight' of undefined
Checking for updates
qrc:///pages/Settings.qml:520: TypeError: Cannot read property 'walletCreationHeight' of undefined
QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled
Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior 2, swapInterval 1, profile  0) 
Aborted (core dumped)

Worked fine until I stepped up to cuda v9.0 
using QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui  seemed to work for me though 
Thanks!

## erciccione | 2018-11-18T13:52:26+00:00
Related to old version

+resolved

# Action History
- Created by: Simon0Harms | 2017-08-24T11:57:25+00:00
- Closed at: 2018-11-18T13:54:29+00:00
