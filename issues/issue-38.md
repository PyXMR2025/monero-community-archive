---
title: msys2 compiling win 10 needs additional dll
source_url: https://github.com/xmrig/xmrig/issues/38
author: johndoetheanimal
assignees: []
labels: []
created_at: '2017-07-13T22:39:10+00:00'
updated_at: '2017-07-19T23:57:52+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:57:52+00:00'
---

# Original Description
Hi, 

i did the compiling as you suggested, but the exe file needs additional DLL files that are not static linked.
It's libwinpthread, libstdc++-6 and libgcc_seh

If I copy them to the Exe it will work, but not without copying them to the same folder.

# Discussion History
# Action History
- Created by: johndoetheanimal | 2017-07-13T22:39:10+00:00
- Closed at: 2017-07-19T23:57:52+00:00
