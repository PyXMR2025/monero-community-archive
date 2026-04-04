---
title: Cannot enter passphrase from GUI
source_url: https://github.com/monero-project/monero/issues/8656
author: Janaka-Steph
assignees: []
labels: []
created_at: '2022-11-29T14:43:41+00:00'
updated_at: '2022-12-20T21:44:21+00:00'
type: issue
status: closed
closed_at: '2022-12-20T18:38:37+00:00'
---

# Original Description
Running GUI 0.18.1.2 on Mac M1 with Trezor 2.5.3, from cli `/Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui`. If I try to enter the passphrase from the computer in GUI, it fails with below error. I can access the wallet if I enter the phrase from the device.
```
2022-11-29 14:28:43.456	T READ ENDS: Connection err_code 2
2022-11-29 14:28:43.456	T Connection err_code eof.
2022-11-29 14:28:43.457	T Returning false because of wrong state machine. state: 5
2022-11-29 14:28:43.458	E Failed to invoke http request to  /call/91
2022-11-29 14:28:43.459	E Get public address exception: Call method failed
2022-11-29 14:28:43.460	E !hwdev.get_public_address(device_account_public_address). THROW EXCEPTION: error::wallet_internal_error
2022-11-29 14:28:43.460	W /Users/mojado/monero-gui/monero/src/wallet/wallet2.cpp:4510:N5tools5error21wallet_internal_errorE: Cannot get a device address
2022-11-29 14:28:43.461	E Error opening wallet: Cannot get a device address
2022-11-29 14:28:43.462	D Refreshing addressbook
2022-11-29 14:28:43.462	D Wallet *WalletManager::openWallet(const QString &, const QString &, NetworkType::Type, quint64): opened wallet: 4......, status: 2
2022-11-29 14:28:43.462	D Hiding processing splash
2022-11-29 14:28:43.464	D >>> wallet opened: Wallet(0x....)
2022-11-29 14:28:43.464	E Error opening wallet with password:  Cannot get a device address
```

or 

```
2022-11-29 14:40:12.675	T READ ENDS: Connection err_code 2
2022-11-29 14:40:12.675	T Connection err_code eof.
2022-11-29 14:40:12.675	T Returning false because of wrong state machine. state: 5
2022-11-29 14:40:12.675	E Failed to invoke http request to  /call/97
2022-11-29 14:40:12.677	E Get public address exception: Call method failed
2022-11-29 14:40:12.677	E !hwdev.get_public_address(device_account_public_address). THROW EXCEPTION: error::wallet_internal_error
2022-11-29 14:40:12.677	W /Users/mojado/monero-gui/monero/src/wallet/wallet2.cpp:4510:N5tools5error21wallet_internal_errorE: Cannot get a device address
2022-11-29 14:40:12.679	E Error opening wallet: Cannot get a device address
2022-11-29 14:40:12.679	D Refreshing addressbook
2022-11-29 14:40:12.679	D Wallet *WalletManager::openWallet(const QString &, const QString &, NetworkType::Type, quint64): opened wallet: 4..., status: 2
2022-11-29 14:40:12.680	D Hiding processing splash
2022-11-29 14:40:12.681	D >>> wallet opened: Wallet(0x....)
2022-11-29 14:40:12.682	E Error opening wallet with password:  Cannot get a device address
2022-11-29 14:40:12.684	D closing wallet async : function() { [native code] }
```

It's not always the same endpoint `/call/91` or `/call/97`.

# Discussion History
## selsta | 2022-11-29T14:44:50+00:00
I'm quite sure this is related to your other issue.

## Janaka-Steph | 2022-11-29T14:45:51+00:00
Yep possibly

## Janaka-Steph | 2022-11-29T15:29:38+00:00
@ph4r05 It might be related to #8655 

## Janaka-Steph | 2022-12-20T18:38:37+00:00
The problem was that I was running Trezor Suite along with the GUI, because I didn't have trezord process running in the background otherwise.

## selsta | 2022-12-20T21:44:21+00:00
Glad you got the issue resolved! The always different random error messages and endpoint calls hinted at interference from a different program.

# Action History
- Created by: Janaka-Steph | 2022-11-29T14:43:41+00:00
- Closed at: 2022-12-20T18:38:37+00:00
