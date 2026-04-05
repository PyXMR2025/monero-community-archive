---
title: Copy-paste bugs in cw_WalletListener wrapper functions
source_url: https://github.com/MrCyjaneK/monero_c/issues/182
author: phrontizo
assignees: []
labels: []
created_at: '2026-03-19T12:28:09+00:00'
updated_at: '2026-03-20T10:08:00+00:00'
type: issue
status: closed
closed_at: '2026-03-20T10:08:00+00:00'
---

# Original Description
## Summary

Three C wrapper functions in `monero_wallet2_api_c.cpp` (lines 2638–2657) call the wrong underlying method on `MONERO_cw_WalletListener`. They all call `cw_isNeedToRefresh()` instead of their intended methods.

## Affected functions

The struct defines the correct methods:

```cpp
bool cw_isNewTransactionExist() { return m_new_transaction; }
void cw_resetIsNewTransactionExist() { m_new_transaction = false; }
uint64_t cw_height() { return m_height; }
```

But the exported wrapper functions don't call them:

### 1. `MONERO_cw_WalletListener_isNewTransactionExist` (line 2638)

```cpp
// Should call cw_isNewTransactionExist(), actually calls cw_isNeedToRefresh()
bool MONERO_cw_WalletListener_isNewTransactionExist(void* cw_walletListener_ptr) {
    DEBUG_START()
    MONERO_cw_WalletListener *listener = reinterpret_cast<MONERO_cw_WalletListener*>(cw_walletListener_ptr);
    return listener->cw_isNeedToRefresh();  // BUG
    DEBUG_END()
};
```

**Effect:** Callers checking for new transactions actually get the "needs refresh" flag. In Cake Wallet, this means `onNewTransaction` fires after every refresh cycle rather than only when `moneySpent`/`moneyReceived`/`unconfirmedMoneyReceived`/`updated` is called.

### 2. `MONERO_cw_WalletListener_resetIsNewTransactionExist` (line 2645)

```cpp
// Should call cw_resetIsNewTransactionExist(), actually calls cw_isNeedToRefresh() (read-only!)
void MONERO_cw_WalletListener_resetIsNewTransactionExist(void* cw_walletListener_ptr) {
    DEBUG_START()
    MONERO_cw_WalletListener *listener = reinterpret_cast<MONERO_cw_WalletListener*>(cw_walletListener_ptr);
    listener->cw_isNeedToRefresh();  // BUG: reads but doesn't reset
    DEBUG_END()
};
```

**Effect:** `m_new_transaction` is never reset to `false` through this API. Once a transaction is received, the flag stays `true` forever.

### 3. `MONERO_cw_WalletListener_height` (line 2652)

```cpp
// Should call cw_height(), actually calls cw_isNeedToRefresh()
uint64_t MONERO_cw_WalletListener_height(void* cw_walletListener_ptr) {
    DEBUG_START()
    MONERO_cw_WalletListener *listener = reinterpret_cast<MONERO_cw_WalletListener*>(cw_walletListener_ptr);
    return listener->cw_isNeedToRefresh();  // BUG: returns 0 or 1 instead of block height
    DEBUG_END()
};
```

**Effect:** Returns a boolean (0 or 1) cast to `uint64_t` instead of the actual block height from `newBlock()`.

## Expected fix

```cpp
bool MONERO_cw_WalletListener_isNewTransactionExist(void* cw_walletListener_ptr) {
    DEBUG_START()
    MONERO_cw_WalletListener *listener = reinterpret_cast<MONERO_cw_WalletListener*>(cw_walletListener_ptr);
    return listener->cw_isNewTransactionExist();
    DEBUG_END()
};

void MONERO_cw_WalletListener_resetIsNewTransactionExist(void* cw_walletListener_ptr) {
    DEBUG_START()
    MONERO_cw_WalletListener *listener = reinterpret_cast<MONERO_cw_WalletListener*>(cw_walletListener_ptr);
    listener->cw_resetIsNewTransactionExist();
    DEBUG_END()
};

uint64_t MONERO_cw_WalletListener_height(void* cw_walletListener_ptr) {
    DEBUG_START()
    MONERO_cw_WalletListener *listener = reinterpret_cast<MONERO_cw_WalletListener*>(cw_walletListener_ptr);
    return listener->cw_height();
    DEBUG_END()
};
```

## Impact on Cake Wallet

These bugs likely contribute to stale transaction confirmation counts in Cake Wallet. The interaction is subtle — bug #1 accidentally causes *more frequent* transaction updates than intended (because every refresh triggers the "new transaction" path), which partially masks the other issues. But bug #2 means the new-transaction flag is never cleared, creating unnecessary work, and bug #3 means any caller relying on `MONERO_cw_WalletListener_height` gets garbage data.

Note: the identical pattern likely exists in the Wownero copy at `wownero_libwallet2_api_c/src/main/cpp/wownero_wallet2_api_c.cpp`.

# Discussion History
# Action History
- Created by: phrontizo | 2026-03-19T12:28:09+00:00
- Closed at: 2026-03-20T10:08:00+00:00
