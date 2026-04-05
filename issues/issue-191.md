---
title: In house transaction and block types (wrappers)
source_url: https://github.com/Cuprate/cuprate/issues/191
author: Boog900
assignees: []
labels:
- A-types
- C-proposal
created_at: '2024-06-22T21:47:13+00:00'
updated_at: '2024-06-23T23:45:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What

Currently we are using `monero-serai` directly across multiple crates, this proposal is to create wrapper types in `types` that we use across crates instead. 

## Why

This will allow us to do things like caching the tx hash, we currently do this in the consensus crates, however we also calculate tx hashes in the block downloader, which isn't cached.  

## Where

`types` and anywhere currently using monero-serai

## How

Right now monero-serai is planning a big change to their transaction type seen as we are going to have to make (a lot of) changes for this it makes sense to do this at the same time 


# Discussion History
## kayabaNerve | 2024-06-23T18:20:20+00:00
Not to say you shouldn't add a wrapper struct, yet I'm curious the argument against localized hashes.

Hash a TX as it comes in, store said hash with the TX.

Is the argument that the wrapper, despite being a wrapper, would offer better overall UX and prevent cache misses across distinct areas? If you use the Deref types as Box does, it _should_ be quite seamless I think...

## Boog900 | 2024-06-23T23:45:25+00:00
yes, mainly for UX. I am also considering only exposing the necessary API for Cuprate on the the types although I don't really think the benefits are there.

# Action History
- Created by: Boog900 | 2024-06-22T21:47:13+00:00
