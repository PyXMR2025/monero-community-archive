---
title: A better way to tell the txpool about spent key images
source_url: https://github.com/Cuprate/cuprate/issues/695
author: Boog900
assignees: []
labels:
- C-proposal
created_at: '2026-08-26T21:55:32+00:00'
updated_at: '2026-08-26T21:56:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently we just send the tx pool all the key images in a block. Instead we should only send the key images to the tx pool if there are less key images in the block(s) than in the pool, if there are more the txpool should do the reverse and check its key image against the main chain.

# Discussion History
# Action History
- Created by: Boog900 | 2026-08-26T21:55:32+00:00
