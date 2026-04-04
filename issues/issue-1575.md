---
title: Replace term "block height" with a time based value
source_url: https://github.com/monero-project/monero-gui/issues/1575
author: Herroo
assignees: []
labels: []
created_at: '2018-09-30T17:17:15+00:00'
updated_at: '2018-09-30T19:20:50+00:00'
type: issue
status: closed
closed_at: '2018-09-30T19:20:49+00:00'
---

# Original Description
The term "block height" is a somewhat technical term which non-tech users does not really understand. Because of this far to many users use no block height value resulting in syncing the entire blockchain. This impacts their overall feeling of Monero as being "slow" to sync.

Idea:
Replace the "block height" term with a time-based representation. The block height would still need to exist in the backend, but a time based value would help users use it.

Example:
Instead of having an input box for a block height value have a slider: 
<-- January 2017 -->                  (regular font)
 (block height xxxxxxx)                (smaller font)

Requires:
Calculator in the backend to recalculate block height to dates.

Hopeful outcome:
More frequently used "block height" resulting in a better overall experience of the syncing process

# Discussion History
## dEBRUYNE-1 | 2018-09-30T18:23:41+00:00
Basically similar as the idea proposed in #1551 right? 

## Herroo | 2018-09-30T19:20:49+00:00
@dEBRUYNE-1 Ohh! Yes the same idea - missed it before creating mine. Now I just need to figure out how to close my issue

# Action History
- Created by: Herroo | 2018-09-30T17:17:15+00:00
- Closed at: 2018-09-30T19:20:49+00:00
