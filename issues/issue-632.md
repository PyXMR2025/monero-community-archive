---
title: RPC should return Ok response on some errors
source_url: https://github.com/Cuprate/cuprate/issues/632
author: Boog900
assignees: []
labels:
- C-bug
created_at: '2026-06-08T12:25:41+00:00'
updated_at: '2026-06-08T13:14:16+00:00'
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

# Action History
- Created by: Boog900 | 2026-06-08T12:25:41+00:00
