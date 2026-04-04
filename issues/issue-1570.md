---
title: 'build problem: unblackballOutput() signature changed'
source_url: https://github.com/monero-project/monero-gui/issues/1570
author: MoroccanMalinois
assignees: []
labels: []
created_at: '2018-09-24T21:28:05+00:00'
updated_at: '2018-09-30T16:42:19+00:00'
type: issue
status: closed
closed_at: '2018-09-30T16:42:19+00:00'
---

# Original Description
    ../src/libwalletqt/Wallet.cpp:780:64: error: too few arguments to function call, expected 2, have 1
        return m_walletImpl->unblackballOutput(pubkey.toStdString());


# Discussion History
## MoroccanMalinois | 2018-09-30T16:42:19+00:00
Fixed by #1574 

# Action History
- Created by: MoroccanMalinois | 2018-09-24T21:28:05+00:00
- Closed at: 2018-09-30T16:42:19+00:00
