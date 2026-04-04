---
title: Static builds fail on Ubuntu 18.04 x64
source_url: https://github.com/monero-project/monero-gui/issues/2697
author: Snipa22
assignees: []
labels:
- resolved
created_at: '2020-01-05T12:25:16+00:00'
updated_at: '2020-06-27T20:37:38+00:00'
type: issue
status: closed
closed_at: '2020-02-13T11:54:49+00:00'
---

# Original Description
Version: v0.15.0.3
Environment; Ubuntu 18.04.3 x64 (WSL 2 VM)

Steps to reproduce:  Follow the install guide on a clean Ubuntu 18.04.3 x64 setup

The core of this issue appears to be due to libudev not having a static library available (Ref: https://packages.ubuntu.com/bionic/amd64/libudev-dev/filelist ) due to the upstream (Systemd) being unwilling to provide a static library for such. (Ref: https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1358372 / https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=915566 )


```
/home/snipa/Qt5.9.7/5.9.7/gcc_64/bin/rcc -name translations translations/translations.qrc -o qrc_translations.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_SVG_LIB -DQT_WIDGETS_LIB -DQT_QUICK_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I../monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/libusb-1.0 -isystem /usr/include/hidapi -I../../../Qt5.9.7/5.9.7/gcc_64/include -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtSvg -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtWidgets -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtGui/5.9.7 -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtGui/5.9.7/QtGui -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtQuick -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtGui -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtQml -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtNetwork -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtCore/5.9.7 -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtCore/5.9.7/QtCore -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtCore -I. -isystem /usr/include/libdrm -I../../../Qt5.9.7/5.9.7/gcc_64/mkspecs/linux-g++ -o qrc_translations.o qrc_translations.cpp
/home/snipa/Qt5.9.7/5.9.7/gcc_64/bin/rcc -name qml ../qml.qrc -o qrc_qml.cpp
g++ -c -pipe -fPIC -fstack-protector -fstack-protector-strong -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_SVG_LIB -DQT_WIDGETS_LIB -DQT_QUICK_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I../monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/libusb-1.0 -isystem /usr/include/hidapi -I../../../Qt5.9.7/5.9.7/gcc_64/include -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtSvg -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtWidgets -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtGui/5.9.7 -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtGui/5.9.7/QtGui -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtQuick -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtGui -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtQml -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtNetwork -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtCore/5.9.7 -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtCore/5.9.7/QtCore -I../../../Qt5.9.7/5.9.7/gcc_64/include/QtCore -I. -isystem /usr/include/libdrm -I../../../Qt5.9.7/5.9.7/gcc_64/mkspecs/linux-g++ -o qrc_qml.o qrc_qml.cpp
g++ -fstack-protector -fstack-protector-strong -static-libgcc -static-libstdc++ -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-O1 -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o SubaddressAccountModel.o SubaddressAccount.o zxcvbn.o UnsignedTransaction.o Logger.o MainApp.o FutureScheduler.o ipc.o KeysFiles.o utils.o prices.o MoneroSettings.o TailsOS.o DaemonManager.o qrc_translations.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_SubaddressAccountModel.o moc_SubaddressAccount.o moc_UnsignedTransaction.o moc_MainApp.o moc_FutureScheduler.o moc_ipc.o moc_KeysFiles.o moc_prices.o moc_MoneroSettings.o moc_DaemonManager.o   -L/usr/local/ssl/lib -L/home/snipa/projects/monero-gui/monero/lib -lwallet_merged -lepee -leasylogging -lrandomx -Wl,-Bstatic -lunbound -lhidapi-hidraw -ludev -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -llmdb -lsodium -lcrypto -Wl,-Bdynamic -lX11 -lusb-1.0 -lhidapi-libusb -L/home/snipa/Qt5.9.7/5.9.7/gcc_64/lib -lQt5Svg -lQt5Widgets -lQt5Quick -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
/usr/bin/ld: cannot find -ludev
collect2: error: ld returned 1 exit status
Makefile:446: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1
```

I've confirmed libudev is available in my build chain, but there's no .a file available and in ldconfig:
```
ldconfig -p | grep libudev
	libudev.so.1 (libc6,x86-64) => /lib/x86_64-linux-gnu/libudev.so.1
	libudev.so (libc6,x86-64) => /lib/x86_64-linux-gnu/libudev.so
```

# Discussion History
## selsta | 2020-02-13T11:47:46+00:00
I think this has been resolved by compiling static libudev from source?

+resolved

## jeandudey | 2020-06-27T20:37:38+00:00
Same here error here. At least should be pointed on the README.md :wink:

# Action History
- Created by: Snipa22 | 2020-01-05T12:25:16+00:00
- Closed at: 2020-02-13T11:54:49+00:00
