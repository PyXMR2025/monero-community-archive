---
title: Arm compiling v5.0.1
source_url: https://github.com/xmrig/xmrig/issues/1317
author: go140point6
assignees: []
labels: []
created_at: '2019-11-26T19:08:47+00:00'
updated_at: '2021-04-12T15:28:14+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:28:14+00:00'
---

# Original Description
This doesn't seem related to the bug that was just closed for arm compilation, but my Pi4 w/ latest Raspbian Buster was failing the build at 100% (Linking CXX executable xmrig) with lots of:

undefined reference to `__atomic_load_8'

I seemed to "fix" this issue by inserting the following on line 210 of CMakeLists.txt:

set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")

Once in place, I was able to follow the normal build instructions and get a working binary for my Pi.  Don't know if this issue is just something with my setup, but maybe it will help others if experienced.

# Discussion History
# Action History
- Created by: go140point6 | 2019-11-26T19:08:47+00:00
- Closed at: 2021-04-12T15:28:14+00:00
