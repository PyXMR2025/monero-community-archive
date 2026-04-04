---
title: Mingw64 Compile Error
source_url: https://github.com/monero-project/monero-gui/issues/1304
author: italocoin-project
assignees: []
labels:
- resolved
created_at: '2018-04-10T17:52:59+00:00'
updated_at: '2018-04-12T19:36:23+00:00'
type: issue
status: closed
closed_at: '2018-04-12T19:36:23+00:00'
---

# Original Description
I have compiled boost from source and i can find the libs in lib library but it says it can't find here is the error 
Monero GUI version 12.0
Boost boost_1_63_0
Mingw64

```
g++ -c -fno-keep-inline-dllexport -march=nocona -mtune=core2 -Wa,-mbig-obj -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -Wall -W -Wextra -fexceptions -mthreads -DUNICODE -D_UNICODE -DWIN32 -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN -I../../monero-core -I. -I../monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -I../../../../mingw64/include/QtQuick -I../../../../mingw64/include/QtWidgets -I../../../../mingw64/include/QtGui -I../../../../mingw64/include/QtQml -I../../../../mingw64/include/QtNetwork -I../../../../mingw64/include/QtCore -Irelease -I../../../../mingw64/include -I../../../../mingw64/share/qt5/mkspecs/win32-g++  -o release/moc_DaemonManager.o release/moc_DaemonManager.cpp
g++ -fstack-protector -Wl,--stack,4194304 -Wl,--dynamicbase -Wl,--nxcompat -Wl,-s,--relax,--gc-sections -static -Wl,-subsystem,windows -mthreads -o release/bin/monero-wallet-gui.exe object_script.monero-wallet-gui.Release  -lglu32 -lopengl32 -luser32 -lmingw32 -LC:/msys64/mingw64/lib C:/msys64/mingw64/lib/libqtmain.a -lshell32 -LC:/msys64/home/dawn/monero-core/monero/lib -lwallet_merged -llmdb -lepee -lunbound -leasylogging -Lc:/msys64/mingw64/lib -L/mingw64/lib -Lc:/msys64/mingw64/boost/lib -L/mingw64/boost/lib -Wl,-Bstatic -lboost_serialization-mt -lboost_thread-mt -lboost_system-mt -lboost_date_time-mt -lboost_filesystem-mt -lboost_regex-mt -lboost_chrono-mt -lboost_program_options-mt -lboost_locale-mt -licuio -licuin -licuuc -licudt -licutu -liconv -lssl -lcrypto -Wl,-Bdynamic -lws2_32 -lwsock32 -lIphlpapi -lgdi32 C:/msys64/mingw64/lib/libQt5Quick.dll.a C:/msys64/mingw64/lib/libQt5Widgets.dll.a C:/msys64/mingw64/lib/libQt5Gui.dll.a C:/msys64/mingw64/lib/libQt5Qml.dll.a C:/msys64/mingw64/lib/libQt5Network.dll.a C:/msys64/mingw64/lib/libQt5Core.dll.a
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_serialization-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_thread-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_system-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_date_time-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_filesystem-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_regex-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_chrono-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_program_options-mt
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lboost_locale-mt
collect2.exe: error: ld returned 1 exit status
```

Anyone had this problem?

# Discussion History
## pazos | 2018-04-10T18:13:27+00:00
We're using mingw boost instead of building a new one. Try installing mingw-w64-x86_64-boost (if it isn't installed yet) and delete your own compilation. Rebuild monero-gui (to be sure delete monero and build folders b4)

## italocoin-project | 2018-04-10T18:29:35+00:00
@pazos  I'm compiling release-static, it needs boost compiled.

## pazos | 2018-04-10T18:50:14+00:00
In that case you'll need to revert #1205 

## italocoin-project | 2018-04-12T17:57:58+00:00
+resolved

@pazos suggestion solved the problem!

## dEBRUYNE-1 | 2018-04-12T19:35:21+00:00
+resolved

# Action History
- Created by: italocoin-project | 2018-04-10T17:52:59+00:00
- Closed at: 2018-04-12T19:36:23+00:00
