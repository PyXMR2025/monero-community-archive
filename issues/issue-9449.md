---
title: '[GUI][Restore wallet] ''Create wallet'' stays disabled until monero-wallet-gui
  is closed'
source_url: https://github.com/monero-project/monero/issues/9449
author: b4n6-b4n6
assignees: []
labels:
- invalid
created_at: '2024-08-22T21:30:02+00:00'
updated_at: '2024-08-22T22:10:59+00:00'
type: issue
status: closed
closed_at: '2024-08-22T22:10:53+00:00'
---

# Original Description
Kindly observe video @ 00:37 where 'Create wallet' button stays disabled even though mnemonic seed has been corrected
[restore-bug-2.webm](https://github.com/user-attachments/assets/f611803b-65d8-4a3a-87e8-c0b78dbed754)


# Discussion History
## selsta | 2024-08-22T21:35:55+00:00
It says "Electrum style seed verification failed", which means the seed is invalid. That's why it is grayed out.

## b4n6-b4n6 | 2024-08-22T21:39:45+00:00
It stays grayed out after I have corrected the seed, please observe 00:34

## selsta | 2024-08-22T21:44:34+00:00
Sorry, not sure how I missed that! Seems like a valid report. Can you re-open it here?

https://github.com/monero-project/monero-gui/issues

## selsta | 2024-08-22T22:10:53+00:00
Continuing in GUI repo.

# Action History
- Created by: b4n6-b4n6 | 2024-08-22T21:30:02+00:00
- Closed at: 2024-08-22T22:10:53+00:00
