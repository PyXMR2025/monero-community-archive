---
title: estimateTransactionFee no longer takes fee priority into account?
source_url: https://github.com/monero-project/monero/issues/8595
author: pokkst
assignees: []
labels: []
created_at: '2022-09-25T04:46:22+00:00'
updated_at: '2022-10-13T01:38:59+00:00'
type: issue
status: closed
closed_at: '2022-10-13T01:38:59+00:00'
---

# Original Description
Hi.

I've been messing around with Monero's code base as I work on MyNero, and I noticed that in wallet.cpp the estimateTransactionFee method no longer takes the fee priority parameter into account? It appears to simply be unused now. Is there any reason for this? Is there a new method somewhere else that I am not aware of?

https://github.com/monero-project/monero/blob/master/src/wallet/api/wallet.cpp#L1767

# Discussion History
## selsta | 2022-09-25T11:15:02+00:00
We have an issue for it open here: https://github.com/monero-project/monero-gui/issues/4032

## selsta | 2022-10-13T01:38:59+00:00
https://github.com/monero-project/monero/pull/8610

# Action History
- Created by: pokkst | 2022-09-25T04:46:22+00:00
- Closed at: 2022-10-13T01:38:59+00:00
