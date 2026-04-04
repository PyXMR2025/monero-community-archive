---
title: Display block heights in the GUI
source_url: https://github.com/monero-project/monero-gui/issues/1168
author: leafcutterant
assignees: []
labels:
- enhancement
created_at: '2018-03-06T15:41:27+00:00'
updated_at: '2018-04-25T11:25:55+00:00'
type: issue
status: closed
closed_at: '2018-04-25T11:25:54+00:00'
---

# Original Description
Related: 
#766 GUI says "Synchronizing" when it hasn't connected yet

When the highest block height is higher than the last block that was scanned for all addresses in the wallet, there could be another line under the progress bar:

{lastBlockScannedForAllAddresses}/{highestKnownBlock}

(There is a third block height, the highest downloaded block, but I suggest not including that in the GUI. NEO's Neon wallet does that and it looks super confusing. Users mostly watch the progress just to see if they received their funds.)

If the wallet is all synced and scanned, I propose displaying just the latest block height next to/under the "Connected" text box.

# Discussion History
## sanderfoobar | 2018-03-29T23:14:36+00:00
+enhancement

## sanderfoobar | 2018-03-30T01:39:44+00:00
#891

## leafcutterant | 2018-04-25T11:25:54+00:00
I believe this is fixed now, so closing.

# Action History
- Created by: leafcutterant | 2018-03-06T15:41:27+00:00
- Closed at: 2018-04-25T11:25:54+00:00
