---
title: 'Feature request: add ConnectionStatus_Connecting state'
source_url: https://github.com/monero-project/monero/issues/6308
author: rating89us
assignees: []
labels: []
created_at: '2020-01-27T14:12:02+00:00'
updated_at: '2020-01-30T21:33:32+00:00'
type: issue
status: closed
closed_at: '2020-01-30T21:33:32+00:00'
---

# Original Description
Currently the wallet returns the following connection states:
- `ConnectionStatus_Connected`
- `ConnectionStatus_WrongVersion`
- `ConnectionStatus_Disconnected`

It would be nice to have an additional `ConnectionStatus_Connecting` state, so we could display in monero GUI a "Connecting..." message, which would mean that the wallet is currently disconnected, but trying to connect.

# Discussion History
## moneromooo-monero | 2020-01-27T16:15:28+00:00
Those are GUI things (or at least I don't recognize the names) so should be filed in the GUI repo.

## xiphon | 2020-01-28T05:09:34+00:00
Yep, implemented this on the GUI side https://github.com/monero-project/monero-gui/pull/2747

# Action History
- Created by: rating89us | 2020-01-27T14:12:02+00:00
- Closed at: 2020-01-30T21:33:32+00:00
