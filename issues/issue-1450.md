---
title: How to reduce the volume of compilation
source_url: https://github.com/xmrig/xmrig/issues/1450
author: axsoftshi
assignees: []
labels:
- question
created_at: '2019-12-20T14:18:32+00:00'
updated_at: '2019-12-21T19:41:22+00:00'
type: issue
status: closed
closed_at: '2019-12-21T19:41:22+00:00'
---

# Original Description
How to reduce the compilation volume to about 800KB without UDX shell Microsoft Visual Studio 2017

# Discussion History
## axsoftshi | 2019-12-21T11:41:41+00:00
@xmrig 

## xmrig | 2019-12-21T19:41:22+00:00
1. Remove unused algorithms/features https://xmrig.com/docs/miner/cmake-options
2. Change flags https://github.com/xmrig/xmrig/blob/master/cmake/flags.cmake#L60 to prefer smaller size.

But I not sure is 800KB still possible.
Thank you.

# Action History
- Created by: axsoftshi | 2019-12-20T14:18:32+00:00
- Closed at: 2019-12-21T19:41:22+00:00
