---
title: 'collect2.exe error: ld returned 1 exit status'
source_url: https://github.com/monero-project/monero-gui/issues/1474
author: ghost
assignees: []
labels:
- resolved
created_at: '2018-06-21T14:44:20+00:00'
updated_at: '2018-07-04T08:54:29+00:00'
type: issue
status: closed
closed_at: '2018-07-04T08:54:29+00:00'
---

# Original Description
Hello,

I am trying to compile the GUI Wallet and i'm presented with the following error 

`g++ -c -pipe -fno-keep-inline-dllexport -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -frtti -Wall -Wextra -fexceptions -mthreads -DUNICODE -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN -I../../monero-gui -I. -IC:/msys64/home/Miner/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -IC:/Qt/5.7/mingw53_32/include -IC:/Qt/5.7/mingw53_32/include/QtQuick -IC:/Qt/5.7/mingw53_32/include/QtWidgets -IC:/Qt/5.7/mingw53_32/include/QtGui -IC:/Qt/5.7/mingw53_32/include/QtANGLE -IC:/Qt/5.7/mingw53_32/include/QtQml -IC:/Qt/5.7/mingw53_32/include/QtNetwork -IC:/Qt/5.7/mingw53_32/include/QtCore -Irelease -IC:/Qt/5.7/mingw53_32/mkspecs/win32-g++  -o release/qrc_qml.o release/qrc_qml.cpp
g++ -fstack-protector -Wl,--stack,4194304 -Wl,--dynamicbase -Wl,--nxcompat -Wl,-s -Wl,-subsystem,windows -mthreads -o release/bin/monero-wallet-gui.exe object_script.monero-wallet-gui.Release  -lmingw32 -LC:/Qt/5.7/mingw53_32/lib C:/Qt/5.7/mingw53_32/lib/libqtmain.a -lshell32 C:/Qt/5.7/mingw53_32/lib/libQt5Core.a -LC:/utils/my_sql/my_sql/lib -LC:/utils/postgresql/pgsql/lib -LC:/msys64/home/Miner/monero-gui/monero/lib -lwallet_merged -llmdb -lepee -lunbound -leasylogging -Lc:/msys64/mingw32/lib -L/mingw32/lib -Lc:/msys64/mingw32/boost/lib -L/mingw32/boost/lib -Wl,-Bstatic -lboost_serialization-mt -lboost_thread-mt -lboost_system-mt -lboost_date_time-mt -lboost_filesystem-mt -lboost_regex-mt -lboost_chrono-mt -lboost_program_options-mt -lboost_locale-mt -licuio -licuin -licuuc -licudt -licutu -liconv -lssl -lcrypto -Wl,-Bdynamic -lws2_32 -lwsock32 -lIphlpapi -lgdi32 C:/Qt/5.7/mingw53_32/lib/libQt5Quick.a C:/Qt/5.7/mingw53_32/lib/libQt5Widgets.a C:/Qt/5.7/mingw53_32/lib/libQt5Gui.a C:/Qt/5.7/mingw53_32/lib/libQt5Qml.a C:/Qt/5.7/mingw53_32/lib/libQt5Network.a C:/Qt/5.7/mingw53_32/lib/libQt5Core.a release/monero-wallet-gui_resource_res.o
./release/filter.o: file not recognized: File format not recognized
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:209: release/bin/monero-wallet-gui.exe] Error 1
make[1]: Leaving directory '/home/Miner/monero-gui/build'
make: *** [Makefile:34: release] Error 2
`

# Discussion History
## pazos | 2018-06-21T16:40:13+00:00
Sorry, not a Windows boy here. Assuming that you can replicate that error following the instructions to build the gui I would look at it. Are you building for 64 bits?, why are you using a binary release of qt targeting 32 bits binaries instead of qt provided by msys64?

## dEBRUYNE-1 | 2018-07-04T08:47:41+00:00
Given the inactivity of this issue, I am going to close it. 

## dEBRUYNE-1 | 2018-07-04T08:47:45+00:00
+resolved

# Action History
- Created by: ghost | 2018-06-21T14:44:20+00:00
- Closed at: 2018-07-04T08:54:29+00:00
