---
title: '[Feature request] "Fix busted wallet" option'
source_url: https://github.com/monero-project/monero-gui/issues/700
author: Gingeropolous
assignees: []
labels: []
created_at: '2017-04-29T03:59:36+00:00'
updated_at: '2017-06-04T10:17:20+00:00'
type: issue
status: closed
closed_at: '2017-06-04T10:17:20+00:00'
---

# Original Description
Some button that attempts to fix a wallet thats broken.

For instance, this seems like a good goto

"Removing the cache would result in losing the private tx keys (which are needed in case of disputes) and recipient addresses (which may come in handy from time to time). In this case it's better to first open monerod and type "flush_txpool". Subsequently, open monero-wallet-cli and type "rescan_spent". "

https://bitcointalk.org/index.php?topic=583449.msg18786307#msg18786307

# Discussion History
## Jaqueeee | 2017-05-03T13:53:42+00:00
"rescan spent" is already available. Moved button to settings page in #707 and renamed it to "Rescan wallet balance". Not adding "flush_txpool" for now since it's potentially dangerous for avg users. (the tx could still be mined and the user can end up with sending multiple times)

# Action History
- Created by: Gingeropolous | 2017-04-29T03:59:36+00:00
- Closed at: 2017-06-04T10:17:20+00:00
