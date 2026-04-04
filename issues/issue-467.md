---
title: history tab in gui does not autmatically refresh date/transactions
source_url: https://github.com/monero-project/monero-gui/issues/467
author: TheSwampThing
assignees: []
labels: []
created_at: '2017-02-09T19:35:01+00:00'
updated_at: '2017-03-07T11:04:06+00:00'
type: issue
status: closed
closed_at: '2017-03-07T11:04:06+00:00'
---

# Original Description
noticed some weird behavior in the GUI wallet

2 days ago i synced and left my wallet open since.
1 day ago the pool send me some XMR. it showed up in the balance indicator, but the transaction did not show in the 'history' tab. Only after close/restart gui it did appear. also, the filter date showed the date from when i opened the wallet, not today's date.
Apparently this page does not dynamically update both date and transactions.
gui version: 13253c3
embedded monero version dd580d7

# Discussion History
## Jaqueeee | 2017-03-04T23:19:53+00:00
@TheSwampThing first issue is fixed in #541.

# Action History
- Created by: TheSwampThing | 2017-02-09T19:35:01+00:00
- Closed at: 2017-03-07T11:04:06+00:00
