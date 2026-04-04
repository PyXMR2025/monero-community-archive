---
title: New wallet synchronizing, but network status "Disconnected"
source_url: https://github.com/monero-project/monero-gui/issues/344
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2016-12-22T21:58:04+00:00'
updated_at: '2017-04-22T10:34:38+00:00'
type: issue
status: closed
closed_at: '2017-04-22T10:34:38+00:00'
---

# Original Description
With today's released [beta](https://getmonero.org/2016/12/22/monero-core-gui-beta-released.html), I created a new wallet. While the wallet is synchronizing with the (local) daemon, the network status still shows "**Disconnected**". Afterwards, the network status updates to "Connected". It seems that the network status is not updated at the right time, because synchronizing without connection seems impossible to me?

![monero-wallet-gui beta disconnected](https://cloud.githubusercontent.com/assets/21346321/21441753/0a0f080c-c89a-11e6-83fa-1a7f826e7111.png)


# Discussion History
## medusadigital | 2017-04-18T09:34:10+00:00
that should be solved in Beta 2  AFAIK

## peanutsformonkeys | 2017-04-22T10:34:38+00:00
Indeed, Beta 2 shows "Synchronizing" as Network status right from the start.

# Action History
- Created by: peanutsformonkeys | 2016-12-22T21:58:04+00:00
- Closed at: 2017-04-22T10:34:38+00:00
