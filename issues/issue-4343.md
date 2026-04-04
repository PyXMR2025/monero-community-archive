---
title: '[GUI][Open wallet] Wallet sync status is not correct after changing wallet'
source_url: https://github.com/monero-project/monero-gui/issues/4343
author: b4n6-b4n6
assignees: []
labels:
- bug
created_at: '2024-08-23T08:12:48+00:00'
updated_at: '2024-12-13T23:53:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When I open an unsynchronised wallet after closing a synchronised wallet the unsynched wallet will display 'Wallet is syncronised' for a brief period, before continueing to display  correct status

This bug is much more noticable in bad network conditions or when proxying through tor

[sync-status-bug.webm](https://github.com/user-attachments/assets/ab7372ff-1791-43bc-b6fd-5bd2004f3826)
Please observe 00:17-00:19 status displays 'Wallet is synchronised' even though it is not yet synchronised

[sync-status-bug-2.webm](https://github.com/user-attachments/assets/27339195-e0b8-414d-a8e1-62dd799c92b0)
Please observe 00:11-00:14 status displays 'Wallet is synchronised' even though it is not yet synchronised

Expected behaviour: Wallet displays correct status

# Discussion History
# Action History
- Created by: b4n6-b4n6 | 2024-08-23T08:12:48+00:00
