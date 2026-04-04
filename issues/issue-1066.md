---
title: GUI doesn't fit on a 10" screen
source_url: https://github.com/monero-project/monero-gui/issues/1066
author: ordtrogen
assignees: []
labels:
- bug
- enhancement
- resolved
created_at: '2018-01-07T09:17:37+00:00'
updated_at: '2018-12-17T11:45:31+00:00'
type: issue
status: closed
closed_at: '2018-12-17T11:45:31+00:00'
---

# Original Description
System:

OS: Manjaro Linux i686
Model: Compaq Mini 110c-1000 03A81000000000001000
Kernel: 4.9.74-2-MANJARO
Packages: 976
Shell: bash 4.4.12
CPU: Intel Atom N270 (2) @ 1.600GHz
GPU: Intel Integrated Graphics
GPU: Intel Integrated Graphics
Memory: 298MiB / 995MiB

10 inch screen

GUI installed from https://aur.archlinux.org/monero-wallet-qt.git

See attached screen shot. Stuff below "Privacy level (ringsize 5)" etc doesn't fit. However the font size is generously large and there's plenty of unused screen estate.

There is no visual clue, like a scroll bar, that indicates that you can bring the off-screen parts into view, although I did discover after a while that you can mouse wheel to scroll. 

I still think prio would be to display scroll bars, which are the basic UI element for scrolling, and then allow mouse wheeling as a shortcut to using the scroll bars.

I'm not familiar with the QML format we use for the GUI but it looks html/css/js - esque so would it be difficult to have some settings to allow changing font size for example?

![screen](https://user-images.githubusercontent.com/15184875/34648115-f59acb88-f393-11e7-9fc9-050c5f075cb4.png)


# Discussion History
## sanderfoobar | 2018-01-07T20:13:25+00:00
Will be fixed in #952

## sanderfoobar | 2018-03-28T23:47:53+00:00
New GUI version is releasing soon, could you post here after you've tried it?

Must note that this new version does not have any redesigned wizards, so some components there might still 'fall off the screen'. This is being worked on.

self-note: env var `QT_SCALE_FACTOR`

## sanderfoobar | 2018-03-30T01:25:30+00:00
+enhancement

## sanderfoobar | 2018-03-30T01:27:25+00:00
+bug

## sanderfoobar | 2018-03-30T01:43:18+00:00
Also related to #754 #623

## ordtrogen | 2018-03-30T12:11:00+00:00
I'm having trouble building the GUI on the machine where this bug manifests. 
(Arch linux, 32-bit)
I have cloned the latest master

This might not be the place to report a build problem, but looks like a problem linking:

/home/mini-me/Dokument/github/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.o): I funktionen ”hw::ledger::device_ledger::init()”:
device_ledger.cpp:(.text+0x5b97): odefinierad referens till ”SCardEstablishContext”
device_ledger.cpp:(.text+0x5c84): odefinierad referens till ”pcsc_stringify_error”
device_ledger.cpp:(.text+0x5d4d): odefinierad referens till ”pcsc_stringify_error”
/home/mini-me/Dokument/github/monero-gui/monero/lib/libwallet_merged.a(device_ledger.cpp.o): I funktionen ”hw::ledger::device_ledger::connect()”:
device_ledger.cpp:(.text+0x6463): odefinierad referens till ”SCardListReaders”
device_ledger.cpp:(.text+0x65b5): odefinierad referens till ”pcsc_stringify_error”
device_ledger.cpp:(.text+0x6672): odefinierad referens till ”pcsc_stringify_error”
device_ledger.cpp:(.text+0x6bd3): odefinierad referens till ”SCardFreeMemory”
device_ledger.cpp:(.text+0x6c00): odefinierad referens till ”SCardDisconnect”
device_ledger.cpp:(.text+0x702e): odefinierad referens till ”SCardConnect”
device_ledger.cpp:(.text+0x7183): odefinierad referens till ”SCardStatus”
device_ledger.cpp:(.text+0x769a): odefinierad referens till ”SCardFreeMemory”
collect2: fel: ld returnerade avslutningsstatus 1
make: *** [Makefile:399: release/bin/monero-wallet-gui] Fel 1




## ordtrogen | 2018-03-30T12:11:24+00:00
It says "undefined reference" (in Swedish)

## mmbyday | 2018-12-17T08:57:11+00:00
+resolved.
scrollbars were re-introduced.

## erciccione | 2018-12-17T11:15:35+00:00
@ordtrogen please reopen if the issue is not completely resolved 

+resolved

# Action History
- Created by: ordtrogen | 2018-01-07T09:17:37+00:00
- Closed at: 2018-12-17T11:45:31+00:00
