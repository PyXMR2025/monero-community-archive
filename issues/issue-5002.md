---
title: 3-of-5 multisig creation results in 5 different addresses
source_url: https://github.com/monero-project/monero/issues/5002
author: jacoblyles
assignees: []
labels: []
created_at: '2018-12-20T17:21:40+00:00'
updated_at: '2019-01-16T20:41:20+00:00'
type: issue
status: closed
closed_at: '2019-01-16T20:41:20+00:00'
---

# Original Description
I attempted to create a 3-of-5 multisig wallet. When I finished, opening the wallets with `monero-wallet-cli` shows that each of them has a different address. 

I attempted to `export_multisig_info` and `import_multisig_info` to create a transaction. I received the error message `Error: Failed to import multisig info: Multisig info is for a different account`

Testing on commit https://github.com/monero-project/monero/commit/ed54ac8fdfe332c4ec6b9fd9331024d862ecad51

# Discussion History
## jacoblyles | 2018-12-21T22:51:42+00:00
It seems like I was using the wrong APIs to make these wallets. According to [this comment ](https://github.com/monero-project/monero/issues/5000#issuecomment-449515006) I should be using `exchange_multisig_keys` for (n-m)+1 rounds instead of using  `finalize_multisig` if m < n-1. 

In that case `finalize_multisig` should probably return an error instead of making malformed wallets. 

## moneromooo-monero | 2018-12-21T23:42:47+00:00
https://github.com/monero-project/monero/pull/5004 does now.

## jacoblyles | 2019-01-01T01:16:10+00:00
I confirmed the software rejects improper calls to `finalize_multisig` now. This issue can be closed when #5004 is merged

## moneromooo-monero | 2019-01-16T20:29:09+00:00
+resolved

# Action History
- Created by: jacoblyles | 2018-12-20T17:21:40+00:00
- Closed at: 2019-01-16T20:41:20+00:00
