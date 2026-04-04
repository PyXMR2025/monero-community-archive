---
title: Values input to prove/check remain cached
source_url: https://github.com/monero-project/monero-gui/issues/4148
author: luphoria
assignees: []
labels: []
created_at: '2023-04-10T21:23:54+00:00'
updated_at: '2023-08-17T15:31:38+00:00'
type: issue
status: closed
closed_at: '2023-08-17T15:31:38+00:00'
---

# Original Description
I entered a TXID, address, and OutProofV2 to the Check Transaction / Reserve section, verified the transaction, and then fully signed out and deleted the wallet. I created a new wallet without closing the GUI, and I still see all of the values I previously input.
This is a security risk given physical access - especially considering it bypasses the timer to lock the wallet, if someone wants to view the data in there.

# Discussion History
## plowsof | 2023-04-10T21:47:42+00:00
Hi, a similar issue was fixed in this pull request https://github.com/monero-project/monero-gui/pull/4078/files , won't be a problem to have these cleared also , thanks for reporting 

# Action History
- Created by: luphoria | 2023-04-10T21:23:54+00:00
- Closed at: 2023-08-17T15:31:38+00:00
