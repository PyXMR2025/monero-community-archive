---
title: Unstable sync towards the top of the chain.
source_url: https://github.com/Cuprate/cuprate/issues/373
author: Boog900
assignees: []
labels:
- A-p2p
- C-bug
- A-binaries
created_at: '2025-01-20T14:42:22+00:00'
updated_at: '2025-03-08T01:54:36+00:00'
type: issue
status: closed
closed_at: '2025-03-08T01:54:36+00:00'
---

# Original Description

## Bug
When you get close to the top of the chain the syncer often exits early, this isn't a problem as it'll be restarted but it does get shown in the logs and probably means we are downloading some of the top blocks multiple times.

## Expected behavior
We should be able to sync without needing to restart the syncer as long as all peers give us valid data.

## Steps to reproduce
Just start `cuprated` and wait to get near the top then look at the logs.


# Discussion History
# Action History
- Created by: Boog900 | 2025-01-20T14:42:22+00:00
- Closed at: 2025-03-08T01:54:36+00:00
