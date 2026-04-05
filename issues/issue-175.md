---
title: Improve network initialization
source_url: https://github.com/Cuprate/cuprate/issues/175
author: Boog900
assignees:
- Asurar0
labels:
- A-p2p
- C-proposal
- E-medium
- P-medium
created_at: '2024-06-19T18:39:11+00:00'
updated_at: '2025-04-08T18:49:31+00:00'
type: issue
status: closed
closed_at: '2025-04-08T18:49:31+00:00'
---

# Original Description


## What

Network initialization without an existing `p2p_store` file is pretty unstable, taking a while to complete. 

## Where

`cuprate-p2p` specifically the connection maintainer. 

## How

Separate connecting to initial peers from maintaining the peer count.


# Discussion History
## Asurar0 | 2024-09-10T10:51:19+00:00
Hello, I'd like to take on this issue, if it remains unassigned.

## Boog900 | 2024-09-10T17:15:46+00:00
Sure, this is more of an open ended issue than #176 though lmk if you want to discuss anything 

# Action History
- Created by: Boog900 | 2024-06-19T18:39:11+00:00
- Closed at: 2025-04-08T18:49:31+00:00
