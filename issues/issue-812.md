---
title: Please add -DWITH_TLS=OFF into wiki's build instructions
source_url: https://github.com/xmrig/xmrig/issues/812
author: adem4ik
assignees: []
labels:
- bug
created_at: '2018-10-18T14:39:37+00:00'
updated_at: '2018-10-18T15:53:12+00:00'
type: issue
status: closed
closed_at: '2018-10-18T15:15:39+00:00'
---

# Original Description
2.8.1 added TSL support, but this increases binary size for 2 MB, some people may not need it at all, so there is possibility to build w/o TLS. So my suggestion is simple - please add `-DWITH_TLS=OFF` into wiki: https://github.com/xmrig/xmrig/wiki/Build inside `Additional CMake options`.

# Discussion History
## xmrig | 2018-10-18T15:15:39+00:00
Done.

## adem4ik | 2018-10-18T15:53:11+00:00
@xmrig thank you!

# Action History
- Created by: adem4ik | 2018-10-18T14:39:37+00:00
- Closed at: 2018-10-18T15:15:39+00:00
