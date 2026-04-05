---
title: initial p2p code
source_url: https://github.com/Cuprate/cuprate/pull/8
author: Boog900
assignees: []
labels:
- A-p2p
created_at: '2023-03-11T23:58:33+00:00'
updated_at: '2024-05-27T01:09:31+00:00'
type: pull_request
status: merged
closed_at: '2023-04-24T21:37:41+00:00'
merged_at: '2023-04-24T21:37:41+00:00'
---

# Original Description
No description

# Discussion History
## SyntheticBird45 | 2023-04-23T11:11:08+00:00
Rust convention is to format satefy comment :
`// SAFETY: Reason`
maybe just change this comment as 
```
// This function use unwrap
// SAFETY : Its caller responsability to ensure the timestamp is valid.
```

# Action History
- Created by: Boog900 | 2023-03-11T23:58:33+00:00
- Merged at: 2023-04-24T21:37:41+00:00
