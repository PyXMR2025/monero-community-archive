---
title: GhostRider algo does not honor `cpu-max-threads-hint`
source_url: https://github.com/xmrig/xmrig/issues/3546
author: mwp-foss
assignees: []
labels: []
created_at: '2024-09-03T17:52:36+00:00'
updated_at: '2025-06-28T10:29:39+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:29:39+00:00'
---

# Original Description
              > XMRig runs threads in pairs for GhostRider (each thread in config = 2 threads running), so this is expected behavior.

This behavior is counter intuitive to `cpu-max-threads-hint`. The algorithm should query `cpu-max-threads-hint` and auto set itself to thread pairs within the suggested limit, not double the limit because it needs thread-pairs.

For example:

`cpu-max-threads-hint` is set to `25` on a 16c/32t processor, this would mean use a max of 8 threads; GhostRider would set itself to 4 thread pairs

`cpu-max-threads-hint` is set to `22` on a 16c/32t processor, this would mean use a max of 7 threads; GhostRider would set itself to 3 thread pairs

_Originally posted by @mwpow3ll in https://github.com/xmrig/xmrig/issues/2865#issuecomment-2327099680_

# Discussion History
# Action History
- Created by: mwp-foss | 2024-09-03T17:52:36+00:00
- Closed at: 2025-06-28T10:29:39+00:00
