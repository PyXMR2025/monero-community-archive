---
title: Enable displaying balance in other currencies - BROKEN in Qubes/Whonix
source_url: https://github.com/monero-project/monero-gui/issues/4675
author: duterlyfly
assignees: []
labels: []
created_at: '2026-08-05T07:40:43+00:00'
updated_at: '2026-08-25T05:30:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am running Monero Wallet GUI 0.18.5.2 AppImage in a Qubes/Whonix installation. When I go to Settings>Interface>Enable displaying balance in other currencies, and check mark it, and select USD as my currency, the USD balance does NOT show up in the top left corner of the wallet under Primary account. Instead it just shows "USD ?.??". This is true for all three price sources (Cryptocompare, Kraken, Coingecko). This issue started happening to me since Monero Wallet GUI 0.18.5.1. Before that everything was working perfectly.

Could you please help me fix this in Whonix?

# Discussion History
## nahuhh | 2026-08-05T08:20:32+00:00
If you run 0.18.5.0 now, it works?

## EntropyHoover | 2026-08-25T05:29:27+00:00
There is indeed a commit about network between 0.18.5.0 and 0.18.5.1 https://github.com/monero-project/monero-gui/commit/082cf9a4e6e567d96e85227e8c7707fcfe59bbbc, but I cannot reproduce this error @selsta 


# Action History
- Created by: duterlyfly | 2026-08-05T07:40:43+00:00
