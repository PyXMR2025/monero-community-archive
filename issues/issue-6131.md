---
title: wallet2::estimate_blockchain_height() returns 0 if there’s no daemon
source_url: https://github.com/monero-project/monero/issues/6131
author: selsta
assignees: []
labels: []
created_at: '2019-11-14T00:57:51+00:00'
updated_at: '2019-11-16T17:00:43+00:00'
type: issue
status: closed
closed_at: '2019-11-16T17:00:43+00:00'
---

# Original Description
Since somewhere between 2899379791b7542e4eb920b5d9d58cf232806937 and master `wallet2::estimate_blockchain_height()` started to always return 0 if there’s no daemon connection.

It should fallback to `wallet2::get_approximate_blockchain_height()` in this case, but this appears to be broken.

Can be tested with: `./monero-wallet-cli --offline --generate-new-wallet "test" --mnemonic-language English` and then `restore_height`.

# Discussion History
# Action History
- Created by: selsta | 2019-11-14T00:57:51+00:00
- Closed at: 2019-11-16T17:00:43+00:00
