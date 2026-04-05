---
title: Linker error compiling on Windows (MSYS2)
source_url: https://github.com/xmrig/xmrig/issues/471
author: Detuner
assignees: []
labels: []
created_at: '2018-03-22T12:03:48+00:00'
updated_at: '2018-03-22T14:59:04+00:00'
type: issue
status: closed
closed_at: '2018-03-22T14:59:04+00:00'
---

# Original Description
I'm past quite a few errors trying to compile on mingw64, can't figure out how to solve this:
`
[ 15%] Linking CXX executable xmrig
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/7.3.0/../../../../x86_64-w64-mingw32/bin/ld.exe: cannot find -lrt
`

# Discussion History
## xmrig | 2018-03-22T12:11:15+00:00
Something wrong with your MSYS2 instalation, `rt` used only on Linux, you can remove `rt` from this line https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L140 but you likely get other errors.
Thank you.

## Detuner | 2018-03-22T14:58:49+00:00
All right, it compiles now, was totally my fault. It's the first time I tried compiling something using MSYS2 and cmake. I accidentally installed 'cmake' instead of 'mingw-w64-x86_64-cmake', then ignored cmake telling me it cannot recognize platform, and then tried messing around with CMakeLists.txt to get it working :)
Thanks a lot!



# Action History
- Created by: Detuner | 2018-03-22T12:03:48+00:00
- Closed at: 2018-03-22T14:59:04+00:00
