---
title: Monero GUI crashes periodically after upgrade to 15
source_url: https://github.com/monero-project/monero-gui/issues/2483
author: ericmnel
assignees: []
labels: []
created_at: '2019-11-24T19:47:23+00:00'
updated_at: '2019-12-23T14:05:19+00:00'
type: issue
status: closed
closed_at: '2019-12-23T14:05:19+00:00'
---

# Original Description
GUI version: v0.15.0.1 (Qt 5.9.7)
Embedded Monero version: v0.15.0.1
Wallet path: /Users/eric/Monero/wallets/eric/eric
Wallet creation height: 1953049
Wallet log path: /Users/eric/Library/Logs/monero-wallet-gui.log
Wallet mode: Advanced modeOpenGL

Macbook Pro running MacOS 10.15.1

This is a new zero balance wallet created after I downloaded Monero 15.0.1.

crash report:

Process:               monero-wallet-gui [66306]
Path:                  /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
Identifier:            org.monero-project.monero-wallet-gui
Version:               0
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           monero-wallet-gui [66306]
User ID:               501

Date/Time:             2019-11-24 12:03:11.386 -0700
OS Version:            Mac OS X 10.15.1 (19B88)
Report Version:        12
Bridge OS Version:     4.1 (17P1081)
Anonymous UUID:        E83B53D0-AA13-0CC5-5D42-5110A7691ED5

Sleep/Wake UUID:       74F8FA16-1925-4CD9-A30B-4880F0643D67

Time Awake Since Boot: 1400000 seconds
Time Since Wake:       500000 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       KERN_INVALID_ADDRESS at 0x0000000000000024
Exception Note:        EXC_CORPSE_NOTIFY

Termination Signal:    Segmentation fault: 11
Termination Reason:    Namespace SIGNAL, Code 0xb
Terminating Process:   exc handler [66306]

VM Regions Near 0x24:
--> 
    __TEXT                 00000001028ae000-0000000103adb000 [ 18.2M] r-x/rwx SM=COW  /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   org.qt-project.QtQml          	0x000000010757a01b 0x1073fd000 + 1560603
1   org.qt-project.QtQml          	0x000000010757a07b 0x1073fd000 + 1560699
2   org.qt-project.QtQml          	0x0000000107579fb9 QV4::QObjectWrapper::markObjects(QV4::Heap::Base*, QV4::ExecutionEngine*) + 105
3   org.qt-project.QtQml          	0x0000000107418780 QV4::MemoryManager::mark() + 800
4   org.qt-project.QtQml          	0x0000000107415ea6 QV4::MemoryManager::runGC() + 1398
5   org.qt-project.QtQml          	0x0000000107415821 QV4::MemoryManager::allocString(unsigned long) + 81
6   org.qt-project.QtQml          	0x00000001074f349d QV4::ExecutionEngine::newString(QString const&) + 77
7   org.qt-project.QtQml          	0x0000000107576f12 QV4::QObjectWrapper::getProperty(QV4::ExecutionEngine*, QObject*, QQmlPropertyData*, bool) + 2498
8   org.qt-project.QtQml          	0x0000000107592a40 QV4::Runtime::method_getQmlQObjectProperty(QV4::ExecutionEngine*, QV4::Value const&, int, bool) + 224
9   ???                           	0x000000010ce87be8 0 + 4511529960
10  org.qt-project.QtQml          	0x00000001074fde4b QV4::ExecutionContext::simpleCall(QV4::Scope&, QV4::CallData*, QV4::Function*) + 475
11  org.qt-project.QtQml          	0x000000010751e83a 0x1073fd000 + 1185850
12  org.qt-project.QtQml          	0x000000010758e655 QV4::Runtime::method_callProperty(QV4::ExecutionEngine*, int, QV4::CallData*) + 853
13  ???                           	0x000000010ce2d901 0 + 4511160577
14  org.qt-project.QtQml          	0x00000001074fde4b QV4::ExecutionContext::simpleCall(QV4::Scope&, QV4::CallData*, QV4::Function*) + 475
15  org.qt-project.QtQml          	0x000000010751e83a 0x1073fd000 + 1185850
16  org.qt-project.QtQml          	0x000000010758e655 QV4::Runtime::method_callProperty(QV4::ExecutionEngine*, int, QV4::CallData*) + 853
17  ???                           	0x000000010c6506ba 0 + 4502914746
18  org.qt-project.QtQml          	0x00000001074fde4b QV4::ExecutionContext::simpleCall(QV4::Scope&, QV4::CallData*, QV4::Function*) + 475
19  org.qt-project.QtQml          	0x000000010751e83a 0x1073fd000 + 1185850
20  org.qt-project.QtQml          	0x000000010757d8ec 0x1073fd000 + 1575148
21  org.qt-project.QtCore         	0x0000000104d50591 QObject::event(QEvent*) + 801
22  org.qt-project.QtWidgets      	0x0000000104087e8d QApplicationPrivate::notify_helper(QObject*, QEvent*) + 301
23  org.qt-project.QtWidgets      	0x0000000104089207 QApplication::notify(QObject*, QEvent*) + 391
24  org.qt-project.QtCore         	0x0000000104d266b4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 164
25  org.qt-project.QtCore         	0x0000000104d2783b QCoreApplicationPrivate::sendPostedEvents(QObject*, int, QThreadData*) + 891
26  libqcocoa.dylib               	0x00000001096fa53e 0x1096d2000 + 165182
27  libqcocoa.dylib               	0x00000001096fae01 0x1096d2000 + 167425
28  com.apple.CoreFoundation      	0x00007fff2ca4ab81 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
29  com.apple.CoreFoundation      	0x00007fff2ca4ab20 __CFRunLoopDoSource0 + 103
30  com.apple.CoreFoundation      	0x00007fff2ca2e154 __CFRunLoopDoSources0 + 209
31  com.apple.CoreFoundation      	0x00007fff2ca2d760 __CFRunLoopRun + 1272
32  com.apple.CoreFoundation      	0x00007fff2ca2cfe3 CFRunLoopRunSpecific + 499
33  com.apple.HIToolbox           	0x00007fff2b5b467d RunCurrentEventLoopInMode + 292
34  com.apple.HIToolbox           	0x00007fff2b5b43bd ReceiveNextEventCommon + 600
35  com.apple.HIToolbox           	0x00007fff2b5b4147 _BlockUntilNextEventMatchingListInModeWithFilter + 64
36  com.apple.AppKit              	0x00007fff29c39864 _DPSNextEvent + 990
37  com.apple.AppKit              	0x00007fff29c385d4 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1352
38  com.apple.AppKit              	0x00007fff29c32d76 -[NSApplication run] + 658
39  libqcocoa.dylib               	0x00000001096f9b6d 0x1096d2000 + 162669
40  org.qt-project.QtCore         	0x0000000104d221b1 QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 417
41  org.qt-project.QtCore         	0x0000000104d26d58 QCoreApplication::exec() + 392
42  org.monero-project.monero-wallet-gui	0x00000001028b694b main + 11915
43  libdyld.dylib                 	0x00007fff63d6e2e5 start + 1

Thread 1:: QQmlThread
0   libsystem_kernel.dylib        	0x00007fff63ebf5be poll + 10
1   org.qt-project.QtCore         	0x0000000104d7b700 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 544
2   org.qt-project.QtCore         	0x0000000104d7cd77 QEventDispatcherUNIX::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) + 871
3   org.qt-project.QtCore         	0x0000000104d221b1 QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 417
4   org.qt-project.QtCore         	0x0000000104b56483 QThread::exec() + 115
5   org.qt-project.QtQml          	0x000000010764c3c9 0x1073fd000 + 2421705
6   org.qt-project.QtCore         	0x0000000104b5a32f 0x104b2e000 + 181039
7   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
8   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 2:: Qt bearer thread
0   libsystem_kernel.dylib        	0x00007fff63ebf5be poll + 10
1   org.qt-project.QtCore         	0x0000000104d7b550 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 112
2   org.qt-project.QtCore         	0x0000000104d7cd77 QEventDispatcherUNIX::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) + 871
3   org.qt-project.QtCore         	0x0000000104d221b1 QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 417
4   org.qt-project.QtCore         	0x0000000104b56483 QThread::exec() + 115
5   org.qt-project.QtCore         	0x0000000104b5a32f 0x104b2e000 + 181039
6   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
7   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 3:: QQuickXmlQueryEngine
0   libsystem_kernel.dylib        	0x00007fff63ebf5be poll + 10
1   org.qt-project.QtCore         	0x0000000104d7b700 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 544
2   org.qt-project.QtCore         	0x0000000104d7cd77 QEventDispatcherUNIX::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) + 871
3   org.qt-project.QtCore         	0x0000000104d221b1 QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 417
4   org.qt-project.QtCore         	0x0000000104b56483 QThread::exec() + 115
5   libqmlxmllistmodelplugin.dylib	0x000000010c8fc39a 0x10c8f8000 + 17306
6   org.qt-project.QtCore         	0x0000000104b5a32f 0x104b2e000 + 181039
7   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
8   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 4:: QSGRenderThread
0   libsystem_kernel.dylib        	0x00007fff63ebb032 __semwait_signal + 10
1   libsystem_c.dylib             	0x00007fff63e3e0fa nanosleep + 196
2   org.qt-project.QtCore         	0x0000000104d7b0eb 0x104b2e000 + 2412779
3   org.qt-project.QtQuick        	0x0000000107113eb2 0x107055000 + 782002
4   org.qt-project.QtQuick        	0x0000000107114fa8 0x107055000 + 786344
5   org.qt-project.QtCore         	0x0000000104b5a32f 0x104b2e000 + 181039
6   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
7   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 5:: Thread (pooled)
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.qt-project.QtCore         	0x0000000104b5bb80 0x104b2e000 + 187264
3   org.qt-project.QtCore         	0x0000000104b5b8cb 0x104b2e000 + 186571
4   org.qt-project.QtCore         	0x0000000104b5b882 QWaitCondition::wait(QMutex*, unsigned long) + 162
5   org.qt-project.QtCore         	0x0000000104b5727e 0x104b2e000 + 168574
6   org.qt-project.QtCore         	0x0000000104b5a32f 0x104b2e000 + 181039
7   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
8   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 6:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 7:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 8:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 9:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 10:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 11:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 12:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 13:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 14:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 15:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 16:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 17:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 18:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 19:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 20:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a2bcb 0x1028ae000 + 8342475
3   org.monero-project.monero-wallet-gui	0x0000000102e27f90 tools::threadpool::run(bool) + 224
4   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
5   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
6   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 21:: com.apple.CFSocket.private
0   libsystem_kernel.dylib        	0x00007fff63ebe7e6 __select + 10
1   com.apple.CoreFoundation      	0x00007fff2ca5ba8a __CFSocketManager + 632
2   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
3   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 22:: com.apple.NSEventThread
0   libsystem_kernel.dylib        	0x00007fff63eb7166 mach_msg_trap + 10
1   libsystem_kernel.dylib        	0x00007fff63eb76cc mach_msg + 60
2   com.apple.CoreFoundation      	0x00007fff2ca2e36b __CFRunLoopServiceMachPort + 322
3   com.apple.CoreFoundation      	0x00007fff2ca2d907 __CFRunLoopRun + 1695
4   com.apple.CoreFoundation      	0x00007fff2ca2cfe3 CFRunLoopRunSpecific + 499
5   com.apple.AppKit              	0x00007fff29c40dba _NSEventThread + 132
6   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
7   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 23:: Thread (pooled)
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.qt-project.QtCore         	0x0000000104b5bb80 0x104b2e000 + 187264
3   org.qt-project.QtCore         	0x0000000104b5b8cb 0x104b2e000 + 186571
4   org.qt-project.QtCore         	0x0000000104b5b882 QWaitCondition::wait(QMutex*, unsigned long) + 162
5   org.qt-project.QtCore         	0x0000000104b5727e 0x104b2e000 + 168574
6   org.qt-project.QtCore         	0x0000000104b5a32f 0x104b2e000 + 181039
7   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
8   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 24:
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.monero-project.monero-wallet-gui	0x00000001030a310e 0x1028ae000 + 8343822
3   org.monero-project.monero-wallet-gui	0x000000010292c927 0x1028ae000 + 518439
4   org.monero-project.monero-wallet-gui	0x000000010292b524 Monero::WalletImpl::refreshThreadFunc() + 1236
5   org.monero-project.monero-wallet-gui	0x00000001030a2412 0x1028ae000 + 8340498
6   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
7   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 25:: Thread (pooled)
0   libsystem_kernel.dylib        	0x00007fff63eba916 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff63f7b040 _pthread_cond_wait + 701
2   org.qt-project.QtCore         	0x0000000104b5bb80 0x104b2e000 + 187264
3   org.qt-project.QtCore         	0x0000000104b5b8cb 0x104b2e000 + 186571
4   org.qt-project.QtCore         	0x0000000104b5b882 QWaitCondition::wait(QMutex*, unsigned long) + 162
5   org.qt-project.QtCore         	0x0000000104b5727e 0x104b2e000 + 168574
6   org.qt-project.QtCore         	0x0000000104b5a32f 0x104b2e000 + 181039
7   libsystem_pthread.dylib       	0x00007fff63f7ad36 _pthread_start + 125
8   libsystem_pthread.dylib       	0x00007fff63f7758f thread_start + 15

Thread 26:
0   libsystem_pthread.dylib       	0x00007fff63f7756c start_wqthread + 0

Thread 0 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000004  rbx: 0x0000000000000002  rcx: 0x0000600001e09200  rdx: 0x0000000000000006
  rdi: 0x00006000024cc080  rsi: 0x00007fdfd8046c00  rbp: 0x00007ffeed34ec20  rsp: 0x00007ffeed34ec00
   r8: 0x0001fffffffffffe   r9: 0x000000012c5f09e0  r10: 0x000000010d600000  r11: 0x0000000000000017
  r12: 0x00006000024531a0  r13: 0x00007ffeed34eca8  r14: 0x00007fdfd8046c00  r15: 0x0000600000bdc460
  rip: 0x000000010757a01b  rfl: 0x0000000000010202  cr2: 0x0000000000000024
  
Logical CPU:     10
Error Code:      0x00000004 (no mapping for user data write)
Trap Number:     14


Binary Images:
       0x1028ae000 -        0x103adafff +org.monero-project.monero-wallet-gui (0) <D3D1207B-586B-357D-99FB-39B561EF31CB> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
       0x104022000 -        0x104058ffb +org.qt-project.QtSvg (5.9 - 5.9.7) <F3921A90-4B16-363C-BBCA-D5DF282971FE> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtSvg.framework/Versions/5/QtSvg
       0x104076000 -        0x1044deff3 +org.qt-project.QtWidgets (5.9 - 5.9.7) <4AAB81DF-A045-359B-A135-2A9A83F2024D> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets
       0x10463f000 -        0x104a34fe3 +org.qt-project.QtGui (5.9 - 5.9.7) <F35C62D3-57C6-3916-96F3-4707C533A7F2> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtGui.framework/Versions/5/QtGui
       0x104b2e000 -        0x106eecff3 +org.qt-project.QtCore (5.9 - 5.9.7) <DB6FF4E4-CE3D-3925-9E5D-BD6ED790FC0D> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore
       0x107055000 -        0x107302ff7 +org.qt-project.QtQuick (5.9 - 5.9.7) <2793D797-0C54-31B5-8182-8594F47B5C61> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQuick.framework/Versions/5/QtQuick
       0x1073fd000 -        0x1076daff3 +org.qt-project.QtQml (5.9 - 5.9.7) <122E69C2-AA25-32B3-BC81-CE6A00DE4C01> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQml.framework/Versions/5/QtQml
       0x107786000 -        0x1079e4ffb +org.qt-project.QtNetwork (5.9 - 5.9.7) <6C034B12-0002-3C37-9CCE-3344D9423715> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtNetwork.framework/Versions/5/QtNetwork
       0x107a9b000 -        0x107aa3ff7 +org.qt-project.QtMacExtras (5.9 - 5.9.7) <6D8B69F7-D49C-3CD8-9C78-49BA360640BE> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtMacExtras.framework/Versions/5/QtMacExtras
       0x1096d2000 -        0x1097fbff3 +libqcocoa.dylib (0) <F7E2A4CD-37C1-3E25-ABFC-70E4EDA6E23C> /Applications/monero-wallet-gui.app/Contents/PlugIns/platforms/libqcocoa.dylib
       0x109840000 -        0x10986cff3 +org.qt-project.QtPrintSupport (5.9 - 5.9.7) <C0A2D7BE-AB07-3FF2-AFF2-93AB231A2C73> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtPrintSupport.framework/Versions/5/QtPrintSupport
       0x10c61e000 -        0x10c626ffb +libqgenericbearer.dylib (0) <21FCF10C-7CB5-3F88-BFDB-03541EBD7469> /Applications/monero-wallet-gui.app/Contents/PlugIns/bearer/libqgenericbearer.dylib
       0x10c67c000 -        0x10c67fff3 +libqtquick2plugin.dylib (0) <D475BC21-BBA7-3C42-B155-BFA98A408281> /Applications/monero-wallet-gui.app/Contents/Resources/qml/QtQuick.2/libqtquick2plugin.dylib
       0x10c682000 -        0x10c685ff3 +libwindowplugin.dylib (0) <25C6842C-41AF-368C-BA1F-D63C8ED03412> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/Window.2/libwindowplugin.dylib
       0x10c688000 -        0x10c6cbfff +libqtquickcontrolsplugin.dylib (0) <745818FB-8A40-3568-B88D-926442AD9F7A> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/Controls/libqtquickcontrolsplugin.dylib
       0x10c6e7000 -        0x10c705ffb +libdialogplugin.dylib (0) <75AC277F-F2C6-33F2-9A1B-6A24F547DF99> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/Dialogs/libdialogplugin.dylib
       0x10c72d000 -        0x10c741ff3 +libqtquickcontrols2plugin.dylib (0) <1BF98774-0DE3-3BB5-A61E-46BFDCC62648> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/Controls.2/libqtquickcontrols2plugin.dylib
       0x10c74d000 -        0x10c7c4ff7 +org.qt-project.QtQuickTemplates2 (5.9 - 5.9.7) <4F24D388-8873-37E5-B1FC-26886A84DF5B> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQuickTemplates2.framework/Versions/5/QtQuickTemplates2
       0x10c823000 -        0x10c832ff3 +org.qt-project.QtQuickControls2 (5.9 - 5.9.7) <D3A34625-9023-3FDC-AB53-E40E35A7214E> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQuickControls2.framework/Versions/5/QtQuickControls2
       0x10c846000 -        0x10c857ffb +libqquicklayoutsplugin.dylib (0) <A4209010-0C3A-3FF5-B333-3DB2F5A1EB75> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/Layouts/libqquicklayoutsplugin.dylib
       0x10c880000 -        0x10c8acffb +libqtquicktemplates2plugin.dylib (0) <59E6B297-6888-30FA-9685-CBFF488E275D> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/Templates.2/libqtquicktemplates2plugin.dylib
       0x10c8e7000 -        0x10c8eaff7 +libqtgraphicaleffectsplugin.dylib (0) <321C9F88-48A9-3579-81D0-B3D5BF3FF9B9> /Applications/monero-wallet-gui.app/Contents/MacOS/QtGraphicalEffects/libqtgraphicaleffectsplugin.dylib
       0x10c8f8000 -        0x10c906ffb +libqmlxmllistmodelplugin.dylib (0) <96F61FEC-8937-32BE-9FD5-99B3940F4833> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/XmlListModel/libqmlxmllistmodelplugin.dylib
       0x10c90f000 -        0x10cc54fff +org.qt-project.QtXmlPatterns (5.9 - 5.9.7) <19B203F1-2564-329B-A6BE-07C42F3599C3> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtXmlPatterns.framework/Versions/5/QtXmlPatterns
       0x10ccb3000 -        0x10ccbbff3 +libqtgraphicaleffectsprivate.dylib (0) <A3CBE9C3-27EE-304A-A713-FE804772D6BD> /Applications/monero-wallet-gui.app/Contents/MacOS/QtGraphicalEffects/private/libqtgraphicaleffectsprivate.dylib
       0x10cce5000 -        0x10ccedff3 +libdialogsprivateplugin.dylib (0) <79484102-3E99-36B0-B148-80A39379853F> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/Dialogs/Private/libdialogsprivateplugin.dylib
       0x10ccf4000 -        0x10ccfdff7 +libqmlfolderlistmodelplugin.dylib (0) <6BA6EB91-1FD2-3658-A174-F10B9BF86CFF> /Applications/monero-wallet-gui.app/Contents/MacOS/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.dylib
       0x10cd05000 -        0x10cd09ffb +libqmlsettingsplugin.dylib (0) <D5317BD9-72B6-37F4-82F7-44842524BE0D> /Applications/monero-wallet-gui.app/Contents/MacOS/Qt/labs/settings/libqmlsettingsplugin.dylib
       0x10ce4e000 -        0x10ce63ff7 +libwidgetsplugin.dylib (0) <8A4ADB4F-99BE-3526-B9A6-221451EA6397> /Applications/monero-wallet-gui.app/Contents/MacOS/QtQuick/PrivateWidgets/libwidgetsplugin.dylib
       0x10d19f000 -        0x10d22fb5f  dyld (733.6) <DAFEA246-2F9A-3DCB-A37C-4246D4F92770> /usr/lib/dyld
       0x10d780000 -        0x10d89efff  com.apple.AMDRadeonX5000GLDriver (3.2.24 - 3.0.2) <95DB1C68-4EDC-3FB4-9163-F83FBB4DEE7C> /System/Library/Extensions/AMDRadeonX5000GLDriver.bundle/Contents/MacOS/AMDRadeonX5000GLDriver
       0x10dc50000 -        0x10dc56fff +libqgif.dylib (0) <42F4D7EB-68A3-30AF-9EDB-AA7F9509629E> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqgif.dylib
       0x10dc5a000 -        0x10dc61ffb +libqicns.dylib (0) <899A54F7-2B16-33D9-AF93-37FCDD084D46> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqicns.dylib
       0x10dc66000 -        0x10dc6bff3 +libqico.dylib (0) <081B7952-B299-37A7-B913-023D59466653> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqico.dylib
       0x10dc70000 -        0x10dca1ffb +libqjpeg.dylib (0) <84A1BC7D-071E-3888-9320-7EDB2A73810E> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqjpeg.dylib
       0x10dca9000 -        0x10dcadfff +libqmacjp2.dylib (0) <EA427292-7B14-39AC-9CA4-C4024E97E96B> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqmacjp2.dylib
       0x10dcb1000 -        0x10dcb5ff7 +libqsvg.dylib (0) <19EA3077-6F50-30A6-9FED-42210120742D> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqsvg.dylib
       0x10dcb9000 -        0x10dcbdff7 +libqtga.dylib (0) <A1DE617E-CAC3-30D4-B1CF-71C47AA5BF94> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqtga.dylib
       0x10dcc1000 -        0x10dcc7ffb +libqtiff.dylib (0) <D2654667-3623-31EB-86EE-19F708B126E6> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqtiff.dylib
       0x10dccc000 -        0x10dd26ffb +libtiff.5.dylib (0) <85BA07EA-3A6C-3FDE-8070-66AE42EBB45C> /Applications/monero-wallet-gui.app/Contents/Frameworks/libtiff.5.dylib
       0x10dd30000 -        0x10dd34ff3 +libqwbmp.dylib (0) <1225D353-152A-3CF0-94B8-FE1074BFDDDB> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqwbmp.dylib
       0x10dd53000 -        0x10dd56047  libobjc-trampolines.dylib (781) <6CF41A53-C75E-3AAA-9E47-E35C1EE56CE4> /usr/lib/libobjc-trampolines.dylib
       0x10e1ea000 -        0x10e216ffb +libjpeg.9.dylib (0) <8D69399D-C6B6-3679-BFD7-FCE79ABD2B67> /Applications/monero-wallet-gui.app/Contents/Frameworks/libjpeg.9.dylib
       0x10e21b000 -        0x10e271ffb +libqwebp.dylib (0) <357ECACE-1B7B-3FA5-B842-6CE04BFEE117> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqwebp.dylib
    0x7fff210d0000 -     0x7fff212dcff7  com.apple.RawCamera.bundle (9.00.1 - 1310.23) <A0E1BB1F-4D68-3415-90E8-79ACA52791A8> /System/Library/CoreServices/RawCamera.bundle/Contents/MacOS/RawCamera
    0x7fff21437000 -     0x7fff2146dfff  ATIRadeonX5000SCLib.dylib (3.2.24) <A70A1419-E52F-3C6C-9504-62F5037F00FD> /System/Library/Extensions/AMDRadeonX5000GLDriver.bundle/Contents/MacOS/ATIRadeonX5000SCLib.dylib
    0x7fff2146e000 -     0x7fff217f1ff1  com.apple.AMDRadeonX5000MTLDriver (3.2.24 - 3.0.2) <9BCEE375-1E7E-3295-838B-D3F3954920B1> /System/Library/Extensions/AMDRadeonX5000MTLDriver.bundle/Contents/MacOS/AMDRadeonX5000MTLDriver
    0x7fff22a24000 -     0x7fff2369cfff  libSC.dylib (3.2.24) <FE028806-66DD-33A6-9E5C-BB838360F440> /System/Library/Extensions/AMDShared.bundle/Contents/PlugIns/libSC.dylib
    0x7fff248e9000 -     0x7fff25711fff  com.apple.driver.AppleIntelKBLGraphicsGLDriver (14.2.16 - 14.0.2) <1602F44C-6FE2-3ABC-AEF6-980CB564AD9D> /System/Library/Extensions/AppleIntelKBLGraphicsGLDriver.bundle/Contents/MacOS/AppleIntelKBLGraphicsGLDriver
    0x7fff25712000 -     0x7fff25b11ff0  com.apple.driver.AppleIntelKBLGraphicsMTLDriver (14.2.16 - 14.0.2) <DB072379-5E2E-3D62-A61E-04128EABD551> /System/Library/Extensions/AppleIntelKBLGraphicsMTLDriver.bundle/Contents/MacOS/AppleIntelKBLGraphicsMTLDriver
    0x7fff283d8000 -     0x7fff283dcffb  com.apple.agl (3.3.3 - AGL-3.3.3) <2DAAE917-6792-35B7-8BCE-C785ACDF8174> /System/Library/Frameworks/AGL.framework/Versions/A/AGL
    0x7fff287c3000 -     0x7fff287c3fff  com.apple.Accelerate (1.11 - Accelerate 1.11) <956D070C-B522-3A08-891A-CAD6BA4082D1> /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
    0x7fff287c4000 -     0x7fff287daff7  libCGInterfaces.dylib (524.2) <23142415-0CD0-3020-B17E-F600C3889856> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/Libraries/libCGInterfaces.dylib
    0x7fff287db000 -     0x7fff28e46fdf  com.apple.vImage (8.1 - 524.2) <DCF3349F-1159-3F46-81E0-C18E041DC940> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage
    0x7fff28e47000 -     0x7fff290affff  libBLAS.dylib (1303) <B950B953-116A-3C78-91A9-F983F61BC795> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib
    0x7fff290b0000 -     0x7fff2939fff7  libBNNS.dylib (144.40.3) <BAE2A5E4-14A1-3C54-86DF-888FA26C745E> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib
    0x7fff293a1000 -     0x7fff29746fff  libLAPACK.dylib (1303) <5C248B39-F233-3074-A3A5-AF8F436FBF87> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLAPACK.dylib
    0x7fff29747000 -     0x7fff2975cff8  libLinearAlgebra.dylib (1303) <3AEC87AB-568C-3D88-959A-D6D8C2776FEC> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLinearAlgebra.dylib
    0x7fff2975d000 -     0x7fff29762ff3  libQuadrature.dylib (7) <7EE59014-8FC5-3369-868B-8A87E590BF78> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libQuadrature.dylib
    0x7fff29763000 -     0x7fff297d3fff  libSparse.dylib (103) <093F97A4-47DE-38DF-BB7A-FF5A3FB0BB3B> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libSparse.dylib
    0x7fff297d4000 -     0x7fff297e6fef  libSparseBLAS.dylib (1303) <4536B3F7-7017-36F5-B500-1A63F691CE03> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libSparseBLAS.dylib
    0x7fff297e7000 -     0x7fff299c0ffb  libvDSP.dylib (735) <E849AEB0-2995-38A4-B0C3-4ACEAF434D12> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvDSP.dylib
    0x7fff299c1000 -     0x7fff29a7cfd3  libvMisc.dylib (735) <18B48679-444E-3680-A9B2-006A8D1DE3EB> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvMisc.dylib
    0x7fff29a7d000 -     0x7fff29a7dfff  com.apple.Accelerate.vecLib (3.11 - vecLib 3.11) <79C1A1C7-E97A-3B7A-8737-444B402A7AA0> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/vecLib
    0x7fff29a7e000 -     0x7fff29addffc  com.apple.Accounts (113 - 113) <93F6714C-3028-3F7B-AA9B-82ED89D20D88> /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
    0x7fff29c22000 -     0x7fff2a9daffe  com.apple.AppKit (6.9 - 1894.10.126) <76EB4086-CA3D-3448-8CE0-9812F9A94F3A> /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
    0x7fff2aa2a000 -     0x7fff2aa2afff  com.apple.ApplicationServices (48 - 50) <0748E453-524B-33BA-806B-22786DED2958> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
    0x7fff2aa2b000 -     0x7fff2aa96fff  com.apple.ApplicationServices.ATS (377 - 493) <CF8434BF-B51D-3A68-B6FC-AFB0765530A2> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/ATS
    0x7fff2ab2f000 -     0x7fff2ab6dffa  libFontRegistry.dylib (274) <A512DEE5-A697-3EE6-AF9D-606C9D9156A0> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontRegistry.dylib
    0x7fff2abc8000 -     0x7fff2abf7ff7  com.apple.ATSUI (1.0 - 1) <50DC5F09-5336-3718-AEE9-490773BA3070> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATSUI.framework/Versions/A/ATSUI
    0x7fff2abf8000 -     0x7fff2abfcff3  com.apple.ColorSyncLegacy (4.13.0 - 1) <D4F7C969-FE2C-3036-94E3-FD2882F89C6F> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ColorSyncLegacy.framework/Versions/A/ColorSyncLegacy
    0x7fff2ac97000 -     0x7fff2acedffa  com.apple.HIServices (1.22 - 672) <0B1FD2E8-DEBD-3ED3-82F7-E0F80F21621A> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices
    0x7fff2acee000 -     0x7fff2acfcfff  com.apple.LangAnalysis (1.7.0 - 1.7.0) <72ECDBB9-F607-3FB3-ABC3-882C9EFB3245> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/LangAnalysis.framework/Versions/A/LangAnalysis
    0x7fff2acfd000 -     0x7fff2ad42ff2  com.apple.print.framework.PrintCore (15 - 516) <78F4A9D5-82F5-3578-A78F-CDD438DB6A6C> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Versions/A/PrintCore
    0x7fff2ad43000 -     0x7fff2ad4dfff  com.apple.QD (4.0 - 413) <63CCC6D7-659A-341A-A8A4-55B596EEFE9C> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/QD.framework/Versions/A/QD
    0x7fff2ad4e000 -     0x7fff2ad5bff0  com.apple.speech.synthesis.framework (9.0.22 - 9.0.22) <202F6033-A76D-3B2C-9BA9-9CCF4493AB4D> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/SpeechSynthesis.framework/Versions/A/SpeechSynthesis
    0x7fff2ad5c000 -     0x7fff2ae3cff2  com.apple.audio.toolbox.AudioToolbox (1.14 - 1.14) <CAE6B655-8D07-3040-811E-CE5DE42249AE> /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
    0x7fff2ae3e000 -     0x7fff2ae3efff  com.apple.audio.units.AudioUnit (1.14 - 1.14) <FE7A9727-7F3F-3E0F-B827-DF421993ED12> /System/Library/Frameworks/AudioUnit.framework/Versions/A/AudioUnit
    0x7fff2b1b4000 -     0x7fff2b52bffb  com.apple.CFNetwork (1120 - 1120) <5EA797F3-2F7A-3E0C-8DBC-DBE145004EC5> /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
    0x7fff2b5a5000 -     0x7fff2b5a5fff  com.apple.Carbon (160 - 162) <56A09CBE-D5EB-3918-B42B-B3ABFF52E1D1> /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
    0x7fff2b5a6000 -     0x7fff2b5a9ffb  com.apple.CommonPanels (1.2.6 - 101) <9286951D-8B2F-3A4B-86B2-767AFCC6A591> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/CommonPanels.framework/Versions/A/CommonPanels
    0x7fff2b5aa000 -     0x7fff2b89eff3  com.apple.HIToolbox (2.1.1 - 993.4) <AB2DC9D2-6A2A-3EB0-8ED9-8053CFEEC0A9> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox
    0x7fff2b89f000 -     0x7fff2b8a2ff3  com.apple.help (1.3.8 - 68) <64630D33-B292-3FD1-A3B7-AE98D4157EF1> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Help.framework/Versions/A/Help
    0x7fff2b8a3000 -     0x7fff2b8a8ff7  com.apple.ImageCapture (9.0 - 1600.18) <4B628CBB-65EC-3A36-8EBB-2F9D7D328744> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/ImageCapture.framework/Versions/A/ImageCapture
    0x7fff2b8a9000 -     0x7fff2b8a9fff  com.apple.ink.framework (10.15 - 227) <ED29C75F-6E14-352E-ACB9-AA899E2F5429> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Ink.framework/Versions/A/Ink
    0x7fff2b8aa000 -     0x7fff2b8c4ff2  com.apple.openscripting (1.7 - 185.1) <D300E418-CF0F-3127-BCBA-A7553F2F1E88> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/OpenScripting.framework/Versions/A/OpenScripting
    0x7fff2b8e5000 -     0x7fff2b8e5fff  com.apple.print.framework.Print (15 - 271) <4DDF3DC5-A69B-3BB8-B5F3-42ECC341A0B4> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Print.framework/Versions/A/Print
    0x7fff2b8e6000 -     0x7fff2b8e8ff7  com.apple.securityhi (9.0 - 55008) <8E09C68A-87BB-3D55-A52F-AB1B249D06F8> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/SecurityHI.framework/Versions/A/SecurityHI
    0x7fff2b8e9000 -     0x7fff2b8efff7  com.apple.speech.recognition.framework (6.0.3 - 6.0.3) <E2CECD92-568A-3C7A-AD98-D99CEF1BBCBF> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/SpeechRecognition.framework/Versions/A/SpeechRecognition
    0x7fff2ba98000 -     0x7fff2bc83ff7  com.apple.ColorSync (4.13.0 - 3394.3) <DCAECEC5-F7D0-3A28-AE9D-3FA59CC9FB26> /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
    0x7fff2bf6d000 -     0x7fff2c47cffa  com.apple.audio.CoreAudio (5.0 - 5.0) <73C7F0DD-8919-3056-AB1F-67705F942A04> /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
    0x7fff2c4cf000 -     0x7fff2c506ff0  com.apple.CoreBluetooth (1.0 - 1) <E57B1D4A-DF7A-37F3-833A-CD440EB58685> /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
    0x7fff2c507000 -     0x7fff2c8e5ffc  com.apple.CoreData (120 - 973.1) <AC3856BC-894E-30C4-BA99-25C06A3D9FE8> /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
    0x7fff2c8e6000 -     0x7fff2c9f2ff6  com.apple.CoreDisplay (1.0 - 186.2.4) <AD10EEEB-9A5F-3904-A487-50F13E4B2357> /System/Library/Frameworks/CoreDisplay.framework/Versions/A/CoreDisplay
    0x7fff2c9f3000 -     0x7fff2ce72fe7  com.apple.CoreFoundation (6.9 - 1673.126) <15D61616-B29B-3BDB-8624-4B84A4956485> /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
    0x7fff2ce74000 -     0x7fff2d4ecff0  com.apple.CoreGraphics (2.0 - 1348.12.4.3) <B8D7910C-0C72-315F-8CE1-C257FD0ADD84> /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
    0x7fff2d4fa000 -     0x7fff2d857ff5  com.apple.CoreImage (15.0.0 - 910.8) <CE3DB305-25FF-31FE-9334-C2370473BAAF> /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage
    0x7fff2dc1b000 -     0x7fff2dcf5ffc  com.apple.CoreMedia (1.0 - 2510.17.4.6) <A455F944-F862-3668-AA2C-008106F9814F> /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
    0x7fff2dde0000 -     0x7fff2dde0fff  com.apple.CoreServices (1069.11 - 1069.11) <C8F86BE7-AAED-30A6-BBC2-550446137E7C> /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
    0x7fff2dde1000 -     0x7fff2de66ff7  com.apple.AE (838 - 838) <3301AF1B-D178-306A-9641-B57AA03FB1BE> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/AE
    0x7fff2de67000 -     0x7fff2e148fff  com.apple.CoreServices.CarbonCore (1217 - 1217) <FAA1467B-6D39-3EBE-9810-A4DF49478F10> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CarbonCore.framework/Versions/A/CarbonCore
    0x7fff2e149000 -     0x7fff2e196ffd  com.apple.DictionaryServices (1.2 - 323) <C1798F09-36D3-3C8E-AF72-A3DE63962AF1> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/DictionaryServices.framework/Versions/A/DictionaryServices
    0x7fff2e197000 -     0x7fff2e19ffff  com.apple.CoreServices.FSEvents (1268.40.5 - 1268.40.5) <9BB76885-7CD7-3369-B759-33F7E5DA5392> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/FSEvents.framework/Versions/A/FSEvents
    0x7fff2e1a0000 -     0x7fff2e3d9ff0  com.apple.LaunchServices (1069.11 - 1069.11) <88F59BD5-412A-35EE-AD45-E6BF80B24891> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices
    0x7fff2e3da000 -     0x7fff2e472ff9  com.apple.Metadata (10.7.0 - 2074.4) <028AC15A-35B7-3E1F-BCDC-470C8EA0CA09> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Metadata
    0x7fff2e473000 -     0x7fff2e4a0ff7  com.apple.CoreServices.OSServices (1069.11 - 1069.11) <A667F007-A599-3869-99F7-1F8460011015> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/OSServices.framework/Versions/A/OSServices
    0x7fff2e4a1000 -     0x7fff2e508fff  com.apple.SearchKit (1.4.1 - 1.4.1) <F0A931E4-0C31-36BA-8DD7-01FDF9813FB7> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/SearchKit.framework/Versions/A/SearchKit
    0x7fff2e509000 -     0x7fff2e52dffd  com.apple.coreservices.SharedFileList (131 - 131) <62C3066A-3991-313F-AE2D-75B2B5934D52> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/SharedFileList.framework/Versions/A/SharedFileList
    0x7fff2e855000 -     0x7fff2ea09ff6  com.apple.CoreText (643.1.1.5 - 643.1.1.5) <4525DC61-0B5B-33B2-A249-68C6A1267EE7> /System/Library/Frameworks/CoreText.framework/Versions/A/CoreText
    0x7fff2ea0a000 -     0x7fff2ea4efff  com.apple.CoreVideo (1.8 - 334.0) <52692CD0-764F-3D77-9087-2825ED39AD0F> /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo
    0x7fff2ea4f000 -     0x7fff2eadcff1  com.apple.framework.CoreWLAN (13.0 - 1455.3) <3F7DCCA2-A5E2-3196-B2C7-31491192E75C> /System/Library/Frameworks/CoreWLAN.framework/Versions/A/CoreWLAN
    0x7fff2eca2000 -     0x7fff2ecadff7  com.apple.DirectoryService.Framework (10.15 - 220.40.1) <71100385-C865-3DEE-9B4E-B78E918E542B> /System/Library/Frameworks/DirectoryService.framework/Versions/A/DirectoryService
    0x7fff2ecae000 -     0x7fff2ed59ff0  com.apple.DiscRecording (9.0.3 - 9030.4.5) <F200BFE6-5AF1-34BA-8A87-B06753141358> /System/Library/Frameworks/DiscRecording.framework/Versions/A/DiscRecording
    0x7fff2ed7e000 -     0x7fff2ed84ff7  com.apple.DiskArbitration (2.7 - 2.7) <A3D2B0A0-3C72-3893-87BF-D45FE398A905> /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
    0x7fff2ef77000 -     0x7fff2f09eff7  com.apple.FileProvider (257 - 257) <E6755796-E58D-3C24-A0E9-0029521120C4> /System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider
    0x7fff2f0b6000 -     0x7fff2f47dff4  com.apple.Foundation (6.9 - 1673.126) <470C2315-3047-39BB-BB6B-2C620087091C> /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
    0x7fff2f4ea000 -     0x7fff2f53aff3  com.apple.GSS (4.0 - 2.0) <A149061D-5893-35B5-AE7F-BA889DFEADB2> /System/Library/Frameworks/GSS.framework/Versions/A/GSS
    0x7fff2f674000 -     0x7fff2f78cff8  com.apple.Bluetooth (7.0.1 - 7.0.1f1) <61A2BDF8-E3AC-3714-A967-92404AC52389> /System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth
    0x7fff2f7f3000 -     0x7fff2f896ffb  com.apple.framework.IOKit (2.0.2 - 1726.41.1) <FBB4A97B-D7CF-3B8C-932D-672343D63260> /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
    0x7fff2f898000 -     0x7fff2f8a8ff4  com.apple.IOSurface (269.6 - 269.6) <DB88C9C2-0F53-3C77-98F0-1D8A1DFA9CB1> /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
    0x7fff2f91f000 -     0x7fff2fa7bffe  com.apple.ImageIO.framework (3.3.0 - 1972.11.4.4) <2809F8D6-7B13-3703-B266-C5B7A6B62D97> /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
    0x7fff2fa7c000 -     0x7fff2fa7ffff  libGIF.dylib (1972.11.4.4) <2BFC7FDD-4A4F-323C-B60A-3B4AE526F7CE> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libGIF.dylib
    0x7fff2fa80000 -     0x7fff2fb3afef  libJP2.dylib (1972.11.4.4) <214BCCF5-2A06-3B4A-B2B8-4ECCB4B32D1C> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJP2.dylib
    0x7fff2fb3b000 -     0x7fff2fb5ffef  libJPEG.dylib (1972.11.4.4) <DBE9F84B-D9A2-3044-BFE2-B3853025FD9F> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJPEG.dylib
    0x7fff2fddd000 -     0x7fff2fdf7fe7  libPng.dylib (1972.11.4.4) <BD63D82F-55E5-32DB-96F9-8D7A3CDDA272> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libPng.dylib
    0x7fff2fdf8000 -     0x7fff2fdf9fff  libRadiance.dylib (1972.11.4.4) <2454AEBE-BE87-3D0F-BE68-6ECA3FCA361C> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libRadiance.dylib
    0x7fff2fdfa000 -     0x7fff2fe43fff  libTIFF.dylib (1972.11.4.4) <73A90FA4-9A51-3653-8F14-2EBBFEED3F78> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libTIFF.dylib
    0x7fff31268000 -     0x7fff3127aff3  com.apple.Kerberos (3.0 - 1) <8018F664-0026-3CC3-8685-3E2FE0BF2C7F> /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos
    0x7fff3127b000 -     0x7fff3127bfff  libHeimdalProxy.dylib (77) <51DB9CFB-808F-32E8-BB34-39F6702DBDED> /System/Library/Frameworks/Kerberos.framework/Versions/A/Libraries/libHeimdalProxy.dylib
    0x7fff3127c000 -     0x7fff312b2fff  com.apple.LDAPFramework (2.4.28 - 194.5) <33F235C9-B0D4-3005-B395-DACE6DD93855> /System/Library/Frameworks/LDAP.framework/Versions/A/LDAP
    0x7fff3160e000 -     0x7fff31618fff  com.apple.MediaAccessibility (1.0 - 125) <DD6304A2-1692-3C69-9FEA-B51F92510D5B> /System/Library/Frameworks/MediaAccessibility.framework/Versions/A/MediaAccessibility
    0x7fff316e4000 -     0x7fff31e27ff7  com.apple.MediaToolbox (1.0 - 2510.17.4.6) <3F852775-C302-3EE8-8631-31D96375BD73> /System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox
    0x7fff31e29000 -     0x7fff31eecff9  com.apple.Metal (212.2.3 - 212.2.3) <AA7DE079-2DFD-3E9F-A041-464CFBE1ABAE> /System/Library/Frameworks/Metal.framework/Versions/A/Metal
    0x7fff31f09000 -     0x7fff31f45ff3  com.apple.MetalPerformanceShaders.MPSCore (1.0 - 1) <FB95B500-E5A3-3FAD-882E-D12FD9CA0964> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/Versions/A/MPSCore
    0x7fff31f46000 -     0x7fff31fccfe6  com.apple.MetalPerformanceShaders.MPSImage (1.0 - 1) <C0E349E7-ADE3-3353-8CFF-3DAD653F810E> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/Versions/A/MPSImage
    0x7fff31fcd000 -     0x7fff31ff1ff8  com.apple.MetalPerformanceShaders.MPSMatrix (1.0 - 1) <8665FDF1-210F-3A8C-9D5D-FA0C49FD8C8C> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/Versions/A/MPSMatrix
    0x7fff31ff2000 -     0x7fff32007fff  com.apple.MetalPerformanceShaders.MPSNDArray (1.0 - 1) <EE7CF802-BF7F-3EEC-9EC2-26A3B3432275> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray
    0x7fff32008000 -     0x7fff32167ff4  com.apple.MetalPerformanceShaders.MPSNeuralNetwork (1.0 - 1) <46C9BDBB-1FB9-3E1A-A02C-818D16E472D9> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/Versions/A/MPSNeuralNetwork
    0x7fff32168000 -     0x7fff321b6fff  com.apple.MetalPerformanceShaders.MPSRayIntersector (1.0 - 1) <7CFEE008-E1AD-30FE-B0B7-9A7459701234> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/Versions/A/MPSRayIntersector
    0x7fff321b7000 -     0x7fff321b8ff5  com.apple.MetalPerformanceShaders.MetalPerformanceShaders (1.0 - 1) <241617D0-E5E7-3E36-971E-E278D15990A9> /System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/MetalPerformanceShaders
    0x7fff330fe000 -     0x7fff3310affe  com.apple.NetFS (6.0 - 4.0) <5C3C3672-2549-316E-9AC6-A1CFDCD16E9C> /System/Library/Frameworks/NetFS.framework/Versions/A/NetFS
    0x7fff3310b000 -     0x7fff3324eff6  com.apple.Network (1.0 - 1) <38F65393-1393-3888-9F02-C4087F19CA0D> /System/Library/Frameworks/Network.framework/Versions/A/Network
    0x7fff35c6e000 -     0x7fff35c76fff  libcldcpuengine.dylib (2.12.7) <A868A807-EA7D-3F78-9AEB-74E0AC72F8EC> /System/Library/Frameworks/OpenCL.framework/Versions/A/Libraries/libcldcpuengine.dylib
    0x7fff35c77000 -     0x7fff35ccfff7  com.apple.opencl (3.5 - 3.5) <D734AF0C-0EA3-3264-BBF9-D3099ACF47E3> /System/Library/Frameworks/OpenCL.framework/Versions/A/OpenCL
    0x7fff35cd0000 -     0x7fff35cecfff  com.apple.CFOpenDirectory (10.15 - 220.40.1) <AA81FC34-A7F6-3DA2-A275-B34F75099C7B> /System/Library/Frameworks/OpenDirectory.framework/Versions/A/Frameworks/CFOpenDirectory.framework/Versions/A/CFOpenDirectory
    0x7fff35ced000 -     0x7fff35cf8fff  com.apple.OpenDirectory (10.15 - 220.40.1) <ECFA2FFB-D5B6-3916-96F7-9F3A1EB1E534> /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory
    0x7fff36653000 -     0x7fff36655fff  libCVMSPluginSupport.dylib (17.10.22) <48C3CA4F-69EF-31E7-9120-0BA8E9162ACA> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCVMSPluginSupport.dylib
    0x7fff36656000 -     0x7fff3665bfff  libCoreFSCache.dylib (176.9) <D5D62F22-9099-370B-B264-B5398554EF0B> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCoreFSCache.dylib
    0x7fff3665c000 -     0x7fff36660fff  libCoreVMClient.dylib (176.9) <31DA9263-05A0-35A5-9CB8-40F8311B964B> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCoreVMClient.dylib
    0x7fff36661000 -     0x7fff36669ff7  libGFXShared.dylib (17.10.22) <B153F11B-C10F-38FE-AB8D-9E6C5315F210> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGFXShared.dylib
    0x7fff3666a000 -     0x7fff36674fff  libGL.dylib (17.10.22) <59E124FF-8F56-3028-9816-40699F152B3B> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib
    0x7fff36675000 -     0x7fff366aafff  libGLImage.dylib (17.10.22) <7EC55D26-7FA5-3B7B-A552-C50FA0308101> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLImage.dylib
    0x7fff366ab000 -     0x7fff3683dff7  libGLProgrammability.dylib (17.10.22) <832152E0-CE51-3BFD-B21E-DF2111D0C8F7> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLProgrammability.dylib
    0x7fff3683e000 -     0x7fff3687afff  libGLU.dylib (17.10.22) <A4C86485-7CDF-30B0-ACB5-B0D11CA88ED0> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLU.dylib
    0x7fff372aa000 -     0x7fff372b9ff7  com.apple.opengl (17.10.22 - 17.10.22) <0142B045-DCF8-3554-A7FB-48A173541E40> /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
    0x7fff372ba000 -     0x7fff37433ff7  GLEngine (17.10.22) <3B0B4AB6-3D54-3475-A50B-73C565244063> /System/Library/Frameworks/OpenGL.framework/Versions/A/Resources/GLEngine.bundle/GLEngine
    0x7fff37434000 -     0x7fff3745cfff  GLRendererFloat (17.10.22) <F2C6CBD1-30C3-3A1F-9976-C888359930A4> /System/Library/Frameworks/OpenGL.framework/Versions/A/Resources/GLRendererFloat.bundle/GLRendererFloat
    0x7fff38273000 -     0x7fff384f1ff0  com.apple.QuartzCore (1.11 - 815.19.4.2) <5F492A40-BBBC-3A31-83A8-32462A7B1FB4> /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
    0x7fff3903e000 -     0x7fff39384ff6  com.apple.security (7.0 - 59306.41.2) <FB3774D5-C940-35FB-960A-86253A01BDAE> /System/Library/Frameworks/Security.framework/Versions/A/Security
    0x7fff39385000 -     0x7fff3940dff7  com.apple.securityfoundation (6.0 - 55236) <6482C994-4DB4-320D-8FD4-50C998EA8856> /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
    0x7fff39467000 -     0x7fff3946bff8  com.apple.xpc.ServiceManagement (1.0 - 1) <2B80E13A-AFFC-355A-AA82-CCDEF4718E66> /System/Library/Frameworks/ServiceManagement.framework/Versions/A/ServiceManagement
    0x7fff3a1f8000 -     0x7fff3a262ff7  com.apple.SystemConfiguration (1.19 - 1.19) <A52A533D-DA25-3607-A18E-CA7C539E1C52> /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
    0x7fff3a4de000 -     0x7fff3a838ff4  com.apple.VideoToolbox (1.0 - 2510.17.4.6) <D8DDFD1A-003E-399A-9469-E6E55551726D> /System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox
    0x7fff3dfbe000 -     0x7fff3e082fef  com.apple.APFS (1412.41.1 - 1412.41.1) <0319F563-43AE-3F80-9107-7F0056E726DB> /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
    0x7fff3f15e000 -     0x7fff3f15fff1  com.apple.AggregateDictionary (1.0 - 1) <93D38CEB-C8F2-3011-8810-64D1E33B0D62> /System/Library/PrivateFrameworks/AggregateDictionary.framework/Versions/A/AggregateDictionary
    0x7fff3f4ec000 -     0x7fff3f509ffc  com.apple.AppContainer (4.0 - 448.40.2) <1A1D23EF-A9CA-3D46-ABAC-E87628E3DF26> /System/Library/PrivateFrameworks/AppContainer.framework/Versions/A/AppContainer
    0x7fff3f55e000 -     0x7fff3f56cff7  com.apple.AppSandbox (4.0 - 448.40.2) <19B46F6D-3F13-3679-81E0-C626E7E9749D> /System/Library/PrivateFrameworks/AppSandbox.framework/Versions/A/AppSandbox
    0x7fff3f9f3000 -     0x7fff3fa17ff3  com.apple.framework.Apple80211 (13.0 - 1460.1) <5290ABDC-D781-31CF-AD23-C39D3BA3FBD6> /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Apple80211
    0x7fff3fb4d000 -     0x7fff3fb5cfdf  com.apple.AppleFSCompression (119 - 1.0) <7EEDBF8A-8812-33D6-A5B0-F7D36825EE73> /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
    0x7fff3fc5b000 -     0x7fff3fc66ff7  com.apple.AppleIDAuthSupport (1.0 - 1) <B84D3BAB-BCF7-3DD8-A656-498D5444DC9D> /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/Versions/A/AppleIDAuthSupport
    0x7fff3fca8000 -     0x7fff3fcf0fff  com.apple.AppleJPEG (1.0 - 1) <CFE57DD6-F663-3DBF-8D37-BEFABF557D1F> /System/Library/PrivateFrameworks/AppleJPEG.framework/Versions/A/AppleJPEG
    0x7fff400c9000 -     0x7fff400cdff7  com.apple.AppleSRP (5.0 - 1) <77EB08CE-419B-38D5-9160-C1D4D3EE5131> /System/Library/PrivateFrameworks/AppleSRP.framework/Versions/A/AppleSRP
    0x7fff400ce000 -     0x7fff400f0ffb  com.apple.applesauce (1.0 - 16.22) <EFF69698-9566-3957-B3F5-CEC2B206EE7C> /System/Library/PrivateFrameworks/AppleSauce.framework/Versions/A/AppleSauce
    0x7fff401b0000 -     0x7fff401b3ffb  com.apple.AppleSystemInfo (3.1.5 - 3.1.5) <F4F1A097-C691-38BC-B91B-FFD828C3EA4E> /System/Library/PrivateFrameworks/AppleSystemInfo.framework/Versions/A/AppleSystemInfo
    0x7fff401b4000 -     0x7fff40204ff7  com.apple.AppleVAFramework (6.1.2 - 6.1.2) <C380FF1E-965E-3F05-BDCF-BB9EAC7F7B74> /System/Library/PrivateFrameworks/AppleVA.framework/Versions/A/AppleVA
    0x7fff4024d000 -     0x7fff4025cff1  com.apple.AssertionServices (1.0 - 223.40.19) <73B5C0D9-AB04-3961-A01D-FFBC94D1348E> /System/Library/PrivateFrameworks/AssertionServices.framework/Versions/A/AssertionServices
    0x7fff40798000 -     0x7fff40b96ff4  com.apple.audio.AudioResourceArbitration (1.0 - 1) <D51DC94A-FFDE-3B61-8E71-A05298853297> /System/Library/PrivateFrameworks/AudioResourceArbitration.framework/Versions/A/AudioResourceArbitration
    0x7fff40ded000 -     0x7fff4102afff  com.apple.audio.AudioToolboxCore (1.0 - 1104.26) <9D7C2174-0854-3C13-AF80-E814A9EC013C> /System/Library/PrivateFrameworks/AudioToolboxCore.framework/Versions/A/AudioToolboxCore
    0x7fff4102b000 -     0x7fff41144ff0  com.apple.AuthKit (1.0 - 1) <F190E8C4-1D9B-34F2-9255-902509534E6A> /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
    0x7fff412ff000 -     0x7fff41308ff3  com.apple.coreservices.BackgroundTaskManagement (1.0 - 104) <5E2B9000-49D6-3BFA-97F1-3B47A8A7418D> /System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/BackgroundTaskManagement
    0x7fff41309000 -     0x7fff413aaff8  com.apple.backup.framework (1.11.1 - 1298.1.2) <3C069796-5360-32F6-8841-BC263B94B2A3> /System/Library/PrivateFrameworks/Backup.framework/Versions/A/Backup
    0x7fff413ab000 -     0x7fff4142cffd  com.apple.BaseBoard (464.1 - 464.1) <1A44B522-904F-3541-BC8C-5EDF0C6EE49C> /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
    0x7fff4152e000 -     0x7fff4156aff7  com.apple.bom (14.0 - 219.1) <4D4C4ACA-A1DD-3D0B-B362-8D202EBE8D9B> /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom
    0x7fff420df000 -     0x7fff4212efff  com.apple.ChunkingLibrary (302 - 302) <593921FE-7EFE-36F6-8B05-4E89B00EABD6> /System/Library/PrivateFrameworks/ChunkingLibrary.framework/Versions/A/ChunkingLibrary
    0x7fff4225d000 -     0x7fff422e7ff3  com.apple.CloudDocs (1.0 - 681) <BC8D1A81-55F1-3236-BD13-5A01AC27CD68> /System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs
    0x7fff42fb7000 -     0x7fff42fc8fff  com.apple.CommonAuth (4.0 - 2.0) <1D04F654-22B1-37EF-90AD-3ADB5238806A> /System/Library/PrivateFrameworks/CommonAuth.framework/Versions/A/CommonAuth
    0x7fff42fdc000 -     0x7fff42ff3fff  com.apple.commonutilities (8.0 - 900) <0B13423D-84E7-394A-8E2A-62D815B5BC4B> /System/Library/PrivateFrameworks/CommonUtilities.framework/Versions/A/CommonUtilities
    0x7fff436ec000 -     0x7fff43ac1fc8  com.apple.CoreAUC (283.0.0 - 283.0.0) <505292C7-A6F0-392F-A94D-03D74F61F717> /System/Library/PrivateFrameworks/CoreAUC.framework/Versions/A/CoreAUC
    0x7fff43ac2000 -     0x7fff43af0ffb  com.apple.CoreAVCHD (6.1.0 - 6100.4.1) <BB2011D9-77DB-3C50-9228-C0A7B3880821> /System/Library/PrivateFrameworks/CoreAVCHD.framework/Versions/A/CoreAVCHD
    0x7fff43b13000 -     0x7fff43b32ff4  com.apple.analyticsd (1.0 - 1) <CFAD97DE-F4F0-3A1B-B6FE-855164CC68CC> /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
    0x7fff43dfd000 -     0x7fff43e08ff7  com.apple.frameworks.CoreDaemon (1.3 - 1.3) <E382C414-45C5-370B-A011-ED8FFCE8737D> /System/Library/PrivateFrameworks/CoreDaemon.framework/Versions/B/CoreDaemon
    0x7fff44080000 -     0x7fff44090ff3  com.apple.CoreEmoji (1.0 - 107) <8D1CA277-C4F7-3F3B-919E-73B68D39535E> /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
    0x7fff446e1000 -     0x7fff4474bff8  com.apple.CoreNLP (1.0 - 213) <329A9840-CBD8-33A2-A584-2805042284A9> /System/Library/PrivateFrameworks/CoreNLP.framework/Versions/A/CoreNLP
    0x7fff44bba000 -     0x7fff44bc2ff8  com.apple.CorePhoneNumbers (1.0 - 1) <D4405704-6DD4-3486-9DE4-80FC91F1F80B> /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/Versions/A/CorePhoneNumbers
    0x7fff4530e000 -     0x7fff45331fff  com.apple.CoreSVG (1.0 - 129) <00FDBCD4-A7CC-3E32-AC10-878B6A74596F> /System/Library/PrivateFrameworks/CoreSVG.framework/Versions/A/CoreSVG
    0x7fff45332000 -     0x7fff45365fff  com.apple.CoreServicesInternal (446.4 - 446.4) <E9CE4776-4375-384B-B4A8-D0BF1D5BBFA4> /System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal
    0x7fff45366000 -     0x7fff45394ff7  com.apple.CSStore (1069.11 - 1069.11) <792520D2-5D81-3867-8DC7-75F8205D5A5B> /System/Library/PrivateFrameworks/CoreServicesStore.framework/Versions/A/CoreServicesStore
    0x7fff45895000 -     0x7fff4591cfff  com.apple.CoreSymbolication (11.0 - 64509.98.1) <F0A1415B-068A-3CE6-9AB3-B11EF978B58A> /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
    0x7fff459b4000 -     0x7fff45ae0ffc  com.apple.coreui (2.1 - 607) <5FB17928-EB0D-3C46-B078-7B9621261385> /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
    0x7fff45ae1000 -     0x7fff45c7cffe  com.apple.CoreUtils (6.1 - 610.14) <62284EE1-1F77-3487-8DD0-43BDCFFD27D2> /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
    0x7fff45db1000 -     0x7fff45dc4ff1  com.apple.CrashReporterSupport (10.13 - 15011) <E4E96CDA-DFC4-3096-BCFC-994DB61D3E4D> /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
    0x7fff46030000 -     0x7fff46042ff0  com.apple.framework.DFRFoundation (1.0 - 252) <A7A09B8B-CEAD-3480-906E-9C3B685E6611> /System/Library/PrivateFrameworks/DFRFoundation.framework/Versions/A/DFRFoundation
    0x7fff46043000 -     0x7fff46048fff  com.apple.DSExternalDisplay (3.1 - 380) <F34E4A29-FD30-3DD0-946E-0AEDAE04EB18> /System/Library/PrivateFrameworks/DSExternalDisplay.framework/Versions/A/DSExternalDisplay
    0x7fff460b1000 -     0x7fff4612cff8  com.apple.datadetectorscore (8.0 - 659) <0E160ECD-98B5-3D9E-B155-0942A4B009A5> /System/Library/PrivateFrameworks/DataDetectorsCore.framework/Versions/A/DataDetectorsCore
    0x7fff46178000 -     0x7fff461b6ff0  com.apple.DebugSymbols (194 - 194) <FF16F79C-0D6B-32BF-B2DC-25BAF1E914C2> /System/Library/PrivateFrameworks/DebugSymbols.framework/Versions/A/DebugSymbols
    0x7fff461b7000 -     0x7fff46312ff7  com.apple.desktopservices (1.14.1 - 1281.1.1) <44D9F114-0D09-331E-8CD2-3A191E5AE8E1> /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
    0x7fff4643e000 -     0x7fff46506ff6  com.apple.DiskImagesFramework (559.40.3 - 559.40.3) <E2E4EDD4-00DA-3002-81A4-258281876871> /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
    0x7fff46507000 -     0x7fff465d7ff6  com.apple.DiskManagement (13.0 - 1648.0.5) <ADE3EAEE-5EAF-359E-BD5F-B2C348C3EEB0> /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
    0x7fff466b6000 -     0x7fff466baff9  com.apple.EFILogin (2.0 - 2) <A50E6356-A248-31DE-931C-F89ED4B22F38> /System/Library/PrivateFrameworks/EFILogin.framework/Versions/A/EFILogin
    0x7fff47b30000 -     0x7fff47f4bff9  com.apple.vision.FaceCore (4.3.0 - 4.3.0) <9F0FB4FD-C77F-3494-9898-9709BA2F1315> /System/Library/PrivateFrameworks/FaceCore.framework/Versions/A/FaceCore
    0x7fff485b1000 -     0x7fff486e8ffc  libFontParser.dylib (277.2.1.2) <92F025B1-AEE5-3BF8-8515-24FAF66AD7C2> /System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib
    0x7fff486e9000 -     0x7fff4871dfff  libTrueTypeScaler.dylib (277.2.1.2) <AD3D80AD-FF50-3652-B42B-A26030249CDF> /System/Library/PrivateFrameworks/FontServices.framework/libTrueTypeScaler.dylib
    0x7fff48782000 -     0x7fff48792ff6  libhvf.dylib (1.0 - $[CURRENT_PROJECT_VERSION]) <E7C8B563-8C55-30CC-AA12-EC9A6B1DAB1A> /System/Library/PrivateFrameworks/FontServices.framework/libhvf.dylib
    0x7fff4bc56000 -     0x7fff4bc57fff  libmetal_timestamp.dylib (902.11.1) <FA6BD306-D8F5-3F48-A98E-5BA327F3B679> /System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/3902/Libraries/libmetal_timestamp.dylib
    0x7fff4d2f2000 -     0x7fff4d2fdff7  libGPUSupportMercury.dylib (17.10.22) <4FBD47A2-1E5F-3FAB-81E0-BCAF8E31A46A> /System/Library/PrivateFrameworks/GPUSupport.framework/Versions/A/Libraries/libGPUSupportMercury.dylib
    0x7fff4d2fe000 -     0x7fff4d304fff  com.apple.GPUWrangler (4.5.9 - 4.5.9) <382B7462-5644-3C3E-968A-A5A9EBAFEECA> /System/Library/PrivateFrameworks/GPUWrangler.framework/Versions/A/GPUWrangler
    0x7fff4d61f000 -     0x7fff4d645ffb  com.apple.GenerationalStorage (2.0 - 312) <C0B51C28-86E3-350E-BE7D-009032478C18> /System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage
    0x7fff4e763000 -     0x7fff4e771ffb  com.apple.GraphVisualizer (1.0 - 100.1) <415AAD69-0A45-3B21-9698-D8798A48E5A2> /System/Library/PrivateFrameworks/GraphVisualizer.framework/Versions/A/GraphVisualizer
    0x7fff4e904000 -     0x7fff4e9c2ff4  com.apple.Heimdal (4.0 - 2.0) <735D30D6-8713-382B-97EA-12EFCC053486> /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
    0x7fff50aef000 -     0x7fff50af8ffe  com.apple.IOAccelMemoryInfo (1.0 - 1) <8FCBD2DE-0094-3F8B-BB86-646646BA5D9C> /System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/Versions/A/IOAccelMemoryInfo
    0x7fff50af9000 -     0x7fff50b01ff5  com.apple.IOAccelerator (438.2.7 - 438.2.7) <98C1C6DE-68A7-3396-B3D6-336CF11964AD> /System/Library/PrivateFrameworks/IOAccelerator.framework/Versions/A/IOAccelerator
    0x7fff50b04000 -     0x7fff50b1aff7  com.apple.IOPresentment (1.0 - 37) <E3AACF97-C85A-3720-90F0-61CAEF721F3D> /System/Library/PrivateFrameworks/IOPresentment.framework/Versions/A/IOPresentment
    0x7fff50ea4000 -     0x7fff50eefffc  com.apple.IconServices (438.2 - 438.2) <49E47D81-CBE8-3CB3-82F6-927B0AE64086> /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
    0x7fff510ac000 -     0x7fff510b2ffc  com.apple.InternationalSupport (1.0 - 44) <E881A3F9-7D1E-3943-B8DB-7BF31057CBB6> /System/Library/PrivateFrameworks/InternationalSupport.framework/Versions/A/InternationalSupport
    0x7fff512f3000 -     0x7fff51313fff  com.apple.security.KeychainCircle.KeychainCircle (1.0 - 1) <A6E97F92-DF9D-35F3-9DD8-2951FF162578> /System/Library/PrivateFrameworks/KeychainCircle.framework/Versions/A/KeychainCircle
    0x7fff5146a000 -     0x7fff51538ff5  com.apple.LanguageModeling (1.0 - 215) <D3478ED9-A757-355F-A4A0-464E133182D6> /System/Library/PrivateFrameworks/LanguageModeling.framework/Versions/A/LanguageModeling
    0x7fff51539000 -     0x7fff51581ff7  com.apple.Lexicon-framework (1.0 - 72) <94910CCB-C386-3912-84A2-1A730BB6EF62> /System/Library/PrivateFrameworks/Lexicon.framework/Versions/A/Lexicon
    0x7fff51588000 -     0x7fff5158cff6  com.apple.LinguisticData (1.0 - 353) <23AF4473-4FDB-39D9-8862-7D23276606A9> /System/Library/PrivateFrameworks/LinguisticData.framework/Versions/A/LinguisticData
    0x7fff51630000 -     0x7fff51635ff7  com.apple.LoginUICore (4.0 - 4.0) <7E1FC261-596B-3EBF-8BA2-0E2D616C9103> /System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/Frameworks/LoginUICore.framework/Versions/A/LoginUICore
    0x7fff51e24000 -     0x7fff51e27fff  com.apple.Mangrove (1.0 - 25) <445D1183-447D-3F73-9532-11DAFF69F2A8> /System/Library/PrivateFrameworks/Mangrove.framework/Versions/A/Mangrove
    0x7fff52089000 -     0x7fff52113ff0  com.apple.MediaExperience (1.0 - 1) <40A6CE90-66FA-341B-ABF9-5EE0FB506645> /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
    0x7fff52114000 -     0x7fff52147fff  com.apple.MediaKit (16 - 923) <F4E063D9-5302-3A54-A80E-721D2555E367> /System/Library/PrivateFrameworks/MediaKit.framework/Versions/A/MediaKit
    0x7fff528dd000 -     0x7fff52929ff7  com.apple.spotlight.metadata.utilities (1.0 - 2074.4) <8957F147-9371-3728-896E-FC517AC7E86E> /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
    0x7fff5292a000 -     0x7fff529f8ffd  com.apple.gpusw.MetalTools (1.0 - 1) <494BAEE0-8742-31F9-BC6D-C947A2756C5F> /System/Library/PrivateFrameworks/MetalTools.framework/Versions/A/MetalTools
    0x7fff52a52000 -     0x7fff52a6bff8  com.apple.MobileAssets (1.0 - 619.40.6) <2DBD115A-ACC8-37D9-9F5E-DE2F8C9F5D09> /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
    0x7fff52c28000 -     0x7fff52c46fff  com.apple.MobileKeyBag (2.0 - 1.0) <C137BEF9-6103-3AA5-B4BB-25BFE550B473> /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
    0x7fff52ead000 -     0x7fff52edbff7  com.apple.MultitouchSupport.framework (3410.2 - 3410.2) <67076218-F639-3C44-9670-20B54714E339> /System/Library/PrivateFrameworks/MultitouchSupport.framework/Versions/A/MultitouchSupport
    0x7fff53350000 -     0x7fff5335afff  com.apple.NetAuth (6.2 - 6.2) <BA114B8C-BE33-3DBB-BDC8-25423DBBD3A3> /System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth
    0x7fff53d48000 -     0x7fff53d94ff7  com.apple.OTSVG (1.0 - 643.1.1.5) <239EB765-2776-30F4-A300-4DF12C987D0F> /System/Library/PrivateFrameworks/OTSVG.framework/Versions/A/OTSVG
    0x7fff54f23000 -     0x7fff54f2effe  com.apple.PerformanceAnalysis (1.243 - 243) <FCF592E9-A0C8-3E31-BC87-91AEE71C2869> /System/Library/PrivateFrameworks/PerformanceAnalysis.framework/Versions/A/PerformanceAnalysis
    0x7fff54f2f000 -     0x7fff54f57ffb  com.apple.persistentconnection (1.0 - 1.0) <E6842FE3-D767-3540-95D3-39A213B45BD7> /System/Library/PrivateFrameworks/PersistentConnection.framework/Versions/A/PersistentConnection
    0x7fff5699e000 -     0x7fff569b1ff0  com.apple.PowerLog (1.0 - 1) <C7526E78-CCEB-3178-B560-32E6315AC4D1> /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
    0x7fff5781c000 -     0x7fff57876fff  com.apple.ProtectedCloudStorage (1.0 - 1) <9B166C3E-ACED-3528-A68F-22491EE811BA> /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage
    0x7fff57877000 -     0x7fff57890fff  com.apple.ProtocolBuffer (1 - 274.20.7.15.1) <89CB1292-0A41-3848-9AE1-CC5CEA756A25> /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
    0x7fff57c95000 -     0x7fff57cbeff9  com.apple.RemoteViewServices (2.0 - 148) <D8DCE656-7CBF-381A-827A-B8AA2A34CC08> /System/Library/PrivateFrameworks/RemoteViewServices.framework/Versions/A/RemoteViewServices
    0x7fff57e23000 -     0x7fff57e5eff0  com.apple.RunningBoardServices (1.0 - 223.40.19) <30C89668-9DEE-3948-B4EA-6DC9099497C2> /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
    0x7fff59772000 -     0x7fff59775ff1  com.apple.SecCodeWrapper (4.0 - 448.40.2) <C2138BC2-5F03-3E79-AC0C-F95F0BC9C0B3> /System/Library/PrivateFrameworks/SecCodeWrapper.framework/Versions/A/SecCodeWrapper
    0x7fff598bd000 -     0x7fff599e1ff4  com.apple.Sharing (1496.4 - 1496.4) <509EE7C8-C096-372E-B1CC-1CBB7B59DFEF> /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
    0x7fff5aa15000 -     0x7fff5ad0dffa  com.apple.SkyLight (1.600.0 - 440.14) <87B4BC36-78DA-3320-B455-FACB48DC63AA> /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
    0x7fff5b555000 -     0x7fff5b563fff  com.apple.SpeechRecognitionCore (6.0.91 - 6.0.91) <6D164E0A-5C8D-3125-933F-F4842C731E01> /System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/SpeechRecognitionCore
    0x7fff5b626000 -     0x7fff5b8b0ffe  com.apple.spotlight.index (10.7.0 - 2074.4) <D5D50BCE-287B-3C95-8F7E-B85182D64A97> /System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex
    0x7fff5bc34000 -     0x7fff5bc75ff9  com.apple.StreamingZip (1.0 - 1) <A2156ED8-DD0F-3F42-851D-1EF9ECA6AE2B> /System/Library/PrivateFrameworks/StreamingZip.framework/Versions/A/StreamingZip
    0x7fff5bd86000 -     0x7fff5bd8fff3  com.apple.SymptomDiagnosticReporter (1.0 - 1238.40.4) <FB255398-53B0-3462-8227-EBD173B5F93E> /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter
    0x7fff5be01000 -     0x7fff5be2bff0  com.apple.framework.SystemAdministration (1.0 - 1.0) <37D8FA9B-7C69-30D4-A8E9-8973924733B0> /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
    0x7fff5c044000 -     0x7fff5c054ff3  com.apple.TCC (1.0 - 1) <87BE8D5C-5D35-3434-8BDF-1615349C7A21> /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
    0x7fff5c546000 -     0x7fff5c60dff4  com.apple.TextureIO (3.10.9 - 3.10.9) <499A5034-C527-30AC-9580-912423C3C2D8> /System/Library/PrivateFrameworks/TextureIO.framework/Versions/A/TextureIO
    0x7fff5c78a000 -     0x7fff5c78bfff  com.apple.TrustEvaluationAgent (2.0 - 33) <4327B52D-2681-3195-B1F8-270D9137F932> /System/Library/PrivateFrameworks/TrustEvaluationAgent.framework/Versions/A/TrustEvaluationAgent
    0x7fff5d464000 -     0x7fff5d6bdffa  com.apple.UIFoundation (1.0 - 659.5) <99072103-6A73-3538-944A-5FD2AF709A78> /System/Library/PrivateFrameworks/UIFoundation.framework/Versions/A/UIFoundation
    0x7fff5e2ae000 -     0x7fff5e2cefff  com.apple.UserManagement (1.0 - 1) <CAD75201-57C8-338E-BE1B-5C5E2EEB9DAB> /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
    0x7fff5f080000 -     0x7fff5f16affe  com.apple.ViewBridge (462 - 462) <627E4CA4-2E4E-3CF7-8DBB-F09990DDF0FF> /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
    0x7fff5f30f000 -     0x7fff5f310fff  com.apple.WatchdogClient.framework (1.0 - 67.40.1) <B1228D4E-50B5-3630-A7F4-5598651CE963> /System/Library/PrivateFrameworks/WatchdogClient.framework/Versions/A/WatchdogClient
    0x7fff5fee7000 -     0x7fff5feeaffe  com.apple.dt.XCTTargetBootstrap (1.0 - 15508) <BA4C9007-2C3E-33DE-B81C-608918D2FDF1> /System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/Versions/A/XCTTargetBootstrap
    0x7fff5ff63000 -     0x7fff5ff71ffd  com.apple.audio.caulk (1.0 - 32.3) <089441BF-D7F6-388F-8D89-0262AB2EEA3F> /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk
    0x7fff602b1000 -     0x7fff602b3ff3  com.apple.loginsupport (1.0 - 1) <FFE90A0A-BEBC-3032-9368-94C016BE0795> /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
    0x7fff602b4000 -     0x7fff602c7ffd  com.apple.login (3.0 - 3.0) <51B9680F-41CE-394E-A600-1B5B0EC8D52B> /System/Library/PrivateFrameworks/login.framework/Versions/A/login
    0x7fff605e6000 -     0x7fff6061bff2  libAudioToolboxUtility.dylib (1104.26) <261CDFD3-BEFF-3BE8-9322-8A0F5282D4B9> /usr/lib/libAudioToolboxUtility.dylib
    0x7fff60622000 -     0x7fff60657ff7  libCRFSuite.dylib (48) <CDEA70A4-318B-3990-9AAE-1D7B18132760> /usr/lib/libCRFSuite.dylib
    0x7fff6065a000 -     0x7fff60664ff3  libChineseTokenizer.dylib (34) <4D68248B-BD40-32E3-ABCA-CE23BCA0A6A4> /usr/lib/libChineseTokenizer.dylib
    0x7fff60665000 -     0x7fff606eefff  libCoreStorage.dylib (551) <440FD2FE-94FD-3456-898A-6420EAC5A71F> /usr/lib/libCoreStorage.dylib
    0x7fff606f1000 -     0x7fff606f3fff  libDiagnosticMessagesClient.dylib (112) <83F42398-DB41-3BB2-B8A1-10D78C4B5778> /usr/lib/libDiagnosticMessagesClient.dylib
    0x7fff60738000 -     0x7fff608efff3  libFosl_dynamic.dylib (100.4) <F5583DFD-E3A1-3D6A-8698-613F7FA119A0> /usr/lib/libFosl_dynamic.dylib
    0x7fff60916000 -     0x7fff6091cff3  libIOReport.dylib (54) <EC75DB3B-CFC4-3235-8C2F-CE3C29CA8CFE> /usr/lib/libIOReport.dylib
    0x7fff609fc000 -     0x7fff60a03fff  libMatch.1.dylib (36) <D059FA22-1620-3A26-BF81-70EA469C97EB> /usr/lib/libMatch.1.dylib
    0x7fff60a33000 -     0x7fff60a52fff  libMobileGestalt.dylib (826.40.7) <C9875B8D-F7C6-32F6-A94D-1F2CA20D00CE> /usr/lib/libMobileGestalt.dylib
    0x7fff60bb9000 -     0x7fff60bbaff3  libSystem.B.dylib (1281) <1DD1BCD2-2C85-3B81-8CAF-224FB042F441> /usr/lib/libSystem.B.dylib
    0x7fff60c4a000 -     0x7fff60c4bfff  libThaiTokenizer.dylib (3) <22582C9C-3D32-3832-8925-813E4F2BA8DA> /usr/lib/libThaiTokenizer.dylib
    0x7fff60c63000 -     0x7fff60c79fff  libapple_nghttp2.dylib (1.39.2) <9B990E6A-D9EB-3F2C-B7CA-085A47D4BC62> /usr/lib/libapple_nghttp2.dylib
    0x7fff60cae000 -     0x7fff60d20ff7  libarchive.2.dylib (72.40.2) <25C00824-621A-3FF1-9B6C-52999B6DDF4E> /usr/lib/libarchive.2.dylib
    0x7fff60d21000 -     0x7fff60db7fc5  libate.dylib (2.0.9) <53750831-1A8E-3AF3-A22D-53C08F9D7002> /usr/lib/libate.dylib
    0x7fff60dbb000 -     0x7fff60dbbff3  libauto.dylib (187) <F4B3519A-A4FC-30E0-805C-70C99BA3FDDA> /usr/lib/libauto.dylib
    0x7fff60e79000 -     0x7fff60e89fff  libbsm.0.dylib (60) <E57A0CC6-226D-3529-A23A-D5DD6674DB3E> /usr/lib/libbsm.0.dylib
    0x7fff60e8a000 -     0x7fff60e96fff  libbz2.1.0.dylib (44) <F3D26C17-BC6E-3A83-A3BB-137343C87303> /usr/lib/libbz2.1.0.dylib
    0x7fff60e97000 -     0x7fff60eeafff  libc++.1.dylib (800.7) <1D42387D-206A-3F06-9B5F-705B83EAC295> /usr/lib/libc++.1.dylib
    0x7fff60eeb000 -     0x7fff60efffff  libc++abi.dylib (800.7) <D89ABFBF-3754-35AB-BAEE-FBF14857F79B> /usr/lib/libc++abi.dylib
    0x7fff60f00000 -     0x7fff60f00ffb  libcharset.1.dylib (59) <EC5B95D9-388B-3351-9192-CD6CDB8C3E0F> /usr/lib/libcharset.1.dylib
    0x7fff60f01000 -     0x7fff60f12ffb  libcmph.dylib (8) <49C8E101-945E-369B-91D3-2129000DFF35> /usr/lib/libcmph.dylib
    0x7fff60f13000 -     0x7fff60f2afe7  libcompression.dylib (87) <77B35FFD-CE66-3CCA-BEDD-9771D698CEE3> /usr/lib/libcompression.dylib
    0x7fff611f7000 -     0x7fff6120dfff  libcoretls.dylib (167) <4F054E37-783A-3FCD-B90B-23A0A83621D9> /usr/lib/libcoretls.dylib
    0x7fff6120e000 -     0x7fff6120fffb  libcoretls_cfhelpers.dylib (167) <62E31BC8-A823-3816-B130-2BB550433203> /usr/lib/libcoretls_cfhelpers.dylib
    0x7fff613b2000 -     0x7fff614acfff  libcrypto.35.dylib (47.11.1) <BE850B43-B562-38AD-9A0B-EBDAD26B9875> /usr/lib/libcrypto.35.dylib
    0x7fff616b3000 -     0x7fff617b7fe7  libcrypto.44.dylib (47.11.1) <7607262D-CEFA-3B52-A07E-7DC7904F9BD8> /usr/lib/libcrypto.44.dylib
    0x7fff617ba000 -     0x7fff617c5ff7  libcsfde.dylib (551) <0A7CE4E1-45F7-3C3E-A092-EAB17818F4A8> /usr/lib/libcsfde.dylib
    0x7fff617cd000 -     0x7fff6182cfff  libcups.2.dylib (483) <38F989F6-5143-3D01-9F41-3B34553B68F0> /usr/lib/libcups.2.dylib
    0x7fff6182e000 -     0x7fff61895fff  libcurl.4.dylib (118) <F75E40BA-8DA6-39E7-BDFE-C9F4823BF5E0> /usr/lib/libcurl.4.dylib
    0x7fff61938000 -     0x7fff61938ff3  libenergytrace.dylib (21) <1CE2BD78-F68E-36A3-BCE9-E9EAB78D9FF3> /usr/lib/libenergytrace.dylib
    0x7fff61939000 -     0x7fff61952ff7  libexpat.1.dylib (19) <E209623A-A410-3749-AD6D-2850241CB873> /usr/lib/libexpat.1.dylib
    0x7fff61960000 -     0x7fff61962ff7  libfakelink.dylib (149) <528A0ABE-B583-3DA1-8E5B-9CA7E89303DE> /usr/lib/libfakelink.dylib
    0x7fff61971000 -     0x7fff61976fff  libgermantok.dylib (24) <5E297121-22A7-3A2F-92B9-DD3E5C829CC7> /usr/lib/libgermantok.dylib
    0x7fff61977000 -     0x7fff61980ff7  libheimdal-asn1.dylib (564.40.3) <6C5102F7-85BE-34E0-BFC7-0569FCAE2755> /usr/lib/libheimdal-asn1.dylib
    0x7fff61981000 -     0x7fff61a71ff7  libiconv.2.dylib (59) <EB71AC8F-EA44-3BEE-A210-2D92251CA51D> /usr/lib/libiconv.2.dylib
    0x7fff61a72000 -     0x7fff61ccaff7  libicucore.A.dylib (64243.0.1) <4CBF52D7-7235-34C8-9FF1-8657076B604F> /usr/lib/libicucore.A.dylib
    0x7fff61ce4000 -     0x7fff61ce5fff  liblangid.dylib (133) <DCC4FA36-0563-3BD2-AE35-9BAF52F5BD98> /usr/lib/liblangid.dylib
    0x7fff61ce6000 -     0x7fff61cfeffb  liblzma.5.dylib (16) <7D2522C8-8CBE-32C9-8743-A8F598602F4C> /usr/lib/liblzma.5.dylib
    0x7fff61d16000 -     0x7fff61dbdfff  libmecab.dylib (883) <FDA0E623-F6F2-3402-B72C-0C60A32C2CC1> /usr/lib/libmecab.dylib
    0x7fff61dbe000 -     0x7fff6201eff9  libmecabra.dylib (883) <2E84458F-5748-3A9B-94F3-CAF3C79E6383> /usr/lib/libmecabra.dylib
    0x7fff6238a000 -     0x7fff623b9ff7  libncurses.5.4.dylib (57) <7115BD9E-9A53-3538-BA7C-6D71E8C0F9F1> /usr/lib/libncurses.5.4.dylib
    0x7fff624e8000 -     0x7fff6295aff4  libnetwork.dylib (1880.40.26) <D8C5B7F0-04D5-3470-A9C4-EF8B2FF96986> /usr/lib/libnetwork.dylib
    0x7fff629f9000 -     0x7fff62a2aff6  libobjc.A.dylib (781) <D866A31E-5CB1-3327-8D22-C4F83C9225D0> /usr/lib/libobjc.A.dylib
    0x7fff62a2b000 -     0x7fff62a2cff7  libodfde.dylib (26) <104DFC2F-ACCF-321A-974D-734E19056B21> /usr/lib/libodfde.dylib
    0x7fff62a3d000 -     0x7fff62a41fff  libpam.2.dylib (25) <02ABA04D-5843-3850-82A3-EBECA6FC2CDF> /usr/lib/libpam.2.dylib
    0x7fff62a44000 -     0x7fff62a77ff7  libpcap.A.dylib (89.40.2) <C4F9F5BD-BA21-3038-9665-4D298FB7511C> /usr/lib/libpcap.A.dylib
    0x7fff62af9000 -     0x7fff62b11fff  libresolv.9.dylib (67.40.1) <34848168-B77D-3749-A7ED-B1F3F92E5162> /usr/lib/libresolv.9.dylib
    0x7fff62b13000 -     0x7fff62b57ff7  libsandbox.1.dylib (1217.41.1) <EAC4CA6F-6527-373C-8AD8-F8F1B590B54B> /usr/lib/libsandbox.1.dylib
    0x7fff62b58000 -     0x7fff62b6afff  libsasl2.2.dylib (213) <FA0CF2A0-1989-3CCF-8118-45017132788B> /usr/lib/libsasl2.2.dylib
    0x7fff62b6b000 -     0x7fff62b6cff7  libspindump.dylib (281.1) <D330C232-51A7-3943-87EB-FAEA3C9352DC> /usr/lib/libspindump.dylib
    0x7fff62b6d000 -     0x7fff62d5aff7  libsqlite3.dylib (308.4) <2D0B1BE5-9B8A-394F-82F7-F612B1A6C73F> /usr/lib/libsqlite3.dylib
    0x7fff62e4e000 -     0x7fff62e7bffb  libssl.46.dylib (47.11.1) <37B2EA03-9748-3324-ADDD-75F67D1E9D15> /usr/lib/libssl.46.dylib
    0x7fff62fab000 -     0x7fff62faeffb  libutil.dylib (57) <B88D4C21-DAEF-3566-8EAE-5973C51A16FD> /usr/lib/libutil.dylib
    0x7fff62faf000 -     0x7fff62fbcfff  libxar.1.dylib (420) <46AAA43E-6FC6-38A8-B696-62143706D33B> /usr/lib/libxar.1.dylib
    0x7fff62fc2000 -     0x7fff630a4ff7  libxml2.2.dylib (32.12) <0DB777D9-F9A1-3921-BFCE-05A000293915> /usr/lib/libxml2.2.dylib
    0x7fff630a8000 -     0x7fff630d0fff  libxslt.1.dylib (16.7) <C30A840F-E7E7-39D5-A633-9C256650B552> /usr/lib/libxslt.1.dylib
    0x7fff630d1000 -     0x7fff630e3fff  libz.1.dylib (76) <3EC7A143-AF2D-35EE-9C08-542B2907E3D2> /usr/lib/libz.1.dylib
    0x7fff63b49000 -     0x7fff63b4eff7  libcache.dylib (83) <74F6459D-3606-3ADB-9808-F6B0FE70062D> /usr/lib/system/libcache.dylib
    0x7fff63b4f000 -     0x7fff63b5aff7  libcommonCrypto.dylib (60165) <1333752F-5117-3E86-803A-06E166D80C8C> /usr/lib/system/libcommonCrypto.dylib
    0x7fff63b5b000 -     0x7fff63b62fff  libcompiler_rt.dylib (101.2) <0437EBEF-8191-3912-A365-D6BB75C7A810> /usr/lib/system/libcompiler_rt.dylib
    0x7fff63b63000 -     0x7fff63b6cfff  libcopyfile.dylib (166.40.1) <7FAF372E-BAD5-30E6-A8F2-A3D06B91DC80> /usr/lib/system/libcopyfile.dylib
    0x7fff63b6d000 -     0x7fff63c04fef  libcorecrypto.dylib (866.40.8) <AE25C9EE-5D63-3E49-B3AA-D482D35C085A> /usr/lib/system/libcorecrypto.dylib
    0x7fff63d1b000 -     0x7fff63d5cff0  libdispatch.dylib (1173.40.5) <1FF421B6-4BF0-3B5F-8F56-5ED3B3EFE06F> /usr/lib/system/libdispatch.dylib
    0x7fff63d5d000 -     0x7fff63d92fff  libdyld.dylib (733.6) <2FA4B359-624B-337C-9207-CDCF841C2E52> /usr/lib/system/libdyld.dylib
    0x7fff63d93000 -     0x7fff63d93ffb  libkeymgr.dylib (30) <7EEF9246-30B4-34DD-8AD6-79679D1A7784> /usr/lib/system/libkeymgr.dylib
    0x7fff63d94000 -     0x7fff63da0ff7  libkxld.dylib (6153.41.3) <F9FF90CE-DCB0-3918-882F-6E475A6E244A> /usr/lib/system/libkxld.dylib
    0x7fff63da1000 -     0x7fff63da1ff7  liblaunch.dylib (1738.40.10) <CC02D5B3-A95D-3B16-8EE5-D62521CFE899> /usr/lib/system/liblaunch.dylib
    0x7fff63da2000 -     0x7fff63da7ff7  libmacho.dylib (949.0.1) <6C3E49B2-594D-3B9D-82DB-C4ABEB9788AB> /usr/lib/system/libmacho.dylib
    0x7fff63da8000 -     0x7fff63daaff3  libquarantine.dylib (110.40.3) <A1BCAA32-A194-3DBE-9930-8F49A4AEF284> /usr/lib/system/libquarantine.dylib
    0x7fff63dab000 -     0x7fff63dacff7  libremovefile.dylib (48) <DD7AE862-F179-3C07-A4FC-5775DDD4D3E6> /usr/lib/system/libremovefile.dylib
    0x7fff63dad000 -     0x7fff63dc4fff  libsystem_asl.dylib (377.40.1) <ECE44856-D279-3B5D-A0AA-8BE421D200C4> /usr/lib/system/libsystem_asl.dylib
    0x7fff63dc5000 -     0x7fff63dc5fff  libsystem_blocks.dylib (74) <DC521115-905A-3A0D-9337-C55FACCEA85F> /usr/lib/system/libsystem_blocks.dylib
    0x7fff63dc6000 -     0x7fff63e4dff7  libsystem_c.dylib (1353.41.1) <5AD50779-955E-3F56-BCB9-1E14833B3455> /usr/lib/system/libsystem_c.dylib
    0x7fff63e4e000 -     0x7fff63e51fff  libsystem_configuration.dylib (1061.40.2) <7A2329E0-3C84-3DB7-BC32-E7796C50D621> /usr/lib/system/libsystem_configuration.dylib
    0x7fff63e52000 -     0x7fff63e55ff7  libsystem_coreservices.dylib (114) <DF341577-A307-3722-BB24-D4AACEAB19B3> /usr/lib/system/libsystem_coreservices.dylib
    0x7fff63e56000 -     0x7fff63e5dfff  libsystem_darwin.dylib (1353.41.1) <E862B5B1-A367-39CA-8319-B2F9DFADF606> /usr/lib/system/libsystem_darwin.dylib
    0x7fff63e5e000 -     0x7fff63e65ffb  libsystem_dnssd.dylib (1096.40.7) <2A9C6F3E-427B-332E-BDD3-D4651306F3DE> /usr/lib/system/libsystem_dnssd.dylib
    0x7fff63e66000 -     0x7fff63e67ffb  libsystem_featureflags.dylib (17) <B94C0052-B75A-3169-80AA-5F480588AF6E> /usr/lib/system/libsystem_featureflags.dylib
    0x7fff63e68000 -     0x7fff63eb5ff7  libsystem_info.dylib (538) <18CC56C5-5325-3375-BF99-FAE7F4F19DDD> /usr/lib/system/libsystem_info.dylib
    0x7fff63eb6000 -     0x7fff63ee2ff7  libsystem_kernel.dylib (6153.41.3) <18918E9C-45BC-3D5A-A6B6-3DBC60EEE2E1> /usr/lib/system/libsystem_kernel.dylib
    0x7fff63ee3000 -     0x7fff63f2aff7  libsystem_m.dylib (3178) <636A1A1C-7AFC-3E82-B86B-0173912A3437> /usr/lib/system/libsystem_m.dylib
    0x7fff63f2b000 -     0x7fff63f52ff7  libsystem_malloc.dylib (283.40.1) <F82A587B-44A2-3699-A218-9D3ECEE23D5A> /usr/lib/system/libsystem_malloc.dylib
    0x7fff63f53000 -     0x7fff63f60ff3  libsystem_networkextension.dylib (1095.40.22) <7F206A43-A941-3BAB-AE3A-16169F2FE6AB> /usr/lib/system/libsystem_networkextension.dylib
    0x7fff63f61000 -     0x7fff63f6afff  libsystem_notify.dylib (241) <C95CC58E-35E7-3828-AA2A-6EED73C12DE5> /usr/lib/system/libsystem_notify.dylib
    0x7fff63f6b000 -     0x7fff63f74fe7  libsystem_platform.dylib (220) <0CCDD81F-0891-3400-8A97-6CAC3BBBE2F9> /usr/lib/system/libsystem_platform.dylib
    0x7fff63f75000 -     0x7fff63f7fff7  libsystem_pthread.dylib (416.40.3) <53C65598-9E9E-36FF-BDC2-74F228E58C5C> /usr/lib/system/libsystem_pthread.dylib
    0x7fff63f80000 -     0x7fff63f84ffb  libsystem_sandbox.dylib (1217.41.1) <2183D15E-2CFD-3160-80CE-A948F0529005> /usr/lib/system/libsystem_sandbox.dylib
    0x7fff63f85000 -     0x7fff63f87fff  libsystem_secinit.dylib (62.40.2) <D2782294-ACDC-30FF-A794-B4C1B324526B> /usr/lib/system/libsystem_secinit.dylib
    0x7fff63f88000 -     0x7fff63f8fffb  libsystem_symptoms.dylib (1238.40.4) <A44E4405-E22E-32E9-83DE-8C7A82401DA0> /usr/lib/system/libsystem_symptoms.dylib
    0x7fff63f90000 -     0x7fff63fa6ff2  libsystem_trace.dylib (1147.40.13) <376CC435-E656-37D9-A5FF-C49B6E4525E2> /usr/lib/system/libsystem_trace.dylib
    0x7fff63fa8000 -     0x7fff63fadffb  libunwind.dylib (35.4) <44448F1F-08E5-3425-ADBA-C38A9E8F90C7> /usr/lib/system/libunwind.dylib
    0x7fff63fae000 -     0x7fff63fe2ff6  libxpc.dylib (1738.40.10) <99CC9436-D653-3762-ADBB-9054EBD1BA2B> /usr/lib/system/libxpc.dylib

External Modification Summary:
  Calls made by other processes targeting this process:
    task_for_pid: 17
    thread_create: 0
    thread_set_state: 0
  Calls made by this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by all processes on this machine:
    task_for_pid: 1115654
    thread_create: 0
    thread_set_state: 0

VM Region Summary:
ReadOnly portion of Libraries: Total=670.6M resident=0K(0%) swapped_out_or_unallocated=670.6M(100%)
Writable regions: Total=2.5G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=2.5G(100%)
 
                                VIRTUAL   REGION 
REGION TYPE                        SIZE    COUNT (non-coalesced) 
===========                     =======  ======= 
Accelerate framework               384K        3 
Activity Tracing                   256K        1 
CG backing stores                  664K        2 
CoreGraphics                         8K        1 
CoreImage                            8K        2 
CoreUI image data                   44K        1 
Foundation                           4K        1 
JS JIT generated code                4K        1 
JS VM register file               8192K        3 
Kernel Alloc Once                    8K        1 
MALLOC                           961.4M      115 
MALLOC guard page                   48K        9 
MALLOC_MEDIUM (reserved)           1.4G       13         reserved VM address space (unallocated)
Memory Tag 242                      12K        1 
OpenGL GLSL                        256K        3 
STACK GUARD                       56.1M       27 
Stack                             88.7M       27 
VM_ALLOCATE                       6364K      185 
VM_ALLOCATE (reserved)               8K        1         reserved VM address space (unallocated)
WebAssembly memory                16.0M        4 
__DATA                            46.7M      367 
__DATA_CONST                        80K        2 
__FONT_DATA                          4K        1 
__GLSLBUILTINS                    5176K        1 
__LINKEDIT                       363.4M       45 
__OBJC_RO                         32.0M        1 
__OBJC_RW                         1780K        2 
__TEXT                           307.2M      357 
__UNICODE                          564K        1 
mapped file                      592.9M      384 
shared memory                      660K       20 
===========                     =======  ======= 
TOTAL                              3.8G     1582 
TOTAL, minus reserved VM space     2.4G     1582 

Model: MacBookPro15,3, BootROM 1037.40.124.0.0 (iBridge: 17.16.11081.0.0,0), 8 processors, 8-Core Intel Core i9, 2.4 GHz, 32 GB, SMC 
Graphics: kHW_IntelUHDGraphics630Item, Intel UHD Graphics 630, spdisplays_builtin
Graphics: kHW_AMDRadeonProVega20Item, Radeon Pro Vega 20, spdisplays_pcie_device, 4 GB
Memory Module: BANK 0/ChannelA-DIMM0, 16 GB, DDR4, 2400 MHz, SK Hynix, -
Memory Module: BANK 2/ChannelB-DIMM0, 16 GB, DDR4, 2400 MHz, SK Hynix, -
AirPort: spairport_wireless_card_type_airport_extreme (0x14E4, 0x7BF), wl0: Oct 19 2019 15:33:10 version 9.113.2.0.32.5.39 FWID 01-5eb3e1fa
Bluetooth: Version 7.0.1f1, 3 services, 27 devices, 1 incoming serial ports
Network Service: Wi-Fi, AirPort, en0
PCI Card: pci1b73,1100, sppci_usbxhci, Thunderbolt@196,0,0
PCI Card: pci1b21,612, sppci_ahci, Thunderbolt@195,0,0
PCI Card: ethernet, sppci_ethernet, Thunderbolt@197,0,0
USB Device: USB 3.1 Bus
USB Device: USB 3.0 Bus
USB Device: USB audio CODEC
USB Device: Hub
USB Device: Composite Device
USB Device: C922 Pro Stream Webcam
USB Device: General Purpose USB Hub
USB Device: SteelSeries Siberia 800
USB Device: SteelSeries Siberia 800
USB Device: Keyboard Hub
USB Device: Razer DeathAdder
USB Device: Apple Keyboard
USB Device: Apple T2 Bus
USB Device: Touch Bar Backlight
USB Device: Touch Bar Display
USB Device: Apple Internal Keyboard / Trackpad
USB Device: Headset
USB Device: Ambient Light Sensor
USB Device: FaceTime HD Camera (Built-in)
USB Device: Apple T2 Controller
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.3
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.3
Thunderbolt Device: TS3, CalDigit, Inc., 3, 23.1


# Discussion History
## selsta | 2019-11-24T19:51:02+00:00
Any tips to reproduce this? Just letting the GUI run in background?

## ericmnel | 2019-11-24T19:54:23+00:00
Here is what I did:

1. I had Monero v14 synced up with wallet A that has coins in it
2. Download Monero v15, replace executable
3. Lanched Monero v15, clicked cancel to prevent opening wallet A, created a new wallet B instead
4. Left it running in the background with wallet B until it crashed

## dEBRUYNE-1 | 2019-11-24T21:47:59+00:00
Can you check whether extracting the `.tar.bz2` to a fresh directory makes any difference? 

## ericmnel | 2019-11-25T04:17:45+00:00
I moved the .tar.bz2 to my desktop, extracted it there, and ran that executable.  Still crashes after a few hours.

## rating89us | 2019-11-25T05:53:38+00:00
I confirm Windows version is also crashing. I had 3 crashes in 2 days.

## xiphon | 2019-11-25T05:57:43+00:00
Investigating the issue. According to the stack trace, it looks like a use-after-free bug. Will be non-trivial to catch and fix this one.

## juazki | 2019-11-30T14:45:47+00:00
Same thing here in Ubuntu 18.04, command line shows:

> Segmentation fault (core dumped)

Several crashes in the last few days. 


# Action History
- Created by: ericmnel | 2019-11-24T19:47:23+00:00
- Closed at: 2019-12-23T14:05:19+00:00
