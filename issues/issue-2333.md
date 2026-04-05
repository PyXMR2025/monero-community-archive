---
title: 'DNS error: "unknown node or service"  on Linux'
source_url: https://github.com/xmrig/xmrig/issues/2333
author: Aload
assignees: []
labels: []
created_at: '2021-04-30T07:22:50+00:00'
updated_at: '2025-06-16T20:31:08+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:31:08+00:00'
---

# Original Description

Appears when I boot

![image](https://user-images.githubusercontent.com/13082598/116661996-afa92b80-a941-11eb-955e-bcc955f32880.png)


# Discussion History
## SChernykh | 2021-04-30T07:42:21+00:00
You have a typo in xmrig commad line. Check it for missing or excess spaces, dashes, quotes etc. Or use https://xmrig.com/wizard to generate correct command line.

## Spudz76 | 2021-05-02T04:34:32+00:00
If you missed double dash, it will think you mean `-d -o nate-level 1 ....`

# Action History
- Created by: Aload | 2021-04-30T07:22:50+00:00
- Closed at: 2025-06-16T20:31:08+00:00
