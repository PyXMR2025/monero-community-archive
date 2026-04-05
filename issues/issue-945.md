---
title: v2.13.0 What is the default CPU occupation?
source_url: https://github.com/xmrig/xmrig/issues/945
author: ttsite
assignees: []
labels:
- question
created_at: '2019-02-24T05:49:07+00:00'
updated_at: '2019-03-02T06:32:56+00:00'
type: issue
status: closed
closed_at: '2019-03-02T06:32:56+00:00'
---

# Original Description
How much CPU does v2.13.0 currently occupy by default? If you want to remain at 75% occupancy, how to modify the source code, where is the location? Thank you!!!

# Discussion History
## xmrig | 2019-02-24T05:56:23+00:00
https://github.com/xmrig/xmrig/blob/master/src/core/Config.cpp#L52 this option now deprecated and likely will be removed or renamed for something less confusing in xmrig3.
Thank you.

## xmrig | 2019-03-02T06:32:56+00:00
https://github.com/xmrig/xmrig/issues/957#issuecomment-468890667

# Action History
- Created by: ttsite | 2019-02-24T05:49:07+00:00
- Closed at: 2019-03-02T06:32:56+00:00
