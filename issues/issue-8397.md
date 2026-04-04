---
title: Add `generate_blocks addr numblocks [starting_nonce]` command to monerod when
  in regtest mode
source_url: https://github.com/monero-project/monero/issues/8397
author: LeoNero
assignees: []
labels: []
created_at: '2022-06-21T18:12:58+00:00'
updated_at: '2024-01-17T12:39:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When in `--regtest`, `monerod` provides a RPC call `generateblocks` that receives as parameters: `amount_of_blocks`, `wallet_address`, and `starting_nonce`. This is really useful when you don't want to keep mining all the time when testing and only mine blocks when you need/want to.

However, having to call it using `curl`/`httpie` in another terminal gets boring and annoying really fast, especially since, when testing, I do not want to run `monerod` in the background (i.e no `--detach` flag) . So I would suggest having a command `generate_blocks` on `monerod` that receives the same arguments (but makes `starting_nonce` optional for simplicity).

Such command would only be available if `--regtest` was passed when initializing `monerod`.

# Discussion History
## LeoNero | 2022-06-21T18:13:08+00:00
I am down to implement this feature.

## meglio | 2024-01-17T12:39:15+00:00
Any updates?

# Action History
- Created by: LeoNero | 2022-06-21T18:12:58+00:00
