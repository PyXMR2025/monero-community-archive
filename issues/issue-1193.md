---
title: no matching function for call to 'Monero::Wallet::debug(const char [4], std::__cxx11::string)'
source_url: https://github.com/monero-project/monero-gui/issues/1193
author: danrmiller
assignees: []
labels: []
created_at: '2018-03-20T21:44:31+00:00'
updated_at: '2018-07-28T20:44:24+00:00'
type: issue
status: closed
closed_at: '2018-03-20T22:44:44+00:00'
---

# Original Description
Any ideas about this?

https://build.getmonero.org/builders/monero-core-ubuntu-amd64/builds/1460/steps/compile/logs/stdio

```
g++ -c -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=gnu++11 -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../build -I. -I../monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -I/home/jaquee/Qt/include -I/home/jaquee/Qt/include/QtQuick -I/home/jaquee/Qt/include/QtWidgets -I/home/jaquee/Qt/include/QtGui -I/home/jaquee/Qt/include/QtQml -I/home/jaquee/Qt/include/QtNetwork -I/home/jaquee/Qt/include/QtCore -I. -I/home/jaquee/Qt/mkspecs/linux-g++ -o main.o ../main.cpp
../main.cpp: In function 'void messageHandler(QtMsgType, const QMessageLogContext&, const QString&)':
../main.cpp:71:51: error: no matching function for call to 'Monero::Wallet::debug(const char [4], std::__cxx11::string)'
     Monero::Wallet::debug("qml", msg.toStdString());
                                                   ^
In file included from ../src/libwalletqt/WalletManager.h:6:0,
                 from ../main.cpp:42:
../monero/src/wallet/api/wallet2_api.h:543:17: note: candidate: static void Monero::Wallet::debug(const string&)
     static void debug(const std::string &str);
                 ^
../monero/src/wallet/api/wallet2_api.h:543:17: note:   candidate expects 1 argument, 2 provided
../main.cpp: At global scope:
../main.cpp:68:31: warning: unused parameter 'type' [-Wunused-parameter]
 void messageHandler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
                               ^
../main.cpp:68:63: warning: unused parameter 'context' [-Wunused-parameter]
 void messageHandler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
                                                               ^
../main.cpp: In function 'int main(int, char**)':
../main.cpp:76:5: error: 'onStartup' is not a member of 'Monero::Utils'
     Monero::Utils::onStartup();
     ^
../main.cpp:186:10: warning: unused variable 'isMac' [-Wunused-variable]
     bool isMac = false;
          ^
Makefile:3119: recipe for target 'main.o' failed
make: *** [main.o] Error 1
```

# Discussion History
## danrmiller | 2018-03-20T22:44:44+00:00
Was a problem with the PR

## lutsifer | 2018-07-26T07:37:22+00:00
How did you make it to work?

## danrmiller | 2018-07-28T20:44:23+00:00
I think there was an issue with the proposed code change that was since fixed.

# Action History
- Created by: danrmiller | 2018-03-20T21:44:31+00:00
- Closed at: 2018-03-20T22:44:44+00:00
