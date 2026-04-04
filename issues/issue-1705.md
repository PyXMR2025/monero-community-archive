---
title: Build error - Makefile:278
source_url: https://github.com/monero-project/monero-gui/issues/1705
author: lunarthegrey
assignees: []
labels: []
created_at: '2018-10-27T00:47:03+00:00'
updated_at: '2018-10-28T16:22:33+00:00'
type: issue
status: closed
closed_at: '2018-10-28T16:22:32+00:00'
---

# Original Description
I'm getting this when trying to build the latest release. Any ideas? Did a fresh `git clone https://github.com/monero-project/monero-gui.git` today.

I ran this `QT_SELECT=5 ./build.sh`

```
g++ -m64 -fstack-protector -fstack-protector-strong -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-O1 -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o zxcvbn.o UnsignedTransaction.o Logger.o MainApp.o DaemonManager.o qrc_translations.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o   -L/usr/X11R6/lib64 -L/home/user/Wallets/source/monero-gui/monero/lib -lwallet_merged -lepee -lunbound -leasylogging -ldl -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -llmdb -lsodium -lcrypto -Wl,-Bdynamic -Wl,-Bdynamic -lunwind -lhidapi-libusb -lQt5Quick -lQt5Widgets -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL -lpthread 
/usr/bin/ld: cannot find -lwallet_merged
collect2: error: ld returned 1 exit status
Makefile:278: recipe for target 'release/bin/monero-wallet-gui' failed
make: *** [release/bin/monero-wallet-gui] Error 1
```

# Discussion History
## ascandella | 2018-10-27T05:10:08+00:00
I can't reproduce on master, do you have any more logs? I've had build issues in the past when missing other dependencies (e.g. boost)

For reference, here's what mine looks like when building wallet_merged:

```
Scanning dependencies of target wallet_merged
Scanning dependencies of target wallet
[ 96%] Linking CXX static library ../../lib/libwallet_merged.a
[ 96%] Linking CXX static library ../../lib/libwallet.a
[ 96%] Built target wallet
Scanning dependencies of target wallet_rpc_server
[ 98%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_serv
[ 98%] Built target wallet_merged
[100%] Linking CXX executable ../../bin/monero-wallet-rpc
```

## lunarthegrey | 2018-10-28T16:22:32+00:00
Hmm this may have been memory related. After I increased the memory of my VM from 2GB to 4GB it built just fine. Closing this out.

# Action History
- Created by: lunarthegrey | 2018-10-27T00:47:03+00:00
- Closed at: 2018-10-28T16:22:32+00:00
