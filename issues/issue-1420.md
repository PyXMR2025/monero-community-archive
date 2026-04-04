---
title: Pretty basic compile fail of GUI -  candidate expects 2 arguments, 4 provided
source_url: https://github.com/monero-project/monero-gui/issues/1420
author: ronohara
assignees: []
labels: []
created_at: '2018-05-16T12:18:34+00:00'
updated_at: '2018-05-25T18:09:20+00:00'
type: issue
status: closed
closed_at: '2018-05-25T18:09:20+00:00'
---

# Original Description
Linux Mint 18.3

Fresh:    git clone https://github.com/monero-project/monero-gui.git

./build.sh 

gives



/translations/monero-core_zh-tw.qm
Updating '/root/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/root/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 104 untranslated source text(s)
g++ -c -m64 -pipe -fPIC -fstack-protector -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -O2 -std=c++0x -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_WIDGETS_LIB -DQT_GUI_LIB -DQT_QML_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I../../monero-gui -I. -I../monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/x86_64-linux-gnu/qt5 -isystem /usr/include/x86_64-linux-gnu/qt5/QtQuick -isystem /usr/include/x86_64-linux-gnu/qt5/QtWidgets -isystem /usr/include/x86_64-linux-gnu/qt5/QtGui -isystem /usr/include/x86_64-linux-gnu/qt5/QtQml -isystem /usr/include/x86_64-linux-gnu/qt5/QtNetwork -isystem /usr/include/x86_64-linux-gnu/qt5/QtCore -I. -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++-64 -o main.o ../main.cpp
../main.cpp: In function ‘int main(int, char**)’:
../main.cpp:126:91: error: no matching function for call to ‘Monero::Wallet::init(char*&, const char [18], const char*, bool)’
 allet::init(argv[0], "monero-wallet-gui", logPath.toStdString().c_str(), true);
                                                                              ^
In file included from ../src/libwalletqt/WalletManager.h:6:0,
                 from ../main.cpp:42:
../monero/include/wallet/api/wallet2_api.h:440:18: note: candidate: virtual bool Monero::Wallet::init(const string&, uint64_t, const string&, const string&, bool, bool)
     virtual bool init(const std::string &daemon_address, uint64_t upper_transac
                  ^
../monero/include/wallet/api/wallet2_api.h:440:18: note:   no known conversion for argument 4 from ‘bool’ to ‘const string& {aka const std::__cxx11::basic_string<char>&}’
../monero/include/wallet/api/wallet2_api.h:559:17: note: candidate: static void Monero::Wallet::init(const char*, const char*)
     static void init(const char *argv0, const char *default_log_base_name);
                 ^
../monero/include/wallet/api/wallet2_api.h:559:17: note:   candidate expects 2 arguments, 4 provided
Makefile:986: recipe for target 'main.o' failed
make: *** [main.o] Error 1


# Discussion History
## dEBRUYNE-1 | 2018-05-16T12:54:52+00:00
GUI won't build without #3796 from the monero repository if I recall correctly. 

## pazos | 2018-05-17T17:59:15+00:00
also, afaik linux mint don't have the qt version needed to build the gui.

You can check that with `apt-cache madison qt5-default` if returns a version lower than 5.7 then the gui will build but it will give an error at runtime.

# Action History
- Created by: ronohara | 2018-05-16T12:18:34+00:00
- Closed at: 2018-05-25T18:09:20+00:00
