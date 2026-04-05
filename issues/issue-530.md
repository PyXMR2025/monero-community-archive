---
title: Change config ports for different networks
source_url: https://github.com/Cuprate/cuprate/issues/530
author: Boog900
assignees: []
labels:
- C-proposal
- E-easy
- A-binaries
created_at: '2025-08-18T22:25:57+00:00'
updated_at: '2025-08-26T15:03:38+00:00'
type: issue
status: closed
closed_at: '2025-08-26T15:03:38+00:00'
---

# Original Description


## What
The config should default to different ports depending on the network zone. 

## Why
monerod does this and to allow easy setup of nodes on different zones on the same computer 

## Where
cuprated's config

## How
changing the port's `u16` value to an enum:

```
enum Port {
    Default,
    Custom(u16)
}
```


# Discussion History
# Action History
- Created by: Boog900 | 2025-08-18T22:25:57+00:00
- Closed at: 2025-08-26T15:03:38+00:00
