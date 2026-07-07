---
title: 'Wallet_addressValid: int nettype picks the deprecated bool-testnet overload
  — stagenet addresses never validate'
source_url: https://github.com/MrCyjaneK/monero_c/issues/190
author: star7js
assignees: []
labels: []
created_at: '2026-07-07T09:09:46+00:00'
updated_at: '2026-07-07T09:09:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Summary

`MONERO_Wallet_addressValid` never validates stagenet addresses, and validates testnet addresses for *any* nonzero nettype. The cause is C++ overload resolution in the wrapper.

## Repro

Observed with the official `v0.18.4.6-RC2` prebuilt (`aarch64-apple-darwin`), and the code is unchanged on current master. Via the Dart wrapper (or the C API directly):

```dart
final w = monero.WalletManager_createWallet(wm, path: p, password: 'x', networkType: net);
final addr = monero.Wallet_address(w);
[for (var n = 0; n < 3; n++) monero.Wallet_addressValid(addr, n)]
```

| wallet network | its own primary address validates as |
|---|---|
| mainnet (0) | `[true, false, false]` ✔ |
| testnet (1) | `[false, true, true]` ✘ (also "valid" for 2) |
| stagenet (2) | `[false, false, false]` ✘ (never valid) |

## Cause

`monero_libwallet2_api_c/src/main/cpp/monero_wallet2_api_c.cpp`:

```cpp
bool MONERO_Wallet_addressValid(const char* str, int nettype) {
    return Monero::Wallet::addressValid(std::string(str), nettype);
}
```

`wallet2_api.h` has two overloads:

```cpp
static bool addressValid(const std::string &str, NetworkType nettype);
static bool addressValid(const std::string &str, bool testnet); // deprecated
```

An `int` argument converts implicitly to `bool` but **not** to an enum, so overload resolution always picks the deprecated `bool testnet` overload: `0` → MAINNET, any nonzero → TESTNET, and STAGENET is unreachable. That matches the table exactly.

## Fix

```cpp
return Monero::Wallet::addressValid(std::string(str), static_cast<Monero::NetworkType>(nettype));
```

`MONERO_Wallet_keyValid` has the same `int nettype` signature one function down and is worth checking for the same pattern (`keyValid` also has a deprecated bool overload).

Happy to send a PR if useful. Found while running a Flutter wallet's send-screen address validation on stagenet — every valid stagenet address was rejected. (Same passthrough exists in the wownero/zano wrappers.)


# Discussion History
# Action History
- Created by: star7js | 2026-07-07T09:09:46+00:00
