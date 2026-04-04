---
title: Error while compiling Monero GUI
source_url: https://github.com/monero-project/monero-gui/issues/1103
author: cryptobender69
assignees: []
labels: []
created_at: '2018-01-30T04:44:48+00:00'
updated_at: '2018-01-30T16:59:26+00:00'
type: issue
status: closed
closed_at: '2018-01-30T16:59:26+00:00'
---

# Original Description
Hello,

I keep on getting this below error while compiling monero-gui. I have monero-gui and monero both at the latest branch. I am compiling this on Mac OSX 10.12.6. Please let me know what other details would you like, Thanks!

Please help!

``
    struct
In file included from ../main.cpp:42:
In file included from ../src/libwalletqt/Wallet.h:11:
**../src/libwalletqt/UnsignedTransaction.h:30:27: **error**: no member named 'Priority_Low' in 'Monero::UnsignedTransaction'; did you mean**
      'Monero::PendingTransaction::Priority_Low'?
        Priority_Low    = Monero::UnsignedTransaction::Priority_Low,
                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                          Monero::PendingTransaction::Priority_Low
../monero/include/wallet/api/wallet2_api.h:74:9: note: 'Monero::PendingTransaction::Priority_Low' declared here
        Priority_Low = 1,
        ^


In file included from ../main.cpp:42:
In file included from ../src/libwalletqt/Wallet.h:11:
**../src/libwalletqt/UnsignedTransaction.h:31:27: error: no member named 'Priority_Medium' in 'Monero::UnsignedTransaction'; did you mean**
      'Monero::PendingTransaction::Priority_Medium'?
        Priority_Medium = Monero::UnsignedTransaction::Priority_Medium,
                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                          Monero::PendingTransaction::Priority_Medium
../monero/include/wallet/api/wallet2_api.h:75:9: note: 'Monero::PendingTransaction::Priority_Medium' declared here
        Priority_Medium = 2,
        ^


In file included from ../main.cpp:42:
In file included from ../src/libwalletqt/Wallet.h:11:
**../src/libwalletqt/UnsignedTransaction.h:32:27: error: no member named 'Priority_High' in 'Monero::UnsignedTransaction'; did you mean**
      'Monero::PendingTransaction::Priority_High'?
        Priority_High   = Monero::UnsignedTransaction::Priority_High
                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                          Monero::PendingTransaction::Priority_High
../monero/include/wallet/api/wallet2_api.h:76:9: note: 'Monero::PendingTransaction::Priority_High' declared here
        Priority_High = 3,
        ^
``


# Discussion History
## stoffu | 2018-01-30T06:02:00+00:00
Fixed by #1101 

## koicafe | 2018-01-30T08:43:15+00:00
Got problem while compile on MAC OSX Elcapitan 10.11.6

In file included from ../main.cpp:53:
../src/libwalletqt/Subaddress.h:41:45: error: expected expression
    Q_INVOKABLE QList<Monero::SubaddressRow*> getAll(bool update = false) const;
                                            ^
../src/libwalletqt/Subaddress.h:41:31: error: no member named 'SubaddressRow' in namespace 'Monero'
    Q_INVOKABLE QList<Monero::SubaddressRow*> getAll(bool update = false) const;
                      ~~~~~~~~^
../src/libwalletqt/Subaddress.h:42:17: error: no type named 'SubaddressRow' in namespace 'Monero'; did you mean 'Subaddress'?
    Q_INVOKABLE Monero::SubaddressRow * getRow(int index) const;
                ^~~~~~~~~~~~~~~~~~~~~
                Subaddress
../src/libwalletqt/Subaddress.h:37:7: note: 'Subaddress' declared here
class Subaddress : public QObject
      ^
../src/libwalletqt/Subaddress.h:55:25: error: no type named 'Subaddress' in namespace 'Monero'; did you mean simply 'Subaddress'?
    explicit Subaddress(Monero::Subaddress * subaddressImpl, QObject *parent);
                        ^~~~~~~~~~~~~~~~~~
                        Subaddress
../src/libwalletqt/Subaddress.h:37:7: note: 'Subaddress' declared here
class Subaddress : public QObject
      ^
../src/libwalletqt/Subaddress.h:57:5: error: no type named 'Subaddress' in namespace 'Monero'; did you mean simply 'Subaddress'?
    Monero::Subaddress * m_subaddressImpl;
    ^~~~~~~~~~~~~~~~~~
    Subaddress
../src/libwalletqt/Subaddress.h:37:7: note: 'Subaddress' declared here
class Subaddress : public QObject
      ^
../src/libwalletqt/Subaddress.h:58:41: error: expected expression
    mutable QList<Monero::SubaddressRow*> m_rows;
                                        ^
../src/libwalletqt/Subaddress.h:58:27: error: no member named 'SubaddressRow' in namespace 'Monero'
    mutable QList<Monero::SubaddressRow*> m_rows;
                  ~~~~~~~~^
../main.cpp:68:31: warning: unused parameter 'type' [-Wunused-parameter]
void messageHandler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
                              ^
../main.cpp:68:63: warning: unused parameter 'context' [-Wunused-parameter]
void messageHandler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
                                                              ^
../main.cpp:76:20: error: no member named 'onStartup' in namespace 'Monero::Utils'
    Monero::Utils::onStartup();
    ~~~~~~~~~~~~~~~^
6 warnings and 8 errors generated.
detail: https://pastebin.com/HhEVHpTh

## stoffu | 2018-01-30T09:52:44+00:00
@koicafe Your error log seems unrelated to the issue raised here. It seems like something is wrong with your build environment. Try removing the 'monero' and 'build' folders and running 'build.sh' again. If your error persists, please open a new issue.


## koicafe | 2018-01-30T11:03:29+00:00
Thank you let me try again. 

## cryptobender69 | 2018-01-30T11:07:14+00:00
@stoffu trying to compile now. Will let you know.

## cryptobender69 | 2018-01-30T16:59:26+00:00
works!

# Action History
- Created by: cryptobender69 | 2018-01-30T04:44:48+00:00
- Closed at: 2018-01-30T16:59:26+00:00
