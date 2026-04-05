---
title: Question:NOT AN ISSUE  how to compile xmrig ?
source_url: https://github.com/xmrig/xmrig/issues/384
author: Gill1000
assignees: []
labels:
- question
created_at: '2018-02-04T09:49:56+00:00'
updated_at: '2018-03-14T22:48:20+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:48:20+00:00'
---

# Original Description
How to compile xmrig except visual studio or cmake ...I mean how to compile with other c++ compilers like code-blocks,dev-c++ or any other.!!

# Discussion History
## xmrig | 2018-02-04T14:01:25+00:00
Run `cmake -G` it will show all available generators, take look to
`CodeBlocks - Unix Makefiles`
`CodeBlocks - NMake Makefiles`

For me `CodeBlocks - Unix Makefiles` works fine with Qt Creator (MSYS2).
Thank you.

## Gill1000 | 2018-02-08T10:18:09+00:00
I checked that...but thats not what i was looking for..i mean in this we use cmake ..........I dont want to use this..is there another way like open code:block or any other except given above ......open codeblock and select the .cpp and .h files ..like this!!! @xmrig

## xmrig | 2018-02-08T10:31:40+00:00
It hard way, it possible, but you will do all cmake work by hand.
Thank you.

# Action History
- Created by: Gill1000 | 2018-02-04T09:49:56+00:00
- Closed at: 2018-03-14T22:48:20+00:00
