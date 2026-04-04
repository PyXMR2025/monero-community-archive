---
title: Remove refresh from call from import_multisig
source_url: https://github.com/monero-project/monero/issues/9312
author: woodser
assignees: []
labels:
- wallet
created_at: '2024-04-29T11:58:38+00:00'
updated_at: '2024-05-04T14:04:12+00:00'
type: issue
status: closed
closed_at: '2024-05-04T14:04:11+00:00'
---

# Original Description
This issue requests removing the `refresh` call from wallet2's `import_multisig` if possible:

https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/wallet/wallet2.cpp#L13892

Refreshing is a relatively expensive operation which can take considerable time, especially over tor, and the wallet should be refreshing periodically anyway, so it could make most sense to remove this call.

Otherwise I observe this call hanging on the tor network and even timing out when it may not be necessary at all.

For comparison, refresh isn't called when key images are imported, etc.

# Discussion History
## jeffro256 | 2024-04-29T17:08:31+00:00
To keep behavior consistent, we could make an argument `do_refresh_after` and default it to `true`. 

## woodser | 2024-04-30T19:56:30+00:00
That sounds ok; the important part is to change the default behavior in monero-wallet-rpc's `import_multisig` call so clients do not have to refresh in order to use this function.

That would lead to the question if the internal default should be false too, considering very few services are hooking into this call directly. But that'd be an internal implementation detail, as long as clients do not need to refresh.

## woodser | 2024-05-04T14:04:12+00:00
Based on testing, the refresh is necessary or the wallet cannot create txs.

# Action History
- Created by: woodser | 2024-04-29T11:58:38+00:00
- Closed at: 2024-05-04T14:04:11+00:00
