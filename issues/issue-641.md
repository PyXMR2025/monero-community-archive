---
title: Launching Monero GUI on Linux and Wallet Hangs on Black Screen
source_url: https://github.com/monero-project/monero-gui/issues/641
author: guini-monero
assignees: []
labels:
- resolved
created_at: '2017-03-29T22:22:39+00:00'
updated_at: '2017-08-07T17:20:07+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:20:07+00:00'
---

# Original Description
So I am using Fedora 25, and when I run "./monero-wallet-gui," it does not respond and I'm left to force quit the process.

# Discussion History
## guini-monero | 2017-03-29T22:30:57+00:00
This is the "monero-wallet-gui.log":
```
2017-03-29 17:29:23.232	    7f1112673740	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-03-29 17:29:24.147	    7f1112673740	INFO 	global	contrib/epee/src/mlog.cpp:153	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
```

## guini-monero | 2017-03-29T22:55:56+00:00
This is also on the 64-bit version.

## swalecko | 2017-03-30T07:08:41+00:00
Same here on Win10 64 bit, Intel Core i5-5200U CPU @ 2.20GHz , Intel HD Graphics 5500, Display solution 1920 x 1080 Full HD 

Edit: Strange, yesterday I tried to open the GUI at least 10 times and got this error. Today after I connected my X250 Lenovo to the docking station where 2 extern Displays are connected, it works directly. I disconnected my laptop from the docking station and tried again, and it works again..

Edit: When I came home today and opened my laptop and woke up from the sleeping mode the same behavior occurs again, the GUI starts only with a black screen

## medusadigital | 2017-03-30T17:05:13+00:00
hei @guini-monero , did you try this allready ? https://monero.stackexchange.com/questions/2928/how-to-change-the-monero-wallet-gui-rendering-mode-for-older-computers/2929#2929

## medusadigital | 2017-03-30T17:06:16+00:00
set QMLSCENE_DEVICE=softwarecontext && ./monero-wallet-gui

## mariodian | 2017-05-09T12:17:01+00:00
The same happens occasionally on MacBook Pro 2016 13" with the latest OSX Sierra 10.12.4. I have to quit the process and restart several times before it works normally.

## tschauner-s | 2017-05-25T22:09:51+00:00
Same here on Windows 8.1 and 10, 64 bit.

## mariodian | 2017-05-26T04:21:48+00:00
After a bit of investigation I found that if I start monerod from the console first, wait ~10 seconds and then open the GUI, everything works normally.

## muusbolla | 2017-06-08T18:38:03+00:00
On Win7 64bit I randomly had this problem (black screen on starting GUI). Starting monerod first did not work. Running with start-low-graphics-mode.bat did not work. As usual, rebooting the PC was the fix... typical Windows.

## medusadigital | 2017-08-07T17:16:05+00:00
probably this was the issue: https://github.com/monero-project/monero-core/pull/777

i therefore consider this as resloved until further notice.

+resolved

# Action History
- Created by: guini-monero | 2017-03-29T22:22:39+00:00
- Closed at: 2017-08-07T17:20:07+00:00
