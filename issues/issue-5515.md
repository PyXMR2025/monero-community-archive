---
title: API deadlock on refresh
source_url: https://github.com/monero-project/monero/issues/5515
author: ph4r05
assignees: []
labels: []
created_at: '2019-05-02T19:16:38+00:00'
updated_at: '2019-05-11T12:46:02+00:00'
type: issue
status: closed
closed_at: '2019-05-11T12:46:02+00:00'
---

# Original Description
During the testing we noticed a deadlock in the `refresh()` in the Monero GUI. (kudos to @vir-satoshi for the detection).

I finally managed to reproduce the problem. The problem manifests with the connected Trezor as the key image computation takes longer but the problem is Trezor independent.

I am not sure whether the problem is in the API or the usage of the API in the GUI.
The problem is in the `monero/src/wallet/api/wallet.cpp -> WalletImpl::doRefresh()`:

```cpp
boost::lock_guard<boost::mutex> guarg(m_refreshMutex2);
```

Monero-GUI has the following logic:

```
gui.wallet.refresh() -> 
WalletImpl::doRefresh() -> 
Monero::Wallet2CallbackImpl::on_money_received() ->
Wallet::moneyReceived() -> 
gui.wallet.refresh() ->
WalletImpl::doRefresh() -> 
DEADLOCK
```

`main.qml` in the monero-gui:
```qml
function onWalletMoneyReceived(txId, amount) {
        // refresh transaction history here
        currentWallet.refresh()  //  <----- invokes another refresh from existing one
        //...
```

The fix could be to redefine `m_refreshMutex2` as a recursive mutex. On the other hand, the fix is maybe needed in the Monero-GUI.

@moneromooo-monero what do you think is the best approach here? @xmrdsc ?

The full stack trace on the main thread:

```lldb
frame #0: 0x00007fff5b1a5f06 libsystem_kernel.dylib`__psynch_mutexwait + 10
    frame #1: 0x00007fff5b25cd52 libsystem_pthread.dylib`_pthread_mutex_firstfit_lock_wait + 96
    frame #2: 0x00007fff5b25a4cd libsystem_pthread.dylib`_pthread_mutex_firstfit_lock_slow + 222
    frame #3: 0x000000010c55108a monero-wallet-gui`boost::mutex::lock() + 42
    frame #4: 0x000000010c50b05c monero-wallet-gui`Monero::WalletImpl::doRefresh() + 1292
    frame #5: 0x000000010c50ab35 monero-wallet-gui`Monero::WalletImpl::refresh() + 101
    frame #6: 0x000000010c4c9339 monero-wallet-gui`Wallet::refresh() + 41
    frame #7: 0x000000010c4f6557 monero-wallet-gui`Wallet::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 1607
    frame #8: 0x000000010c4f8499 monero-wallet-gui`Wallet::qt_metacall(QMetaObject::Call, int, void**) + 121
    frame #9: 0x000000010f994c3d QtQml`___lldb_unnamed_symbol2315$$QtQml + 4365
    frame #10: 0x000000010f99142c QtQml`___lldb_unnamed_symbol2289$$QtQml + 124
    frame #11: 0x000000010f990e49 QtQml`QV4::QObjectMethod::callInternal(QV4::Value const*, QV4::Value const*, int) const + 1273
    frame #12: 0x000000010fa272a0 QtQml`QV4::Runtime::method_callProperty(QV4::ExecutionEngine*, QV4::Value*, int, QV4::Value*, int) + 400
    frame #13: 0x000000010f9a8946 QtQml`___lldb_unnamed_symbol2586$$QtQml + 3910
    frame #14: 0x000000010f9a78db QtQml`___lldb_unnamed_symbol2585$$QtQml + 139
    frame #15: 0x000000010f955c9f QtQml`___lldb_unnamed_symbol1803$$QtQml + 367
    frame #16: 0x000000010f9934ee QtQml`___lldb_unnamed_symbol2314$$QtQml + 734
    frame #17: 0x000000010f4abd7b QtCore`QMetaObject::activate(QObject*, int, int, void**) + 2219
    frame #18: 0x000000010c4f7dd3 monero-wallet-gui`Wallet::moneyReceived(QString const&, unsigned long long) + 67
    frame #19: 0x000000010c4d051b monero-wallet-gui`WalletListenerImpl::moneyReceived(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, unsigned long long) + 203
    frame #20: 0x000000010c52146a monero-wallet-gui`Monero::Wallet2CallbackImpl::on_money_received(unsigned long long, crypto::hash const&, cryptonote::transaction const&, unsigned long long, cryptonote::subaddress_index const&) + 1338
    frame #21: 0x000000010c604024 monero-wallet-gui`tools::wallet2::process_new_transaction(crypto::hash const&, cryptonote::transaction const&, std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> > const&, unsigned long long, unsigned long long, bool, bool, bool, tools::wallet2::tx_cache_data const&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*) + 29620
    frame #22: 0x000000010c610c79 monero-wallet-gui`tools::wallet2::process_new_blockchain_entry(cryptonote::block const&, cryptonote::block_complete_entry const&, tools::wallet2::parsed_block const&, crypto::hash const&, unsigned long long, std::__1::vector<tools::wallet2::tx_cache_data, std::__1::allocator<tools::wallet2::tx_cache_data> > const&, unsigned long, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*) + 2361
    frame #23: 0x000000010c618a7e monero-wallet-gui`tools::wallet2::process_parsed_blocks(unsigned long long, std::__1::vector<cryptonote::block_complete_entry, std::__1::allocator<cryptonote::block_complete_entry> > const&, std::__1::vector<tools::wallet2::parsed_block, std::__1::allocator<tools::wallet2::parsed_block> > const&, unsigned long long&, std::__1::map<std::__1::pair<unsigned long long, unsigned long long>, unsigned long, std::__1::less<std::__1::pair<unsigned long long, unsigned long long> >, std::__1::allocator<std::__1::pair<std::__1::pair<unsigned long long, unsigned long long> const, unsigned long> > >*) + 9182
    frame #24: 0x000000010c61dc3a monero-wallet-gui`tools::wallet2::refresh(bool, unsigned long long, unsigned long long&, bool&, bool) + 1978
    frame #25: 0x000000010c61d40b monero-wallet-gui`tools::wallet2::refresh(bool) + 59
    frame #26: 0x000000010c50b5bc monero-wallet-gui`Monero::WalletImpl::doRefresh() + 2668
    frame #27: 0x000000010c50ab35 monero-wallet-gui`Monero::WalletImpl::refresh() + 101
    frame #28: 0x000000010c4c9339 monero-wallet-gui`Wallet::refresh() + 41
    frame #29: 0x000000010c4f6557 monero-wallet-gui`Wallet::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 1607
    frame #30: 0x000000010c4f8499 monero-wallet-gui`Wallet::qt_metacall(QMetaObject::Call, int, void**) + 121
    frame #31: 0x000000010f994c3d QtQml`___lldb_unnamed_symbol2315$$QtQml + 4365
    frame #32: 0x000000010f99142c QtQml`___lldb_unnamed_symbol2289$$QtQml + 124
    frame #33: 0x000000010f990e49 QtQml`QV4::QObjectMethod::callInternal(QV4::Value const*, QV4::Value const*, int) const + 1273
    frame #34: 0x000000010fa272a0 QtQml`QV4::Runtime::method_callProperty(QV4::ExecutionEngine*, QV4::Value*, int, QV4::Value*, int) + 400
    frame #35: 0x000000010f9a8946 QtQml`___lldb_unnamed_symbol2586$$QtQml + 3910
    frame #36: 0x000000010f9a78db QtQml`___lldb_unnamed_symbol2585$$QtQml + 139
    frame #37: 0x000000010f955c9f QtQml`___lldb_unnamed_symbol1803$$QtQml + 367
    frame #38: 0x000000010f9934ee QtQml`___lldb_unnamed_symbol2314$$QtQml + 734
    frame #39: 0x000000010f4a4801 QtCore`QObject::event(QEvent*) + 753
    frame #40: 0x000000010e2caf8d QtWidgets`QApplicationPrivate::notify_helper(QObject*, QEvent*) + 269
    frame #41: 0x000000010e2cc392 QtWidgets`QApplication::notify(QObject*, QEvent*) + 594
    frame #42: 0x000000010f47afb4 QtCore`QCoreApplication::notifyInternal2(QObject*, QEvent*) + 212
    frame #43: 0x000000010f47c1ee QtCore`QCoreApplicationPrivate::sendPostedEvents(QObject*, int, QThreadData*) + 878
    frame #44: 0x0000000112212b89 libqcocoa.dylib`___lldb_unnamed_symbol578$$libqcocoa.dylib + 313
    frame #45: 0x0000000112213400 libqcocoa.dylib`___lldb_unnamed_symbol590$$libqcocoa.dylib + 32
    frame #46: 0x00007fff2ec125e3 CoreFoundation`__CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17
    frame #47: 0x00007fff2ec12589 CoreFoundation`__CFRunLoopDoSource0 + 108
    frame #48: 0x00007fff2ebf5f3b CoreFoundation`__CFRunLoopDoSources0 + 195
    frame #49: 0x00007fff2ebf5505 CoreFoundation`__CFRunLoopRun + 1189
    frame #50: 0x00007fff2ebf4e0e CoreFoundation`CFRunLoopRunSpecific + 455
    frame #51: 0x00007fff2dee19db HIToolbox`RunCurrentEventLoopInMode + 292
    frame #52: 0x00007fff2dee1715 HIToolbox`ReceiveNextEventCommon + 603
    frame #53: 0x00007fff2dee14a6 HIToolbox`_BlockUntilNextEventMatchingListInModeWithFilter + 64
    frame #54: 0x00007fff2c27bffb AppKit`_DPSNextEvent + 965
    frame #55: 0x00007fff2c27ad93 AppKit`-[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1361
    frame #56: 0x00007fff2c274eb0 AppKit`-[NSApplication run] + 699
    frame #57: 0x000000011221225b libqcocoa.dylib`___lldb_unnamed_symbol572$$libqcocoa.dylib + 2955
    frame #58: 0x000000010f47661f QtCore`QEventLoop::exec(QFlags<QEventLoop::ProcessEventsFlag>) + 431
    frame #59: 0x000000010f47b5c2 QtCore`QCoreApplication::exec() + 130
    frame #60: 0x000000010c4b5980 monero-wallet-gui`main + 8656
    frame #61: 0x00007fff5b06e3d5 libdyld.dylib`start + 1
    frame #62: 0x00007fff5b06e3d5 libdyld.dylib`start + 1
```

# Discussion History
## moneromooo-monero | 2019-05-02T19:18:12+00:00
Does it happen with monero-wallet-cli ? 

## ph4r05 | 2019-05-02T19:24:09+00:00
> Does it happen with monero-wallet-cli ?

No, I can trigger it only via monero-gui. The deadlock is in the `wallet/api` so I opened the issue here. We may want to protect from the deadlock situation by throwing an exception. The fix should be probably done also in the GUI.

## ph4r05 | 2019-05-02T19:35:45+00:00
I can confirm that changing `m_refreshMutex2` to recursive_mutex fixes the problem, but it is maybe not desired to call refresh from the refresh-induced-callback.

## xiphon | 2019-05-02T19:54:48+00:00
> The fix could be to redefine `m_refreshMutex2` as a recursive mutex.

I would prefer to not use recursive mutex and fix the deadlock on the GUI side.

# Action History
- Created by: ph4r05 | 2019-05-02T19:16:38+00:00
- Closed at: 2019-05-11T12:46:02+00:00
