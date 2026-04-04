---
title: Can't build static
source_url: https://github.com/monero-project/monero-gui/issues/2406
author: ohiofun
assignees: []
labels:
- resolved
created_at: '2019-10-03T15:48:34+00:00'
updated_at: '2019-11-11T23:18:38+00:00'
type: issue
status: closed
closed_at: '2019-11-11T23:18:38+00:00'
---

# Original Description
Hi community, I have problem when I build static builds. On linux (Ubuntu 18.04) this is always:
```
g++ -fstack-protector -fstack-protector-strong -static-libgcc -static-libstdc++ -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-O1 -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o SubaddressAccountModel.o SubaddressAccount.o zxcvbn.o UnsignedTransaction.o Logger.o MainApp.o FutureScheduler.o ipc.o KeysFiles.o utils.o prices.o MoneroSettings.o TailsOS.o DaemonManager.o qrc_translations.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_SubaddressAccountModel.o moc_SubaddressAccount.o moc_UnsignedTransaction.o moc_MainApp.o moc_FutureScheduler.o moc_ipc.o moc_KeysFiles.o moc_prices.o moc_MoneroSettings.o moc_DaemonManager.o   -L/usr/local/ssl/lib -L/home/ohiofun/BUILDS/monero-gui/monero/lib -lwallet_merged -lepee -leasylogging -lrandomx -Wl,-Bstatic -lunbound -lhidapi-hidraw -ludev -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -llmdb -lsodium -lcrypto -Wl,-Bdynamic -lX11 -lusb-1.0 -lhidapi-libusb -lprotobuf -pthread -lQt5Svg -lQt5Widgets -lQt5Quick -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
/usr/bin/ld: cannot find -ludev
collect2: error: ld returned 1 exit status
Makefile:346: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1
```
Because linker try to add static `libudev` but libudev is dynamic link.
`monero/contrib/depends/toolchain.cmake.in`, line 33:
`SET(LIBUDEV_LIBRARY @prefix@/lib/libudev.a)`

I already tried to install it with apt-get:
`apt-get -y update && apt-get upgrade -y && apt-get install -y --no-install-recommends curl make cmake file ca-certificates g++ gcc-aarch64-linux-gnu g++-aarch64-linux-gnu libc6-dev-arm64-cross binutils-aarch64-linux-gnu libudev-dev libudev-dev:arm64`
But too no luck.

I build step-by-step:
```
sudo apt install build-essential cmake libboost-all-dev miniupnpc libunbound-dev graphviz doxygen libunwind8-dev pkg-config libssl-dev libzmq3-dev libsodium-dev libhidapi-dev libnorm-dev libusb-1.0-0-dev libpgm-dev
sudo apt install qtbase5-dev qt5-default qtdeclarative5-dev qml-module-qtquick-controls qml-module-qtquick-controls2 qml-module-qtquick-dialogs qml-module-qtquick-xmllistmodel qml-module-qt-labs-settings qml-module-qt-labs-folderlistmodel qttools5-dev-tools qml-module-qtquick-templates2 libqt5svg5-dev
sudo apt install qtmultimedia5-dev qml-module-qtmultimedia libzbar-dev
git clone https://github.com/monero-project/monero-gui.git
cd monero-gui
QT_SELECT=5 ./build.sh release-static
```


On Windows `release\bin\monero-gui.exe` is not a static it have depends with .dll and dirs. After build monero-gui.exe have size only 50 mb, not a 80 mb (monero-gui.exe size in release zip)
Too using step-by-step manual from README. Build have errors like a this: https://github.com/monero-project/monero-gui/issues/2233#issuecomment-506995963 solved by instruction in comment.

Qt Version: Last (5.12)

# Discussion History
## ohiofun | 2019-10-03T16:16:05+00:00
And on linux if I try `QT_SELECT=5 ./build.sh release`:

```
/usr/bin/ld: /home/ohiofun/BUILDS/monero-gui/monero/lib/libusb-1.0.a(libusb_1_0_la-linux_udev.o): undefined reference to external symbol «udev_device_unref@@LIBUDEV_183»
//lib/x86_64-linux-gnu/libudev.so.1: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
Makefile:346: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1
```

## xiphon | 2019-10-04T06:03:31+00:00
You have to use static Qt build

## selsta | 2019-11-11T22:51:50+00:00
Closing due to inactivity.

+resolved

# Action History
- Created by: ohiofun | 2019-10-03T15:48:34+00:00
- Closed at: 2019-11-11T23:18:38+00:00
