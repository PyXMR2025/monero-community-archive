---
title: Committing a transaction can abort the host process (heap corruption) while
  the wallet refresh machinery is active - after the tx has already been relayed
source_url: https://github.com/MrCyjaneK/monero_c/issues/193
author: johnr365
assignees: []
labels: []
created_at: '2026-08-16T10:11:00+00:00'
updated_at: '2026-08-16T21:33:33+00:00'
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
## MrCyjaneK | 2026-08-16T19:50:41+00:00
Hey @johnr365 could you share code that you are using to commit transaction and all (if any) background calls that are happening?

Are you using Isolates?

Can you turn on printStarts and attach them with the log too?

## johnr365 | 2026-08-16T21:33:33+00:00
Thanks. Tracing the exact call path uncovered a deterministic invalid-free path that explains all eight crashes. The refresh thread visible in the crash reports appears to have been incidental to this failure, so my earlier attribution to commit/refresh concurrency was incorrect.

**Root cause**: `PendingTransactionImpl::commit()` drains `m_pending_tx` via `pop_back()` as it commits each entry (pending_transaction.cpp, around line 153). My code then calls `txid()` *after* `commit()` returns, and `txid()` just iterates whatever is left in `m_pending_tx` - which is now empty. For an empty vector, `vectorToString()` (helpers.cpp) returns the string literal `""`, not a heap pointer. The bundled Dart wrapper's `PendingTransaction_txid()` unconditionally passes that pointer to `MONERO_free()`, which calls `free()` on a non-heap address - exactly the invalid/misaligned-pointer crash I've been chasing for eight runs now.

There is also a second, related bug: on the non-empty path, `vectorToString()` allocates with `new char[]`, but `MONERO_free()` releases it with `free()` - an allocator mismatch, undefined behavior even when it doesn't crash outright.

My commit code (Dart FFI wrapper, called from my payment engine):

```dart
String commitTransfer(int handle) {
  final tx = _pendingTxs.remove(handle);
  if (tx == null) throw WalletRejection('No such prepared transfer.');
  _quiesceRefresh();
  try {
    return _commitQuiesced(tx);
  } finally {
    _resumeRefresh();
  }
}

String _commitQuiesced(monero.PendingTransaction tx) {
  final committed = monero.PendingTransaction_commit(tx, filename: '', overwrite: false);
  final status = monero.PendingTransaction_status(tx);
  if (!committed || status != 0) throw WalletRejection(...);
  final txid = monero.PendingTransaction_txid(tx, ''); // <- called AFTER commit, this is the bug
  if (txid.isEmpty) throw StateError('commit succeeded but returned no txid');
  return txid; // deliberately no store() here
}
```

The `_quiesceRefresh`/`_resumeRefresh` pair (pause + stop + a synchronous `Wallet_refresh` join around commit) was my own mitigation attempt for the refresh-race theory - I'll likely pull it now, since it was never addressing the real cause.

**Background calls**: nothing else concurrent on my side beyond the pause/stop/refresh/start sequence above (serialized, one send in flight at a time via a wallet-wide lock). I'd assumed a live `WalletImpl::refreshThreadFunc`/`doRefresh` iteration (visible in every crash's stack trace, inside `wallet2::pull_blocks` waiting on the daemon) was the culprit - in hindsight that's probably just incidental background activity, not related to this bug.

**Isolates**: yes, one long-lived Dart isolate per open wallet, spawned once at wallet-open time. Every call (build/commit/store/etc.) goes through a persistent command/reply port to that same isolate for the wallet's whole lifetime - not one isolate per call, and nothing native-side is invoked from more than one Dart isolate.

My proposed caller-side workaround: capture `PendingTransaction_txid()` before calling `commit()`. This avoids the empty-vector/string-literal path because the transaction is still present in `m_pending_tx`.

I implemented and tested this. A no-relay preflight (build, read the txid, discard without committing - no funds move) passed first. I then ran two funded stagenet self-payments with the txid recorded write-ahead before the commit call. Both `commit()` calls returned cleanly, without a crash, and returned the same txid captured before their respective commits:

- `1088b2e17ad6be67a2d3babf53131d26a7ab30925fa48eeb16460d499118dcfc` - confirmed on chain at height 2186949
- `2c30f59464e23dd2a83c833a5395b4b3eaa5a0d88feb601f63fc9917323c8b74` - confirmed on chain at height 2186961

These are the first two clean commits through this stack, immediately following eight crashes with the post-commit txid ordering.

This is only a workaround for the empty-vector failure, not a complete fix: the non-empty `vectorToString()` path still allocates with `new char[]`, while `MONERO_free()` uses `free()`. Both verification txids took that exact path (a real, non-empty result) without crashing, but two clean runs are not proof that the allocator mismatch is safe under all conditions - it is still undefined behavior on monero_c's side, independent of anything I can fix caller-side.

For monero_c: I think `vectorToString()` should return memory compatible with `MONERO_free()` on every path, including the empty result. For example, allocating with `malloc()`/`strdup()` consistently would fix both the empty-string invalid free and the non-empty allocator mismatch. Documenting the required call order alone would not fix those ownership issues.

printStarts: found it, thanks - `monero.printStarts = true;`. Because my wallet runs in a separate Dart isolate, it had to be enabled inside that wallet isolate rather than in the parent. I repeated the funded verification with it enabled in the correct isolate. The relevant sequence was:

```text
MONERO: MONERO_PendingTransaction_txid
MONERO: MONERO_free
MONERO: MONERO_Wallet_pauseRefresh
MONERO: MONERO_Wallet_stop
MONERO: MONERO_Wallet_refresh
MONERO: MONERO_PendingTransaction_txid
MONERO: MONERO_free
MONERO: MONERO_PendingTransaction_commit
MONERO: MONERO_PendingTransaction_status
MONERO: MONERO_Wallet_startRefresh
MONERO: MONERO_Wallet_refreshAsync
```

The full trace is available as `verify-traced-run.log` if useful.


# Action History
- Created by: johnr365 | 2026-08-16T10:11:00+00:00
