---
title: RandomX Seg Fault
source_url: https://github.com/xmrig/xmrig/issues/1063
author: Peterlustig420
assignees: []
labels:
- arm
created_at: '2019-07-17T15:33:56+00:00'
updated_at: '2019-08-10T12:33:45+00:00'
type: issue
status: closed
closed_at: '2019-08-10T12:33:45+00:00'
---

# Original Description
Compiled xmrig with RandomWOW Package on Arm8 device.
after starting xmrig i always get Segmentation fault (Memory is only 2gb)
My Question is:
How can i switch with RandomX algo between light and fast mode?
light requires only 256mb and fast 2gb, so at default xmrig is running with fast mode ?

# Discussion History
## xmrig | 2019-07-17T16:20:43+00:00
Current version always run in fast mode, next major release (v3+) will automatically switch to light mode if failed to allocate dataset. https://i.imgur.com/xr7G5hS.png but ARM code not optimized, it just works and very slow.
Thank you.

# Action History
- Created by: Peterlustig420 | 2019-07-17T15:33:56+00:00
- Closed at: 2019-08-10T12:33:45+00:00
