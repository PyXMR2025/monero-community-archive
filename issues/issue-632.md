---
title: RPC should return Ok response on some errors
source_url: https://github.com/Cuprate/cuprate/issues/632
author: Boog900
assignees: []
labels:
- C-bug
created_at: '2026-06-08T12:25:41+00:00'
updated_at: '2026-07-11T17:45:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monerod sends ok responses on some errors with the errors in the status field, we should do the same.

As RPC is still being worked on this will need to wait though. 


# Discussion History
## SyntheticBird45 | 2026-06-08T13:12:43+00:00
more details please

## Boog900 | 2026-06-08T13:14:16+00:00
This is just an issue for myself, but if you look at monerod it will return some errors in the status field of the JSON response, we will return a http error 

## Boog900 | 2026-07-11T17:45:02+00:00
At a certain point we need to draw a line at compatibility, we wont match error messages exactly, the response will also not be the _exact_ byte for byte same.

I am open to fixes for someone who needs something specific, for a good reason, but we can't go out our way to support fragile software for the sake of it. 

# Action History
- Created by: Boog900 | 2026-06-08T12:25:41+00:00
