---
title: Ubuntu 17.04 build failed - makefile:258
source_url: https://github.com/monero-project/monero-gui/issues/942
author: 1337tester
assignees: []
labels:
- resolved
created_at: '2017-11-07T15:47:09+00:00'
updated_at: '2017-11-26T18:56:59+00:00'
type: issue
status: closed
closed_at: '2017-11-26T18:56:59+00:00'
---

# Original Description
I tried to rebuild my GUI installation with the latest master (a01bb50), it did not succeeded 
[log_build.txt](https://github.com/monero-project/monero-core/files/1450631/log_build.txt)


# Discussion History
## Jaqueeee | 2017-11-07T15:51:38+00:00
https://github.com/monero-project/monero/pull/2764 is needed to build monero API currently.
It will hopefully be merged into master branch in a couple of hours.

## 1337tester | 2017-11-07T15:57:27+00:00
sorry to ask, but how can I do this? Should I clone a specific branch then?

## OlegFisher | 2017-11-07T16:23:05+00:00
The same problem on Ubuntu 16.04 

`    Generated 377 translation(s) (377 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_he.ts -qm /home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_he.qm
Updating '/home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_he.qm'...
Removing translations equal to source text in '/home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_he.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 21 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ko.ts -qm /home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_ko.qm
Updating '/home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_ko.qm'...
    Generated 373 translation(s) (373 finished and 0 unfinished)
    Ignored 3 untranslated source text(s)
/usr/lib/x86_64-linux-gnu/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ro.ts -qm /home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_ro.qm
Updating '/home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/home/oleg/Projects/monero-core/build/release/bin/translations/monero-core_ro.qm'...
    Generated 357 translation(s) (357 finished and 0 unfinished)
/usr/lib/x86_64-linux-gnu/qt5/bin/rcc -name qml ../qml.qrc -o qrc_qml.cpp
g++ -c -m64 -pipe -O2 -std=gnu++0x -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-core -I. -I/home/oleg/Projects/monero-core/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++-64 -o qrc_qml.o qrc_qml.cpp
g++ -m64 -Wl,-O1 -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o zxcvbn.o UnsignedTransaction.o MainApp.o DaemonManager.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o   -L/usr/X11R6/lib64 -L/home/oleg/Projects/monero-core/monero/lib -lwallet_merged -lepee -lunbound -leasylogging -lreadline -ldl -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -lcrypto -Wl,-Bdynamic -lQt5Quick -lQt5Widgets -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
/usr/bin/ld: cannot find -lwallet_merged
/usr/bin/ld: cannot find -lreadline
collect2: error: ld returned 1 exit status
Makefile:255: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1
`

## 1337tester | 2017-11-08T00:32:01+00:00
with the latest master (v0.11.1.0-71-ga01bb50) it works again
for me you can close, @OlegFisher try again please

## 1337tester | 2017-11-22T18:16:05+00:00
Can be closed

## dEBRUYNE-1 | 2017-11-24T15:31:02+00:00
+resolved 

# Action History
- Created by: 1337tester | 2017-11-07T15:47:09+00:00
- Closed at: 2017-11-26T18:56:59+00:00
