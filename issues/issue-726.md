---
title: '"Network status - Connected" message confusing'
source_url: https://github.com/monero-project/monero-gui/issues/726
author: knaccc
assignees: []
labels:
- duplicate
created_at: '2017-05-13T20:33:56+00:00'
updated_at: '2017-08-08T00:05:08+00:00'
type: issue
status: closed
closed_at: '2017-08-08T00:05:08+00:00'
---

# Original Description
When I launch the GUI wallet, it first says "Network status - Connected". This means that if my wallet is not synchronized with the daemon yet, I will not have any visual indication that I need to wait to see the most up-to-date balance figure for my wallet. Someone that thinks their balance should be higher will panic for the first minute wondering if something has gone wrong.

Then after about a minute, it says "Network status - Synchronizing". This is my first indication that my wallet might not be showing a balance that reflects the latest state of the blockchain.

After the synchronizing finishes, and my balance does reflect the latest state of the blockchain, it goes back to "Network status - Connected", which is a message indistinguishable from the situation where my wallet has yet to synchronize.

Hopefully it should be quite straightforward to quickly determine the block height that other nodes are seeing, and display a more informative message when a user starts the GUI.

# Discussion History
## medusadigital | 2017-08-08T00:00:29+00:00
very related: https://github.com/monero-project/monero-core/issues/766

basically a new introduced state will solve the issue. status will show something like "connecting..." as long as wallet is waiting to start synchronize. 

will close this in favour of the other ticket.

+duplicate



# Action History
- Created by: knaccc | 2017-05-13T20:33:56+00:00
- Closed at: 2017-08-08T00:05:08+00:00
