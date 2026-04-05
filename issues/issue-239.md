---
title: Standalone xmrig without configuration failed to compile
source_url: https://github.com/xmrig/xmrig/issues/239
author: Halo07
assignees: []
labels:
- question
- libuv
created_at: '2017-12-04T19:18:38+00:00'
updated_at: '2017-12-07T14:07:43+00:00'
type: issue
status: closed
closed_at: '2017-12-07T14:07:43+00:00'
---

# Original Description
I try to compile my own version of xmrig without configuration file. 
But i can't because i got an error: fatal error: uv.h: No such file or directory
How can i fix this? Or if is there another way to make a standalone version of xmrig?

# Discussion History
## xmrig | 2017-12-06T15:40:20+00:00
libuv mandatory dependency, you can use precompiled libuv version.
Thank you.

## Halo07 | 2017-12-06T15:42:03+00:00
but if i used precompiled libuv verssion (latest) after copile, xmrig request libuv.dll in the same dir

## xmrig | 2017-12-07T04:34:04+00:00
Did you check compile docs https://github.com/xmrig/xmrig/wiki/Windows-Build ?
You can use https://github.com/xmrig/xmrig-deps/releases or build libuv byself, it's not too hard.
Official precompiled libuv provide only dynamic library (not static) so dll file required.
Thank you.

## Halo07 | 2017-12-07T14:07:43+00:00
i need to compile libuv on x64... That was the problem! Thank you!

# Action History
- Created by: Halo07 | 2017-12-04T19:18:38+00:00
- Closed at: 2017-12-07T14:07:43+00:00
