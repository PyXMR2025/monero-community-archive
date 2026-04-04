---
title: Aborted (core dumped) as soon as I run monero-wallet-gui built from latest
  commit.
source_url: https://github.com/monero-project/monero-gui/issues/524
author: osensei
assignees: []
labels:
- resolved
created_at: '2017-03-03T02:41:25+00:00'
updated_at: '2017-08-07T17:55:09+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:55:09+00:00'
---

# Original Description
I'm able to build current latest commit (e826f7c) but as soon as I run it I get:

    2017-03-03 02:27:27.597	    7f9936bac900	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
    Aborted (core dumped)

That's with the debug build, if I do a release build then instead of "Aborted" I get "Segmentation fault".

A stack trace in gdb from the dumped core shows this:

    #0  0x00007f9932d35428 in raise () from /lib/x86_64-linux-gnu/libc.so.6
    #1  0x00007f9932d3702a in abort () from /lib/x86_64-linux-gnu/libc.so.6
    #2  0x00007f9933c19f81 in QMessageLogger::fatal(char const*, ...) const () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #3  0x00007f9933c150ee in qt_assert(char const*, char const*, int) () from /usr/lib/x86_64-linux-gnu/libQt5Core.so.5
    #4  0x000000000043b1e9 in QList<QObject*>::first (this=0x7ffdf4252f00) at /usr/include/x86_64-linux-gnu/qt5/QtCore/qlist.h:316
    #5  0x0000000000435e7f in main (argc=1, argv=0x7ffdf4253118) at ../main.cpp:197

In case it matters... I'm building it on Ubuntu 16.04 amd64

# Discussion History
## Jaqueeee | 2017-03-03T08:21:09+00:00
@osensei Which Qt version version do you have? Could you try this build from same commit and see if it runs? Built with Qt 5.7.
https://build.getmonero.org/downloads/monero-core-e826f7c-linux-amd64.tar.gz


## osensei | 2017-03-03T12:03:04+00:00
@Jaqueeee I have Qt 5.5.1. 
I just tried that build you linked and it works fine.

## antanst | 2017-03-04T13:32:19+00:00
I also have the above issue on Debian Testing, Qt 5.7.1, and the above build works.

## moneromooo-monero | 2017-03-18T08:59:24+00:00
That looks light it might be the camera thing, I think I remember a similar crash before due to it.


## MoroccanMalinois | 2017-03-22T23:53:53+00:00
@osensei : Could you please retry  after installing `qml-module-qtmultimedia`

        apt-get install qml-module-qtmultimedia

I can also reproduce with debian testing (fresh install, no vm, no docker). 
@moneromooo-monero : I reverted the commit that adds the "camera thing" ;) , but same crash (whereas it fixed the crash in ubuntu).
It works with downloaded 5.7.1 and with local build 5.7.1 and there is currently no Qt dbg package in debian stretch, so ... dunno. FWIW, I suspect another missing qml package or qt plugin as they are usually the ones that doesn't cause a build error. 


## medusadigital | 2017-04-18T10:01:12+00:00
can this be closed ? 

## MaxXor | 2017-05-18T16:13:00+00:00
@medusadigital No, I'm experiencing the same issue when building from latest commit. Once I try to run `monero-wallet-gui` it crashes with message "Segmentation fault (core dumped)". (Ubuntu 16.04 x86)

## MoroccanMalinois | 2017-05-22T23:22:40+00:00
I can confirm the issue. In the same environnement i have a 2 months old branch that works. imho, i think it's https://github.com/monero-project/monero-core/commit/2e53c524a13c4b4ef3cccfc7c7cfc4243144d6f9 which introduces the usage of QtQuick.Controls 2.0, which is AFAICT not available before Qt 5.7 and ubuntu ships with Qt 5.5.1

## MaxXor | 2017-05-27T11:50:57+00:00
I'm getting the following error when trying to debug the binaries (built in release mode):
> Thread 1 "monero-wallet-g" received signal SIGSEGV, Segmentation fault.
> 0xb635a7cf in QObject::connect(QObject const*, char const*, QObject const*, char const*, Qt::ConnectionType) ()
>   from /usr/lib/i386-linux-gnu/sse2/libQt5Core.so.5

## MaxXor | 2017-07-09T12:52:18+00:00
This has been fixed in one of the latest commits (I'm not sure which one exactly).

## dEBRUYNE-1 | 2017-08-07T17:50:43+00:00
+resolved

# Action History
- Created by: osensei | 2017-03-03T02:41:25+00:00
- Closed at: 2017-08-07T17:55:09+00:00
