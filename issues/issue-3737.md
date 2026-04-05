---
title: Can we get a --start-paused argument?
source_url: https://github.com/xmrig/xmrig/issues/3737
author: divinity76
assignees: []
labels: []
created_at: '2025-12-02T19:04:08+00:00'
updated_at: '2025-12-03T00:06:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I want a --start-paused argument where all initialization, config validation, and allocation is done, 
but it's started paused, waiting for a resume command. Can we get that? Would a PR be considered? 

Rationale is that in some situations I only want to allocate hugepages at boot.

Edit: made a PR: https://github.com/xmrig/xmrig/pull/3738

# Discussion History
# Action History
- Created by: divinity76 | 2025-12-02T19:04:08+00:00
