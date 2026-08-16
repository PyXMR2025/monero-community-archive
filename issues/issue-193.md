---
title: Committing a transaction can abort the host process (heap corruption) while
  the wallet refresh machinery is active - after the tx has already been relayed
source_url: https://github.com/MrCyjaneK/monero_c/issues/193
author: johnr365
assignees: []
labels: []
created_at: '2026-08-16T10:11:00+00:00'
updated_at: '2026-08-16T10:19:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Summary

Committing a transaction through the C API killed my host process seven times out of seven attempts - six with a malloc abort ("pointer being freed was not allocated" -> SIGABRT), one silently with exit 0 - across both Dart JIT and Dart AOT hosts. In every captured case the transaction HAD already been relayed and later confirmed on chain. For an app driving payments through monero_c this is the worst failure shape: the process dies after the money moved, and only an application-level write-ahead record prevents a double send on relaunch.

Three caller-side mitigations across four configurations failed to prevent it, which is why I am reporting rather than working around.

## Environment

- monero_c v0.18.4.6-RC2, official prebuilt aarch64-apple-darwin (`libmonero_wallet2_api_c.dylib`, checksum matching the release), loaded via Dart FFI (`impls/monero.dart` at the same tag)
- macOS (arm64), stagenet, remote node over SSL
- Host: reproduced on BOTH Dart runtimes - six deaths under JIT VMs (flutter_tester / dart run) and a seventh, identical, under a `dart compile exe` AOT binary (Dart SDK 3.13.0 stable, macos_arm64; dylib sha256 cfcd0b602d91b833a1c4d16e6408b479ee7792f4b5c096b42fa03c91434dc734). So the failure is not specific to Dart JIT.
- Wallet synced before each send; `Wallet_startRefresh` active

## The failure, seven times

Call sequence on one thread:

1. `MONERO_Wallet_createTransaction` -> status 0, fee reads fine
2. write-ahead record on disk (application side)
3. `MONERO_PendingTransaction_commit(tx, "", false)` -> relays
4. seconds later the process dies; six times via `___BUG_IN_CLIENT_OF_LIBMALLOC_POINTER_BEING_FREED_WAS_NOT_ALLOCATED` (the faulting thread is an ordinary free on the caller's side), once silently with exit code 0

Every crash report captures another thread concurrently INSIDE the refresh machinery (symbolicated against the shipped dylib):

    Monero::WalletImpl::refreshThreadFunc()
      -> Monero::WalletImpl::doRefresh()
      -> tools::wallet2::refresh(...)
      -> tools::wallet2::pull_and_parse_next_blocks(...)
      -> tools::wallet2::pull_blocks(...)   // mid-RPC at abort time

## Why I believe commit vs refresh is the collision

- `Monero::WalletImpl::createTransactionMultDest` re-arms refresh unconditionally on exit (trailing [`startRefresh()`, wallet.cpp:1824](https://github.com/monero-project/monero/blob/dbcc7d212c094bd1a45f7291dbb99a4b4627a96d/src/wallet/api/wallet.cpp#L1824) at the pinned submodule revision dbcc7d21), so a commit that follows a build always races a freshly woken refresh thread.
- `PendingTransactionImpl::commit` guards itself with [`pauseRefresh()`, pending_transaction.cpp:112](https://github.com/monero-project/monero/blob/dbcc7d212c094bd1a45f7291dbb99a4b4627a96d/src/wallet/api/pending_transaction.cpp#L112) - but that only flips a flag; it never waits for the iteration the build's trailing startRefresh just kicked off - and re-arms again at its own tail ([line 161](https://github.com/monero-project/monero/blob/dbcc7d212c094bd1a45f7291dbb99a4b4627a96d/src/wallet/api/pending_transaction.cpp#L161)). (Line numbers are the pristine submodule revision; the monero_c patch set does not touch these call sites' logic.)
- The 0002-store-crash-fix patch (present in this build) gives store a real LOCK_REFRESH; commit has no equivalent.

## Caller-side mitigations that did NOT stop it

1. Removing my post-commit `Wallet_store` call entirely - crashed.
2. `pauseRefresh` + `stop` + 500ms settle before build - crashed (the in-flight iteration outlives a fixed delay; it sat in a stalled recv).
3. `pauseRefresh` + `stop` + a synchronous `Wallet_refresh()` intended as a join (doRefresh's m_refreshMutex2) immediately before commit - still crashed, with a refresh iteration again live at abort time.

So either commit's own trailing startRefresh reopens the race before the caller regains control, or the shipped fork's locking differs from what the upstream sources suggest. Either way it does not appear fixable from outside the library.

## Ask

A LOCK_REFRESH-style guard around the whole of `PendingTransactionImpl::commit` (as store received in 0002-store-crash-fix), or an exported synchronous stop/join for the refresh thread so callers can build one. Happy to share all six .ips crash reports and logs. For context: Cake's cw_monero pins this same monero_c commit (3bfb3856) and commits through this same binding with refresh armed - if there is a usage pattern that makes this safe, I would love to know what it is.




# Discussion History
# Action History
- Created by: johnr365 | 2026-08-16T10:11:00+00:00
