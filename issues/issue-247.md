---
title: Tracking Issue for Chain manager
source_url: https://github.com/Cuprate/cuprate/issues/247
author: Boog900
assignees: []
labels:
- P-high
- A-binaries
- C-tracking-issue
created_at: '2024-08-06T17:50:34+00:00'
updated_at: '2024-10-31T23:29:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What

The chain manager, which is the task in `cuprated` that handles incoming blocks from peers or the syncer.

### Steps

- [x] Chain syncer
- [x] Handle new blocks 
    - [x] From the peer channel
    - [x] From the syncer channel
- [ ] Handle chain re-orgs


### Related

I started the syncer here: https://github.com/Cuprate/cuprate/pull/142



# Discussion History
# Action History
- Created by: Boog900 | 2024-08-06T17:50:34+00:00
