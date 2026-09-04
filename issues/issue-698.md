---
title: Remove RPC service helpers
source_url: https://github.com/Cuprate/cuprate/issues/698
author: Boog900
assignees: []
labels:
- C-proposal
created_at: '2026-09-01T15:05:40+00:00'
updated_at: '2026-09-01T15:05:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What

The helpers that just call Cuprate's tower::Services should be removed with their calls in-lined. 

## Why

They should be clunky to call, they are expensive. IMO the RPC abuses these helpers to make multiple expensive requests where instead just 1 request or context lookup would have done.



# Discussion History
# Action History
- Created by: Boog900 | 2026-09-01T15:05:40+00:00
