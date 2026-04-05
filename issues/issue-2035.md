---
title: Can memory be used instead of the three-level cache
source_url: https://github.com/xmrig/xmrig/issues/2035
author: ahTy
assignees: []
labels: []
created_at: '2021-01-12T03:57:06+00:00'
updated_at: '2021-01-12T03:58:51+00:00'
type: issue
status: closed
closed_at: '2021-01-12T03:58:51+00:00'
---

# Original Description
**Describe the bug**
Compared with the number of threads, the intel server cpu three-level cache cannot allocate 2M three-level cache per thread, so there is a great waste of resources

**To Reproduce**
E5 2680 V3 only hava 30M three-level cache, 24 threads.

**Expected behavior**
Add an optional parameter to let the remaining core CPU directly read the memory instead of not using it


# Discussion History
# Action History
- Created by: ahTy | 2021-01-12T03:57:06+00:00
- Closed at: 2021-01-12T03:58:51+00:00
