---
title: App Keeps Crashing When Try to Open it, and my funds are now currently locked.
  Memory error?
source_url: https://github.com/monero-project/monero-gui/issues/3157
author: alexwolf22
assignees: []
labels: []
created_at: '2020-10-15T01:25:49+00:00'
updated_at: '2024-10-20T10:56:39+00:00'
type: issue
status: closed
closed_at: '2020-10-15T03:55:25+00:00'
---

# Original Description
Hello,

I just installed and downloaded the Moreno wallet yesterday. I deposited some funds into it and sent a transaction which was never getting confirmed, and was up for 12 hours.

After some research, I saw that I should update the GUI it to the newer version to fix the issue.

Now each time I open the desktop app and enter my wallet passcode the app crashes and I get this error message.

Would be great if you can help me figure out what's going on here because I have a fair amount of funds in that wallet and would hate to see it disappear.

I do see this one error which may the culprit. I'm not a C/C#/C++ guy so unsure how to debug this further.

```
3   com.apple.driver.AppleIntelKBLGraphicsGLDriver	0x00007fff25d94d50 llvm::report_bad_alloc_error(char const*, bool) (.cold.1) + 64
4   com.apple.driver.AppleIntelKBLGraphicsGLDriver	0x00007fff25c1824a llvm::report_bad_alloc_error(char const*, bool) + 74
5   com.apple.driver.AppleIntelKBLGraphicsGLDriver	0x00007fff25c18355 out_of_memory_new_handler() + 21
```

Let me know thanks for the help.

Cheers,
Alex


Logs
=====
Process:               monero-wallet-gui [1931]
Path:                  /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
Identifier:            org.monero-project.monero-wallet-gui
Version:               0.17.1.0 (???)
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           monero-wallet-gui [1931]
User ID:               501

Date/Time:             2020-10-14 20:14:41.718 -0500
OS Version:            Mac OS X 10.15.5 (19F101)
Report Version:        12
Bridge OS Version:     4.5 (17P5300)
Anonymous UUID:        DD8B03AD-212B-4E58-E34B-BA7FCB07E8ED


Time Awake Since Boot: 350 seconds

System Integrity Protection: enabled

Crashed Thread:        22  Thread (pooled)

Exception Type:        EXC_CRASH (SIGABRT)
Exception Codes:       0x0000000000000000, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Application Specific Information:
abort() called

Thread 0:: Dispatch queue: com.apple.main-thread
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.qt-project.QtCore         	0x00000001030dba4b 0x1030b1000 + 174667
3   org.qt-project.QtCore         	0x00000001030db9ac QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108
4   org.qt-project.QtQuick        	0x0000000101cc6afb 0x101bfc000 + 830203
5   org.qt-project.QtQuick        	0x0000000101cc71c2 0x101bfc000 + 831938
6   org.qt-project.QtQuick        	0x0000000101d1e5d6 QQuickWindow::event(QEvent*) + 774
7   org.qt-project.QtWidgets      	0x000000010244d70d QApplicationPrivate::notify_helper(QObject*, QEvent*) + 269
8   org.qt-project.QtWidgets      	0x000000010244eb12 QApplication::notify(QObject*, QEvent*) + 594
9   org.qt-project.QtCore         	0x000000010329b4c4 QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
10  org.qt-project.QtGui          	0x0000000102a193d5 QPlatformWindow::deliverUpdateRequest() + 69
11  libqcocoa.dylib               	0x0000000103e54003 0x103e34000 + 131075
12  libqcocoa.dylib               	0x0000000103e42273 0x103e34000 + 57971
13  libdispatch.dylib             	0x00007fff675d1658 _dispatch_client_callout + 8
14  libdispatch.dylib             	0x00007fff675d3818 _dispatch_continuation_pop + 414
15  libdispatch.dylib             	0x00007fff675e34be _dispatch_source_invoke + 2084
16  libdispatch.dylib             	0x00007fff675dcb6d _dispatch_main_queue_callback_4CF + 618
17  com.apple.CoreFoundation      	0x00007fff2d644f11 __CFRUNLOOP_IS_SERVICING_THE_MAIN_DISPATCH_QUEUE__ + 9
18  com.apple.CoreFoundation      	0x00007fff2d604d17 __CFRunLoopRun + 2028
19  com.apple.CoreFoundation      	0x00007fff2d603ece CFRunLoopRunSpecific + 462
20  com.apple.HIToolbox           	0x00007fff2c232abd RunCurrentEventLoopInMode + 292
21  com.apple.HIToolbox           	0x00007fff2c2327d5 ReceiveNextEventCommon + 584
22  com.apple.HIToolbox           	0x00007fff2c232579 _BlockUntilNextEventMatchingListInModeWithFilter + 64
23  com.apple.AppKit              	0x00007fff2a87a829 _DPSNextEvent + 883
24  com.apple.AppKit              	0x00007fff2a879070 -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1352
25  com.apple.AppKit              	0x00007fff2a86ad7e -[NSApplication run] + 658
26  libqcocoa.dylib               	0x0000000103e69de3 0x103e34000 + 220643
27  org.qt-project.QtCore         	0x0000000103296adf QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 431
28  org.qt-project.QtCore         	0x000000010329bad2 QCoreApplication::exec() + 130
29  org.monero-project.monero-wallet-gui	0x0000000100716674 main + 14228
30  libdyld.dylib                 	0x00007fff6762acc9 start + 1

Thread 1:: QQmlThread
0   libsystem_kernel.dylib        	0x00007fff677723d6 poll + 10
1   org.qt-project.QtCore         	0x00000001032f1830 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 608
2   org.qt-project.QtCore         	0x00000001032f3027 QEventDispatcherUNIX::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) + 903
3   org.qt-project.QtCore         	0x0000000103296adf QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 431
4   org.qt-project.QtCore         	0x00000001030d22dc QThread::exec() + 140
5   org.qt-project.QtQml          	0x000000010228a2f9 0x102003000 + 2650873
6   org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
7   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
8   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 2:: QQuickXmlQueryEngine
0   libsystem_kernel.dylib        	0x00007fff677723d6 poll + 10
1   org.qt-project.QtCore         	0x00000001032f1830 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 608
2   org.qt-project.QtCore         	0x00000001032f3027 QEventDispatcherUNIX::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) + 903
3   org.qt-project.QtCore         	0x0000000103296adf QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 431
4   org.qt-project.QtCore         	0x00000001030d22dc QThread::exec() + 140
5   libqmlxmllistmodelplugin.dylib	0x000000010a9bb55a 0x10a9b7000 + 17754
6   org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
7   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
8   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 3:: Qt bearer thread
0   libsystem_kernel.dylib        	0x00007fff677723d6 poll + 10
1   org.qt-project.QtCore         	0x00000001032f1830 qt_safe_poll(pollfd*, unsigned int, timespec const*) + 608
2   org.qt-project.QtCore         	0x00000001032f3027 QEventDispatcherUNIX::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) + 903
3   org.qt-project.QtCore         	0x0000000103296adf QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 431
4   org.qt-project.QtCore         	0x00000001030d22dc QThread::exec() + 140
5   org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
6   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
7   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 4:: com.apple.CFSocket.private
0   libsystem_kernel.dylib        	0x00007fff677740fe __select + 10
1   com.apple.CoreFoundation      	0x00007fff2d62ece3 __CFSocketManager + 641
2   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
3   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 5:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 6:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 7:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 8:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 9:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 10:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 11:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 12:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 13:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 14:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 15:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100784dab 0x1006b0000 + 871851
3   org.monero-project.monero-wallet-gui	0x0000000100af2f0b tools::threadpool::run(bool) + 299
4   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
5   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
6   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 16:: QSGRenderThread
0   libsystem_kernel.dylib        	0x00007fff6776bdfa mach_msg_trap + 10
1   libsystem_kernel.dylib        	0x00007fff6776c170 mach_msg + 60
2   com.apple.framework.IOKit     	0x00007fff303787d3 io_connect_method + 383
3   com.apple.framework.IOKit     	0x00007fff3037862c IOConnectCallMethod + 244
4   com.apple.framework.IOKit     	0x00007fff30379464 IOConnectCallStructMethod + 35
5   com.apple.IOAccelerator       	0x00007fff5228dedf IOAccelContextSubmitDataBuffersExt2 + 253
6   libGPUSupportMercury.dylib    	0x00007fff4ea1a53f gpusSubmitDataBuffers + 136
7   com.apple.AMDRadeonX4000GLDriver	0x000000010b717dc7 glrATI_Hwl_SubmitPacketsWithToken + 91
8   com.apple.AMDRadeonX4000GLDriver	0x000000010b76fa82 gldPresentFramebufferData + 83
9   GLEngine                      	0x00007fff381258d1 glSwap_Exec + 97
10  com.apple.opengl              	0x00007fff38107473 CGLFlushDrawable + 59
11  com.apple.AppKit              	0x00007fff2ac24f2a -[NSOpenGLContext flushBuffer] + 20
12  libqcocoa.dylib               	0x0000000103e8ad3d 0x103e34000 + 355645
13  org.qt-project.QtGui          	0x0000000102a6baec QOpenGLContext::swapBuffers(QSurface*) + 412
14  org.qt-project.QtQuick        	0x0000000101cc4309 0x101bfc000 + 819977
15  org.qt-project.QtQuick        	0x0000000101cc4c5c 0x101bfc000 + 822364
16  org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
17  libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
18  libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 17:: com.apple.NSEventThread
0   libsystem_kernel.dylib        	0x00007fff6776bdfa mach_msg_trap + 10
1   libsystem_kernel.dylib        	0x00007fff6776c170 mach_msg + 60
2   com.apple.CoreFoundation      	0x00007fff2d605f85 __CFRunLoopServiceMachPort + 247
3   com.apple.CoreFoundation      	0x00007fff2d604a52 __CFRunLoopRun + 1319
4   com.apple.CoreFoundation      	0x00007fff2d603ece CFRunLoopRunSpecific + 462
5   com.apple.AppKit              	0x00007fff2aa1c144 _NSEventThread + 132
6   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
7   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 18:: FileInfoThread
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.qt-project.QtCore         	0x00000001030dba4b 0x1030b1000 + 174667
3   org.qt-project.QtCore         	0x00000001030db9ac QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108
4   libqmlfolderlistmodelplugin.dylib	0x000000010ada6d23 0x10ad9e000 + 36131
5   org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
6   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
7   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 19:
0   libsystem_pthread.dylib       	0x00007fff6782ab68 start_wqthread + 0

Thread 20:
0   libsystem_pthread.dylib       	0x00007fff6782ab68 start_wqthread + 0

Thread 21:: Thread (pooled)
0   libcrypto.1.1.dylib           	0x00000001019e1f4b BN_mod_word + 112
1   libcrypto.1.1.dylib           	0x00000001019df35a BN_generate_prime_ex + 948
2   libcrypto.1.1.dylib           	0x0000000101abbfb1 RSA_generate_multi_prime_key + 1061
3   org.monero-project.monero-wallet-gui	0x0000000100c6bc50 epee::net_utils::create_rsa_ssl_certificate(evp_pkey_st*&, x509_st*&) + 592
4   org.monero-project.monero-wallet-gui	0x0000000100c6df71 epee::net_utils::ssl_options_t::create_context() const + 3521
5   org.monero-project.monero-wallet-gui	0x00000001006d82e2 0x1006b0000 + 164578
6   org.monero-project.monero-wallet-gui	0x00000001006c37b1 0x1006b0000 + 79793
7   org.monero-project.monero-wallet-gui	0x0000000100c3d8a0 epee::net_utils::http::abstract_http_client::set_server(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, boost::optional<epee::net_utils::http::login>, epee::net_utils::ssl_options_t) + 528
8   org.monero-project.monero-wallet-gui	0x000000010079a511 Monero::WalletManagerImpl::setDaemonAddress(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&) + 97
9   org.monero-project.monero-wallet-gui	0x0000000100744de3 0x1006b0000 + 609763
10  org.monero-project.monero-wallet-gui	0x000000010074fe00 0x1006b0000 + 654848
11  org.monero-project.monero-wallet-gui	0x000000010074fd2e 0x1006b0000 + 654638
12  org.qt-project.QtCore         	0x00000001030d81ed 0x1030b1000 + 160237
13  org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
14  libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
15  libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 22 Crashed:: Thread (pooled)
0   libsystem_kernel.dylib        	0x00007fff6777233a __pthread_kill + 10
1   libsystem_pthread.dylib       	0x00007fff6782ee60 pthread_kill + 430
2   libsystem_c.dylib             	0x00007fff676f9808 abort + 120
3   com.apple.driver.AppleIntelKBLGraphicsGLDriver	0x00007fff25d94d50 llvm::report_bad_alloc_error(char const*, bool) (.cold.1) + 64
4   com.apple.driver.AppleIntelKBLGraphicsGLDriver	0x00007fff25c1824a llvm::report_bad_alloc_error(char const*, bool) + 74
5   com.apple.driver.AppleIntelKBLGraphicsGLDriver	0x00007fff25c18355 out_of_memory_new_handler() + 21
6   libc++abi.dylib               	0x00007fff6495adfb operator new(unsigned long) + 43
7   libc++.1.dylib                	0x00007fff6492e491 std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >::__grow_by(unsigned long, unsigned long, unsigned long, unsigned long, unsigned long, unsigned long) + 139
8   libc++.1.dylib                	0x00007fff6492df9c std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >::append(unsigned long, char) + 112
9   libc++.1.dylib                	0x00007fff6492df0b std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >::resize(unsigned long, char) + 39
10  libboost_serialization-mt.dylib	0x0000000101887ff0 boost::archive::basic_binary_iprimitive<boost::archive::binary_iarchive, char, std::__1::char_traits<char> >::load(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&) + 80
11  libboost_serialization-mt.dylib	0x0000000101888f89 boost::archive::basic_binary_iarchive<boost::archive::binary_iarchive>::init() + 73
12  org.monero-project.monero-wallet-gui	0x0000000100982a71 0x1006b0000 + 2959985
13  org.monero-project.monero-wallet-gui	0x000000010080d181 tools::wallet2::load(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, epee::wipeable_string const&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&) + 14465
14  org.monero-project.monero-wallet-gui	0x000000010076cbe5 Monero::WalletImpl::open(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&) + 453
15  org.monero-project.monero-wallet-gui	0x0000000100798d79 Monero::WalletManagerImpl::openWallet(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, Monero::NetworkType, unsigned long long, Monero::WalletListener*) + 105
16  org.monero-project.monero-wallet-gui	0x000000010073f3cc WalletManager::openWallet(QString const&, QString const&, NetworkType::Type, unsigned long long) + 700
17  org.monero-project.monero-wallet-gui	0x00000001007446d2 0x1006b0000 + 607954
18  org.monero-project.monero-wallet-gui	0x000000010074fe00 0x1006b0000 + 654848
19  org.monero-project.monero-wallet-gui	0x000000010074fd2e 0x1006b0000 + 654638
20  org.qt-project.QtCore         	0x00000001030d81ed 0x1030b1000 + 160237
21  org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
22  libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
23  libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 23:: Thread (pooled)
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.qt-project.QtCore         	0x00000001030dbd7f 0x1030b1000 + 175487
3   org.qt-project.QtCore         	0x00000001030dba6e 0x1030b1000 + 174702
4   org.qt-project.QtCore         	0x00000001030db9ac QWaitCondition::wait(QMutex*, QDeadlineTimer) + 108
5   org.qt-project.QtCore         	0x00000001030db90e QWaitCondition::wait(QMutex*, unsigned long) + 62
6   org.qt-project.QtCore         	0x00000001030d83d7 0x1030b1000 + 160727
7   org.qt-project.QtCore         	0x00000001030d3253 0x1030b1000 + 139859
8   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
9   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 24:: CVDisplayLink
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f457 _pthread_cond_wait + 748
2   com.apple.CoreVideo           	0x00007fff2f596d2b CVDisplayLink::waitUntil(unsigned long long) + 229
3   com.apple.CoreVideo           	0x00007fff2f596238 CVDisplayLink::runIOThread() + 482
4   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
5   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 25:
0   libsystem_pthread.dylib       	0x00007fff6782ab68 start_wqthread + 0

Thread 26:
0   libsystem_pthread.dylib       	0x00007fff6782ab68 start_wqthread + 0

Thread 27:
0   libsystem_kernel.dylib        	0x00007fff6776e882 __psynch_cvwait + 10
1   libsystem_pthread.dylib       	0x00007fff6782f425 _pthread_cond_wait + 698
2   org.monero-project.monero-wallet-gui	0x0000000100797dce 0x1006b0000 + 949710
3   org.monero-project.monero-wallet-gui	0x0000000100784ce5 0x1006b0000 + 871653
4   org.monero-project.monero-wallet-gui	0x0000000100783928 Monero::WalletImpl::refreshThreadFunc() + 1256
5   libboost_thread-mt.dylib      	0x00000001017a394f 0x1017a1000 + 10575
6   libsystem_pthread.dylib       	0x00007fff6782f109 _pthread_start + 148
7   libsystem_pthread.dylib       	0x00007fff6782ab8b thread_start + 15

Thread 22 crashed with X86 Thread State (64-bit):
  rax: 0x0000000000000000  rbx: 0x0000700008700000  rcx: 0x00007000086ff218  rdx: 0x0000000000000000
  rdi: 0x000000000000e16f  rsi: 0x0000000000000006  rbp: 0x00007000086ff240  rsp: 0x00007000086ff218
   r8: 0x0000000000004ca1   r9: 0x00007fff836f35a0  r10: 0x0000700008700000  r11: 0x0000000000000246
  r12: 0x000000000000e16f  r13: 0x00007fff836f3588  r14: 0x0000000000000006  r15: 0x0000000000000016
  rip: 0x00007fff6777233a  rfl: 0x0000000000000246  cr2: 0x00000001007e82a0
  
Logical CPU:     0
Error Code:      0x0100001f
Trap Number:     133


Binary Images:
       0x1006b0000 -        0x101371fe3 +org.monero-project.monero-wallet-gui (0.17.1.0 - ???) <0183CD35-9CCF-347B-AC1E-8AEDF89B3B53> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
       0x101728000 -        0x101768fe7 +libsodium.23.dylib (0) <F23799A3-9781-3641-A1F6-A99B3EB35C7C> /Applications/monero-wallet-gui.app/Contents/Frameworks/libsodium.23.dylib
       0x10177e000 -        0x10178fff7 +libboost_filesystem-mt.dylib (0) <47DD59A7-6745-39A8-B989-668BDCEA964D> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_filesystem-mt.dylib
       0x1017a1000 -        0x1017affff +libboost_thread-mt.dylib (0) <8A742B67-41BD-3701-A975-A884E2628F56> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_thread-mt.dylib
       0x1017c3000 -        0x1017c7fff +libboost_chrono-mt.dylib (0) <CD843465-C2D8-3BAB-8430-9639F3396BA0> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_chrono-mt.dylib
       0x1017d7000 -        0x101868ff7 +libboost_regex-mt.dylib (0) <054F85AF-84DC-3314-8444-5BB1D144E524> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_regex-mt.dylib
       0x101882000 -        0x1018a5fff +libboost_serialization-mt.dylib (0) <3E75CEED-0996-36CD-B2F7-F030B48B671D> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_serialization-mt.dylib
       0x1018c5000 -        0x1018fcfff +libboost_program_options-mt.dylib (0) <D9472437-18CB-3959-AFDA-FCF6DC964AE0> /Applications/monero-wallet-gui.app/Contents/Frameworks/libboost_program_options-mt.dylib
       0x101922000 -        0x101971ff3 +libssl.1.1.dylib (0) <AAAD445F-8DBE-3ED8-BA6D-8290FC9410BF> /Applications/monero-wallet-gui.app/Contents/Frameworks/libssl.1.1.dylib
       0x10199e000 -        0x101b60d33 +libcrypto.1.1.dylib (0) <C54CB9D7-BEAF-3FFE-8E11-6A284CF5C30D> /Applications/monero-wallet-gui.app/Contents/Frameworks/libcrypto.1.1.dylib
       0x101bef000 -        0x101bf1fff +libhidapi.0.dylib (0) <1B576F5D-DDF6-3270-9743-282C306D1D84> /Applications/monero-wallet-gui.app/Contents/Frameworks/libhidapi.0.dylib
       0x101bfc000 -        0x101eeaff7 +org.qt-project.QtQuick (5.12 - 5.12.8) <F1F7FBA0-5CC4-3188-AA68-3BCEAD1078CD> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQuick.framework/Versions/5/QtQuick
       0x102003000 -        0x10237cff3 +org.qt-project.QtQml (5.12 - 5.12.8) <21316A43-D7F3-3BB4-82DD-520706403102> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQml.framework/Versions/5/QtQml
       0x10243d000 -        0x10287bff7 +org.qt-project.QtWidgets (5.12 - 5.12.8) <CAC50E2E-DC1C-37F4-8BEF-9953C603230F> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtWidgets.framework/Versions/5/QtWidgets
       0x1029f0000 -        0x102e3efe7 +org.qt-project.QtGui (5.12 - 5.12.8) <6D5A30B0-E836-303B-B20F-BA809ABF7D57> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtGui.framework/Versions/5/QtGui
       0x102f52000 -        0x10305cff7 +org.qt-project.QtNetwork (5.12 - 5.12.8) <2AAC3EE7-771E-3138-9835-E0CA479CBB19> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtNetwork.framework/Versions/5/QtNetwork
       0x1030b1000 -        0x1035e6ff7 +org.qt-project.QtCore (5.12 - 5.12.8) <AB81B515-9C42-3545-B1D2-06E8090C5422> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtCore.framework/Versions/5/QtCore
       0x1036b8000 -        0x10380bfff +libprotobuf.23.dylib (0) <A672131E-58C1-38DA-9561-0E2D1445DF37> /Applications/monero-wallet-gui.app/Contents/Frameworks/libprotobuf.23.dylib
       0x1038ca000 -        0x10395dff3 +libgcrypt.20.dylib (0) <77D20356-BCDD-3210-A0D8-445E3D761152> /Applications/monero-wallet-gui.app/Contents/Frameworks/libgcrypt.20.dylib
       0x10397a000 -        0x103afcfff +libicui18n.66.dylib (0) <5A40751B-98AB-31CD-AC84-062543378725> /Applications/monero-wallet-gui.app/Contents/Frameworks/libicui18n.66.dylib
       0x103bbf000 -        0x103cdbff3 +libicuuc.66.dylib (0) <A98D72CC-C445-3E02-A597-60AE06CECD45> /Applications/monero-wallet-gui.app/Contents/Frameworks/libicuuc.66.dylib
       0x103d35000 -        0x103d49ff3 +libgpg-error.0.dylib (0) <025C2A81-38C4-3527-9FCE-6C88EFBB1243> /Applications/monero-wallet-gui.app/Contents/Frameworks/libgpg-error.0.dylib
       0x103e34000 -        0x103f9bfff +libqcocoa.dylib (0) <3BAB11D8-80A5-3E87-97A8-C1FEE7022B22> /Applications/monero-wallet-gui.app/Contents/PlugIns/platforms/libqcocoa.dylib
       0x103ff1000 -        0x10404ffff +org.qt-project.QtDBus (5.12 - 5.12.8) <B743D812-EC44-31D3-B311-B06FBD614D17> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtDBus.framework/Versions/5/QtDBus
       0x10406e000 -        0x104097ff7 +org.qt-project.QtPrintSupport (5.12 - 5.12.8) <E536797B-2C8A-3231-932C-C2EB648E3F07> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtPrintSupport.framework/Versions/5/QtPrintSupport
       0x10480e000 -        0x10489feff  dyld (750.5) <E4698FBD-806A-3396-B279-E685BA37430B> /usr/lib/dyld
       0x104913000 -        0x1063d0fff +libicudata.66.dylib (0) <51CD7641-33B7-3C63-875C-3767EB6E1D48> /Applications/monero-wallet-gui.app/Contents/Frameworks/libicudata.66.dylib
       0x10a59d000 -        0x10a5a0fff +libqtquick2plugin.dylib (0) <293D4163-7942-3E05-A12A-06B0B9F8F9C4> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqtquick2plugin.dylib
       0x10a5a8000 -        0x10a5abffb +libwindowplugin.dylib (0) <A33D67DC-ED09-3967-AB9F-9ABC19DEAF46> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libwindowplugin.dylib
       0x10a5b3000 -        0x10a5f4ffb +libqtquickcontrolsplugin.dylib (0) <94D997F6-B90E-3E63-92DB-AC07C8DC23EC> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqtquickcontrolsplugin.dylib
       0x10a615000 -        0x10a632ffb +libdialogplugin.dylib (0) <8CD3E085-6E85-39E4-929F-3027DA7CDBBD> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libdialogplugin.dylib
       0x10a644000 -        0x10a652ff3 +libqtgraphicaleffectsplugin.dylib (0) <6AEBDC52-7A75-3341-9665-9FB1FCF1B067> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqtgraphicaleffectsplugin.dylib
       0x10a685000 -        0x10a6ecff7 +libqtquickcontrols2plugin.dylib (0) <03ADC974-0950-3157-8FD5-A1C971F771F3> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqtquickcontrols2plugin.dylib
       0x10a704000 -        0x10a7a8ff7 +org.qt-project.QtQuickTemplates2 (5.12 - 5.12.8) <0332B87E-C10B-3D8C-9FB4-C486F0D1A57E> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQuickTemplates2.framework/Versions/5/QtQuickTemplates2
       0x10a82a000 -        0x10a841fff +org.qt-project.QtQuickControls2 (5.12 - 5.12.8) <5537B00A-E740-3C79-B056-45B07B0FAC31> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtQuickControls2.framework/Versions/5/QtQuickControls2
       0x10a862000 -        0x10a8c4ffb +libqtquickcontrols2fusionstyleplugin.dylib (0) <20658EB9-E36C-33A6-82DC-BA3BCAB7836C> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqtquickcontrols2fusionstyleplugin.dylib
       0x10a8d3000 -        0x10a8e4ffb +libqquicklayoutsplugin.dylib (0) <EBA67417-9864-35C9-93F0-CD8D8FD1B468> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqquicklayoutsplugin.dylib
       0x10a8fd000 -        0x10a936ffb +libqtquicktemplates2plugin.dylib (0) <D874E1B3-E32F-3181-A623-C2880DDFF524> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqtquicktemplates2plugin.dylib
       0x10a973000 -        0x10a97cffb +libqtgraphicaleffectsprivate.dylib (0) <44ECF0C9-649C-3BEF-B46B-B8CF443664BD> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqtgraphicaleffectsprivate.dylib
       0x10a9b7000 -        0x10a9c5ff7 +libqmlxmllistmodelplugin.dylib (0) <E8A501A9-E9D9-3051-B647-64E160EE35D2> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqmlxmllistmodelplugin.dylib
       0x10a9d3000 -        0x10acd8ff3 +org.qt-project.QtXmlPatterns (5.12 - 5.12.8) <96B3809B-F68C-3654-B38B-028EDA8B62BD> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtXmlPatterns.framework/Versions/5/QtXmlPatterns
       0x10ad8a000 -        0x10ad92ff3 +libdialogsprivateplugin.dylib (0) <307B31B3-27B0-3F2B-8734-302599E161A5> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libdialogsprivateplugin.dylib
       0x10ad9e000 -        0x10ada8fff +libqmlfolderlistmodelplugin.dylib (0) <B6AE490A-47C1-3D7C-8D19-82FEE788D811> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqmlfolderlistmodelplugin.dylib
       0x10adb5000 -        0x10adbbff7 +libqmlsettingsplugin.dylib (0) <239E6A4A-F816-3BE4-9119-2CD5C48C8220> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libqmlsettingsplugin.dylib
       0x10aeec000 -        0x10af00ff3 +libwidgetsplugin.dylib (0) <4A28378A-E871-396A-B562-ED6C8FC57ABA> /Applications/monero-wallet-gui.app/Contents/PlugIns/quick/libwidgetsplugin.dylib
       0x10b70d000 -        0x10b7d3fff  com.apple.AMDRadeonX4000GLDriver (3.9.15 - 3.0.9) <35DFDCB5-77BC-3216-A42B-CC4B31B9E63E> /System/Library/Extensions/AMDRadeonX4000GLDriver.bundle/Contents/MacOS/AMDRadeonX4000GLDriver
       0x10b875000 -        0x10b87cff7 +libqgenericbearer.dylib (0) <A9E082FE-2FE2-3A90-BED6-56B02582C4E5> /Applications/monero-wallet-gui.app/Contents/PlugIns/bearer/libqgenericbearer.dylib
       0x10bb0d000 -        0x10bb13ff3 +libqgif.dylib (0) <28055A28-2E59-3AF4-9556-4BB140248103> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqgif.dylib
       0x10bb1c000 -        0x10bb23ffb +libqicns.dylib (0) <09EAC99F-355F-3BE6-A6CD-BD6FA482E409> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqicns.dylib
       0x10bb2c000 -        0x10bb31ff3 +libqico.dylib (0) <187F0F7C-3CD1-3915-8A81-B6CCB0B963C6> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqico.dylib
       0x10bb3a000 -        0x10bb9dffb +libqjpeg.dylib (0) <D3905DAB-111B-3EEA-BACD-DD3781F84C28> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqjpeg.dylib
       0x10bba8000 -        0x10bbadff7 +libqmacheif.dylib (0) <7CD0EE1A-7B3E-3D6B-A6D2-66583037E744> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqmacheif.dylib
       0x10bbb6000 -        0x10bbbbffb +libqmacjp2.dylib (0) <9AA9EA3C-D386-35DB-AA7B-97FF9C66D489> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqmacjp2.dylib
       0x10bbc4000 -        0x10bbc8fff +libqsvg.dylib (0) <2C1BF307-C2BA-39B4-AE7A-B774B15C783E> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqsvg.dylib
       0x10bbd1000 -        0x10bc04ff3 +org.qt-project.QtSvg (5.12 - 5.12.8) <6312A82E-B9E0-3817-9D16-AA3E2134DC5C> /Applications/monero-wallet-gui.app/Contents/Frameworks/QtSvg.framework/Versions/5/QtSvg
       0x10c085000 -        0x10c089ffb +libqtga.dylib (0) <73EAF7A1-1F69-3A00-81EE-FB47BA03DDF7> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqtga.dylib
       0x10c092000 -        0x10c0f7ff3 +libqtiff.dylib (0) <A107F12F-9A02-3C64-8DBF-88599CEA0626> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqtiff.dylib
       0x10c106000 -        0x10c109ff3 +libqwbmp.dylib (0) <EF5A8E6A-3290-3326-BEC4-54A929844EA4> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqwbmp.dylib
       0x10c112000 -        0x10c1a6ff7 +libqwebp.dylib (0) <033064BD-432E-3A6A-BFCD-C954D49FF91D> /Applications/monero-wallet-gui.app/Contents/PlugIns/imageformats/libqwebp.dylib
       0x126a7c000 -        0x126a7f047  libobjc-trampolines.dylib (787.1) <8212B354-A106-3806-A022-A60F2B2FA5C9> /usr/lib/libobjc-trampolines.dylib
    0x7fff20674000 -     0x7fff208c1ff8  com.apple.RawCamera.bundle (9.02.0 - 1350.29) <0CC24FF1-0754-3A75-BA2D-212CF70ADDC1> /System/Library/CoreServices/RawCamera.bundle/Contents/MacOS/RawCamera
    0x7fff208c4000 -     0x7fff209f2ff0  com.apple.AMDMTLBronzeDriver (3.9.15 - 3.0.9) <D901C675-0E10-38B7-975A-82BB92383B60> /System/Library/Extensions/AMDMTLBronzeDriver.bundle/Contents/MacOS/AMDMTLBronzeDriver
    0x7fff209f3000 -     0x7fff20a29fff  ATIRadeonX4000SCLib.dylib (3.9.15) <8EF3D12C-FC1A-31AF-BDDA-7F697AE1BAB7> /System/Library/Extensions/AMDRadeonX4000GLDriver.bundle/Contents/MacOS/ATIRadeonX4000SCLib.dylib
    0x7fff21f03000 -     0x7fff22884ffb  libSC.dylib (3.9.15) <8B9CE960-1CF4-3618-8B5D-2A231D185639> /System/Library/Extensions/AMDShared.bundle/Contents/PlugIns/libSC.dylib
    0x7fff24f7e000 -     0x7fff25f85ff7  com.apple.driver.AppleIntelKBLGraphicsGLDriver (14.6.18 - 14.0.6) <B049C672-7CE4-3251-937E-99D0A84430D7> /System/Library/Extensions/AppleIntelKBLGraphicsGLDriver.bundle/Contents/MacOS/AppleIntelKBLGraphicsGLDriver
    0x7fff25f86000 -     0x7fff26385ff1  com.apple.driver.AppleIntelKBLGraphicsMTLDriver (14.6.18 - 14.0.6) <568AB53D-A275-3FAC-932C-A32C3E277CA3> /System/Library/Extensions/AppleIntelKBLGraphicsMTLDriver.bundle/Contents/MacOS/AppleIntelKBLGraphicsMTLDriver
    0x7fff28e20000 -     0x7fff28e24ffb  com.apple.agl (3.3.3 - AGL-3.3.3) <E9A0E636-1C0A-3825-8933-46D798321D6F> /System/Library/Frameworks/AGL.framework/Versions/A/AGL
    0x7fff2920d000 -     0x7fff2920dfff  com.apple.Accelerate (1.11 - Accelerate 1.11) <56DFF715-6A4E-3231-BDCC-A348BCB05047> /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
    0x7fff2920e000 -     0x7fff29224fef  libCGInterfaces.dylib (524.2.1) <A423F932-C044-3CEB-BF20-BF4CB323361E> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/Libraries/libCGInterfaces.dylib
    0x7fff29225000 -     0x7fff2987bfff  com.apple.vImage (8.1 - 524.2.1) <17C93AB9-1625-3FDB-9851-C5E77BBE3428> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage
    0x7fff2987c000 -     0x7fff29ae3ff7  libBLAS.dylib (1303.60.1) <CBC28BE4-3C78-3AED-9565-0D625251D121> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib
    0x7fff29ae4000 -     0x7fff29fb7fef  libBNNS.dylib (144.100.2) <8D653678-1F9B-3670-AAE2-46DFB8D37643> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib
    0x7fff29fb8000 -     0x7fff2a353fff  libLAPACK.dylib (1303.60.1) <F8E9D081-7C60-32EC-A47D-2D30CAD73C5F> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLAPACK.dylib
    0x7fff2a354000 -     0x7fff2a369fec  libLinearAlgebra.dylib (1303.60.1) <D2C1ACEA-2B6A-339A-9EEB-62A76CC92CBE> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLinearAlgebra.dylib
    0x7fff2a36a000 -     0x7fff2a36fff3  libQuadrature.dylib (7) <3112C977-8306-3190-8313-01A952B7F3CF> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libQuadrature.dylib
    0x7fff2a370000 -     0x7fff2a3e0fff  libSparse.dylib (103) <40510BF9-99A7-3155-A81D-6DE5A0C73EDC> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libSparse.dylib
    0x7fff2a3e1000 -     0x7fff2a3f3fef  libSparseBLAS.dylib (1303.60.1) <3C1066AB-20D5-38D2-B1F2-70A03DE76D0B> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libSparseBLAS.dylib
    0x7fff2a3f4000 -     0x7fff2a5cbfd7  libvDSP.dylib (735.121.1) <74702E2E-ED05-3765-B18C-64BEFF62B517> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvDSP.dylib
    0x7fff2a5cc000 -     0x7fff2a68efef  libvMisc.dylib (735.121.1) <137558BF-503D-3A6E-96DC-A181E3FB31FF> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvMisc.dylib
    0x7fff2a68f000 -     0x7fff2a68ffff  com.apple.Accelerate.vecLib (3.11 - vecLib 3.11) <D7E8E400-35C8-3174-9956-8D1B483620DA> /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/vecLib
    0x7fff2a690000 -     0x7fff2a6efff0  com.apple.Accounts (113 - 113) <0510C893-F1F2-38B2-B3AA-A30DB2F5B688> /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
    0x7fff2a839000 -     0x7fff2b5f9ffd  com.apple.AppKit (6.9 - 1894.50.103) <61269B8C-C432-335F-8894-B95C235A41A5> /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
    0x7fff2b649000 -     0x7fff2b649fff  com.apple.ApplicationServices (48 - 50) <EEC73694-1A37-3C14-A839-6991E2BD8655> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
    0x7fff2b64a000 -     0x7fff2b6b5fff  com.apple.ApplicationServices.ATS (377 - 493.0.4.1) <A6912C4A-55CC-3701-BACA-E63423B99481> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/ATS
    0x7fff2b74e000 -     0x7fff2b78cff0  libFontRegistry.dylib (274.0.5.1) <A78A7869-C96C-3AD6-A038-DE541639BB60> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/Resources/libFontRegistry.dylib
    0x7fff2b7e7000 -     0x7fff2b816fff  com.apple.ATSUI (1.0 - 1) <4B3C2201-DBB3-352C-936B-9C423122EFF6> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATSUI.framework/Versions/A/ATSUI
    0x7fff2b817000 -     0x7fff2b81bffb  com.apple.ColorSyncLegacy (4.13.0 - 1) <47D42CDE-2E9A-3AF6-9365-1BFD1189196B> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ColorSyncLegacy.framework/Versions/A/ColorSyncLegacy
    0x7fff2b8b5000 -     0x7fff2b90cffa  com.apple.HIServices (1.22 - 675.1) <273492E3-FF0F-3A8A-A83F-0F11F99B5F26> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices
    0x7fff2b90d000 -     0x7fff2b91bfff  com.apple.LangAnalysis (1.7.0 - 1.7.0) <DA175323-5BE3-3C54-92D4-A171A4A067E6> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/LangAnalysis.framework/Versions/A/LangAnalysis
    0x7fff2b91c000 -     0x7fff2b961ffa  com.apple.print.framework.PrintCore (15.4 - 516.2) <99AEBCDB-2DCA-3A13-906F-7F0D7962B002> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Versions/A/PrintCore
    0x7fff2b962000 -     0x7fff2b96cff7  com.apple.QD (4.0 - 413) <D2E1DC80-D26F-3508-BBA5-B8AE7ED6CB0E> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/QD.framework/Versions/A/QD
    0x7fff2b96d000 -     0x7fff2b97affc  com.apple.speech.synthesis.framework (9.0.24 - 9.0.24) <823C0DE7-1351-3B39-8F06-AB5FCAD2C874> /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/SpeechSynthesis.framework/Versions/A/SpeechSynthesis
    0x7fff2b97b000 -     0x7fff2ba5cffa  com.apple.audio.toolbox.AudioToolbox (1.14 - 1.14) <75651F0A-F2CE-3F68-B86A-E66B8815DCF4> /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
    0x7fff2ba5e000 -     0x7fff2ba5efff  com.apple.audio.units.AudioUnit (1.14 - 1.14) <E51DCB3C-CF4F-320B-AC86-D445E30C0891> /System/Library/Frameworks/AudioUnit.framework/Versions/A/AudioUnit
    0x7fff2bdf4000 -     0x7fff2c182ffd  com.apple.CFNetwork (1126 - 1126) <BB8F4C63-10B8-3ACD-84CF-D4DCFA9245DD> /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
    0x7fff2c1fe000 -     0x7fff2c1fefff  com.apple.Carbon (160 - 162) <4F1F60CB-6C1E-3D79-832E-8D606601F282> /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
    0x7fff2c1ff000 -     0x7fff2c202ff3  com.apple.CommonPanels (1.2.6 - 101) <333BBF55-AF23-3B99-A9FF-7906175B9406> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/CommonPanels.framework/Versions/A/CommonPanels
    0x7fff2c203000 -     0x7fff2c4f7ff3  com.apple.HIToolbox (2.1.1 - 994.6) <5C44ACA7-D158-3F9B-8F88-0477510D44FA> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox
    0x7fff2c4f8000 -     0x7fff2c4fbff3  com.apple.help (1.3.8 - 71) <4B2701A0-8813-35F8-82F8-676B184D15C4> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Help.framework/Versions/A/Help
    0x7fff2c4fc000 -     0x7fff2c501ff7  com.apple.ImageCapture (9.0 - 1600.60.4.2) <20872A2D-CBF9-38E6-BD16-C1D387120651> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/ImageCapture.framework/Versions/A/ImageCapture
    0x7fff2c502000 -     0x7fff2c502fff  com.apple.ink.framework (10.15 - 227) <5B60FDDE-D60E-326B-BD3D-6EA5FA1CBB76> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Ink.framework/Versions/A/Ink
    0x7fff2c503000 -     0x7fff2c51dffa  com.apple.openscripting (1.7 - 185.1) <E59F893B-1A73-3098-8924-79227EC9787E> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/OpenScripting.framework/Versions/A/OpenScripting
    0x7fff2c53e000 -     0x7fff2c53efff  com.apple.print.framework.Print (15 - 271) <07C50BF6-2222-3769-A5B8-79D7F996183F> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Print.framework/Versions/A/Print
    0x7fff2c53f000 -     0x7fff2c541ff7  com.apple.securityhi (9.0 - 55008) <D7017D5A-4206-3E2F-9F8E-0F932422CA87> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/SecurityHI.framework/Versions/A/SecurityHI
    0x7fff2c542000 -     0x7fff2c548fff  com.apple.speech.recognition.framework (6.0.3 - 6.0.3) <1188E643-967C-334E-BC1A-60A0F82C67E5> /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/SpeechRecognition.framework/Versions/A/SpeechRecognition
    0x7fff2c6f0000 -     0x7fff2c7e6fff  com.apple.ColorSync (4.13.0 - 3394.9) <61698A7B-BB8C-3891-9547-703FF84671A8> /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
    0x7fff2cad1000 -     0x7fff2cfdaffb  com.apple.audio.CoreAudio (5.0 - 5.0) <62BEE4B7-8A26-3951-9D78-4E193617AF7A> /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
    0x7fff2d02d000 -     0x7fff2d065fff  com.apple.CoreBluetooth (1.0 - 1) <6BC7F863-4495-371F-BC54-543E5CFE1665> /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
    0x7fff2d066000 -     0x7fff2d450fe8  com.apple.CoreData (120 - 977.3) <D902A2E3-1D0A-3995-974E-A526976E5735> /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
    0x7fff2d451000 -     0x7fff2d581ffe  com.apple.CoreDisplay (1.0 - 186.6.12) <EA74CC46-8715-3B90-95E8-4594D2F0CC8A> /System/Library/Frameworks/CoreDisplay.framework/Versions/A/CoreDisplay
    0x7fff2d582000 -     0x7fff2da01ffb  com.apple.CoreFoundation (6.9 - 1676.105) <6AF8B3CC-BC3F-3869-B9FB-1D881422364E> /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
    0x7fff2da03000 -     0x7fff2e077ff8  com.apple.CoreGraphics (2.0 - 1355.17) <E1CE3919-F36B-309F-89BA-79F36DC8125E> /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
    0x7fff2e085000 -     0x7fff2e3e0ff0  com.apple.CoreImage (15.0.0 - 940.9) <44F68E8C-315A-32A6-BB19-7F24C00AB347> /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage
    0x7fff2e7a1000 -     0x7fff2e87cffc  com.apple.CoreMedia (1.0 - 2620.11.40.2) <0F490101-ED30-3189-B099-E247B6361A0B> /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia
    0x7fff2e969000 -     0x7fff2e969fff  com.apple.CoreServices (1069.24 - 1069.24) <D9F6AB40-10EC-3682-A969-85560E2E4768> /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
    0x7fff2e96a000 -     0x7fff2e9effff  com.apple.AE (838.1 - 838.1) <5F26DA9B-FB2E-3AF8-964B-63BD6671CF12> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/AE
    0x7fff2e9f0000 -     0x7fff2ecd1ff7  com.apple.CoreServices.CarbonCore (1217 - 1217) <8022AF47-AA99-3786-B086-141D84F00387> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CarbonCore.framework/Versions/A/CarbonCore
    0x7fff2ecd2000 -     0x7fff2ed1fffd  com.apple.DictionaryServices (1.2 - 323.6) <C0F3830C-A4C6-3046-9A6A-DE1B5D448C2C> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/DictionaryServices.framework/Versions/A/DictionaryServices
    0x7fff2ed20000 -     0x7fff2ed28ff7  com.apple.CoreServices.FSEvents (1268.100.1 - 1268.100.1) <E4B2CAF2-1203-335F-9971-1278CB6E2AE0> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/FSEvents.framework/Versions/A/FSEvents
    0x7fff2ed29000 -     0x7fff2ef63ff6  com.apple.LaunchServices (1069.24 - 1069.24) <2E0AD228-B1CC-3645-91EE-EB7F46F2147B> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices
    0x7fff2ef64000 -     0x7fff2effcff1  com.apple.Metadata (10.7.0 - 2076.6) <C8034E84-7DD4-34B9-9CDF-16A05032FF39> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Metadata
    0x7fff2effd000 -     0x7fff2f02afff  com.apple.CoreServices.OSServices (1069.24 - 1069.24) <72FDEA52-7607-3745-AC43-630D80962099> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/OSServices.framework/Versions/A/OSServices
    0x7fff2f02b000 -     0x7fff2f092fff  com.apple.SearchKit (1.4.1 - 1.4.1) <086EB5DF-A2EC-3342-8028-CA7996BE5CB2> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/SearchKit.framework/Versions/A/SearchKit
    0x7fff2f093000 -     0x7fff2f0b7ff5  com.apple.coreservices.SharedFileList (131.4 - 131.4) <AE333DA2-C279-3751-8C15-B963E58EE61E> /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/SharedFileList.framework/Versions/A/SharedFileList
    0x7fff2f3dc000 -     0x7fff2f593ffc  com.apple.CoreText (643.1.5.1 - 643.1.5.1) <715FE3F7-E8FB-3997-85A0-3AB2839F6C30> /System/Library/Frameworks/CoreText.framework/Versions/A/CoreText
    0x7fff2f594000 -     0x7fff2f5d8ffb  com.apple.CoreVideo (1.8 - 344.3) <A200AFC7-2CB2-30CD-8B2A-1269CA64A29B> /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo
    0x7fff2f5d9000 -     0x7fff2f666ffc  com.apple.framework.CoreWLAN (13.0 - 1601.2) <855E51AA-DF3A-3BB9-A4F0-6880D42B8762> /System/Library/Frameworks/CoreWLAN.framework/Versions/A/CoreWLAN
    0x7fff2f822000 -     0x7fff2f82dff7  com.apple.DirectoryService.Framework (10.15 - 220.40.1) <06D98FD0-796F-356F-B492-A6D8F3D5BEC0> /System/Library/Frameworks/DirectoryService.framework/Versions/A/DirectoryService
    0x7fff2f82e000 -     0x7fff2f8d8ff0  com.apple.DiscRecording (9.0.3 - 9030.4.5) <D9033DDA-E4C8-36FB-AE60-4EF66F4F1F9E> /System/Library/Frameworks/DiscRecording.framework/Versions/A/DiscRecording
    0x7fff2f8fd000 -     0x7fff2f903fff  com.apple.DiskArbitration (2.7 - 2.7) <52E7D181-2A18-37CD-B24F-AA32E93F7A69> /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
    0x7fff2faf6000 -     0x7fff2fc24ff6  com.apple.FileProvider (304.1 - 304.1) <58D64236-947E-3E6A-85E6-C66AEF9E0EE0> /System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider
    0x7fff2fc3c000 -     0x7fff30001fff  com.apple.Foundation (6.9 - 1676.105) <1FA28BAB-7296-3A09-8E1E-E62A7D233DB8> /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
    0x7fff3006e000 -     0x7fff300beff7  com.apple.GSS (4.0 - 2.0) <4E241C00-42A5-3572-9430-D950FBB7A4A0> /System/Library/Frameworks/GSS.framework/Versions/A/GSS
    0x7fff301fb000 -     0x7fff3030fff3  com.apple.Bluetooth (7.0.5 - 7.0.5f6) <5897C368-9674-3E34-B144-FFB06A2DF37B> /System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth
    0x7fff30375000 -     0x7fff30419ff3  com.apple.framework.IOKit (2.0.2 - 1726.121.1) <A0F54725-036F-3279-A46E-C2ABDBFD479B> /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
    0x7fff3041b000 -     0x7fff3042cffb  com.apple.IOSurface (269.11 - 269.11) <D3CC2AA1-4AE2-30EE-A9DB-C04CCAA88ADE> /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface
    0x7fff304ab000 -     0x7fff30607ffe  com.apple.ImageIO.framework (3.3.0 - 1976.6) <5B4C2E04-9161-3C82-A7FB-F4D51E3C1E10> /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
    0x7fff30608000 -     0x7fff3060bfff  libGIF.dylib (1976.6) <3B26EE1C-C570-305C-A9A3-EA62D2F2E7B8> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libGIF.dylib
    0x7fff3060c000 -     0x7fff306c5fff  libJP2.dylib (1976.6) <EB4E4E09-DD81-3E6B-A513-3667E810AEF3> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJP2.dylib
    0x7fff306c6000 -     0x7fff306e9fe3  libJPEG.dylib (1976.6) <9D7FAC55-85A6-34AB-9F26-0BCA381E8CE7> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libJPEG.dylib
    0x7fff30965000 -     0x7fff3097ffef  libPng.dylib (1976.6) <4886A1F8-E9CA-38F2-BF2F-1FCA1DFDD1C9> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libPng.dylib
    0x7fff30980000 -     0x7fff30981fff  libRadiance.dylib (1976.6) <FA759D33-131A-33B8-943E-32409F162738> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libRadiance.dylib
    0x7fff30982000 -     0x7fff309cbfff  libTIFF.dylib (1976.6) <E9994BF8-6CF5-3422-B4FD-A14DC390EF12> /System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libTIFF.dylib
    0x7fff31f2d000 -     0x7fff31f3fff3  com.apple.Kerberos (3.0 - 1) <AE0E56CA-D924-3CC8-BBAA-8C6EEC3038BE> /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos
    0x7fff31f40000 -     0x7fff31f40fff  libHeimdalProxy.dylib (77) <A970C7A8-7CCD-3701-A459-078BD5E8FE4E> /System/Library/Frameworks/Kerberos.framework/Versions/A/Libraries/libHeimdalProxy.dylib
    0x7fff31f41000 -     0x7fff31f77ff7  com.apple.LDAPFramework (2.4.28 - 194.5) <4CFB6351-53B9-36AF-B654-AE636BBC361A> /System/Library/Frameworks/LDAP.framework/Versions/A/LDAP
    0x7fff322d2000 -     0x7fff322dcffb  com.apple.MediaAccessibility (1.0 - 125.1) <DBF40A12-65A6-33E4-839C-292600B7D910> /System/Library/Frameworks/MediaAccessibility.framework/Versions/A/MediaAccessibility
    0x7fff323a8000 -     0x7fff32af5ff5  com.apple.MediaToolbox (1.0 - 2620.11.40.2) <40F16AF6-79D1-3C2E-976C-E7E7870A4EF9> /System/Library/Frameworks/MediaToolbox.framework/Versions/A/MediaToolbox
    0x7fff32af7000 -     0x7fff32bc1ff7  com.apple.Metal (212.7 - 212.7) <CC7BF715-142B-3C2A-81AD-0E35693230F2> /System/Library/Frameworks/Metal.framework/Versions/A/Metal
    0x7fff32bde000 -     0x7fff32c1bff7  com.apple.MetalPerformanceShaders.MPSCore (1.0 - 1) <52089325-EC97-3EED-ABB3-9B39EC0BD429> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSCore.framework/Versions/A/MPSCore
    0x7fff32c1c000 -     0x7fff32ca6fe2  com.apple.MetalPerformanceShaders.MPSImage (1.0 - 1) <9E434EA0-6BCA-3903-B882-CEB69730A63B> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSImage.framework/Versions/A/MPSImage
    0x7fff32ca7000 -     0x7fff32cccff4  com.apple.MetalPerformanceShaders.MPSMatrix (1.0 - 1) <EDD6C3A5-E231-3FB1-B4D4-45742AFB9A4E> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSMatrix.framework/Versions/A/MPSMatrix
    0x7fff32ccd000 -     0x7fff32ce2ffb  com.apple.MetalPerformanceShaders.MPSNDArray (1.0 - 1) <C5A2B865-5CE2-3E5D-8452-54639FCB0954> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/Versions/A/MPSNDArray
    0x7fff32ce3000 -     0x7fff32e41ffc  com.apple.MetalPerformanceShaders.MPSNeuralNetwork (1.0 - 1) <47CCDBAC-5843-366A-A68C-6E8851D0865D> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/Versions/A/MPSNeuralNetwork
    0x7fff32e42000 -     0x7fff32e91ff4  com.apple.MetalPerformanceShaders.MPSRayIntersector (1.0 - 1) <302BDF8E-B00A-3123-A6C4-E262B7513CF6> /System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSRayIntersector.framework/Versions/A/MPSRayIntersector
    0x7fff32e92000 -     0x7fff32e93ff5  com.apple.MetalPerformanceShaders.MetalPerformanceShaders (1.0 - 1) <14F84B42-9DA2-39A1-81B4-666B8020520C> /System/Library/Frameworks/MetalPerformanceShaders.framework/Versions/A/MetalPerformanceShaders
    0x7fff33f1a000 -     0x7fff33f26ffe  com.apple.NetFS (6.0 - 4.0) <AC74E6A4-6E9B-3AB1-9577-8277F8A3EDE0> /System/Library/Frameworks/NetFS.framework/Versions/A/NetFS
    0x7fff33f27000 -     0x7fff3407eff3  com.apple.Network (1.0 - 1) <B5B8E999-BBCC-3DEF-8881-8FFF69F8EC4B> /System/Library/Frameworks/Network.framework/Versions/A/Network
    0x7fff36aa6000 -     0x7fff36aaeff7  libcldcpuengine.dylib (2.14) <D8583B54-FE2A-33FD-A702-ABF307D99FD1> /System/Library/Frameworks/OpenCL.framework/Versions/A/Libraries/libcldcpuengine.dylib
    0x7fff36aaf000 -     0x7fff36b07fff  com.apple.opencl (3.5 - 3.5) <9B101D40-EA79-3C0D-B7AE-A3F18094B2D7> /System/Library/Frameworks/OpenCL.framework/Versions/A/OpenCL
    0x7fff36b08000 -     0x7fff36b24fff  com.apple.CFOpenDirectory (10.15 - 220.40.1) <BFC32EBE-D95C-3267-B95C-5CEEFD189EA6> /System/Library/Frameworks/OpenDirectory.framework/Versions/A/Frameworks/CFOpenDirectory.framework/Versions/A/CFOpenDirectory
    0x7fff36b25000 -     0x7fff36b30ffd  com.apple.OpenDirectory (10.15 - 220.40.1) <76A20BBA-775F-3E17-AB0F-FEDFCDCE0716> /System/Library/Frameworks/OpenDirectory.framework/Versions/A/OpenDirectory
    0x7fff37496000 -     0x7fff37498fff  libCVMSPluginSupport.dylib (17.10.22) <AAE07E0C-4B28-364B-A7D9-028C7CD14954> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCVMSPluginSupport.dylib
    0x7fff37499000 -     0x7fff3749efff  libCoreFSCache.dylib (176.15) <609C5DFC-9A97-344D-BBC7-E0B08D862C63> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCoreFSCache.dylib
    0x7fff3749f000 -     0x7fff374a3fff  libCoreVMClient.dylib (176.15) <8F8DD27F-AC7C-398D-A8E3-396F1528E317> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libCoreVMClient.dylib
    0x7fff374a4000 -     0x7fff374acff7  libGFXShared.dylib (17.10.22) <D0649AB5-5331-328D-8141-E5A6F06D4AD7> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGFXShared.dylib
    0x7fff374ad000 -     0x7fff374b7fff  libGL.dylib (17.10.22) <116DDBF7-D725-3B8C-BD0B-A21B758FE421> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib
    0x7fff374b8000 -     0x7fff374ecff7  libGLImage.dylib (17.10.22) <2B314C76-C7E6-3AC5-9157-70B0529C1F9B> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLImage.dylib
    0x7fff374ed000 -     0x7fff37681ff7  libGLProgrammability.dylib (17.10.22) <757192B3-4509-3C26-B3B3-C10165F97661> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLProgrammability.dylib
    0x7fff37682000 -     0x7fff376befff  libGLU.dylib (17.10.22) <B29F73B2-B5A9-3C38-AF77-351173D2E3DB> /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLU.dylib
    0x7fff380fa000 -     0x7fff38109ff7  com.apple.opengl (17.10.22 - 17.10.22) <D5BF32A8-2E0A-345D-80A3-7CA7C2CF748D> /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
    0x7fff3810a000 -     0x7fff38283fff  GLEngine (17.10.22) <0B6AF0FD-DBF3-3D91-B0EA-80402E9E1484> /System/Library/Frameworks/OpenGL.framework/Versions/A/Resources/GLEngine.bundle/GLEngine
    0x7fff38284000 -     0x7fff382acfff  GLRendererFloat (17.10.22) <A3D159EB-39BB-3F7C-8C1E-005D81788963> /System/Library/Frameworks/OpenGL.framework/Versions/A/Resources/GLRendererFloat.bundle/GLRendererFloat
    0x7fff390c7000 -     0x7fff39349ff9  com.apple.QuartzCore (1.11 - 841.2) <444E6F22-DFA6-391B-B51F-A96AE69E524D> /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
    0x7fff39eca000 -     0x7fff3a213ff1  com.apple.security (7.0 - 59306.120.7) <AEA33464-1507-36F1-8CAE-A86EB787F9B5> /System/Library/Frameworks/Security.framework/Versions/A/Security
    0x7fff3a214000 -     0x7fff3a29cffb  com.apple.securityfoundation (6.0 - 55236.60.1) <79289FE1-CB5F-3BEF-A33F-11A29A93A681> /System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation
    0x7fff3a2cb000 -     0x7fff3a2cfff8  com.apple.xpc.ServiceManagement (1.0 - 1) <4194D29D-F0D4-33F8-839A-D03C6C62D8DB> /System/Library/Frameworks/ServiceManagement.framework/Versions/A/ServiceManagement
    0x7fff3af7b000 -     0x7fff3afe9ff7  com.apple.SystemConfiguration (1.19 - 1.19) <0CF8726A-BE41-3E07-B895-FBC44B75450E> /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
    0x7fff3b268000 -     0x7fff3b5ebff4  com.apple.VideoToolbox (1.0 - 2620.11.40.2) <53E0D852-61CA-34FE-9A9B-788708ADE495> /System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox
    0x7fff3ef4a000 -     0x7fff3f00fff7  com.apple.APFS (1412.120.2 - 1412.120.2) <1E8FD511-FDC4-31A2-ACDE-EB5192032BC6> /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
    0x7fff3f7d2000 -     0x7fff3f7daff5  com.apple.AccessibilityBundles (1.0 - 131.5) <7A4B7097-CA15-3947-B465-D7D24FB6653E> /System/Library/PrivateFrameworks/AccessibilityBundles.framework/Versions/A/AccessibilityBundles
    0x7fff4011f000 -     0x7fff40120ff1  com.apple.AggregateDictionary (1.0 - 1) <B907CE7A-0122-3E63-BF39-0A242B0DD7C4> /System/Library/PrivateFrameworks/AggregateDictionary.framework/Versions/A/AggregateDictionary
    0x7fff406bc000 -     0x7fff406d9ff4  com.apple.AppContainer (4.0 - 448.100.6) <9C2D0065-9B38-3D1C-A090-46F129A1B3CA> /System/Library/PrivateFrameworks/AppContainer.framework/Versions/A/AppContainer
    0x7fff4072e000 -     0x7fff4073cff7  com.apple.AppSandbox (4.0 - 448.100.6) <7DAB58B1-8176-3FB0-A7B0-8A38E118E90B> /System/Library/PrivateFrameworks/AppSandbox.framework/Versions/A/AppSandbox
    0x7fff40bb7000 -     0x7fff40bdbffb  com.apple.framework.Apple80211 (13.0 - 1610.1) <B4B80CD6-B38E-3748-B30B-5088CCE9A7A8> /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Apple80211
    0x7fff40e99000 -     0x7fff40ea8fd7  com.apple.AppleFSCompression (119.100.1 - 1.0) <2E75CF51-B693-3275-9A4F-40571D48745E> /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
    0x7fff40fa7000 -     0x7fff40fb2ff7  com.apple.AppleIDAuthSupport (1.0 - 1) <F4651654-E24F-3BF4-8DDF-8F91E5219BA4> /System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/Versions/A/AppleIDAuthSupport
    0x7fff40ff4000 -     0x7fff4103cff7  com.apple.AppleJPEG (1.0 - 1) <4655FF70-9772-3D7C-8159-5A5E56C9F84B> /System/Library/PrivateFrameworks/AppleJPEG.framework/Versions/A/AppleJPEG
    0x7fff41426000 -     0x7fff4142aff7  com.apple.AppleSRP (5.0 - 1) <B683AD55-A121-31DD-9A87-3A31C35FEABF> /System/Library/PrivateFrameworks/AppleSRP.framework/Versions/A/AppleSRP
    0x7fff4142b000 -     0x7fff4144dfff  com.apple.applesauce (1.0 - 16.25) <33B66B71-64A4-365D-9953-E0545E69A5E7> /System/Library/PrivateFrameworks/AppleSauce.framework/Versions/A/AppleSauce
    0x7fff4150c000 -     0x7fff4150fffb  com.apple.AppleSystemInfo (3.1.5 - 3.1.5) <92580EE3-74BF-3488-90ED-C8EBD7A1B4C3> /System/Library/PrivateFrameworks/AppleSystemInfo.framework/Versions/A/AppleSystemInfo
    0x7fff41510000 -     0x7fff41560ff7  com.apple.AppleVAFramework (6.1.2 - 6.1.2) <39C3583D-C824-3168-B67A-498487FD03D9> /System/Library/PrivateFrameworks/AppleVA.framework/Versions/A/AppleVA
    0x7fff415a9000 -     0x7fff415b8ff9  com.apple.AssertionServices (1.0 - 223.100.31) <478D2004-9B84-3AE9-9A0B-0A0B68ED028F> /System/Library/PrivateFrameworks/AssertionServices.framework/Versions/A/AssertionServices
    0x7fff41afa000 -     0x7fff41ef5ff8  com.apple.audio.AudioResourceArbitration (1.0 - 1) <9ABFE41A-FD01-3111-BA73-D2DD1BF96525> /System/Library/PrivateFrameworks/AudioResourceArbitration.framework/Versions/A/AudioResourceArbitration
    0x7fff4214b000 -     0x7fff4238bfe0  com.apple.audio.AudioToolboxCore (1.0 - 1104.84) <FA17E892-6A1A-309D-95C7-30ACFC44319C> /System/Library/PrivateFrameworks/AudioToolboxCore.framework/Versions/A/AudioToolboxCore
    0x7fff4238f000 -     0x7fff424abff0  com.apple.AuthKit (1.0 - 1) <375C3886-5430-3C02-BD2C-4244BF490ABA> /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
    0x7fff42668000 -     0x7fff42671ff7  com.apple.coreservices.BackgroundTaskManagement (1.0 - 104) <F070F440-27AB-3FCF-9602-F278C332CA01> /System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/BackgroundTaskManagement
    0x7fff42672000 -     0x7fff42713ff5  com.apple.backup.framework (1.11.5 - 1298.5.10) <637CA389-627A-365C-98C2-D297C47D6EE3> /System/Library/PrivateFrameworks/Backup.framework/Versions/A/Backup
    0x7fff42714000 -     0x7fff427a0ff6  com.apple.BaseBoard (466.3 - 466.3) <1718A41A-9923-3FD0-96B8-82376E153D27> /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
    0x7fff428a2000 -     0x7fff428deff7  com.apple.bom (14.0 - 219.2) <586F1D9C-23B0-3F38-9C5B-728E9DD8B953> /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom
    0x7fff4345d000 -     0x7fff434acfff  com.apple.ChunkingLibrary (307 - 307) <32E0F1A1-9DD6-3B52-91C2-93643041AA60> /System/Library/PrivateFrameworks/ChunkingLibrary.framework/Versions/A/ChunkingLibrary
    0x7fff43606000 -     0x7fff43691ff8  com.apple.CloudDocs (1.0 - 698.14) <4CFF0DF0-8A89-3DAD-8A07-A208FDDD163B> /System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs
    0x7fff44353000 -     0x7fff44363ffb  com.apple.CommonAuth (4.0 - 2.0) <91EC83B5-857D-3D4F-93B1-AAD7E0E029D8> /System/Library/PrivateFrameworks/CommonAuth.framework/Versions/A/CommonAuth
    0x7fff44377000 -     0x7fff4438efff  com.apple.commonutilities (8.0 - 900) <12C6DEE5-1740-39A5-9711-6F815C6D77BD> /System/Library/PrivateFrameworks/CommonUtilities.framework/Versions/A/CommonUtilities
    0x7fff44a92000 -     0x7fff44e67fc8  com.apple.CoreAUC (283.0.0 - 283.0.0) <BA9522E5-95D0-30D0-BEF4-691CEB51035B> /System/Library/PrivateFrameworks/CoreAUC.framework/Versions/A/CoreAUC
    0x7fff44e68000 -     0x7fff44e95ff7  com.apple.CoreAVCHD (6.1.0 - 6100.4.1) <14FC549B-86BD-396A-B03E-6F5219482943> /System/Library/PrivateFrameworks/CoreAVCHD.framework/Versions/A/CoreAVCHD
    0x7fff44eb8000 -     0x7fff44ed7ffc  com.apple.analyticsd (1.0 - 1) <A4F653CA-2FD6-348B-B7B3-48D91A67508A> /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
    0x7fff451e2000 -     0x7fff451edff7  com.apple.frameworks.CoreDaemon (1.3 - 1.3) <8F8E586D-C153-3ABA-88B7-6CEC7F476F0E> /System/Library/PrivateFrameworks/CoreDaemon.framework/Versions/B/CoreDaemon
    0x7fff4546e000 -     0x7fff4547eff3  com.apple.CoreEmoji (1.0 - 107.1) <CDCCB4B0-B98F-38E8-9568-C81320E756EB> /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
    0x7fff45abe000 -     0x7fff45b28ff0  com.apple.CoreNLP (1.0 - 213) <40FC46D2-844C-3282-A8E4-69DD827F05C5> /System/Library/PrivateFrameworks/CoreNLP.framework/Versions/A/CoreNLP
    0x7fff45f56000 -     0x7fff45f5eff8  com.apple.CorePhoneNumbers (1.0 - 1) <B2CE100D-B82F-3481-86F6-7F85FF8BFAFB> /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/Versions/A/CorePhoneNumbers
    0x7fff4694b000 -     0x7fff4696efff  com.apple.CoreSVG (1.0 - 129) <3141D198-0507-3F72-A2C9-752EAFE3EEB3> /System/Library/PrivateFrameworks/CoreSVG.framework/Versions/A/CoreSVG
    0x7fff4696f000 -     0x7fff469a2fff  com.apple.CoreServicesInternal (446.7 - 446.7) <B2CEC515-2225-3CB1-B34A-904AAEA54FDF> /System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal
    0x7fff469a3000 -     0x7fff469d1ffd  com.apple.CSStore (1069.24 - 1069.24) <C96E5CE8-D604-3F13-B079-B2BA33B90081> /System/Library/PrivateFrameworks/CoreServicesStore.framework/Versions/A/CoreServicesStore
    0x7fff46ef6000 -     0x7fff46f8cff7  com.apple.CoreSymbolication (11.4 - 64535.33.2) <0E7A1529-C737-33FD-AA7D-A32EB8B192DA> /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
    0x7fff47024000 -     0x7fff47150ff6  com.apple.coreui (2.1 - 609.4) <9B93CC42-804B-305A-8FCE-5F06821B544C> /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
    0x7fff47151000 -     0x7fff47307ff5  com.apple.CoreUtils (6.2.1 - 621.5) <CD4B58E5-1494-3457-84FF-3869378E2DC9> /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
    0x7fff47441000 -     0x7fff47454ff1  com.apple.CrashReporterSupport (10.13 - 15016) <827F4E31-9F23-3683-AC5A-59CCA90F2359> /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
    0x7fff4750d000 -     0x7fff4751fff8  com.apple.framework.DFRFoundation (1.0 - 252.50.1) <19F79D32-71D3-3A87-98C9-B5C6C96076C4> /System/Library/PrivateFrameworks/DFRFoundation.framework/Versions/A/DFRFoundation
    0x7fff47520000 -     0x7fff47525fff  com.apple.DSExternalDisplay (3.1 - 380) <971F24F1-B1FC-3674-9C00-F88EEF94DC05> /System/Library/PrivateFrameworks/DSExternalDisplay.framework/Versions/A/DSExternalDisplay
    0x7fff475af000 -     0x7fff47629ff0  com.apple.datadetectorscore (8.0 - 659) <9FD9BDFA-3724-3BEA-946C-0473447196A3> /System/Library/PrivateFrameworks/DataDetectorsCore.framework/Versions/A/DataDetectorsCore
    0x7fff47675000 -     0x7fff476b2ff8  com.apple.DebugSymbols (194 - 194) <9BCE6685-6C45-3DF9-98EB-FCF8196160F0> /System/Library/PrivateFrameworks/DebugSymbols.framework/Versions/A/DebugSymbols
    0x7fff476b3000 -     0x7fff4783bff6  com.apple.desktopservices (1.14.5 - 1281.5.3) <79972B8B-7B60-3AD5-9A5F-17976DE8080B> /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
    0x7fff47ad8000 -     0x7fff47ba0ffe  com.apple.DiskImagesFramework (559.100.2 - 559.100.2) <DE281E96-21D0-3BE3-BEE0-D901B24D71EE> /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
    0x7fff47ba1000 -     0x7fff47c74ff1  com.apple.DiskManagement (13.0 - 1648.120.5) <650DBBE4-6624-3064-A26D-6BCAA0FE41F9> /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
    0x7fff47d57000 -     0x7fff47d5bff9  com.apple.EFILogin (2.0 - 2) <B95015BC-5BC2-33D9-AD94-01905DD56193> /System/Library/PrivateFrameworks/EFILogin.framework/Versions/A/EFILogin
    0x7fff491e9000 -     0x7fff49604ff1  com.apple.vision.FaceCore (4.3.0 - 4.3.0) <1B5D7DD6-718E-3111-A702-EB04B8903662> /System/Library/PrivateFrameworks/FaceCore.framework/Versions/A/FaceCore
    0x7fff49ca2000 -     0x7fff49ddaffc  libFontParser.dylib (277.2.5.3) <DEB18756-082F-359B-AE93-F9C3B5EC7AF4> /System/Library/PrivateFrameworks/FontServices.framework/libFontParser.dylib
    0x7fff49ddb000 -     0x7fff49e0ffff  libTrueTypeScaler.dylib (277.2.5.3) <B16255A6-C51A-328B-B679-8FBF64495770> /System/Library/PrivateFrameworks/FontServices.framework/libTrueTypeScaler.dylib
    0x7fff49e74000 -     0x7fff49e84ff6  libhvf.dylib (1.0 - $[CURRENT_PROJECT_VERSION]) <6396BC1F-13C1-37D7-91B9-1FF60910C7FA> /System/Library/PrivateFrameworks/FontServices.framework/libhvf.dylib
    0x7fff4d365000 -     0x7fff4d366fff  libmetal_timestamp.dylib (902.14.11) <BE88F259-0A3C-3910-8983-FB5E2C905E87> /System/Library/PrivateFrameworks/GPUCompiler.framework/Versions/3902/Libraries/libmetal_timestamp.dylib
    0x7fff4ea17000 -     0x7fff4ea22ff7  libGPUSupportMercury.dylib (17.10.22) <B2E086E1-6E50-3A3D-B014-FCDAACBACE90> /System/Library/PrivateFrameworks/GPUSupport.framework/Versions/A/Libraries/libGPUSupportMercury.dylib
    0x7fff4ea23000 -     0x7fff4ea29fff  com.apple.GPUWrangler (5.2.4 - 5.2.4) <5B819701-9F0C-374B-8925-A22DFC16514F> /System/Library/PrivateFrameworks/GPUWrangler.framework/Versions/A/GPUWrangler
    0x7fff4ed48000 -     0x7fff4ed6eff1  com.apple.GenerationalStorage (2.0 - 314) <5613706F-710A-39E0-8B25-BA103A768613> /System/Library/PrivateFrameworks/GenerationalStorage.framework/Versions/A/GenerationalStorage
    0x7fff4fe9d000 -     0x7fff4feabffb  com.apple.GraphVisualizer (1.0 - 100.1) <0A86C9FF-4484-3C7F-BC71-3D23BDBE81CE> /System/Library/PrivateFrameworks/GraphVisualizer.framework/Versions/A/GraphVisualizer
    0x7fff5004a000 -     0x7fff50108ff4  com.apple.Heimdal (4.0 - 2.0) <F2C504F6-E211-3AB0-9754-D96D2F96634B> /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
    0x7fff52282000 -     0x7fff5228bffe  com.apple.IOAccelMemoryInfo (1.0 - 1) <903349F6-F3B0-3269-8946-2CE3E2C49E70> /System/Library/PrivateFrameworks/IOAccelMemoryInfo.framework/Versions/A/IOAccelMemoryInfo
    0x7fff5228c000 -     0x7fff52294ff5  com.apple.IOAccelerator (438.5.4 - 438.5.4) <A3CF45E0-4D88-33BF-BAEC-690D5664CDA0> /System/Library/PrivateFrameworks/IOAccelerator.framework/Versions/A/IOAccelerator
    0x7fff522a1000 -     0x7fff522b8fff  com.apple.IOPresentment (1.0 - 37) <3EDBB454-D248-394B-A026-9717CD8535C3> /System/Library/PrivateFrameworks/IOPresentment.framework/Versions/A/IOPresentment
    0x7fff52640000 -     0x7fff5268bff1  com.apple.IconServices (438.3 - 438.3) <2AE74790-64F1-3B0A-9534-DEEEE307E562> /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
    0x7fff52849000 -     0x7fff52850ff9  com.apple.InternationalSupport (1.0 - 45.4) <C22AA77A-EDA6-3626-8816-521A8CD43C4A> /System/Library/PrivateFrameworks/InternationalSupport.framework/Versions/A/InternationalSupport
    0x7fff52add000 -     0x7fff52afcffd  com.apple.security.KeychainCircle.KeychainCircle (1.0 - 1) <76DB5326-BE5D-3339-975C-D9FCF39A341E> /System/Library/PrivateFrameworks/KeychainCircle.framework/Versions/A/KeychainCircle
    0x7fff52c31000 -     0x7fff52cffffd  com.apple.LanguageModeling (1.0 - 215.1) <A6FAA215-9A01-3EE1-B304-2238801C5883> /System/Library/PrivateFrameworks/LanguageModeling.framework/Versions/A/LanguageModeling
    0x7fff52d00000 -     0x7fff52d48fff  com.apple.Lexicon-framework (1.0 - 72) <6AE1872C-0352-36FE-90CC-7303F13A5BEF> /System/Library/PrivateFrameworks/Lexicon.framework/Versions/A/Lexicon
    0x7fff52d4f000 -     0x7fff52d54ff3  com.apple.LinguisticData (1.0 - 353.18) <686E7B7C-640F-3D7B-A9C1-31E2DFACD457> /System/Library/PrivateFrameworks/LinguisticData.framework/Versions/A/LinguisticData
    0x7fff52df8000 -     0x7fff52dfdff7  com.apple.LoginUICore (4.0 - 4.0) <5D60C7D1-9DB7-30A3-9209-7E13644D3E9D> /System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/Frameworks/LoginUICore.framework/Versions/A/LoginUICore
    0x7fff535ec000 -     0x7fff535effff  com.apple.Mangrove (1.0 - 25) <11A30F47-B1C1-375E-9FE7-0A196E92A52C> /System/Library/PrivateFrameworks/Mangrove.framework/Versions/A/Mangrove
    0x7fff53858000 -     0x7fff538e2ff8  com.apple.MediaExperience (1.0 - 1) <34E15DA2-02AA-32FA-99E1-9A139521E226> /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
    0x7fff538e3000 -     0x7fff53916fff  com.apple.MediaKit (16 - 923) <14E38848-C9BD-37F1-AE44-FC4CC839E8A1> /System/Library/PrivateFrameworks/MediaKit.framework/Versions/A/MediaKit
    0x7fff540bb000 -     0x7fff54107fff  com.apple.spotlight.metadata.utilities (1.0 - 2076.6) <C3AEA22D-1FEB-3E38-9821-1FA447C8AF9D> /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
    0x7fff54108000 -     0x7fff541d9ffa  com.apple.gpusw.MetalTools (1.0 - 1) <A23FFAB6-437C-303C-A3E8-99F323F8E734> /System/Library/PrivateFrameworks/MetalTools.framework/Versions/A/MetalTools
    0x7fff54237000 -     0x7fff54250ff4  com.apple.MobileAssets (1.0 - 619.120.1) <5AF95641-68C7-351A-A317-3C7B793502D6> /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
    0x7fff54435000 -     0x7fff54453fff  com.apple.MobileKeyBag (2.0 - 1.0) <B564179F-A5E9-3BD8-892D-CEF2BE0DA0D7> /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
    0x7fff546b6000 -     0x7fff546e6ff7  com.apple.MultitouchSupport.framework (3440.1 - 3440.1) <4E7CB188-382E-3128-8671-4A3EF6E06622> /System/Library/PrivateFrameworks/MultitouchSupport.framework/Versions/A/MultitouchSupport
    0x7fff54be6000 -     0x7fff54bf0fff  com.apple.NetAuth (6.2 - 6.2) <D660F2CB-5A49-3DD0-9DB3-86EF0797828C> /System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth
    0x7fff55606000 -     0x7fff55651ffb  com.apple.OTSVG (1.0 - 643.1.5.1) <CD494F00-9AA4-3A48-916B-EA8661F9772D> /System/Library/PrivateFrameworks/OTSVG.framework/Versions/A/OTSVG
    0x7fff56865000 -     0x7fff56870ff2  com.apple.PerformanceAnalysis (1.243.2 - 243.2) <941698D6-EF00-3D59-8560-F160BC04B412> /System/Library/PrivateFrameworks/PerformanceAnalysis.framework/Versions/A/PerformanceAnalysis
    0x7fff56871000 -     0x7fff56899ffb  com.apple.persistentconnection (1.0 - 1.0) <FFC20BB6-9CF3-39F2-AE5C-8DEE348FE0C1> /System/Library/PrivateFrameworks/PersistentConnection.framework/Versions/A/PersistentConnection
    0x7fff5836d000 -     0x7fff58380ffc  com.apple.PowerLog (1.0 - 1) <63A89A9B-2ACC-3378-9BD0-7FA971E07C2A> /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
    0x7fff591fc000 -     0x7fff59256ff6  com.apple.ProtectedCloudStorage (1.0 - 1) <969BF7A2-E989-3A22-BC1B-72B72E107229> /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage
    0x7fff59257000 -     0x7fff59270ffb  com.apple.ProtocolBuffer (1 - 274.24.9.16.3) <A2E34123-7CED-378B-A43D-1B98B5B85F5C> /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
    0x7fff596cf000 -     0x7fff596f8ff1  com.apple.RemoteViewServices (2.0 - 148) <1C61CFC2-F76F-31E5-BA13-EFD5DC69C8D5> /System/Library/PrivateFrameworks/RemoteViewServices.framework/Versions/A/RemoteViewServices
    0x7fff5985d000 -     0x7fff59898ff0  com.apple.RunningBoardServices (1.0 - 223.100.31) <9FD1FC53-186A-3327-A359-B0BC7F4360EF> /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
    0x7fff5b178000 -     0x7fff5b17bff5  com.apple.SecCodeWrapper (4.0 - 448.100.6) <813B3E57-6A95-3D7B-9094-C65D687A72B8> /System/Library/PrivateFrameworks/SecCodeWrapper.framework/Versions/A/SecCodeWrapper
    0x7fff5b2ee000 -     0x7fff5b415ff0  com.apple.Sharing (1526.31 - 1526.31) <2CB07F08-7794-3BF2-9ED5-BAB5C55C9D2C> /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
    0x7fff5c828000 -     0x7fff5cb1eff7  com.apple.SkyLight (1.600.0 - 451.4) <F5B9065A-E975-36D1-8D53-9FBF02171FAB> /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
    0x7fff5d36b000 -     0x7fff5d379ffb  com.apple.SpeechRecognitionCore (6.0.91.2 - 6.0.91.2) <820602AB-117B-3C3E-B20B-819CBC97B7A4> /System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/SpeechRecognitionCore
    0x7fff5d43b000 -     0x7fff5d6c5ffe  com.apple.spotlight.index (10.7.0 - 2076.6) <38E208FE-A4E5-3B6C-9937-97CA152F1BB2> /System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex
    0x7fff5da53000 -     0x7fff5da94ff9  com.apple.StreamingZip (1.0 - 1) <EFCDDC94-28EE-3BCA-A105-0A928D15ED8C> /System/Library/PrivateFrameworks/StreamingZip.framework/Versions/A/StreamingZip
    0x7fff5dbab000 -     0x7fff5dbb4ff7  com.apple.SymptomDiagnosticReporter (1.0 - 1238.120.1) <581F31D6-94CB-38AA-BD56-1A63606E516E> /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter
    0x7fff5dc25000 -     0x7fff5dc4fffa  com.apple.framework.SystemAdministration (1.0 - 1.0) <926BB2F5-E02C-30B7-949A-20EFE57CF242> /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
    0x7fff5de6b000 -     0x7fff5de7bff3  com.apple.TCC (1.0 - 1) <FD146B21-6DC0-3B66-BB95-57A5016B1365> /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
    0x7fff5e3a0000 -     0x7fff5e466ff0  com.apple.TextureIO (3.10.9 - 3.10.9) <E23E05ED-8190-3564-985E-446F15CB0709> /System/Library/PrivateFrameworks/TextureIO.framework/Versions/A/TextureIO
    0x7fff5e5f2000 -     0x7fff5e5f3fff  com.apple.TrustEvaluationAgent (2.0 - 33) <11DF5A28-4410-36A8-B3B8-BF1094BE1544> /System/Library/PrivateFrameworks/TrustEvaluationAgent.framework/Versions/A/TrustEvaluationAgent
    0x7fff5e62b000 -     0x7fff5e883ff0  com.apple.UIFoundation (1.0 - 662) <DFD3DD4A-E661-3A12-BB02-06898949617D> /System/Library/PrivateFrameworks/UIFoundation.framework/Versions/A/UIFoundation
    0x7fff5f4f6000 -     0x7fff5f516ffc  com.apple.UserManagement (1.0 - 1) <E168206A-9DC1-3C67-A9A6-52D816DBD5B1> /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
    0x7fff602c2000 -     0x7fff603acff8  com.apple.ViewBridge (464.1 - 464.1) <C698BAC9-26C8-39F1-BBC0-F57EBD2EFD7B> /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
    0x7fff60552000 -     0x7fff60553fff  com.apple.WatchdogClient.framework (1.0 - 67.120.2) <3B8EBB6B-77D0-317C-A3DB-D0D2E294B18D> /System/Library/PrivateFrameworks/WatchdogClient.framework/Versions/A/WatchdogClient
    0x7fff61180000 -     0x7fff61183ffa  com.apple.dt.XCTTargetBootstrap (1.0 - 16091) <D4F09EC7-C63F-3861-B5DA-3F7C0DFF153D> /System/Library/PrivateFrameworks/XCTTargetBootstrap.framework/Versions/A/XCTTargetBootstrap
    0x7fff611fd000 -     0x7fff6120bff5  com.apple.audio.caulk (1.0 - 32.3) <7D3D2F91-8B1D-3558-B324-45BDF11306DB> /System/Library/PrivateFrameworks/caulk.framework/Versions/A/caulk
    0x7fff6154d000 -     0x7fff6154fff3  com.apple.loginsupport (1.0 - 1) <31F02734-1ECF-37D9-9DF6-7C3BC3A324FE> /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
    0x7fff61550000 -     0x7fff61563ffd  com.apple.login (3.0 - 3.0) <1DC570FD-29EC-3AE8-BD34-D44C00E4621B> /System/Library/PrivateFrameworks/login.framework/Versions/A/login
    0x7fff64033000 -     0x7fff64066ffa  libAudioToolboxUtility.dylib (1104.84) <BB234563-F952-3E7F-B630-4140DB5E0380> /usr/lib/libAudioToolboxUtility.dylib
    0x7fff6406d000 -     0x7fff640a1fff  libCRFSuite.dylib (48) <02C52318-C537-3FD8-BBC4-E5BD25430652> /usr/lib/libCRFSuite.dylib
    0x7fff640a4000 -     0x7fff640aefff  libChineseTokenizer.dylib (34) <04A7CB5A-FD68-398A-A206-33A510C115E7> /usr/lib/libChineseTokenizer.dylib
    0x7fff640af000 -     0x7fff64137fff  libCoreStorage.dylib (551) <BBD3B3DC-270D-35F2-8C67-4595A257EEBB> /usr/lib/libCoreStorage.dylib
    0x7fff6413a000 -     0x7fff6413cff7  libDiagnosticMessagesClient.dylib (112) <27220E98-6CE2-33E3-BD48-3CC3CE4AA036> /usr/lib/libDiagnosticMessagesClient.dylib
    0x7fff64182000 -     0x7fff64339ffb  libFosl_dynamic.dylib (100.4) <68038226-8CAA-36B5-B5D6-510F900B318D> /usr/lib/libFosl_dynamic.dylib
    0x7fff64360000 -     0x7fff64366ff3  libIOReport.dylib (54) <E3A2148E-C5B2-30A8-ACD3-E081DD02BE90> /usr/lib/libIOReport.dylib
    0x7fff64448000 -     0x7fff6444ffff  libMatch.1.dylib (36) <081FB6A9-0482-3697-A98B-6821FF476C6E> /usr/lib/libMatch.1.dylib
    0x7fff6447e000 -     0x7fff6449efff  libMobileGestalt.dylib (826.120.5) <1977AD00-533A-31AA-8D74-EA6CB962F668> /usr/lib/libMobileGestalt.dylib
    0x7fff64610000 -     0x7fff64611fff  libSystem.B.dylib (1281.100.1) <B6FDA8A9-3D2B-3BD5-B5B0-57D311C0FF3D> /usr/lib/libSystem.B.dylib
    0x7fff6469e000 -     0x7fff6469ffff  libThaiTokenizer.dylib (3) <97DC10ED-3C11-3C89-B366-299A644035E7> /usr/lib/libThaiTokenizer.dylib
    0x7fff646b7000 -     0x7fff646cdfff  libapple_nghttp2.dylib (1.39.2) <B99D7150-D4E2-31A2-A594-36DA4B90D558> /usr/lib/libapple_nghttp2.dylib
    0x7fff64702000 -     0x7fff64774ff7  libarchive.2.dylib (72.100.1) <20B70252-0C4B-3AFD-8C8D-F51921E9D324> /usr/lib/libarchive.2.dylib
    0x7fff64775000 -     0x7fff6480efe5  libate.dylib (3.0.1) <C4A5AE88-4E44-36FA-AD3E-0629AF9B94E0> /usr/lib/libate.dylib
    0x7fff64812000 -     0x7fff64812ff3  libauto.dylib (187) <85383E24-1592-36BC-BB39-308B7F1C826E> /usr/lib/libauto.dylib
    0x7fff648d8000 -     0x7fff648e8ffb  libbsm.0.dylib (60.100.1) <B2331E11-3CBB-3BCF-93A6-12627AE444D0> /usr/lib/libbsm.0.dylib
    0x7fff648e9000 -     0x7fff648f5fff  libbz2.1.0.dylib (44) <BF40E193-8856-39B7-98F8-7A17B328B1E9> /usr/lib/libbz2.1.0.dylib
    0x7fff648f6000 -     0x7fff64948fff  libc++.1.dylib (902.1) <AD0805FE-F98B-3E2F-B072-83782B22DAC9> /usr/lib/libc++.1.dylib
    0x7fff64949000 -     0x7fff6495effb  libc++abi.dylib (902) <771E9263-E832-3985-9477-8F1B2D73B771> /usr/lib/libc++abi.dylib
    0x7fff6495f000 -     0x7fff6495ffff  libcharset.1.dylib (59) <FF23D4ED-A5AD-3592-9574-48486C7DF85B> /usr/lib/libcharset.1.dylib
    0x7fff64960000 -     0x7fff64971fff  libcmph.dylib (8) <296A51E6-9661-3AC2-A1C9-F1E3510F91AA> /usr/lib/libcmph.dylib
    0x7fff64972000 -     0x7fff64989fd7  libcompression.dylib (87) <21F37C2E-B9AA-38CE-9023-B763C8828AC6> /usr/lib/libcompression.dylib
    0x7fff64c63000 -     0x7fff64c79ff7  libcoretls.dylib (167) <9E5D1E0C-03F8-37B6-82A1-0D0597021CB8> /usr/lib/libcoretls.dylib
    0x7fff64c7a000 -     0x7fff64c7bfff  libcoretls_cfhelpers.dylib (167) <C23BE09B-85D1-3744-9E7B-E2B11ACD5442> /usr/lib/libcoretls_cfhelpers.dylib
    0x7fff6511e000 -     0x7fff65222fef  libcrypto.44.dylib (47.120.1) <B48C0D1A-CDCB-34E4-921E-00EBFF1208DE> /usr/lib/libcrypto.44.dylib
    0x7fff65225000 -     0x7fff65230fff  libcsfde.dylib (551) <8FBB94EC-712C-3C0F-A8A9-88EE5F4679EF> /usr/lib/libcsfde.dylib
    0x7fff65238000 -     0x7fff65297ff7  libcups.2.dylib (483.6) <FFE8FE67-A6CC-3C38-A9D7-D411D7B562F1> /usr/lib/libcups.2.dylib
    0x7fff65299000 -     0x7fff652feff7  libcurl.4.dylib (118.120.2) <F2C246F3-460E-31A7-B900-2A9560533730> /usr/lib/libcurl.4.dylib
    0x7fff653a1000 -     0x7fff653a1fff  libenergytrace.dylib (21) <DBF8BDEE-7229-3F06-AC10-A28DCC4243C0> /usr/lib/libenergytrace.dylib
    0x7fff653a2000 -     0x7fff653bafff  libexpat.1.dylib (19.60.2) <C9163264-BA81-3CC6-9B8C-48A9A0709DD5> /usr/lib/libexpat.1.dylib
    0x7fff653c8000 -     0x7fff653cafff  libfakelink.dylib (149.1) <122F530F-F10E-3DD5-BBEA-91796BE583F3> /usr/lib/libfakelink.dylib
    0x7fff653d9000 -     0x7fff653defff  libgermantok.dylib (24) <DD279BF6-E906-30D3-A69E-DC797E95F147> /usr/lib/libgermantok.dylib
    0x7fff653df000 -     0x7fff653e8ff7  libheimdal-asn1.dylib (564.100.1) <68FA1BE5-8FFC-3345-8980-8D8629EBA451> /usr/lib/libheimdal-asn1.dylib
    0x7fff653e9000 -     0x7fff654d9fff  libiconv.2.dylib (59) <F58FED71-6CCA-30E8-9A51-13E9B46E568D> /usr/lib/libiconv.2.dylib
    0x7fff654da000 -     0x7fff65731fff  libicucore.A.dylib (64260.0.1) <7B9204AC-EA14-3FF3-B6B9-4C85B37EED79> /usr/lib/libicucore.A.dylib
    0x7fff6574b000 -     0x7fff6574cfff  liblangid.dylib (133) <36581D30-1C7B-3A58-AA07-36237BD75E0E> /usr/lib/liblangid.dylib
    0x7fff6574d000 -     0x7fff65765ff3  liblzma.5.dylib (16) <4DB30730-DBD1-3503-957A-D604049B98F9> /usr/lib/liblzma.5.dylib
    0x7fff6577d000 -     0x7fff65824ff7  libmecab.dylib (883.11) <66AD729B-2BCC-3347-B9B3-FD88570E884D> /usr/lib/libmecab.dylib
    0x7fff65825000 -     0x7fff65a87ff1  libmecabra.dylib (883.11) <2AE744D2-AC95-3720-8E66-4F9C7A79384C> /usr/lib/libmecabra.dylib
    0x7fff65df4000 -     0x7fff65e23fff  libncurses.5.4.dylib (57) <B0B09D08-A7C9-38E9-8BF4-E4F4882F93A6> /usr/lib/libncurses.5.4.dylib
    0x7fff65f53000 -     0x7fff663cfff5  libnetwork.dylib (1880.120.4) <715FB943-BA01-351C-BEA6-121970472985> /usr/lib/libnetwork.dylib
    0x7fff66470000 -     0x7fff664a3fde  libobjc.A.dylib (787.1) <CA836D3E-4595-33F1-B70C-7E39A3FBBE16> /usr/lib/libobjc.A.dylib
    0x7fff664a4000 -     0x7fff664a5ff7  libodfde.dylib (26) <2DDA61BF-E92A-3463-B1C4-D59E40D34D34> /usr/lib/libodfde.dylib
    0x7fff664b6000 -     0x7fff664bafff  libpam.2.dylib (25.100.1) <732E8D8E-C630-3EC2-B6C3-A1564E3B68B8> /usr/lib/libpam.2.dylib
    0x7fff664bd000 -     0x7fff664f3ff7  libpcap.A.dylib (89.120.1) <CF2ADF15-2D44-3A35-94B4-DD24052F9B23> /usr/lib/libpcap.A.dylib
    0x7fff66577000 -     0x7fff6658ffff  libresolv.9.dylib (67.40.1) <B0F5D204-7EF2-3B0B-90EF-BB4D196FCC62> /usr/lib/libresolv.9.dylib
    0x7fff66591000 -     0x7fff665d5ff7  libsandbox.1.dylib (1217.120.7) <728BC15F-9A6C-3634-9427-60C01CB5A5D6> /usr/lib/libsandbox.1.dylib
    0x7fff665d6000 -     0x7fff665e8ff7  libsasl2.2.dylib (213.120.1) <E6375405-168D-3B75-8042-C8B329D01AB9> /usr/lib/libsasl2.2.dylib
    0x7fff665e9000 -     0x7fff665eaff7  libspindump.dylib (281.3) <0C3A8B48-DC31-3F61-B4CC-746157042D0E> /usr/lib/libspindump.dylib
    0x7fff665eb000 -     0x7fff667d5ff7  libsqlite3.dylib (308.5) <AF518115-4AD1-39F2-9B82-E2640E2221E1> /usr/lib/libsqlite3.dylib
    0x7fff668c9000 -     0x7fff668f6ffb  libssl.46.dylib (47.120.1) <6209494A-4AAD-344E-992C-03ACD2D4C402> /usr/lib/libssl.46.dylib
    0x7fff66a26000 -     0x7fff66a29ffb  libutil.dylib (57) <D33B63D2-ADC2-38BD-B8F2-24056C41E07B> /usr/lib/libutil.dylib
    0x7fff66a2a000 -     0x7fff66a37ff7  libxar.1.dylib (425.2) <943A4CBB-331B-3A04-A11F-A2301189D40B> /usr/lib/libxar.1.dylib
    0x7fff66a3d000 -     0x7fff66b1fff7  libxml2.2.dylib (33.3) <262EF7C6-7D83-3C01-863F-36E97F5ACD34> /usr/lib/libxml2.2.dylib
    0x7fff66b23000 -     0x7fff66b4bfff  libxslt.1.dylib (16.9) <86FE4382-BD77-3C19-A678-11EBCD70685A> /usr/lib/libxslt.1.dylib
    0x7fff66b4c000 -     0x7fff66b5eff3  libz.1.dylib (76) <DB120508-3BED-37A8-B439-5235EAB4618A> /usr/lib/libz.1.dylib
    0x7fff6740c000 -     0x7fff67411ff3  libcache.dylib (83) <A5ECC751-A681-30D8-B33C-D192C15D25C8> /usr/lib/system/libcache.dylib
    0x7fff67412000 -     0x7fff6741dfff  libcommonCrypto.dylib (60165.120.1) <C321A74A-AA91-3785-BEBF-BEDC6975026C> /usr/lib/system/libcommonCrypto.dylib
    0x7fff6741e000 -     0x7fff67425fff  libcompiler_rt.dylib (101.2) <652A6012-7E5C-3F4F-9438-86BC094526F3> /usr/lib/system/libcompiler_rt.dylib
    0x7fff67426000 -     0x7fff6742fff7  libcopyfile.dylib (166.40.1) <40113A69-A81C-3397-ADC6-1D16B9A22C3E> /usr/lib/system/libcopyfile.dylib
    0x7fff67430000 -     0x7fff674c2fe3  libcorecrypto.dylib (866.120.3) <5E4B0E50-24DD-3E04-9374-EDA9FFD6257B> /usr/lib/system/libcorecrypto.dylib
    0x7fff675cf000 -     0x7fff6760fff0  libdispatch.dylib (1173.100.2) <201EDBF3-0B36-31BA-A7CB-443CE35C05D4> /usr/lib/system/libdispatch.dylib
    0x7fff67610000 -     0x7fff67646fff  libdyld.dylib (750.5) <7E711A46-5E4D-393C-AEA6-440E2A5CCD0C> /usr/lib/system/libdyld.dylib
    0x7fff67647000 -     0x7fff67647ffb  libkeymgr.dylib (30) <52662CAA-DB1F-30A3-BE13-D6274B1A6D7B> /usr/lib/system/libkeymgr.dylib
    0x7fff67648000 -     0x7fff67654ff3  libkxld.dylib (6153.121.2) <5EBB4886-C7B6-31D6-AA63-D861B2D58FCE> /usr/lib/system/libkxld.dylib
    0x7fff67655000 -     0x7fff67655ff7  liblaunch.dylib (1738.120.8) <07CF647B-F9DC-3907-AD98-2F85FCB34A72> /usr/lib/system/liblaunch.dylib
    0x7fff67656000 -     0x7fff6765bff7  libmacho.dylib (959.0.1) <D91DFF00-E22F-3796-8A1C-4C1F5F8FA03C> /usr/lib/system/libmacho.dylib
    0x7fff6765c000 -     0x7fff6765eff3  libquarantine.dylib (110.40.3) <D3B7D02C-7646-3FB4-8529-B36DCC2419EA> /usr/lib/system/libquarantine.dylib
    0x7fff6765f000 -     0x7fff67660ff7  libremovefile.dylib (48) <B5E88D9B-C2BE-3496-BBB2-C996317E18A3> /usr/lib/system/libremovefile.dylib
    0x7fff67661000 -     0x7fff67678ff3  libsystem_asl.dylib (377.60.2) <1170348D-2491-33F1-AA79-E2A05B4A287C> /usr/lib/system/libsystem_asl.dylib
    0x7fff67679000 -     0x7fff67679ff7  libsystem_blocks.dylib (74) <7AFBCAA6-81BE-36C3-8DB0-AAE0A4ACE4C5> /usr/lib/system/libsystem_blocks.dylib
    0x7fff6767a000 -     0x7fff67701fff  libsystem_c.dylib (1353.100.2) <935DDCE9-4ED0-3F79-A05A-A123DDE399CC> /usr/lib/system/libsystem_c.dylib
    0x7fff67702000 -     0x7fff67705ffb  libsystem_configuration.dylib (1061.120.2) <EA9BC2B1-5001-3463-9FAF-39FF61CAC87C> /usr/lib/system/libsystem_configuration.dylib
    0x7fff67706000 -     0x7fff67709fff  libsystem_coreservices.dylib (114) <3D0A3AA8-8415-37B2-AAE3-66C03BCE8B55> /usr/lib/system/libsystem_coreservices.dylib
    0x7fff6770a000 -     0x7fff67712fff  libsystem_darwin.dylib (1353.100.2) <6EEC9975-EE3B-3C95-AA5B-030FD10587BC> /usr/lib/system/libsystem_darwin.dylib
    0x7fff67713000 -     0x7fff6771afff  libsystem_dnssd.dylib (1096.100.3) <0115092A-E61B-317D-8670-41C7C34B1A82> /usr/lib/system/libsystem_dnssd.dylib
    0x7fff6771b000 -     0x7fff6771cffb  libsystem_featureflags.dylib (17) <AFDB5095-0472-34AC-BA7E-497921BF030A> /usr/lib/system/libsystem_featureflags.dylib
    0x7fff6771d000 -     0x7fff6776aff7  libsystem_info.dylib (538) <851693E9-C079-3547-AD41-353F8C248BE8> /usr/lib/system/libsystem_info.dylib
    0x7fff6776b000 -     0x7fff67797ff7  libsystem_kernel.dylib (6153.121.2) <9F9902C9-A46F-3CA9-B7F9-5CCFE98FBF75> /usr/lib/system/libsystem_kernel.dylib
    0x7fff67798000 -     0x7fff677dffff  libsystem_m.dylib (3178) <436CFF76-6A99-36F2-A3B6-8D017396A050> /usr/lib/system/libsystem_m.dylib
    0x7fff677e0000 -     0x7fff67807fff  libsystem_malloc.dylib (283.100.6) <D4BA7DF2-57AC-33B0-B948-A688EE43C799> /usr/lib/system/libsystem_malloc.dylib
    0x7fff67808000 -     0x7fff67815ffb  libsystem_networkextension.dylib (1095.120.6) <6DE86DB0-8CD2-361E-BD6A-A34282B47847> /usr/lib/system/libsystem_networkextension.dylib
    0x7fff67816000 -     0x7fff6781fff7  libsystem_notify.dylib (241.100.2) <7E9E2FC8-DF26-340C-B196-B81B11850C46> /usr/lib/system/libsystem_notify.dylib
    0x7fff67820000 -     0x7fff67828fef  libsystem_platform.dylib (220.100.1) <736920EA-6AE0-3B1B-BBDA-7DCDF0C229DF> /usr/lib/system/libsystem_platform.dylib
    0x7fff67829000 -     0x7fff67833fff  libsystem_pthread.dylib (416.100.3) <77488669-19A3-3993-AD65-CA5377E2475A> /usr/lib/system/libsystem_pthread.dylib
    0x7fff67834000 -     0x7fff67838ff3  libsystem_sandbox.dylib (1217.120.7) <20C93D69-6452-3C82-9521-8AE54345C66F> /usr/lib/system/libsystem_sandbox.dylib
    0x7fff67839000 -     0x7fff6783bfff  libsystem_secinit.dylib (62.100.2) <E851113D-D5B1-3FB0-9D29-9C7647A71961> /usr/lib/system/libsystem_secinit.dylib
    0x7fff6783c000 -     0x7fff67843ffb  libsystem_symptoms.dylib (1238.120.1) <25C3866B-004E-3621-9CD3-B1E9C4D887EB> /usr/lib/system/libsystem_symptoms.dylib
    0x7fff67844000 -     0x7fff6785aff2  libsystem_trace.dylib (1147.120) <A1ED1D3A-5FAD-3559-A1D6-1BE4E1C5756A> /usr/lib/system/libsystem_trace.dylib
    0x7fff6785c000 -     0x7fff67861ff7  libunwind.dylib (35.4) <253A12E2-F88F-3838-A666-C5306F833CB8> /usr/lib/system/libunwind.dylib
    0x7fff67862000 -     0x7fff67897ffe  libxpc.dylib (1738.120.8) <68D433B6-DCFF-385D-8620-F847FB7D4A5A> /usr/lib/system/libxpc.dylib

External Modification Summary:
  Calls made by other processes targeting this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by this process:
    task_for_pid: 0
    thread_create: 0
    thread_set_state: 0
  Calls made by all processes on this machine:
    task_for_pid: 968
    thread_create: 0
    thread_set_state: 0

VM Region Summary:
ReadOnly portion of Libraries: Total=705.7M resident=0K(0%) swapped_out_or_unallocated=705.7M(100%)
Writable regions: Total=1.0G written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=1.0G(100%)
 
                                VIRTUAL   REGION 
REGION TYPE                        SIZE    COUNT (non-coalesced) 
===========                     =======  ======= 
Accelerate framework               256K        2 
Activity Tracing                   256K        1 
CG backing stores                 25.5M        5 
CG image                            60K        1 
CoreAnimation                      112K        8 
CoreGraphics                         8K        1 
CoreImage                           32K        4 
CoreUI image data                  444K        4 
Foundation                          32K        2 
IOKit                             15.5M        2 
JS JIT generated code              668K      153 
JS VM Gigacage                    16.0M        4 
JS VM Isolated Heap               6400K        5 
Kernel Alloc Once                    8K        1 
MALLOC                           625.3M      241 
MALLOC guard page                   32K        7 
MALLOC_LARGE (reserved)           1708K        1         reserved VM address space (unallocated)
MALLOC_NANO (reserved)           256.0M        1         reserved VM address space (unallocated)
Memory Tag 242                      12K        1 
OpenGL GLSL                        256K        3 
STACK GUARD                       56.1M       28 
Stack                             71.2M       29 
VM_ALLOCATE                       9048K      245 
VM_ALLOCATE (reserved)              16K        1         reserved VM address space (unallocated)
__DATA                            44.0M      394 
__DATA_CONST                        76K        2 
__FONT_DATA                          4K        1 
__GLSLBUILTINS                    5176K        1 
__LINKEDIT                       400.9M       70 
__OBJC_RO                         32.2M        1 
__OBJC_RW                         1892K        2 
__TEXT                           304.8M      373 
__UNICODE                          564K        1 
mapped file                      591.1M      255 
shared memory                      652K       18 
===========                     =======  ======= 
TOTAL                              2.4G     1868 
TOTAL, minus reserved VM space     2.2G     1868 

Model: MacBookPro15,1, BootROM 1037.120.87.0.0 (iBridge: 17.16.15300.0.0,0), 6 processors, 6-Core Intel Core i7, 2.2 GHz, 16 GB, SMC 
Graphics: kHW_IntelUHDGraphics630Item, Intel UHD Graphics 630, spdisplays_builtin
Graphics: kHW_AMDRadeonPro555XItem, Radeon Pro 555X, spdisplays_pcie_device, 4 GB
Memory Module: BANK 0/ChannelA-DIMM0, 8 GB, DDR4, 2400 MHz, Micron, 8ATF1G64HZ-2G6E1
Memory Module: BANK 2/ChannelB-DIMM0, 8 GB, DDR4, 2400 MHz, Micron, 8ATF1G64HZ-2G6E1
AirPort: spairport_wireless_card_type_airport_extreme (0x14E4, 0x7BF), wl0: Feb 28 2020 15:24:56 version 9.30.357.35.32.5.47 FWID 01-9ce4adf3
Bluetooth: Version 7.0.5f6, 3 services, 27 devices, 1 incoming serial ports
Network Service: Wi-Fi, AirPort, en0
USB Device: USB3.0 Hub
USB Device: USB 3.1 Bus
USB Device: USB2.0 Hub
USB Device: USB 2.0 BILLBOARD
USB Device: Apple T2 Bus
USB Device: Touch Bar Backlight
USB Device: Touch Bar Display
USB Device: Apple Internal Keyboard / Trackpad
USB Device: Headset
USB Device: Ambient Light Sensor
USB Device: FaceTime HD Camera (Built-in)
USB Device: Apple T2 Controller
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.4
Thunderbolt Bus: MacBook Pro, Apple Inc., 47.4


# Discussion History
## alexwolf22 | 2020-10-15T01:28:22+00:00
Seems like it's there's something with the wallet. I was able to create a new one and use the app.

ANy idea how to fix this?

## xiphon | 2020-10-15T01:37:20+00:00
According to the stack trace the wallet got corrupted

## alexwolf22 | 2020-10-15T01:42:41+00:00
Hmm, I am new to Moreno. Is it possible to recover the wallet with my mnemonic and restore the funds?

## xiphon | 2020-10-15T01:47:33+00:00
Shouldn't happen again with v0.17.1.0.

We fixed wallet corruption case in v0.17.1.0 (the bug existed in the version you used initially v0.17.0.1).
There were other changes in wallet serialization format recently. Although they are backward-compatible.

> Hmm, I am new to Moreno. Is it possible to recover the wallet with my mnemonic and restore the funds?

Sure, navigate to the `Welcome to Monero` screen, then `Restore wallet from keys or mnemonic seed`.

## alexwolf22 | 2020-10-15T03:55:25+00:00
Okay that did the trick thanks! Yeah unsure what caused it to get corrupted but hopefully it was because I sued the old version of the software.

Have a good one.

Cheers,
Alex

## SamAlexander007 | 2024-10-20T10:56:38+00:00
#4367 

# Action History
- Created by: alexwolf22 | 2020-10-15T01:25:49+00:00
- Closed at: 2020-10-15T03:55:25+00:00
