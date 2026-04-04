---
title: Daemon is still running even after closing GUI Monero-wallet
source_url: https://github.com/monero-project/monero/issues/9216
author: Jessie-1
assignees: []
labels:
- question
- low priority
- more info needed
created_at: '2024-03-07T13:58:39+00:00'
updated_at: '2024-03-12T02:19:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Platform : MacOS Sonoma 14.3.1
Monero Version: 0.18.3.1 - Fluorine Fermi. gui/mac64

I see traffic to remote nodes hours after closing GUI wallet gracefully.

# Discussion History
## selsta | 2024-03-07T13:59:56+00:00
When closing the GUI it asks you if you want to also stop the daemon or keep it running in the background.

## Jessie-1 | 2024-03-07T14:18:26+00:00
I can't reproduce it now, but previously I did. I logged out of 'simple wallet' mode to switch to 'advanced mode' to input a custom RPC node. Perhaps the first step didn't kill the daemon if the app was exited from 'advanced mode'.

## selsta | 2024-03-07T14:20:27+00:00
If you have a remote node selected the daemon won't try to interact with your local node. In this case you can stop the running daemon before switching to a remote node.

## Jessie-1 | 2024-03-07T14:31:06+00:00
> you can stop the running daemon before switching to a remote node.

Yes, there is an option to stop the daemon before switching to a remote node, and the wallet asks the user (image 1) to either stop it or keep it running in the background if the wallet is closed from the 'Local node' interface. However, it does not ask the user if they switch to a remote node without stopping the daemon.

For a better user experience (UX), the wallet should prompt the user ( image 2) whether to close the daemon when the user clicks 'close wallet'.

Image 1:
----------
![imag3 1](https://github.com/monero-project/monero/assets/80989068/cab6df6c-2ef6-4c52-998e-f560926e0415)

Image 2:
----------
![image 2](https://github.com/monero-project/monero/assets/80989068/b8691ebf-5317-45ec-afc9-eb447fe78849)


## selsta | 2024-03-12T02:19:02+00:00
> For a better user experience (UX), the wallet should prompt the user ( image 2) whether to close the daemon when the user clicks 'close wallet'.

When selecting remote node then you tell the wallet you don't want to manage your local node. It does not try to connect to it, which means also means the GUI does not even know if a local node is running.

The current behavior is working as intended.

# Action History
- Created by: Jessie-1 | 2024-03-07T13:58:39+00:00
