---
title: Windows compiling error
source_url: https://github.com/monero-project/monero-gui/issues/15
author: jwinterm
assignees: []
labels: []
created_at: '2016-09-05T18:19:08+00:00'
updated_at: '2016-11-01T08:25:20+00:00'
type: issue
status: closed
closed_at: '2016-11-01T08:25:20+00:00'
---

# Original Description
I'm trying to compile in MSYS2 and getting these warnings from qmake:  

```
WARNING: Failure to find: debug/monero-core_res.o
WARNING: Failure to find: release/monero-core_res.o
```

Then this error when I run make:  

```
windres -i monero-core.rc -o debug/monero-core_res.o --include-dir=. -DUNICODE -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN
g++ -c -pipe -fno-keep-inline-dllexport -march=nocona -mtune=core2 -Wa,-mbig-obj -g -std=gnu++0x -frtti -Wall -Wextra -fexceptions -mthreads -DUNICODE -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN -I. -ID:/msys64/home/johno/monero-core/bitmonero/include -Isrc/libwalletqt -I../../../mingw64/include/QtQuick -I../../../mingw64/include/QtWidgets -I../../../mingw64/include/QtGui -I../../../mingw64/include/QtQml -I../../../mingw64/include/QtNetwork -I../../../mingw64/include/QtCore -Idebug -I../../../mingw64/share/qt5/mkspecs/win32-g++  -o debug/main.o main.cpp
In file included from main.cpp:38:0:
src/libwalletqt/WalletManager.h:5:32: fatal error: wallet/wallet2_api.h: No such file or directory
 #include <wallet/wallet2_api.h>
                                ^
compilation terminated.
```


# Discussion History
## jwinterm | 2016-09-05T18:54:12+00:00
If I make a folder in liqwalletqt called wallet, and manually copy wallet2_api.h over from the bitmonero folder, then compilation can make it a bit further, but eventually errors with:  

```
D:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/6.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lwallet_merged
collect2.exe: error: ld returned 1 exit status
```


## radfish | 2016-09-06T03:35:42+00:00
you need to tell the linker where libwallet_merged.a is by passing the path via `-L/path/to/lib/folder`
if libwallet_merged.a wasn't built, then check that your bitmonerod build passed `-DBUILD_GUI_DEPS=ON` to cmake.


## medusadigital | 2016-11-01T06:19:55+00:00
this issue can be closed i assume


# Action History
- Created by: jwinterm | 2016-09-05T18:19:08+00:00
- Closed at: 2016-11-01T08:25:20+00:00
