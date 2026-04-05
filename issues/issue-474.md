---
title: Log more info on blockchain sync progress
source_url: https://github.com/Cuprate/cuprate/issues/474
author: hinto-janai
assignees: []
labels:
- C-request
- E-medium
- E-help-wanted
created_at: '2025-05-13T02:12:06+00:00'
updated_at: '2025-05-23T13:12:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
<!--
Note: Please search to see if an issue already exists for this request, or if the feature already exists.
-->

## Feature
Log more info when syncing the blockchain, similar to `monerod`.

## How
Current log:
```
INFO incoming_block{height=3402413 txs=66}: Successfully added block hash="e93464a7feea9b472dd734e61574e295f4b8f809c48ff78ef76d12111992ada7"
```

Potential log:
```
INFO incoming_block{height=3402413 txs=66}: Successfully added block (99.52%, 151 left, estimate: 1h 6m 25s) hash="e93464a7feea9b472dd734e61574e295f4b8f809c48ff78ef76d12111992ada7"
```

Logs after `Synchronised with the network` may not need to emit extra info.

# Discussion History
## SyntheticBird45 | 2025-05-13T09:59:46+00:00
I've discussed with @Boog900 about the how the estimate time is broken on monerod. Ultimately this is hard to achieve because it is multi-factorial. I think we could apply some weight on the estimate with some sample data that could be updated at every release to get more precise timing. (eg we know pre-RCT is near instant and early-RCT is extremely slow, so let's take that into account to avoid having cuprate saying "entire blockchain syncing in 10 minutes" at start.)

I'm not sure of the usefulness of having the top hash of the batch displayed but why not. Otherwise the proposed log format lgtm

## hinto-janai | 2025-05-23T13:12:40+00:00
We could leave time estimates as a TODO and start with `(99.52%, 151 left)` for now.

> I'm not sure of the usefulness of having the top hash of the batch displayed

FYI this was added in https://github.com/Cuprate/cuprate/pull/456.

# Action History
- Created by: hinto-janai | 2025-05-13T02:12:06+00:00
