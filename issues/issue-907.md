---
title: Unable to start gui
source_url: https://github.com/monero-project/monero-gui/issues/907
author: joonaskaskisola
assignees: []
labels: []
created_at: '2017-10-19T19:04:46+00:00'
updated_at: '2017-12-14T22:04:09+00:00'
type: issue
status: closed
closed_at: '2017-10-19T19:09:33+00:00'
---

# Original Description
```
joonas➜~/monero-gui-0.11.0.0» ./start-gui.sh                                                                                                                                                                                [21:56:50]
app startd
qml: check next false
qml: Checking seed
qml: check next false
qml: check next false
qml: log level changed:  0
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 4
qml: qrScannerEnabled disabled
qml: setting demo token
qml: initializing..
setLanguage   "en"
qml: transfer page loaded
qml: PrivacyLevel changed:0
qml: mixin count: 4
qml: opening wallet at:  /home/joonas/Monero/wallets/joonas/joonas , testnet:  false
Checking for updates
Wallet* WalletManager::openWallet(const QString&, const QString&, bool): opening wallet at /home/joonas/Monero/wallets/joonas/joonas, testnet = 0 
2017-10-19 18:58:38.920	    7f7b33fff700	ERROR	net.http	contrib/epee/include/storages/portable_storage.h:161	portable_storage: wrong binary format - signature mismatch
2017-10-19 18:58:38.920	    7f7b33fff700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:2128	!r. THROW EXCEPTION: error::invalid_password
2017-10-19 18:58:38.920	    7f7b33fff700	WARN 	net.http	src/wallet/wallet_errors.h:707	/home/vagrant/slave/monero-core-ubuntu-amd64/build/monero/src/wallet/wallet2.cpp:2128:N5tools5error16invalid_passwordE: invalid password
2017-10-19 18:58:38.921	    7f7b33fff700	ERROR	WalletAPI	src/wallet/api/wallet.cpp:504	Error opening wallet: invalid password
Wallet* WalletManager::openWallet(const QString&, const QString&, bool): opened wallet: 41d7FXjswpK1111111111111111111111111111111111111111111111111111111111111111111111111111112KhNi4, status: 2
AddressBook
getAll
Failed to create OpenGL context for format QSurfaceFormat(version 2.0, options QFlags(), depthBufferSize 24, redBufferSize -1, greenBufferSize -1, blueBufferSize -1, alphaBufferSize -1, stencilBufferSize 8, samples -1, swapBehavior 2, swapInterval 1, profile  0) 
./start-gui.sh: line 7: 15074 Aborted                 (core dumped) "$SCRIPT_DIR"/monero-wallet-gui
```

# Discussion History
## naitsirhc007 | 2017-12-11T14:23:43+00:00
Dear friend, how to solved this problem, did you?

## math3os | 2017-12-14T22:04:09+00:00
same issue here, may it's because i've withdraw my graphic card to put it in my new rig ?

# Action History
- Created by: joonaskaskisola | 2017-10-19T19:04:46+00:00
- Closed at: 2017-10-19T19:09:33+00:00
