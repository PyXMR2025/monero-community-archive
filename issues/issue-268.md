---
title: Monero-GUI segfault on close
source_url: https://github.com/seraphis-migration/monero/issues/268
author: ComputeryPony
assignees: []
labels: []
created_at: '2025-12-16T23:03:52+00:00'
updated_at: '2025-12-17T19:36:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This may not be related to the fcmp++ work but I have experienced occasianal crashes on closing the gui wallet.
When this happens I see `munmap_chunk(): invalid pointer` followed by a segfault.
I changed my script to launch monero-gui to always launch it attached to gdb and today I happened to have it crash again while attached.

Segfault at:
```
QHashData::nextNode (node=0x55556169a950) at tools/qhash.cpp:591                                                                                                                                                                                                               
591         if (next->next)
```

Backtrace:
```
#0  QHashData::nextNode (node=0x55556169a950) at tools/qhash.cpp:591
#1  0x00007ffff5ca12fd in QHash<QModelIndex, QSortFilterProxyModelPrivate::Mapping*>::const_iterator::operator++ (this=<synthetic pointer>) at ../../include/QtCore/../../src/corelib/tools/qhash.h:425
#2  qDeleteAll<QHash<QModelIndex, QSortFilterProxyModelPrivate::Mapping*>::const_iterator> (begin=..., end=...) at ../../include/QtCore/../../src/corelib/tools/qalgorithms.h:321
#3  qDeleteAll<QHash<QModelIndex, QSortFilterProxyModelPrivate::Mapping*> > (c=...) at ../../include/QtCore/../../src/corelib/tools/qalgorithms.h:328
#4  QSortFilterProxyModel::~QSortFilterProxyModel (this=0x555561699120, this=<optimized out>) at itemmodels/qsortfilterproxymodel.cpp:2063
#5  0x0000555555821f43 in TransactionHistorySortFilterModel::~TransactionHistorySortFilterModel (this=0x555561699120)
    at /monero-gui/build/src/monero-wallet-gui_autogen/NLOY5YBGEN/../../../../src/model/TransactionHistorySortFilterModel.h:42
#6  TransactionHistorySortFilterModel::~TransactionHistorySortFilterModel (this=0x555561699120) at /monero-gui/build/src/monero-wallet-gui_autogen/NLOY5YBGEN/../../../../src/model/TransactionHistorySortFilterModel.h:42
#7  0x00007ffff5cf78eb in QObjectPrivate::deleteChildren (this=this@entry=0x7fffc0001930) at kernel/qobject.cpp:2137
#8  0x00007ffff5cfbe67 in QObject::~QObject (this=<optimized out>, this=<optimized out>) at kernel/qobject.cpp:1115
#9  0x000055555585b322 in Wallet::~Wallet (this=0x7fffc0bc5ab0) at /monero-gui/src/libwalletqt/Wallet.cpp:1221
#10 0x000055555585faf2 in WalletManager::closeWallet (this=0x55555cca8ed0) at /monero-gui/src/libwalletqt/WalletManager.cpp:221
#11 0x00005555558642a0 in operator() (__closure=<optimized out>) at /monero-gui/src/libwalletqt/WalletManager.cpp:232
#12 std::__invoke_impl<QList<QJSValue>, WalletManager::closeWalletAsync(const QJSValue&)::<lambda()>&> (__f=<optimized out>) at /usr/include/c++/15.2.1/bits/invoke.h:63
#13 std::__invoke_r<QList<QJSValue>, WalletManager::closeWalletAsync(const QJSValue&)::<lambda()>&> (__fn=<optimized out>) at /usr/include/c++/15.2.1/bits/invoke.h:118
#14 std::_Function_handler<QList<QJSValue>(), WalletManager::closeWalletAsync(const QJSValue&)::<lambda()> >::_M_invoke(const std::_Any_data &) (__functor=<optimized out>) at /usr/include/c++/15.2.1/bits/std_function.h:293
#15 0x0000555555884f31 in std::function<QList<QJSValue>()>::operator() (this=0x555561678eb0) at /usr/include/c++/15.2.1/bits/std_function.h:593
#16 operator() (__closure=0x555561678ea8) at /monero-gui/src/qt/FutureScheduler.cpp:64
#17 QtConcurrent::StoredFunctorCall0<QList<QJSValue>, FutureScheduler::run(std::function<QList<QJSValue>()>, const QJSValue&)::<lambda(QFutureWatcher<QList<QJSValue> >*)>::<lambda()> >::runFunctor (this=0x555561678e80)
    at /usr/include/qt/QtConcurrent/qtconcurrentstoredfunctioncall.h:60
#18 QtConcurrent::RunFunctionTask<QList<QJSValue> >::run (this=0x555561678e80) at /usr/include/qt/QtConcurrent/qtconcurrentrunbase.h:114
#19 0x00007ffff5af6365 in QThreadPoolThread::run (this=0x555557f78e60) at thread/qthreadpool.cpp:100
#20 0x00007ffff5af19b9 in operator() (__closure=<optimized out>) at thread/qthread_unix.cpp:350
#21 (anonymous namespace)::terminate_on_exception<QThreadPrivate::start(void*)::<lambda()> > (t=<optimized out>) at thread/qthread_unix.cpp:287
#22 QThreadPrivate::start (arg=0x555557f78e60) at thread/qthread_unix.cpp:310
#23 0x00007ffff3c9698b in start_thread (arg=<optimized out>) at pthread_create.c:448
#24 0x00007ffff3d1a9cc in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78
```

This happened when I clicked close while on the Transactions tab of the GUI.

Environment:
Monero-GUI commit (upstream): `1de4a65f90685561bc317d55ad2cfca3277992a1`
monero submodule commit (fcmp++-alpha-stressnet branch): `5504328be07a0d137179b25e20ada04a73218b89`
Host: Arch Linux

# Discussion History
## stianov | 2025-12-17T13:26:51+00:00
This is unlikely to be related to FCMP, as it seems to be caused by a double free of the Qt components. Does the same issue not occur with the regular GUI?

## ComputeryPony | 2025-12-17T19:36:11+00:00
Unfortunately I can't recall if this has happened to me on the regular GUI. I suspect it isn't related to the FCMP work either but since I can't remember if I've encountered it in the regular GUI I went a head and filed the issue here.
If others believe it is unrelated as well I will file it upstream.

# Action History
- Created by: ComputeryPony | 2025-12-16T23:03:52+00:00
