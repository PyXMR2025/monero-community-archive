---
title: '"verRctNonSemanticsSimple() failed" during large TX construction'
source_url: https://github.com/seraphis-migration/monero/issues/164
author: MoneroArbo
assignees: []
labels: []
created_at: '2025-10-10T13:47:26+00:00'
updated_at: '2025-10-21T23:46:57+00:00'
type: issue
status: closed
closed_at: '2025-10-21T23:46:57+00:00'
---

# Original Description
Using Ubuntu 25.04 and compiled the "latest" source (as of 3 days ago) using https://gist.github.com/jeffro256/543932a8b9de3a42ce474e7aa9184c86

When building a large (90 output in this case) transaction using Monero GUI I get the error "verRctNonSemanticsSimple() failed" only about half the time. The other half the time, transaction construction apparently succeeds.

I'm still waiting for the TX to confirm, but that seems to be due to TX pool backlog.

Log level 3 output is attached.

[monero-wallet-gui.zip](https://github.com/user-attachments/files/22851422/monero-wallet-gui.zip)

# Discussion History
## MoneroArbo | 2025-10-11T03:00:20+00:00
After further testing I think it's an issue specifically with the GUI. I have a wallet set up right now that I can get to give the error every single time, but the same transactions succeed or give sensible errors ("Not enough usable money in top 128 inputs to fund minimum output sum") in the CLI wallet.

If it would be helpful I can share the affected wallet file and/or seed words privately.

## j-berman | 2025-10-11T17:46:31+00:00
Can you DM me your seed over Matrix? I'll investigate with the GUI

## j-berman | 2025-10-15T14:56:50+00:00
> I have a wallet set up right now that I can get to give the error every single time, but the same transactions succeed or give sensible errors ("Not enough usable money in top 128 inputs to fund minimum output sum") in the CLI wallet.

Are you using the same wallet file with GUI and CLI in testing? Or same seed, different wallet files?

I wasn't able to repro with the GUI with the seed you shared unfortunately. If you're available, I think it would be helpful if I can share some code to run on your end to help get to the bottom of this.

## j-berman | 2025-10-15T22:17:15+00:00
I have a hunch (and the logs do seem to confirm the hunch): the wallet starts fetching paths from the tree cache to construct the FCMP++ proof, a block gets added to the chain part way, the wallet auto refreshes in the background and the tree cache updates with a new root, the latter paths used in the proof are now from a different tree state than the earlier paths.

Easily fixed by grabbing the refresh mutex during tx creation.

This doesn't look possible in the CLI because the CLI calls `LOCK_IDLE_SCOPE` before constructing a tx or refreshing. The wallet RPC server is single threaded. However the wallet API's auto refresh happens in a separate thread. So that could explain why this would only surface in the GUI.

## j-berman | 2025-10-21T23:46:57+00:00
Fixed by #183, included in v1.3 of the alpha stressnet release

# Action History
- Created by: MoneroArbo | 2025-10-10T13:47:26+00:00
- Closed at: 2025-10-21T23:46:57+00:00
