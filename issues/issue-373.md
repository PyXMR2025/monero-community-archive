---
title: build xmrig step by step
source_url: https://github.com/xmrig/xmrig/issues/373
author: omarraom
assignees: []
labels: []
created_at: '2018-01-29T08:12:11+00:00'
updated_at: '2018-11-05T07:10:41+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:10:41+00:00'
---

# Original Description
Hello can any one help me by explain how to build xmrig miner step by step with all the programme need it to install once for all

# Discussion History
## Gill1000 | 2018-01-29T14:05:24+00:00
https://github.com/xmrig/xmrig/wiki/Build
Here bro..everything is step by step and simple .. @omarraom

## Zelecktor | 2018-02-12T13:33:36+00:00
Watch some videos about how to install cmake, thats the difficult part if you ussing windows (add it on path and defining commandline on cmd). Visual basics is very easy to use, dont need tutorial for that. Your result: an .exe file

On linux is more easy. Just sudo install libraries and dependencies, cmake and compile (make). Thats 100% much easier and faster than windows.
Your result: an executable file no extension called "xmrig", just do this command `./xmrig` to run it. (you need to be on the same directory of the file)

All tutorials are on the wiki https://github.com/xmrig/xmrig/wiki/Build

Note: if you using Linux debian 9.2, use the same build as ubuntu. if you are using linux debian 7-8 see #248 

# Action History
- Created by: omarraom | 2018-01-29T08:12:11+00:00
- Closed at: 2018-11-05T07:10:41+00:00
