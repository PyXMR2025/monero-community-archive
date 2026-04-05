---
title: Cannot open source file uv.h
source_url: https://github.com/xmrig/xmrig/issues/148
author: Ala360
assignees: []
labels:
- libuv
created_at: '2017-10-10T14:06:54+00:00'
updated_at: '2017-10-22T05:19:41+00:00'
type: issue
status: closed
closed_at: '2017-10-22T05:19:41+00:00'
---

# Original Description
Hi,
when I try to debug I get these errors:

>     cannot open source file "uv.h"
> 
>     Cannot open include file: 'microhttpd.h': No such file or directory

I'm using Visual Studio 2017 15

How i can solve them? thank you!



# Discussion History
## Ala360 | 2017-10-13T10:58:52+00:00
No one didn't bother himself to even reply!!

## AlexanderKozhevin | 2017-10-21T22:49:57+00:00
I have the same problem :) 
It happens when you try to compile application without CMake stuff.

## xmrig | 2017-10-22T05:19:33+00:00
https://github.com/xmrig/xmrig/wiki/Windows-Build You can download prebuilt library's or build it byself.

# Action History
- Created by: Ala360 | 2017-10-10T14:06:54+00:00
- Closed at: 2017-10-22T05:19:41+00:00
