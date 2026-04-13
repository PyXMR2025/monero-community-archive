---
title: Optimization for watch-only hot wallet <> cold wallet flow
source_url: https://github.com/monero-project/monero/issues/8962
author: j-berman
assignees: []
labels:
- feature
- proposal
created_at: '2023-07-28T23:32:35+00:00'
updated_at: '2023-12-07T20:26:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### Context

This is how a watch-only hot wallet that doesn't have a spend key is able to tell which outputs are spent (how the watch-only wallet gets each output's key image to see if the key images are included in the chain):

1. Hot wallet: `export_outputs`
2. Cold wallet: `import_outputs` from step 1
3. Cold wallet: `export_key_images`
4. Hot wallet: `import_key_images` from step 3

A hot wallet technically only needs key images it does not already know about. Thus wallet2 offers an `all` boolean to the export functions:
- If a hot wallet calls `export_outputs(all=false)`, the hot wallet only exports outputs it does not know key images for.
- If a cold wallet calls `export_key_images(all=false)`, the cold wallet only exports key images that the hot wallet has told the cold wallet it does not know key images for.

However, a hot wallet needs to call `export_outputs(all=true)` in order to tell the cold wallet which outputs the hot wallet already has key images for. If a hot wallet doesn't do this, every time the cold wallet calls `export_key_images(all=false)`, it will export *all* signed key images in the wallet even if the hot wallet already knows about some of the key images. This hobbles the purpose of the `all` boolean a bit I think.

### The easy optimization

When a hot wallet calls `export_outputs(all=false)`, the payload could include a 1 byte boolean flag indicating to the cold wallet that all outputs prior to the `offset` are known. Alternatively, the cold wallet could just assume that all imported outputs prior to an `offset` have known key images, but this may be unsafe and needs another look.

With this optimization, when hot wallets call `export_outputs(all=false)`, and the cold wallet imports and calls `export_key_images(all=false)`, the cold wallet will only export the key images the hot wallet needs.


# Discussion History
## ghost | 2023-08-11T04:57:37+00:00
these types of optimizations are essential for building great UX around advanced features like airgapped transactions - the smaller/more efficient we can get monero's cold-signing payloads to be, the better

# Action History
- Created by: j-berman | 2023-07-28T23:32:35+00:00
