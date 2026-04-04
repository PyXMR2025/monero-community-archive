---
title: Ledger Nano X wrong device status after upgrading to 0.17.0.1
source_url: https://github.com/monero-project/monero/issues/6861
author: mountassir
assignees: []
labels: []
created_at: '2020-10-05T20:10:41+00:00'
updated_at: '2020-10-06T08:23:12+00:00'
type: issue
status: closed
closed_at: '2020-10-06T08:23:12+00:00'
---

# Original Description
Hi, 

After upgrading to the GUI 0.17.0.1, the wallet can no longer open the hardware wallet, these are the errors I see in the logs:

```
ERROR	device.ledger	src/device/device_ledger.cpp:484	Wrong Device Status: 0x6e00 (SW_CLA_NOT_SUPPORTED), EXPECTED 0x9000 (SW_OK), MASK 0xffff
ERROR	WalletAPI	src/wallet/api/wallet.cpp:719	Error opening wallet: Wrong Device Status: 0x6e00 (SW_CLA_NOT_SUPPORTED), EXPECTED 0x9000 (SW_OK), MASK 0xffff
ERROR	frontend	src/wallet/api/wallet.cpp:416	Error opening wallet with password:  Wrong Device Status: 0x6e00 (SW_CLA_NOT_SUPPORTED), EXPECTED 0x9000 (SW_OK), MASK 0xffff
```

The Ledger app is on version 1.6.

Thanks

# Discussion History
## mountassir | 2020-10-05T20:25:41+00:00
Apparently this error means the the app does not support the client's version, I see a new version of the Ledger app 1.7.2 was released a few days ago, hopefully that will fix the issue. Ledger Live still show 1.6 as the latest version for now.

## dEBRUYNE-1 | 2020-10-05T21:18:57+00:00
v0.17 can only be run in conjunction with Ledger Monero App v1.7.x, which is currently only available in *developer mode*.

## mountassir | 2020-10-06T08:23:12+00:00
Ok thanks for confirming!

# Action History
- Created by: mountassir | 2020-10-05T20:10:41+00:00
- Closed at: 2020-10-06T08:23:12+00:00
