---
title: RandomX does not support windows2003？？？？
source_url: https://github.com/xmrig/xmrig/issues/1389
author: guigeddos123
assignees: []
labels:
- wontfix
created_at: '2019-12-06T05:38:11+00:00'
updated_at: '2020-08-29T04:45:46+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:45:46+00:00'
---

# Original Description
[2019-12-06 12:35:36.668]  rx   #0 skipped (failed to allocate dataset)
[2019-12-06 12:35:36.668]  rx   #1 skipped (failed to allocate dataset)
[2019-12-06 12:35:36.668]  rx   #0 allocated  256 MB huge pages   0% -JIT (0 ms)

[2019-12-06 12:35:36.684]  rx   failed to allocate RandomX datasets, switching t
o slow mode (9 ms)

# Discussion History
## tevador | 2019-12-07T00:08:22+00:00
It's a 32-bit system. No point in mining because:

* There is no 32-bit JIT compiler
* 32-bit Windows limit the amount of user-space memory to 2 GB, which is not enough for efficient mining

You can expect about 1 H/s per core.

# Action History
- Created by: guigeddos123 | 2019-12-06T05:38:11+00:00
- Closed at: 2020-08-29T04:45:46+00:00
