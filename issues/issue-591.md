---
title: FCMP++ tree manager
source_url: https://github.com/Cuprate/cuprate/issues/591
author: Boog900
assignees: []
labels:
- C-proposal
created_at: '2026-03-12T13:36:03+00:00'
updated_at: '2026-03-12T13:36:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
# What

This proposal is for the FCMP tree manager, which will handle storing the FCMP++ tree, building it and keeping it in sync.

# How

## Storage

The tree should be stored in a [tapes](https://github.com/Cuprate/Tapes) database, with each layer being a different tape. The tape at the lowest layer will be
the output tape. Storing each layer in the tapes means we can maximise the benefits of file read-ahead when building a new tree as all children will be contiguous and in order. If we go layer by layer filling in whole layers at a time, this will also make the tree
building parallelisable as different workers can take different child chunks. 

## Keeping in sync

The tree manager should be a separate system to the other blockchain state systems. Because it is relatively expensive to extend the tree
_and_ the result of an extension is not immediately needed, we can let the tree workers extend the tree in the background.

The tree is built ahead of the chain as explained here: https://github.com/j-berman/monero/blob/2cbdf0b7f63ea67505315efe46adc63b8312e716/docs/FCMP%2B%2B_INTEGRATION.md?plain=0#adding-locked-outputs-to-the-db
This means when a block is added to the chain we can add the outputs to the lowest layer of the tree and notify the workers,
but we do _not_ need to wait for the workers to finish. When we need to check the FCMP++ tree hash for an incoming block
we can request it from the manger with a future that resolves immediately if the workers have finished or waits until they do.

When fast syncing, this means the tree building will be a background task and should not impact syncing beyond
the extra CPU usage needed to build the tree, we should not need to wait on the workers during fast sync. 
Once fast sync is over, we will then need to wait for the tree to be sufficiently built.

On startup we can compare the state of the tree to the blockchain to make sure they are in sync, like we do with fjall


# Discussion History
# Action History
- Created by: Boog900 | 2026-03-12T13:36:03+00:00
