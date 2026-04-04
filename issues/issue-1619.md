---
title: MSYS2 MINGW64 Build master error
source_url: https://github.com/monero-project/monero-gui/issues/1619
author: Lafudoci
assignees: []
labels: []
created_at: '2018-10-09T16:06:11+00:00'
updated_at: '2018-10-10T16:47:32+00:00'
type: issue
status: closed
closed_at: '2018-10-10T16:47:32+00:00'
---

# Original Description
Build fail on master 2ac69, MSYS2 MINGW64 Win64.
```
../src/libwalletqt/WalletManager.cpp: In member function 'bool WalletManager::moveWallet(const QString&, const QString&)':
../src/libwalletqt/WalletManager.cpp:170:47: warning: unused parameter 'src' [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                ~~~~~~~~~~~~~~~^~~
../src/libwalletqt/WalletManager.cpp:170:67: warning: unused parameter 'dst' [-Wunused-parameter]
 bool WalletManager::moveWallet(const QString &src, const QString &dst)
                                                    ~~~~~~~~~~~~~~~^~~
../src/libwalletqt/WalletManager.cpp: In member function 'QString WalletManager::walletLanguage(const QString&)':
../src/libwalletqt/WalletManager.cpp:176:54: warning: unused parameter 'locale' [-Wunused-parameter]
 QString WalletManager::walletLanguage(const QString &locale)
                                       ~~~~~~~~~~~~~~~^~~~~~
g++ -c -fno-keep-inline-dllexport -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -O2 -std=gnu++11 -Wall -W -Wextra -fexceptions -mthreads -DUNICODE -D_UNICODE -DWIN32 -DMINGW_HAS_SECURE_API=1 -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -DQT_NEEDS_QMAIN -I../../monero-gui -I. -IC:/msys64/home/LeftC/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -I../../../../mingw64/include/QtQuick -I../../../../mingw64/include/QtWidgets -I../../../../mingw64/include/QtGui -I../../../../mingw64/include/QtQml -I../../../../mingw64/include/QtNetwork -I../../../../mingw64/include/QtCore -Irelease -I../../../../mingw64/include -I../../../../mingw64/share/qt5/mkspecs/win32-g++  -o release/Wallet.o ../src/libwalletqt/Wallet.cpp
../src/libwalletqt/Wallet.cpp: In member function 'bool Wallet::blackballOutput(const QString&, const QString&)':
../src/libwalletqt/Wallet.cpp:743:26: error: 'class Monero::Wallet' has no member named 'blackballOutput'; did you mean 'blackballOutputs'?
     return m_walletImpl->blackballOutput(amount.toStdString(), offset.toStdString());
                          ^~~~~~~~~~~~~~~
                          blackballOutputs
../src/libwalletqt/Wallet.cpp: In member function 'bool Wallet::unblackballOutput(const QString&, const QString&)':
../src/libwalletqt/Wallet.cpp:778:86: error: no matching function for call to 'Monero::Wallet::unblackballOutput(std::__cxx11::string, std::__cxx11::string)'
     return m_walletImpl->unblackballOutput(amount.toStdString(), offset.toStdString());
                                                                                      ^
In file included from ../src/libwalletqt/Wallet.h:10,
                 from ../src/libwalletqt/Wallet.cpp:1:
../monero/src/wallet/api/wallet2_api.h:780:18: note: candidate: 'virtual bool Monero::Wallet::unblackballOutput(const string&)'
     virtual bool unblackballOutput(const std::string &pubkey) = 0;
                  ^~~~~~~~~~~~~~~~~
../monero/src/wallet/api/wallet2_api.h:780:18: note:   candidate expects 1 argument, 2 provided
In file included from ../src/libwalletqt/Wallet.cpp:1:
../src/libwalletqt/Wallet.h: In constructor 'Wallet::Wallet(Monero::Wallet*, QObject*)':
../src/libwalletqt/Wallet.h:350:31: warning: 'Wallet::m_subaddressModel' will be initialized after [-Wreorder]
     mutable SubaddressModel * m_subaddressModel;
                               ^~~~~~~~~~~~~~~~~
../src/libwalletqt/Wallet.h:337:21: warning:   'quint64 Wallet::m_daemonBlockChainHeight' [-Wreorder]
     mutable quint64 m_daemonBlockChainHeight;
                     ^~~~~~~~~~~~~~~~~~~~~~~~
../src/libwalletqt/Wallet.cpp:850:1: warning:   when initialized here [-Wreorder]
 Wallet::Wallet(Monero::Wallet *w, QObject *parent)
 ^~~~~~
make[1]: *** [Makefile.Release:3848: release/Wallet.o] Error 1
make[1]: Leaving directory '/home/LeftC/monero-gui/build'
make: *** [Makefile:36: release] Error 2
```

# Discussion History
## sanderfoobar | 2018-10-09T23:30:05+00:00
Fixed in #1624 

# Action History
- Created by: Lafudoci | 2018-10-09T16:06:11+00:00
- Closed at: 2018-10-10T16:47:32+00:00
