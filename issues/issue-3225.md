---
title: Segmentation fault in QQmlApplicationEngine::load
source_url: https://github.com/monero-project/monero-gui/issues/3225
author: glv2
assignees: []
labels: []
created_at: '2020-11-11T09:22:30+00:00'
updated_at: '2020-11-11T13:11:29+00:00'
type: issue
status: closed
closed_at: '2020-11-11T13:11:29+00:00'
---

# Original Description
Hi!
When launching monero-wallet-gui in GNU Guix, it craches because of a segmentation fault error.
I tried Guix packages for versions 0.17.1.1, 0.17.1.3 and 0.17.1.4, and they all crash in the same way.
It looks like the crash happens inside the ```engine.load(QUrl(QStringLiteral("qrc:///main.qml")))``` call in "src/main/main.cpp".

Does someone have an idea what could cause that issue?

System info:
 - GNU/Linux 5.9.6 x86-64
 - glibc 2.31
 - gcc 7.5.0
 - Qt 5.14.2

Backtrace:
``` gdb
(gdb) run
Starting program: /gnu/store/ma8a0lm0x67y0vjyax7s57pn2m1vl9g6-monero-gui-0.17.1.4/bin/.monero-wallet-gui-real 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/gnu/store/fa6wj5bxkj5ll1d7292a70knmyl7a0cr-glibc-2.31/lib/libthread_db.so.1".
[New Thread 0x7ffff1793700 (LWP 12945)]
2020-11-11 08:51:12.971	W Qt:5.14.2 GUI:0.17.1.4 | screen: 1920x1080 - dpi: 96.1263 - ratio:0.999421
[New Thread 0x7ffff0ef6700 (LWP 12946)]

Thread 3 "QQmlThread" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffff0ef6700 (LWP 12946)]
0x00007ffff62e1e65 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
(gdb) thread apply all bt

Thread 3 (Thread 0x7ffff0ef6700 (LWP 12946) "QQmlThread"):
#0  0x00007ffff62e1e65 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#1  0x00007ffff62e2115 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#2  0x00007ffff62e2115 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#3  0x00007ffff62e2115 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#4  0x00007ffff62de80d in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#5  0x00007ffff6236254 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#6  0x00007ffff6239dfa in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#7  0x00007ffff62269f5 in QQmlDataBlob::tryDone() () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#8  0x00007ffff62806ad in QQmlTypeLoader::setData(QQmlDataBlob*, QQmlDataBlob::SourceCodeData const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#9  0x00007ffff62809a4 in QQmlTypeLoader::setData(QQmlDataBlob*, QString const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#10 0x00007ffff6280fe5 in QQmlTypeLoader::loadThread(QQmlDataBlob*) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#11 0x00007ffff62881ec in void QQmlTypeLoader::doLoad<PlainLoader>(PlainLoader const&, QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#12 0x00007ffff6281196 in QQmlTypeLoader::load(QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#13 0x00007ffff6283be9 in QQmlTypeLoader::getType(QUrl const&, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#14 0x00007ffff6239236 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#15 0x00007ffff623aa3d in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#16 0x00007ffff6280739 in QQmlTypeLoader::setData(QQmlDataBlob*, QQmlDataBlob::SourceCodeData const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#17 0x00007ffff62809a4 in QQmlTypeLoader::setData(QQmlDataBlob*, QString const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#18 0x00007ffff6280fe5 in QQmlTypeLoader::loadThread(QQmlDataBlob*) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#19 0x00007ffff62881ec in void QQmlTypeLoader::doLoad<PlainLoader>(PlainLoader const&, QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#20 0x00007ffff6281196 in QQmlTypeLoader::load(QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#21 0x00007ffff6283be9 in QQmlTypeLoader::getType(QUrl const&, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#22 0x00007ffff6239236 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#23 0x00007ffff623aa3d in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#24 0x00007ffff6280739 in QQmlTypeLoader::setData(QQmlDataBlob*, QQmlDataBlob::SourceCodeData const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#25 0x00007ffff62809a4 in QQmlTypeLoader::setData(QQmlDataBlob*, QString const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#26 0x00007ffff6280fe5 in QQmlTypeLoader::loadThread(QQmlDataBlob*) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#27 0x00007ffff62881ec in void QQmlTypeLoader::doLoad<PlainLoader>(PlainLoader const&, QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#28 0x00007ffff6281196 in QQmlTypeLoader::load(QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#29 0x00007ffff6283be9 in QQmlTypeLoader::getType(QUrl const&, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#30 0x00007ffff6239236 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#31 0x00007ffff623aa3d in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#32 0x00007ffff6280739 in QQmlTypeLoader::setData(QQmlDataBlob*, QQmlDataBlob::SourceCodeData const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#33 0x00007ffff62809a4 in QQmlTypeLoader::setData(QQmlDataBlob*, QString const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#34 0x00007ffff6280fe5 in QQmlTypeLoader::loadThread(QQmlDataBlob*) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#35 0x00007ffff624243d in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#36 0x00007ffff62f97d4 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#37 0x00007ffff62f9eaa in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#38 0x00007ffff6d3bbfc in QApplicationPrivate::notify_helper(QObject*, QEvent*) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Widgets.so.5
#39 0x00007ffff6d4292f in QApplication::notify(QObject*, QEvent*) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Widgets.so.5
#40 0x00007ffff5b7eff8 in QCoreApplication::notifyInternal2(QObject*, QEvent*) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#41 0x00007ffff5b81ad1 in QCoreApplicationPrivate::sendPostedEvents(QObject*, int, QThreadData*) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#42 0x00007ffff5bdb553 in ?? () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#43 0x00007ffff240eeda in g_main_context_dispatch () from /gnu/store/xa1vfhfc42x655hi7vxqmbyvwldnz7r0-glib-2.62.6/lib/libglib-2.0.so.0
#44 0x00007ffff240f0d8 in g_main_context_iterate.isra () from /gnu/store/xa1vfhfc42x655hi7vxqmbyvwldnz7r0-glib-2.62.6/lib/libglib-2.0.so.0
#45 0x00007ffff240f15c in g_main_context_iteration () from /gnu/store/xa1vfhfc42x655hi7vxqmbyvwldnz7r0-glib-2.62.6/lib/libglib-2.0.so.0
#46 0x00007ffff5bdac4c in QEventDispatcherGlib::processEvents(QFlags<QEventLoop::ProcessEventsFlag>) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#47 0x00007ffff5b7d9ba in QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#48 0x00007ffff599f5b7 in QThread::exec() () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#49 0x00007ffff62f9495 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#50 0x00007ffff59a09a9 in ?? () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#51 0x00007ffff4cb1f64 in start_thread () from /gnu/store/fa6wj5bxkj5ll1d7292a70knmyl7a0cr-glibc-2.31/lib/libpthread.so.0
#52 0x00007ffff4be39af in clone () from /gnu/store/fa6wj5bxkj5ll1d7292a70knmyl7a0cr-glibc-2.31/lib/libc.so.6

Thread 2 (Thread 0x7ffff1793700 (LWP 12945) "QXcbEventQueue"):
#0  0x00007ffff4bd99d9 in poll () from /gnu/store/fa6wj5bxkj5ll1d7292a70knmyl7a0cr-glibc-2.31/lib/libc.so.6
#1  0x00007ffff1fd6cc7 in _xcb_conn_wait () from /gnu/store/a8gdwnmpryd39jixzy4xs9p4i7gy17qv-libxcb-1.14/lib/libxcb.so.1
#2  0x00007ffff1fd888a in xcb_wait_for_event () from /gnu/store/a8gdwnmpryd39jixzy4xs9p4i7gy17qv-libxcb-1.14/lib/libxcb.so.1
#3  0x00007ffff1e76620 in ?? () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/qt5/plugins/xcbglintegrations/../../../libQt5XcbQpa.so.5
#4  0x00007ffff59a09a9 in ?? () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#5  0x00007ffff4cb1f64 in start_thread () from /gnu/store/fa6wj5bxkj5ll1d7292a70knmyl7a0cr-glibc-2.31/lib/libpthread.so.0
#6  0x00007ffff4be39af in clone () from /gnu/store/fa6wj5bxkj5ll1d7292a70knmyl7a0cr-glibc-2.31/lib/libc.so.6

Thread 1 (Thread 0x7ffff1ac73c0 (LWP 12941) ".monero-wallet-"):
#0  0x00007ffff4cb894c in pthread_cond_wait@@GLIBC_2.3.2 () from /gnu/store/fa6wj5bxkj5ll1d7292a70knmyl7a0cr-glibc-2.31/lib/libpthread.so.0
#1  0x00007ffff59a6b43 in QWaitCondition::wait(QMutex*, QDeadlineTimer) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#2  0x00007ffff59a6c99 in QWaitCondition::wait(QMutex*, unsigned long) () from /gnu/store/0s3yw8xya1j9wdjgirq76xfwf6apak5x-qtbase-5.14.2/lib/libQt5Core.so.5
#3  0x00007ffff62f9b41 in ?? () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#4  0x00007ffff6288195 in void QQmlTypeLoader::doLoad<PlainLoader>(PlainLoader const&, QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#5  0x00007ffff6281196 in QQmlTypeLoader::load(QQmlDataBlob*, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#6  0x00007ffff6283be9 in QQmlTypeLoader::getType(QUrl const&, QQmlTypeLoader::Mode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#7  0x00007ffff625e032 in QQmlComponentPrivate::loadUrl(QUrl const&, QQmlComponent::CompilationMode) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#8  0x00007ffff62c42b3 in QQmlApplicationEnginePrivate::startLoad(QUrl const&, QByteArray const&, bool) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#9  0x00007ffff62c4300 in QQmlApplicationEngine::load(QUrl const&) () from /gnu/store/7kvjzki8f30gm1cban3ng8cdapzz880k-qtdeclarative-5.14.2/lib/libQt5Qml.so.5
#10 0x0000555555688865 in main (argc=<optimized out>, argv=<optimized out>) at /tmp/guix-build-monero-gui-0.17.1.4.drv-0/source/src/main/main.cpp:499
```


# Discussion History
## selsta | 2020-11-11T09:23:46+00:00
Please test the getmonero.org binaries.

## glv2 | 2020-11-11T10:16:27+00:00
I managed to run the binary from getmonero.org on Guix (by modify it with patchelf to set a rpath to find the system libraries and to change the interpreter path) and the segmentation fault error does not happen.

I noticed that it uses Qt 5.9.9 whereas my Guix package uses Qt 5.14.2. Could that cause the crash?


## selsta | 2020-11-11T10:34:45+00:00
Probably best to report this to the Guix maintainer if possible.

Qt 5.14.2 should be fine.

## glv2 | 2020-11-11T13:09:34+00:00
Apparently the issue came from the QML cache files. I removed everything in ```$HOME/.cache/monero-project/monero-core/qmlcache/```, and now monero-wallet-gui is working fine again.


# Action History
- Created by: glv2 | 2020-11-11T09:22:30+00:00
- Closed at: 2020-11-11T13:11:29+00:00
