---
title: Failed on QT5.9.1
source_url: https://github.com/monero-project/monero-gui/issues/2114
author: ghost
assignees: []
labels:
- resolved
created_at: '2019-04-25T17:36:48+00:00'
updated_at: '2019-04-27T11:14:40+00:00'
type: issue
status: closed
closed_at: '2019-04-26T13:54:46+00:00'
---

# Original Description
Building on ubuntu with qt5.9.1 gave this error

g++ -fstack-protector -fstack-protector-strong -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-O1 -Wl,-rpath,/opt/Qt5.9.1/5.9.1/gcc_64/lib -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o SubaddressAccountModel.o SubaddressAccount.o zxcvbn.o UnsignedTransaction.o Logger.o MainApp.o DaemonManager.o qrc_translations.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_SubaddressAccountModel.o moc_SubaddressAccount.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o   -L/home/laugh26/Documents/monero-gui-master/monero/lib -lwallet_merged -lepee -lunbound -leasylogging -ldl -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -llmdb -lsodium -lcrypto -lprotobuf -Wl,-Bdynamic -lhidapi-libusb -L/opt/Qt5.9.1/5.9.1/gcc_64/lib -lQt5Quick -lQt5Widgets -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
moc_WalletManager.o: In function `WalletManager::qt_static_metacall(QObject*, QMetaObject::Call, int, void**)':
moc_WalletManager.cpp:(.text+0x392): undefined reference to `WalletManager::onPassphraseEntered(QString const&, bool)'
moc_WalletManager.cpp:(.text+0x84a): undefined reference to `WalletManager::createWalletFromDeviceAsync(QString const&, QString const&, NetworkType::Type, QString const&, unsigned long long, QString const&)'
moc_WalletManager.cpp:(.text+0x890): undefined reference to `WalletManager::createWalletFromDeviceAsync(QString const&, QString const&, NetworkType::Type, QString const&, unsigned long long, QString const&)'
moc_WalletManager.cpp:(.text+0x901): undefined reference to `WalletManager::createWalletFromDeviceAsync(QString const&, QString const&, NetworkType::Type, QString const&, unsigned long long, QString const&)'
moc_WalletManager.cpp:(.text+0x10c5): undefined reference to `WalletManager::onWalletPassphraseNeeded(Monero::Wallet*)'
moc_WalletManager.cpp:(.text+0x10da): undefined reference to `WalletManager::onPassphraseEntered(QString const&, bool)'
collect2: error: ld returned 1 exit status
Makefile:405: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1


# Discussion History
## selsta | 2019-04-25T17:37:39+00:00
`rm -r build monero` to clean your build directory and then try again.

## sanderfoobar | 2019-04-25T18:22:48+00:00
Beware 5.9.7 is latest point release of 5.9. That said, selsta's reply should work.

## ghost | 2019-04-25T19:06:38+00:00
same error, it did not work. i feel QT5.9.1 cannot build it without error

## selsta | 2019-04-25T19:14:00+00:00
Your error isn’t Qt related. You have an outdated version of the monero source. Maybe try with a fresh repo clone.

## ghost | 2019-04-25T20:46:27+00:00
master branch is outdated? Just try it with QT5.9.1 and see

## selsta | 2019-04-25T20:48:01+00:00
Did you try with a fresh repo clone?

## ghost | 2019-04-25T21:57:34+00:00
> Did you try with a fresh repo clone?

am starting all over, i normally never experience error building qt wallet i updated my qt to 5.9.1. 

## sanderfoobar | 2019-04-26T13:46:11+00:00
+resolved

## ghost | 2019-04-27T11:14:40+00:00
ok i see my faults, i just git clone, such and every one without git clone -recursive. so sorry

# Action History
- Created by: ghost | 2019-04-25T17:36:48+00:00
- Closed at: 2019-04-26T13:54:46+00:00
