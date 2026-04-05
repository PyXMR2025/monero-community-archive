---
title: Add a RW lock to the context service.
source_url: https://github.com/Cuprate/cuprate/issues/314
author: Boog900
assignees: []
labels:
- C-proposal
created_at: '2024-10-14T17:14:51+00:00'
updated_at: '2024-10-14T17:14:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
RwLock to the blockchain context service to prevent the blockchain from mutating while we handle a request.

## Why
Some requests require looking at multiple service, if the blockchain mutates some of the information will be outdated  

## How
TODO


# Discussion History
# Action History
- Created by: Boog900 | 2024-10-14T17:14:51+00:00
