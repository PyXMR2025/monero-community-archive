---
title: 'Wallet.cpp: too many arguments to function call, expected 3, have 4; no matching
  function for call to Monero::Wallet::getTxProof'
source_url: https://github.com/monero-project/monero-gui/issues/974
author: issue-helper
assignees: []
labels: []
created_at: '2017-11-28T00:21:52+00:00'
updated_at: '2017-11-28T00:27:09+00:00'
type: issue
status: closed
closed_at: '2017-11-28T00:22:54+00:00'
---

# Original Description
(21a9bfb) 

https://build.getmonero.org/builders/monero-core-osx-10.11/builds/1019/steps/compile/logs/stdio

```
../src/libwalletqt/Wallet.cpp:510:136: error: too many arguments to function call, expected 3, have 4
    QString result = QString::fromStdString(m_walletImpl->getTxProof(txid.toStdString(), address.toStdString(), message.toStdString(), error_str));
                                            ~~~~~~~~~~~~~~~~~~~~~~~~                                                                   ^~~~~~~~~
../monero/include/wallet/wallet2_api.h:704:5: note: 'getTxProof' declared here
    virtual std::string getTxProof(const std::string &txid, const std::string &address, const std::string &message) const = 0;
    ^
../src/libwalletqt/Wallet.cpp:655:7: warning: field 'm_addressBookModel' will be initialized after field 'm_daemonBlockChainHeight' [-Wreorder]
    , m_addressBookModel(nullptr)
      ^
```
https://build.getmonero.org/builders/monero-core-ubuntu-amd64/builds/1037/steps/compile/logs/stdio

```
../src/libwalletqt/Wallet.cpp: In member function 'QString Wallet::getTxProof(const QString&, const QString&, const QString&) const':
../src/libwalletqt/Wallet.cpp:510:145: error: no matching function for call to 'Monero::Wallet::getTxProof(std::__cxx11::string, std::__cxx11::string, std::__cxx11::string, std::__cxx11::string&)'
     QString result = QString::fromStdString(m_walletImpl->getTxProof(txid.toStdString(), address.toStdString(), message.toStdString(), error_str));
                                                                                                                                                 ^
In file included from ../src/libwalletqt/Wallet.h:9:0,
                 from ../src/libwalletqt/Wallet.cpp:1:
../monero/include/wallet/wallet2_api.h:704:25: note: candidate: virtual std::__cxx11::string Monero::Wallet::getTxProof(const string&, const string&, const string&) const
     virtual std::string getTxProof(const std::string &txid, const std::string &address, const std::string &message) const = 0;
                         ^
../monero/include/wallet/wallet2_api.h:704:25: note:   candidate expects 3 arguments, 4 provided
In file included from ../src/libwalletqt/Wallet.cpp:1:0:
../src/libwalletqt/Wallet.h: In constructor 'Wallet::Wallet(Monero::Wallet*, QObject*)':
../src/libwalletqt/Wallet.h:304:32: warning: 'Wallet::m_addressBookModel' will be initialized after [-Wreorder]
     mutable AddressBookModel * m_addressBookModel;
                                ^
../src/libwalletqt/Wallet.h:294:21: warning:   'quint64 Wallet::m_daemonBlockChainHeight' [-Wreorder]
     mutable quint64 m_daemonBlockChainHeight;
                     ^
../src/libwalletqt/Wallet.cpp:649:1: warning:   when initialized here [-Wreorder]
 Wallet::Wallet(Monero::Wallet *w, QObject *parent)
 ^
```

# Discussion History
# Action History
- Created by: issue-helper | 2017-11-28T00:21:52+00:00
- Closed at: 2017-11-28T00:22:54+00:00
