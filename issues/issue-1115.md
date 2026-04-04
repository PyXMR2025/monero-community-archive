---
title: Receive pane not updating confirmations at the same time as History pane
source_url: https://github.com/monero-project/monero-gui/issues/1115
author: rex4539
assignees: []
labels:
- resolved
created_at: '2018-02-10T22:50:40+00:00'
updated_at: '2019-04-24T13:09:47+00:00'
type: issue
status: closed
closed_at: '2019-04-24T13:09:47+00:00'
---

# Original Description
GUI version: v0.11.1.0-192-g8aee200
Embedded Monero version: v0.10.3.1-1575-ged67e5c

Steps:
1. Receive a transaction.
2. Check the confirmations on History pane and wait until they reach 10/10 and the transaction is fully confirmed.
3. Switch to the Receive pane.

What happened:
The Receive pane still shows 9 transactions. Only after a couple of minutes it changes to 10.

Expected result:
The Receive pane is synced with the History pane.

# Discussion History
## selsta | 2019-04-24T12:37:17+00:00
This feature has been removed from the Receive page. There is now Merchant page, which is also written from scratch so I consider this most likely resolved. Please comment if this is still happening.

+resolved

# Action History
- Created by: rex4539 | 2018-02-10T22:50:40+00:00
- Closed at: 2019-04-24T13:09:47+00:00
