---
title: The UI seems to break on split transactions
source_url: https://github.com/monero-project/monero-gui/issues/113
author: moneromooo-monero
assignees: []
labels: []
created_at: '2016-11-05T22:02:41+00:00'
updated_at: '2016-11-13T17:58:43+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:58:43+00:00'
---

# Original Description
src/wallet/api/pending_transaction.cpp:    assert(m_pending_tx.size() == 1);



# Discussion History
## medusadigital | 2016-11-06T16:49:42+00:00
@mbg033 can you fix this one? pretty imporant


## mbg033 | 2016-11-06T17:09:17+00:00
yep, will try


## mbg033 | 2016-11-07T10:21:16+00:00
@moneromooo-monero, can you help with tx splitting? is there a way for force it? I'm always getting 1 tx


## moneromooo-monero | 2016-11-07T11:04:20+00:00
Try sending close to your whole balance with highest mixin.

Otherwise, if that still makes only one, find create_transactions_2 in src/wallet/wallet2.cpp, look for "if (try_tx)" in that function, and set try_tx to true just before. 


## mbg033 | 2016-11-07T21:17:46+00:00
ok, it seems I just forgot to remove that assert, it works. Added `PendingTransaction::txCount()` method to API: https://github.com/monero-project/monero-core/pull/129


## fluffypony | 2016-11-13T17:58:43+00:00
Closing as fixed


# Action History
- Created by: moneromooo-monero | 2016-11-05T22:02:41+00:00
- Closed at: 2016-11-13T17:58:43+00:00
