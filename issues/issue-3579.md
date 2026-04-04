---
title: 'Transfer: error when signing tx file (offline transaction signing)'
source_url: https://github.com/monero-project/monero-gui/issues/3579
author: rating89us
assignees: []
labels: []
created_at: '2021-06-20T18:13:21+00:00'
updated_at: '2022-05-05T20:09:45+00:00'
type: issue
status: closed
closed_at: '2022-05-05T20:09:45+00:00'
---

# Original Description
After creating an unsigned transaction file on view-only wallet, I tried to sign this file on the offline wallet and got this error:
`W qrc:/pages/Transfer.qml:1006: Error: Unknown method parameter type: size_t`

# Discussion History
## wojtaswsk | 2021-11-26T12:53:40+00:00
Same problem. Linux and windows.
versions: 0.17.2.3-113efbf (Qt 5.15.2), 0.17.2.3-release

2021-11-26 12:51:58.014	    7f575c621fc0	DEBUG	frontend	src/wallet/api/wallet.cpp:404	Trying to sign  "/home/wojtas/Monero/wallets/tu3"

2021-11-26 12:51:58.041	    7f575c621fc0	INFO	wallet.wallet2	src/wallet/wallet2.cpp:6782	Loaded tx unsigned data from binary: 1 transactions

2021-11-26 12:51:58.042	    7f575c621fc0	WARNING	frontend	src/wallet/api/wallet.cpp:412	qrc:/pages/Transfer.qml:1010: Error: Unknown method parameter type: size_t


## reemuru | 2022-05-05T20:08:48+00:00
This should be fixed with #3862

# Action History
- Created by: rating89us | 2021-06-20T18:13:21+00:00
- Closed at: 2022-05-05T20:09:45+00:00
