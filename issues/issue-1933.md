---
title: Load WinRing0x64.sys from other path?
source_url: https://github.com/xmrig/xmrig/issues/1933
author: ghost
assignees: []
labels: []
created_at: '2020-11-07T09:53:54+00:00'
updated_at: '2021-04-12T14:35:40+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:35:40+00:00'
---

# Original Description
It's possible to load WinRing0x64.sys from another path other than where the xmrig's exe resides?
Thanks

# Discussion History
## Technetium1 | 2021-02-20T06:28:54+00:00
@ghost It's hardcoded, you would need to recompile https://github.com/xmrig/xmrig/blob/4e671a945d52c5a803fa0e19436c7c58e8ac59c7/src/hw/msr/Msr_win.cpp#L125

# Action History
- Created by: ghost | 2020-11-07T09:53:54+00:00
- Closed at: 2021-04-12T14:35:40+00:00
