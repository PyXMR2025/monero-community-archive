---
title: '/lib/libcrypto.so.7: could not read symbols: Bad value'
source_url: https://github.com/monero-project/monero-gui/issues/902
author: danrmiller
assignees: []
labels:
- resolved
created_at: '2017-10-12T21:23:34+00:00'
updated_at: '2018-11-18T15:45:33+00:00'
type: issue
status: closed
closed_at: '2018-11-18T15:45:33+00:00'
---

# Original Description
https://build.getmonero.org/builders/monero-core-freebsd/builds/706/steps/compile/logs/stdio

```
clang++ -pthread -o release/bin/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o zxcvbn.o UnsignedTransaction.o MainApp.o DaemonManager.o qrc_qml.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o   -L/usr/local/lib -L/usr/home/vagrant/slave/monero-core-freebsd/build/monero/lib -lwallet_merged -lepee -lunbound -leasylogging -lQt5Quick -lQt5Widgets -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGL 

/usr/bin/ld: undefined reference to symbol `SHA256_Init' (try adding -lcrypto)
//lib/libcrypto.so.7: could not read symbols: Bad value
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
```
Several sources on the internet suggest recompiling openssl with -fPIC for the "could not read symbols: Bad value." error.


# Discussion History
## erciccione | 2018-11-18T13:58:27+00:00
@danrmiller should this stay open?

## sanderfoobar | 2018-11-18T15:40:30+00:00
+resolved

# Action History
- Created by: danrmiller | 2017-10-12T21:23:34+00:00
- Closed at: 2018-11-18T15:45:33+00:00
