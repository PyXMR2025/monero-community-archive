---
title: Trying to build on PocketCHIP - Debian 8 armv71
source_url: https://github.com/monero-project/monero-gui/issues/1061
author: Coded-Dude
assignees: []
labels:
- resolved
created_at: '2018-01-06T06:13:52+00:00'
updated_at: '2019-07-04T07:27:45+00:00'
type: issue
status: closed
closed_at: '2019-07-04T07:27:45+00:00'
---

# Original Description
I only installed all the x86 dependencies since the ARM chip is not 64 bit.  I have not tried it with the 64 bit dependencies, but that may be my next task.  Anywho, here is the output:


Building release
~/monero-gui ~/monero-gui
~/monero-gui ~/monero-gui
You are currently on commit ac509ed
The most recent tag was at 6f14fde
You are ahead of or behind a tagged release
Reset branch 'ac509ed'
D	include/INode.h
D	include/IWallet.h
libwallet_merged.a not found - Building libwallet
Building libwallet release
cleaning up existing monero build dir, libs and includes
~/monero-gui/monero/build/release ~/monero-gui ~/monero-gui
Configuring build for Linux armv7
Parse error in command line argument: -D
Should be: VAR:type=value
CMake Error: No cmake script provided.
CMake Error: Problem processing arguments. Aborting.

./get_libwallet_api.sh: line 212: pushd: /home/chip/monero-gui/monero/build/release/src/wallet: No such file or directory
make: Entering directory '/home/chip/monero-gui/monero'
cat version.sh >version 
chmod a+x version
make: Leaving directory '/home/chip/monero-gui/monero'
make: *** No targets specified and no makefile found.  Stop.
make: *** No rule to make target 'install'.  Stop.
~/monero-gui ~/monero-gui
./get_libwallet_api.sh: line 221: pushd: /home/chip/monero-gui/monero/build/release/src/daemon: No such file or directory
make: *** No targets specified and no makefile found.  Stop.
make: *** No rule to make target 'install'.  Stop.
~/monero-gui
make: *** /home/chip/monero-gui/monero/build/release/contrib/epee: No such file or directory.  Stop.
make: *** /home/chip/monero-gui/monero/build/release/external/easylogging++: No such file or directory.  Stop.
Installing libunbound...
./get_libwallet_api.sh: line 235: pushd: /home/chip/monero-gui/monero/build/release/external/unbound: No such file or directory
make: *** No rule to make target 'install'.  Stop.
./get_libwallet_api.sh: line 239: popd: directory stack empty
./get_libwallet_api.sh: line 242: popd: directory stack empty
make: Entering directory '/home/chip/monero-gui/src/zxcvbn-c'
make: Nothing to be done for 'all'.
make: Leaving directory '/home/chip/monero-gui/src/zxcvbn-c'
You are currently on commit ac509ed
The most recent tag was at 6f14fde
You are ahead of or behind a tagged release
~/monero-gui/monero ~/monero-gui ~/monero-gui
You are currently on commit a529f0a
The most recent tag was at 793bc97
You are ahead of or behind a tagged release
~/monero-gui ~/monero-gui
Project MESSAGE: Building with libunwind
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 390 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ar.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_ar.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_ar.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_ar.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 390 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pt-br.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_pt-br.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_pt-br.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_pt-br.qm'...
    Generated 364 translation(s) (364 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_de.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_de.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_de.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_de.qm'...
    Generated 314 translation(s) (314 finished and 0 unfinished)
    Ignored 49 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_eo.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_eo.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_eo.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_eo.qm'...
    Generated 372 translation(s) (372 finished and 0 unfinished)
    Ignored 56 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_es.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_es.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_es.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_es.qm'...
    Generated 328 translation(s) (328 finished and 0 unfinished)
    Ignored 22 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fi.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_fi.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_fi.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_fi.qm'...
    Generated 173 translation(s) (173 finished and 0 unfinished)
    Ignored 183 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_fr.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_fr.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_fr.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_fr.qm'...
    Generated 352 translation(s) (352 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hr.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_hr.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_hr.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_hr.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 390 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_id.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_id.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_id.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_id.qm'...
    Generated 342 translation(s) (342 finished and 0 unfinished)
    Ignored 24 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_hi.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_hi.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_hi.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_hi.qm'...
    Generated 66 translation(s) (66 finished and 0 unfinished)
    Ignored 307 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_it.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_it.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_it.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_it.qm'...
    Generated 364 translation(s) (364 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ja.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_ja.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_ja.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_ja.qm'...
    Generated 376 translation(s) (376 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_nl.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_nl.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_nl.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_nl.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_pl.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_pl.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_pl.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_pl.qm'...
    Generated 175 translation(s) (175 finished and 0 unfinished)
    Ignored 150 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ru.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_ru.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_ru.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_ru.qm'...
    Generated 343 translation(s) (343 finished and 0 unfinished)
    Ignored 37 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sv.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_sv.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_sv.qm'...
    Generated 365 translation(s) (365 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-cn.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_zh-cn.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_zh-cn.qm'...
    Generated 349 translation(s) (349 finished and 0 unfinished)
    Ignored 23 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_zh-tw.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_zh-tw.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_zh-tw.qm'...
    Generated 377 translation(s) (377 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_he.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_he.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_he.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_he.qm'...
    Generated 369 translation(s) (369 finished and 0 unfinished)
    Ignored 21 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ko.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_ko.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_ko.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_ko.qm'...
    Generated 373 translation(s) (373 finished and 0 unfinished)
    Ignored 3 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_ro.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_ro.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_ro.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_ro.qm'...
    Generated 357 translation(s) (357 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_da.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_da.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_da.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_da.qm'...
    Generated 346 translation(s) (346 finished and 0 unfinished)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_cs.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_cs.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_cs.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_cs.qm'...
    Generated 921 translation(s) (921 finished and 0 unfinished)
    Ignored 125 untranslated source text(s)
/usr/lib/arm-linux-gnueabihf/qt5/bin/lrelease -compress -nounfinished -removeidentical ../translations/monero-core_sk.ts -qm /home/chip/monero-gui/build/release/bin/translations/monero-core_sk.qm
Updating '/home/chip/monero-gui/build/release/bin/translations/monero-core_sk.qm'...
Removing translations equal to source text in '/home/chip/monero-gui/build/release/bin/translations/monero-core_sk.qm'...
    Generated 367 translation(s) (367 finished and 0 unfinished)
g++ -c -pipe -O2 -std=c++0x -Wall -W -D_REENTRANT -fPIE -DQT_NO_DEBUG -DQT_QUICK_LIB -DQT_QML_LIB -DQT_WIDGETS_LIB -DQT_NETWORK_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I/usr/lib/arm-linux-gnueabihf/qt5/mkspecs/linux-g++ -I../../monero-gui -I/home/chip/monero-gui/monero/include -I../src/libwalletqt -I../src/QR-Code-generator -I../src -I../monero/src -isystem /usr/include/arm-linux-gnueabihf/qt5 -isystem /usr/include/arm-linux-gnueabihf/qt5/QtQuick -isystem /usr/include/arm-linux-gnueabihf/qt5/QtQml -isystem /usr/include/arm-linux-gnueabihf/qt5/QtWidgets -isystem /usr/include/arm-linux-gnueabihf/qt5/QtNetwork -isystem /usr/include/arm-linux-gnueabihf/qt5/QtGui -isystem /usr/include/arm-linux-gnueabihf/qt5/QtCore -I. -I. -o main.o ../main.cpp
In file included from ../src/libwalletqt/Wallet.h:10:0,
                 from ../main.cpp:42:
../src/libwalletqt/PendingTransaction.h:29:18: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Status)
                  ^
../src/libwalletqt/PendingTransaction.h:29:18: error: expected ‘;’ at end of member declaration
../src/libwalletqt/PendingTransaction.h:36:20: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Priority)
                    ^
../src/libwalletqt/PendingTransaction.h:36:20: error: expected ‘;’ at end of member declaration
In file included from ../src/libwalletqt/Wallet.h:11:0,
                 from ../main.cpp:42:
../src/libwalletqt/UnsignedTransaction.h:27:18: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Status)
                  ^
../src/libwalletqt/UnsignedTransaction.h:27:18: error: expected ‘;’ at end of member declaration
../src/libwalletqt/UnsignedTransaction.h:34:20: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Priority)
                    ^
../src/libwalletqt/UnsignedTransaction.h:34:20: error: expected ‘;’ at end of member declaration
In file included from ../main.cpp:42:0:
../src/libwalletqt/Wallet.h:61:18: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Status)
                  ^
../src/libwalletqt/Wallet.h:61:18: error: expected ‘;’ at end of member declaration
../src/libwalletqt/Wallet.h:69:28: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(ConnectionStatus)
                            ^
../src/libwalletqt/Wallet.h:69:28: error: expected ‘;’ at end of member declaration
In file included from ../main.cpp:47:0:
../src/libwalletqt/TransactionInfo.h:37:21: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(Direction)
                     ^
../src/libwalletqt/TransactionInfo.h:37:21: error: expected ‘;’ at end of member declaration
In file included from ../main.cpp:49:0:
../src/model/TransactionHistoryModel.h:42:31: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(TransactionInfoRole)
                               ^
../src/model/TransactionHistoryModel.h:42:31: error: expected ‘;’ at end of member declaration
In file included from ../main.cpp:51:0:
../src/libwalletqt/AddressBook.h:34:21: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(ErrorCode);
                     ^
In file included from ../main.cpp:52:0:
../src/model/AddressBookModel.h:20:30: error: ISO C++ forbids declaration of ‘Q_ENUM’ with no type [-fpermissive]
     Q_ENUM(AddressBookRowRole)
                              ^
../src/model/AddressBookModel.h:20:30: error: expected ‘;’ at end of member declaration
../main.cpp:65:31: warning: unused parameter ‘type’ [-Wunused-parameter]
 void messageHandler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
                               ^
../main.cpp:65:63: warning: unused parameter ‘context’ [-Wunused-parameter]
 void messageHandler(QtMsgType type, const QMessageLogContext &context, const QString &msg)
                                                               ^
In file included from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qcoreapplication.h:45:0,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/qapplication.h:45,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/QApplication:1,
                 from ../main.cpp:29:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h: In instantiation of ‘constexpr int qMetaTypeId() [with T = PendingTransaction::Priority]’:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1622:27:   required from ‘constexpr int qRegisterMetaType() [with T = PendingTransaction::Priority]’
../main.cpp:136:53:   required from here
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1615:5: error: static assertion failed: Type is not registered, please use the Q_DECLARE_METATYPE macro to make it known to Qt's meta-object system
     Q_STATIC_ASSERT_X(QMetaTypeId2<T>::Defined, "Type is not registered, please use the Q_DECLARE_METATYPE macro to make it known to Qt's meta-object system");
     ^
In file included from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qobject.h:56:0,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qcoreapplication.h:48,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/qapplication.h:45,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/QApplication:1,
                 from ../main.cpp:29:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h: In instantiation of ‘static constexpr int QMetaTypeId2<T>::qt_metatype_id() [with T = PendingTransaction::Priority]’:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1616:44:   required from ‘constexpr int qMetaTypeId() [with T = PendingTransaction::Priority]’
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1622:27:   required from ‘constexpr int qRegisterMetaType() [with T = PendingTransaction::Priority]’
../main.cpp:136:53:   required from here
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1476:97: error: ‘qt_metatype_id’ is not a member of ‘QMetaTypeId<PendingTransaction::Priority>’
     static inline Q_DECL_CONSTEXPR int qt_metatype_id() { return QMetaTypeId<T>::qt_metatype_id(); }
                                                                                                 ^
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1476:100: error: body of constexpr function ‘static constexpr int QMetaTypeId2<T>::qt_metatype_id() [with T = PendingTransaction::Priority]’ not a return-statement
     static inline Q_DECL_CONSTEXPR int qt_metatype_id() { return QMetaTypeId<T>::qt_metatype_id(); }
                                                                                                    ^
In file included from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qcoreapplication.h:45:0,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/qapplication.h:45,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/QApplication:1,
                 from ../main.cpp:29:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h: In instantiation of ‘constexpr int qMetaTypeId() [with T = TransactionInfo::Direction]’:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1622:27:   required from ‘constexpr int qRegisterMetaType() [with T = TransactionInfo::Direction]’
../main.cpp:137:51:   required from here
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1615:5: error: static assertion failed: Type is not registered, please use the Q_DECLARE_METATYPE macro to make it known to Qt's meta-object system
     Q_STATIC_ASSERT_X(QMetaTypeId2<T>::Defined, "Type is not registered, please use the Q_DECLARE_METATYPE macro to make it known to Qt's meta-object system");
     ^
In file included from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qobject.h:56:0,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qcoreapplication.h:48,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/qapplication.h:45,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/QApplication:1,
                 from ../main.cpp:29:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h: In instantiation of ‘static constexpr int QMetaTypeId2<T>::qt_metatype_id() [with T = TransactionInfo::Direction]’:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1616:44:   required from ‘constexpr int qMetaTypeId() [with T = TransactionInfo::Direction]’
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1622:27:   required from ‘constexpr int qRegisterMetaType() [with T = TransactionInfo::Direction]’
../main.cpp:137:51:   required from here
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1476:97: error: ‘qt_metatype_id’ is not a member of ‘QMetaTypeId<TransactionInfo::Direction>’
     static inline Q_DECL_CONSTEXPR int qt_metatype_id() { return QMetaTypeId<T>::qt_metatype_id(); }
                                                                                                 ^
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1476:100: error: body of constexpr function ‘static constexpr int QMetaTypeId2<T>::qt_metatype_id() [with T = TransactionInfo::Direction]’ not a return-statement
     static inline Q_DECL_CONSTEXPR int qt_metatype_id() { return QMetaTypeId<T>::qt_metatype_id(); }
                                                                                                    ^
In file included from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qcoreapplication.h:45:0,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/qapplication.h:45,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/QApplication:1,
                 from ../main.cpp:29:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h: In instantiation of ‘constexpr int qMetaTypeId() [with T = TransactionHistoryModel::TransactionInfoRole]’:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1622:27:   required from ‘constexpr int qRegisterMetaType() [with T = TransactionHistoryModel::TransactionInfoRole]’
../main.cpp:138:69:   required from here
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1615:5: error: static assertion failed: Type is not registered, please use the Q_DECLARE_METATYPE macro to make it known to Qt's meta-object system
     Q_STATIC_ASSERT_X(QMetaTypeId2<T>::Defined, "Type is not registered, please use the Q_DECLARE_METATYPE macro to make it known to Qt's meta-object system");
     ^
In file included from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qobject.h:56:0,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtCore/qcoreapplication.h:48,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/qapplication.h:45,
                 from /usr/include/arm-linux-gnueabihf/qt5/QtWidgets/QApplication:1,
                 from ../main.cpp:29:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h: In instantiation of ‘static constexpr int QMetaTypeId2<T>::qt_metatype_id() [with T = TransactionHistoryModel::TransactionInfoRole]’:
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1616:44:   required from ‘constexpr int qMetaTypeId() [with T = TransactionHistoryModel::TransactionInfoRole]’
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1622:27:   required from ‘constexpr int qRegisterMetaType() [with T = TransactionHistoryModel::TransactionInfoRole]’
../main.cpp:138:69:   required from here
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1476:97: error: ‘qt_metatype_id’ is not a member of ‘QMetaTypeId<TransactionHistoryModel::TransactionInfoRole>’
     static inline Q_DECL_CONSTEXPR int qt_metatype_id() { return QMetaTypeId<T>::qt_metatype_id(); }
                                                                                                 ^
/usr/include/arm-linux-gnueabihf/qt5/QtCore/qmetatype.h:1476:100: error: body of constexpr function ‘static constexpr int QMetaTypeId2<T>::qt_metatype_id() [with T = TransactionHistoryModel::TransactionInfoRole]’ not a return-statement
     static inline Q_DECL_CONSTEXPR int qt_metatype_id() { return QMetaTypeId<T>::qt_metatype_id(); }
                                                                                                    ^
../main.cpp: In function ‘int main(int, char**)’:
../main.cpp:173:10: warning: unused variable ‘isMac’ [-Wunused-variable]
     bool isMac = false;
          ^
Makefile:785: recipe for target 'main.o' failed
make: *** [main.o] Error 1


# Discussion History
## dEBRUYNE-1 | 2019-07-04T06:58:48+00:00
Going to close this, as this is a build issue which is over 18 months old (and thus likely not relevant anymore).

## dEBRUYNE-1 | 2019-07-04T06:58:52+00:00
+resolved

# Action History
- Created by: Coded-Dude | 2018-01-06T06:13:52+00:00
- Closed at: 2019-07-04T07:27:45+00:00
