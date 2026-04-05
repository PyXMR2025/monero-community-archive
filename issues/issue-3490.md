---
title: XMRig has a Windows ARM32 build?
source_url: https://github.com/xmrig/xmrig/issues/3490
author: g0newiped
assignees: []
labels:
- wontfix
created_at: '2024-06-03T05:16:11+00:00'
updated_at: '2025-06-16T19:42:52+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:42:52+00:00'
---

# Original Description
I know that maybe is not profitable, but i would try on my Surface RT that has a ARM32 CPU.

# Discussion History
## geekwilliams | 2024-06-03T07:34:15+00:00
[Check out this repo to compile it yourself ](https://github.com/pragathoys/build_xmrig_for_armv7)

## SChernykh | 2024-06-03T07:58:41+00:00
There is no JIT compiler for 32-bit architectures, so it will be VERY slow. I'm talking about less than 1 h/s kind of slow.

# Action History
- Created by: g0newiped | 2024-06-03T05:16:11+00:00
- Closed at: 2025-06-16T19:42:52+00:00
