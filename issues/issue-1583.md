---
title: cross build for armv7?
source_url: https://github.com/xmrig/xmrig/issues/1583
author: esrrhs
assignees: []
labels:
- question
created_at: '2020-03-07T09:11:38+00:00'
updated_at: '2020-08-28T16:40:54+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:40:54+00:00'
---

# Original Description
hi, can somebody tell me how to build xmrig for armv7 on centos x64 or ubuntu x64?  I had search in the issues and did not find it. thanks!


# Discussion History
## DocDrydenn | 2020-03-12T15:16:41+00:00
Start here: [https://github.com/xmrig/xmrig/wiki/Build](https://github.com/xmrig/xmrig/wiki/Build)

What you need to do is add the following:
- For ARMv7 - `cmake .. -DARM_TARGET=7`
- For ARMv8 - `cmake .. -DARM_TARGET=8`


This is what I made to help me. Maybe it will work for you too.
[https://github.com/DocDrydenn/xmrig-build](https://github.com/DocDrydenn/xmrig-build)

## xmrig | 2020-03-12T15:34:25+00:00
@DocDrydenn thanks for sharing the link, but author asking for cross build not sure if it even possible.

## DocDrydenn | 2020-03-12T15:56:59+00:00
Ah... You're right. I saw "ARMv7" and my brain immediately went to the `-DARM_TARGET` parameter.

So cross-compiling.... interesting...

# Action History
- Created by: esrrhs | 2020-03-07T09:11:38+00:00
- Closed at: 2020-08-28T16:40:54+00:00
