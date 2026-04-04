---
title: daemonBlockChainTargetHeight always returns 0
source_url: https://github.com/monero-project/monero/issues/2880
author: rusticbison
assignees: []
labels:
- invalid
created_at: '2017-12-01T06:42:11+00:00'
updated_at: '2017-12-01T10:00:27+00:00'
type: issue
status: closed
closed_at: '2017-12-01T10:00:27+00:00'
---

# Original Description
https://github.com/monero-project/monero/blob/2e54e7ff0b10d262eb95b6f0124ccd8d621af7b7/src/wallet/api/wallet2_api.h#L520

The expected result of this function is the current blockchain height, e.g. 1051347, or an error message. 

However, regardless of daemon syncing or fully synced status, the function always returns 0. 

The error message string is empty: 
`Wallet daemon blockchain height 0, additional info: status=0, errorString=‘’`

How can we find the current blockchain height? 

# Discussion History
## moneromooo-monero | 2017-12-01T09:59:06+00:00
The documentation you quote says it's the target height, and then you proceed to say it's the current height. You can get the current height with the getinfo daemon RPC, as "height" (that RPC also returns the target height).

+invalid


# Action History
- Created by: rusticbison | 2017-12-01T06:42:11+00:00
- Closed at: 2017-12-01T10:00:27+00:00
