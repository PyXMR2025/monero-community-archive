---
title: --prune-blockchain flag not working in AppImage
source_url: https://github.com/monero-project/monero-gui/issues/4508
author: Yagat0
assignees: []
labels: []
created_at: '2025-10-11T13:06:00+00:00'
updated_at: '2026-01-13T13:52:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Without the --prune-blockchain flag the daemon starts and the app successfully connects to it.

When I use the flag and try to start the daemon via the GUI, the app won't connect with an error in log: [11 Oct 2025 14:06:33] 2025-10-11 12:06:32.979 I Monero 'Fluorine Fermi' (v0.18.4.3-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

Now I am using the official AppImage from getmonero.org. Previously I used the AUR package, but it wasn't able to connect to my Trezor.

# Discussion History
## nahuhh | 2025-10-11T15:19:47+00:00
Prune has a gui option/toggle. youre probably setting it twice (via gui and via flag) causing the node to not-start

## Yagat0 | 2025-10-11T15:41:07+00:00
> Prune has a gui option/toggle. youre probably setting it twice (via gui and via flag) causing the node to not-start

I can't find the prune option anywhere in the node settings and anywhere else. Where precisely should it be located?

## selsta | 2025-10-11T15:42:16+00:00
It's an option when you create a new wallet in the wizard, but it can only be selected if you don't have an existing pruned blockchain.

## Yagat0 | 2025-10-11T16:12:45+00:00
I deleted the blockchain files. The wallet creation really shows the prune option, so my problem is pretty much solved. On the other hand I think it is pretty misleading if you want to switch from pruned to full node because there is no other option to disable it than deleting the blockchain and creating a new wallet as far as I know.

## selsta | 2025-10-11T16:14:07+00:00
If a node is pruned the data is deleted, you would have to sync from scratch to get it back that's why there is no unprune option.

## Yagat0 | 2025-10-11T16:18:14+00:00
Yes and therefore if there would be such option, the user should be warned about this consequence, but it shouldn't be an obstacle for it to not exist.

## nahuhh | 2025-10-11T16:56:43+00:00
You cant "unprune" a node. This is normal across btc, xmr, etcetera.

gui defaults to a pruned node, because... if youre using GUI to run a node (as opposed to CLI), you likely dont have any use for a full node

## omurad | 2026-01-13T08:18:09+00:00
I agree with @Yagat0 point regarding warning users. It wouldn't be unreasonable for a technically competent user to assume that a pruned node can become a full node.

The `Prune blockchain` checkbox should should warn the user of this, at least in simple mode.

## nahuhh | 2026-01-13T13:52:00+00:00
@omurad i disagree.

a technically competent user:
- wouldnt expect monero to be the only blockchain that can un-prune a node
- wouldnt be using simple mode (which doesnt sync a node at all)

# Action History
- Created by: Yagat0 | 2025-10-11T13:06:00+00:00
