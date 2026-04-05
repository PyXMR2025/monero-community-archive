---
title: Make cuprate usable as a library
source_url: https://github.com/Cuprate/cuprate/issues/516
author: binarybaron
assignees: []
labels:
- C-request
created_at: '2025-07-16T18:08:06+00:00'
updated_at: '2025-08-01T22:51:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
<!--
Note: Please search to see if an issue already exists for this request, or if the feature already exists.
-->

## Feature
Expose cuprate as a library to allow it to be embedded within other Rust projects.

## Why
This could be useful for a variety of projects:
1. Wallets that might want to integrate `cuprate` as its node. I'm working on [eigenwallet](https://github.com/eigenwallet/core) (previously UnstoppableSwap) and we'd like to bundle cuprate to use as a node for the wallet and for atomic swaps.
2. Someone might want to build a simple GUI for cuprate (e.g with [Tauri](https://v2.tauri.app/))
3. Blockexplorers could be built on top of cuprate and avoid the RPC API all together
4. Light wallet syncing servers (like [monero-lws](https://github.com/vtnerd/monero-lws)) might get re-written in Rust at some point in the future. They could bundle cuprate directly.
5. Maybe for running data science experiments on the Blockchain (like what mrl does all the time). Honestly don't know if this could be useful but naively I'd think it could be useful.
Probably a ton of other use cases I cannot think of at the moment.

## Additional context
1. I'd like to be able to spawn cuprate (e.g `cuprate::launch(...)`. The function should take a config struct to configure how cuprate should run.
2. I'd like to be able to listen for status events: Is the node synced? How many network connections is it doing? How many peers do we know of? Not all of this is necessary but would be cool to be able to display that to a user. I like how `arti_client` is exposing a simple stream where I can listen for events: https://docs.rs/arti-client/latest/arti_client/struct.TorClient.html#method.bootstrap_events


# Discussion History
## binarybaron | 2025-08-01T06:58:25+00:00
Would you want a PR from me for this?

Or anything else I can do to help make this happen? (e.g more details on what would be useful imo) 

## Boog900 | 2025-08-01T22:51:34+00:00
We have a backlog of big PRs so I want to merge them first before I begin any other big changes. If you would like to work on this then feel free, I would be grateful, although I will get round to this eventually if not.

# Action History
- Created by: binarybaron | 2025-07-16T18:08:06+00:00
