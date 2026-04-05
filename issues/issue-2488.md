---
title: How limit CPU cores ?
source_url: https://github.com/xmrig/xmrig/issues/2488
author: TSUKER
assignees: []
labels: []
created_at: '2021-07-23T00:28:19+00:00'
updated_at: '2021-07-23T06:47:29+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
How limit core count in used?

# Discussion History
## Spudz76 | 2021-07-23T06:47:29+00:00
After first-run, edit config.json remove some core numbers from the array(s) for the algo(s) you want to limit.

Such as:

`        "rx": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],`

for 12 threads, becomes:
`        "rx": [1, 3, 5, 7, 9, 11],`

for 6 threads on the odd cores...

Note the ordering of core numbers is different between Windows and Linux.

# Action History
- Created by: TSUKER | 2021-07-23T00:28:19+00:00
