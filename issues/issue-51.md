---
title: Build fails with GCC 6.2.1
source_url: https://github.com/monero-project/monero-gui/issues/51
author: anonimal
assignees: []
labels: []
created_at: '2016-10-11T16:06:59+00:00'
updated_at: '2016-10-15T09:46:06+00:00'
type: issue
status: closed
closed_at: '2016-10-15T09:46:06+00:00'
---

# Original Description
Re-opening from [here](https://github.com/mbg033/monero-core/issues/75)
Built against d9b3f4a4fd1f2082b9867a1f22ecb0fe01f04280
Also reproducible [here](https://aur.archlinux.org/packages/monero-core-git/)

```
src/libwalletqt/WalletManager.cpp: In member function ‘Wallet* WalletManager::recoveryWallet(const QString&, const QString&, bool, quint64)’:
src/libwalletqt/WalletManager.cpp:66:115: error: no matching function for call to ‘Bitmonero::WalletManager::recoveryWallet(std::__cxx11::string, std::__cxx11::string, bool&, quint64&)’
     Bitmonero::Wallet * w = m_pimpl->recoveryWallet(path.toStdString(), memo.toStdString(), testnet, restoreHeight);
                                                                                                                   ^
In file included from src/libwalletqt/WalletManager.h:6:0,
                 from src/libwalletqt/WalletManager.cpp:1:
/usr/include/wallet/wallet2_api.h:293:22: note: candidate: virtual Bitmonero::Wallet* Bitmonero::WalletManager::recoveryWallet(const string&, const string&, bool)
     virtual Wallet * recoveryWallet(const std::string &path, const std::string &memo, bool testnet = false) = 0;
                      ^~~~~~~~~~~~~~
/usr/include/wallet/wallet2_api.h:293:22: note:   candidate expects 3 arguments, 4 provided
src/libwalletqt/WalletManager.cpp: In member function ‘bool WalletManager::moveWallet(const QString&, const QString&)’:
src/libwalletqt/WalletManager.cpp:114:47: warning: unused parameter ‘src’ [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                               ^~~
src/libwalletqt/WalletManager.cpp:114:67: warning: unused parameter ‘dst’ [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                                                   ^~~
src/libwalletqt/WalletManager.cpp: In member function ‘QString WalletManager::walletLanguage(const QString&)’:
src/libwalletqt/WalletManager.cpp:120:54: warning: unused parameter ‘locale’ [-Wunused-parameter]
 QString WalletManager::walletLanguage(const QString &locale)
                                                      ^~~~~~
g++ -c -pipe -O2 -march=x86-64 -mtune=generic -O2 -pipe -fstack-protector-strong -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -I/media/s
f_git/pull/monero-core/monero/include -Isrc/libwalletqt -Isrc -isystem /usr/include/qt -isystem /usr/include/qt/QtQuick -isystem /usr/include/qt/QtWidgets -isystem /usr/include/qt/QtGui -isystem /usr/include/qt/QtQml -isystem /usr/include/
qt/QtNetwork -isystem /usr/include/qt/QtCore -I. -I/usr/lib/qt/mkspecs/linux-g++ -o PendingTransaction.o src/libwalletqt/PendingTransaction.cpp
src/libwalletqt/Wallet.cpp: In member function ‘bool Wallet::synchronized() const’:
src/libwalletqt/Wallet.cpp:95:26: error: ‘class Bitmonero::Wallet’ has no member named ‘synchronized’
     return m_walletImpl->synchronized();
                          ^~~~~~~~~~~~
src/libwalletqt/Wallet.cpp: In member function ‘bool Wallet::init(const QString&, quint64, bool, quint64)’:
src/libwalletqt/Wallet.cpp:118:85: warning: unused parameter ‘isRecovering’ [-Wunused-parameter]
 bool Wallet::init(const QString &daemonAddress, quint64 upperTransactionLimit, bool isRecovering, quint64 restoreHeight)
                                                                                     ^~~~~~~~~~~~
src/libwalletqt/Wallet.cpp:118:107: warning: unused parameter ‘restoreHeight’ [-Wunused-parameter]
 bool Wallet::init(const QString &daemonAddress, quint64 upperTransactionLimit, bool isRecovering, quint64 restoreHeight)
                                                                                                           ^~~~~~~~~~~~~
src/libwalletqt/Wallet.cpp: In member function ‘void Wallet::initAsync(const QString&, quint64, bool, quint64)’:
src/libwalletqt/Wallet.cpp:127:23: error: ‘class Bitmonero::Wallet’ has no member named ‘setRecoveringFromSeed’
         m_walletImpl->setRecoveringFromSeed(true);
                       ^~~~~~~~~~~~~~~~~~~~~
src/libwalletqt/Wallet.cpp:128:23: error: ‘class Bitmonero::Wallet’ has no member named ‘setRefreshFromBlockHeight’
         m_walletImpl->setRefreshFromBlockHeight(restoreHeight);
                       ^~~~~~~~~~~~~~~~~~~~~~~~~
src/libwalletqt/Wallet.cpp: In member function ‘quint64 Wallet::blockChainHeight() const’:
src/libwalletqt/Wallet.cpp:155:26: error: ‘class Bitmonero::Wallet’ has no member named ‘blockChainHeight’
     return m_walletImpl->blockChainHeight();
                          ^~~~~~~~~~~~~~~~
src/libwalletqt/Wallet.cpp: In member function ‘quint64 Wallet::daemonBlockChainHeight() const’:
src/libwalletqt/Wallet.cpp:164:50: error: ‘class Bitmonero::Wallet’ has no member named ‘daemonBlockChainHeight’
         m_daemonBlockChainHeight = m_walletImpl->daemonBlockChainHeight();
                                                  ^~~~~~~~~~~~~~~~~~~~~~
src/libwalletqt/Wallet.cpp: In member function ‘quint64 Wallet::daemonBlockChainTargetHeight() const’:
src/libwalletqt/Wallet.cpp:172:52: error: ‘class Bitmonero::Wallet’ has no member named ‘daemonBlockChainTargetHeight’
     m_daemonBlockChainTargetHeight = m_walletImpl->daemonBlockChainTargetHeight();
                                                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/libwalletqt/Wallet.cpp: In member function ‘void Wallet::setAutoRefreshInterval(int)’:
src/libwalletqt/Wallet.cpp:192:19: error: ‘class Bitmonero::Wallet’ has no member named ‘setAutoRefreshInterval’
     m_walletImpl->setAutoRefreshInterval(seconds);
                   ^~~~~~~~~~~~~~~~~~~~~~
src/libwalletqt/Wallet.cpp: In member function ‘int Wallet::autoRefreshInterval() const’:
src/libwalletqt/Wallet.cpp:197:26: error: ‘class Bitmonero::Wallet’ has no member named ‘autoRefreshInterval’
     return m_walletImpl->autoRefreshInterval();
                          ^~~~~~~~~~~~~~~~~~~
make: *** [Makefile:885: WalletManager.o] Error 1
```


# Discussion History
## mbg033 | 2016-10-15T08:51:41+00:00
Current master of `monero` already contains updated API:
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2_api.h#L374

might be MONERO_URL pointing to some another repo/branch?
can you delete `monero` directory before running this script?


## anonimal | 2016-10-15T09:46:06+00:00
Hi @mbg033. The build was fixed after deleting `monero` and running `build.sh`. Thank you!


# Action History
- Created by: anonimal | 2016-10-11T16:06:59+00:00
- Closed at: 2016-10-15T09:46:06+00:00
