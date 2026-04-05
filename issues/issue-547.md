---
title: Big reorgs cause crashes
source_url: https://github.com/Cuprate/cuprate/issues/547
author: Boog900
assignees: []
labels:
- A-storage
- C-bug
- I-panic
created_at: '2025-09-06T23:48:31+00:00'
updated_at: '2025-09-07T00:00:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Bug
When a lot of blocks are popped (~100,000) the DB crashes as it needs to resize more than 3 times



## Steps to reproduce
start `cuprated` and run `pop_blocks 100000`



# Discussion History
## Boog900 | 2025-09-06T23:49:13+00:00
we probably shouldn't add the blocks to the alt chains when popping blocks, but this is still an issue on huge reorgs 

# Action History
- Created by: Boog900 | 2025-09-06T23:48:31+00:00
