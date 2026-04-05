---
title: api /1/threads not work
source_url: https://github.com/xmrig/xmrig/issues/2318
author: xiongzegang
assignees: []
labels:
- duplicate
created_at: '2021-04-26T15:32:46+00:00'
updated_at: '2022-04-03T14:53:30+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:53:30+00:00'
---

# Original Description
get /1/threads, response is { "status": 404, "error": "Not Found" }
version: 6.12.1

# Discussion History
## Spudz76 | 2021-04-27T16:42:51+00:00
I noticed this also, apparently that endpoint was dropped sometime.  Sucks because it was the only way to get `PCI Location => GPU index` mappings... to know which one was really which...

The only valid endpoint now for status information is `/1/summary`

I do not know when it was changed, but I do know my old monitor script used `/1/threads` and it didn't work when I went to use it again.  And it used PCI location as the GPU identifier, not indices, so the summary doesn't work for me at all.

## xmrig | 2021-04-27T17:16:31+00:00
#1541

## Spudz76 | 2021-04-28T14:49:21+00:00
Oh dang, completely missed the existence of `/2/backends`, thanks for the pointer!

# Action History
- Created by: xiongzegang | 2021-04-26T15:32:46+00:00
- Closed at: 2022-04-03T14:53:30+00:00
