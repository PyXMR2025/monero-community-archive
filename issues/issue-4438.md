---
title: Is ledger flex support planned?
source_url: https://github.com/monero-project/monero-gui/issues/4438
author: folander
assignees: []
labels: []
created_at: '2025-04-28T23:20:40+00:00'
updated_at: '2025-08-31T12:32:45+00:00'
type: issue
status: closed
closed_at: '2025-08-31T12:32:45+00:00'
---

# Original Description
I was recently trying to set up a wallet with my ledger flex and it seems that all other ledger models are supported but the flex. Is this going to be added?

# Discussion History
## selsta | 2025-04-29T09:41:45+00:00
@folander does it work if you select the Ledger Stax or a different Ledger device?

## folander | 2025-04-29T16:58:19+00:00
Okay so update now that I've slept on it. I had tried to initialize the wallet while my ledger was unlocked on the main menu screen. I tried it with all available ledger devices in the GUI setup but it said "no device found" or something. today I tried it again and I was able to get it to work.

You have to open the monero app on your ledger flex before creating it in the GUI. Select ledger Stax from the hardware wallet selection. Then the ledger will ask if you authorize it to export the view key. It's not like on ledger live where it will just open the app automatically. I hope this helps someone.

# Action History
- Created by: folander | 2025-04-28T23:20:40+00:00
- Closed at: 2025-08-31T12:32:45+00:00
