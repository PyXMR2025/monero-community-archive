---
title: 'MSYS2 build error: "qmlcachegen.exe: Bad address"'
source_url: https://github.com/monero-project/monero-gui/issues/1636
author: Lafudoci
assignees: []
labels:
- resolved
created_at: '2018-10-11T08:42:43+00:00'
updated_at: '2019-08-28T16:33:11+00:00'
type: issue
status: closed
closed_at: '2018-10-13T19:09:21+00:00'
---

# Original Description
Built from last master `6ca3c`.
Win7 x64 MSYS2
QMake version 3.1
Using Qt version 5.11.2 in C:/msys64/mingw64/lib

I found the same issue occured at aeonix#15.
```
/C/msys64/mingw64/bin/qmlcachegen.exe --resource-file-mapping=C:/msys64/home/x99/monero-gui/qml.qrc=C:/msys64/home/x99/monero-gui/build/qml_qmlcache.qrc -o release/qmlcache_loader.cpp ../qml.qrc
make[1]: execvp: /C/msys64/mingw64/bin/qmlcachegen.exe: Bad address
make[1]: *** [Makefile.Release:1029: release/qmlcache_loader.cpp] Error 127
make[1]: Leaving directory '/home/x99/monero-gui/build'
make: *** [Makefile:36: release] Error 2
```
Full log: https://paste.fedoraproject.org/paste/xdqtNp14H~b2oFgYp0m~hw

# Discussion History
## sanderfoobar | 2018-10-13T19:01:39+00:00
Solved on IRC. Best to use 5.11.1. 5.11.2 is known to have problems.

+resolved

## Lafudoci | 2018-10-14T01:49:55+00:00
@skftn Sorry this issue occurred on another machine (Win7). Using qt5.11.1 didn't resolve this. @rbrunner7 and me had no idea about the solution yet. In my case, the only difference from the working one is win7 vs. win10 but still needs more test.

update: reported from IRC it doesn't relate to win7

## Lafudoci | 2018-10-15T02:23:54+00:00
@skftn Could you reopen this? This issue wasn't resolved and also reported in #1559.

## sanderfoobar | 2018-10-15T08:40:43+00:00
+reopen

## HarrisonHesslink | 2018-11-03T11:39:54+00:00
Just run it again and it should work

## wrokvidLiac | 2018-11-06T08:14:53+00:00
i did it and still same error!
even delete some qml_cache files and nothing
strace not working on mingw so i cant understand what is happening!


## stoffu | 2018-12-13T02:26:05+00:00
Resolved in #1796

## Lafudoci | 2018-12-13T03:42:18+00:00
@stoffu #1796 did solve my issue of  `qmlcachegen.exe: Bad address`. Thank you!

## naughtyfox | 2019-08-28T16:33:11+00:00
I still get this error:
```make[1]: execvp: /C/msys64/mingw64/bin/qmlcachegen.exe: Bad address```

when i'm trying to invoke in manually i get another error:
```
$ LANG=C /C/msys64/mingw64/bin/qmlcachegen.exe --resource-file-mapping=C:/exa/monero-gui/qml.qrc=C:/exa/monero-gui/build/qml_qmlcache.qrc -o release/qmlcache_loader.cpp ../qml.qrc
Error generating loader stub: ▒▒▒▒▒▒▒ ▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒ ▒▒▒▒.
```
which means that invocation passes. I think this is the bug in mingw `make` utility

# Action History
- Created by: Lafudoci | 2018-10-11T08:42:43+00:00
- Closed at: 2018-10-13T19:09:21+00:00
