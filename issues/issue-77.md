---
title: Crash with Windows x86 build
source_url: https://github.com/monero-project/monero-gui/issues/77
author: mbg033
assignees: []
labels: []
created_at: '2016-10-19T09:49:41+00:00'
updated_at: '2016-11-01T08:25:25+00:00'
type: issue
status: closed
closed_at: '2016-11-01T08:25:25+00:00'
---

# Original Description
Currently there's stable crash on Wizard -> Create Wallet page. Crashed immediately if "This is my first time, I want to create new account" option selected. Was unable to get stack under gdb, it crashed as well. Log:

```
Starting program: C:\msys64\home\mbg033\dev\monero-core\build\debug\bin\monero-core.exe
[New Thread 27544.0x2c8c]
[New Thread 27544.0x5e64]
[New Thread 27544.0x3fe8]
[New Thread 27544.0x6494]
warning: app startd
[New Thread 27544.0x39e4]
[New Thread 27544.0x4ac0]
[New Thread 27544.0x6828]
[New Thread 27544.0x6424]
[New Thread 27544.0x4d90]
[New Thread 27544.0x1418]
[New Thread 27544.0x26cc]
[New Thread 27544.0x514c]
[New Thread 27544.0x2dc0]
[New Thread 27544.0x79f4]
[New Thread 27544.0x2f0]
[New Thread 27544.0x7af4]
[Thread 27544.0x6424 exited with code 0]
[New Thread 27544.0x1c2c]
[New Thread 27544.0x61b0]
warning: qrc:///MiddlePanel.qml:246:9: QML StackView: Cannot anchor to an item that isn't a parent or sibling.
[New Thread 27544.0x559c]
[New Thread 27544.0x6b70]
[New Thread 27544.0x19f4]
warning: qml: rootItem:  ApplicationWindow_QMLTYPE_17_QML_224(0x3b8ba5a0, "appWindow")
warning: qml:
[New Thread 27544.0x5c24]
[New Thread 27544.0x7714]
[New Thread 27544.0x4b78]
warning: setLanguage   "en"
warning: qml: switchpage: currentPage:  0
warning: qml: show create wallet page
[New Thread 27544.0x5d98]
[New Thread 27544.0x7b84]

Thread 1 received signal SIGSEGV, Segmentation fault.
0x00648863 in __chkstk_ms ()
(gdb) bt
#0  0x00648863 in __chkstk_ms ()

This application has requested the Runtime to terminate it in an unusual way.
Please contact the application's support team for more information.
#1  0x00437e62 in cn_slow_hash (
mbg033@asus-n550jk MINGW32 ~/dev/monero-core/build/debug/bin
```


# Discussion History
## mbg033 | 2016-10-19T10:35:59+00:00
narrowed down to `wallet2::generate()` for now


## mbg033 | 2016-10-19T12:33:20+00:00
seems gdb from msys2 is broken, but I managed to run app from gdb that shipped with mingw installation from qt.io.

stack trace:

```
Reading symbols from monero-core.exe...done.
(gdb) r
Starting program: C:\dev\projects\2015-12-Monero\monero-core\build\debug\bin\monero-core.exe
[New Thread 13720.0x7428]
[New Thread 13720.0x74f4]
[New Thread 13720.0x5d5c]
[New Thread 13720.0x407c]
warning: app startd
[New Thread 13720.0x6e24]
[New Thread 13720.0x1818]
[New Thread 13720.0x6728]
[New Thread 13720.0x3a94]
[Thread 13720.0x3a94 exited with code 0]
[New Thread 13720.0x6f40]
[New Thread 13720.0x1570]
[New Thread 13720.0x78bc]
[New Thread 13720.0x649c]
[New Thread 13720.0x5c28]
[New Thread 13720.0x68f0]
[New Thread 13720.0x680c]
[New Thread 13720.0x26b0]
[New Thread 13720.0x1f9c]
[New Thread 13720.0x6630]
warning: qrc:///MiddlePanel.qml:246:9: QML StackView: Cannot anchor to an item that isn't a parent or sibling.
[New Thread 13720.0x2130]
[New Thread 13720.0x3fa8]
[New Thread 13720.0x5658]
warning: qml: rootItem:  ApplicationWindow_QMLTYPE_11_QML_224(0x375cb140, "appWindow")
warning: qml:
[New Thread 13720.0x4ac4]
[New Thread 13720.0x414c]
[New Thread 13720.0x7354]
[New Thread 13720.0x730c]
warning: setLanguage   "en"
warning: qml: switchpage: currentPage:  0
warning: qml: show create wallet page
warning: Creating wallet: , path:  "C:/Users/mbg033/AppData/Local/Temp/monero-core.p13720" , password:  "" , language:  "English" , testnet:  false
[New Thread 13720.0x6880]
[New Thread 13720.0x2f74]

Program received signal SIGSEGV, Segmentation fault.
0x006489e3 in __chkstk_ms ()
(gdb) bt
#0  0x006489e3 in __chkstk_ms ()
#1  0x00437fd2 in cn_slow_hash (data=0x7079020, length=0, hash=hash@entry=0x7078d1c "")
    at C:/msys64/home/mbg033/dev/monero-core/monero/src/crypto/slow-hash.c:1214
#2  0x00459844 in crypto::generate_chacha8_key (key=..., size=<optimized out>, data=<optimized out>)
    at C:/msys64/home/mbg033/dev/monero-core/monero/src/crypto/chacha8.h:76
#3  crypto::generate_chacha8_key (key=..., password=<error reading variable: access outside bounds of object referenced via synthetic pointer>)
    at C:/msys64/home/mbg033/dev/monero-core/monero/src/crypto/chacha8.h:82
#4  tools::wallet2::store_keys (this=this@entry=0x4e93c8b0, keys_file_name=..., password=..., watch_only=<optimized out>, watch_only@entry=false)
    at C:/msys64/home/mbg033/dev/monero-core/monero/src/wallet/wallet2.cpp:1439
#5  0x0045c73d in tools::wallet2::generate (this=0x4e93c8b0, wallet_="C:/Users/mbg033/AppData/Local/Temp/monero-core.p13720", password="",
    recovery_param=..., recover=recover@entry=false, two_random=two_random@entry=false)
    at C:/msys64/home/mbg033/dev/monero-core/monero/src/wallet/wallet2.cpp:1640
#6  0x0040dfed in Bitmonero::WalletImpl::create (this=this@entry=0x4c3678d0, path=..., password=..., language=...)
    at C:/msys64/home/mbg033/dev/monero-core/monero/src/wallet/api/wallet.cpp:228
#7  0x00413586 in Bitmonero::WalletManagerImpl::createWallet (this=<optimized out>, path="C:/Users/mbg033/AppData/Local/Temp/monero-core.p13720",
    password="", language="English", testnet=false) at C:/msys64/home/mbg033/dev/monero-core/monero/src/wallet/api/wallet_manager.cpp:49
#8  0x00402da5 in WalletManager::createWallet (this=0x288f58a0, path=..., password=..., language=..., testnet=false)
    at ../src/libwalletqt/WalletManager.cpp:30
#9  0x00408624 in WalletManager::qt_static_metacall (_o=0x288f58a0, _c=QMetaObject::InvokeMetaMethod, _id=2, _a=0x70798f8) at debug/moc_WalletManager.cpp:168
#10 0x00408e80 in WalletManager::qt_metacall (this=0x288f58a0, _c=QMetaObject::InvokeMetaMethod, _id=2, _a=0x70798f8) at debug/moc_WalletManager.cpp:259
#11 0x6bae124a in QMetaObject::metacall (object=0x288f58a0, cl=QMetaObject::InvokeMetaMethod, idx=7, argv=0x70798f8) at kernel\qmetaobject.cpp:301
#12 0x07976fb0 in QQmlObjectOrGadget::metacall (this=0x7079c70, type=QMetaObject::InvokeMetaMethod, index=7, argv=0x70798f8) at qml\qqmlpropertycache.cpp:154
#13 0x0791ecd6 in CallMethod (object=..., index=7, returnType=1027, argCount=4, argTypes=0x4c3677bc, engine=0x288cbd00, callArgs=0x28e215a8)
    at jsruntime\qv4qobjectwrapper.cpp:1127
#14 0x0791f6d3 in CallPrecise (object=..., data=..., engine=0x288cbd00, callArgs=0x28e215a8) at jsruntime\qv4qobjectwrapper.cpp:1378
#15 0x0791f992 in CallOverloaded (object=..., data=..., engine=0x288cbd00, callArgs=0x28e215a8, propertyCache=0x4e8a91e8)
    at jsruntime\qv4qobjectwrapper.cpp:1451
#16 0x07921acd in QV4::QObjectMethod::callInternal (this=0x28e215f8, callData=0x28e215a8) at jsruntime\qv4qobjectwrapper.cpp:1863
#17 0x079215d0 in QV4::QObjectMethod::call (m=0x28e215f8, callData=0x28e215a8) at jsruntime\qv4qobjectwrapper.cpp:1800
#18 0x07b1b205 in QV4::Object::call (this=0x28e215f8, d=0x28e215a8) at c:/Users/qt/work/qt/qtdeclarative/src/qml/jsruntime/qv4object_p.h:330
#19 0x07933633 in QV4::Runtime::callProperty (engine=0x288cbd00, nameIndex=21, callData=0x28e215a8) at jsruntime\qv4runtime.cpp:1030
#20 0x383108c7 in ?? ()
#21 0x078f67fe in QV4::SimpleScriptFunction::call (that=0x28e21548, callData=0x28e214f8) at jsruntime\qv4functionobject.cpp:582
#22 0x07b1b205 in QV4::Object::call (this=0x28e21548, d=0x28e214f8) at c:/Users/qt/work/qt/qtdeclarative/src/qml/jsruntime/qv4object_p.h:330
#23 0x07933633 in QV4::Runtime::callProperty (engine=0x288cbd00, nameIndex=108, callData=0x28e214f8) at jsruntime\qv4runtime.cpp:1030
#24 0x440608d1 in ?? ()
#25 0x078f67fe in QV4::SimpleScriptFunction::call (that=0x28e214b8, callData=0x28e21468) at jsruntime\qv4functionobject.cpp:582
#26 0x07b1b205 in QV4::Object::call (this=0x28e214b8, d=0x28e21468) at c:/Users/qt/work/qt/qtdeclarative/src/qml/jsruntime/qv4object_p.h:330
#27 0x07933633 in QV4::Runtime::callProperty (engine=0x288cbd00, nameIndex=23, callData=0x28e21468) at jsruntime\qv4runtime.cpp:1030
#28 0x44080f89 in ?? ()
#29 0x078f67fe in QV4::SimpleScriptFunction::call (that=0x4be10988, callData=0x28e213f0) at jsruntime\qv4functionobject.cpp:582
#30 0x07b1b205 in QV4::Object::call (this=0x4be10988, d=0x28e213f0) at c:/Users/qt/work/qt/qtdeclarative/src/qml/jsruntime/qv4object_p.h:330
#31 0x0798a1f8 in QQmlJavaScriptExpression::evaluate (this=0x3777dcc0, callData=0x28e213f0, isUndefined=0x0) at qml\qqmljavascriptexpression.cpp:196
#32 0x0795177e in QQmlBoundSignalExpression::evaluate (this=0x3777dcc0, a=0x707b578) at qml\qqmlboundsignal.cpp:244
#33 0x07951cff in QQmlBoundSignal_callback (e=0x3777dc88, a=0x707b578) at qml\qqmlboundsignal.cpp:376
#34 0x079771de in QQmlNotifier::emitNotify (endpoint=0x0, a=0x707b578) at qml\qqmlnotifier.cpp:100
#35 0x0793e06f in QQmlData::signalEmitted (object=0x3776c268, index=29, a=0x707b578) at qml\qqmlengine.cpp:780
#36 0x6bb0515f in QMetaObject::activate (sender=0x3776c268, signalOffset=29, local_signal_index=0, argv=0x707b578) at kernel\qobject.cpp:3618
#37 0x0793cf3b in QQmlVMEMetaObject::activate (this=0x3776c3f8, object=0x3776c268, index=45, args=0x707b578) at qml\qqmlvmemetaobject.cpp:1205
#38 0x0793b749 in QQmlVMEMetaObject::metaCall (this=0x3776c3f8, o=0x3776c268, c=QMetaObject::InvokeMetaMethod, _id=45, a=0x707b578)
    at qml\qqmlvmemetaobject.cpp:826
#39 0x6bae1222 in QMetaObject::metacall (object=0x3776c268, cl=QMetaObject::InvokeMetaMethod, idx=45, argv=0x707b578) at kernel\qmetaobject.cpp:299
#40 0x07976fb0 in QQmlObjectOrGadget::metacall (this=0x707b6e0, type=QMetaObject::InvokeMetaMethod, index=45, argv=0x707b578)
    at qml\qqmlpropertycache.cpp:1541
#41 0x0791edbc in CallMethod (object=..., index=45, returnType=43, argCount=0, argTypes=0x0, engine=0x288cbd00, callArgs=0x28e21398)
    at jsruntime\qv4qobjectwrapper.cpp:1145
#42 0x0791f71d in CallPrecise (object=..., data=..., engine=0x288cbd00, callArgs=0x28e21398) at jsruntime\qv4qobjectwrapper.cpp:1382
#43 0x07921a8c in QV4::QObjectMethod::callInternal (this=0x28e213e8, callData=0x28e21398) at jsruntime\qv4qobjectwrapper.cpp:1861
#44 0x079215d0 in QV4::QObjectMethod::call (m=0x28e213e8, callData=0x28e21398) at jsruntime\qv4qobjectwrapper.cpp:1800
---Type <return> to continue, or q <return> to quit---
#45 0x07b1b205 in QV4::Object::call (this=0x28e213e8, d=0x28e21398) at c:/Users/qt/work/qt/qtdeclarative/src/qml/jsruntime/qv4object_p.h:330
#46 0x07933633 in QV4::Runtime::callProperty (engine=0x288cbd00, nameIndex=7, callData=0x28e21398) at jsruntime\qv4runtime.cpp:1030
#47 0x44030db7 in ?? ()
#48 0x078f67fe in QV4::SimpleScriptFunction::call (that=0x4be103d0, callData=0x28e21318) at jsruntime\qv4functionobject.cpp:582
#49 0x07b1b205 in QV4::Object::call (this=0x4be103d0, d=0x28e21318) at c:/Users/qt/work/qt/qtdeclarative/src/qml/jsruntime/qv4object_p.h:330
#50 0x0798a1f8 in QQmlJavaScriptExpression::evaluate (this=0x3776ec68, callData=0x28e21318, isUndefined=0x0) at qml\qqmljavascriptexpression.cpp:196
#51 0x0795177e in QQmlBoundSignalExpression::evaluate (this=0x3776ec68, a=0x707c8e8) at qml\qqmlboundsignal.cpp:244
#52 0x07951cff in QQmlBoundSignal_callback (e=0x3776ec00, a=0x707c8e8) at qml\qqmlboundsignal.cpp:376
#53 0x079771de in QQmlNotifier::emitNotify (endpoint=0x0, a=0x707c8e8) at qml\qqmlnotifier.cpp:100
#54 0x0793e06f in QQmlData::signalEmitted (object=0x3776e950, index=45, a=0x707c8e8) at qml\qqmlengine.cpp:780
#55 0x6bb0515f in QMetaObject::activate (sender=0x3776e950, signalOffset=29, local_signal_index=16, argv=0x707c8e8) at kernel\qobject.cpp:3618
#56 0x6bb04ffa in QMetaObject::activate (sender=0x3776e950, m=0x2a02a878 <QQuickMouseArea::staticMetaObject>, local_signal_index=16, argv=0x707c8e8)
    at kernel\qobject.cpp:3602
#57 0x29e9394d in QQuickMouseArea::clicked (this=0x3776e950, _t1=0x707c950) at .moc\debug\moc_qquickmousearea_p.cpp:640
#58 0x29ddea41 in QQuickMouseArea::setPressed (this=0x3776e950, button=Qt::LeftButton, p=false, source=Qt::MouseEventNotSynthesized)
    at items\qquickmousearea.cpp:1204
#59 0x29ddd1dd in QQuickMouseArea::mouseReleaseEvent (this=0x3776e950, event=0x4c3758b8) at items\qquickmousearea.cpp:781
#60 0x29d8c578 in QQuickItem::event (this=0x3776e950, ev=0x4c3758b8) at items\qquickitem.cpp:7608
#61 0x1dd0fb70 in QApplicationPrivate::notify_helper (this=0x26e1b438, receiver=0x3776e950, e=0x4c3758b8) at kernel\qapplication.cpp:3799
#62 0x1dd0d143 in QApplication::notify (this=0x707fd88, receiver=0x3776e950, e=0x4c3758b8) at kernel\qapplication.cpp:3159
#63 0x6badc60f in QCoreApplication::notifyInternal2 (receiver=0x3776e950, event=0x4c3758b8) at kernel\qcoreapplication.cpp:988
#64 0x29f0cf35 in QCoreApplication::sendEvent (receiver=0x3776e950, event=0x4c3758b8) at c:/Users/qt/work/install/include/QtCore/qcoreapplication.h:231
#65 0x29d9c55e in QQuickWindow::sendEvent (this=0x375cb140, item=0x3776e950, e=0x4c3758b8) at items\qquickwindow.cpp:2716
#66 0x29d967b5 in QQuickWindowPrivate::deliverMouseEvent (this=0x37494e70, event=0x707d940) at items\qquickwindow.cpp:1620
#67 0x29d96c09 in QQuickWindow::mouseReleaseEvent (this=0x375cb140, event=0x707d940) at items\qquickwindow.cpp:1664
#68 0x11c05169 in QWindow::event (this=0x375cb140, ev=0x707d940) at kernel\qwindow.cpp:2045
#69 0x29d960aa in QQuickWindow::event (this=0x375cb140, e=0x707d940) at items\qquickwindow.cpp:1518
#70 0x1dd0fb70 in QApplicationPrivate::notify_helper (this=0x26e1b438, receiver=0x375cb140, e=0x707d940) at kernel\qapplication.cpp:3799
#71 0x1dd0d143 in QApplication::notify (this=0x707fd88, receiver=0x375cb140, e=0x707d940) at kernel\qapplication.cpp:3159
#72 0x6badc60f in QCoreApplication::notifyInternal2 (receiver=0x375cb140, event=0x707d940) at kernel\qcoreapplication.cpp:988
#73 0x11f19ba1 in QCoreApplication::sendSpontaneousEvent (receiver=0x375cb140, event=0x707d940)
    at ../../include/QtCore/../../src/corelib/kernel/qcoreapplication.h:234
#74 0x11bfb752 in QGuiApplicationPrivate::processMouseEvent (e=0x4c3757f8) at kernel\qguiapplication.cpp:1909
#75 0x11bfacd6 in QGuiApplicationPrivate::processWindowSystemEvent (e=0x4c3757f8) at kernel\qguiapplication.cpp:1693
#76 0x11bece8a in QWindowSystemInterface::sendWindowSystemEvents (flags=...) at kernel\qwindowsysteminterface.cpp:654
#77 0x62a94fe9 in QWindowsGuiEventDispatcher::sendPostedEvents (this=0x26e1b708) at eventdispatchers\qwindowsguieventdispatcher.cpp:82
#78 0x6bb28e12 in qt_internal_proc(HWND__*, unsigned int, unsigned int, long)@16 (hwnd=0x410736 <Bitmonero::WalletImpl::refreshThreadFunc()+3244>,
    message=1025, wp=0, lp=0) at kernel\qeventdispatcher_win.cpp:443
#79 0x7444d273 in USER32!SetManipulationInputTarget () from C:\WINDOWS\System32\user32.dll
#80 0x7442e84a in USER32!DispatchMessageW () from C:\WINDOWS\System32\user32.dll
#81 0x7442e1a4 in USER32!DispatchMessageW () from C:\WINDOWS\System32\user32.dll
#82 0x7442df60 in USER32!DispatchMessageW () from C:\WINDOWS\System32\user32.dll
#83 0x6bb2a39e in QEventDispatcherWin32::processEvents (this=0x26e1b708, flags=...) at kernel\qeventdispatcher_win.cpp:844
#84 0x62a94fa5 in QWindowsGuiEventDispatcher::processEvents (this=0x26e1b708, flags=...) at eventdispatchers\qwindowsguieventdispatcher.cpp:74
#85 0x6bada28c in QEventLoop::processEvents (this=0x707fcc0, flags=...) at kernel\qeventloop.cpp:134
#86 0x6bada53c in QEventLoop::exec (this=0x707fcc0, flags=...) at kernel\qeventloop.cpp:210
#87 0x6badcc91 in QCoreApplication::exec () at kernel\qcoreapplication.cpp:1261
#88 0x11bfab5a in QGuiApplication::exec () at kernel\qguiapplication.cpp:1639
#89 0x1dd0cc0b in QApplication::exec () at kernel\qapplication.cpp:2975
#90 0x00401fa8 in qMain (argc=1, argv=0x26e19f40) at ../main.cpp:136
#91 0x0040d0a0 in WinMain@16 () at qtmain_win.cpp:113
#92 0x008102cd in main (flags=1, cmdline=0x26e19ce8, inst=0x26e12480) at C:/repo/mingw-w64-crt-git/src/mingw-w64/mingw-w64-crt/crt/crt0_c.c:18
Warning: the current language does not match this frame.
(gdb)

```


## mbg033 | 2016-10-19T17:57:01+00:00
fixed here: https://github.com/monero-project/monero-core/pull/78/commits/15bfc853058c0917a2c40ab8116f6d7bdc4570c6
(needs to be checked on x86 linux as well)


## medusadigital | 2016-11-01T06:13:38+00:00
fixed, can be closed


# Action History
- Created by: mbg033 | 2016-10-19T09:49:41+00:00
- Closed at: 2016-11-01T08:25:25+00:00
